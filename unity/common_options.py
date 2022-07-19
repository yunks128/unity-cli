import click
import os


_common_options = [
 click.option('--env', required=False, default='prod', help='The Unity environment to use. Defaults to production environment.'),
 click.option('--username',  default=lambda: os.environ.get("UNITY_USER", ""), help='Unity Username'),
 click.option('--password', hide_input=True,  default=lambda: os.environ.get("UNITY_PASSWORD", ""), help='Unity Password')
]

def add_options(options):
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options
