import click
import codecs

@click.command()
@click.option('--name', default='', help='Your name?')
@click.password_option()
def cli(name, password):
    if name:
        click.echo('Hello {0}!'.format(name))
    else:
        click.echo("Hello User!")
    click.echo('We received {0} as password.'.format(password))
    click.echo('Encrypting password to %s' % codecs.encode(password, 'rot13'))




    


