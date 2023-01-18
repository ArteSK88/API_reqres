import json

import requests


class ReqRes:
    def __init__(self):
        self.url = "https://reqres.in/api"


    def get_resource_list(self, page: int, per_page: int) -> json:
        uri = f'{self.url}/' + '{resource}'
        params = {'page': page, 'per_page': per_page}
        response = requests.get(url=uri, params=params)
        return response.status_code, response.json()

    def get_user_list(self, page: int, per_page: int) -> json:
        uri = f'{self.url}/users'
        params = {'page': page, 'per_page': per_page}
        response = requests.get(url=uri, params=params)
        return response.status_code, response.json()

    def get_a_user(self, user_id: int) -> json:
        uri = f'{self.url}/users'
        params = {'id': user_id}
        response = requests.get(url=uri, params=params)
        return response.status_code, response.json()

    def update_a_user(self, user_id: int) -> json:
        uri = f'{self.url}/users/{user_id}'
        response = requests.put(url=uri)
        return response.status_code, response.json()

    def patch_a_user(self, user_id: int) -> json:
        uri = f'{self.url}/users/{user_id}'
        response = requests.patch(url=uri)
        return response.status_code, response.json()

    def delete_a_user(self, user_id: int) -> json:
        uri = f'{self.url}/users/{user_id}'
        response = requests.delete(url=uri)
        return response.status_code

    def get_unknown_resource(self, resource_id: int) -> json:
        uri = f'{self.url}/' + '{resource}'
        params = {'id': resource_id}
        response = requests.get(url=uri, params=params)
        return response.status_code, response.json()

    def update_unknown_resource(self, resource_id: int) -> json:
        uri = f'{self.url}/' + '{resource}/' + f'{resource_id}'
        response = requests.put(url=uri)
        return response.status_code, response.json()

    def patch_unknown_resource(self, resource_id: int) -> json:
        uri = f'{self.url}/' + '{resource}/' + f'{resource_id}'
        response = requests.patch(url=uri)
        return response.status_code, response.json()

    def delete_unknown_resource(self, resource_id: int) -> json:
        uri = f'{self.url}/' + '{resource}/' + f'{resource_id}'
        response = requests.delete(url=uri)
        return response.status_code


    def end_session(self):
        uri = f'{self.url}/logout'
        response = requests.post(url=uri)
        return response.status_code, response.json()


    def register(self, username: str, email: str, password: str) -> json:
        uri = f'{self.url}/register'
        data = json.dumps({"username": username, "email": email, "password": password},
                          ensure_ascii=False).encode('utf-8')
        headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        response = requests.post(url=uri, data=data, headers=headers)
        return response.status_code, response.text


    def create_session(self, username: str, email: str, password: str) -> json:
        uri = f'{self.url}/login'
        data = json.dumps({"username": username, "email": email, "password": password},
                          ensure_ascii=False).encode('utf-8')
        headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        response = requests.post(url=uri, data=data, headers=headers)
        return response.status_code, response.text