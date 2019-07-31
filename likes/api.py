from likes.models import Like
from rest_framework import viewsets, permissions
from .serializers import LikeSerializer

class LikeViewSet(viewsets.ModelViewSet):
  queryset = Like.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = LikeSerializer
