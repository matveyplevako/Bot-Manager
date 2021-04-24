from .serializers import TelegramBotModelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from rest_framework.response import Response

from .permissions import IsTheOwnerOf
from .models import TelegramBotModel


class TelegramBotViewSet(viewsets.ModelViewSet):
    queryset = TelegramBotModel.objects
    permission_classes = [IsAuthenticated, IsTheOwnerOf]

    def get_queryset(self):
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
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
