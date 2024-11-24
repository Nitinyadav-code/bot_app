import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# OpenWeatherMap API Key (Use environment variable for security)
API_KEY = os.getenv("9cdf57335c0a3b75dd4577e0d1dc6ca3")
BASE_URL = "http://api.openweathermap.org/data/2.5/"

# Define the '/start' command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome to the bot! Available commands:\n"
        "/meme - Get a meme suggestion\n"
        "/download <YouTube URL> - Download a YouTube video\n"
        "/weather <city> - Get the current weather\n"
        "/forecast <city> - Get the weather forecast"
    )

# Define the '/meme' command
async def meme(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("click on the link to find best memes:  https://www.instagram.com/hasle_kallu")

# Function to fetch current weather
async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Please provide a city name. Example: /weather London")
        return

    city = " ".join(context.args)
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            await update.message.reply_text(f"City {city} not found. Please check the name and try again.")
            return
        
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temperature = main["temp"]
        humidity = main["humidity"]

        weather_message = f"Weather in {city}:\n" \
                          f"Description: {weather_desc}\n" \
                          f"Temperature: {temperature}°C\n" \
                          f"Humidity: {humidity}%"

        await update.message.reply_text(weather_message)

    except Exception as e:
        await update.message.reply_text(f"An error occurred while fetching the weather. {str(e)}")

# Function to fetch 5-day weather forecast
async def forecast(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Please provide a city name. Example: /forecast London")
        return

    city = " ".join(context.args)
    url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != "200":
            await update.message.reply_text(f"City {city} not found. Please check the name and try again.")
            return

        forecast_message = f"5-Day Weather Forecast for {city}:\n"
        for forecast in data["list"][:5]:  # Taking forecast for the next 5 intervals (3 hours each)
            dt = forecast["dt_txt"]
            weather_desc = forecast["weather"][0]["description"]
            temperature = forecast["main"]["temp"]
            forecast_message += f"{dt}: {weather_desc}, Temp: {temperature}°C\n"

        await update.message.reply_text(forecast_message)

    except Exception as e:
        await update.message.reply_text(f"An error occurred while fetching the forecast. {str(e)}")

# Initialize the Application with the bot token
application = Application.builder().token("YOUR_BOT_TOKEN").build()

# Add command handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("meme", meme))
application.add_handler(CommandHandler("weather", weather))
application.add_handler(CommandHandler("forecast", forecast))

# Start polling for updates
application.run_polling()
