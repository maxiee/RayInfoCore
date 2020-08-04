from peewee import *
from ray_info_core.state import app_state

db = SqliteDatabase(None)

class BaseModel(Model):
    class Meta:
        database = db

class Author(BaseModel):
    name = CharField(max_length=128)
    description = CharField()
    
def init_db() -> None:
    db.init(app_state.get_db_path())
    db.create_tables([Author], safe=True)
