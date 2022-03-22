from bs4 import BeautifulSoup
import requests

from Profiles import SignatureBlend
from Profiles import SingleOrigin


def get_site_info(url):
    result = requests.get(url)
    return BeautifulSoup(result.text, 'html.parser')


def get_availability(inStock):
    if (inStock):
        return 'In Stock'
    else:
        return 'Sold Out'


def get_single_origin_coffee():
    doc = get_site_info('https://www.whitepinecoffee.com/private-reserve')

    productList = doc.find(id='productList')
    products = productList.find_all(class_='product')

    coffeeList = []

    for product in products:
        inStock = product.find(class_='sold-out') == None

        doc = get_site_info(
            'https://www.whitepinecoffee.com' + product['href'])

        productExcerpt = doc.find(class_='product-excerpt')
        excerptElements = productExcerpt.find_all('strong')

        origin = excerptElements[2].parent.text
        roast = excerptElements[1].parent.text
        processing = excerptElements[6].parent.text
        notes = excerptElements[0].parent.text

        coffeeList.append(SingleOrigin(
            origin, roast, processing, notes, inStock))

    print("Single Origin Coffee:")

    i = 0

    for coffee in coffeeList:
        print(f' Availability: {get_availability(coffee.inStock)} \
            \n {coffee.origin} \
            \n {coffee.roast} \
            \n {coffee.processing} \
            \n {coffee.origin} \
            \n {coffee.notes}\n')

        i += 1


def get_signature_blend_coffee():
    doc = get_site_info('https://www.whitepinecoffee.com/wpcblends')

    productList = doc.find(id='productList')
    products = productList.find_all(class_='product')

    coffeeList = []

    for product in products:
        inStock = product.find(class_='sold-out') == None

        productTitle = str(product.find(class_='product-title').string)

        productNameIndex = int(productTitle.find('-'))
        productName = productTitle[0:productNameIndex]

        roastProfile = productTitle[productNameIndex + 1:len(productTitle)]

        coffeeList.append(SignatureBlend(productName, roastProfile, inStock))

    print("\nWPC Signature Blends:")

    i = 0
    for coffee in coffeeList:
        print(f' Availability: {get_availability(coffee.inStock)} \
            \n Name: {coffee.name} \
            \n Roast:{coffee.roast}\n')

        i += 1


get_signature_blend_coffee()
get_single_origin_coffee()
