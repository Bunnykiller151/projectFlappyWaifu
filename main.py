# Bibliothek pygame importieren
import pygame
# Bibliothek sys importieren
import sys
#Importiere Time Libary 
import time
# ____________________________________________________________________________________________________



# Funktion, die den Bildschirm loopt
def vordergrund_Bewegung():
    Bildschirm.blit(Vordergrund, (Vordergrund_Start, 900))  # Bei neuer Größe auch ÄNDERN------
    Bildschirm.blit(Vordergrund, (Vordergrund_Start + 576, 900))  # Bei neuer Größe auch ÄNDERN------
# ____________________________________________________________________________________________________


# Funktion, die Hindernisse eine Hitbox gibt und generiert
def create_pipe():
    new_pipe = pipe_surface.get_rect(midtop=(288, 512))
    return new_pipe
# ____________________________________________________________________________________________________


# Hindernisse ggf. bedenken später.  // Für jedes Hinderniss in Hindernisse1 wird die Mitte X um 5 nach links verschoben
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes
# ____________________________________________________________________________________________________


# Hindernisse werden gezeichnet auf der Canvas Bildschirm
def draw_pipes(pipes):
    for pipe in pipes:
        Hintergrund.blit(pipe_surface, pipe)
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
# ____________________________________________________________________________________________________


# Laden und vergroessern der Bilder
Hintergrund = pygame.transform.scale2x(pygame.image.load('assets/background-night.png').convert())
Vordergrund = pygame.transform.scale2x(pygame.image.load('assets/base.png').convert())
# Definition von Bewegungsmodifikator
Vordergrund_Start = 0
# ____________________________________________________________________________________________________


# Laden und vergroessern des Spielers
Waifu_Bild = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png').convert())
# Rechteck um Waifu Bild
Waifu_Hitbox = Waifu_Bild.get_rect(center=(100, 512))
# ____________________________________________________________________________________________________


# Laden und vergroessern der Hindernisse
pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)

# Hindernissliste für Zufallspawn
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
# ____________________________________________________________________________________________________


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
            if event.key == pygame.K_SPACE:
                Waifu_Bewegung = 0
                Waifu_Bewegung -= 13

        # Generierung eines neues Hinderniss durch den "Timer"
        if event.type == SPAWNPIPE:
            pipe_list.append(create_pipe())
# ____________________________________________________________________________________________________



    # Hintergrund wird an der oberen linken Ecke verankert.
    Bildschirm.blit(Hintergrund, (0, 0))

    # Waifu Interaktionen nach unten und oben
    Waifu_Bewegung += Schwerkraft
    Waifu_Hitbox.centery += Waifu_Bewegung
    Bildschirm.blit(Waifu_Bild, Waifu_Hitbox)

    # Hindernisse nach links laufen lassen
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    # Vordergrund nach links laufen lassen
    Vordergrund_Start -= 1
    vordergrund_Bewegung()

    # Vordergrund verschiebt sich, wenn außerhalb des Bildschirms
    if Vordergrund_Start<=-576:
        Vordergrund_Start = 0
# ____________________________________________________________________________________________________



    # Alles darstellen was in der Schleife laeuft
    pygame.display.update()

    # Maximale Framerate des Spiels
    Framerate.tick(120)
