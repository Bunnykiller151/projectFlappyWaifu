#Bibliothek pygame importieren
from os import pipe
import pygame
#Bibliothek sys importieren
import sys
# importiere Time für Zeitticker oder Events
import time

#Funktion, die den Bildschirm loopt
def Vordergrund_Bewegung():
    Bildschirm.blit(Vordergrund,(Vordergrund_Start, 900)) #Bei neuer Größe auch ÄNDERN------
    Bildschirm.blit(Vordergrund,(Vordergrund_Start + 576, 900)) #Bei neuer Größe auch ÄNDERN------

#Funktion, die Hindernisse eine Hitbox gibt und generiert   
def create_pipe():
    new_pipe = pipe_surface.get_rect(midtop = (288,512))
    return new_pipe

#Hindernisse ggf. bedenken später.  // Für jedes Hinderniss in Hindernisse1 wird die Mitte X um 5 nach links verschoben
def move_pipe(pipes):
    for pipe in pipes:
        pipe. -= 5
    return pipes

#Hindernisse werden gezeichnet auf der Canvas Bildschirm
def draw_pipe(pipes):
    for pipe in pipes:
        Hintergrund.blit(pipe_surface, pipe)

    

#Initialisierung pygame
pygame.init()
#Definition Bildschirmgroesse
Bildschirm = pygame.display.set_mode((576,1024)) #1200,1000 später -------
#Definieren des Tickers für die Framerate
Framerate = pygame.time.Clock()

# Game Variablen
Schwerkraft = 0.2
Waifu_Bewegung = 0

#Laden und vergroessern der Bilder
Hintergrund = pygame.transform.scale2x(pygame.image.load('assets/background-night.png').convert())
Vordergrund = pygame.transform.scale2x(pygame.image.load('assets/base.png').convert())

#Definition von Bewegungsmodifikator
Vordergrund_Start = 0

#Laden und vergroessern des Spielers
Waifu_Bild = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png').convert())

#Rechteck um Waifu Bild
Waifu_Hitbox = Waifu_Bild.get_rect(center = (100,512))

#Laden und vergroessern der Hindernisse
pipe_surface = pygame.transform.scale2x(pygame.image.load('assets/pipe-red.png').convert())

#Hindernissliste für Zufall
pipe_list =[]
PIPESPAWN = pygame.USEREVENT
pygame.time.set_timer(PIPESPAWN,1200)


#Wenn das Programm startet, dann ausfuehren
#Spielanzeige Loop
while True:
    
    #Darstellung von allen Eingaben des Users order Timer
    for event in pygame.event.get():
        
        #Wenn Fenster geschlossen wird, Programm schließen
        if event.type == pygame.QUIT:
            pygame.quit()
            
            # ------------------------------- EVTL RAUSNEHMEN ------------------------------------------------------------------
            sys.exit()
            
        #Wenn Space gedrückt wird, springt Waifu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Waifu_Bewegung = 0
                Waifu_Bewegung -= 13
                
        #Generierung eines neues Hinderniss durch den "Timer"
        if event.type == PIPESPAWN:
            pipe_list.append(create_pipe)
                
            
    #Hintergrund wird an der oberen linken Ecke verankert. 
    Bildschirm.blit(Hintergrund,(0,0))

    #Waifu Interaktionen nach unten und oben
    Waifu_Bewegung += Schwerkraft
    Waifu_Hitbox.centery += Waifu_Bewegung
    Bildschirm.blit(Waifu_Bild,Waifu_Hitbox)
    
    #Hindernisse nach links laufen lassen
    pipe_list = move_pipe(pipe_list)
    draw_pipe(pipe_list)

    
    #Vordergrund nach links laufen lassen
    Vordergrund_Start -= 1
    Vordergrund_Bewegung()
    
    #Vordergrund verschiebt sich, wenn außerhalb des Bildschirms
    if Vordergrund_Start <= -576:
        Vordergrund_Start = 0


    #Alles darstellen was in der Schleife laeuft
    pygame.display.update()
    
    #Maximale Framerate des Spiels
    Framerate.tick(144)