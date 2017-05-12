from django.test import TestCase

from api.models import Image


class ImageModelTest(TestCase):

    def test_default_values(self):
        image = Image()
        self.assertEqual(image.file, '')
