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
•	Data Scraping: Extracting bus route information such as route names, bus names, bus types from red bus website
•	Data Storage: Storing the scraped data in a Mysql Database.
•	Interactive Data Filtering: Using Streamlit to create as user interface for filtering and viewing the Data
## Tools Used:
•	Web Scraping using Selenium
•	Python Programming
•	Streamlit Application Development
•	SQL Database Management.
## Problem Statement:
	The “Red-bus Data Scraping and Filtering with Streamlit Application” aims to revolutionize the transportation industry by providing a comprehensive solution for  collecting, analyzing and visualizing bus travel data. By utilizing selenium for web-scraping, this project automates the extraction of detailed information from Red-Bus, including bus_routes, schedules, prices, and seat_availability. By streamlining data collection providing powerful tools for data-driven decision making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.
Data Scraping:
### 1 . Data Scraping Workflow:
•	State-wise link extraction: Begin by extracting separate state links from the Red-Bus website to streamline the process of gathering specific-route data.
•	Route URL Iteration: Iterated through each state-wise extracted links. And for each route URL, initialize Selenium’s Chrome Webdriver and navigate to the all bus URL from that specified state URL.
•	Dynamic Scrolling: Implemented a loop that scrolls down the page (using the PAGE_DOWN key) to load additional data dynamically.
Used a maximum scroll attempt limit and timeouts to manage data loading effectively
•	XPATH Queries for Data Extraction: Extracted elements such as bus types, durations, departure time, reaching time, bus route names, bus route links, seats availability, prices, star-ratings using XPATH queries. 
Append the extracted data to respective lists that accumulate information from each scroll attempt.
•	Data Loading Management: Compare the current count of loaded elements with the previous count to determine if new data has been loaded, guiding whether to continue scrolling.
•	Result Storage: Construct a dictionary (‘res’) containing the list of scraped attributes for each route.
Include metadata like bus route name and link in the dictionary.
Append each ‘res’ dictionary to a final list (‘final_output’) after completing the data extraction for each route.
Quit the webdriver session after processing each state’s route URL 
### 2. Pagination Handling: 
•	Use ‘WebDriverWait’ to handle pagination element on the red-bus website, ensuring all pages of data are accessed and extracted.
### 3. Final Output:
•	The ‘final_output’ list will store dictionaries, each representing data scrapped from one bus route
•	Each dictionary will include various attributes such as bus names, bus types, durations, departure time, reaching time, star ratings, prices, seat availability.
## DataFrame to Database:
### 1. DataFrame Conversion:
•	Convert the ‘final_output’ list of dictionaries into a pandas DataFrame for further analysis:
•	Initialize an empty list ‘dfs’ to store individual DataFrames.
•	Iterate through each dictionary in ‘final_output’, convert it into DataFrame using ‘pd.series’, and append it to ‘dfs’.
•	Concatenate all individual DataFrames in ‘dfs’ into a single DataFrame ‘final_df’ using ‘pd_concat’ with ‘ignore_index=True”.
### 2. Data Cleaning:
•	Replace empty strings in ‘final_df’ with ‘pd.NA’ to handle missing values appropriately.
•	Drop any row that contains NaN values to ensure the dataset is complete and reliable.
•	Replace newline characters in string columns with spaces to clean up text data.
### 3. Combining Data from Excels:
•	Combining data from multiple Excel files containing bus route details into single DataFrame
•	Create a list of file paths of all Excel files.
•	Read each file into a DataFrame and store them in a list.
•	Concatenate all DataFrames in the list into a single DataFrame.
•	Reset the index of combined DataFrame.
•	Save the combined DataFrame to an Excel file.
 
### 4. Creating MySQL Table: 
•	Connect to a MySQL database and create a table to store the bus route details.
•	Establish a connection to the MySQL database.
•	Execute a SQL query to create a table with appropriate columns for storing bus route information.
•	Print confirmation messages for successful connection and table creation.
•	For clarification , I described the table in SQL query and attached below

 
### 5. Loading Data into MySQL:
•	Load the combined DataFrame into the MySQL database using SQLAlchemy
•	Create a connection string for the MySQL database.
•	Use ‘pandas’ and ‘SQLAlchemy’ to read the combined excel file and load it into the MySQL database.
•	Print a confirmation message upon successful data loading.
## Data Cleaning and Transformation in MySQL:
### 1. Data Cleaning and Categorization:
1.	Bus_type categorization: (used case , when and then syntax)
1.	contains_ac: categorizes ‘yes’ if bus has AC otherwise ‘no’.
2.	bus_type_ss: categorizes ‘seater’, ‘sleeper’, ‘semi sleeper’, ‘semi seater’.
2.	Time format Transformation: (used case and when syntax with str_to_datetime)
•	creating a new table ‘newbus_route’ with transformed time format . 
•	t_departing_time and t_reaching_time:  Converts departing_time  into time format and ensures that it follows ‘HH’ format.
•	Converting star rating as float: Converted ‘standardized_star_rating’ into a float format and ensuring consistency in rating values.(used cast syntax)
## Streamlit Application:
### 1. Database Connection: Establish a connection to the MySQL database using SQLAlchemy.
### 2. Streamlit App Layout: Design an interactive web app for filtering and displaying data.
### 3. Data Fetching Functions: 
•	‘fetch_data(query)’: Executes a SQL query to fetch data from the MySQL database and returns it has a pandas DataFrame.
•	‘fetch_data_as_list(query)’: Execute a SQL query to fetch distinct values from a column and returns them as a list.
### 4. Streamlit App Implementation:
•	Title and Filters: 
 Distinct Values Fetching: Use SQL queries to fetch distinct values for bus route, bus types, and seat availability.
•	Filters: 
Route Selection: Drop –down menu for selecting a bus route.
Bus Type Selection: Drop –down menu for selecting a bus type.
Price Range: Slider to select the price range.
AC Bus: Radio buttons to filter for AC and non-AC buses.
Star Rating: Slider to filter based on star rating.
### 5. SQL Query Construction:
•	Constructed a SQL query based on selected filters to retrieve data from the MySQL database.
### 6. Data Display:
•	Fetch data using constructed SQL query.
•	Convert relevant column to appropriate data types.
•	Display the filtered results in a DataFrame.
•	Show a message if no data is available for the selected filters.
### 7. Sidebar Display:
•	Display filtered columns such as bus route name, reaching time, price and seat availability in the sidebar for additional context.
 Key Components:
•	Selenium Webdriver: Used for web scraping and dynamic interaction with web pages.
•	WebDriverWait and ExpectedConditions: Employed to handle dynamic page elements and pagination.
•	JavaScript Execution: Utilized to scroll and click on elements for loading more data.
•	XPATH Queries: Applied for precise extraction of desired data attributes.
•	Pandas DataFrame Conversion and Cleaning: Structured storage and consolidation of scraped data into a single DataFrame with steps to handle missing values and clean text data.
•	Database Connection: Utilizes SQLAlchemy to establish a connection to the MySQl database.
•	Streamlit Filters: Provides interactive filters for users to select bus route, type, price range, AC status and star rating.
Streamlit App Layout:
 
## Conclusion:
•	Harnessing the power of web scraping and data transformation, we seamlessly integrated real them in the Mysql database. 
•	Enabling interactive user experience through streamlit.  
•	This innovative approach ensures accurate and up-to-date bus informations is always at your fingertips.
	


   
