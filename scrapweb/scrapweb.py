#!/usr/bin/env python

class Juego():
    def __init__(self,titulo,precio,etiquetas,plataformas):
        self.titulo=titulo
        self.precio=precio
        self.etiquetas=etiquetas
        self.plataformas=plataformas

import requests
import lxml.html

html = requests.get ('https://store.steampowered.com/explore/new/')

#print(html.content)

doc = lxml.html.fromstring(html.content)

newReleases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]

#print(newReleases)

tittles=newReleases.xpath('.//div[@class="tab_item_name"]/text()')

#print(tittles)

prices = newReleases.xpath('.//div[@class="discount_final_price"]/text()')

#print(prices)

tags = newReleases.xpath('.//div[@class="tab_item_top_tags"]')

totalTags=[]

for tag in tags:
    totalTags.append(tag.text_content())

totalTags = [tag.split(', ') for tag in totalTags]

#print(totalTags)

platformsDiv = newReleases.xpath('.//div[@class="tab_item_details"]')

totalPlatforms=[]

for game in platformsDiv:
    namePlatform = game.xpath('.//span[contains(@class, "platform_img")]')
    platforms=[t.get('class').split(' ')[-1] for t in namePlatform]
    if 'had_separator' in platforms:
        platforms.remove('had separator')
    totalPlatforms.append(platforms)

#print(totalPlatforms)

output = []

for info in zip(tittles,prices,totalTags,totalPlatforms):
    response={}
    response['tittle']=info[0]
    response['price']=info[1]
    response['tags']=info[2]
    response['platforms']=info[3]
    output.append(response)

#print(output)

contador=1

for info in zip(tittles,prices,totalTags,totalPlatforms):
    juego1=Juego(info[0],info[1],info[2],info[3])
    print("----------------------------------------------")
    print("Juego "+str(contador))
    contador=contador+1
    print("Titulo: "+ juego1.titulo)
    print("Precio: "+ juego1.precio)
    print("Etiquetas: "+ str(juego1.etiquetas))
    print("Plataformas: "+ str(juego1.plataformas))
    print("----------------------------------------------")