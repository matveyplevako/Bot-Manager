from django.db import models
from django.contrib.auth.models import User


class TelegramBotModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    token = models.CharField(max_length=46, unique=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
