import requests
import pytest


@pytest.mark.usefixtures("api_setup")
class TestAPI:
    def test_minPrice(self):
        min_price = 1000000
        query = {'minPrice': min_price}
        response = requests.get(url="https://skillacademy.com/skillacademy/discovery/search", params=query)

        results = response.json()['data']['data']

        price_list = []

        for result in results:
            for key, value in result.items():
                if key == "basePrice":
                    price_list.append(value)

        for i in price_list: assert i >= min_price

    def test_searchQuery(self):
        search_query = 'Tokopedia'
        query = {'searchQuery': search_query}
        response = requests.get(url="https://skillacademy.com/skillacademy/discovery/search", params=query)

        results = response.json()['data']['data']

        course_description = []

        for result in results:
            for key, value in result.items():
                if key == "courseDescription":
                    course_description.append(value)

        for i in course_description: assert search_query in i

    def test_maxPrice(self):
        max_price = 1000000
        query = {'maxPrice': max_price}
        response = requests.get(url="https://skillacademy.com/skillacademy/discovery/search", params=query)

        results = response.json()['data']['data']

        price_list = []

        for result in results:
            for key, value in result.items():
                if key == "basePrice":
                    price_list.append(value)

        for i in price_list: assert i <= max_price

    def test_sortBy(self):
        sort_by = 'price'
        query = {'sortBy': sort_by}
        response = requests.get(url="https://skillacademy.com/skillacademy/discovery/search", params=query)

        results = response.json()['data']['data']

        price_list = []

        for result in results:
            for key, value in result.items():
                if key == "basePrice":
                    price_list.append(value)

        for i in range(len(price_list) - 1):
            assert int(price_list[i]) >= int(price_list[i + 1])
