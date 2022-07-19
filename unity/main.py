import click

from common_options import add_options, _common_options
from unity.commands.ds import data
from user import User
import sys

CONTEXT_SETTINGS = dict(help_option_names=['-h', '—help'])

@click.group()
@add_options(_common_options)
@click.pass_context
def cli(ctx, **kwargs):
  ctx.ensure_object(dict)
  ctx.obj['USER'] = User(kwargs['username'], kwargs['password'])
  pass

cli.add_command(data)

if __name__ == "__main__":
    cli()  # pragma: no cover
