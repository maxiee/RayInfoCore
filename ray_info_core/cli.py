import click
from click.decorators import pass_context

from .state.app_config import AppConfig
from .data.db import init_db

@click.group()
@pass_context
def cli(ctx):
    ctx.config = AppConfig()
    
    init_db(ctx.config)

@cli.command()
def a():
    click.echo('a')

@cli.command()
def b():
    click.echo('b')
