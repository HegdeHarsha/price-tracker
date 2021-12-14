import requests
from bs4 import BeautifulSoup

products_to_track = [
    {
        "product_url": "https://www.amazon.in/Samsung-Galaxy-Ocean-128GB-Storage/dp/B07HG8S7KP/ref=sr_1_1?dchild=1&keywords=samsung+m31&qid=1631950403&sr=8-1",
        "name": "Samsung M31",
        "target_price": 16000
    },
    {
        "product_url": "https://www.amazon.in/Redmi-Pro-Black-64GB-Storage/dp/B07DJHXWZZ/ref=sr_1_1?dchild=1&keywords=mi+6+pro&qid=1631952830&sr=8-1",
        "name": "Red mi 6 pro",
        "target_price": 9000
    },
    {
        "product_url": "https://www.amazon.in/Renewed-ASUS-Zenfone-64gb-Grey/dp/B07KFFV4BQ/ref=sr_1_5?crid=3TKTJ23M1O3NU&dchild=1&keywords=asus+mobile&qid=1631952906&sprefix=asus%2Caps%2C520&sr=8-5",
        "name": "Asus renewed",
        "target_price": 11000
    },
    {
        "product_url": "https://www.amazon.in/Samsung-Galaxy-Ocean-128GB-Storage/dp/B07HG8S7KP/ref=sr_1_1?dchild=1&keywords=samsung+m31&qid=1631950403&sr=8-1",
        "name": "Samsung M series",
        "target_price": 16000
    },
    {
        "product_url": "https://www.amazon.in/Redmi-Pro-Black-64GB-Storage/dp/B07DJHXWZZ/ref=sr_1_1?dchild=1&keywords=mi+6+pro&qid=1631952830&sr=8-1",
        "name": "Red mi 6 ",
        "target_price": 14000
    }
]

def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find(id="priceblock_ourprice")
    if product_price is None:
        product_price = soup.find(id="priceblock_ourprice")

    return product_price.getText()


result_file = open('my_result_file.txt', 'w')


try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + " - " + every_product.get("name"))

        my_product_price = product_price_returned[1:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))

        print(my_product_price)
        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get(
                "name") + ' -  \t' + ' Available at Target Price ' + ' Current Price - ' + str(my_product_price) + '\n')

        else:
            print("Still at current price")

finally :
    result_file.close()

