import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1600, 1400))

x = 50
y = 700
speed = 5
dec_height = 2
running = True
jumping = False
jumpCount = 10
PILLCOL = (255, 255, 0)
pill_width = 300
pill_up_height = 700
pill_down_height = 800
pill_down_y = 1000
score = 0

def game():
	global pill_width, pill_up_height, pill_down_height, pill_down_y, x, y, score, speed
	speed += 0.005
	rex = pygame.draw.rect(screen, (0, 0, 0), (x-50, y-50, 100, 100))
	circle = pygame.draw.circle(screen, (0, 255, 0), (x, y), 50)
	
	pill_up = pygame.draw.rect(screen, (255, 255, 0), (500, 0, pill_width, pill_up_height))
	
	pill_down = pygame.draw.rect(screen, (255, 255, 0), (500, pill_down_y, pill_width, pill_down_height))
	
	col_up = rex.colliderect(pill_up)
	col_down = rex.colliderect(pill_down)
	if col_up == True or col_down == True:
		collided()		
		
	if x > 714:
		x = 50
		score += 1
		pill_up_height = random.randint(400,700)
		pill_down_y = random.randint(900, 1200)
		while (pill_down_y - pill_up_height < 300) or (pill_down_y - pill_up_height > 360):
			pill_up_height = random.randint(400,700)
			pill_down_y = random.randint(900, 1200)
		
def collided():
	global running
	while running:
		screen.fill((0, 0, 0))
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		font = pygame.font.Font('freesansbold.ttf', 50)
		text = font.render(f"""Game Over!
Score: {score}""", True, (255, 255, 255), (0, 0, 0))
		textRect = text.get_rect()
		textRect.center = (350, 700)
		screen.blit(text, textRect)
		pygame.display.flip()	

while running:
	screen.fill((0, 0, 0))
	
	font = pygame.font.Font('freesansbold.ttf', 30)
	text = font.render(('Score: ' + str(score)), True, (255, 255, 255), (0, 0, 0))
	textRect = text.get_rect()
	textRect.center = (70, 50)
	screen.blit(text, textRect)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				jumping = True
	
	x += speed
	if jumping == False:
		y += dec_height
	else:
		if jumpCount >= -8:
			neg = 1
			if jumpCount < 0:
				neg = -1
			y -= (jumpCount**2)/3 * neg
			jumpCount -= 1
		else:
			jumpCount = 10
			jumping = False

	game()
	pygame.display.flip()

pygame.quit()
