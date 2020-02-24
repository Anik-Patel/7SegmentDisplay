import pygame
import random
import math
import time






GREEN = (20, 255, 140)

GREY = (210, 210 ,210)

WHITE = (50, 50, 50)



RED = (255, 0, 0)

PURPLE = (255, 0, 255)

BLUE = (0, 0, 255)






class Segment(pygame.sprite.Sprite):

    # This class represents a car. It derives from the "Sprite" class in Pygame.



    def __init__(self, color, width, height):

        # Call the parent class (Sprite) constructor

        super().__init__()



        # Pass in the color of the car, and its x and y position, width and height.

        # Set the background color and set it to be transparent

        self.image = pygame.Surface([width, height])

        self.image.fill((255, 255, 255))

        self.image.set_colorkey((255, 255, 255))

        self.color = color

        self.width = width

        self.height = height

        self.type = 0



        

        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])


        self.rect = self.image.get_rect()

    def update(self):
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])



    
















SCREENWIDTH = 1000

SCREENHEIGHT = 1000


size = (SCREENWIDTH, SCREENHEIGHT)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("7SegmentDisplay")


Segments = pygame.sprite.Group()

s = Segment(WHITE, 100, 15)
s.rect.x = 450
s.rect.y = 300
s.type = 0
Segments.add(s)
#----------------------------
s = Segment(WHITE, 15, 100)
s.rect.x = 550
s.rect.y = 315
s.type = 1
Segments.add(s)
#----------------------------
s = Segment(WHITE, 15, 100)
s.rect.x = 550
s.rect.y = 430
s.type = 2
Segments.add(s)
#----------------------------
s = Segment(WHITE, 100, 15)
s.rect.x = 450
s.rect.y = 530
s.type = 3
Segments.add(s)
#----------------------------
s = Segment(WHITE, 15, 100)
s.rect.x = 435
s.rect.y = 430
s.type = 4
Segments.add(s)
#----------------------------
s = Segment(WHITE, 15, 100)
s.rect.x = 435
s.rect.y = 315
s.type = s.type = 5
Segments.add(s)
#----------------------------
s = Segment(WHITE, 100, 15)
s.rect.x = 450
s.rect.y = 415
s.type = 6
Segments.add(s)










clock = pygame.time.Clock()


carryOn = True



one = [0, 1, 1, 0, 0, 0, 0]
two = [1, 1, 0, 1, 1, 0, 1]
three = [1, 1, 1, 1, 0, 0, 1]
four = [0, 1, 1, 0, 0, 1, 1]
five = [1, 0, 1, 1, 0, 1, 1]
six = [1, 0, 1, 1, 1, 1, 1]
seven = [1, 1, 1, 0, 0, 0, 0]
eight = [1, 1, 1, 1, 1, 1, 1]
nine = [1, 1, 1, 1, 0, 1, 1]

def display(array):
	for i in Segments:
		i.color = WHITE
		i.update()
	c = 0
	for x in Segments:
		if array[c] == 1:

			x.color = RED
			x.update()


		c += 1


def go_up():
	display(one)
	update_screen()
	time.sleep(0.5)
	display(two)
	update_screen()
	time.sleep(0.5)
	display(three)
	update_screen()
	time.sleep(0.5)
	display(four)
	update_screen()
	time.sleep(0.5)
	display(five)
	update_screen()
	time.sleep(0.5)
	display(six)
	update_screen()
	time.sleep(0.5)
	display(seven)
	update_screen()
	time.sleep(0.5)
	display(eight)
	update_screen()
	time.sleep(0.5)
	display(nine)
	update_screen()
	time.sleep(0.5)

def update_screen():
	screen.fill((255, 255, 255))
	Segments.draw(screen)
	pygame.display.flip()
	clock.tick(60)



while carryOn:
	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			carryOn = False
	go_up()
	

pygame.quit()
