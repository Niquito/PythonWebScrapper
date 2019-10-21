import requests
from bs4 import BeautifulSoup

page = requests.get("http://www.alianzapetrolerafc.com/news.html")
soup = BeautifulSoup(page.content, 'html.parser')
articulos = soup.select('.articulo-big')

for art in articulos[:10]:
	fecha = art.h1.get_text()
	fecha = fecha.replace('Barrancabermeja, ', '')
	link = "http://www.alianzapetrolerafc.com/" + art.a.get('href')
	titulo = art.a.p.get_text()

	print(titulo + " - " + fecha + " - " + link)