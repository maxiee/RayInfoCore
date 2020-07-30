import click
import json

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

def loadConfig():
    with open('./config.json', 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    config = loadConfig()

    print("dataPath = %s" % config['dataPath'])
    
    hello()