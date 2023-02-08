from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://listado.mercadolibre.com.co/microfono#D[A:microfono]').text
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find("li", class_= "ui-search-layout__item shops__layout-item")
#print(products.prettify())
name = products.find("h2", class_ = "ui-search-item__title shops__item-title").text

price = products.find("span", class_ ="price-tag-text-sr-only").text



print(price)

print(name)

