import os
from typing import List, Union, Dict

import sqlite3

BASE = os.path.dirname(__file__)
DEFAULT_DB_PATH = os.path.join(BASE, "data_sqlite3.db")

def create_connection(db_file_path):
    conn = sqlite3.connect(db_file_path)
    return conn

def execute_command(query, *args):
    conn = create_connection(DEFAULT_DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    conn.close()

def execute_fetch(query, *args):
    conn = create_connection(DEFAULT_DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query, args)
    data = cursor.fetchall()
    conn.close()
    return data


class Database:
    def __init__(self, tables:Dict):
        """
        tables[table]
        table = Dict
        
        {
            name: table_name
            columns: {
                column: sqlite datatype,
                ...
                ...
            }
        }
        """
        self.tables = tables
        self._create_tables()

    def _create_tables(self):
        for table in self.tables:
            cols_query = ",".join([(k+" "+v) for k, v in table["columns"].items()])
            query = f"""CREATE TABLE IF NOT EXISTS {table["name"]}(
                {cols_query}
            );"""
            execute_command(query)
    
    def add_record(self, table, column_names, record_tuple):
        columns = ",".join(column_names)
        values = ",".join(["?"]*len(column_names))
        query = f"""INSERT INTO TABLE {table}({columns}) VALUES({values})"""
        execute_command(query, record_tuple)
    
    def get_ui_data(self):
        query = f"""SELECT * FROM ui_data"""
        data = execute_fetch(query)
        for row in data:
            print(row)

def create_new_tables():
    db_schema = [
        {
            "name": 'ui_data',
            "columns": {
                "id": "integer primary key autoincrement",
                "field_name": "text",
                "value": "text"
            }
        }, 
        {
            "name": "path_management",
            "columns": {
                "id": "integer primary key autoincrement",
                "field": "text",
                "value": "text"
            }
        },
        {
            "name": "subject_records",
            "columns": {
                "id": "integer primary key autoincrement",
                "sub_name": "text",
                "hours_studied": "text",
                "days_spent": "integer"
            }
        }
    ]
    db = Database(db_schema)
    db.get_ui_data()


if __name__ == "__main__":
    create_new_tables()