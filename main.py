sales = []

def register_sale(product, quantity, price):
    sale = {
        "product": product,
        "quantity": quantity,
        "price": price
    }
    sales.append(sale)
    print("Sale registered:", product)

def show_sales():
    print("\nCurrent sales:")
    for s in sales:
        print(s["product"], "-", s["quantity"], "units")

register_sale("Coffee", 2, 15)
register_sale("Milk", 3, 4)

show_sales()
