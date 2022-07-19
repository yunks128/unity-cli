import json
import requests


auth_json = '''{
     "AuthParameters" : {
        "USERNAME" : "",
        "PASSWORD" : ""
     },
     "AuthFlow" : "USER_PASSWORD_AUTH",
     "ClientId" : ""
  }'''


def get_token(username, password, clientID):
    aj = json.loads(auth_json)
    aj['AuthParameters']['USERNAME'] = username #ctx.obj['USER'].username
    aj['AuthParameters']['PASSWORD'] = password #ctx.obj['USER'].password
    aj['ClientId'] =clientID #"71g0c73jl77gsqhtlfg2ht388c"
    response = requests.post('https://cognito-idp.us-west-2.amazonaws.com', headers={"Content-Type":"application/x-amz-json-1.1", "X-Amz-Target":"AWSCognitoIdentityProviderService.InitiateAuth"}, json=aj)
    token = response.json()['AuthenticationResult']['AccessToken']
    return token
