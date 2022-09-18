
products_list = []

number = int(input(('Enter The Total Number of Products :')))

if number >= 0:

    for i in range(number):
        products = {
        "product_name" : str(input("Enter Product Name:")),
        "product_qty" : int(input("enter product_qty :")),
        "product_price" : int(input("enter product_price :"))

        }
        products_list.append(products)


print(products_list)


def search_product(name,your_list):

    for i in products_list:
        if name in i["product_name"]:
            return i

    return "no products"

name = str(input('enter name :'))


print(search_product(name,products_list))
