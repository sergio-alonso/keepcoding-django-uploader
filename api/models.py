from django.db import models
from django.conf import settings


class Image(models.Model):
    file = models.FileField(upload_to=settings.MEDIA_ROOT)
