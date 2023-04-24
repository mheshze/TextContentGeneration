from bs4 import BeautifulSoup
import requests
import re

def read_pages(url, filt=['h1', 'p']):
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'lxml')
    results = soup.find_all(filt)

    text = [result.text for result in results]
    ARTICLE = ' '.join(text)
    #     art = [x + " " for x in ARTICLE.replace("\xa0"," ").splitlines() if x != "" ]
    art = [x + " " for x in re.sub(r"\x0f|\x15|\xa0", " ", ARTICLE).splitlines() if x != ""]

    return "".join(art).strip()
