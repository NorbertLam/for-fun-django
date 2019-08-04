from likes.models import Like
from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import LikeSerializer


class LikeViewSet(viewsets.ModelViewSet):
  queryset = Like.objects.all()
  lookup_field = 'slug'
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = LikeSerializer
