import streamlit as st
import pandas as pd
from datetime import datetime,timedelta
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

#--- Configuration ---
st.set_page_config(layout="wide",page_title="Dynamic Data Dashboard")

#--- Function to load Data ---
@st.cache_data(ttl=600) # Cache data for 10 minutes
def load_data():
    data=pd.read_csv('synthetic_data.csv')
    data['timestamp']=pd.to_datetime(data['timestamp'])
    st.success("Data loaded successfully")
    return data

#--- Main Application ---
st.title("Dynamic Synthetic Data Dashboard")
st.markdown("An interactive dashboard to explore synthetic data with various visualizations and filters.")

# Refresh button
if st.button("Refresh Data"):
   st.cache_data.clear() # Clear cache to force reload
   st.rerun() # Rerun the app to apply the new data

data=load_data()

st.subheader("Data Overview")
st.write(f'Total rows in dataset: {len(data):,}')

#--- Interactive Widgets ---
st.subheader("Interactive Filters")

# Category filter
available_categories=['All']+sorted(data['Category'].unique().tolist())
selected_category=st.selectbox("Select Category",available_categories, key='category_filter')

# Date Range Slider
min_date = data['timestamp'].min().to_pydatetime().date()
max_date = data['timestamp'].max().to_pydatetime().date()

date_range = st.slider(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
    format="YYYY-MM-DD",
    key='date_range_slider'
)

# Apply filters
filtered_data = data.copy()
if selected_category!='All':
    filtered_data = filtered_data[filtered_data['Category']==selected_category]

filtered_data = filtered_data[
    (filtered_data['timestamp'].dt.date >= date_range[0]) &
    (filtered_data['timestamp'].dt.date <= date_range[1])
]

st.write(f'Filtered rows: {len(filtered_data):,}')
st.dataframe(filtered_data.head())


#--- Display Key Metrics ---
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Number of Rows", f"{len(filtered_data):,}")
with col2:
    st.metric("Average Value", f"{filtered_data['value'].mean():.2f}")
with col3:
    st.metric("Max Value", f"{filtered_data['value'].max():.2f}")

#--- Visualizations ---
st.subheader("Data Visualizations")

# Histogram of 'value' (Distribution) 
st.write("#### Distribution of 'Value' by Category")
fig_hist = px.histogram(filtered_data,
                        x='value',
                        color='Category',
                        marginal='box',
                        title='Distribution of Value',
                        labels={'value': 'Value', 'count': 'Frequency'},
                        color_discrete_map={'A':'blue', 'B':'orange', 'C':'green'}
                       )
fig_hist.update_layout(bargap=0.1, yaxis_title="Count")
st.plotly_chart(fig_hist, use_container_width=True)


# Scatter Plot: 'timestamp' vs 'value' 
st.write("#### Value Over Time by Category")
fig_scatter = px.scatter(filtered_data,
                         x='timestamp',
                         y='value',
                         color='Category',
                         title='Value Over Time',
                         labels={'timestamp': 'Timestamp', 'value': 'Value'},
                         hover_data=['id'], # Add 'id' to hover information
                         color_discrete_map={'A':'blue', 'B':'orange', 'C':'green'}
                        )
st.plotly_chart(fig_scatter, use_container_width=True)


#  Box Plot of Value by Category 
st.write("#### Box Plot of Value by Category")
fig_box = px.box(filtered_data,
                 x='Category',
                 y='value',
                 color='Category',
                 title='Box Plot of Value by Category',
                 labels={'value': 'Value', 'Category': 'Category'},
                 color_discrete_map={'A':'blue', 'B':'orange', 'C':'green'}
st.plotly_chart(fig_box, use_container_width=True)


#  Bar Chart: Count of each Category 
st.write("#### Count of Records per Category")
category_counts = filtered_data['Category'].value_counts().reset_index()
category_counts.columns = ['Category', 'Count']

fig_bar_mpl, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Category', y='Count', data=category_counts, palette='viridis', ax=ax,hue='Category')
ax.set_title('Count of Records per Category')
ax.set_xlabel('Category')
ax.set_ylabel('Count')
st.pyplot(fig_bar_mpl)

st.sidebar.header("Dashboard Information")
st.sidebar.info("This dashboard displays synthetic data, allowing exploration of distributions and relationships. Data is refreshed every 10 minutes or on button click.")
