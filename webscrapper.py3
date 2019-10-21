import datetime
import requests
from prettytable import PrettyTable
from bs4 import BeautifulSoup

# Usando BeautifulSoup, busco el HTML que me interesa.
page = requests.get("http://www.alianzapetrolerafc.com/news.html")
soup = BeautifulSoup(page.content, 'html.parser')
articulos = soup.select('.articulo-big')

# Preparo una tabla para mostrar la información.
t = PrettyTable(['Titulo', 'Fecha', 'Src'])
t.align["Titulo"] = "l"
t.align["Fecha"] = "l"

# Tomo la fecha, porque voy a usar el año como variable más adelante.
año = datetime.datetime.now().year

# Muestro las últimas 10 noticias.
for art in articulos[:10]:
	fecha = art.h1.get_text().replace('Barrancabermeja, ', '').replace(' de ' + str(año) + '.', '')
	link = "http://www.alianzapetrolerafc.com/" + art.a.get('href')
	titulo = art.a.p.get_text()

	t.add_row([titulo, fecha, link])

print(t)