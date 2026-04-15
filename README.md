# Dynamic Synthetic Data Dashboard

## Overview

This project implements an interactive dashboard for exploring synthetic data using Streamlit.

The dashboard provides dynamic visualizations of a large synthetic dataset (750,000 rows) with features for filtering, real-time data refresh, and multiple chart types including histograms, scatter plots, box plots, and bar charts.

## Features

- **Interactive Filters**: Filter data by category (A, B, C) and date range
- **Real-Time Data Refresh**: Automatic cache refresh every 10 minutes or manual refresh button
- **Multiple Visualizations**:
  - Distribution histogram of values by category
  - Scatter plot showing value trends over time
  - Box plot for statistical analysis by category
  - Bar chart showing record counts per category
- **Key Metrics Display**: Shows total rows, average value, and maximum value
- **Responsive Layout**: Wide layout optimized for data exploration

## Dataset

The synthetic dataset includes:
- **id**: Unique identifier for each record
- **timestamp**: DateTime from January 1, 2024, with minute-level granularity
- **Category**: Categorical variable with values A, B, or C
- **value**: Random float values between 0-100

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure the `synthetic_data.csv` file is in the same directory as `app.py`
2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
3. Open your browser to the provided local URL (typically http://localhost:8501)
4. Use the interactive filters in the sidebar to explore the data
5. Click "Refresh Data" to reload the dataset

## Files

- `app.py`: Main Streamlit application code
- `Data_setup_code3.ipynb`: Jupyter notebook for generating the synthetic dataset
- `requirements.txt`: Python package dependencies
- `synthetic_data.csv`: Generated synthetic dataset (750,000 rows)
- `README.md`: This documentation file

## Dependencies

- pandas
- streamlit
- numpy
- matplotlib
- seaborn
- plotly

## Course Context

This project demonstrates:
- Handling large datasets efficiently
- Implementing interactive dashboards
- Real-time data simulation
- Multiple visualization techniques
- User-driven data exploration

## Performance Notes

The application uses Streamlit's caching mechanism to optimize performance with large datasets. Data is cached for 10 minutes to balance freshness with computational efficiency.
