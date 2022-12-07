import requests
import xml.etree.ElementTree as ElementTree

class Currency:
    name = ""
    value = ""
    charcode = ""

def get_currency_rates(charcodes, date_req_date = None):
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    
    if date_req_date is not None:
        url += f"?date_req={date_req_date.strftime('%d/%m/%Y')}"

    r = requests.get(url)
    r.raise_for_status()

    tree = ElementTree.fromstring(r.content)

    curencies = {}

    for valute in tree:
        charcode = valute.find('CharCode').text
        if charcode in charcodes:
            currency = Currency()
            currency.name = valute.find('Name').text
            currency.value = valute.find('Value').text
            currency.charcode = charcode

            curencies[charcode] = currency

    return curencies