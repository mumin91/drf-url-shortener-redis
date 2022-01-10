from rest_framework import serializers


class EncodeDecodeSerializer(serializers.Serializer):

    url = serializers.URLField(max_length=2000)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

