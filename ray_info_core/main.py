import click
import json
from pathlib import Path
from .state import app_state

@click.group()
def hello():
    pass

@click.command()
def a():
    click.echo('a')

@click.command()
def b():
    click.echo('b')

hello.add_command(a)
hello.add_command(b)

def main():
    print('hello main')

def load_config():
    with open('./config.json', 'r') as f:
        return json.load(f)

if __name__ == "__main__":
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
    
    import data.db
    data.db.init_db()
    
    hello()