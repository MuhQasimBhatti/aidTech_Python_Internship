import requests
import json

api_key = '89e9e3f45cac65a2618d4cf5b44a4253'
favorites = {}

# Load favorites from a JSON file if it exists
try:
    with open('favorites.json', 'r') as file:
        favorites = json.load(file)
except FileNotFoundError:
    pass

def get_weather_forecast(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

while True:
    view_favorites = input('Do you want to see weather information for your favorite cities? (Y/N): ')
    if view_favorites.lower() == 'y':
        print('Your Favorite Places:')
        for city, data in favorites.items():
            print(f'City: {city}')
            print(f'Temperature: {data["Temperature"]} K')
            print(f'Description: {data["Description"]}')


    city = input('Enter city name: ')

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f'Temperature: {temp} K')
        print(f'Description: {desc}')

        # Ask the user if they want to save this location as a favorite
        save_favorite = input('Do you want to save this location as a favorite? (Y/N): ')
        if save_favorite.lower() == 'y':
            favorites[city] = {'Temperature': temp, 'Description': desc}
            print(f'{city} has been added to your favorites.')

        # Ask the user if they want to see the weather forecast for the next few days
        view_forecast = input('Do you want to see the weather forecast for the next few days? (Y/N): ')
        if view_forecast.lower() == 'y':
            forecast_data = get_weather_forecast(city)
            if forecast_data:
                print('Weather Forecast for the next few days:')
                for forecast in forecast_data['list']:
                    date = forecast['dt_txt']
                    temp = forecast['main']['temp']
                    desc = forecast['weather'][0]['description']
                    print(f'Date: {date}')
                    print(f'Temperature: {temp} K')
                    print(f'Description: {desc}')
            else:
                print('Error fetching weather forecast data')

    else:
        print('Error fetching weather data')

    choice = input('Search for another location (Y/N): ')
    if choice.lower() == 'n':
        # Save favorites to a JSON file before exiting
        with open('favorites.json', 'w') as file:
            json.dump(favorites, file, indent=4)
        break
