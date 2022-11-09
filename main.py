import re
import pickle
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from catboost import CatBoostClassifier

@st.cache(allow_output_mutation=True)
def load_model():
    model = CatBoostClassifier()
    model.load_model('catboost_model', format='cbm')
    return model

@st.cache(allow_output_mutation=True)
def load_vectorizer():
    vectorizer = pickle.load(open("tfidf.pickle", "rb"))
    return vectorizer

@st.cache(allow_output_mutation=True)
def load_conn_comp():
    conn_comp_lst = pickle.load(open("conn_comp", "rb"))
    return conn_comp_lst

def match_company(model, veczr, connected_components_list, input_name):
    predict_lst = []
    for group in connected_components_list:
        group_lst = [input_name] * len(list(group))
        input_vec = veczr.transform(group_lst)
        group_vec = veczr.transform(list(group))
        summ = input_vec + group_vec
        predict_lst.append(model.predict_proba(summ)[:,1].mean())
    max_idx = predict_lst.index(max(predict_lst))

    return connected_components_list[max_idx]

model = load_model()
tfidf_veczr = load_vectorizer()
cc_lst = load_conn_comp()

# if "visibility" not in st.session_state:
#     st.session_state.visibility = "visible"
#     st.session_state.disabled = False

st.title('Мэтчинг компаний')
title = st.text_input(
    'Введите название компании'
    )
if title:
    with st.spinner('Wait for it...'):
        group = match_company(model, tfidf_veczr, cc_lst, title)
        st.text(group)
    st.success('Done!')