import json
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status

from django.core.urlresolvers import reverse

from api.models import Image


class ImageTests(APITestCase):

    def tearDown(self):
        Image.objects.all().delete()

    def create_test_file(self, path):
        test_file = open(path, 'w')
        test_file.write('test_file\n')
        test_file.close()
        test_file = open(path, 'rb')
        return test_file

    def test_user_can_upload_a_file(self):
        url = '/api/v1/upload/'
        data = {'file':self.create_test_file('/tmp/test_upload')}

        client = APIClient()
        response = client.post(url, data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertIn('id', response.data)
