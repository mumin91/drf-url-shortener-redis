from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from the_shortest_url.settings import BASE_URL
from url_shortener.serializers import EncodeDecodeSerializer
from utils.helpers import get_short_url_code
from utils.redis import redis_object


class EncodeView(APIView):

    def post(self, request: Request) -> Response:
        # Valid serialization
        serializer = EncodeDecodeSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Get short URL code
        short_url_code = get_short_url_code(request.data.get('url'))

        # Build response
        data = {"short_url": f"{BASE_URL}{short_url_code}"}

        # If found in DB
        if redis_object.get(short_url_code):
            return Response(data, status=status.HTTP_200_OK)

        # Store the key-value to redis
        redis_object.set(short_url_code, request.data.get('url'))

        return Response(data, status=status.HTTP_200_OK)


class DecodeView(APIView):

    def post(self, request: Request) -> Response:
        # Valid serialization
        serializer = EncodeDecodeSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Get short URL
        url = request.data.get('url')
        short_url = url.rsplit('/', 1)[1]

        # Store the key-value to redis
        if long_url := redis_object.get(short_url):
            # Build response
            data = {"long_url": long_url}
            return Response(data, status=status.HTTP_200_OK)

        # Not found response
        return Response("URL not found", status.HTTP_404_NOT_FOUND)
