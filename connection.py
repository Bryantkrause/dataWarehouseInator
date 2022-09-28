import mysql.connector
from mysql.connector import Error
import pandas as pd
from dotenv import load_dotenv
import os
from pandas.io import sql
from sqlalchemy import create_engine

# get super secret information
load_dotenv('.env')
db = os.environ.get("database")
pw = os.environ.get("pw")
df = pd.DataFrame



# engine = create_engine(f'mysql://root:{pw}@localhost/{db}')
# create connection to db
def create_server_connection(host_name, user_name, user_password, db):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

# connection to db
connection = create_server_connection("localhost", "root", pw, db)

# db creation
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


create_database_query = f"CREATE DATABASE {db}"
# create_database(connection, create_database_query)


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

create_Approvertable = """


"""







