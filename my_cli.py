import click

@click.command()
@click.option('--name', default='', help='Your name?')
def cli(name):
    if name:
        click.echo('Hello {0}!'.format(name))
    else:
        click.echo("Hello User!")



