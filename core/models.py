from django.db import models
from django.contrib.auth.models import User


class TelegramBotModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)  # as it is not specified that user must enter name
    token = models.CharField(max_length=46, unique=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
