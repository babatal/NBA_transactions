# streamlit_app.py

import streamlit as st
import psycopg2
import pandas as pd

def create_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="nba_transactions",
        user="postgres",
        password="root",
    )
    return connection

def main():
    st.title("Latest NBA Transactions by Team")
    
    # Connect to the database
    connection = create_connection()
    cursor = connection.cursor()


    option = st.selectbox(
        'Select one team', pd.read_sql("SELECT displayname FROM teams;", connection)
    )

    st.write('You selected:', option)


    # Query data from the database
    cursor.execute(f"SELECT * FROM transactions WHERE team_name = '{option}';")
    data = cursor.fetchall()
    df_data = pd.DataFrame(data, columns=['Transaction Date', 'Team', 'Description'])

    # Display the data
    st.table(df_data)

    # Close the database connection
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
