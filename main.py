# Bibliothek pygame importieren
import pygame
# Bibliothek sys importieren
import sys
# Importiere Time Libary 
import time
# Importiere Random Libary 
import random
# ____________________________________________________________________________________________________

# Initialisieren des Soundmixers
pygame.mixer.init(48000, -16, 1, 1024)

# Funktion, die den Bildschirm loopt
def Vordergrund_Bewegung():
    Bildschirm.blit(Vordergrund, (Vordergrund_Start, 900))  # Vordergrund linker Teil
    Bildschirm.blit(Vordergrund, (Vordergrund_Start + 576, 900))  # Vordergrund rechter Teil
# ____________________________________________________________________________________________________


# Funktion, die Hindernisse eine Hitbox gibt und generiert
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pipe_pos - 300)) # Groesse des Hindernisses, Spawnort || Platz zwischen Hindernis: hard 250-350 easy
    return bottom_pipe, top_pipe
# ____________________________________________________________________________________________________


# Hindernisse ggf. bedenken später.  // Für jedes Hinderniss in Hindernisse1 wird die Mitte X um 5 nach links verschoben
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= Geschwindigkeit_Hindernis # Geschwindigkeit der Hindernisse
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
# Waifu Kollision Check
def check_collision(pipes):
    for pipe in pipes:
        # Wenn Waifu gegen Hindernis fliegt, wird Game Inactive gesetzt
        if Waifu_Hitbox.colliderect(pipe):
            Kollision_Sound.play()
            print("coll pipe")
            Hintergrund_Musik.stop()
            FastHintergrund_Musik.stop()

            return False
            
# Wenn Waifu gegen Boden/Decke fliegt, wird Game Inactive gesetzt
    if Waifu_Hitbox.top <= -100 or Waifu_Hitbox.bottom >= 900:
        print("coll bottom or top")
        Kollision_Sound.play()
        Hintergrund_Musik.stop()
        FastHintergrund_Musik.stop()
        

        return False
    
    return True



# ____________________________________________________________________________________________________
#Bewegung von Waifu beim springen/fallen
def Waifu_Rotation(Waifu):
    new_Waifu = pygame.transform.rotozoom(Waifu, -Waifu_Bewegung *5, 1) # Oberflaeche, Rotation, Skallierung
    return new_Waifu



# ____________________________________________________________________________________________________



# ____________________________________________________________________________________________________
#Zeichnen der Spielpunkte und Highscores im Spiel und im Menu
def score_display(Umgebung):
    if Umgebung == 'Spiel':
        Punkte_Tafel =  Spieltext.render('Punkte: ' + str(int(Punkte)),True,(255,255,255)) # Punkte in der Farbe XX in dem Textstil des Spieles
        Punkte_posi = Punkte_Tafel.get_rect(center= (288,100)) # Positionierung der Punkte
        Bildschirm.blit(Punkte_Tafel, Punkte_posi)
    if Umgebung == 'Menu':
        Punkte_Tafel =  Spieltext.render('Punkte: ' + str(int(Punkte)),True,(255,255,255)) # Punkte in der Farbe XX in dem Textstil des Spieles
        Punkte_posi = Punkte_Tafel.get_rect(center= (288,150)) # Positionierung der Punkte
        Bildschirm.blit(Punkte_Tafel, Punkte_posi)

        Highscore_Tafel = Spieltext.render('Highscore: '+  str(int(Highscore_Punkte)),True,(255,255,255))
        Highscore_posi = Highscore_Tafel.get_rect(center= (288,200)) # Positionierung der Punkte
        Bildschirm.blit(Highscore_Tafel, Highscore_posi)
    
# ____________________________________________________________________________________________________

def score_update(Punkte,Highscore_Punkte):
    if Punkte > Highscore_Punkte:
        Highscore_Punkte = Punkte
    return Highscore_Punkte

def Musik_Loop(Spielzeitchecker):
    print("lol")
    MUSIKLOOP = pygame.USEREVENT
    pygame.time.set_timer(MUSIKLOOP, 2000)

    if event.type == MUSIKLOOP and Spielzeitchecker == 0:
        Hintergrund_Musik.play()
        

# ____________________________________________________________________________________________________




# Initialisierung pygame
pygame.init()
# Definition Bildschirmgroesse
Bildschirm = pygame.display.set_mode((576, 1024))
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
check = 0
Startzeit = int(time.time())
Spielzeitchecker = 0
Aktuelle_Spielzeit = 0
Geschwindigkeit_Hindernis = 5
SpielzeitBisNextLevel = 0
Zeitcheck = 0
InMenu = 0
Alive = True

# ____________________________________________________________________________________________________


# Laden und vergroessern der Bilder
Hintergrund = pygame.image.load('assets/background-japan.png')
Hintergrund = pygame.transform.scale(Hintergrund, (576,1024)).convert()
Vordergrund = pygame.image.load('assets/Vordergrund_Base.png')
Vordergrund = pygame.transform.scale(Vordergrund,(576,224)).convert_alpha()
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
pipe_surface = pygame.image.load('assets/towerofyum.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)


pipe_list = [] # Hindernisliste für Zufallsspawn 

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 2000) # Hindernisspawn, Spawnrate in Millisekunden

NEUERPUNKT = pygame.USEREVENT
pygame.time.set_timer(NEUERPUNKT, 2000) # Zaehlen aufrufen, Aufrufrate in Millisekunden

pipe_height = [400,600,800] # Höhe bzw. Positionen auf der Y Achse der Hindernisse

Game_Over_Screen = pygame.image.load('assets/menu.png').convert_alpha() # Menubild anzeigen
Game_Over_Hitbox = Game_Over_Screen.get_rect(center = (288,512)) # Position des Menubildes.
# ____________________________________________________________________________________________________
#Musik und Sound einfügen
Hintergrund_Musik  = pygame.mixer.Sound('assets/Start_Waifu.wav')
Hintergrund_Musik.set_volume(0.1) #Lautstärke
FastHintergrund_Musik = pygame.mixer.Sound('assets/LoopWaifu.wav')
FastHintergrund_Musik.set_volume(0.1)
Sprung_Sound = pygame.mixer.Sound('sound/sfx_wing.wav')
Sprung_Sound.set_volume(0.15) #Lautsärke
Kollision_Sound = pygame.mixer.Sound('sound/sfx_hit.wav')
Kollision_Sound.set_volume(0.15) #Lautsärke

# ____________________________________________________________________________________________________

# Wenn das Programm startet, dann ausfuehren
# Spielanzeige Loop
while True:

    # Darstellung von allen Eingaben des Users oder Timer
    for event in pygame.event.get():

        # Wenn Fenster geschlossen wird, Programm schließen
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# ____________________________________________________________________________________________________

        if event.type == pygame.KEYDOWN:
            # Wenn Space gedrückt wird, springt "Waifu"
            if event.key == pygame.K_SPACE and InMenu == 0 and Aktives_Spiel == True:
                Waifu_Bewegung = 0 # Zuruecksetzen der Gravitation
                Waifu_Bewegung -= 7 # Höhe der Sprünge von "Waifu"
                Sprung_Sound.play() # Start des Sprungsounds
                


                # Spring Animation - nicht auswirkend implementiert.
                if Waifu_Index < 1:
                    Waifu_Sprung = pygame.time.get_ticks()
                    
                    Waifu_Index += 1
                    Waifu_Bild = Waifu_Bildliste[Waifu_Index]
                else: 
                    Waifu_Bild = Waifu_Bildliste[Waifu_Index]
                    Waifu_Index = 0
                
                #Evtl Implementierung: Nach Sprung Userevent machen (wie bei Neuerpunkt & Spawnpipe)
                
                

            # Spiel Neustart  
            if event.key == pygame.K_SPACE and InMenu == 0 and Aktives_Spiel == False: 
                Hintergrund_Musik.play() # Hintergrund Musik wird gestartet
                Aktives_Spiel = True
                pipe_list.clear()
                Waifu_Hitbox.center = (100, 512)
                Waifu_Bewegung = 0
                Waifu_Index = 0 # evtl ändern / rausnehmen wenn keine Animation
                Punkte = 0
                check = 0
                Aktuelle_Spielzeit = 0
                Spielzeitchecker = 0
                Geschwindigkeit_Hindernis = 5 # Zuruecksetzen Anfangsgeschwindigkeit
                Startzeit = int(time.time()) # Neue Startzeit definieren
                Alive = True
                


            # Pause Button
            if event.key == pygame.K_ESCAPE and Alive == True and Aktives_Spiel == True:
                Aktives_Spiel = False
                Waifu_Bewegung = 0
                Geschwindigkeit_Hindernis = 0
                Schwerkraft = 0
                InMenu = 1
            # Resume Button
            elif event.key == pygame.K_ESCAPE and Alive == True and Aktives_Spiel == False:
                    Aktives_Spiel = True
                    if check == 0:
                        Geschwindigkeit_Hindernis = 5
                    elif check == 1:
                        Geschwindigkeit_Hindernis = 6
                    elif check == 2:
                        Geschwindigkeit_Hindernis = 7
                    Schwerkraft = 0.2
                    InMenu = 0

# ____________________________________________________________________________________________________     

        # Generierung eines neues Hindernisses durch Userevent
        if event.type == SPAWNPIPE and InMenu == 0 and Aktives_Spiel == True:
            pipe_list.extend(create_pipe())

        # Hochzaehlen der Punkte durch Userevent
        if event.type == NEUERPUNKT and InMenu == 0 and Aktives_Spiel == True:
            Punkte += 1


        
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
        Alive = check_collision(pipe_list)
        Waifu_Bild = Waifu_Bildliste[Waifu_Index]

        # Hindernisse nach links laufen lassen
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        #Darstellen derzeitige Punktzahl
        score_display('Spiel')

        # Errechnung der aktuellen Spielzeit fuer die Schwierigkeitsstufen
        Spielzeitchecker = int(time.time())
        Aktuelle_Spielzeit = Spielzeitchecker - Startzeit
        
    else:
        #Game Over Screen anzeigen
        Bildschirm.blit(Game_Over_Screen, Game_Over_Hitbox)
        #Ausführen Funktion score_update
        Highscore_Punkte = score_update(Punkte, Highscore_Punkte)
        #Darstellen Punktzahl im Menu
        score_display('Menu')
        
# ____________________________________________________________________________________________________  

    # Wenn erster Teil zuende
    
    if Aktuelle_Spielzeit >= 59.5 and check == 0: # Wenn Spielzeit > X-Sekunden & mit einmaliger Ausführung
        check = 1
        Hintergrund_Musik.stop()
        FastHintergrund_Musik.stop()
        FastHintergrund_Musik.play(loops = -1) # Dauerloop für Musik
        Geschwindigkeit_Hindernis = 6 # Neue Geschwindigkeit der Hindernisse
        
    
    # Wenn zweiter Teil zuende
        
    if Aktuelle_Spielzeit >= 119 and check == 1:
        check = 2
        Geschwindigkeit_Hindernis = 7 # Neue Geschwindigkeit der Hindernisse
        
    # Wenn dritter Teil zuende
    
    if Aktuelle_Spielzeit >= 178.5 and check == 2:
        check = 3
        Geschwindigkeit_Hindernis = 8 # Neue Geschwindigkeit der Hindernisse
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
