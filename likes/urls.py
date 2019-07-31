from rest_framework import routers
from .api import LikeViewSet

router =routers.DefaultRouter()
router.register('api/likes', LikeViewSet, 'likes')

urlpatterns = router.urls
