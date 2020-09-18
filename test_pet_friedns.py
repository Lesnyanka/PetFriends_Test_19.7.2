from api import PetFriends
from settings import *

import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filters=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filters)
    assert status == 200
    assert len(result['pets']) > 0

    # 1


def test_add_new_pet_without_photo(name="Кафка", animal_types="Котик", age="3"):
    """  Добавить питомца с корректными данными, но БЕЗ фото"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_types, age)
    assert status == 200
    assert result['name'] == name


#  2
def test_add_photo_for_pet(pet_photo='images/котик.jpg'):
    """ Можно добавить или изменить фото питомцу"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.add_photo_for_pet(auth_key, pet_id, pet_photo)
    assert status == 200
    assert 'jpg' in pet_photo


#  3
def test_add_un_normal_name(name="#*&&^", animal_type="Котик",
                            age="3", pet_photo='images/котик.jpg'):
    """ Можно добавить питомца с некорректным  именем """
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name_pet


#  4
def test_add_un_normal_age(name="Кафка", animal_types="Котик",
                           age="555", pet_photo='images/котик.jpg'):
    """Можно добавить питомца с некорректным возрастом"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_with_photo(auth_key, name, animal_types, age, pet_photo)

    assert status == 200
    assert result['age'] == age


#  5
def test_add_un_normal_animal_type(name="Кафка", animal_types="#$%^",
                                   age='3', pet_photo='images/котик.jpg'):
    """ Возможно добавить питомца с некорректным типом"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_with_photo(auth_key, name, animal_types, age, pet_photo)
    assert status == 200
    assert result['age'] == age


# 6
def test_add_space_in_param(name=' ', animal_types=' ', age=' '):
    """ Можно добавить питомца с пустыми полями и без фото
    :type name: object
    """
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name_pet, animal_types, age)
    assert status == 200
    assert result['name'] == name


# 7
def test_change_to_empty_value(name=' ', animal_type=' ', age=5):
    """ Возможно обновить имя и тип питомца на пробелы"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")


# 8
def test_add_str_in_age(name="Кафка", animal_types="Котик",
                        age='семь', pet_photo='images/котик.jpg'):
    """ Возможно добавить тип данных str в параметр age"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_with_photo(auth_key, name, animal_types, age, pet_photo)

    assert status == 200
    assert result['age'] == age
