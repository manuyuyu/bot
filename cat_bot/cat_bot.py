from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import cat_api


async def cats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('incoming hello message')
    await update.message.reply_photo(cat_api.get_random_cat_image_url())
    print(update.effective_user.username)


app = ApplicationBuilder().token("5835081117:AAGTt3RYE6ffLSOt2lr-f6WVGg9-fbE7dIE").build()

app.add_handler(CommandHandler("catplease", cats))

print('Starting bot')

app.run_polling()