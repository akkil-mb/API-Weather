import requests

API = '9fa154dbba09cfe21cd18ec53a73aede'
base_url = 'http://api.openweathermap.org/data/2.5/weather'


def calling():
    city = input('Enter a city name :')
    request_url = f'{base_url}?appid={API}&q={city}'
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        print(data)
        description = data['weather'][0]['description']
        temperature = round(data['main']['temp'] - 273.15,2)
        print(f'\nDescription : {description}')
        print(f'Temperature : {temperature}')

    else:
        print('Enter a valid name')
        calling()

calling()