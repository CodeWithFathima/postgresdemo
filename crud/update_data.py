import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from db import get_db_connection

def update_user_table():

    conn = get_db_connection()

    if conn is not None:
        try:
            cursor = conn.cursor()

            user_id = int(input("Enter user ID to update: "))
            new_name = input("Enter new name: ")

            update_query = """
            UPDATE users
            SET name = %s
            WHERE id = %s;
            """

            cursor.execute(update_query, (new_name, user_id))

            conn.commit()

            print("Data updated successfully")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()