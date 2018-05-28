import requests
from bs4 import BeautifulSoup

http_proxy  = "http://10.90.1.5:80"
https_proxy = "https://10.90.1.5:80"
ftp_proxy   = "ftp://10.90.1.5:80"

proxyDict = {
              "http"  : http_proxy,
              "https" : https_proxy,
              "ftp"   : ftp_proxy
            }

print("hace el request")
page = requests.get("http://www.alianzapetrolerafc.com/news.html", proxies=proxyDict)
print("parsea")
soup = BeautifulSoup(page.content, 'html.parser')

articulos = soup.select('.articulo-big a p')
"""noticias = [art.get_text() for art in articulos]"""
for art in reversed(articulos):
    print art.get_text()

print("fin")


""" articulo-big > a > p"""