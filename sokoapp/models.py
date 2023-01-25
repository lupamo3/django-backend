from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=255)
    currencies = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    timezones = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='employees')
    region = models.CharField(max_length=255)
    company = models.CharField(max_length=255, default='Soko')
    job_title = models.CharField(max_length=255, default='Software Engineer')

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_age(self):
        import datetime
        today = datetime.date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    def get_country(self):
        return self.country.name
