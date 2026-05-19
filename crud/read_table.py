import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import get_db_connection

def read_user_table():
    conn = get_db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            read_table_query = 'SELECT * FROM users;'
            cursor.execute(read_table_query)
            conn.commit()
            print("read users table successfully.")
            row=cursor.fetchall()
            for i in row:
                print(i)
        except Exception as e:
            print(f'An error occured: {e}')
        finally:
            cursor.close()
            conn.close()
read_user_table()