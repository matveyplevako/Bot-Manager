from rest_framework import serializers


def token_validator(token):
    if len(token) != 46:
        raise serializers.ValidationError('Token must be 46 characters long.')
