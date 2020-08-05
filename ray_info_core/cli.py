from os import name
import click
from click.decorators import pass_context

from .state.app_config import AppConfig
from .data.dao_author import *
from .data.db import init_db

@click.group()
@pass_context
def cli(ctx):
    ctx.config = AppConfig()
    
    init_db(ctx.config)

@cli.command()
@click.option('--name', type=str)
@click.option('--description', type=str, default="")
@click.pass_obj
def author_add(ctx, name, description):
    dao_author_add(name, description)

@cli.command()
@click.option('--name', type=str)
@click.option('--description', type=str, default="")
@click.pass_obj
def author_update(ctx, name, description):
    dao_author_update(name, description)

@cli.command()
def b():
    click.echo('b')
