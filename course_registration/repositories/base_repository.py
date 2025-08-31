import sqlite3
from ..db_init import get_db_connection

class BaseRepository:
    def __init__(self, table_name):
        self.table_name = table_name

    def _execute(self, query, params=(), fetch=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        if fetch == "one":
            result = cursor.fetchone()
        elif fetch == "all":
            result = cursor.fetchall()
        else:
            result = None
        conn.commit()
        conn.close()
        return result

    def get_all(self):
        query = f"SELECT * FROM {self.table_name}"
        return self._execute(query, fetch="all")

    def get_by_id(self, id):
        query = f"SELECT * FROM {self.table_name} WHERE id = ?"
        return self._execute(query, (id,), fetch="one")

    def delete(self, id):
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self._execute(query, (id,))
