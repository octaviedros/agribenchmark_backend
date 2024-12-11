# update_schema.py
 
import psycopg2
from config import username, password, \
    dialect, server, db
uri = f"host='localhost' dbname='{db}' user='{username}' password='{password}'"

 
def update_schema(sql_file_path):

    try:

        # Read the .sql file

        with open(sql_file_path, 'r') as file:

            sql_commands = file.read()
 
        # Establish a connection to the database

        conn = psycopg2.connect(

            uri

        )

        # Create a new database session and return a new instance of the connection class

        cursor = conn.cursor()
 
        # Execute the SQL commands

        cursor.execute(sql_commands)

        conn.commit()
 
        print("Schema updated successfully.")
 
    except Exception as error:

        print(f"Error updating schema: {error}")

    finally:

        # Close the database connection

        if conn:

            cursor.close()

            conn.close()
 
if __name__ == "__main__":

    # Path to your .sql schema file

    sql_file_path = './agribenchmark_schema.sql'

    update_schema(sql_file_path)
