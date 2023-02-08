from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://listado.mercadolibre.com.co/microfono#D[A:microfono]').text
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find_all("li", class_= "ui-search-layout__item shops__layout-item")
for product in products:
    #print(products.prettify())
    name = product.find("h2", class_ = "ui-search-item__title shops__item-title").text

    price = product.find("span", class_ ="price-tag-text-sr-only").text


    print("----------------")
    print(price)
    print(name)
    print("----------------")
