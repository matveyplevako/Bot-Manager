from .views import TelegramBotViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('telegram-bot', TelegramBotViewSet, basename='user')
urlpatterns = router.urls
