from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Artisan
from .serializers import ArtisanSerializer

class ArtisanTestCase(APITestCase):

    def setUp(self):
        self.country = 'kenya'
        self.first_name = 'Norbert'
        self.last_name = 'Anjichi'
        self.date_of_birth = '1993-01-27'
        self.holiday_allowance = 12
        self.marital_status = 'Married'
        self.id_number = "29663036"
        self.working_hours = 0
        self.number_of_children = 0
        self.religion = ''
        self.artisan = Artisan.objects.create(
            country=self.country,
            first_name=self.first_name,
            last_name=self.last_name,
            date_of_birth=self.date_of_birth,
            holiday_allowance=self.holiday_allowance,
            marital_status=self.marital_status,
            id_number=self.id_number,
            working_hours=self.working_hours,
            number_of_children=self.number_of_children,
            religion=self.religion
        )

    def test_get_all_artisans(self):
        # get API response
        url = reverse('artisan-list')
        response = self.client.get(url)
        # get data from db
        artisans = Artisan.objects.all()
        serializer = ArtisanSerializer(artisans, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_artisan(self):
        url = reverse('artisan-list')
        data = {
            'country': self.country,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth,
            'holiday_allowance': self.holiday_allowance,
            'marital_status': self.marital_status,
            'id_number': self.id_number,
            'working_hours': self.working_hours,
            'number_of_children': self.number_of_children,
            'religion': self.religion,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artisan.objects.count(), 2)
        self.assertEqual(Artisan.objects.get(pk=2).first_name, self.first_name)


from rest_framework.test import APITestCase
from rest_framework import status

class EmployeeViewSetTestCase(APITestCase):
    def setUp(self):
        self.valid_employee_data = {
            'first_name': 'Norbert',
            'last_name': 'Anjichi',
            'date_of_birth': '1993-01-27',
            'job_title': 'Software Engineer',
            'company': 'Soko',
            'country': 'KE',
            'region': 'Africa'
        }
        self.invalid_employee_data = {
            'first_name': '',
            'last_name': 'Doe',
            'date_of_birth': '2000-01-01',
            'job_title': 'Software Engineer',
            'company': 'Soko',
            'country': 'KE',
            'region': 'Africa'
        }

    def test_create_employee_with_valid_data(self):
        response = self.client.post('/employees/', self.valid_employee_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_employee_with_invalid_data(self):
        response = self.client.post('/employees/', self.invalid_employee_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_employees(self):
        response = self.client.get('/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
