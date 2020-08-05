from peewee import *

db = SqliteDatabase(None)

class BaseModel(Model):
    class Meta:
        database = db

class Author(BaseModel):
    name = CharField(max_length=128)
    description = CharField()
    
def init_db(config) -> None:
    db.init(config.get_db_path())
    db.create_tables([Author], safe=True)
