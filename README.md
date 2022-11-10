# Мэтчинг по группам наименований компаний
На вход подается название компании. Алгоритм соотносит входное название с группой похожих на него наименований одной из компаний.
### Деплой
Проект развернут на облачной платформе Heroku: [matching-itmo](https://matching-itmo.herokuapp.com/).
При этом вычислительных мощностей на бесплатном тарифном плане недостаточно.
### Структура репозитория
    .
    ├── .gitignore
    ├── Procfile
    ├── README.md
    ├── catboost_model
    ├── conn_comp
    ├── main.ipynb
    ├── main.py
    ├── requirements.txt
    ├── runtime.txt
    ├── setup.sh
    └── tfidf.pickle