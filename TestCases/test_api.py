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

    def test_sortBy_orderBy(self):
        sort_by = 'price'
        order_by = 'DESC'
        query = {'sortBy': sort_by, 'orderBy': order_by}
        response = requests.get(url="https://skillacademy.com/skillacademy/discovery/search", params=query)

        results = response.json()['data']['data']

        price_list = []

        for result in results:
            for key, value in result.items():
                if key == "basePrice":
                    price_list.append(value)

        for i in range(len(price_list) - 1):
            assert int(price_list[i]) >= int(price_list[i + 1])

    def test_page_size_page(self):
        page = 2
        page_size = 10
        query = {'page': page, "pageSize": page_size}
        response = requests.get(url="https://skillacademy.com/skillacademy/discovery/search", params=query)

        pagejson = response.json()['data']['page']
        pagesizejson = response.json()['data']['pageSize']
        totalpagejson = response.json()['data']['pageSize']
        results = response.json()['data']['data']

        print(f"pagejson: {response.json()['data']['page']}")
        print(f"pagesizejson: {response.json()['data']['pageSize']}")
        print(f"totalpagesizejson: {response.json()['data']['totalPage']}")
        print(f"result length size: {len(results)}")

        assert pagejson == page
        assert pagesizejson == page_size