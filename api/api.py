from rest_framework import routers
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from api.viewsets import UploadViewSet

router = routers.DefaultRouter()
router.register('api/v1/upload', UploadViewSet)
