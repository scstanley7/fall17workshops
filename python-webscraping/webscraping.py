from bs4 import BeautifulSoup
from contextlib import closing
from urllib import request

readme_URL = "https://github.com/scstanley7/fall17workshops/tree/master/python-webscraping/html"
html = request.urlopen(readme_URL).read()
soup = BeautifulSoup(html, 'lxml')
ota_links = soup.select("ul#ota-links a")
print(ota_links)

readme_URL = "https://github.com/scstanley7/fall17workshops/tree/master/python-webscraping/html"
html = request.urlopen(readme_URL).read()
soup = BeautifulSoup(html, 'lxml')
ws_links = soup.select("ul#ws-links a")

ws_urls = []
for link in ota_links:
  ws_url = link['href']
  ws_urls.append(ws_url)
  
print(ws_urls)

texts = []
for ws_url in ws_urls:
    print(url)
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    text = soup.text.replace('\n', '')
    text = soup.text[0:1000]
    texts.append(text)
# print out the contents of the thing
print(corpus_texts)