from django.http import Http404
from rest_framework.viewsets import GenericViewSet

from .serializers import TelegramBotModelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .bot_interactor import process_update, set_webhook, remove_webhook
from .permissions import IsTheOwnerOf
from .models import TelegramBotModel

import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


class TelegramBotViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         GenericViewSet):

    queryset = TelegramBotModel.objects
    permission_classes = [IsAuthenticated, IsTheOwnerOf]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return self.queryset.none()
        return self.queryset.filter(owner=self.request.user)

    serializer_class = TelegramBotModelSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if self.get_queryset().count() > 4:
                return Response({"error": "Limit of 5 bots per user is reached"},
                                status=status.HTTP_403_FORBIDDEN)

            token = serializer.validated_data["token"]
            telegram_response = set_webhook(token)
            if not telegram_response["ok"]:
                return Response(telegram_response["description"], status=status.HTTP_400_BAD_REQUEST)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            remove_webhook(instance.token)
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def bot_action(request, bot_token):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        process_update(request.body.decode(), bot_token)
        return Response(status=status.HTTP_200_OK)
