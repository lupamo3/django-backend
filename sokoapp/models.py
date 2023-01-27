from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=255)
    currencies = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    timezones = models.CharField(max_length=255)
    country_code = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.name
        

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    job_title = models.CharField(max_length=255, default='Software Engineer')
    company = models.CharField(max_length=255, default='Soko')
    country = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255, blank=True)
    country_currency = models.CharField(max_length=255, blank=True)
    country_language = models.CharField(max_length=255, blank=True)
    country_timezone = models.CharField(max_length=255, blank=True)
    employee_identifier = models.CharField(max_length=255, blank=True)
    region = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_age(self):
        import datetime
        today = datetime.date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    def get_country(self):
        return self.country.name

class Artisan(models.Model):
    country = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    holiday_allowance = models.IntegerField()
    marital_status = models.CharField(max_length=20, choices=(('Single', 'Single'), ('Married', 'Married')), default='S')
    id_number = models.IntegerField()
    working_hours = models.IntegerField()
    number_of_children = models.IntegerField(default=0)
    religion = models.CharField(max_length=20, choices=(('Christian', 'Christian'), ('Muslim', 'Muslim')), default='C')

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_age(self):
        import datetime
        today = datetime.date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))