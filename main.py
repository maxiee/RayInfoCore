import click

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

if __name__ == "__main__":
    hello()