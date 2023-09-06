import requests
from bs4 import BeautifulSoup as bs
from django.views.decorators.csrf import csrf_exempt

URL = 'https://filmix.ac/'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',

}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

@csrf_exempt
def get_data(html):
    soup = bs(html, 'html.parser')
    items = soup.find_all('article', class_='shortstory line')
    filmix = []

    for item in items:
        filmix.append(
            {
                'title_text': item.find('div', class_='name-block').get_text(),
                'title_url': item.find('a', class_='watch icon-play').get('href'),
                'image': item.find('a', class_='fancybox').find('img').get('src')
            }
        )

    return filmix

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        filmix2 = []
        for page in range(0, 1):
            html = get_html(f'https://filmix.ac/films/boevik/', params=page)
            filmix2.extend(get_data(html.text))
            return filmix2
            # print(filmix2)
    else:
        raise Exception('Ошибка!!!')

# parser()