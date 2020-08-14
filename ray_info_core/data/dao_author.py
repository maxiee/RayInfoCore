import click
from .db import Author

def dao_author_is_existed(name : str) -> bool:
    return Author.select().where(Author.name==name).exists()

def dao_author_get(name: str) -> Author:
    return Author.select().where(Author.name==name).get()

def dao_author_add(name : str, description=""):
    if dao_author_is_existed(name):
        click.echo('author is existed, use dao_author_upadate command.')
        return
    author = Author()
    author.name = name
    author.description = description
    author.save()
    click.echo("author %s saved seccussfully." % name)

def dao_author_update(name: str, description: str):
    if not dao_author_is_existed(name):
        click.echo("author is not exist, user dao_author_add command.")
        return
    author = dao_author_get(name)
    if author.name != name:
        author.name = name;
    if author.description != description:
        author.description = description
    author.save()
    click.echo('authod %s udpated seccussfully.' % name)
