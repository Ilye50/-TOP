"""
()
**
-+ Унарные
* / // %
-+
== =! > < >= <= is is_not in not_in
not
and
or
"""
"""chislo1 = 12
chislo2 = 3.4
bool = True #False
string1 = "qweasdzxc"""
"""import math
while True:
	try:
		d = int(input("Введите диаметр окружности: "))
		raise ZeroDivisionError
		vibor = int(input("Что нужно найти?"
		                  "\n\t1)Площадь"
		                  "\n\t2)Периметр\n\t"))
		break
	except SyntaxError:
		pass
	except ValueError:
		print("error")
		continue
	finally:
		break
		
while vibor < 1 or vibor > 2:
	vibor = int(input("Что нужно найти?"
	                  "\n\t1)Площадь"
	                  "\n\t2)Периметр\n\t"))
if vibor == 1:
	print(f"Площадь окружности = {round(math.pi * (d / 2) ** 2)}")
else:
	print(f"Периметр окружности = {round(d * math.pi)}")
	"""
"""while True:
	while True:
		try:
			N1 = int(input("Введите число: "))
		except ValueError:
			print("Error\n")
			break
		if N1 % 7 == 0:
			print("Number is multiple 7\n")
		else:
			print("Number is not multiple 7\n")
		break"""

import pygame , random
pygame.init()

dispWidht = 600
dispHight = 600
disp = pygame.display.set_mode((dispWidht,dispHight))
pygame.display.set_caption("Games")

white = (255,255,255)
green = (0,255,0)
red = (255,0,0)

bodyImg = pygame.image.load("body.png")
foodImg = pygame.image.load("food.png")
rockImg = pygame.image.load("rock.png")

snakeBlock = 10
snakeX = dispWidht / 2
snakeY = dispHight / 2

snakeChangeX = 0
snakeChangeY = 0
snakeSpeed = 15

foodX = round(random.randrange(0, dispWidht - snakeBlock) / snakeBlock) * snakeBlock
foodY = round(random.randrange(0, dispHight - snakeBlock) / snakeBlock) * snakeBlock

snakeList = []
lengthSnake = 1

gameOver = False

clock = pygame.time.Clock()
def drawSnake(snakeBlock, snakeList):
	for i in snakeList:
		"""pygame.draw.rect(disp, green, [i[0], i[1], snakeBlock, snakeBlock])"""
		disp.blit(bodyImg)

while not gameOver:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				snakeChangeX = 0
				snakeChangeY = -snakeSpeed
			elif event.key == pygame.K_s:
				snakeChangeX = 0
				snakeChangeY = snakeSpeed
			elif event.key == pygame.K_a:
				snakeChangeX = -snakeBlock
				snakeChangeY = 0
			elif event.key == pygame.K_d:
				snakeChangeX = snakeBlock
				snakeChangeY = 0
	if snakeX >= dispWidht or snakeX < 0 or snakeY >= dispHight or snakeY < 0:
		gameOver = True
	disp.fill(white)
	snakeX += snakeChangeX
	snakeY += snakeChangeY
	snakeHead = []
	snakeHead.append(snakeX)
	snakeHead.append(snakeY)
	snakeList.append(snakeHead)
	if len(snakeList) > lengthSnake:
		del snakeList[0]
	for i in snakeList[:-1]:
		if i == snakeHead:
			gameOver = True
	
	disp.blit(foodImg,[foodX,foodY,snakeBlock,snakeBlock])
	
	drawSnake(snakeBlock,snakeList)
	
	pygame.display.update()
	if snakeX == foodX and snakeY == foodY:
		foodX = round(random.randrange(0, dispWidht - snakeBlock) / snakeBlock) * snakeBlock
		foodY = round(random.randrange(0, dispHight - snakeBlock) / snakeBlock) * snakeBlock
		lengthSnake += 1
	clock.tick(snakeSpeed)
	
