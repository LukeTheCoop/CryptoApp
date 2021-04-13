import pygame
import os
import time 
from tracker import *
import string

pygame.font.init()

WIDTH, HEIGHT = 500, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Crypto Tracker')

BACKGROUND = pygame.transform.scale(
	pygame.image.load(os.path.join('Assets', 'Background.png')), (WIDTH,HEIGHT))

XImage = pygame.image.load(
	os.path.join('Assets', 'XMark.png'))

INPUT_BORDER = pygame.Rect(WIDTH//2 - 120, 50, 240, 50)
ENTER_BORDER = pygame.Rect(WIDTH//2 - 60, INPUT_BORDER.y + 100, 120, 40)
CLEAR_BORDER = pygame.Rect(WIDTH//2 - 41, ENTER_BORDER.y + 50, 82, 25)

TRACK_INPUT_BORDER = pygame.Rect(WIDTH//2 - 120, HEIGHT//2 - 25 - 50, 240, 50)
TRACK_ENTER = pygame.Rect(WIDTH//2 - 60, TRACK_INPUT_BORDER.y + 80, 120, 40)

BASE_FONT = pygame.font.SysFont('timesnewroman', 40)
BASE_BOLD = pygame.font.SysFont('bold_timesnewroman', 80)
TITLE_FONT = pygame.font.SysFont('counterstrikeregular', 50)
STATUS_FONT = pygame.font.SysFont('timesnewroman', 20)
SMALL_FONT = pygame.font.SysFont('timesnewroman', 14)

#Tracked Fonts
MAIN_TRACK_FONT = pygame.font.SysFont('timesnewroman', 25)
GOAL_TRACK_FONT = pygame.font.SysFont('timesnewroman', 16)

#X marks
X_ONE, X_TWO, X_THREE = pygame.Rect(395, 310, 25, 25), pygame.Rect(395, 430, 25, 25), pygame.Rect(395, 550, 25, 25) 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED =  (255, 0, 0)
GRAY = (134, 134, 134)
GREEN = (0, 255, 0)

FPS = 60


def header():
	title_text = TITLE_FONT.render('Crypto App', True, BLACK)

	WIN.blit(BACKGROUND, (0, 0))
	WIN.blit(title_text, (WIDTH - title_text.get_width() - 10, HEIGHT - title_text.get_height() - 10))

def get_tracked():
	track_height = 310

	for i in get_tracked_list():
		TRACK_RECT = pygame.Rect(WIDTH//2 - 350//2, track_height, 350, 80)

        
		#Draws

		pygame.draw.rect(WIN, WHITE, TRACK_RECT)
		pygame.draw.rect(WIN, BLACK, TRACK_RECT, 5)

		WIN.blit(XImage, (TRACK_RECT.x, TRACK_RECT.y))

		#Text
		crypto, goal = i.split('-')[0], i.split('-')[1]

		price = get_currency(crypto)

		main_text = MAIN_TRACK_FONT.render(crypto.title() + ': ${:,}'.format(price), True, BLACK)
		goal_text = GOAL_TRACK_FONT.render('Alert: ${:,}'.format(float(goal)), True, BLACK)

		
		WIN.blit(main_text, (TRACK_RECT.x + 8, TRACK_RECT.y + 8))

		x, y = 425 , track_height + 80 
		WIN.blit(goal_text, (x - goal_text.get_width() - 5, y - goal_text.get_height() - 5))

		track_height += 120
	
def checkHover():
	enter_text = BASE_FONT.render('Enter', True, BLACK)
	small_text = SMALL_FONT.render('Clear tracked', True, BLACK)


	if ENTER_BORDER.collidepoint(pygame.mouse.get_pos()):
		pygame.draw.rect(WIN, GRAY, ENTER_BORDER)
		WIN.blit(enter_text, (ENTER_BORDER.x + 15, ENTER_BORDER.y - 3))
	else:
		pygame.draw.rect(WIN, BLACK, ENTER_BORDER, 2)
		WIN.blit(enter_text, (ENTER_BORDER.x + 15, ENTER_BORDER.y - 3))

	if CLEAR_BORDER.collidepoint(pygame.mouse.get_pos()):
		pygame.draw.rect(WIN, GRAY, CLEAR_BORDER)
		WIN.blit(small_text, (CLEAR_BORDER.x + 3, CLEAR_BORDER.y + 5))
	else:
		pygame.draw.rect(WIN, BLACK, CLEAR_BORDER, 2)
		WIN.blit(small_text, (CLEAR_BORDER.x + 3, CLEAR_BORDER.y + 5))



def draw_window(user_text, status):
	search_text = BASE_FONT.render(user_text, True, BLACK)
	status_text = STATUS_FONT.render(status, True, RED)
	track_title_text = BASE_BOLD.render('Tracked:',  True, WHITE)

	header()

	checkHover()

	pygame.draw.rect(WIN, BLACK, INPUT_BORDER, 4)
	WIN.blit(search_text, (INPUT_BORDER.x + 5, INPUT_BORDER.y))

	WIN.blit(status_text, (WIDTH//2 - status_text.get_width()//2, INPUT_BORDER.y + 60))

	#tracked
	WIN.blit(track_title_text, (20, 250))

	get_tracked()

	pygame.display.update()



def draw_crypto(cur, user_text):
	#Call functionprice = tracker.get_currency(cur)
	price = get_currency(cur)

	title_text = BASE_BOLD.render(cur.title(), True, BLACK)
	price_string = 'Crypto Price: ${:,}'.format(price)

	track_text = BASE_FONT.render('Enter alert price', True, BLACK)
	sub_track_text = STATUS_FONT.render('(Leave blank if none)', True, BLACK)

	track_add_text = BASE_FONT.render('Enter', True, BLACK)
	added_text = BASE_FONT.render(user_text, True, BLACK)
	#price_string =  str(price)
	crypto_text = BASE_FONT.render(price_string, True, BLACK)

	#header
	header()

	#INFO
	WIN.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 50))

	WIN.blit(crypto_text, (WIDTH//2 - crypto_text.get_width()//2, title_text.get_height() + 100))

	#Track currency
	WIN.blit(track_text, (WIDTH//2 - track_text.get_width()//2, TRACK_INPUT_BORDER.y - 100))
	WIN.blit(sub_track_text, (WIDTH//2 - sub_track_text.get_width()//2, TRACK_INPUT_BORDER.y - 50))

	pygame.draw.rect(WIN, WHITE, TRACK_INPUT_BORDER)
	pygame.draw.rect(WIN, BLACK, TRACK_INPUT_BORDER, 4)

	WIN.blit(added_text, (TRACK_INPUT_BORDER.x + 5, TRACK_INPUT_BORDER.y))

	pygame.draw.rect(WIN, BLACK, TRACK_ENTER, 2)
	WIN.blit(track_add_text, (TRACK_ENTER.x + 15, TRACK_ENTER.y - 2))


	pygame.display.update()


def crypto_window(text):
	clock = pygame.time.Clock()

	error = 'Currency couldn\'t be found!'
	if check_currency(text):
		run = True
	else:
		main(error)
		run = False

	user_text = ''
	type_active = False

	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				break

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_ESCAPE:
					main('')
					run = False

				if event.key == pygame.K_BACKSPACE:
					user_text = user_text[:-1]
				elif type_active:
					if event.key != pygame.K_RETURN:
						user_text += event.unicode
				
				if event.key == pygame.K_RETURN:
					if len(get_tracked_list()) <= 3:
						type_active = False
						finished_text = user_text.lower()

						if finished_text != '':
							try:
								float(user_text)
								add_track(text, user_text)
								main('Alert added!')
								run = False
								break
							except:
								main('Please make sure to enter a number!')
						else:
							pass
					else:
						main('You have reached the max amount of tracked currency\'s (3/3)')
						run = False
						break


			if event.type == pygame.MOUSEBUTTONDOWN:
				if TRACK_INPUT_BORDER.collidepoint(event.pos) and type_active == False:
					type_active = True
				else:
					type_active = False

				if TRACK_ENTER.collidepoint(event.pos):
					type_active = False
					finished_text = user_text.lower()
					if finished_text != '':
						try:
							float(user_text)
							add_track(text, user_text)
							main('Alert added!')
							run = False
							break
						except:
							main('Please make sure to enter a number!')
					else:
						pass
		draw_crypto(text, user_text)

def main(status):
	clock = pygame.time.Clock()

	run = True
	user_text = ''

	enter_hover = False
	reset_hover = False

	error = 'Currency couldn\'t be found!'
	type_active = False
	while run:

		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				break

			if event.type == pygame.MOUSEBUTTONDOWN:
				if INPUT_BORDER.collidepoint(event.pos) and type_active == False:
					type_active = True
				else:
					type_active = False

				if ENTER_BORDER.collidepoint(event.pos):
					type_active = False
					finished_text = user_text.lower()
					if finished_text != '':
						crypto_window(finished_text)
					else:
						main(error)

					run = False

				if CLEAR_BORDER.collidepoint(event.pos):
					clear_tracked_list()
					run = False
					main('Cleared')
					break

				if X_ONE.collidepoint(event.pos):
					if len(get_tracked_list()) >= 1:
						remove_track(0)
				elif X_TWO.collidepoint(event.pos):
					if len(get_tracked_list()) >= 2:
						remove_track(1)
				elif X_THREE.collidepoint(event.pos):
					if len(get_tracked_list()) >= 3:
						remove_track(2)





			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_BACKSPACE:
					user_text = user_text[:-1]
				elif type_active:
					if event.key != pygame.K_RETURN:
						user_text += event.unicode
				
				if event.key == pygame.K_RETURN:
					type_active = False
					finished_text = user_text.lower()
					if finished_text != '':
						crypto_window(finished_text)
					else:
						main(error)
					run = False
		if len(user_text) >= 10:
			type_active = False
		else:
			type_active = True


		draw_window(user_text, status)


if __name__ == '__main__':
	check_data()
	main('')
