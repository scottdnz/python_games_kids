import pgzrun
from random import randint

 # a file named this has to be placed in a folder named "images"
apple = Actor("apple")

# called automatically
def draw():
	screen.clear()
	apple.draw()

# called automatically
def on_mouse_down(pos):
	if apple.collidepoint(pos):
		print("Good shot")
		place_apple()
	else:
		print("You missed")
		quit()

def place_apple():
	# apple.x = 300
	# apple.y = 200
	apple.x = randint(10, 800)
	apple.y = randint(10, 600)

place_apple()

pgzrun.go()
