from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import TelegramBotModel
from .validators import token_validator


class TelegramBotModelSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=46, validators=[token_validator,
                                                             UniqueValidator(queryset=TelegramBotModel.objects.all())])

    class Meta:
        model = TelegramBotModel
        fields = ["id", "name", "token"]
