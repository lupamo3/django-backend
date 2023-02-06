# MRP Backend

### This is a Django application that implements an endpoint to retrieve a list of employees and artisans with country specific information added to each employee. The country specific information includes the full name of the country, currency used in the country, language/s of the country, and timezone/s for the country. Additionally, employees in Middle East and Africa regions have an additional identifier which takes the form of {firstName}{lastName}{dateOfBirth}.

### Installation

```
Clone the repository:
git clone https://github.com/lupamo3/django-backend
Install the dependencies:
pip install -r requirements.txt
Run the migrations:
python manage.py makemigrations
python manage.py migrate
Run the development server:
python manage.py runserver
python manage.py tests
```

### Usage

```
The endpoint to retrieve the list of employees is /employees/. To retrieve the employees, you can use a tool such as Postman to make a GET request to the endpoint.

The application also includes a viewset for countries, which can be accessed at the endpoint /countries/.
```

###  Models

The application includes three models: Artisan, Country and Employee. The Country model contains fields for the country's code, name, currency, languages, and timezones. The Employee model contains fields for the employee's first name, last name, date of birth, and country code.

### Services

The application includes a service called CountryService which retrieves country details from the Rest Countries API using the country code of the employee. This service is called in the views to retrieve the country specific information for each employee.

### Views

```
The application includes views that handle the logic for retrieving the employees from the database, and then retrieving the country details from the service and adding them to the employee object. The views use Django Rest Framework viewsets to handle the requests.

The EmployeeViewSet retrieves the employee data from the Employee model, then uses the country code to retrieve the country's details from the Rest Countries API, and then adds the country specific information to the employee object and returns it as a response.

The CountryViewSet retrieves the countries data from the Country model and returns it as a response.
```

### Tests

```
This tests verify that the API endpoint for creating and updating employees, artisans and countries is working correctly, and that the API endpoints for listing employees, artisans and countries is returning the correct response.
```
### CI/CD
```
Github Actions Continuous Integration and Development has been set up in the application. 
```
### Black
```
Used black for code formatting. 
```
### Pagination
```
Pagination implemented using PageNumberPagination
```

### Assumptions

The Country model is assumed that there is a need to store the timezone and languages as a list of strings,
The Employee model is assumed that there is a need to store the date of birth as a date field
Requests library is used to fetch the data from restcountries API
The EmployeeViewSet is assumed that the Middle East and Africa regions are not fixed and will be updated in future.
The CountryViewSet is assumed that the endpoint for listing countries is not restricted.

### Conclusion

This application demonstrates how to use Django and Django REST framework to create an endpoint that retrieves a list of employees with country specific information added to each employee. It also shows how to use services to retrieve data from external APIs. 