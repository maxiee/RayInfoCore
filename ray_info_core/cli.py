import click
import json
from pathlib import Path

from click.decorators import pass_context
from ray_info_core.state import app_state
from ray_info_core.data.db import init_db

def load_config():
    with open('./config.json', 'r') as f:
        return json.load(f)

@click.group()
@pass_context
def cli(ctx):
    config = load_config()
    app_state.config = config

    if config == None:
        print('Config.json load failed')
        exit(0)
    
    data_path = config['dataPath']
    app_state.data_path = data_path
    print("dataPath = %s" % config['dataPath'])

    Path(data_path) \
        .expanduser() \
        .mkdir(parents=True, exist_ok=True)
    
    init_db()

@cli.command()
def a():
    click.echo('a')

@cli.command()
def b():
    click.echo('b')
