class Shopping:
	def __init__(self, shop):
		self.shop = shop
		self.cart = {}
	
	def add_cart(self, item, quantity):
		if item in self.cart:
			self.cart[item] += quantity
		else:
			self.cart[item] = quantity
	
	def remove_cart(self, item, quantity):
		if item in self.cart:
			self.cart[item] -= quantity
			if self.cart[item] <= 0:
				self.cart.pop(item)
