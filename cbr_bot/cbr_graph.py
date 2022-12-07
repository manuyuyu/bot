import cbr_api
from datetime import date, timedelta, time
import matplotlib.pyplot as plt
import io

def get_figure_image():
    numdays = 7
    base = date.today() - timedelta(days=6)
    dates_list = [base + timedelta(days=x) for x in range(numdays)]

    charcodes = ['EUR', 'USD', 'CNY']

    last_week_eur = []
    last_week_usd = []
    last_week_cny = []

    for elem in dates_list:
        currencies = cbr_api.get_currency_rates(charcodes, elem)
        eur = currencies['EUR']
        usd = currencies['USD']
        cny = currencies['CNY']
        last_week_eur.append(float(eur.value.replace(',', '.')))
        last_week_usd.append(float(usd.value.replace(',', '.')))
        last_week_cny.append(float(cny.value.replace(',', '.')))

    plt.figure()
    plt.plot(dates_list, last_week_eur, label = 'Euro')
    plt.plot(dates_list, last_week_usd, label = 'USD')
    plt.plot(dates_list, last_week_cny, label = 'CNY')
    plt.title('Курс евро, доллара, юаня за последние 7 дней')
    plt.xlabel('Дата')
    plt.ylabel('Курс в рублях')
    plt.legend(loc='best')
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.grid()
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf


