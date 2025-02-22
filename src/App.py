import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# Load your customer data
customer_data = pd.read_csv('C:/Users/Rahul/Desktop/Web_App/Data_Science/Customer Segmentation/data/raw/Mall_Customers.csv')

# Check if the 'Cluster' column exists; if not, create it using KMeans
if 'Cluster' not in customer_data.columns:
    kmeans = KMeans(n_clusters=4)
    customer_data['Cluster'] = kmeans.fit_predict(customer_data[['Annual Income (k$)', 'Spending Score (1-100)']])

st.title('Customer Segmentation Analysis')
cluster_option = st.selectbox('Select Cluster to Analyze', customer_data['Cluster'].unique())

filtered_data = customer_data[customer_data['Cluster'] == cluster_option]
st.write(filtered_data)

fig, ax = plt.subplots()
sns.scatterplot(data=filtered_data, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster')
st.pyplot(fig)
