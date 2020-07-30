from os.path import join
from peewee import *
from state import app_state

db = None

def init_db():
    global db

    print("db path = %s" % app_state.get_db_path())

    db = SqliteDatabase(app_state.get_db_path(), {
        'journal_mode': 'wal',
        'foreign_keys': 1,
        'ignore_check_constraints': 0,
        'synchronous': 0
    })

    db.connect()
    db.create_tables([], safe=True)
