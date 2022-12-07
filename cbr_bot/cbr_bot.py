from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import cbr_api, cbr_graph
from datetime import date, datetime


async def cbr(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f'Команда /cbr от username={update.effective_user.username} chat_id={update.message.chat_id}')

    # -- парсим аргументы команды /cbr
    if (len(context.args) > 0):
        # в параметрах команды передали дату, на которую получаем курс валют
        date_req_from_user = context.args[0]
        
        try:
            # пытаемся распарсить дату из параметра команды /cbr
            date_req_date = datetime.date(datetime.strptime(date_req_from_user, '%d.%m.%Y'))
        except ValueError:
            await update.message.reply_text("Ошибка. Дата должна быть в формате 'день.месяц.год' .")
            return

        # до 1999 года не было евро! потому и курс получить нельзя.
        if date_req_date < date(1999, 1, 1) or date_req_date > date.today():
            await update.message.reply_text('Ошибка. На такую дату нет курса валют!')
            return
    else:
        date_req_date = None

    await update.message.reply_chat_action(ChatAction.TYPING)
    
    # -- получаем данные по курсам валют из апи ЦБ
    charcodes = ['EUR', 'USD', 'CNY']
    currencies = cbr_api.get_currency_rates(charcodes, date_req_date)
    eur = currencies['EUR']
    usd = currencies['USD']
    cny = currencies['CNY']

    # -- выводим курсы валют пользователю
    if date_req_date is None:
        date_req_date_or_today = datetime.today()
    else:
        date_req_date_or_today = date_req_date

    await update.message.reply_text(f"Курсы валют на {date_req_date_or_today.strftime('%d %b %Y')}. Евро = {eur.value}, Доллар = {usd.value}, Юань = {cny.value}")

    await update.message.reply_chat_action(ChatAction.TYPING)

    # -- выводим график изменения курсов валют
    image_bytes = cbr_graph.get_figure_image()
    await update.message.reply_photo(image_bytes)
   

if __name__ == '__main__':
    app = ApplicationBuilder().token("5655342101:AAG4SveEB81nDXOpIfw5iSGMrsEA42fjmAY").build()

    app.add_handler(CommandHandler("cbr", cbr))
    print('Starting bot')
    app.run_polling()