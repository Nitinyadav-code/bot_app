from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes



# Define the command handler function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Welcome to my mini-app!  write  /meme for meme')
async def meme(update:Update, context: ContextTypes.DEFAULT_TYPE)-> None:
    await update.message.reply_text("serach @hasle_kallu on instagram" )
async def download(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    web_app_url = "https://youtube-download-rb1x.onrender.com"
    await update.message.reply_text(f"Please use the web app to download videos: {web_app_url}")

    


# Initialize the Application with the bot token
application = Application.builder().token('7824250935:AAEDJ0gWhe1jsIhybpDA1cgY9IWRUPjgmps').build()

# Add a command handler for the '/start' command
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('meme',meme))
application.add_handler(CommandHandler('youtube video download',download))


# Start polling for updates
application.run_polling()
