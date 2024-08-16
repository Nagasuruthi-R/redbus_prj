# Real-time Dynamic Red Bus Project
This project extracts, stores and analyses real-time bus data from the red-bus website using Selenium, Mysql and Streamlit. It ensures up-to-date data and interactive visualization for enhanced user experience. This project integrates web scraping, database management and dynamic filtering.
REDUBUS DATA SCRAPING WITH SELENIUM AND DYNAMIC FILTERING USING STREAMLIT
## Project Index
1.	Introduction
2.	Overview
•	Data Scraping
•	Data Storage
•	Interactive Data Filtering
3.	Tools Used
4.	Problem Statement
5.	Data Scraping Workflow
6.	DataFrame to Database
7.	Data Cleaning and Transformation in MySQL
8.	Streamlit application
9.	Key Components
10.	 Conclusion
                
## Introduction:
	Red-Bus web scraping project aims to extract bus routes information from the red bus website from at least 10 state bus details to store the data in a structured format and provide filtering options using streamlit.
## Overview:
1. Data Scraping: Extracting bus route information such as route names, bus names, bus types from red bus website
2. Data Storage: Storing the scraped data in a Mysql Database.
3. Interactive Data Filtering: Using Streamlit to create as user interface for filtering and viewing the Data
## Tools Used:
1. Web Scraping using Selenium
2. Python Programming
3. Streamlit Application Development
4. SQL Database Management.
## Problem Statement:
	The “Red-bus Data Scraping and Filtering with Streamlit Application” aims to revolutionize the transportation industry by providing a comprehensive solution for  collecting, analyzing and visualizing bus travel data. By utilizing selenium for web-scraping, this project automates the extraction of detailed information from Red-Bus, including bus_routes, schedules, prices, and seat_availability. By streamlining data collection providing powerful tools for data-driven decision making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.
Data Scraping:
### 1 . Data Scraping Workflow:
#### Imported libraries: 
1. Webdriver: Controls the browser.
2. By: Locates elements on the page.
3. Keys: Simulates keyboard actions.
4. WebDriverWait: Waits for conditions to be met before proceedings.
5. expected_conditions: Conditions to wait for.
6. Time: Adds delays to handle page load times.
#### Created function to extract data:
1. Extracts data from the current page and finds elements using XPATH and collects their text content
2. Return: a dictionary with lilsts of extracted data.
#### Created a function to click button and extract data:
1. Clicks a button and waits for new content to load and scrolls down to extract data.
2. Exception Handling: If the button click fails, it returns empty data.
3. Scrolling: Continues until a maximum number of attempts and until no new data is found.
#### Created a function to navigate and extract links:
1. Navigate through paginations, click on pages and extract bus_route_links.
2. Paginations: Handle multiple pages by scrolling and clicking page elements.
3. Error Handling: catches error related to navigation and link extractions.
#### Main Executiion:
1. Run the flow by initializing the driver, extracting links and then visiting each link to extract detailed data.
2. Final Output: Collects and prints the final results.
### DataFrame to Database:
#### Importing libraries:
1. pandas: A powerful data analysis library used for handling data structures and operations for manipiulating numerical tables and time series.
2. glob: Not used in the code but typically used for file pattern matching.
#### Defining file_paths:
1. Lists the file paths of all excel files that I want to combine. This paths should point to the locations of my files.
2. Reading excel files into DataFrames:
#### Read each excel files into separate DataFrame and stores them in a list.
1. pd.read_excel(file): Reads the excel files at the path file in the DataFrame.
#### Combining DataFrames:
1. Concatenate all DataFrames in the list DataFrames into a single DataFrame.
2. pd.concat(dataframe): Aranges the DataFrames vertically (ie., rows from each df are added to one after another)
#### List comprehension:
1. Iterates a each file paths in file_paths, reads the file into a DataFrame and collects this DataFrames into a list.
2. Resetting the Index:
Resets the index of the combined DataFrames to ensure  it is sequential from 0.
Drop = True: Ensures that old index is not added as a column in the DataFrame.
#### Connecting to Mysql and creating the table and described:
1. Uses ‘mysql.connector.connect()’ to establish a connection.
2. Checks if the connection is successful and prints the connection message.
#### Creating a table:
1. Creates the ‘redbus’ table with the specified columns if it does not already exists.
2. Uses ‘create table if not exists’ avoid errors if the table exists.
#### Reading data from excel and load into Mysql:
1. Used pandas to read data from an excel file (‘read_excel’),
2. Uses SQLAlchemy to create an engine and load the data into the redbus table with ‘to_sql’.
3. The ‘If_exists=’replace’’ argument replaces the table if it exists, which ensures that the table will be overwritten with the new data.
### Data cleaning in Mysql:
#### Data Cleaning and Categorization:
1. Bus_type categorization: (used case , when and then syntax)
2. contains_ac: categorizes ‘yes’ if bus has AC otherwise ‘no’.
3. bus_type_ss: categorizes ‘seater’, ‘sleeper’, ‘other_type’.
4. Time format Transformation: (used case and when syntax with str_to_datetime)
5. creating a new table ‘redbus_prj’ with transformed time format .
6. t_departing_time and t_reaching_time: Converts departing_time into time format and ensures that it follows ‘HH’ format.
7. Converting star rating as float: Converted ‘new_star_rating’ into a float format and ensuring consistency in rating values.(used cast syntax).
### Streamlit Application:
1. Database Connection: Establish a connection to the MySQL database using SQLAlchemy.
2. Streamlit App Layout: Design an interactive web app for filtering and displaying data.
#### Data Fetching Functions:
1. ‘fetch_data(query)’: Executes a SQL query to fetch data from the MySQL database and returns it has a pandas DataFrame.
2. ‘fetch_data_as_list(query)’: Execute a SQL query to fetch distinct values from a column and returns them as a list.
#### Streamlit App Implementation:
1. Title and Filters:
2. Distinct Values Fetching: Use SQL queries to fetch distinct values for bus route, bus types, and seat availability.
#### Filters:
1. State_selectiion: Drop –down menu for selecting a bus route.
2. Route Selection: Drop –down menu for selecting a bus route.
3. Bus Type Selection: Drop –down menu for selecting a bus type.
4. Price Range: Selectbox to select the price range.
5. AC Bus: Radio buttons to filter for AC and non-AC buses.6
6. Star Rating: Selectbox to filter based on star rating.
#### SQL Query Construction:
1. Constructed a SQL query based on selected filters to retrieve data from the MySQL database.
#### Data Display:
1. Fetch data using constructed SQL query.
2. Convert relevant column to appropriate data types.
3. Display the filtered results in a DataFrame.
4. Show a message if no data is available for the selected filters.
### Key Components:
1. Selenium Webdriver: Used for web scraping and dynamic interaction with web pages.
2. WebDriverWait and ExpectedConditions: Employed to handle dynamic page elements and pagination.
3. JavaScript Execution: Utilized to scroll and click on elements for loading more data.
4. XPATH Queries: Applied for precise extraction of desired data attributes.
5. Pandas DataFrame Conversion and Cleaning: Structured storage and consolidation of scraped data into a single DataFrame with steps to handle missing values and clean text data.
6. Database Connection: Utilizes SQLAlchemy to establish a connection to the MySQl database.
7. Streamlit Filters: Provides interactive filters for users to select bus route, type, price range, AC status and star rating.
### Streamlit app layout:

 ![streamlit_layout](https://github.com/user-attachments/assets/2cd87e3c-e22f-41be-885b-656beb4fabd7)


### Conclusion:

1. Harnessing the power of web scraping and data transformation, we seamlessly integrated real them in the Mysql database.
2. Enabling interactive user experience through streamlit.
3. This innovative approach ensures accurate and up-to-date bus informations is always at your fingertips. 
