import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400

score = 0
game_over = False

 # a file named this has to be placed in a folder named "images"
fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

# called automatically
def draw():
	screen.fill("green")
	fox.draw()
	coin.draw()
	screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

	if game_over:
		screen.fill("pink")
		screen.draw.text("Final score: " + str(score), topleft=(10, 10), fontsize=60)

def update():
	global score

	if keyboard.left:
		fox.x = fox.x - 2
	elif keyboard.right:
		fox.x = fox.x + 2
	elif keyboard.up:
		fox.y = fox.y - 2
	elif keyboard.down:
		fox.y = fox.y + 2

	coin_collected = fox.colliderect(coin)

	if coin_collected:
		score = score + 10
		place_coin()

def place_coin():
	coin.x = randint(20, (WIDTH - 20))
	coin.y = randint(20, (HEIGHT - 20))

def time_up():
	global game_over
	game_over = True

clock.schedule(time_up, 20.0)
place_coin()



# # called automatically
# def on_mouse_down(pos):
# 	if apple.collidepoint(pos):
# 		print("Good shot")
# 		place_apple()
# 	else:
# 		print("You missed")
# 		quit()


# place_apple()

pgzrun.go()
