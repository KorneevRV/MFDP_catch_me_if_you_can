import streamlit as st
import requests

import pages.elements as elements

# Блок настроек по умолчанию
elements.set_wide()
elements.create_navbar()
cookie_manager = elements.get_manager()
access_token = cookie_manager.get("access_token")
elements.token_check(access_token)

st.title("Новый запрос")
st.warning(
    "Внимание! Для вакансий уровня Teamlead, Head, C-level предсказания могут "
    "быть недостоверными из-за недостатка данных о зарплатах. Интерпретируйте "
    "результаты для этих уровней с осторожностью."
)

# Выбор сезона
name = st.text_input('Название вакансии')

# Загрузка списка городов
description = st.text_area('Описание вакансии', height=300)

if st.button('Отправить запрос'):
    # Отправка запроса
    response = requests.post(
        'http://app:8080/ml/process_request/',
        params={
            'token': access_token,
            'name': name,
            'description': description
        }
    )
    response = response.json()
    salary_from = response['salary_from']
    salary_to = response['salary_to']

    # Fancy вывод диапазона зарплат
    st.subheader("Предсказанный диапазон зарплат:")

    # Рассчитываем среднюю зарплату
    average_salary = (salary_from + salary_to) / 2

    # Располагаем зарплаты в одну строку по возрастанию
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Минимальная зарплата",
            f"{salary_from // 1000 * 1000:,.0f} руб."
        )
    with col2:
        st.metric(
            "Средняя зарплата",
            f"{average_salary // 1000 * 1000:,.0f} руб."
        )
    with col3:
        st.metric(
            "Максимальная зарплата",
            f"{salary_to // 1000 * 1000:,.0f} руб."
        )

    # Проверка условий для отображения дисклеймера
    if average_salary < 150000:
        st.warning(
            "Внимание! Предсказанная зарплата ниже типичного диапазона. "
            "Это может быть связано с начальным уровнем позиции или неполной "
            "занятостью. Обратите внимание, что ошибка в предсказании может "
            "составлять до 50 000 рублей. Пожалуйста, используйте "
            "предсказанную зарплату с осторожностью."
        )
    elif salary_to > 600000:
        st.warning(
            "Внимание! Предсказанная максимальная зарплата выше типичного "
            "диапазона. Из-за недостатка данных об оплате "
            "высококвалифицированных специалистов, предсказанные зарплаты "
            "следует рассматривать скорее как минимальные, особенно для "
            "уровня Teamlead / Head / VP / CTO."
        )
