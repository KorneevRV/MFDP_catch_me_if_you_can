# MFDP_catch_me_if_you_can

Решение автоматизирует процесс определения заработной платы на основе данных о вакансии в области Data Jobs.

# <ins>How-to</ins>
## Работа с веб-интерфейсом и API <img src="https://img.shields.io/badge/status-в%20разработке-orange" alt="в разработке" width="100"/>



## Работа с моделью
Для работы с моделью необходимо:
- Загрузить данные для обучения - [Яндекс.Диск](https://disk.yandex.ru/d/xKuLrDvpwh2wZQ)
- Поместить данные в папку `/data` в корневом каталоге.
- Код обучения модели содержится в папке `/notebooks`. Самая совершенная модель - [enhanced_model](https://github.com/KorneevRV/MFDP_catch_me_if_you_can/blob/main/notebooks/enhanced_model.ipynb).

# <ins>Структура репозитория</ins>

### /docs
 - [Бизнес-анализ](https://github.com/KorneevRV/MFDP_catch_me_if_you_can/blob/main/docs/Business%20analysis.md)
 - Описание функционала <img src="https://img.shields.io/badge/status-в%20разработке-orange" alt="в разработке" width="100"/>
 - Документацию к API <img src="https://img.shields.io/badge/status-в%20разработке-orange" alt="в разработке" width="100"/>

### /notebooks
Ноутбуки с обучением модели и тестированием гипотез:
- [baseline](https://github.com/KorneevRV/MFDP_catch_me_if_you_can/blob/main/notebooks/baseline.ipynb) - ноутбук с baseline решением
- [enhanced_model](https://github.com/KorneevRV/MFDP_catch_me_if_you_can/blob/main/notebooks/enhanced_model.ipynb) - ноутбук с экспериментами пол улучшению модели
- [enhanced_model_embed](https://github.com/KorneevRV/MFDP_catch_me_if_you_can/blob/main/notebooks/enhanced_model_embed.ipynb) - ноутбук с экспериментами по преобразованию текста в эмбеддинги

### /src <img src="https://img.shields.io/badge/status-в%20разработке-orange" alt="в разработке" width="100"/>

Исходные файлы для запуска приложения с веб-интерфейсом.

### /data
Раздел для хранения данных для обучения модели.

Из-за инфраструктурных ограничений данные хранятся не в репозитории, автоматических средств управления данными в проекте не предусмотрено. Для переобучения модели данные следует загрузить и поместить в папку `/data` вручную. Данные для обучения модели - [Яндекс.Диск](https://disk.yandex.ru/d/xKuLrDvpwh2wZQ).