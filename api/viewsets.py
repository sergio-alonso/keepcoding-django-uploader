from rest_framework import viewsets

from api.models import Image
from api.serializers import ImageSerializer

class UploadViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
