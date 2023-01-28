from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Artisan

class ArtisanAPITestCase(APITestCase):
    def setUp(self):
        self.artisan_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1980-01-01',
            'country': 'kenya',
            'holiday_allowance': 21,
            'marital_status': 'Single',
            'id_number': 29663036,
            'working_hours': 0,
            'number_of_children': 0,
            'religion': 'Christian'
        }
        self.artisan = Artisan.objects.create(**self.artisan_data)
    
    def test_create_artisan(self):
        url = reverse('artisan')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1980-01-01',
            'country': 'kenya',
            'holiday_allowance': 21,
            'marital_status': 'Single',
            'id_number': 29663036,
            'working_hours': 0,
            'number_of_children': 0,
            'religion': 'Christian'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artisan.objects.count(), 2)
        self.assertEqual(Artisan.objects.get(pk=2).first_name, 'Jane')
    
    def test_list_artisans(self):
        url = reverse('artisan')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['first_name'], 'John')
    
    def test_update_artisan(self):
        url = reverse('artisans-detail', args=[self.artisan.pk])
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'date_of_birth': '1980-01-01',
            'country': 'kenya',
            'holiday_allowance': 21,
            'marital_status': 'Single',
            'id_number': 29663036,
            'working_hours': 0,
            'number_of_children': 0,
            'religion': 'Christian'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Artisan.objects.get(pk=1).first_name, 'John Doe')
        self.assertEqual(Artisan.objects.get(pk=1).holiday_allowance, 25)
    
    def test_delete_artisan(self):
        url = reverse('artisans-detail', args=[self.artisan.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Artisan.objects.count(), 0)
