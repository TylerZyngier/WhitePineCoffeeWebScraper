from bs4 import BeautifulSoup
import requests
import sys
import os

from Coffee import SignatureBlend
from Coffee import SingleOrigin


def get_site_info(url):
    result = requests.get(url)
    return BeautifulSoup(result.text, 'html.parser')


def get_availability(inStock):
    return 'In Stock' if inStock else 'Sold Out'


def get_single_origin_coffee():
    doc = get_site_info('https://www.whitepinecoffee.com/private-reserve')

    productList = doc.find(id='productList')

    if (productList == None):
        print('Web request failed for Single Origin product list\n')
        return None

    products = productList.find_all(class_='product')

    coffeeList = []

    print("Single Origin Coffee")

    for product in products:
        inStock = product.find(class_='sold-out') == None

        productLink = 'https://www.whitepinecoffee.com' + product['href']

        doc = get_site_info(productLink)

        productExcerpt = doc.find(class_='product-excerpt')

        if (productExcerpt == None):
            print(f' Web request failed for \'{productLink}\'\n')
            continue

        excerptElements = productExcerpt.find_all('strong')

        origin = excerptElements[2].parent.text
        roast = excerptElements[1].parent.text
        processing = excerptElements[6].parent.text
        notes = excerptElements[0].parent.text

        coffeeList.append(SingleOrigin(
            origin, roast, processing, notes, inStock))

    for coffee in coffeeList:
        print(f' Availability: {get_availability(coffee.inStock)} \
            \n {coffee.origin} \
            \n {coffee.roast} \
            \n {coffee.processing} \
            \n {coffee.origin} \
            \n {coffee.notes}\n')


def get_signature_blend_coffee():
    doc = get_site_info('https://www.whitepinecoffee.com/wpcblends')

    productList = doc.find(id='productList')

    if (productList == None):
        print('Web request failed for WPC Singature product list\n')
        return None

    products = productList.find_all(class_='product')

    coffeeList = []

    print("WPC Signature Blends:")

    for product in products:
        inStock = product.find(class_='sold-out') == None

        productTitle = str(product.find(class_='product-title').string)

        productNameIndex = int(productTitle.find('-'))
        productName = productTitle[0:productNameIndex]

        roastProfile = productTitle[productNameIndex + 1:len(productTitle)]

        coffeeList.append(SignatureBlend(productName, roastProfile, inStock))

    for coffee in coffeeList:
        print(f' Availability: {get_availability(coffee.inStock)} \
            \n Name: {coffee.name} \
            \n Roast:{coffee.roast}\n')


def clear_console():
    os.system('cls')


while(True):
    print("Enter 1 to view WPCs Signature Blends \
    \nEnter 2 to view Single Origin Coffee \
    \nEnter 3 to close program")

    userInput = input("\nInput: ")

    clear_console()

    if userInput == '1':
        get_signature_blend_coffee()
    elif userInput == '2':
        get_single_origin_coffee()
    elif userInput == '3':
        sys.exit()
