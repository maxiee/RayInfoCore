from peewee import *

db = SqliteDatabase(None)

class BaseModel(Model):
    class Meta:
        database = db

class Author(BaseModel):
    name = CharField(max_length=128)
    description = CharField()

class Tag(BaseModel):
    name = CharField(64)

class Site(BaseModel):
    name = CharField(max_length=128)
    url = CharField()
    description = CharField()

class TagSiteRelation(BaseModel):
    tag = ForeignKeyField(Tag, backref='site_relations')
    site = ForeignKeyField(Site, backref='tag_relations')

    
def init_db(config) -> None:
    db.init(config.get_db_path())
    db.create_tables([Author, Site, Tag, TagSiteRelation], safe=True)
