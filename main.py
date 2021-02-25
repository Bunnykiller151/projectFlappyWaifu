# Bibliothek pygame importieren
import pygame
# Bibliothek sys importieren
import sys
# Importiere Time Libary 
import time
# Importiere Random Libary 
import random
# ____________________________________________________________________________________________________

#Initialisieren des Soundmixers
pygame.mixer.init(48000, -16, 1, 1024)

# Funktion, die den Bildschirm loopt
def Vordergrund_Bewegung():
    Bildschirm.blit(Vordergrund, (Vordergrund_Start, 900))  # Bei neuer Größe auch ÄNDERN------
    Bildschirm.blit(Vordergrund, (Vordergrund_Start + 576, 900))  # Bei neuer Größe auch ÄNDERN------
# ____________________________________________________________________________________________________


# Funktion, die Hindernisse eine Hitbox gibt und generiert
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pipe_pos - 300)) # Groesse des Hindernisses, Spawnort || Platz zwischen Hindernis: hard 300-350 easy
    return bottom_pipe, top_pipe
# ____________________________________________________________________________________________________


# Hindernisse ggf. bedenken später.  // Für jedes Hinderniss in Hindernisse1 wird die Mitte X um 5 nach links verschoben
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5 # Geschwindigkeit der Hindernisse
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
# Wenn Waifu gegen Hindernis  fliegt, wird Game Inactive gesetzt
def check_collision(pipes):
    for pipe in pipes:
        if Waifu_Hitbox.colliderect(pipe):
            print("coll pipe")
            Hintergrund_Musik.stop()
            return False
        
# Wenn Waifu gegen Boden/Decke fliegt, wird Game Inactive gesetzt
    if Waifu_Hitbox.top <= -100 or Waifu_Hitbox.bottom >= 900:
        print("coll bottom or top")
        Hintergrund_Musik.stop()
        return False
        
    return True



# ____________________________________________________________________________________________________
#Bewegung von Waifu beim springen/fallen
def Waifu_Rotation(Waifu):
    new_Waifu = pygame.transform.rotozoom(Waifu, -Waifu_Bewegung *5, 1) # Oberflaeche, Rotation, Skallierung
    return new_Waifu



# ____________________________________________________________________________________________________
def Test_Index():
    
    print("Index changed to" + Waifu_Index)

# ____________________________________________________________________________________________________
#Zeichnen der Spielpunkte und Highscores im Spiel und im Menu
def score_display(Umgebung):
    if Umgebung == 'Spiel':
        Punkte_Tafel =  Spieltext.render('Punkte: ' + str(int(Punkte)),True,(0,0,0)) # Punkte in der Farbe XX in dem Textstil des Spieles
        Punkte_posi = Punkte_Tafel.get_rect(center= (288,100)) # Positionierung der Punkte
        Bildschirm.blit(Punkte_Tafel, Punkte_posi)
    if Umgebung == 'Menu':
        Punkte_Tafel =  Spieltext.render('Punkte: ' + str(int(Punkte)),True,(0,0,0)) # Punkte in der Farbe XX in dem Textstil des Spieles
        Punkte_posi = Punkte_Tafel.get_rect(center= (288,100)) # Positionierung der Punkte
        Bildschirm.blit(Punkte_Tafel, Punkte_posi)

        Highscore_Tafel = Spieltext.render('Highscore: '+  str(int(Highscore_Punkte)),True,(0,0,0))
        Highscore_posi = Highscore_Tafel.get_rect(center= (288,150)) # Positionierung der Punkte
        Bildschirm.blit(Highscore_Tafel, Highscore_posi)
    
# ____________________________________________________________________________________________________

def score_update(Punkte,Highscore_Punkte):
    if Punkte > Highscore_Punkte:
        Highscore_Punkte = Punkte
    return Highscore_Punkte





# Initialisierung pygame
pygame.init()
# Definition Bildschirmgroesse
Bildschirm = pygame.display.set_mode((576, 1024))  ### 1200,1000 später ###
# Definieren des Tickers für die Framerate
Framerate = pygame.time.Clock()
#Textfont 
Spieltext = pygame.font.Font("Stay_and_Shine.ttf",50) # Spiele Textstil festlegen als TTF-Format,Groesse
# ____________________________________________________________________________________________________


# Game Variablen
Schwerkraft = 0.2
Waifu_Bewegung = 0
Aktives_Spiel = False
Punkte = 0
Highscore_Punkte = 0
# ____________________________________________________________________________________________________


# Laden und vergroessern der Bilder
Hintergrund = pygame.transform.scale2x(pygame.image.load('assets/background-night.png').convert())
Vordergrund = pygame.transform.scale2x(pygame.image.load('assets/base.png').convert())
# Definition von Bewegungsmodifikator
Vordergrund_Start = 0
# ____________________________________________________________________________________________________
# Laden und vergroessern des Spielers
Waifu_Bildrunter = pygame.image.load('assets/Waifu_cut_test2.png')
Waifu_Bildrunter = pygame.transform.scale(Waifu_Bildrunter,(68,68)).convert_alpha()
Waifu_Bildhoch = pygame.image.load('assets/Waifu_cut_test2.png')
Waifu_Bildhoch = pygame.transform.scale(Waifu_Bildrunter,(68,68)).convert_alpha()
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
pygame.time.set_timer(SPAWNPIPE, 2000) # Hindernis, Spawnrate in Millisekunde

pipe_height = [400,600,800] # Höhe bzw. Positionen auf der Y Achse der Hindernisse

Game_Over_Screen = pygame.transform.scale2x(pygame.image.load('assets/message.png')).convert_alpha() # Menubild anzeigen
Game_Over_Hitbox = Game_Over_Screen.get_rect(center = (288,512)) # Position des Menubildes.
# ____________________________________________________________________________________________________
#Musik und Sound einfügen
Hintergrund_Musik  = pygame.mixer.Sound('assets/Start_Waifu.wav')
Hintergrund_Musik.set_volume(0.1) #Lautstärke
Sprung_Sound = pygame.mixer.Sound('sound/sfx_wing.wav')
Sprung_Sound.set_volume(0.15) #Lautsärke
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
            if event.key == pygame.K_SPACE and Aktives_Spiel == True:
                Waifu_Bewegung = 0
                Waifu_Bewegung -= 6 #Höhe der Sprünge von Waifu"
                Sprung_Sound.play()
                



                #Spring Animation
                if Waifu_Index < 1:
                    Waifu_Sprung = pygame.time.get_ticks()
                    
                    Waifu_Index += 1
                    Waifu_Bild = Waifu_Bildliste[Waifu_Index]
                else: 
                    Waifu_Bild = Waifu_Bildliste[Waifu_Index]
                    Waifu_Index = 0
                
                

                
            if event.key == pygame.K_SPACE and Aktives_Spiel == False: # Spiel Neustart
                Hintergrund_Musik.play()
                Aktives_Spiel = True
                pipe_list.clear()
                Waifu_Hitbox.center = (100, 512)
                Waifu_Bewegung = 0
                Waifu_Index = 0 # evtl ändern / rausnehmen wenn keine Animation
                Punkte = 0
                

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

        #Punkte hochzählen
        Punkte += 0.0045
        #Darstellen derzeitige Punktzahl
        score_display('Spiel')
    else:
        #Game Over Screen anzeigen
        Bildschirm.blit(Game_Over_Screen, Game_Over_Hitbox)
        #Ausführen Funktion score_update
        Highscore_Punkte = score_update(Punkte, Highscore_Punkte)
        #Darstellen Punktzahl im Menu
        score_display('Menu')
    

    
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
