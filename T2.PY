import requests

def get_weather_data(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main_data = data["main"]
        weather_data = data["weather"][0]

        print(f"Weather in {city_name}:")
        print(f"Temperature: {main_data['temp']}°C")
        print(f"Description: {weather_data['description']}")
        print(f"Humidity: {main_data['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("Error fetching weather data.")

if __name__ == "__main__":
    api_key = "62d6b7042dc82f3fd28219c55e5ded16"
    city_name = input("Enter the city name: ")
    get_weather_data(api_key, city_name)