import requests
import json
import logging

from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Artisan, Employee
from .serializers import ArtisanSerializer, EmployeeSerializer

logger = logging.getLogger("django_rest_framework")


country_info_cache = {}


def get_country_details(country_code):
    if country_code in country_info_cache:
        return country_info_cache[country_code]

    REST_COUNTRIES_API_URL = "https://restcountries.com/v3.1/alpha/"
    url = REST_COUNTRIES_API_URL + country_code
    response = requests.get(url)
    if response.status_code != 200:
        return None
    country_info = response.json()
    country_info_cache[country_code] = country_info
    return country_info


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class EmployeeViewSet(viewsets.ViewSet):
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        try:
            country_code = request.data["country"]
            response = get_country_details(country_code)
            country_info = response[0]
            region = country_info.get("region", None)
            date_of_birth = request.data["date_of_birth"]
            date_of_birth = date_of_birth.replace("-", "")
            if region in ["Middle East", "Africa"]:
                identifier = f"{request.data['first_name']}{request.data['last_name']}{date_of_birth}"

            currency = country_info["currencies"]
            currency_list = list(currency.values())[0]
            currency_code = currency_list["name"]
            country_name = country_info["name"]["common"]

            language = country_info["languages"]
            languages = [value for key, value in language.items()]
            languages = ", ".join(languages)
            timezones = country_info["timezones"]
            timezones = "".join(timezones)

            serializer = self.serializer_class(
                data={
                    **request.data,
                    "country_name": country_name,
                    "country_currency": currency_code,
                    "country_language": languages,
                    "country_timezone": timezones,
                    "employee_identifier": identifier,
                    "region": region,
                }
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info(status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            logger.error(e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        try:
            queryset = Employee.objects.all()
            serializer = self.serializer_class(queryset, many=True)
            logger.info(status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            employee = Employee.objects.get(pk=pk)
            employee.delete()
            logger.info(status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ExistingEmployeesViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            with open(
                "/Users/lj22/Code/python/django/djangosoko/sokoapp/employee.json", "r"
            ) as f:
                json_data = json.load(f)
            employee_data = []
            for person in json_data:
                first_name = person["firstName"]
                last_name = person["lastName"]
                dob = person["dateOfBirth"]
                job_title = person["jobTitle"]
                company = person["company"]
                country = person["country"]
                response = get_country_details(country)
                country_info = response[0]
                region = country_info.get("region", None)

                date_of_birth = dob.replace("/", "")
                if region in ["Middle East", "Africa"]:
                    identifier = f"{first_name}{last_name}{date_of_birth}"
                else:
                    identifier = region

                currency = country_info["currencies"]
                currency_list = list(currency.values())[0]
                currency_code = currency_list["name"]
                country_name = country_info["name"]["common"]

                language = country_info["languages"]
                languages = [value for key, value in language.items()]
                languages = ", ".join(languages)
                timezones = country_info["timezones"]
                timezones = "".join(timezones)

                employee_data.append(
                    {
                        "first_name": first_name,
                        "last_name": last_name,
                        "dob": date_of_birth,
                        "job_title": job_title,
                        "company": company,
                        "country": country,
                        "country_name": country_name,
                        "country_currency": currency_code,
                        "country_language": languages,
                        "country_timezone": timezones,
                        "employee_identifier": identifier,
                    }
                )
            logger.info(status.HTTP_200_OK)
            return Response(employee_data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ArtisanViewSet(viewsets.ViewSet):
    artisan_serializer = ArtisanSerializer
    queryset = Artisan.objects.all()
    pagination_class = CustomPagination

    def get(self, request):
        try:
            serializer = self.artisan_serializer(self.queryset, many=True)
            logger.info(status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = self.artisan_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info(status.HTTP_201_CREATED)
            print(status.HTTP_201_CREATED, "serializer ")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
