import requests

API_KEY = 'abcdefghijklmnopqrstuvwxyz' #api key to be entered here

def get_city_name() -> str:
    return input('Enter the name of the city: ')

def main():
    try:
        city = get_city_name()
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
        response = requests.get(url)
        
        if response.status_code == 200:
            weather_data = response.json()
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            print(f'Temperature: {temperature} K')
            print(f'Description: {description}')
        else:
            print('Error fetching weather data') 
    except Exception as e:
        print(f'ERROR: exception {e} occurred')

main()
