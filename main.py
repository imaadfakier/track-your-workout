import config
import requests
# from requests.auth import HTTPBasicAuth
import datetime

NUTRITIONIX_BASE_URL = 'enter base url'
EXERCISE_ENDPOINT = 'enter exercise endpoint'
SHEETY_BASE_URL = 'enter base url'
PROJECT_ENDPOINT = config.SHEETY_PROJECT_ENDPOINT

# how to (do): (http) basic authentication
USERNAME = config.SHEETY_AUTH_USERNAME
PASSWORD = config.SHEETY_AUTH_PASSWORD

date_today = datetime.datetime.now().strftime('%d/%m/%Y')
time_right_now = datetime.datetime.now().strftime('%H:%M:%S')

url = NUTRITIONIX_BASE_URL + EXERCISE_ENDPOINT

parameters = {
    'query': input('Tell me what exercises you did: '),
    'gender': 'enter gender',
    'weight_kg': # enter weight,
    'height_cm': # enter height,
    'age': # enter age
}
# print(parameters)

headers = {
    'x-app-id': config.NUTRITIONIX_APP_ID,
    'x-app-key': config.NUTRITIONIX_API_KEY,
    'Content-Type': 'application/json',
}

# response = requests.post(url=url, params=parameters, headers=headers)  # wrong! exception will be thrown
# response.raise_for_status()
nutritionix_response = requests.post(url=url, json=parameters, headers=headers)
nutritionix_response.raise_for_status()
# print(response)
# print(response.json())

exercises = nutritionix_response.json()['exercises']
# print(exercises)
exercise_names = [exercise['name'] for exercise in exercises]
# print(exercise_names)
exercise_durations = [exercise['duration_min'] for exercise in exercises]
# print(exercise_durations)
exercises_calories_burned = [exercise['nf_calories'] for exercise in exercises]

url = SHEETY_BASE_URL + PROJECT_ENDPOINT
# print(url)

sheety_headers = {
    'Authorization': config.BEARER_AUTHENTICATION_TOKEN
}

for index in range(len(exercise_names)):
    sheety_parameters = {
        'workout': {
            'date': date_today,
            'time': time_right_now,
            'exercise': exercise_names[index].title(),
            # 'exercise': exercise_names[index].capitalize(),
            'duration': exercise_durations[index],
            'calories': exercises_calories_burned[index],
        }
    }

    # sheety_response = requests.post(url=url, json=sheety_parameters)
    sheety_response = requests.post(
        url=url,
        json=sheety_parameters,
        # auth=requests.auth.HTTPBasicAuth(USERNAME, PASSWORD),
        auth=(USERNAME, PASSWORD),
    )
    # sheety_response = requests.post(url=url, json=sheety_parameters, headers=sheety_headers)
    sheety_response.raise_for_status()
    print(sheety_response.text)
