import streamlit as st
import pandas as pd
import plotly.express as px
from random import choice
from styles import plotly_color_palettes, color_scales

@st.cache_resource
def get_customers_scatter_map(data: pd.DataFrame, churn_label: str, color: str, max_size: float, label: str):
    return px.scatter_map(
        data_frame=data[data["Churn Label"] == churn_label],
        lat="Latitude",
        lon="Longitude",
        size="Count",
        hover_name="City",
        hover_data="Count",
        title=label,
        subtitle="Larger size, as well as higher opacity, indicates higher customers density...",
        color_discrete_sequence=[color],
        opacity=0.4,
        zoom=4,
        size_max=max_size,
        height=500
        )


@st.cache_resource
def get_histogram_plot(data: pd.DataFrame, category_x: str, category_color: str):
    return px.histogram(
        data_frame=data,
        x=category_x,
        color=category_color,
        color_discrete_sequence=choice(plotly_color_palettes),
        template="plotly_white"
    )

@st.cache_resource
def get_univariate_box_plot(data: pd.DataFrame, numeric_axis: str, category_color: str):
    return px.box(
        data_frame=data,
        y=numeric_axis,
        color=category_color,
        color_discrete_sequence=choice(plotly_color_palettes),
        template="plotly_white"
    )

@st.cache_resource
def get_pie_chart(data: pd.DataFrame, category: str, numeric: str):
    return px.pie(
        data_frame=data,
        names=category,
        values=numeric,
        title=category,
        subtitle=numeric,
        color_discrete_sequence=choice(plotly_color_palettes),
        template="plotly_white"
    )

@st.cache_resource
def get_multivariate_box_plot(data: pd.DataFrame, category_axis: str, numeric: str, category_color: str):
    return px.box(
        data_frame=data,
        x=numeric,
        y=category_axis,
        color=category_color,
        color_discrete_sequence=choice(plotly_color_palettes),
        template="plotly_white"
    )

@st.cache_resource
def get_density_heatmap_plot(data: pd.DataFrame, numeric_x: str, numeric_y: str, color_scales: list):
    return px.density_heatmap(
        data_frame=data,
        x=numeric_x,
        y=numeric_y,
        color_continuous_scale=choice(color_scales),
        template="plotly_white"
    )