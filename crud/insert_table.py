import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import get_db_connection

def insert_data():
    conn = get_db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            insert_table_query = "INSERT INTO users(name) VALUES ('Fathima'),('Nasrin'),('Nufida'),('Amina');"
            cursor.execute(insert_table_query)
            conn.commit()
            print("Data inserted into Table 'users' successfully.")
        except Exception as e:
            print(f'An error occured: {e}')
        finally:
            cursor.close()
            conn.close()
insert_data()