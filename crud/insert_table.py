import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from db import get_db_connection

def insert_data():

    conn = get_db_connection()

    if conn is not None:
        try:
            cursor = conn.cursor()

            name = input("Enter name: ")

            insert_query = """
            INSERT INTO users(name)
            VALUES (%s);
            """

            cursor.execute(insert_query, (name,))

            conn.commit()

            print("Data inserted successfully")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()