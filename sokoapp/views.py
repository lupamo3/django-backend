from rest_framework import viewsets
from rest_framework.response import Response

from .services import CountryService
from .models import Country, Employee
from .serializers import CountrySerializer, EmployeeSerializer

class EmployeeViewSet(viewsets.ViewSet):
    serializer_class = EmployeeSerializer
    country_service = CountryService()

    def list(self, request):
        employees = Employee.objects.all()
        serializer = self.serializer_class(employees, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        employee = Employee.objects.get(pk=pk)
        country_details = self.country_service.get_country_details(employee.country_code)
        if country_details is None:
            return Response({'error': 'Country details not found'}, status=404)

        serializer = self.serializer_class(employee)
        employee_data = serializer.data
        employee_data.update({
            'country_name': country_details['name'],
            'currency': country_details['currencies'][0]['code'],
            'languages': [language['name'] for language in country_details['languages']],
            'timezones': country_details['timezones']
        })

        if employee.region in ('Middle East', 'Africa'):
            employee_data['identifier'] = f"{employee.first_name}{employee.last_name}{employee.date_of_birth}"
        return Response(employee_data)

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer



