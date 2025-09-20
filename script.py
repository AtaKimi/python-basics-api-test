import os
import gspread
import requests

from dotenv import load_dotenv

load_dotenv()

# It's still a bit sucks that I'm forced to use a oauth2 for the authentication process.
# It's very inconvenient for a simple script like this.
# I did try to use a service account, but it didn't work out because I don't have workspace email.
# So I have to use oauth2, which requires manual intervention to authenticate the first time.

# List of cities to fetch weather data for
CITY = ["London", "New York", "Tokyo"]
def main():
    # Initialize lists to store weather data and information
    weather_data_list = []
    weather_info_list = []

    for city in CITY:
        # Fetch weather data from the API
        weather_data = get_weather_data(city)
        weather_data_list.append(weather_data)
        print(weather_data)

        # Extract and print specific weather information
        weather_info = extract_weather_info(weather_data)
        weather_info_list.append(weather_info)
        print(weather_info)

    # Create a Google Spreadsheet and populate it with weather data
    spreadsheet = create_weather_spreadsheet(weather_info_list)

def get_weather_data(city):
    # Fetch weather data from OpenWeatherMap API
    api_key = os.getenv("WEATHER_API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch weather data"}

def extract_weather_info(weather_data):
    # Extract specific weather information from the API response
    # City name, temperature, humidity
    if "error" in weather_data:
        return weather_data["error"]

    city = weather_data.get("name")
    temp = weather_data.get("main", {}).get("temp")
    humidity = weather_data.get("main", {}).get("humidity")

    return f"City: {city}, Temperature: {temp}°C, Humidity: {humidity}%"

def create_weather_spreadsheet(data, title="Weather Data"):
    try:
        # Authenticate and create a new Google Spreadsheet
        gc = gspread.oauth(
            credentials_filename='client_secret.json',
            authorized_user_filename='authorized_user.json'
        )        
        
        # Create a new spreadsheet and share it
        sht1 = gc.create(title)
        sht1.share(None, perm_type='anyone', role='writer')
        
        # Populate the spreadsheet with weather data
        worksheet = sht1.sheet1
        worksheet.append_row(["City", "Temperature (°C)", "Humidity (%)"])
        for entry in data:
            if "error" in entry:
                continue
            parts = entry.split(", ")
            city = parts[0].split(": ")[1]
            temp = parts[1].split(": ")[1].replace("°C", "")
            humidity = parts[2].split(": ")[1].replace("%", "")
            worksheet.append_row([city, temp, humidity])
        print(f"Spreadsheet created: {sht1.url}")
        return sht1.url
    except Exception as error:
        print(f"An error occurred: {error}")
        return error

if __name__ == "__main__":
    main()