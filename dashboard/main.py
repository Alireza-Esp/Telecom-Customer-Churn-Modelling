import streamlit as st
from data import *
from charts import *
from styles import *

st.set_page_config(
    page_title="Telecom Customer Churn Dashboard",
    page_icon="📊",
    initial_sidebar_state="expanded",
    layout="centered",
)

st.markdown(css_styles, unsafe_allow_html=True)

with st.sidebar:
    st.title("📲 Telecom Customer Churn Dashboard")
    st.container(height=20, border=False)
    
    sidebar_col1, = st.columns(1, border=True)
    with sidebar_col1:
        st.markdown("#### Quick Access:")
        st.container(height=5, border=False)
        st.markdown("- [Geographic Distribution of Customers](#what-is-the-geographic-distribution-of-customers-in-california)")
        st.markdown("- [Count of Unique Values](#how-many-of-each-unique-value-of-the-indices-are-there)")
        st.markdown("- [Distribution of Numerical Indices](#how-is-the-distribution-of-each-numerical-index)")
        st.markdown("- [Fraction of Total Values](#what-fraction-of-the-total-values-of-a-numerical-index-does-each-unique-value-of-a-categorical-index-make-up)")
        st.markdown("- [Distribution of Numerical Indices Over Categorical indices](#how-is-the-distribution-of-numerical-indices-over-categorical-indices)")
        st.markdown("- [Distribution of Numerical Indices Relative to Each Other](#how-are-the-numerical-indices-distributed-relative-to-each-other)")
    
    st.container(height=10, border=False)
    
    sidebar_col2, = st.columns(1, border=True)
    with sidebar_col2:
        st.markdown("#### About Us:")
        st.container(height=5, border=False)
        st.markdown("This dashboard is designed to visualize and analyze customer churn data for a telecom company. It provides insights into customer demographics, service usage, and churn patterns.")
        st.markdown("Designed and developed by:")
        st.markdown("#### 👨‍💼 Alireza Esmaeilpour")
        st.markdown(" - [GitHub](https://github.com/alireza-Esp)")
        st.markdown(" - [Kaggle](https://www.kaggle.com/alirezaesmaeilpour)")
        st.markdown(" - [Website](https://alireza-esp.ir/)")


data = get_main_dataset()
cities_density = get_cities_density_dataset()


sec1 = st.container(border=True)
with sec1:
    st.markdown("### What is the geographic distribution of customers in California?")
    
    sec1_col1, sec1_col2 = st.columns((1,1), gap="small", vertical_alignment="center")
    
    with sec1_col1:
        scatter_map_plot1 = get_customers_scatter_map(
            data=cities_density,
            churn_label="No",
            color="blue",
            max_size=5,
            label="Churn : No",
        )
        st.plotly_chart(scatter_map_plot1, key="scatter_map_plot1")
    
    with sec1_col2:
        scatter_map_plot2 = get_customers_scatter_map(
            data=cities_density,
            churn_label="Yes",
            color="red",
            max_size=5.5,
            label="Churn : Yes",
        )
        st.plotly_chart(scatter_map_plot2, key="scatter_map_plot2")
    
st.container(height=20, border=False)

categorical_columns, numerical_columns = get_categorical_numerical_columns(data=data)

sec2 = st.container(border=True)
with sec2:
    st.markdown("### How many of each unique value of the indices are there?")
    st.container(height=20, border=False)
    
    sec2_col1, sec2_col2, sec2_col3 = st.columns((1,1,1), gap="small")
    
    select_main_category_text = "Select a main category:"
    select_secondary_category_text = "Select a secondary category:"
    with sec2_col1:
        histogram_plot1_main_category = st.selectbox(
            label=select_main_category_text,
            options=categorical_columns,
            index=categorical_columns.index("Internet Service"),
            key="histogram_plot1_main_category"
        )
        histogram_plot1_secondary_category = st.selectbox(
            label=select_secondary_category_text,
            options=categorical_columns,
            index=categorical_columns.index("Churn Label"),
            key="histogram_plot1_secondary_category"
        )
        histogram_plot1 = get_histogram_plot(
            data=data,
            category_x=histogram_plot1_main_category,
            category_color=histogram_plot1_secondary_category,
        )
        st.plotly_chart(histogram_plot1, key="histogram_plot1")
    
    with sec2_col2:
        histogram_plot2_main_category = st.selectbox(
            label=select_main_category_text,
            options=categorical_columns,
            index=categorical_columns.index("Customer Status"),
            key="histogram_plot2_main_category"
        )
        histogram_plot2_secondary_category = st.selectbox(
            label=select_secondary_category_text,
            options=categorical_columns,
            index=categorical_columns.index("Referred a Friend"),
            key="histogram_plot2_secondary_category"
        )
        histogram_plot2 = get_histogram_plot(
            data=data,
            category_x=histogram_plot2_main_category,
            category_color=histogram_plot2_secondary_category,
        )
        st.plotly_chart(histogram_plot2, key="histogram_plot2")
    
    with sec2_col3:
        histogram_plot3_main_category = st.selectbox(
            label=select_main_category_text,
            options=categorical_columns,
            index=categorical_columns.index("Contract"),
            key="histogram_plot3_main_category"
        )
        histogram_plot3_secondary_category = st.selectbox(
            label=select_secondary_category_text,
            options=categorical_columns,
            index=categorical_columns.index("Tech Support"),
            key="histogram_plot3_secondary_category"
        )
        histogram_plot3 = get_histogram_plot(
            data=data,
            category_x=histogram_plot3_main_category,
            category_color=histogram_plot3_secondary_category
        )
        st.plotly_chart(histogram_plot3, key="histogram_plot3")
    
st.container(height=20, border=False)

sec3 = st.container(border=True)
with sec3:
    st.markdown("### How is the distribution of each numerical index?")
    st.container(height=20, border=False)
    
    sec3_col1, sec3_col2, sec3_col3 = st.columns((1,1,1), gap="small")
    
    select_numeric_feature_text = "Select a numeric feature:"
    select_category_text = "Select a category:"
    with sec3_col1:
        univariate_box_plot1_numeric_feature = st.selectbox(
            label=select_numeric_feature_text,
            options=numerical_columns,
            index=numerical_columns.index("Monthly Charges"),
            key="univariate_box_plot1_numeric_feature"
        )
        univariate_box_plot1_category = st.selectbox(
            label=select_category_text,
            options=categorical_columns,
            index=categorical_columns.index("Unlimited Data"),
            key="univariate_box_plot1_category"
        )
        univariate_box_plot1 = get_univariate_box_plot(
            data=data,
            numeric_axis=univariate_box_plot1_numeric_feature,
            category_color=univariate_box_plot1_category,
        )
        st.plotly_chart(univariate_box_plot1, key="univariate_box_plot1")
    
    with sec3_col2:
        univariate_box_plot2_numeric_feature = st.selectbox(
            label=select_numeric_feature_text,
            options=numerical_columns,
            index=numerical_columns.index("Number of Referrals"),
            key="univariate_box_plot2_numeric_feature"
        )
        univariate_box_plot2_category = st.selectbox(
            label=select_category_text,
            options=categorical_columns,
            index=categorical_columns.index("Offer"),
            key="univariate_box_plot2_category"
        )
        univariate_box_plot2 = get_univariate_box_plot(
            data=data,
            numeric_axis=univariate_box_plot2_numeric_feature,
            category_color=univariate_box_plot2_category,
        )
        st.plotly_chart(univariate_box_plot2, key="univariate_box_plot2")
    
    with sec3_col3:
        univariate_box_plot3_numeric_feature = st.selectbox(
            label=select_numeric_feature_text,
            options=numerical_columns,
            index=numerical_columns.index("Total Long Distance Charges"),
            key="univariate_box_plot3_numeric_feature"
        )
        univariate_box_plot3_category = st.selectbox(
            label=select_category_text,
            options=categorical_columns,
            index=categorical_columns.index("Gender"),
            key="univariate_box_plot3_category"
        )
        univariate_box_plot3 = get_univariate_box_plot(
            data=data,
            numeric_axis=univariate_box_plot3_numeric_feature,
            category_color=univariate_box_plot3_category,
        )
        st.plotly_chart(univariate_box_plot3, key="univariate_box_plot3")
    
st.container(height=20, border=False)

sec4 = st.container(border=True)
with sec4:
    st.markdown("### What fraction of the total values of a numerical index does each unique value of a categorical index make up?")
    st.container(height=20, border=False)
    
    sec4_col1, sec4_col2, sec4_col3 = st.columns((1,1,1), gap="small")
    
    with sec4_col1:
        pie_plot1_numeric_feature = st.selectbox(
            label=select_numeric_feature_text,
            options=numerical_columns,
            index=numerical_columns.index("Tenure Months"),
            key="pie_plot1_numeric_feature"
        )
        pie_plot1_category = st.selectbox(
            label=select_category_text,
            options=categorical_columns,
            index=categorical_columns.index("Churn Label"),
            key="pie_plot1_category"
        )
        pie_plot1 = get_pie_chart(
            data=data,
            category=pie_plot1_category,
            numeric=pie_plot1_numeric_feature,
        )
        st.plotly_chart(pie_plot1, key="pie_plot1")
    
    with sec4_col2:
        pie_plot2_numeric_feature = st.selectbox(
            label=select_numeric_feature_text,
            options=numerical_columns,
            index=numerical_columns.index("Total Extra Data Charges"),
            key="pie_plot2_numeric_feature"
        )
        pie_plot2_category = st.selectbox(
            label=select_category_text,
            options=categorical_columns,
            index=categorical_columns.index("Streaming TV"),
            key="pie_plot2_category"
        )
        pie_plot2 = get_pie_chart(
            data=data,
            category=pie_plot2_category,
            numeric=pie_plot2_numeric_feature,
        )
        st.plotly_chart(pie_plot2, key="pie_plot2")
    
    with sec4_col3:
        pie_plot3_numeric_feature = st.selectbox(
            label=select_numeric_feature_text,
            options=numerical_columns,
            index=numerical_columns.index("Total Charges"),
            key="pie_plot3_numeric_feature"
        )
        pie_plot3_category = st.selectbox(
            label=select_category_text,
            options=categorical_columns,
            index=categorical_columns.index("Contract"),
            key="pie_plot3_category"
        )
        pie_plot3 = get_pie_chart(
            data=data,
            category=pie_plot3_category,
            numeric=pie_plot3_numeric_feature,
        )
        st.plotly_chart(pie_plot3, key="pie_plot3")
    
st.container(height=20, border=False)

sec5 = st.container(border=True)
with sec5:
    st.markdown("### How is the distribution of numerical indices over categorical indices?")
    
    sec5_col1, sec5_col2, sec5_col3 = st.columns((1,1,1), gap="small")
    
    with sec5_col1:
        multivariate_box_plot1 = get_multivariate_box_plot(
            data=data,
            category_axis="Internet Service",
            numeric="Satisfaction Score",
            category_color="Churn Label",
        )
        st.plotly_chart(multivariate_box_plot1, key="multivariate_box_plot1")
    
    with sec5_col2:
        multivariate_box_plot2 = get_multivariate_box_plot(
            data=data,
            category_axis="Internet Service",
            numeric="Satisfaction Score",
            category_color="Churn Label",
        )
        st.plotly_chart(multivariate_box_plot2, key="multivariate_box_plot2")
    
    with sec5_col3:
        multivariate_box_plot3 = get_multivariate_box_plot(
            data=data,
            category_axis="Internet Service",
            numeric="Satisfaction Score",
            category_color="Churn Label",
        )
        st.plotly_chart(multivariate_box_plot3, key="multivariate_box_plot3")
    
st.container(height=20, border=False)

sec6 = st.container(border=True)
with sec6:
    st.markdown("### How are the numerical indices distributed relative to each other?")
    
    sec6_col1, sec6_col2, sec6_col3 = st.columns((1,1,1), gap="small")
    
    with sec6_col1:
        density_heatmap1 = get_density_heatmap_plot(
            data=data,
            numeric_x="Total Revenue",
            numeric_y="Satisfaction Score",
            color_scales=color_scales
        )
        st.plotly_chart(density_heatmap1, key="density_heatmap1")
    
    with sec6_col2:
        density_heatmap2 = get_density_heatmap_plot(
            data=data,
            numeric_x="Total Revenue",
            numeric_y="Satisfaction Score",
            color_scales=color_scales
        )
        st.plotly_chart(density_heatmap2, key="density_heatmap2")
    
    with sec6_col3:
        density_heatmap3 = get_density_heatmap_plot(
            data=data,
            numeric_x="Total Revenue",
            numeric_y="Satisfaction Score",
            color_scales=color_scales
        )
        st.plotly_chart(density_heatmap3, key="density_heatmap3")
    
