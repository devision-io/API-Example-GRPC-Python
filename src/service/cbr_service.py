import requests
from datetime import datetime
from xml.etree import ElementTree as ET


def get_rates(date: str):
    # Если у вас зреет api v2 вы можете вынести Бизнес логику в отдельный файл-сервис и вызывать его отсюда
    d = datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
    url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req={d}".format(d=d)
    r = requests.get(url)
    valuta = ET.fromstring(r.text)

    rates = []
    for line in valuta.findall('Valute'):
        char_code = line.find('CharCode').text
        name = line.find('Name').text
        rub = line.find('Value').text
        nom = line.find('Nominal').text
        rate = float(rub.replace(',', '.')) / float(nom)
        rates.append({
            "rate": rate,
            "name": name,
            "char_code": char_code,
        })
    return rates
