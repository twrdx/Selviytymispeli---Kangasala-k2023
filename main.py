import pygame

pygame.init()
pelialue = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Selviytymispeli')

#vaihdetaan taustan väri
pelialue.fill("#ccccff")

#hiiri
mouse = pygame.mouse.get_pos()

#luodaan pelaajahahmo
pelaaja = pygame.Rect(mouse[0], mouse[1], 30, 30)
pelaaja_kuva = pygame.image.load("donut1.png")
pelaaja_kuva.convert()
pelaaja_kuva = pygame.transform.scale(pelaaja_kuva, (30, 30))

#luodaan vihollinen
vihollinen = pygame.Rect(0,0,40,20)
vihollinen_nopeus = [3,1]

rajahdys_kuva = pygame.image.load("explosion.png")
rajahdys_kuva = pygame.transform.scale(rajahdys_kuva, (70, 70))

FPS = 30
FramePerSec = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		mouse = pygame.mouse.get_pos()
		print(mouse)
	pelaaja = pygame.Rect(mouse[0] - 12.5, mouse[1] - 12.5, 25, 25)
	

FramePerSec.tick(FPS)

#pidetään tämä rivi aina viimeisenä:
pygame.display.update()