from rest_framework import serializers
from .models import TelegramBotModel

class TelegramBotModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramBotModel
        fields = ["id", "name", "token"]
