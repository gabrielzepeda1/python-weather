import requests


def main():
    city = input("Enter the name of a city: ")
    latitude, longitude = get_coordinates(city)
    temperature = get_weather(latitude, longitude)
    print(f"The current temperature in {city} is {temperature}°C")


def get_coordinates(city):
    base_url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1, "language": "en", "format": "json"}
    response = requests.get(base_url, params=params)
    data = response.json()

    if data.get("results"): 
        city_data = data["results"][0]
        return city_data["latitude"], city_data["longitude"]
    else: 
        raise ValueError("City not found.")



def get_weather(latitude, longitude):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True 
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    return data["current_weather"]["temperature"]

if __name__ == "__main__":
    main()
