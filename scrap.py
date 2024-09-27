import requests
from bs4 import BeautifulSoup

url = 'http://www.soria-goig.org/fuentesymanantialesdesoria/ftes0015.htm'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    word = 'pintura'

    if word in soup.get_text().lower():
        print(f'Se encuentra la palabra {word} en la url {url}')

else:
    print('Error , no se puede acceder a la página')        