import datetime
import os
import sqlite3
from typing import List, Dict, Sequence, Tuple, TypeVar

try:
    import empty_schema
except ImportError:
    from . import empty_schema

BASE = os.path.dirname(__file__)
DEFAULT_DB_PATH = os.path.join(BASE, "data_sqlite3.db")

F_ = TypeVar('F_', Tuple[str, str], type(None))


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
    def __init__(self, tables: List[Dict]):
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
            cols_query = ",".join([(k + " " + v)
                                   for k, v in table["columns"].items()])
            query = f"""CREATE TABLE IF NOT EXISTS {table["name"]}(
                {cols_query}
            );"""
            execute_command(query)

    @staticmethod
    def add_record(table, column_names, record_tuple):
        columns = ",".join(column_names)
        values = ",".join(["?"] * len(column_names))
        query = f"""INSERT INTO {table}({columns}) VALUES({values})"""
        execute_command(query, record_tuple)

    @staticmethod
    def get_ui_data():
        query = f"""SELECT * FROM ui_data"""
        ui_data = execute_fetch(query)
        data_dict = {}
        for row in ui_data:
            """
            row[0] => id
            row[1] => field_name
            row[2] => value
            """
            data_dict[row[1]] = row[2]
        return data_dict

    @staticmethod
    def get_subject_names():
        """
        To get only subject names from subject_records database
        """
        query = """SELECT sub_name FROM subject_records"""
        data = execute_fetch(query)
        subjects = []
        for name in data:
            subjects.append(name[0])
        return subjects

    @staticmethod
    def get_subject_data(sub_name: str, fields: Sequence[str]):
        """
        To a mentioned column data in subject_records db
        """
        field_query = ""
        if type(fields) == tuple or type(fields) == list:
            field_query = ", ".join(fields)
        query = f"""SELECT {field_query} FROM subject_records WHERE sub_name=?;"""
        args = (sub_name,)
        print("args:", args, "\nquery:", query)
        return execute_fetch(query, *args)

    def update_passed_days(self):
        ui_data = self.get_ui_data()
        start_date = ui_data['start_date']
        days_passed = datetime.datetime.today() - (datetime.datetime.today()
                                                   if start_date is None
                                                   else datetime.datetime.strptime(start_date,
                                                                                   "%d-%m-%Y")) + datetime.timedelta(
            days=1)
        query = """UPDATE ui_data 
        SET value=?
        WHERE field_name=?;"""
        execute_command(query, str(days_passed.days), 'days_passed')
        if start_date is None:
            execute_command(query, "21-11-2021", 'start_date')
        print("days passed :", days_passed.days, " updated")

    @staticmethod
    def update_subject_study_hours(subject_name: str, hours=None, days=None):
        if not any((hours is None, days is None)):
            raise ValueError("hours and days both cannot be empty")

        # check if the subject actually exists and get it's hours and days data
        query = f"""
        SELECT hours_studied, days_spent
            FROM subject_records
            WHERE sub_name=?;
        """
        hours_studied_rows = execute_fetch(query, subject_name)  # get query rows, if subject exists
        if hours_studied_rows:
            db_hours, db_days = hours_studied_rows[0]
        else:
            raise ValueError(f"{subject_name} doesn't exist in the database.")

        # add hours and days data with the current data and update in the table
        if hours:
            db_hours = float(db_hours) + float(hours)
        if days:
            db_days = int(db_days) + days

        query = f"""
        UPDATE subject_records 
            SET hours_studied=?, days_spent=?
        WHERE
            sub_name=?;
        """

        # execute the update command
        execute_command(query, str(db_hours), str(db_days) if db_days else None, subject_name)
        print("updated successfully")


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


def update_subject_data(s_name: str, hrs_add=None, days_spent=None):
    db = Database(empty_schema.db_schema)
    subjects = db.update_subject_study_hours(s_name, hrs_add, days_spent)
    return subjects


def update_days_passed():
    db = Database(empty_schema.db_schema)
    db.update_passed_days()


def get_subject_data(sub_name: str) -> F_:
    db = Database(empty_schema.db_schema)
    data = db.get_subject_data(sub_name, fields=('hours_studied', 'days_spent'))
    if data:
        print("data:", data)
        fetched_row = data[0]
        hours_, days_ = fetched_row[0], fetched_row[1]
        return hours_, days_
    else:
        return None


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
    # data = get_subject_names()
    # print(data)
    # print(f"Total {len(data)} subjects")

    # --------- update subject data --------
    # data = update_subject_data('p & ds', 0.0)
    # print(update_days_passed())

    # -------- get subject data ------------
    print(get_subject_data('CNW'))
