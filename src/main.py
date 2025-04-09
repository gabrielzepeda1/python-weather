import requests


def main():
    city = input("Enter the name of a city: ") 

    try:
        latitude, longitude = get_coordinates(city)
        temperature = get_weather(latitude, longitude)
        print(f"The current temperature in {city} is {temperature}°C")

    except ValueError as ve:
        print(f"Error: {ve}")
    
    except ConnectionError as ce: 
        print(f"Network error: {ce}")
    
    except Exception as e: 
        print("Something went wrong. Please try again.", e)


def get_coordinates(city):
    base_url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1, "language": "en", "format": "json"}

    try: 
        response = requests.get(base_url, params=params)
        data = response.json()
    except requests.RequestException: 
        raise ConnectionError("Failed to connect to the geocoding API.")

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

    try:
        response = requests.get(base_url, params=params, timeout=5)
        data = response.json()
    except requests.RequestException: 
        raise ConnectionError("Failed to connect to the weather API.")
    
    if "current_weather" not in data or "temperature" not in data["current_weather"]:
        raise ValueError("Weather data is unavailable or incomplete.")

    return data["current_weather"]["temperature"]

if __name__ == "__main__":
    main()
