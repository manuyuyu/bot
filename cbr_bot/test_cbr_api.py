charcodes = ['EUR', 'USD']
date_req = "06/12/2022"

currencies = get_currency_rates(charcodes, date_req)
eur = currencies['EUR']
usd = currencies['USD']

print(f"Курсы валют. Евро = {eur.value}, Доллар = {usd.value}")