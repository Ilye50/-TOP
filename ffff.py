import pygame, random
pygame.init()

dispWidth = 1200
dispHight = 600
disp = pygame.display.set_mode((dispWidth,dispHight))
pygame.display.set_caption("Der Grosse schlange")

white = (255,255,255)
green = (0,255,0)
red = (255,0,0)

bodyImg = pygame.image.load("body.png")
foodImg = pygame.image.load("food.png")
rockImg = pygame.image.load("rock.png")

snakeBlock = 50
snakeX = dispWidth / 2
snakeY = dispHight / 2
snakeChangeX = 0
snakeChangeY = 0
snakeSpeed = 10

snakeList = []
lengthSnake = 1

foodX = round(random.randrange(0, dispWidth - snakeBlock) / snakeBlock) * snakeBlock
foodY = round(random.randrange(0, dispHight - snakeBlock) / snakeBlock) * snakeBlock

rockX = round(random.randrange(0,dispWidth - snakeBlock) / snakeBlock) * snakeBlock
rockY = round(random.randrange(0,dispHight - snakeBlock) / snakeBlock) * snakeBlock
gameOver = False

clock = pygame.time.Clock()
def drawSnake(snakeBlock,snakeList):
	for i in snakeList:
		# pygame.draw.rect(disp, green, [i[0], i[1], snakeBlock, snakeBlock])
		disp.blit(bodyImg,[i[0], i[1], snakeBlock, snakeBlock])
while not gameOver:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				snakeChangeX = 0
				snakeChangeY = -snakeBlock
			elif event.key == pygame.K_s:
				snakeChangeX = 0
				snakeChangeY = snakeBlock
			elif event.key == pygame.K_a:
				snakeChangeX = -snakeBlock
				snakeChangeY = 0
			elif event.key == pygame.K_d:
				snakeChangeX = snakeBlock
				snakeChangeY = 0
	if snakeX >= dispWidth or snakeX < 0 or snakeY >= dispHight or snakeY <0:
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
	
	drawSnake(snakeBlock,snakeList)
	disp.blit(foodImg,[foodX,foodY,snakeBlock,snakeBlock])
	
	"""disp.blit((rockImg,[rockX,rockY,snakeBlock,snakeBlock]))"""
	
	pygame.display.update()
	if snakeX == foodX and snakeY == foodY:
		foodX = round(random.randrange(0, dispWidth - snakeBlock) / snakeBlock) * snakeBlock
		foodY = round(random.randrange(0, dispHight - snakeBlock) / snakeBlock) * snakeBlock
		lengthSnake += 1
	
	if snakeX == rockX and snakeY == rockY:
		gameOver = True
	clock.tick(snakeSpeed)