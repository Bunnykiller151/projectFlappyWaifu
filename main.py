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
Titel_Programm = pygame.display.set_caption('Flappy Waifu') #Programm Titel.

# Funktion, die den Bildschirm loopt
# Erstellt von Can und Pascal
def Vordergrund_Bewegung():
    Bildschirm.blit(Vordergrund, (Vordergrund_Start, 900))  # Vordergrund linker Teil
    Bildschirm.blit(Vordergrund, (Vordergrund_Start + 576, 900))  # Vordergrund rechter Teil
# ____________________________________________________________________________________________________


# Funktion, die Cups eine Hitbox gibt und generiert
# Erstellt von Can und Pascal
def create_cup():
    random_cup_pos = random.choice(cup_height)
    bottom_cup = cup_surface.get_rect(midtop = (700, random_cup_pos))
    top_cup = cup_surface.get_rect(midbottom = (700, random_cup_pos - 300)) # Groesse des Cups, Spawnort || Platz zwischen Cup: hard 250-350 easy
    return bottom_cup, top_cup
# ____________________________________________________________________________________________________


# Für jeden Cup in Cups werden die Cups um "Geschwindigkeit_Cups" nach links verschoben
# Erstellt von Can und Pascal
def move_cups(cups):
    for cup in cups:
        cup.centerx -= Geschwindigkeit_Cups # Geschwindigkeit der Cups
    return cups
# ____________________________________________________________________________________________________


# Cups werden gezeichnet auf der Canvas Bildschirm, durch die flip_cup funktion wird die Cup um 180° gedreht
# Erstellt von Can und Pascal
def draw_cups(cups):
    for cup in cups:
        if cup.bottom >= 1024:
            Bildschirm.blit(cup_surface, cup)
        # Wenn Cup oben positioniert ist, dann wird diese geflippt 
        else:
            flip_cup = pygame.transform.flip(cup_surface, False, True)
            Bildschirm.blit(flip_cup,cup)
# ____________________________________________________________________________________________________


# Waifu Kollision Check
# Erstellt von Can und Pascal
def check_collision(cups):
    for cup in cups:
        # Wenn Waifu gegen Cup fliegt, wird Game gestoppt
        if Waifu_Hitbox.colliderect(cup):
            Kollision_Sound.play()
            Hintergrund_Musik.stop()
            FastHintergrund_Musik.stop()

            return False
            
# Wenn Waifu gegen Boden/Decke fliegt, wird Game gestoppt
    if Waifu_Hitbox.top <= -100 or Waifu_Hitbox.bottom >= 900:
        Kollision_Sound.play()
        Hintergrund_Musik.stop()
        FastHintergrund_Musik.stop()
        
        return False
    
    return True
# ____________________________________________________________________________________________________


#Bewegung von Waifu beim springen/fallen
# Erstellt von Can und Pascal
def Waifu_Rotation(Waifu):
    new_Waifu = pygame.transform.rotozoom(Waifu, -Waifu_Bewegung *5, 1) # Oberflaeche, Rotation, Skallierung
    return new_Waifu
# ____________________________________________________________________________________________________


#Zeichnen der Spielpunkte und Highscores im Spiel und im Menu
# Erstellt von Can und Pascal
def score_display(Umgebung):
    if Umgebung == 'Spiel':
        Punkte_Tafel =  Spieltext.render('Punkte: ' + str(int(Punkte)),True,(255,255,255)) # Punkte in der Farbe XX in dem Textstil des Spieles
        Punkte_posi = Punkte_Tafel.get_rect(center= (288,100)) # Positionierung der Punkte
        Bildschirm.blit(Punkte_Tafel, Punkte_posi)
    # Wenn der Spieler
    if Umgebung == 'Menu':
        Punkte_Tafel =  Spieltext.render('Punkte: ' + str(int(Punkte)),True,(255,255,255)) # Punkte in der Farbe XX in dem Textstil des Spieles
        Punkte_posi = Punkte_Tafel.get_rect(center= (288,150)) # Positionierung der Punkte
        Bildschirm.blit(Punkte_Tafel, Punkte_posi)
        Highscore_Tafel = Spieltext.render('Highscore: '+  str(int(Highscore_Punkte)),True,(255,255,255))
        Highscore_posi = Highscore_Tafel.get_rect(center= (288,200)) # Positionierung der Punkte
        Bildschirm.blit(Highscore_Tafel, Highscore_posi)
# ____________________________________________________________________________________________________


# Aktualisieren des Highscores wenn Punktzahl höher ist
# Erstellt von Can und Pascal
def score_update(Punkte,Highscore_Punkte):
    if Punkte > Highscore_Punkte:
        Highscore_Punkte = Punkte
        Highscore_Sound.play()
    return Highscore_Punkte
# ____________________________________________________________________________________________________
# Erstellt von Can und Pascal

# Initialisierung pygame
pygame.init()
# Definition Bildschirmgroesse
Bildschirm = pygame.display.set_mode((576, 1024))
# Definieren des Tickers für die Framerate
Framerate = pygame.time.Clock()
#Textfont 
Spieltext = pygame.font.Font("bin/Stay_and_Shine.ttf",50) # Spiele Textstil festlegen als TTF-Format,Groesse
# ____________________________________________________________________________________________________
# Erstellt von Can und Pascal

# Game Variablen
Schwerkraft = 0.2
Waifu_Bewegung = 0
Aktives_Spiel = False
Punkte = 0
Highscore_Punkte = 0
Stage_Check = 0
Startzeit = int(time.time())
Spielzeitchecker = 0
Aktuelle_Spielzeit = 0
Geschwindigkeit_Cups = 5
Spielzeit_BisNextLevel = 0
Zeit_Check = 0
InMenu = 0
Alive = True
Vordergrund_Start = 0
# ____________________________________________________________________________________________________
# Erstellt von Can und Pascal

# Laden und vergroessern der Bilder
Hintergrund = pygame.image.load('bin/assets/background-japan.png')
Hintergrund = pygame.transform.scale(Hintergrund, (576,1024)).convert()
Vordergrund = pygame.image.load('bin/assets/Vordergrund_Base.png')
Vordergrund = pygame.transform.scale(Vordergrund,(576,224)).convert_alpha()
# ____________________________________________________________________________________________________
# Erstellt von Can und Pascal

# Laden und vergroessern des Spielers
Waifu_Bildrunter = pygame.image.load('bin/assets/Waifu_cut_test2.png')
Waifu_Bildrunter = pygame.transform.scale(Waifu_Bildrunter,(68,68)).convert_alpha()
Waifu_Bildhoch = pygame.image.load('bin/assets/Waifu_cut_test2.png')
Waifu_Bildhoch = pygame.transform.scale(Waifu_Bildrunter,(68,68)).convert_alpha()
Waifu_Bildliste = [Waifu_Bildrunter,Waifu_Bildhoch]
Waifu_Index = 0
Waifu_Bild = Waifu_Bildliste[Waifu_Index]
Waifu_Hitbox = Waifu_Bild.get_rect(center=(100, 512))# Rechteck um Waifu Bild
# ____________________________________________________________________________________________________
# Erstellt von Can und Pascal

# Laden und vergroessern der Cups
cup_surface = pygame.image.load('bin/assets/towerofyum.png')
# cup_surface = pygame.transform.scale2x(cup_surface)


cup_list = [] # Cupliste für Zufallsspawn 

SPAWNCUP = pygame.USEREVENT
pygame.time.set_timer(SPAWNCUP, 2000) # Cupspawn, Spawnrate in Millisekunden

NEUERPUNKT = pygame.USEREVENT
pygame.time.set_timer(NEUERPUNKT, 2000) # Zaehlen aufrufen, Aufrufrate in Millisekunden

cup_height = [400,600,800] # Höhe bzw. Positionen auf der Y Achse der Cups

Game_Over_Screen = pygame.image.load('bin/assets/menu.png').convert_alpha() # Menubild anzeigen
Game_Over_Hitbox = Game_Over_Screen.get_rect(center = (288,512)) # Position des Menubildes.
# ____________________________________________________________________________________________________
# Erstellt von Can und Pascal

# Musik und bin/sound einfügen
Hintergrund_Musik  = pygame.mixer.Sound('bin/sound/Start_Waifu.wav')
Hintergrund_Musik.set_volume(0.1) # Lautstärke
FastHintergrund_Musik = pygame.mixer.Sound('bin/sound/LoopWaifu.wav')
FastHintergrund_Musik.set_volume(0.1)
Sprung_Sound = pygame.mixer.Sound('bin/sound/sfx_wing.wav')
Sprung_Sound.set_volume(0.15) # Lautsärke
Kollision_Sound = pygame.mixer.Sound('bin/sound/ouch.wav')
Kollision_Sound.set_volume(0.25) # Lautsärke
Highscore_Sound = pygame.mixer.Sound('bin/sound/highscore_wow.wav')
Highscore_Sound.set_volume(0.15)
# ____________________________________________________________________________________________________
# Erstellt von Can und Pascal

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
# Erstellt von Can und Pascal

        # Events bei Tastendruck
        if event.type == pygame.KEYDOWN:
            # Wenn Space gedrückt wird, springt "Waifu"
            if event.key == pygame.K_SPACE and InMenu == 0 and Aktives_Spiel == True:
                Waifu_Bewegung = 0 # Zuruecksetzen der Gravitation
                Waifu_Bewegung -= 7 # Höhe der Sprünge von "Waifu"
                Sprung_Sound.play() # Start des Sprungsounds
                

                # Spring Animation | Bild ändern bei Sprung
                if Waifu_Index < 1:
                    Waifu_Sprung = pygame.time.get_ticks()
                    
                    Waifu_Index += 1
                    Waifu_Bild = Waifu_Bildliste[Waifu_Index]
                else: 
                    Waifu_Bild = Waifu_Bildliste[Waifu_Index]
                    Waifu_Index = 0
                

            # Spiel Neustart  
            if event.key == pygame.K_SPACE and InMenu == 0 and Aktives_Spiel == False: 
                Hintergrund_Musik.play() # Hintergrund Musik wird gestartet
                Aktives_Spiel = True
                cup_list.clear()
                Waifu_Hitbox.center = (100, 512)
                Waifu_Bewegung = 0
                Waifu_Index = 0 
                Punkte = 0
                Stage_Check = 0
                Aktuelle_Spielzeit = 0
                Spielzeitchecker = 0
                Geschwindigkeit_Cups = 5 # Zuruecksetzen Anfangsgeschwindigkeit
                Startzeit = int(time.time()) # Neue Startzeit bei neuem Versuch definieren 
                Alive = True
                

            # Pause Button
            if event.key == pygame.K_ESCAPE and Alive == True and Aktives_Spiel == True:
                Aktives_Spiel = False
                # Spielfigur einfrieren und Menue oeffnen
                Waifu_Bewegung = 0
                Geschwindigkeit_Cups = 0
                Schwerkraft = 0
                InMenu = 1
            # Resume Button
            elif event.key == pygame.K_ESCAPE and Alive == True and Aktives_Spiel == False:
                    Aktives_Spiel = True
                    # Setzen der derzeitigen Geschwindigkeit
                    if Stage_Check == 0:
                        Geschwindigkeit_Cups = 5
                    elif Stage_Check == 1:
                        Geschwindigkeit_Cups = 6
                    elif Stage_Check == 2:
                        Geschwindigkeit_Cups = 7
                    elif Stage_Check == 3:
                        Geschwindigkeit_Cups = 8
                    Schwerkraft = 0.2 # Schwerkraft aktivieren
                    InMenu = 0 # Menue deaktivieren
# ____________________________________________________________________________________________________
# Erstellt von Can und Pascal

        # Generierung eines neues Cups durch Userevent
        if event.type == SPAWNCUP and InMenu == 0 and Aktives_Spiel == True:
            cup_list.extend(create_cup())

        # Hochzaehlen der Punkte durch Userevent
        if event.type == NEUERPUNKT and InMenu == 0 and Aktives_Spiel == True:
            Punkte += 1
# ____________________________________________________________________________________________________
# Erstellt von Can und Pascal

    # Hintergrund wird an der oberen linken Ecke verankert.
    Bildschirm.blit(Hintergrund, (0, 0))
# ____________________________________________________________________________________________________
# Erstellt von Can und Pascal

    # Allgemeine Spielumgebung wenn Spiel läuft
    if Aktives_Spiel == True:

        # Waifu Interaktionen nach unten und oben
        Waifu_Bewegung += Schwerkraft
        Waifu_Rotiert = Waifu_Rotation(Waifu_Bild)
        Waifu_Hitbox.centery += Waifu_Bewegung
        Bildschirm.blit(Waifu_Rotiert, Waifu_Hitbox)
        Aktives_Spiel = check_collision(cup_list)
        Alive = check_collision(cup_list) # Abfrage ob Kollision erfolgte
        Waifu_Bild = Waifu_Bildliste[Waifu_Index]

        # Cups nach links laufen lassen
        cup_list = move_cups(cup_list)
        draw_cups(cup_list)

        #Darstellen derzeitige Punktzahl
        score_display('Spiel')

        # Errechnung der aktuellen Spielzeit fuer die Schwierigkeitsstufen
        Spielzeitchecker = int(time.time())
        Aktuelle_Spielzeit = Spielzeitchecker - Startzeit
    
    # Anzeige wenn kein Aktives Spiel läuft
    else:
        # Game Over Screen anzeigen
        Bildschirm.blit(Game_Over_Screen, Game_Over_Hitbox)
        # Ausführen Funktion score_update
        Highscore_Punkte = score_update(Punkte, Highscore_Punkte)
        # Darstellen Punktzahl im Menu
        score_display('Menu')
# ____________________________________________________________________________________________________
# Erstellt von Can und Pascal

    # Wenn erste Stage beendet, dann Übergang
    if Aktuelle_Spielzeit >= 59.5 and Stage_Check == 0: # Wenn Spielzeit > X-Sekunden & mit einmaliger Ausführung
        Stage_Check = 1
        Hintergrund_Musik.stop()
        FastHintergrund_Musik.stop()
        FastHintergrund_Musik.play(loops = -1) # Dauerloop für Musik
        Geschwindigkeit_Cups = 6 # Neue Geschwindigkeit der Cups
        
    
    # Wenn zweite Stage beendet, dann Übergang
    if Aktuelle_Spielzeit >= 119 and Stage_Check == 1:
        Stage_Check = 2
        Geschwindigkeit_Cups = 7 # Neue Geschwindigkeit der Cups
        

    # Wenn dritte Stage beendet, dann Übergang
    if Aktuelle_Spielzeit >= 178.5 and Stage_Check == 2:
        Stage_Check = 3
        Geschwindigkeit_Cups = 8 # Neue Geschwindigkeit der Cups
# ____________________________________________________________________________________________________
# Erstellt von Can und Pascal

    # Vordergrund nach links laufen lassen (soll immer laufen!)
    Vordergrund_Start -= 1
    Vordergrund_Bewegung()

    # Vordergrund verschiebt sich, wenn außerhalb des Bildschirms
    if Vordergrund_Start<=-576:
        Vordergrund_Start = 0
# ____________________________________________________________________________________________________
# Erstellt von Can und Pascal

    # Alles darstellen was in der Schleife laeuft
    pygame.display.update()

    # Maximale Framerate des Spiels
    Framerate.tick(120)
