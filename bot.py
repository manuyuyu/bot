from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('incoming hello message')
    await update.message.reply_text(f'Юлька Рулит!!! {update.effective_user.first_name}')
    print(update.effective_user.username)


app = ApplicationBuilder().token("5707244270:AAGo9o78m7zFVHP_NEf2m1q46F8-468Rgi4").build()

app.add_handler(CommandHandler("hello", hello))

print('Starting bot')

app.run_polling()