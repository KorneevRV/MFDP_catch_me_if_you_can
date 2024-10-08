import streamlit as st
import requests

import pages.elements as elements

# Блок настроек по умолчанию
elements.set_wide()
elements.create_navbar()
cookie_manager = elements.get_manager()
access_token = cookie_manager.get("access_token")

st.title("SalaryScout")

overview_col, tabs_col = st.columns(2)

# Колонка с описанием
with overview_col:
    st.write('## Описание')
    st.write("""
    На основании названия вакансии и описания должностных обязанностей сервис предлагает
    прогноз диапазона заработной платы для данной позиции.
    """)
    st.write('## Сценарии использования')
    st.write("""
    1) **HR и рекрутинг**: Специалисты по подбору персонала могут использовать
    сервис для формирования конкурентоспособных предложений о работе и
    определения рыночных зарплат для различных позиций на основании описания вакансии.
    2) **Аналитика рынка труда**: Исследователи и аналитики могут использовать
    данные для анализа тенденций в области оплаты труда и прогнозирования
    изменений на рынке труда.
    """)

# Колонка со входом и регистрацией
with tabs_col:
    login, register = st.tabs(["Вход", "Регистрация"])

# Вкладка входа
with login:
    email = st.text_input("E-mail", key="email")
    password = st.text_input("Пароль", type="password", key="password")

    if st.button("Войти", type="primary", key="signin"):
        response = requests.post('http://app:8080/user/signin',
                                 params={'email': email,
                                         'password': password})
        if response.status_code in [401, 404]:
            error_desc = response.json()["detail"]
            st.error("""Пароль или e-mail введены неверно или
                     аккаунт с таким e-mail не существует""")
        # TODO понять почему не срабатывает редирект
        else:
            token = response.json()["access_token"]
            cookie_manager.set('access_token', token)
    if access_token is not None:
        st.success('Вы вошли!', icon="✅")
        if st.button("Перейти к описанию сервиса"):
            st.switch_page("pages/description.py")

# Вкладка регистрации
with register:
    username = st.text_input("Имя пользователя")
    email = st.text_input("E-mail")
    password = st.text_input("Пароль", type="password")

    if st.button("Зарегистрироваться", type="primary", key="sign_up"):
        response = requests.post('http://app:8080/user/signup',
                                 params={'username': username,
                                         'password': password,
                                         'email': email})
        if response.status_code == 200:
            message = response.json()
            st.success('Регистрация успешна!', icon="✅")
        else:
            message = response.json()
            st.error(message['detail'], icon="🚨")
