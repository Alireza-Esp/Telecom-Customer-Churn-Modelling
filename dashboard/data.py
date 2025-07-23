import streamlit as st
import pandas as pd


@st.cache_data
def get_main_dataset():
    return pd.read_csv("https://github.com/Alireza-Esp/Telecom-Customer-Churn-Modelling/raw/refs/heads/main/data/telecom-customer-churn-v2.csv")

st.cache_data
def get_cities_density_dataset():
    return pd.read_csv("")