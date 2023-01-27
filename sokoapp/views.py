import requests
import json

from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Artisan, Employee
from .serializers import ArtisanSerializer, EmployeeSerializer


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
            return Response(serializer.data, status=status.HTTP_201_CREATED)

            
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)      


    def list(self, request):
        # with open("/Users/lj22/Code/python/django/djangosoko/sokoapp/employee.json", "r") as f:
        #     json_data = json.load(f)
        # return Response(json_data)
        queryset = Employee.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

   
    # def retrieve(self, request, pk=1):
    #     # employee = Employee.objects.get(pk=pk)
    #     # country_details = self.country_service.get_country_details(employee.country_code)
    #     # if country_details is None:
    #         # return Response({'error': 'Country details not found'}, status=404)

    #     # serializer = self.serializer_class(employee)
    #     # employee_data = serializer.data
    #     # employee_data.update({
    #     #     'country_name': country_details['name'],
    #     #     'currency': country_details['currencies'][0]['code'],
    #     #     'languages': [language['name'] for language in country_details['languages']],
    #     #     'timezones': country_details['timezones']
    #     # })
    #     response = requests.get(url)
    #     country_info = json.loads(response.text)[0]
    #     print("show res", country_info)
    #     serializer = self.serializer_class(employee)
    #     # employee_data = serializer.data
    #     employee_data = employee
    #     currency = country_info['currencies']
    #     currency_list = list(currency.values())[0]
    #     currency_code =  currency_list['name']   
    #     languages = country_info['languages']

    #     employee_data.update({
    #         'country_name': country_info['name'],
    #         'currency': currency_code,
    #         'languages': [value for key, value in languages.items()],
    #         'timezones': country_info['timezones']
    #     })        

    #     if employee.region in ["Middle East", "Africa"]:
    #         identifier = f"{employee.first_name}{employee.last_name}{employee.date_of_birth.strftime('%d%m%Y')}"
    #         employee.identifier = identifier
    #         employee.save()

    #     serializer = self.get_serializer(employee)
    #     return JsonResponse(serializer.data)

class ArtisanViewSet(viewsets.ViewSet):
    artisan_serializer = ArtisanSerializer

    def get(self, request):
        queryset = Artisan.objects.all()
        serializer = self.artisan_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.artisan_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    



