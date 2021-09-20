import object
import random
import pygame
pygame.init()

def text(message, x, y, color, size, bold=False, italic=False):
    font = pygame.font.Font('/System/Library/Fonts/Avenir.ttc', size, bold=bold, italic=italic)
    message = font.render(message, False, color)
    screen.blit(message, (x, y))

def choose_trade(do_promote=False):
	global order, promote
	order = [random.choice(companies), random.choice(list(tertiary)), random.randint(1, 3), random.randint(100000, 500000)]
	if do_promote:
		promote = [True, 80, random.randint(10, 30)]

def run_factory(number, source, end):
	global open_window, open_chooser, window_release, chooser_release

	slots = []
	for x in range(50, 651, 150):
		slots.append(pygame.draw.rect(screen, (150, 150, 150), (x, 200, 100, 100)))

	if clicked and not open_chooser:
		for slot in slots:
			if slot.collidepoint(mouse):
				if not factories[number][slots.index(slot)]:
					open_chooser = slots.index(slot) + 1
				break
		else:
			open_window = ''
			window_release = False
	
	if open_chooser and not clicked and not chooser_release:
		chooser_release = True

	if open_chooser and chooser_release:
		transparent = pygame.Surface((800, 600), flags=pygame.SRCALPHA)
		pygame.draw.rect(transparent, (0, 0, 0, 75), (0, 0, 800, 600))
		screen.blit(transparent, (0, 0))
		pygame.draw.rect(screen, (150, 150, 150), slots[open_chooser - 1])

		items = []
		for x in range(50, end, 150):
			items.append(pygame.draw.rect(screen, (150, 150, 150), (x, 350, 100, 100)))
		
		if number == 0:
			screen.blit(plastic, (60, 370))
			screen.blit(iron, (210, 370))
			screen.blit(water, (360, 370))
			screen.blit(electronic_parts, (515, 370))
		elif number == 1:
			screen.blit(plastic_bottle, (60, 370))
			screen.blit(plastic_container, (210, 370))
			screen.blit(paint, (360, 370))
			screen.blit(computer_chip, (515, 370))
			screen.blit(display, (665, 370))
		elif number == 2:
			screen.blit(water_bottle, (60, 370))
			screen.blit(car, (210, 370))
			screen.blit(appliance, (360, 370))
			screen.blit(laptop, (515, 370))
			

		if clicked:
			for item in items:
				if item.collidepoint(mouse):
					if number > 0:
						ingredients = source[list(source)[items.index(item)]][1]
						for ingredient in ingredients:
							if inventory.count(ingredient) < ingredients[ingredient]:
								break
						else:
							factories[number][open_chooser - 1] = [list(source)[items.index(item)], object.Timer()]
							open_window, window_release = '', False
							open_chooser, chooser_release = '', False
					else:
						factories[number][open_chooser - 1] = [list(source)[items.index(item)], object.Timer()]
						open_window, window_release = '', False
						open_chooser, chooser_release = '', False
					break

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tradify')

companies = ['Mega Tech', 'Big Brain', 'Innovation Corp', 'Pacific Union', 'Glacier Products']
inventory = []
money = 0

factories = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]
open_window, window_release = '', False
open_chooser, chooser_release = '', False

primary = {'Plastic': 0.25, 'Iron': 0.25, 'Water': 0.325, 'Electronic Part': 0.5}
secondary = {'Plastic Bottle': [0.5, {'Plastic': 2}], 'Plastic Container': [0.625, {'Plastic': 3}], 'Paint': [0.5, {'Water': 2, 'Iron': 1}], 'Computer Chip': [1, {'Electronic Part': 3}], 'Display': [1.25, {'Electronic Part': 4}]}
tertiary = {'Water Bottle': [0.75, {'Plastic Bottle': 1, 'Water': 2}], 'Car': [2, {'Iron': 3, 'Paint': 2, 'Computer Chip': 1, 'Display': 3}], 'Appliance': [1.5, {'Iron': 2, 'Plastic Container': 2, 'Computer Chip': 1, 'Display': 1}], 'Laptop': [3, {'Iron': 1, 'Electronic Part': 6, 'Computer Chip': 2, 'Display': 2}]}

order = ['Practice', 'Water Bottle', 1, 100]
promote = [False, 0, 0]
# Order contains: [company, item, quantity, price]
# Promote contains: [True/False, time, percent]

mouse = [0, 0]
clicked = 0
help = 1

plastic = pygame.transform.rotozoom(pygame.image.load('Plastic.png'), 0, 0.15)
iron = pygame.transform.rotozoom(pygame.image.load('Iron.png'), 0, 0.15)
water = pygame.transform.rotozoom(pygame.image.load('Water.png'), 0, 0.15)
electronic_parts = pygame.transform.rotozoom(pygame.image.load('Electronic-Parts.png'), 0, 0.15)

plastic_bottle = pygame.transform.rotozoom(pygame.image.load('Plastic-Bottle.png'), 0, 0.15)
plastic_container = pygame.transform.rotozoom(pygame.image.load('Plastic-Container.png'), 0, 0.15)
paint = pygame.transform.rotozoom(pygame.image.load('Paint.png'), 0, 0.15)
computer_chip = pygame.transform.rotozoom(pygame.image.load('Computer-Chip.png'), 0, 0.15)
display = pygame.transform.rotozoom(pygame.image.load('Display.png'), 0, 0.15)

water_bottle = pygame.transform.rotozoom(pygame.image.load('Water-Bottle.png'), 0, 0.4)
car = pygame.transform.rotozoom(pygame.image.load('Car.png'), 0, 0.4)
appliance = pygame.transform.rotozoom(pygame.image.load('Appliance.png'), 0, 0.4)
laptop = pygame.transform.rotozoom(pygame.image.load('Laptop.png'), 0, 0.4)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.MOUSEMOTION:
			mouse = event.pos
		elif event.type == pygame.MOUSEBUTTONUP:
			clicked = 0
		elif event.type == pygame.MOUSEBUTTONDOWN:
			clicked = 1
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				help = 1 - help
	
	screen.fill((100, 200, 255))

	if help:
		text('For charts and crafting guides, see CRAFT.png.', 10, 10, (255, 255, 255), 20)
		text('Press [space] to play.', 10, 40, (255, 255, 255), 20)
		text('Press [space] to come back to this page.', 10, 70, (255, 255, 255), 20, False, True)
		pygame.display.update()
		continue

	text(order[0], 10, 10, (255, 255, 255), 20, True)
	text(f'{order[2]} {order[1]}', 10, 40, (255, 255, 255), 20)
	text(f'${order[3]}', 10, 70, (255, 255, 255), 20, False, True)
	text(f'You have ${money}.', 10, 130, (255, 255, 255), 20)


	# Trade
	if inventory.count(order[1]) < order[2]:
		pygame.draw.rect(screen, (0, 100, 0), (200, 30, 100, 50))
	else:
		ok_rect = pygame.draw.rect(screen, (50, 200, 50), (200, 30, 100, 50))
		if clicked and ok_rect.collidepoint(mouse):
			for _ in range(order[2]):
				inventory.remove(order[1])
			money += order[3]
			choose_trade()
	text('OK', 235, 43, (255, 255, 255), 20, True)
	

	# GUI

	primary_rect = pygame.draw.rect(screen, (150, 150, 150), (200, 200, 100, 100))  # primary
	secondary_rect = pygame.draw.rect(screen, (150, 150, 150), (350, 200, 100, 100))  # secondary
	tertiary_rect = pygame.draw.rect(screen, (150, 150, 150), (500, 200, 100, 100))  # tertiary

	if clicked and not open_window:
		if primary_rect.collidepoint(mouse):
			open_window = 'primary'
		elif secondary_rect.collidepoint(mouse):
			open_window = 'secondary'
		elif tertiary_rect.collidepoint(mouse):
			open_window = 'tertiary'
	
	if open_window and not clicked and not window_release:
		window_release = True

	if open_window and window_release:
		transparent = pygame.Surface((800, 600), flags=pygame.SRCALPHA)
		pygame.draw.rect(transparent, (0, 0, 0, 75), (0, 0, 800, 600))
		screen.blit(transparent, (0, 0))

		if open_window == 'primary':
			run_factory(0, primary, 501)
		elif open_window == 'secondary':
			run_factory(1, secondary, 651)
		elif open_window == 'tertiary':
			run_factory(2, tertiary, 501)
	

	# Engine

	for slot in factories[0]:
		if slot and slot[1].get() / 1000 >= primary[slot[0]] * 60:
			inventory.append(slot[0])
			factories[0][factories[0].index(slot)] = ''

	for slot in factories[1]:
		if slot and slot[1].get() / 1000 >= secondary[slot[0]][0] * 60:
			inventory.append(slot[0])
			factories[1][factories[1].index(slot)] = ''

	for slot in factories[2]:
		if slot and slot[1].get() / 1000 >= tertiary[slot[0]][0] * 60:
			inventory.append(slot[0])
			factories[2][factories[2].index(slot)] = ''

	pygame.display.update()
