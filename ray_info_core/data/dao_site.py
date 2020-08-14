import click
from .db import Site

def dao_site_is_existed(name : str) -> bool:
    return Site.select().where(Site.name==name).exists()

def dao_site_get(name : str) -> Site:
    return Site.select().where(Site.name==name).get()

def dao_site_add(name: str, url="", description="", tags=""):
    if dao_site_is_existed(name):
        click.echo('site is existed, use dao_site_update command.')
        return
    site = Site()
    site.name = name
    site.description = description
    site.save()
    click.echo('site %s saved successfully.' % name)



