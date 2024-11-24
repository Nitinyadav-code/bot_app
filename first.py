from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes



# Define the command handler function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Welcome to my mini-app!  write  /meme for meme')
async def meme(update:Update, context: ContextTypes.DEFAULT_TYPE)-> None:
    await update.message.reply_text("serach @hasle_kallu on instagram" )
    


# Initialize the Application with the bot token
application = Application.builder().token('7824250935:AAEDJ0gWhe1jsIhybpDA1cgY9IWRUPjgmps').build()

# Add a command handler for the '/start' command
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('meme',meme))


# Start polling for updates
application.run_polling()
