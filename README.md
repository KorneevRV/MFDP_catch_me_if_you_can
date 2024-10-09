# MFDP_catch_me_if_you_can

Решение автоматизирует процесс определения заработной платы на основе данных о вакансии в области Data Jobs.
<details>  
<summary>Веб-интерфейс</summary>

![](https://github.com/KorneevRV/MFDP_catch_me_if_you_can/blob/main/docs/images/prediction.gif)
</details>

# <ins>How-to</ins>
## Запуск веб-интерфейса
1. Переименовать все `.env.template` файлы в `.env`. При необходимости изменить переменные окружения в `.env` файлах.
```bash
find . -name ".env.template" -exec sh -c 'mv "$0" "${0%.template}"' {} \;
```

2. Запустить контейнеры:
``` bash
cd src
docker compose build 
docker compose up
```
3. Открыть веб-интерфейс по адресу: http://127.0.0.11/

4. Следовать подсказкам в интерфейсе

5. (Опционально) Запустить автотесты:
```bash
docker exec src-app-1 pytest -v
```

## Работа с моделью
Для обучения модели необходимо:
- Загрузить данные для обучения - [Яндекс.Диск](https://disk.yandex.ru/d/xKuLrDvpwh2wZQ)
- Поместить данные в папку `/data` в корневом каталоге.
- Код обучения модели содержится в папке `/notebooks`. Самая совершенная модель - [enhanced_model](https://github.com/KorneevRV/MFDP_catch_me_if_you_can/blob/main/notebooks/enhanced_model.ipynb).

# <ins>Структура репозитория</ins>

### /docs
 - [Бизнес-анализ](https://github.com/KorneevRV/MFDP_catch_me_if_you_can/blob/main/docs/Business%20analysis.md)
 - [Документация к веб-сервису](https://github.com/KorneevRV/MFDP_catch_me_if_you_can/blob/main/docs/Software%20documentation.md)

### /notebooks
Ноутбуки с обучением модели и тестированием гипотез:
- [baseline](https://github.com/KorneevRV/MFDP_catch_me_if_you_can/blob/main/notebooks/baseline.ipynb) - ноутбук с baseline решением
- [enhanced_model](https://github.com/KorneevRV/MFDP_catch_me_if_you_can/blob/main/notebooks/enhanced_model.ipynb) - ноутбук с экспериментами пол улучшению модели
- [enhanced_model_embed](https://github.com/KorneevRV/MFDP_catch_me_if_you_can/blob/main/notebooks/enhanced_model_embed.ipynb) - ноутбук с экспериментами по преобразованию текста в эмбеддинги

### /src

Исходные файлы для запуска приложения с веб-интерфейсом.

### /data
Раздел для хранения данных для обучения модели.

Из-за инфраструктурных ограничений данные хранятся не в репозитории, автоматических средств управления данными в проекте не предусмотрено. Для переобучения модели данные следует загрузить и поместить в папку `/data` вручную. Данные для обучения модели - [Яндекс.Диск](https://disk.yandex.ru/d/xKuLrDvpwh2wZQ).