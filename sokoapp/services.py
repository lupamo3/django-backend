import requests


class CountryService:
    REST_COUNTRIES_API_URL = 'https://restcountries.com/v2/alpha/'

    def get_country_details(self, country_code):
        url = self.REST_COUNTRIES_API_URL + country_code
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None