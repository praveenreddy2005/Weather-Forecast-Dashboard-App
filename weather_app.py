import tkinter as tk
from tkinter import ttk
import requests
from datetime import datetime
from config import API_KEY

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast App")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.is_dark_mode = False
        self.unit = "metric"  # "metric" for Celsius, "imperial" for Fahrenheit

        self.create_widgets()
        self.set_theme()

    def create_widgets(self):
        self.theme_frame = ttk.LabelFrame(self.root, text="Theme:")
        self.theme_frame.pack(pady=5)

        self.theme_var = tk.StringVar(value="light")
        ttk.Radiobutton(self.theme_frame, text="Light", variable=self.theme_var, value="light", command=self.toggle_theme).pack(side="left", padx=10)
        ttk.Radiobutton(self.theme_frame, text="Dark", variable=self.theme_var, value="dark", command=self.toggle_theme).pack(side="left")

        ttk.Label(self.root, text="Enter City Name:").pack(pady=5)
        self.city_entry = ttk.Entry(self.root, font=("Arial", 14))
        self.city_entry.pack(pady=5)

        self.unit_var = tk.StringVar(value="metric")
        self.unit_frame = ttk.LabelFrame(self.root, text="Unit:")
        self.unit_frame.pack(pady=5)

        ttk.Radiobutton(self.unit_frame, text="Celsius", variable=self.unit_var, value="metric").pack(side="left", padx=10)
        ttk.Radiobutton(self.unit_frame, text="Fahrenheit", variable=self.unit_var, value="imperial").pack(side="left")

        self.search_button = ttk.Button(self.root, text="Fetch Weather", command=self.get_weather)
        self.search_button.pack(pady=10)

        self.weather_output = tk.Text(self.root, height=25, width=48, font=("Courier", 9))
        self.weather_output.pack(padx=10)

    def toggle_theme(self):
        self.is_dark_mode = self.theme_var.get() == "dark"
        self.set_theme()

    def set_theme(self):
        bg = "#2E2E2E" if self.is_dark_mode else "#F0F0F0"
        fg = "#FFFFFF" if self.is_dark_mode else "#000000"
        self.root.configure(bg=bg)
        self.weather_output.configure(bg=bg, fg=fg, insertbackground=fg)

    def get_weather(self):
        city = self.city_entry.get()
        unit = self.unit_var.get()
        api_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units={unit}&appid={API_KEY}"

        try:
            response = requests.get(api_url)
            data = response.json()
            self.display_weather(data, unit)
        except Exception as e:
            self.weather_output.delete("1.0", tk.END)
            self.weather_output.insert(tk.END, f"Error fetching weather data: {e}")

    def display_weather(self, data, unit):
        self.weather_output.delete("1.0", tk.END)

        if data["cod"] != "200":
            self.weather_output.insert(tk.END, f"City not found.\n")
            return

        city_name = data["city"]["name"]
        country = data["city"]["country"]
        sunrise = datetime.utcfromtimestamp(data["city"]["sunrise"] + data["city"]["timezone"]).strftime('%H:%M')
        sunset = datetime.utcfromtimestamp(data["city"]["sunset"] + data["city"]["timezone"]).strftime('%H:%M')
        degree = "°C" if unit == "metric" else "°F"

        output = f"\U0001F4CD Weather in {city_name}, {country}\n"
        output += f"\u2600 Sunrise: {sunrise}   \U0001F319 Sunset: {sunset}\n\n"

        daily_forecast = {}
        for entry in data["list"]:
            date = datetime.fromtimestamp(entry["dt"]).strftime('%A, %d %B')
            if date not in daily_forecast:
                temp = entry["main"]["temp"]
                humidity = entry["main"]["humidity"]
                wind_speed = entry["wind"]["speed"]
                description = entry["weather"][0]["description"].capitalize()
                wind_unit = "km/h" if unit == "metric" else "mph"
                wind_speed = round(wind_speed * 3.6, 2) if unit == "metric" else round(wind_speed, 2)

                daily_forecast[date] = (temp, humidity, wind_speed, description)

        for date, (temp, humidity, wind_speed, description) in list(daily_forecast.items())[:5]:
            output += f"{date}\n"
            output += f"\U0001F327 {description}\n"
            output += f"\U0001F321 Temp: {temp:.2f}{degree}\n"
            output += f"\U0001F4A7 Humidity: {humidity}%\n"
            output += f"\U0001F32C Wind: {wind_speed} {wind_unit}\n\n"

        self.weather_output.insert(tk.END, output)

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()



