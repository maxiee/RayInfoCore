from peewee import *
from state import app_state

db = SqliteDatabase(app_state.get_db_path(), {
        'journal_mode': 'wal',
        'foreign_keys': 1,
        'ignore_check_constraints': 0,
        'synchronous': 0
    })

class Author(Model):
    name = CharField(max_length=128)
    description = CharField()

    class Meta:
        database = db
    
def init_db() -> None:
    db.connect()
    db.create_tables([Author], safe=True)