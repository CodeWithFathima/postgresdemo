import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from db import get_db_connection

def delete_user():

    conn = get_db_connection()

    if conn is not None:
        try:
            cursor = conn.cursor()

            user_id = int(input("Enter user ID to delete: "))

            delete_query = """
            DELETE FROM users
            WHERE id = %s;
            """

            cursor.execute(delete_query, (user_id,))

            conn.commit()

            print("User deleted successfully")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()