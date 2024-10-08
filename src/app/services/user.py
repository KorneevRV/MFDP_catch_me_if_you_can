import warnings
from datetime import datetime
from typing import List, Optional

import pandas as pd
from pydantic import ValidationError

from models.logs import Request, SalaryData
from models.user import User
from services.logs import log_request

warnings.filterwarnings("ignore")


def get_all_users(session) -> List[User]:
    """Возвращает список всех зарегистрированных пользователей."""
    return session.query(User).all()


def get_user(user_id: int, session) -> Optional[User]:
    """Возвращает объект класса User, если такой user_id есть в БД."""
    return session.query(User).where(User.user_id == user_id).first()


def get_user_by_email(email: str, session) -> Optional[User]:
    """Возвращает объект класса User, если такой email есть в БД."""
    return session.query(User).where(User.email == email).first()


def create_user(
    username: str,
    email: str,
    password: str,
    session
) -> dict[str, str]:
    """
    Проверяет, что пользователь с таким e-mail не зарегистрирован и
    создает нового пользователя в БД.
    """
    # Проверка на отсутствие email в БД
    old_user = session.query(User).where(User.email == email).first()
    if old_user is not None:
        return {'error': 'Email already in use'}

    # Запись информации о новом пользователе в БД
    new_user = User(
        email=email,
        username=username,
        password_hash=password
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {'success': 'Successfully created'}


def process_request(
    user_id: int,
    name: str,
    description: str,
    model_from,
    model_to,
    session
) -> dict:
    """
    Принимает запрос от пользователя, обрабатывает запрос и
    возвращает результат.
    """
    # Приведение запроса в нужный формат
    request = pd.DataFrame({
        'Name': [name],
        'Description': [description]
    })
    # Получение предсказания от модели
    salary_from = model_from.predict(request)
    salary_to = model_to.predict(request)

    # Конвертация в JSON
    response = {
        'salary_from': int(salary_from[0]),
        'salary_to': int(salary_to[0])
    }

    # Проверка ответа модели
    try:
        SalaryData(**response)
    except ValidationError:
        return {'error': 'Model failed'}

    # Сохранение данных запроса в БД
    request = Request(
        user_id=user_id,
        vacancy_name=name,
        vacancy_description=description,
        salary_from=response['salary_from'],
        salary_to=response['salary_to'],
        timestamp=datetime.now()
    )
    log_request(request, session)
    return response
