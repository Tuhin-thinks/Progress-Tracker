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
    },
    # TODO: implement subject log table
    {
        "name": "subject_log",
        "columns": {
            "id": "integer primary key autoincrement",
            "sub_id": "integer",
            "day_num": "integer",
            "hours_studied": "text"
        }
    }
]

"""
subjects schema:
    subjects[subject]
    subject: {
        name
 }"""
subjects = [
    'COA',
    'TOC',
    'CD',
    'OS',
    'CNW',
    'Engg. Math',
    'Discrete Math',
    'DL',
    'P & DS',
    'ALGO',
    'DBMS', 
    'GEN. APT.'
]
