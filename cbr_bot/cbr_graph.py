import cbr_api
from datetime import date, timedelta, time
import matplotlib.pyplot as plt

numdays = 7
base = date.today() - timedelta(days=6)
dates_list = [base + timedelta(days=x) for x in range(numdays)]
dates_list = [date.strftime('%d/%m/%Y') for date in dates_list]

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


plt.plot(dates_list, last_week_eur, label = 'Euro')
plt.plot(dates_list, last_week_usd, label = 'USD')
plt.plot(dates_list, last_week_cny, label = 'CNY')
plt.title('Курс евро, доллара, юаня за последние 7 дней')
plt.xlabel('Дата')
plt.ylabel('Курс в рублях')
plt.legend(loc='best')
plt.xticks(rotation=45, horizontalalignment='right')
plt.grid()
plt.show()


