import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Echo the user message."""
    text = update.message.text
    #print(update)
    if str(text).__contains__('vendo'):
        text1 = f"El usuario {update.message.from_user.first_name} ( @{update.message.from_user.username}) ha escrito en {update.message.chat.title}: {text}"
        await context.bot.send_message(chat_id='1530975146', text=text1)    
    #await update.message.reply_text(update.message.text)

if __name__ == '__main__':
    application = ApplicationBuilder().token('6182686134:AAEQ5LjMOuenNEBU0e0JFsIP7iWD5VjvGgw').build()
    
    

    start_handler = CommandHandler('start', start)
    application.add_handler(MessageHandler(filters.TEXT, echo))
    #application.add_handler(start_handler)
    
    application.run_polling()