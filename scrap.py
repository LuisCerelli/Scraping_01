# Este codigo es para sacar palabras directamente: 

import requests
from bs4 import BeautifulSoup

for num in range(15,30):

    url = f'http://www.soria-goig.org/fuentesymanantialesdesoria/ftes00{num}.htm'

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        word = 'habilitado'

        if word in soup.get_text().lower():
            print(f'Se encuentra la palabra {word} en la url {url}')

    else:
        print('Error , no se puede acceder a la página')        