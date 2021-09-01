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