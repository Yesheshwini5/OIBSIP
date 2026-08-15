import requests


# Your OpenWeatherMap API key
API_KEY = "25a1b390fe85bfafe1c6180fe39286ff"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetch weather information for a given city."""

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        # Handle HTTP errors
        if response.status_code == 401:
            print("Error: Invalid API key.")
            return

        if response.status_code == 404:
            print("Error: City not found.")
            return

        response.raise_for_status()

        # Convert JSON response into a Python dictionary
        data = response.json()

        # Extract weather information
        city_name = data["name"]
        country = data["sys"]["country"]

        temperature_c = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        description = data["weather"][0]["description"]

        wind_speed = data["wind"]["speed"]

        # Convert Celsius to Fahrenheit
        temperature_f = (temperature_c * 9 / 5) + 32

        # Display results
        print("\n" + "=" * 40)
        print("           CURRENT WEATHER")
        print("=" * 40)

        print(f"Location      : {city_name}, {country}")
        print(f"Temperature   : {temperature_c:.2f} °C")
        print(f"Temperature   : {temperature_f:.2f} °F")
        print(f"Humidity      : {humidity}%")
        print(f"Condition     : {description.title()}")
        print(f"Wind Speed    : {wind_speed} m/s")

        print("=" * 40)

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the weather service.")

    except requests.exceptions.RequestException as error:
        print(f"Error: Something went wrong: {error}")

    except (KeyError, ValueError):
        print("Error: Unable to read the weather data.")


def main():
    """Main program."""

    print("================================")
    print("       BASIC WEATHER APP")
    print("================================")

    city = input("Enter city name or ZIP code: ").strip()

    # Input validation
    if not city:
        print("Error: City name or ZIP code cannot be empty.")
        return

    get_weather(city)


if __name__ == "__main__":
    main()

