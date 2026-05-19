import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import get_db_connection

def delete_user():
    conn = get_db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            delete_data_query = "DELETE FROM users WHERE id=8;"
            cursor.execute(delete_data_query)
            conn.commit()
            print("Data deleted successfully.")
        except Exception as e:
            print(f'An error occured: {e}')
        finally:
            cursor.close()
            conn.close()
delete_user()