# Bibliothek pygame importieren
import pygame
# Bibliothek sys importieren
import sys
# Importiere Time Libary 
import time
# Importiere Random Libary 
import random
# ____________________________________________________________________________________________________



# Funktion, die den Bildschirm loopt
def Vordergrund_Bewegung():
    Bildschirm.blit(Vordergrund, (Vordergrund_Start, 900))  # Bei neuer Größe auch ÄNDERN------
    Bildschirm.blit(Vordergrund, (Vordergrund_Start + 576, 900))  # Bei neuer Größe auch ÄNDERN------
# ____________________________________________________________________________________________________


# Funktion, die Hindernisse eine Hitbox gibt und generiert
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pipe_pos - 300))
    return bottom_pipe, top_pipe
# ____________________________________________________________________________________________________


# Hindernisse ggf. bedenken später.  // Für jedes Hinderniss in Hindernisse1 wird die Mitte X um 5 nach links verschoben
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 4.5
    return pipes
# ____________________________________________________________________________________________________


# Hindernisse werden gezeichnet auf der Canvas Bildschirm, durch die flip_pipe funktion wird das Hindernis um 180° gedreht
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            Bildschirm.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            Bildschirm.blit(flip_pipe,pipe)



# ____________________________________________________________________________________________________
# Wenn Waifu gegen Hindernis oder Boden/Decke fliegt, wird Game Inactive gesetzt
def check_collision(pipes):
    for pipe in pipes:
        if Waifu_Hitbox.colliderect(pipe):
            print("coll pipe")
            return False
        

    if Waifu_Hitbox.top <= -100 or Waifu_Hitbox.bottom >= 900:
        print("coll bottom or top")
        return False

    return True



# ____________________________________________________________________________________________________
#Bewegung von Waifu beim springen/fallen
def Waifu_Rotation(Waifu):
    new_Waifu = pygame.transform.rotozoom(Waifu, -Waifu_Bewegung *5, 1)
    return new_Waifu



# ____________________________________________________________________________________________________
def Test_Index():
    
    print("Index changed to" + Waifu_Index)

# ____________________________________________________________________________________________________


# Initialisierung pygame
pygame.init()
# Definition Bildschirmgroesse
Bildschirm = pygame.display.set_mode((576, 1024))  # 1200,1000 später -------
# Definieren des Tickers für die Framerate
Framerate = pygame.time.Clock()
# ____________________________________________________________________________________________________


# Game Variablen
Schwerkraft = 0.2
Waifu_Bewegung = 0
Aktives_Spiel = True
# ____________________________________________________________________________________________________


# Laden und vergroessern der Bilder
Hintergrund = pygame.transform.scale2x(pygame.image.load('assets/background-night.png').convert())
Vordergrund = pygame.transform.scale2x(pygame.image.load('assets/base.png').convert())
# Definition von Bewegungsmodifikator
Vordergrund_Start = 0
# ____________________________________________________________________________________________________
# Laden und vergroessern des Spielers
Waifu_Bildrunter = pygame.transform.scale2x(pygame.image.load('assets/bluebird-downflap.png').convert_alpha())
Waifu_Bildhoch = pygame.transform.scale2x(pygame.image.load('assets/redbird-upflap.png').convert_alpha())
Waifu_Bildliste = [Waifu_Bildrunter,Waifu_Bildhoch]
Waifu_Index = 0
Waifu_Bild = Waifu_Bildliste[Waifu_Index]
Waifu_Hitbox = Waifu_Bild.get_rect(center=(100, 512))# Rechteck um Waifu Bild



# ____________________________________________________________________________________________________


# Laden und vergroessern der Hindernisse
pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)

# Hindernissliste für Zufallspawn
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

pipe_height = [400,600,800]
# ____________________________________________________________________________________________________

Hintergrund_Musik  = pygame.mixer.Sound('musik_Waifu.mp3')

# Wenn das Programm startet, dann ausfuehren
# Spielanzeige Loop
while True:

    # Darstellung von allen Eingaben des Users order Timer
    for event in pygame.event.get():

        # Wenn Fenster geschlossen wird, Programm schließen
        if event.type == pygame.QUIT:
            pygame.quit()

            # ------------------------------- EVTL RAUSNEHMEN
            sys.exit()

        # Wenn Space gedrückt wird, springt Waifu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and Aktives_Spiel == True:
                Waifu_Bewegung = 0
                Waifu_Bewegung -= 10 #Höhe der Sprünge von Waifu"
                



                #Spring Animation
                if Waifu_Index < 1:
                    print(0)

                    Waifu_Sprung = pygame.time.get_ticks()
                    
                    Waifu_Index += 1
                    Waifu_Bild = Waifu_Bildliste[Waifu_Index]
                else: 
                    print(1)
                    Waifu_Bild = Waifu_Bildliste[Waifu_Index]
                    Waifu_Index = 0
                

                
                
                
                
                

                
            if event.key == pygame.K_SPACE and Aktives_Spiel == False:
                Aktives_Spiel = True
                pipe_list.clear()
                Waifu_Hitbox.center = (100, 512)
                Waifu_Bewegung = 0
                Waifu_Index = 0
                Hintergrund_Musik.play()

        # Generierung eines neues Hindernisses durch den "Timer"
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())


        
# ____________________________________________________________________________________________________



    # Hintergrund wird an der oberen linken Ecke verankert.
    Bildschirm.blit(Hintergrund, (0, 0))
# ____________________________________________________________________________________________________

    
    if Aktives_Spiel == True:
        # Waifu Interaktionen nach unten und oben
        Waifu_Bewegung += Schwerkraft
        Waifu_Rotiert = Waifu_Rotation(Waifu_Bild)
        Waifu_Hitbox.centery += Waifu_Bewegung
        Bildschirm.blit(Waifu_Rotiert, Waifu_Hitbox)
        Aktives_Spiel = check_collision(pipe_list)
        Waifu_Bild = Waifu_Bildliste[Waifu_Index]

        # Hindernisse nach links laufen lassen
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        

    
# ____________________________________________________________________________________________________
    
    # Vordergrund nach links laufen lassen (soll immer laufen!)
    Vordergrund_Start -= 1
    Vordergrund_Bewegung()

    # Vordergrund verschiebt sich, wenn außerhalb des Bildschirms
    if Vordergrund_Start<=-576:
        Vordergrund_Start = 0
# ____________________________________________________________________________________________________




# ____________________________________________________________________________________________________



    # Alles darstellen was in der Schleife laeuft
    pygame.display.update()

    # Maximale Framerate des Spiels
    Framerate.tick(120)
