from django.db import models
from django.contrib.auth.models import User
from time import timezone


class TelegramBotModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    token = models.CharField(max_length=46)
    created = models.DateTimeField(auto_now_add=True, editable=False)
