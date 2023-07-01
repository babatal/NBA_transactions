# Data Engineering NBA Latest Transactions Project

![image](https://github.com/babatal/NBA_transactions/assets/94752515/1fc2ec2b-9935-447c-ba8c-445bd31e9708)

## Overview

This project aims to provide a convenient way to keep track of the latest NBA player transactions. It involves three main steps: data extraction, data transformation, and data loading. The extracted data is transformed using pandas and loaded into a PostgreSQL database. This web app extends the project by visualizing the loaded data using Streamlit, making it easy to explore and analyze the transactions.

## Technologies Used
* Python
* Pandas
* Insomnia API
* PostgreSQL
* Streamlit

## Data Extraction
The data extraction step involves scraping the latest NBA transactions from ESPN's website. I have used 'requests' Library to interact with hidden API (image down below), fetch the data from the specific page on ESPN and obtain the relevant information, such as player names, teams involved, and transaction details. The extracted data is then ready for further processing.

### Hidden api
![image](https://github.com/babatal/NBA_transactions/assets/94752515/8d7695a8-5b6a-45bb-a082-dc40338af91b)


## Data Transformation
In this step, I have utilize pandas to clean and transform the extracted data into a structured format. I have handle any missing or inconsistent data, convert data types as needed, and organize the information into a well-defined tabular structure. This ensures that the data is consistent and ready for loading into the database.

## Data Loading
The last step of the process involves loading the transformed data into a PostgreSQL database. I've establish a connection to the PostgreSQL server using psycopg2 and insert the data into a designated table. The database acts as a centralized repository for all the latest NBA transactions, providing an efficient and organized way to access and analyze the data.

## Data Visualization with Streamlit
To provide an interactive and user-friendly way to explore the latest NBA transactions, I've built a Streamlit web app. Streamlit connects to the PostgreSQL database and retrieves the latest data. It then visualizes the transactions using selectbox, allowing users to customize their view based on their choice.


https://github.com/babatal/NBA_transactions/assets/94752515/784fb21e-48ac-46a5-931d-0caa819718dd

