import click
from .db import Author

def dao_author_is_existed(name : str) -> bool:
    return Author.select().where(Author.name==name).exists()

def dao_author_add(name : str, description=""):
    if (dao_author_is_existed(name)):
        click.echo('author is exist, use author_upadate command')
        return
    author = Author()
    author.name = name
    author.description = description
    author.save()
    
    click.echo("author %s saved seccussfully." % name)
