import requests
from bs4 import BeautifulSoup
import re
import urllib.request

csv_link = BeautifulSoup(requests.get("https://datos.cdmx.gob.mx/tl/dataset/matrimonios-registrados-en-la-ciudad-de-mexico").text, 'html.parser').find('a', href=re.compile(r'\.csv$')).get('href')

urllib.request.urlretrieve(csv_link, "Matrimonios2010-2023.csv")
