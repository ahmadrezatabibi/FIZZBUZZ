from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Fizzbuzz

class FizzbuzzTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.list_create_url = reverse('fizzbuzz-list-create')
        cls.first_fizzbuzz = Fizzbuzz.objects.create(useragent='TestAgent', message='First message')
        cls.second_fizzbuzz = Fizzbuzz.objects.create(useragent='TestAgent', message='Second message')

    def test_list_fizzbuzz(self):
        """
        Ensure we can retrieve a list of fizzbuzz items.
        """
        response = self.client.get(self.list_create_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) 

    def test_create_fizzbuzz(self):
        """
        Ensure we can create a new fizzbuzz item.
        """
        data = {'useragent': 'TestAgent', 'message': 'A new message'}
        response = self.client.post(self.list_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Fizzbuzz.objects.count(), 3)
        self.assertEqual(Fizzbuzz.objects.latest('fizzbuzz_id').message, 'A new message')

    def test_get_valid_fizzbuzz(self):
        """
        Ensure we can retrieve a valid fizzbuzz item.
        """
        detail_url = reverse('fizzbuzz-detail', kwargs={'id': self.first_fizzbuzz.fizzbuzz_id})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], self.first_fizzbuzz.message)

    def test_get_invalid_fizzbuzz(self):
        """
        Ensure that an invalid fizzbuzz item returns a 404.
        """
        detail_url = reverse('fizzbuzz-detail', kwargs={'id': 999})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_fizzbuzz_not_allowed(self):
        """
        Ensure DELETE requests to the fizzbuzz_detail API are not allowed.
        """
        detail_url = reverse('fizzbuzz-detail', kwargs={'id': self.first_fizzbuzz.fizzbuzz_id})
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_fizzbuzz_not_allowed(self):
        """
        Ensure PUT requests to the fizzbuzz_detail API are not allowed.
        """
        detail_url = reverse('fizzbuzz-detail', kwargs={'id': self.first_fizzbuzz.fizzbuzz_id})
        data = {'useragent': 'TestAgent', 'message': 'Updated message'}
        response = self.client.put(detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

