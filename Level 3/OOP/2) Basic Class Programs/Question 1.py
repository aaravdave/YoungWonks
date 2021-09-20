class Shape:
	def __init__(self, sides, name):
		self.sides = sides
		self.name = name

rectangle = Shape(4, 'rectangle')
triangle = Shape(3, 'triangle')
circle = Shape(0, 'circle')
pentagon = Shape(5, 'pentagon')

for shape in [rectangle, triangle, circle, pentagon]:
	print(shape.name, shape.sides)
