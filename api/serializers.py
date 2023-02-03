from rest_framework import serializers


class EncodeJsonSerializer(serializers.Serializer):
    url = serializers.URLField(required=True, max_length=500)


class DecodeJsonSerializer(serializers.Serializer):
    short_url = serializers.URLField(required=True, max_length=500)
