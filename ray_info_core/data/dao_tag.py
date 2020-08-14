import click
from .db import Tag

def dao_tag_is_existed(name: str) -> bool:
    return Tag.select().where(Tag.name == name).exists()

def dao_tag_get(name: str) -> Tag:
    return Tag.select().where(Tag.name==name).get()

