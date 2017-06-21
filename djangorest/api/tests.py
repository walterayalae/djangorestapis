from django.test import TestCase
from .models import Bucketlist
from rest_framework import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.

class ModelTestCase(TestCase):

    def setUp(self):
        # Define the test client and other test variables
        self.bucketlist_name = "Write code"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

    def test_model_can_create_a_bucketlist(self):
        # Test if bucketlist can be creted
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):

    def setUp(self):

        self.client = APIClient()
        self.bucketlist_data = {'name' : 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create')
            self.bucketlist_data,
            format = 'json')

    def test_api_can_create_a_bucketlist(self):

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

        
