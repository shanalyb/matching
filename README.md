# Мэтчинг по группам наименований компаний
На вход подается название компании. Алгоритм соотносит входное название с группой похожих на него наименований одной из компаний.
### Деплой
Проект развернут на облачной платформе Heroku: [matching-itmo](https://matching-itmo.herokuapp.com/).
При этом вычислительных мощностей на бесплатном тарифном плане недостаточно.
![streamlit](https://github.com/shanalyb/matching/blob/master/img/streamlit.png)
### Структура репозитория
    .
    ├── .gitignore
    ├── Procfile
    ├── README.md
    ├── catboost_model
    ├── conn_comp
    ├── catboost.ipynb
    ├── main.py
    ├── requirements.txt
    ├── runtime.txt
    ├── setup.sh
    └── tfidf.pickle