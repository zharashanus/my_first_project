import requests

def get_weather(city):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": city}

    headers = {
        "x-rapidapi-key": "faa7763d74msh5b00b30e485780dp1f058fjsnf655e6f127aa",
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        weather_info = {
            'city': data['location']['name'],
            'temperature_c': data['current']['temp_c'],
            'wind_kph': data['current']['wind_kph']
        }
        return weather_info

        # if response.status_code == 200:
        #     temp_c = response.json()['current']['temp_c']
        #     wind_kph = response.json()['current']['wind_kph']
        #     humidity = response.json()['current']['humidity']
        #     cloud = response.json()['current']['cloud']
        #
        #
        # else:
        #     return (f"Ошибка: не удалось найти город '{city}'.")
    except:
        return ("Ошибка соединения:", e)

