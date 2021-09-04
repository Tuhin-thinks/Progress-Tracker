import os
from typing import List, Union, Dict

import sqlite3

import empty_schema
# from . import empty_schema

BASE = os.path.dirname(__file__)
DEFAULT_DB_PATH = os.path.join(BASE, "data_sqlite3.db")


def create_connection(db_file_path):
    conn = sqlite3.connect(db_file_path)
    return conn


def execute_command(query, *args):
    conn = create_connection(DEFAULT_DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query, *args)
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
    def __init__(self, tables: Dict):
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
            cols_query = ",".join([(k+" "+v)
                                  for k, v in table["columns"].items()])
            query = f"""CREATE TABLE IF NOT EXISTS {table["name"]}(
                {cols_query}
            );"""
            execute_command(query)

    def add_record(self, table, column_names, record_tuple):
        columns = ",".join(column_names)
        values = ",".join(["?"]*len(column_names))
        query = f"""INSERT INTO {table}({columns}) VALUES({values})"""
        execute_command(query, record_tuple)

    def get_ui_data(self):
        query = f"""SELECT * FROM ui_data"""
        data = execute_fetch(query)
        data_dict = {}
        for row in data:
            """
            row[0] => id
            row[1] => field_name
            row[2] => value
            """
            data_dict[row[1]] = row[2]
        return data_dict
    
    def get_subject_names(self):
        """
        To get only subject names from subject_records database
        """
        query = """SELECT sub_name FROM subject_records"""
        data = execute_fetch(query)
        subjects = []
        for name in data:
            subjects.append(name[0])
        return subjects
    
    def get_subject_data(self, sub_name:str, fields: Union[str, List]):
        """
        To a mentioned column data in subject_records db
        """
        field_query = "?"
        if type(fields) == list:
            field_query = ",".join(["?"]*len(fields))
        query = f"""SELECT ? from subject_records where sub_name=?"""
        args = (field_query, sub_name)

        return execute_fetch(query, args)

    def update_subject_study_hours(self, subject_name:str, hours=None, days=None):
        if not any((hours, days)):
            raise ValueError("hours and days both cannot be empty")
        
        # TODO: check if the subject actually exists and get it's hours and days data
        
        # TODO: add hours and days data with the current data and udate in the table

        query = f"""UPDATE subject_records
                        SET hours_studied=?,
                        SET days_spent=?
                    WHERE
                        subject_name=?"""
        args = (hours, days, subject_name)

        # TODO: execute the update command

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


def get_ui_data():
    """
    function to use the default schema and get the UI field data
    """
    db = Database(empty_schema.db_schema)
    return db.get_ui_data()

def add_ui_data():
    db = Database(empty_schema.db_schema)
    records = [("question 1", "Select Subjects"),
               ("question 2", "Select Hours Studied"),
               ("subjects", "")]
    for record in records:
        db.add_record("ui_data", ['field_name', 'value'], record_tuple=record)

def add_subjects():
    db = Database(empty_schema.db_schema)
    subjects = empty_schema.subjects
    for subject in subjects:
        db.add_record('subject_records', ['sub_name', 'hours_studied'], record_tuple=(subject, '0.0'))

def get_subject_names():
    db = Database(empty_schema.db_schema)
    subjects = db.get_subject_names()
    return subjects

if __name__ == "__main__":
    # ---------- create new database with basic/empty schema --------
    # create_new_tables()
    # add_ui_data()

    # ---------- get UI label related data ----------
    # data = get_ui_data()
    # print(data)

    # --------- add subjects -----------
    # add_subjects()

    # --------- get subject names -------
    data = get_subject_names()
    print(data)
    print(f"Total {len(data)} subjects")
