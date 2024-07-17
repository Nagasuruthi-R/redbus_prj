import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
import urllib.parse

# Database connection details
host = "localhost"
user = "test"
password = "Nagunaveen@143"
database = "bus_informations"
password_encoded = urllib.parse.quote_plus(password)
DATABASE_URL = f"mysql+pymysql://{user}:{password_encoded}@{host}/{database}"

# Create an engine instance
engine = create_engine(DATABASE_URL)

# Function to fetch data from the database
def fetch_data(query):
    with engine.connect() as connection:
        result = connection.execute(text(query))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
    return df

# Function to fetch distinct values as a list
def fetch_data_as_list(query):
    with engine.connect() as connection:
        res = connection.execute(text(query))
    return [row[0] for row in res]

# Streamlit app layout
st.title('RedBus Data Filtering')

# Fetch distinct bus routes
bus_route_query = "SELECT DISTINCT bus_route_name FROM redbus_new_table"
try:
    bus_route_list = fetch_data_as_list(bus_route_query)
except Exception as e:
    st.error(f"Error fetching bus routes: {e}")
    bus_route_list = []

# Fetch distinct bus types
bus_type_query = "SELECT DISTINCT bus_types_ss FROM redbus_new_table"
try:
    bus_type_list = fetch_data_as_list(bus_type_query)
except Exception as e:
    st.error(f"Error fetching bus types: {e}")
    bus_type_list = []

# Fetch distinct seat availabilities
bus_seat_availability_query = "SELECT DISTINCT seat_availability FROM redbus_new_table"
try:
    bus_seat_list = fetch_data_as_list(bus_seat_availability_query)
except Exception as e:
    st.error(f"Error fetching seat availabilities: {e}")
    bus_seat_list = []

# Filters
col1, col2, col3 = st.columns(3)
with col1:
    route = st.selectbox('Select Route', options=bus_route_list)
with col2:
    bustype = st.selectbox('Select Bus Type', options=bus_type_list)
with col3:
    price_range = st.slider('Select Price Range', 0, 5000, (100, 2000))

col4, col5 = st.columns(2)
with col4:
    contains_ac = st.radio('AC Bus', options=['Yes', 'No'])
with col5:
    star_rating = st.slider('Select Star Rating', 0.0, 5.0, (3.0, 5.0))

#seat_availability = st.selectbox('Select Availability', options=bus_seat_list)

# SQL query with filters
query = f"""
SELECT *,
TIME_TO_SEC(reaching_time) / 60 AS reaching_time_minutes
FROM redbus_new_table
WHERE bus_route_name = '{route}'
AND bus_types_ss = '{bustype}'
AND contains_ac = '{contains_ac}'
AND star_rating BETWEEN {star_rating[0]} AND {star_rating[1]}
AND price BETWEEN {price_range[0]} AND {price_range[1]}
"""

# Debug the query
# st.write(f"SQL Query: {query}")

# Fetch and display data
try:
    data = fetch_data(query)
    # Convert price and reaching_time_minutes columns to integer
    if not data.empty:
        #data['price'] = data['price'].astype(int)
        data['reaching_time_minutes'] = data['reaching_time_minutes'].astype(int)
        st.write("### Filtered Results")
        st.dataframe(data)
    else:
        st.write("### No data available for the selected filters.")
except Exception as e:
    st.error(f"Error fetching data: {e}")

# Display filtered columns on the side
st.sidebar.write("Filtered Columns:")
if not data.empty:
    st.sidebar.write(data[['bus_route_name', 
                           'reaching_time', 
                           'price', 
                           'seat_availability']])
