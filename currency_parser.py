import requests
from bs4 import BeautifulSoup

def get_usd_exchange_rate() -> float:
    url = "https://minfin.com.ua/ua/currency/usd/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    rate_block = soup.find("div", class_="sc-1x32wa2-9 bKmKjX")  
    rate_text = rate_block.text.strip().replace(",", ".")
    rate_text = rate_text.split('-')[0]
    return round(float(rate_text),2)


def convert_to_usd(number:float):
    return round( number / get_usd_exchange_rate(),2)
