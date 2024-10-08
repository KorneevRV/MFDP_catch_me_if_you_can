from auth.jwt_handler import create_access_token


def user_cases():
    users = [
        {"user_id": 1,
         "username": "first_user",
         "email": "test1@ya.ru",
         "password": "qwerty1"},
        {"user_id": 2,
         "username": "second_user",
         "email": "test2@mail.ru",
         "password": "qwerty1"}
         ]

    for user in users:
        user['token'] = create_access_token(user['user_id'])

    return users
