from rest_framework import serializers
from .models import Country, Employee, Artisan

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        date_of_birth = serializers.DateTimeField(
        required=False, allow_null=True,
        format="%Y-%m-%d", 
        input_formats=["%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"]
    )
        fields = '__all__'


class ArtisanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artisan
        date_of_birth = serializers.DateTimeField(
        required=False, allow_null=True,
        format="%Y-%m-%d", 
        input_formats=["%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"]
    )
        fields = '__all__'
