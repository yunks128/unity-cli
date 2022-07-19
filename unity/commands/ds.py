import click
import json
import string
import requests
import sys

import os.path
from os import path
from pathlib import Path
from common_options import add_options
import common_options as co
import auth

_ds_endpoints = {
    "ops":{
        "clientId":"",
        "url":""
    },
    "uat":{
        "clientId":"",
        "url":""
    },
    "sit":{
        "clientId":"71g0c73jl77gsqhtlfg2ht388c",
        "url":"https://1gp9st60gd.execute-api.us-west-2.amazonaws.com/dev/"
        ""
    }
}

# This section is for common DATA SERVICE options, added to the unity common options
# Add common options for all DAPA commands here
_ds_common_options = [ ]
_ds_common_options.extend(co._common_options)


@click.group()
@click.pass_context
def data(ctx):
  pass

def get_input(ctx, param, value):
    if not value and not click.get_text_stream('stdin').isatty():
        return click.get_text_stream('stdin').read().strip().split()
    else:
        return value

@data.command()
@add_options(_ds_common_options)
@click.argument('collection', callback=get_input, required=False)
@click.pass_context
def get_collections(ctx, **kwargs):
    """List collection in the Unity data services"""
    token = auth.get_token(ctx.obj['USER'].username,ctx.obj['USER'].password, "71g0c73jl77gsqhtlfg2ht388c" )
    response = requests.get('https://1gp9st60gd.execute-api.us-west-2.amazonaws.com/dev/am-uds-dapa/collections', headers={"Authorization": "Bearer " + token})
    print(json.dumps(response.json()))

@data.command()
@add_options(_ds_common_options)
@click.argument('collection', callback=get_input, required=True)
@click.option('--datetime', required=False, default=None, help='startdate/enddate for filtering items. e.g. --datetime=2000-02-12T00:00:00Z/2023-03-18T12:31:12Z')
@click.option('--limit', required=False, default=None, help='number of results to include.')
# bbox is not supported yet
# offset is not included, the cli should handle the paging on behalf of the users
@click.pass_context
def get_collection(ctx, collection, **kwargs):
    """get the items for a given collection in the Unity data services"""
    token = auth.get_token(ctx.obj['USER'].username,ctx.obj['USER'].password, "71g0c73jl77gsqhtlfg2ht388c" )
    url = "https://1gp9st60gd.execute-api.us-west-2.amazonaws.com/dev/am-uds-dapa/collections/{}/items".format(collection)
    # the datetime,limit, and offset are included due to a current bug in the API Gatway setting these values to 'none'.
    response = requests.get(url, headers={"Authorization": "Bearer " + token}, params={"datetime":"2000-02-12T00:00:00Z/2023-03-18T12:31:12Z", "limit":100, "offset":0})
    print(json.dumps(response.json()))
