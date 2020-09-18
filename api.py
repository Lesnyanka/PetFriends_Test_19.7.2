import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetFriends:
     def __init__(self):
         self.base_url = "https://petfriends1.herokuapp.com/"


     def get_api_key(self, email, password):


         headers = {
             'email':email,
             'password':password
         }
         res = requests.get(self.base_url+'api/key', headers=headers)
         status = res.status_code
         result = ""
         try:
             result = res.json()
         except:
             result = res.txt()
         return status, result

     def get_list_of_pets(self, auth_key, filter):
         headers = {'auth_key': auth_key['key']}
         filter = {'filter': filter}
         res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)

         status = res.status_code
         result = ""
         try:
             result = res.json()
         except:
             result = res.txt()
         return status, result

     def add_new_pet_without_photo(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
         """ Отправка   данных о добавляемом питомце и возврат статуса
         запроса  и результат в формате JSON с данными добавленного питомца"""

         data = MultipartEncoder(
             fields={
                 'name': name,
                 'animal_type': animal_type,
                 'age': age
             })
         headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

         res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
         status = res.status_code
         result = ""
         try:
             result = res.json()
         except json.decoder.JSONDecodeError:
             result = res.text
         print(result)
         return status, result

     def get_api_key(self, email: str, passwd: str) -> json:
         """ Запрос к API сервера и возврат статуса запроса и результата в формате
         JSON с  ключем пользователя"""

         headers = {
             'email': email,
             'password': passwd,
         }
         res = requests.get(self.base_url + 'api/key', headers=headers)
         status = res.status_code
         result = ""
         try:
             result = res.json()
         except json.decoder.JSONDecodeError:
             result = res.text
         return status, result

     def get_list_of_pets(self, auth_key: json, filter: str = "") -> json:
         """ Запрос к API сервера и возврат статуса запроса и результата в формате JSON
         со списком найденных питомцев, по фильтру.  Фильтр может иметь
          пустое значение - получить список всех питомцев, или 'my_pets' - получить список
         собственных питомцев"""

         headers = {'auth_key': auth_key['key']}
         filter = {'filter': filter}

         res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
         status = res.status_code
         result = ""
         try:
             result = res.json()
         except json.decoder.JSONDecodeError:
             result = res.text
         return status, result

     def add_new_pet_with_photo(self, auth_key: json, name: str, animal_type: str,
                                age: str, pet_photo: str) -> json:
         """Отправление на сервер данных(С ФОТО) о добавляемом питомце , возврт статуса
         запроса на сервер и результата в формате JSON с данными добавленного питомца"""

         data = MultipartEncoder(
             fields={
                 'name': name,
                 'animal_type': animal_type,
                 'age': age,
                 'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'images/jpeg')
             })
         headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

         res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
         status = res.status_code
         result = ""
         try:
             result = res.json()
         except json.decoder.JSONDecodeError:
             result = res.text
         print(result)
         return status, result

     def add_photo_for_pet(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
         """Метод отправляет (постит) на сервер фото  питомца и возвращает статус
         запроса на сервер и результат в формате JSON с данными добавленного питомца"""

         data = MultipartEncoder(
             fields={'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'images/jpeg')}
         )
         headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

         res = requests.post(self.base_url + '/api/pets/set_photo/' + pet_id, headers=headers, data=data)
         status = res.status_code
         result = ""
         try:
             result = res.json()
         except json.decoder.JSONDecodeError:
             result = res.text
         print(result)
         return status, result

     def delete_pet(self, auth_key: json, pet_id: str) -> json:
         """ Запрос на удаление питомца по  ID и возврат
         статуса запроса и результата в формате JSON с текстом уведомления об успешном удалении"""

         headers = {'auth_key': auth_key['key']}

         res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
         status = res.status_code
         result = ""
         try:
             result = res.json()
         except json.decoder.JSONDecodeError:
             result = res.text
         return status, result

     def update_pet_info(self, auth_key: json, pet_id: str, name: str,
                         animal_type: str, age: int) -> json:
         """ Запрос на сервер об обновлении данных питомца по  ID и
         возврат статуса запроса  в формате JSON с обновлённыи данными питомца"""

         headers = {'auth_key': auth_key['key']}
         data = {
             'name': name,
             'age': age,
             'animal_type': animal_type
         }

         res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
         status = res.status_code
         result = ""
         try:
             result = res.json()
         except json.decoder.JSONDecodeError:
             result = res.text
         return status, result

