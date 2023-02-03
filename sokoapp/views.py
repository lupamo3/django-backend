import requests
import json
import logging

from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Artisan, Employee
from .serializers import ArtisanSerializer, EmployeeSerializer

logger = logging.getLogger('django_rest_framework')


def get_country_details(country_code):
    REST_COUNTRIES_API_URL = 'https://restcountries.com/v3.1/alpha/'
    url = REST_COUNTRIES_API_URL + country_code
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


class EmployeeViewSet(viewsets.ViewSet):
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        try:
            country_code = request.data['country']
            response = get_country_details(country_code) 
            country_info = response[0]
            region = country_info.get('region', None)
            date_of_birth = request.data['date_of_birth']
            date_of_birth = date_of_birth.replace("-", "")
            if region in ["Middle East", "Africa"]:
                identifier = f"{request.data['first_name']}{request.data['last_name']}{request.data['date_of_birth']}"

            currency = country_info['currencies']
            currency_list = list(currency.values())[0]
            currency_code =  currency_list['name']   
            country_name = country_info['name']['common']

            language = country_info['languages']
            languages = [value for key, value in language.items()]
            languages = ', '.join(languages)
            timezones = country_info['timezones']
            timezones = ''.join(timezones)

            serializer = self.serializer_class(data={**request.data, 'country_name': country_name, 'country_currency': currency_code, 'country_language': languages, 'country_timezone': timezones, 'region': identifier})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info(status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

            
        except Exception as e:
            logger.error(e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)      


    def list(self, request):
        # with open("/Users/lj22/Code/python/django/djangosoko/sokoapp/employee.json", "r") as f:
        #     json_data = json.load(f)
        # return Response(json_data)
        try:
            queryset = Employee.objects.all()
            serializer = self.serializer_class(queryset, many=True)
            logger.info(status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ArtisanViewSet(viewsets.ViewSet):
    artisan_serializer = ArtisanSerializer
    queryset = Artisan.objects.all()


    def get(self, request):
        try:
            serializer = self.artisan_serializer(self.queryset, many=True)
            logger.info(status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        print("request", request.data)
        try:
            serializer = self.artisan_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info(status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    



