from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('likes.urls'))
]
