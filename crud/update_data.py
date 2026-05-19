import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import get_db_connection

def update_user_table():
    conn = get_db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            update_table_query = "UPDATE users SET name = 'Nazriya' where name = 'Nasrin';"
            cursor.execute(update_table_query)
            conn.commit()
            print("user updated successfully.")
        except Exception as e:
            print(f'An error occured: {e}')
        finally:
            cursor.close()
            conn.close()
update_user_table()