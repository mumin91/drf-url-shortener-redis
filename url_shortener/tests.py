from django.urls import reverse
from rest_framework import status
from rest_framework.test import APISimpleTestCase, APIClient


class EncodeTestCase(APISimpleTestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.url = reverse('encode')

        self.long_url = "https://medium.com/analytics-vidhya/redis-sorted-sets-explained-2d8b6302525"
        self.request_body = {"url": self.long_url}
        self.short_url_code = "eKv0a96"

    def test_decode_serializer_error(self) -> None:
        """Test wrong key error"""
        response = self.client.post(
            self.url, {"aaaa": "sldfkj"}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
            "url": [
                "This field is required."
            ]
        })


class DecodeTestCase(APISimpleTestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.url = reverse('encode')

        self.long_url = "https://medium.com/analytics-vidhya/redis-sorted-sets-explained-2d8b6302525"
        self.request_body = {"url": self.long_url}
        self.short_url_code = "eKv0a96"

    def test_decode_serializer_error(self) -> None:
        """Test wrong key error"""
        response = self.client.post(
            self.url, {"aaaa": "sldfkj"}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
            "url": [
                "This field is required."
            ]
        })

        response = self.client.post(
            self.url, {"url": ""}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
            "url": [
                "This field may not be blank."
            ]
        })
