import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from db import get_db_connection

def read_user_table():

    conn = get_db_connection()

    if conn is not None:
        try:
            cursor = conn.cursor()

            select_query = "SELECT * FROM users;"

            cursor.execute(select_query)

            rows = cursor.fetchall()

            print("\nUsers Table Data:\n")

            for row in rows:
                print(row)

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()