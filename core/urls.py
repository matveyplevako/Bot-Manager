from .views import TelegramBotViewSet, bot_action
from rest_framework.routers import DefaultRouter
from django.urls import path


router = DefaultRouter()
router.register('telegram-bot', TelegramBotViewSet, basename='telegram-bot')

urlpatterns = router.urls
urlpatterns += [path('bot/<bot_token>', bot_action)]
