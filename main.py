#Bibliothek pygame importieren
import pygame
#Bibliothek sys importieren
import sys

#Initialisierung pygame
pygame.init()
#Definition Bildschirmgroesse
Bildschirm = pygame.display.set_mode((576,1024)) #1200,1000 später
#Definieren 
Framrate = pygame.time.Clock()

#Wenn das Programm startet, dann ausfuehren
while True:
    #Darstellung von allen Eingaben des Users order Timer
    for event in pygame.event.get():
        
        #Wenn Fenster geschlossen wird, Programm schließen
        if event.type == pygame.QUIT:
            pygame.quit()
            # ------------------------------- EVTL RAUSNEHMEN ------------------------------------------------------------------
            sys.exit()

    #image of player 1 fehlt
    #background image fehlt

    #Alles darstellen was in der Schleife laeuft
    pygame.display.update()
    Framerate.tick(144)