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
    
    col1, = st.columns(1, border=True)
    with col1:
        st.markdown("#### Quick Access:")
        st.container(height=5, border=False)
        st.markdown(" - [Context](#context)")
        st.markdown("- [Geographic Distribution of Customers](#what-is-the-geographic-distribution-of-customers-in-california)")
        st.markdown("- [Count of Unique Values](#how-many-of-each-unique-value-of-the-indices-are-there)")
        st.markdown("- [Distribution of Numerical Indices](#how-is-the-distribution-of-each-numerical-index)")
        st.markdown("- [Fraction of Total Values](#what-fraction-of-the-total-values-of-a-numerical-index-does-each-unique-value-of-a-categorical-index-make-up)")
        st.markdown("- [Distribution of Numerical Indices Over Categorical indices](#how-is-the-distribution-of-numerical-indices-over-categorical-indices)")
        st.markdown("- [Distribution of Numerical Indices Relative to Each Other](#how-are-the-numerical-indices-distributed-relative-to-each-other)")
    
    st.container(height=10, border=False)
    
    col2, = st.columns(1, border=True)
    with col2:
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

sec0 = st.container(border=True)
with sec0:
    st.markdown("### Context")
    st.container(height=20, border=False)
    
    st.markdown(
        """
        **This dataset tracks a telco company's customer churn located in California based on a variety of possible factors.\
        The churn column indicates whether or not the customer left within the last month.\
        Other columns include gender, dependents, monthly charges, and many with information about the types of services each customer has.<br>\
        Sources: [Kaggle](https://www.kaggle.com/datasets/ylchang/telco-customer-churn-1113), [IBM](https://community.ibm.com/community/user/blogs/steven-macko/2019/07/11/telco-customer-churn-1113)**
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """
        **Description of features:**
        - **City:** The city of the customer’s primary residence.
        - **Latitude:** The latitude of the customer’s primary residence.
        - **Longitude:** The longitude of the customer’s primary residence.
        - **Gender:** The customer’s gender: Male, Female
        - **Partner:** Indicates if the customer has a domestic partner (e.g., spouse or live-in partner): Yes, No
        - **Dependents:** Indicates if the customer lives with any dependents: Yes, No. Dependents could be children, parents, grandparents, etc.
        - **Phone Service:** Indicates if the customer subscribes to home phone service with the company: Yes, No
        - **Multiple Lines:** Indicates if the customer subscribes to multiple telephone lines with the company: Yes, No
        - **Internet Service:** Indicates if the customer subscribes to Internet service with the company: No, DSL, Fiber Optic, Cable.
        - **Unlimited Data:** Indicates if the customer has paid an additional monthly fee to have unlimited data downloads/uploads: Yes, No
        - **Online Security:** Indicates if the customer subscribes to an additional online security service provided by the company: Yes, No
        - **Online Backup:** Indicates if the customer subscribes to an additional online backup service provided by the company: Yes, No
        - **Device Protection Plan:** Indicates if the customer subscribes to an additional device protection plan for their Internet equipment provided by the company: Yes, No
        - **Tech Support:** Indicates if the customer subscribes to the company’s technical support service for general troubleshooting and assistance: Yes, No
        - **Premium Tech Support:** Indicates if the customer subscribes to an additional technical support plan from the company with reduced wait times: Yes, No
        - **Streaming TV:** Indicates if the customer uses their Internet service to stream television programing from a third party provider: Yes, No. The company does not charge an additional fee for this service.
        - **Streaming Movies:** Indicates if the customer uses their Internet service to stream movies from a third party provider: Yes, No. The company does not charge an additional fee for this service.
        - **Streaming Music:** Indicates if the customer uses their Internet service to stream music from a third party provider: Yes, No. The company does not charge an additional fee for this service.
        - **Contract:** Indicates the customer’s current contract type: Month-to-Month, One Year, Two Year.
        - **Payment Method:** Indicates how the customer pays their bill: Bank Withdrawal, Credit Card, Mailed Check
        - **Offer:** Identifies the last marketing offer that the customer accepted, if applicable. Values include None, Offer A, Offer B, Offer C, Offer D, and Offer E.
        - **Referred a Friend:** Indicates if the customer has ever referred a friend or family member to this company: Yes, No
        - **Number of Referrals:** Indicates the number of referrals to date that the customer has made.
        - **Monthly Charge:** Indicates the customer’s current total monthly charge for all their services from the company.
        - **Total Charges:** Indicates the customer’s total charges, calculated to the end of the quarter specified above.
        - **Avg Monthly Long Distance Charges:** Indicates the customer’s average long distance charges, calculated to the end of the quarter specified above.
        - **Total Long Distance Charges:** Indicates the customer’s total charges for long distance above those specified in their plan, by the end of the quarter specified above.
        - **Avg Monthly GB Download:** Indicates the customer’s average download volume in gigabytes, calculated to the end of the quarter specified above.
        - **Total Extra Data Charges:** Indicates the customer’s total charges for extra data downloads above those specified in their plan, by the end of the quarter specified above.
        - **Total Revenue:** Indicates the total revenue generated from the customer by the end of the quarter specified above. This includes all services and charges across the customer’s lifetime.
        - **Total Refunds:** Indicates the customer’s total refunds, calculated to the end of the quarter specified above.
        - **Tenure Months:** Indicates the total amount of months that the customer has been with the company by the end of the quarter specified above.
        - **CLTV:** Customer Lifetime Value. A predicted CLTV is calculated using corporate formulas and existing data. The higher the value, the more valuable the customer. High value customers should be monitored for churn.
        - **Satisfaction Score:** A customer’s overall satisfaction rating of the company from 1 (Very Unsatisfied) to 5 (Very Satisfied).
        - **Customer Status:** Indicates the status of the customer at the end of the quarter: Churned, Stayed, or Joined
        - **Churn Label:** Yes = the customer left the company this quarter. No = the customer remained with the company. Directly related to Churn Value.
        - **Churn Category:** A high-level category for the customer’s reason for churning: Attitude, Competitor, Dissatisfaction, Other, Price. When they leave the company, all customers are asked about their reasons for leaving. Directly related to Churn Reason.
        - **Churn Reason:** A customer’s specific reason for leaving the company. Directly related to Churn Category.
        """,
    )
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("**Dataset review:**")
    st.container(height=20, border=False)
    st.dataframe(data=data)
    
st.container(height=20, border=False)

sec1 = st.container(border=True)
with sec1:
    st.markdown("### What is the geographic distribution of customers in California?")
    
    col1, col2 = st.columns((1,1), gap="small", vertical_alignment="center")
    
    with col1:
        scatter_map_plot1 = get_customers_scatter_map(
            data=cities_density,
            churn_label="No",
            color="blue",
            max_size=5,
            label="Churn : No",
        )
        st.plotly_chart(scatter_map_plot1, key="scatter_map_plot1")
    
    with col2:
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
    
    col1, col2, col3 = st.columns((1,1,1), gap="small")
    
    select_main_category_text = "Select a main category:"
    select_secondary_category_text = "Select a secondary category:"
    with col1:
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
    
    with col2:
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
    
    with col3:
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
    
    col1, col2, col3 = st.columns((1,1,1), gap="small")
    
    select_numeric_feature_text = "Select a numeric feature:"
    select_category_text = "Select a category:"
    with col1:
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
    
    with col2:
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
    
    with col3:
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
    
    col1, col2, col3 = st.columns((1,1,1), gap="small")
    
    with col1:
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
    
    with col2:
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
    
    with col3:
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
    st.container(height=20, border=False)
    
    col1, col2, col3 = st.columns((1,1,1), gap="small")
    
    with col1:
        multivariate_box_plot1_category_axis = st.selectbox(
            label=select_category_text,
            options=categorical_columns,
            index=categorical_columns.index("Internet Service"),
            key="multivariate_box_plot1_category_axis"
        )
        multivariate_box_plot1_numeric = st.selectbox(
            label=select_numeric_feature_text,
            options=numerical_columns,
            index=numerical_columns.index("Satisfaction Score"),
            key="multivariate_box_plot1_numeric"
        )
        multivariate_box_plot1_category_color = st.selectbox(
            label=select_secondary_category_text,
            options=categorical_columns,
            index=categorical_columns.index("Churn Label"),
            key="multivariate_box_plot1_category_color"
        )
        multivariate_box_plot1 = get_multivariate_box_plot(
            data=data,
            category_axis=multivariate_box_plot1_category_axis,
            numeric=multivariate_box_plot1_numeric,
            category_color=multivariate_box_plot1_category_color,
        )
        st.plotly_chart(multivariate_box_plot1, key="multivariate_box_plot1")
    
    with col2:
        multivariate_box_plot2_category_axis = st.selectbox(
            label=select_category_text,
            options=categorical_columns,
            index=categorical_columns.index("Customer Status"),
            key="multivariate_box_plot2_category_axis"
        )
        multivariate_box_plot2_numeric = st.selectbox(
            label=select_numeric_feature_text,
            options=numerical_columns,
            index=numerical_columns.index("CLTV"),
            key="multivariate_box_plot2_numeric"
        )
        multivariate_box_plot2_category_color = st.selectbox(
            label=select_secondary_category_text,
            options=categorical_columns,
            index=categorical_columns.index("Offer"),
            key="multivariate_box_plot2_category_color"
        )
        multivariate_box_plot2 = get_multivariate_box_plot(
            data=data,
            category_axis=multivariate_box_plot2_category_axis,
            numeric=multivariate_box_plot2_numeric,
            category_color=multivariate_box_plot2_category_color,
        )
        st.plotly_chart(multivariate_box_plot2, key="multivariate_box_plot2")
    
    with col3:
        multivariate_box_plot3_category_axis = st.selectbox(
            label=select_category_text,
            options=categorical_columns,
            index=categorical_columns.index("Online Security"),
            key="multivariate_box_plot3_category_axis"
        )
        multivariate_box_plot3_numeric = st.selectbox(
            label=select_numeric_feature_text,
            options=numerical_columns,
            index=numerical_columns.index("Tenure Months"),
            key="multivariate_box_plot3_numeric"
        )
        multivariate_box_plot3_category_color = st.selectbox(
            label=select_secondary_category_text,
            options=categorical_columns,
            index=categorical_columns.index("Online Backup"),
            key="multivariate_box_plot3_category_color"
        )
        multivariate_box_plot3 = get_multivariate_box_plot(
            data=data,
            category_axis=multivariate_box_plot3_category_axis,
            numeric=multivariate_box_plot3_numeric,
            category_color=multivariate_box_plot3_category_color,
        )
        st.plotly_chart(multivariate_box_plot3, key="multivariate_box_plot3")
    
st.container(height=20, border=False)

sec6 = st.container(border=True)
with sec6:
    st.markdown("### How are the numerical indices distributed relative to each other?")
    st.container(height=20, border=False)
    
    col1, col2, col3 = st.columns((1,1,1), gap="small")
    
    select_main_numeric_feature_text = "Select a main numeric feature:"
    select_secondary_numeric_feature_text = "Select a secondary numeric feature:"
    with col1:
        density_heatmap1_main_numeric_feature = st.selectbox(
            label=select_main_numeric_feature_text,
            options=numerical_columns,
            index=numerical_columns.index("Satisfaction Score"),
            key="density_heatmap1_main_numeric_feature"
        )
        density_heatmap1_secondary_numeric_feature = st.selectbox(
            label=select_secondary_numeric_feature_text,
            options=numerical_columns,
            index=numerical_columns.index("Tenure Months"),
            key="density_heatmap1_secondary_numeric_feature"
        )
        density_heatmap1 = get_density_heatmap_plot(
            data=data,
            numeric_x=density_heatmap1_main_numeric_feature,
            numeric_y=density_heatmap1_secondary_numeric_feature
        )
        st.plotly_chart(density_heatmap1, key="density_heatmap1")
    
    with col2:
        density_heatmap2_main_numeric_feature = st.selectbox(
            label=select_main_numeric_feature_text,
            options=numerical_columns,
            index=numerical_columns.index("Number of Referrals"),
            key="density_heatmap2_main_numeric_feature"
        )
        density_heatmap2_secondary_numeric_feature = st.selectbox(
            label=select_secondary_numeric_feature_text,
            options=numerical_columns,
            index=numerical_columns.index("Monthly Charges"),
            key="density_heatmap2_secondary_numeric_feature"
        )
        density_heatmap2 = get_density_heatmap_plot(
            data=data,
            numeric_x=density_heatmap2_main_numeric_feature,
            numeric_y=density_heatmap2_secondary_numeric_feature,
        )
        st.plotly_chart(density_heatmap2, key="density_heatmap2")
    
    with col3:
        density_heatmap3_main_numeric_feature = st.selectbox(
            label=select_main_numeric_feature_text,
            options=numerical_columns,
            index=numerical_columns.index("Avg Monthly GB Download"),
            key="density_heatmap3_main_numeric_feature"
        )
        density_heatmap3_secondary_numeric_feature = st.selectbox(
            label=select_secondary_numeric_feature_text,
            options=numerical_columns,
            index=numerical_columns.index("Avg Monthly Long Distance Charges"),
            key="density_heatmap3_secondary_numeric_feature"
        )
        density_heatmap3 = get_density_heatmap_plot(
            data=data,
            numeric_x=density_heatmap3_main_numeric_feature,
            numeric_y=density_heatmap3_secondary_numeric_feature,
        )
        st.plotly_chart(density_heatmap3, key="density_heatmap3")
    
