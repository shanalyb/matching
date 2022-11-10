# Мэтчинг по группам наименований компаний
На вход подается название компании. Алгоритм соотносит входное название с группой похожих на него наименований одной из компаний.
### Деплой
Проект развернут на облачной платформе Heroku: [matching-itmo](https://matching-itmo.herokuapp.com/).
При этом вычислительных мощностей на бесплатном тарифном плане недостаточно.
![streamlit](https://github.com/shanalyb/matching/blob/master/img/streamlit.png)
### Результаты

| Model                     | F1   | Recall | Presicion |
|---------------------------|------|--------|-----------|
| LogisticRegression        | 0.79 | 0.67   | 0.96      |
| CatBoostClassifier        | 0.92 | 0.86   | 0.98      |


### Структура репозитория
    .
    ├── .gitignore
    ├── Procfile
    ├── README.md
    ├── catboost.ipynb
    ├── catboost_model
    ├── conn_comp
    ├── inference.ipynb
    ├── log_reg.ipynb
    ├── main.py
    ├── requirements.txt
    ├── runtime.txt
    ├── setup.sh
    └── tfidf.pickle

### Минимальное необходимое оборудование
CPU: 1 vCPU, 4 Gb RAM  

i5-1035G1
~80 запросов в секунду  
### Масштабирование
Использование Yandex Container Solution  
### Метрики
F1-score, recall, precision.  
Был выбран recall, т.к. данные не сбалансированы.