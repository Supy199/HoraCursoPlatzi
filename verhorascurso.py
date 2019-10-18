import bs4

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

print('Agrega url curso:')
url = input()

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
data=urlopen(req).read()

page = soup(data, "html.parser")

containers = page.findAll("article",{"class":"Material"})

horas = []

for container in containers:
	hora = container.findAll("span",{"class":"MaterialContent-duration"})
	tiempos = hora[0].text
	tiemp = tiempos.replace("min",'')
	tiem = tiemp.replace("00",'')
	real = tiem.replace(":",'')
	
	horas.append(int(real))

horas = sum(horas)

total = horas / 60

print("las horas del curso son = " + str(total))
