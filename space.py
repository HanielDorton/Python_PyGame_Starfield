import sys, time, random, pygame
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0,0,0)
WINWIDTH = 800
WINHEIGHT = 600
FPS = 30

class CurrentGame():
	def __init__(self, numStars, r, g, b,flicker):
		self.numStars = numStars
		self.r = r
		self.g = g
		self.b = b
		self.flicker = flicker
		
	def currentMain(self):
		stars = generateRandomStars(self.numStars, self.r, self.g, self.b)
		
		while True:
			SCREEN.fill(BLACK)
			flickerStars(stars, self.flicker)
			for event in pygame.event.get():
				if event.type == QUIT:
					terminate()

				elif event.type == KEYUP:
					if event.key == K_ESCAPE:
						terminate()
				
					if event.key == K_UP:
						return planetWhite
					if event.key == K_RIGHT:
						return planetAqua
					if event.key == K_LEFT:
						return planetPink
					if event.key == K_DOWN:
						return planetWhitetoBlue
				


			pygame.display.update()
			FPSCLOCK.tick(FPS)

			
planetYellow = CurrentGame(400, 220, 220, 20, [2,3])
planetBlue = CurrentGame(1250, 20, 20, 'r', [4])
planetRed = CurrentGame(500, 'r', 28, 0, [2])
planetGreen = CurrentGame(500,  0, 'r', 0, [3])
planetWhite = CurrentGame(400, 220, 220, 220, [2,3,4])
planetAqua = CurrentGame(400, 20, 220, 220, [3,4])
planetPink = CurrentGame(400, 220, 20, 220, [2,4])
planetWhitetoBlue = CurrentGame(400, 220, 220, 220, [2,3])




def main():
    global SCREEN, FPSCLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode([WINWIDTH, WINHEIGHT])
    pygame.display.set_caption('Space')
    FPSCLOCK = pygame.time.Clock()
	
    start = planetRed 
	
    while True:
    
        start = start.currentMain()


def terminate():
    pygame.quit()
    sys.exit()

def generateRandomStars(numOfStars, r, g, b):
    """
    generate a given amount of stars which is returned as a list of lists
    each star has:
    [0]:width
    [1]:height
    [2]:rcolor - put number for fixed else 'r'
    [3]:gcolor
    [4]:bcolor
    [5]:rateofchangeofcolor
    """
    stars = []
    for i in range(numOfStars):       
        newstar = []
        newstar.append(random.randint(0, WINWIDTH))
        newstar.append(random.randint(0, WINHEIGHT))
        if type(r) == int:
            newstar.append(r)
        else:
            newstar.append(random.randint(100, 234))
        if type(g) == int:
            newstar.append(g)
        else:
            newstar.append(random.randint(100, 234))
        if type(b) == int:
            newstar.append(b)
        else:
            newstar.append(random.randint(100, 234))
        newstar.append(random.randint(0,4))
        stars.append(newstar)
    return(stars)
		
def flickerStars(stars, flicker):
    count = 20
    """
    Paramaters are:
    flicker is 2 for red, 3 for green, 4 for blue
    """    
    for star in stars:
        change = False
        if count > 15:
            SCREEN.set_at((star[0], star[1]), (star[2], star[3], star[4]))
            SCREEN.set_at((star[0]+1, star[1]), (star[2], star[3], star[4]))
            SCREEN.set_at((star[0]-1, star[1]), (star[2], star[3], star[4]))
            SCREEN.set_at((star[0], star[1]+1), (star[2], star[3], star[4]))
            SCREEN.set_at((star[0], star[1]-1), (star[2], star[3], star[4]))
            count = 0
        else:
            SCREEN.set_at((star[0], star[1]), (star[2], star[3], star[4]))
        for i in flicker:
                star[i] += (star[5])*2
                if star[i] < 11 or star[i] > 244: change = True
        if change == True:
                star[5] = -(star[5])        
        count += 1




main()
