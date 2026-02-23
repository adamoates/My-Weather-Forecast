# My Weather Forecast


A lightweight weather app built with Flask that displays current conditions for any city using the OpenWeatherMap API.

## Features

- Look up current weather by city name, with support for multiple comma-separated cities
- Displays temperature (°F), humidity, weather description, and icon
- Clean gradient UI with a simple search form

## Tech Stack

- **Backend:** Python 3, Flask
- **Frontend:** HTML, Jinja2 templates, inline CSS
- **API:** [OpenWeatherMap](https://openweathermap.org/api)

## Getting Started

### Prerequisites

- Python 3
- An [OpenWeatherMap API key](https://openweathermap.org/appid) (free tier works)

### Installation

1. Fork and clone the repository:
   ```bash
   # Fork via GitHub, then:
   git clone https://github.com/<your-username>/My-Weather-Forecast.git
   cd My-Weather-Forecast
   ```

2. Install dependencies:
   ```bash
   pip install flask requests
   ```

3. Update the `API_KEY` variable in `app.py` with your own OpenWeatherMap key.

4. Run the app:
   ```bash
   python app.py
   ```

5. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Project Structure

```
├── app.py         # Flask server and API logic
├── index.html     # Jinja2 template (UI)
└── README.md
```

## Usage

Enter a city name in the search field and click **Get Weather**. The app will display the current temperature, humidity, weather description, and an icon representing conditions. You can also enter multiple cities separated by commas (e.g. `New York, London, Tokyo`) to view weather for all of them at once.
