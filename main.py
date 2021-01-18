import datetime
import os
from bs4 import BeautifulSoup
import requests

headers = {
    "user-agent": "curl/7.74.0",
    "Host": "www.decathlon.fr",
    "accept": "*/*"
}

r = requests.get("https://www.decathlon.fr/p/disque-de-fonte-musculation-28-mm/_/R-p-7278?mc=1042303", headers=headers)

needed = [5.0, 10.0]

soup = BeautifulSoup(r.text, 'html.parser')

for item in soup.find_all("li", class_="sizes__size"):
    size = float(item.find("span", class_="sizes__info").get_text().split(" KG")[0].replace(",", "."))
    available = int(item.find("span", class_="sizes__stock__info").get_text())
    now = datetime.datetime.now()
    time = "{:02d}h{:02d}".format(now.hour, now.minute)

    if size in needed and available > 0:
        os.system("notify-send --urgency critical \"Decathlon at {}\" \"{} items available for {} kg\"".format(time, available, size))

