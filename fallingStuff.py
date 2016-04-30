#Nancy McNamara, ncmnama1

import math
import pygame
import os
import sys
from pygame.locals import *
import random

pirates = dict([("player_image","pirate.png"),("background_image","piratebeach.jpg"),("box_image", "treasurechest.png"), ("ball_image", "piratecoin.png"), ('gun_image', "canon2.jpg"), ('player_x',300),('player_y',400)])

class Mode:
	def __init__(self, dict):
		self.player_image = dict['player_image']
		self.background_image = dict['background_image']
		self.box_image = dict['box_image']
		self.ball_image = dict['ball_image']
		self.gun_image = dict['gun_image']
		self.player_start = [dict['player_x'],dict['player_y']]
mode = Mode(pirates)

class GameSpace:
	def main(self):
		#1. basic initialization
		pygame.init()

		self.size = self.width, self.height = 640, 480
		self.background = 50, 50, 50
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption("ppprrrrooooojjjjeeeeccccttttt")
		#2. set up game objects
		self.clock = pygame.time.Clock()
		self.rain = Rain(self)
		self.player1 = Player1(self)
		bg = pygame.image.load("media/"+mode.background_image)
		bg = pygame.transform.scale(bg, (854,480))
		#random variables in GameSpace
		self.score1 = 0
		self.keyspressed = 0

		#3. start game loop
		while 1:
			mx, my = pygame.mouse.get_pos()


			for guy in self.rain.drops:
				if pygame.sprite.collide_rect(guy, self.player1.box):
					self.rain.drops.remove(guy)
					self.score1+=1
			#4. clock tick regulation (framerate)
			self.clock.tick(60)
			
			#5. handle user inputs
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == KEYDOWN:
					if event.key == 275:
						self.player1.Moving = "R" 
					elif event.key == 276:
						self.player1.Moving = "L"
					self.keyspressed +=1
				if event.type == KEYUP:
					self.keyspressed -=1
					if self.keyspressed ==0:
						self.player1.Moving = "N"
			#6. send a tick to every game object
			self.rain.tick()
			self.player1.tick()
			#7. finally, display game object
			self.screen.fill(self.background)
			self.screen.blit(bg, (0,0))
			self.screen.blit(self.player1.image, self.player1.rect)
			lt = pygame.font.Font('freesansbold.ttf',115)
			textSurf = lt.render(str(self.score1), True, (100, 100, 100))
			TextRect = textSurf.get_rect()
			self.screen.blit(textSurf, TextRect)
			self.screen.blit(self.player1.box.image, self.player1.box.rect)	
			for guy in self.rain.drops:
				self.screen.blit(guy.image, guy.rect)
			pygame.display.flip()


class Rain(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		self.drops = []
	def tick(self):
		create = random.randint(1,10)
		if create==8:
			self.drops.append(Raindrops())
		for guy in self.drops:
			guy.rect = guy.rect.move([0,1])

class Raindrops(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs
		self.image = pygame.image.load("media/"+mode.ball_image)
		self.rect = self.image.get_rect()
		self.x = random.randint(30,610)
		self.rect.center = [self.x,-25]

class Player1(pygame.sprite.Sprite):
	def __init__(self, gs = None):
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs
		self.image = pygame.image.load("media/"+mode.player_image)
		self.rect = self.image.get_rect()
		self.rect.center = mode.player_start
		self.Moving = "N"
		self.box = Box(self.rect.center)
	def tick(self):
		if self.Moving == "R":
			self.rect = self.rect.move([5,0])
			self.box.rect = self.box.rect.move([5,0])
		elif self.Moving == "L":
			self.rect = self.rect.move([-5,0])
			self.box.rect = self.box.rect.move([-5,0])
		if self.rect.center[0]<20:
			self.rect.center = [20, self.rect.center[1]]
			#self.box.rect = self.box.rect.move([5,0])
		elif self.rect.center[0]>620:
			self.rect.center = [620, self.rect.center[1]]
			#self.box.rect = self.box.rect.move([5,0])		
class Box(pygame.sprite.Sprite):
	def __init__(self, center):
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs
		self.image = pygame.image.load("media/"+mode.box_image)
		self.rect = self.image.get_rect()
		self.x = center[0]-15
		self.y = center[1]+38
		self.rect.center = [self.x,self.y]

def dist(x1, y1, x2, y2):
	return ((y2-y1)**2+(x2-x1)**2)**.5

if __name__ == '__main__':
	gs = GameSpace()
	gs.main()
