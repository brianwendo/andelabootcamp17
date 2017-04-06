class fashion:
	tag_price = 0

	def __init__(self,designer,gender,size,origin,material,year):
		self.designer = designer
		self.gender = gender
		self.size = size
		self.origin = origin
		self.material = material
		self.year = year


	def price(self):
		if self.year == 2017:
			tag_price += 10000
			return tag_price
		elif self.year >= 2012:
			tag_price -= 5000
			return tag_price
		else:
			print('Sorry. Out of Stock')

	def return_price(self):
		if self.year == 2017:
			tag_price = tag_price/2
			return tag_price
		elif self.year >= 2012:
			tag_price = tag_price/ (2017 - self.year)
			return tag_price
		else:
			print('Sorry we don\'t accept those')

	def designer_made(self):
		if self.designer == 'Foreign':
			tag_price += 5000
		else:
			return tag_price

	def material_made(self):
		if self.material == 'Silk':
			tag_price += 5000
			return tag_price
		elif self.material == 'Wool':
			tag_price += 2500
			return tag_price
		else:
			return tag_price

	def size_made(self):
		if self.size == 42:
			tag_price += 2500
			return tag_price
		elif self.size >= 36 and self.size <= 41:
			tag_price += 2000
			return tag_price
		else:
			return tag_price

	def country_made(self):
		if self.origin == 'United States':
			tag_price +=2500
			return tag_price
		elif self.origin == 'China':
			tag_price -=2500
		else:
			return tag_price 
	def sex_type(self):
		if self.gender == 'woman':
			tag_price -= 2500
			return tag_price
		elif self.gender == 'child':
			tag_price  -= 3000
			return tag_price
		else:
			return tag_price

"""	def cloth_type(self):
		print(" Suits, Dresses, Sweaters, Shirts, Trousers, Jumpers available from %s shillings." % suits.tag_price)

class store_location(fashion): 
	def street(self):
		print("Waiyaki Way, Mombasa Rd, Langata Rd, CBD, Thiks Rd")

class name(store_location):
	def brand(self):
		print("Deacons, Nakumatt, Style Up, Clothes Dont Lie")"""


suits = fashion('Foreign', 'man', 42, 'China', 'Silk', 2017)

