import streamlit as st
import pandas as pd


@st.cache_data
def get_main_dataset():
    data = pd.read_csv("https://github.com/Alireza-Esp/Telecom-Customer-Churn-Modelling/raw/refs/heads/main/data/telecom-customer-churn-v2.csv")
    data.fillna("NULL", inplace=True)
    return data

@st.cache_data
def get_cities_density_dataset():
    return pd.read_csv("https://github.com/Alireza-Esp/Telecom-Customer-Churn-Modelling/raw/refs/heads/main/data/cities-density.csv")

@st.cache_data
def get_categorical_numerical_columns(data: pd.DataFrame):
    categorical_columns = []
    numerical_columns = []
    
    for i in data.columns:
        if data[i].dtype == "object":
            categorical_columns.append(i)
        else:
            numerical_columns.append(i)
    
    return [categorical_columns, numerical_columns]