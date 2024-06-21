import requests


class ApiTest:

    def __init__(self, url, token="63c16381-4ce8-4885-9d54-4cbac66bf8bd"):
        self.url = url
        self.token = token

    def get_film_by_id(self, id: int):
        my_headers = {
            "X-API-KEY": self.token
        }
        resp = requests.get(self.url+f'/api/v2.2/films/{id}', headers=my_headers)
        return resp.json()

    def get_collection_list(self, collection: str):
        my_headers = {
            "X-API-KEY": self.token
        }
        my_params = {
            "type": collection
        }
        resp = requests.get(self.url+'/api/v2.2/films/collections', headers=my_headers, params=my_params)
        return resp.json()

    def get_list_of_content_by_params(self, order, type, rating_from, rating_to, year_from, year_to):
        my_headers = {
            "X-API-KEY": self.token
        }
        my_params = {
            "order": order,
            "type": type,
            "ratingFrom": rating_from,
            "ratingTo": rating_to,
            "yearFrom": year_from,
            "yearTo": year_to,
        }
        resp = requests.get(self.url+'/api/v2.2/films', headers=my_headers, params=my_params)
        return resp.json()

    def get_staff_by_film_id(self, id):
        my_headers = {
            "X-API-KEY": self.token
        }
        my_params = {
            "filmId": id
        }
        resp = requests.get(self.url+'/api/v1/staff', headers=my_headers, params=my_params)
        return resp.json()

    def get_actor_info(self, id):
        my_headers = {
            "X-API-KEY": self.token
        }
        resp = requests.get(self.url+f'/api/v1/staff/{id}', headers=my_headers)
        return resp.json()
