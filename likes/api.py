from likes.models import Like
from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import LikeSerializer

class LikeViewSet(viewsets.ViewSet):

  def list(self, request):
    queryset = Like.objects.all()
    serializer = LikeSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, pk=Like.slug):
    queryset = Like.objects.all()
    like = get_object_or_404(queryset, slug=pk)
    serializer = LikeSerializer(like)
    print(like)
    return Response(serializer.data)

# class LikeViewSet(viewsets.ModelViewSet):
#   queryset = Like.objects.all()
#   permission_classes = [
#     permissions.AllowAny
#   ]
#   serializer_class = LikeSerializer
