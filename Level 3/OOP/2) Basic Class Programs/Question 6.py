Shopping = __import__('Question 5').Shopping

cart = Shopping('Walmart')

cart.add_cart('milk', 3)
cart.add_cart('bread', 1)
cart.add_cart('eggs', 5)
cart.add_cart('chips', 4)
cart.add_cart('apples', 4)
cart.add_cart('bananas', 3)

cart.remove_cart('milk', 1)
cart.remove_cart('eggs', 5)
cart.remove_cart('apples', 2)

print(cart.cart)
