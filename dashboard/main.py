import streamlit as st
from data import get_main_dataset, get_cities_density_dataset

data = get_main_dataset()
cities_density = get_cities_density_dataset()

st.set_page_config(
    page_title="Telecom Customer Churn Dashboard",
    page_icon="📊",
    initial_sidebar_state="expanded",
    layout="centered",
    menu_items={
        "Get help":"https://alireza-esp.ir/",
        "Report a Bug":"https://alireza-esp.ir/",
        "About":"https://alireza-esp.ir/"
    } # type: ignore
)

st.markdown("""
        <style>
                .block-container {
                    padding-top: 100px;
                    padding-bottom: 100px;
                    padding-left: 0px;
                    padding-right: 0px;
                    margin-top: 0px;
                    margin-bottom: 0px;
                    margin-left: 0px;
                    margin-right: 0px;
                }
        </style>
        """, unsafe_allow_html=True)

with st.sidebar:
    st.title("📲 Telecom Customer Churn Dashboard")
    sidebar_col1, = st.columns(1, border=True)
    with sidebar_col1:
        st.text("Quick Access:")
    
    sidebar_col2, = st.columns(1, border=True)
    with sidebar_col2:
        st.text("About Us:")

main_col1, = st.columns(1, border=True,)


st.markdown("### Geographic Distribution of Dustomers")
st.dataframe(data=data)