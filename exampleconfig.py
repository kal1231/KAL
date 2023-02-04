import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

bot = telegram.Bot(token="5447331145:AAGa2c0VZfZ8bJFLsT_HEMID93NZbhFujFM")

def start(update, context):
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    query.answer()
    if query.data == '1':
        query.edit_message_text(text="You chose option 1.")
    elif query.data == '2':
        query.edit_message_text(text="You chose option 2.")

updater = Updater(token="YOUR_BOT_TOKEN", use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
