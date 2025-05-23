# Weather Forecast Dashboard

A beginner-friendly Python desktop app using Tkinter that fetches live weather data and displays current weather and a 5-day forecast for any city. The app uses the OpenWeatherMap API and presents weather details with a clean, interactive GUI including icons, charts, and theme toggling.


## Features

- Search weather by city name
- Display current temperature, humidity, wind speed, weather condition, sunrise & sunset times
- Show weather icon based on current condition
- 5-day weather forecast with temperature, condition, and icons
- Interactive temperature plot for 5-day forecast using Matplotlib
- Toggle temperature units between Celsius and Fahrenheit
- Dark mode / Light mode toggle for modern UI experience
- Error handling for invalid cities or connectivity issues

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/weather-dashboard.git
cd weather-dashboard
Create and activate a virtual environment (recommended):


# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Install required packages:

pip install -r requirements.txt
Configure your OpenWeatherMap API key:
Sign up at OpenWeatherMap for a free API key.
Open the config.py file and replace the placeholder with your API key:


API_KEY = "your_actual_api_key_here"
Usage
Run the application with:

python weather_app.py

Enter a city name and click Get Weather.
Use Switch to °F/°C button to toggle units.
Use Dark Mode/Light Mode button to toggle themes.
View current weather info, 5-day forecast, and temperature plot.

Project Structure

weather-dashboard/
├── weather_app.py          # Main application code with GUI and API calls
├── config.py               # Contains your API key
├── requirements.txt        # Project dependencies
├── README.md               # This file
└── assets/                 # (Optional) Icons or images if used locally

Dependencies
Python 3.x

requests
Pillow (for handling icons)
matplotlib (for plotting forecast data)
tkinter (usually included with Python)

Install all dependencies with:

pip install -r requirements.txt
Contributing
Feel free to submit issues or pull requests to improve the app! Suggestions for additional features or UI improvements are welcome.

License
This project is licensed under the MIT License.

Acknowledgments
OpenWeatherMap API for providing weather data
Tkinter and Matplotlib communities for GUI and plotting tools

If you have questions or need help, reach out anytime!
