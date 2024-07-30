import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
import urllib.parse

# Database connection details
host = "localhost"
user = "root"
password = "Nagunaveen@143"
database = "bus"
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
def fetch_data_as_list(query, state=None):
    with engine.connect() as connection:
        res = connection.execute(text(query))
    return [row[0] for row in res]

# Streamlit app layout
st.title('RedBus Data')

# Sidebar filters
st.sidebar.header('Filters')

# Fetch distinct state of bus
state_of_bus_query = "SELECT DISTINCT state_of_bus FROM redbus_prj"
try:
    state_of_bus_list = fetch_data_as_list(state_of_bus_query)
except Exception as e:
    st.sidebar.error(f"Error fetching states of bus: {e}")
    state_of_bus_list = []


# Fetch distinct bus types
bus_type_query = "SELECT DISTINCT filtered_bus_types FROM redbus_prj"
try:
    bus_type_list = fetch_data_as_list(bus_type_query)
except Exception as e:
    st.sidebar.error(f"Error fetching bus types: {e}")
    bus_type_list = []

# Fetch distinct seat availabilities
bus_seat_availability_query = "SELECT DISTINCT seat_availability FROM redbus_prj"
try:
    bus_seat_list = fetch_data_as_list(bus_seat_availability_query)
except Exception as e:
    st.sidebar.error(f"Error fetching seat availabilities: {e}")
    bus_seat_list = []

# Sidebar filter widgets
state_of_bus = st.sidebar.selectbox('Select State of Bus', options=state_of_bus_list)

# Fetch distinct bus routes
bus_route_query = f"SELECT DISTINCT bus_route_name FROM redbus_prj where state_of_bus = '{state_of_bus}'"
try:
    bus_route_list = fetch_data_as_list(bus_route_query, state=state_of_bus)
except Exception as e:
    st.sidebar.error(f"Error fetching bus routes: {e}")
    bus_route_list = []

route = st.sidebar.selectbox('Select Route', options=bus_route_list)
bustype = st.sidebar.selectbox('Select Bus Type', options=bus_type_list)
price_range = st.sidebar.selectbox(
    'Select Price Range',
    options=[
        '<500',
        '500 - 1000',
        '1000 - 2000',
        '2000 - 3000',
        '3000 - 4000'
    ]
)
contains_ac = st.sidebar.radio('AC Bus', options=['Yes', 'No'])
star_rating_range = st.sidebar.selectbox(
    'Select Star Rating',
    options=[
        '<3.00',
        '3.00 - 4.00',
        '4.00 - 5.00'
    ]
)

# Set price range based on user selection
if price_range == '<500':
    price_min, price_max = 0, 500
elif price_range == '500 - 1000':
    price_min, price_max = 500, 1000
elif price_range == '1000 - 2000':
    price_min, price_max = 1000, 2000
elif price_range == '2000 - 3000':
    price_min, price_max = 2000, 3000
elif price_range == '3000 - 4000':
    price_min, price_max = 3000, 4000

# Set star rating range based on user selection
if star_rating_range == '<3.00':
    star_rating_min, star_rating_max = 0.0, 3.0
elif star_rating_range == '3.00 - 4.00':
    star_rating_min, star_rating_max = 3.0, 4.0
elif star_rating_range == '4.00 - 5.00':
    star_rating_min, star_rating_max = 4.0, 5.0

# SQL query with filters
query = f"""
SELECT *
FROM redbus_prj
WHERE state_of_bus = '{state_of_bus}'
AND bus_route_name = '{route}'
AND filtered_bus_types = '{bustype}'
AND contains_ac = '{contains_ac}'
AND new_star_rating BETWEEN {star_rating_min} AND {star_rating_max}
AND price_numeric BETWEEN {price_min} AND {price_max}
"""

# Fetch and display data
try:
    data = fetch_data(query)
    #st.write("### Filtered Results")
    #st.write("#### Columns in DataFrame:")
    #st.write(data.columns.tolist())  # Display columns for debugging
    if not data.empty:
        
        # data['reaching_time_minutes'] = data['reaching_time_minutes'].astype(int)
        st.dataframe(data)
    else:
        st.write("### No data available for the selected filters.")
except Exception as e:
    st.error(f"Error fetching data: {e}")
