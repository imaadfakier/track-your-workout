import os

# app id
os.environ['NUTRITIONIX_APP_ID'] = 'enter app id'
NUTRITIONIX_APP_ID = os.environ.get('NUTRITIONIX_APP_ID')
# api key
os.environ['NUTRITIONIX_API_KEY'] = 'enter api key'
NUTRITIONIX_API_KEY = os.environ.get('NUTRITIONIX_API_KEY')
# sheety project endpoint
os.environ['SHEETY_PROJECT_ENDPOINT'] = 'enter project endpoint'
SHEETY_PROJECT_ENDPOINT = os.environ.get('SHEETY_PROJECT_ENDPOINT')
# http basic authentication: username and password
#   username
os.environ['SHEETY_AUTH_USERNAME'] = 'enter username'
SHEETY_AUTH_USERNAME = os.environ.get('SHEETY_AUTH_USERNAME')
#   password
os.environ['SHEETY_AUTH_PASSWORD'] = 'enter auth password'
SHEETY_AUTH_PASSWORD = os.environ.get('SHEETY_AUTH_PASSWORD')
# bearer authentication token
os.environ['BEARER_AUTHENTICATION_TOKEN'] = 'enter bearer token'
BEARER_AUTHENTICATION_TOKEN = os.environ.get('BEARER_AUTHENTICATION_TOKEN')
