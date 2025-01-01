import time

import pygame
import random
import numpy as np
import os

#CIAO

# Inizializza pygame
pygame.init()

# Costanti
WIDTH, HEIGHT = 800, 600
FPS = 60
OMINO_SPEED = 5
SPIT_RADIUS = 15

# Colori
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

# Configura la finestra
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Leo si Arrampicata sulle Cascate di Ghiaccio")
clock = pygame.time.Clock()


# Classe per l'omino
class Omino:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 50
        self.body_width = 30
        self.body_height = 50
        self.head_radius = 15
        self.color = BLUE
        self.sxdx = 30
        self.color_head = BLACK
        self.rect = pygame.Rect(self.x - self.body_width // 2, self.y - self.body_height // 2, self.body_width,
                                self.body_height)


    def draw(self):
        # Disegna il corpo rettangolare
        pygame.draw.rect(display, self.color, self.rect)

        # Disegna la testa
        head_center = (self.rect.centerx, self.rect.top - self.head_radius)
        pygame.draw.circle(display, self.color_head, head_center, self.head_radius)

        # Disegna le braccia
        pygame.draw.line(display, self.color, (self.rect.left, self.rect.y),
                         (self.rect.left - 30, self.rect.centery - 20- self.sxdx), 3)
        pygame.draw.line(display, self.color, (self.rect.right, self.rect.y),
                         (self.rect.right + 30, self.rect.centery - 20 + self.sxdx), 3)

        # Disegna le gambe
        pygame.draw.line(display, self.color, (self.rect.left, self.rect.bottom),
                         (self.rect.left - 10, self.rect.bottom + 30 + self.sxdx), 2)
        pygame.draw.line(display, self.color, (self.rect.right, self.rect.bottom),
                         (self.rect.right + 10, self.rect.bottom + 30 - self.sxdx), 2)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= OMINO_SPEED
            self.sxdx = 0
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += OMINO_SPEED
            self.sxdx = 0
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= OMINO_SPEED
            if self.sxdx == 30:
                self.sxdx = -30
            else:
                self.sxdx = 30

        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += OMINO_SPEED
            if self.sxdx == 30:
                self.sxdx = -30
            else:
                self.sxdx = 30

    def barriera(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x += OMINO_SPEED
            self.sxdx = 0
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x -= OMINO_SPEED
            self.sxdx = 0
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y += OMINO_SPEED
            if self.sxdx == 30:
                self.sxdx = -30
            else:
                self.sxdx = 30

        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y -= OMINO_SPEED
            if self.sxdx == 30:
                self.sxdx = -30
            else:
                self.sxdx = 30
# Classe per gli spit
class Spit:
    def __init__(self):
        self.x = random.randint(0, WIDTH - SPIT_RADIUS * 2)
        self.y = random.randint(HEIGHT*0.1, HEIGHT // 1.2)
        self.color = GRAY
        self.radius = SPIT_RADIUS
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)

    def draw(self):
        pygame.draw.circle(display, self.color, (self.x + self.radius, self.y + self.radius), 10)

# Classe per arrivo
class Arrivo:
    def __init__(self):
        self.x = random.randint(0, WIDTH - SPIT_RADIUS * 2)
        self.y = + SPIT_RADIUS 
        self.color = RED
        self.radius = SPIT_RADIUS
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)

    def draw(self):
        pygame.draw.circle(display, self.color, (self.x + self.radius, self.y + self.radius), 10)

class Barriera:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 100)
        y_options = [HEIGHT * 0.2, HEIGHT * 0.8, HEIGHT * 0.4, HEIGHT * 0.6]
        self.y = random.choice(y_options)
        #self.y = random.randint(HEIGHT*0.2, HEIGHT *0.8)
        self.width = random.randint(50, 100)
        self.height = random.randint(10, 40)
        self.color = BLACK
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self):
        pygame.draw.rect(display, self.color, self.rect)

 
        

# Classe per le valanghe e le stalattiti
class Ostacolo:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 20)
        self.y = random.randint(-200, -50)
        self.width = 20
        self.height = 50
        self.color = GRAY
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        #pygame.draw.rect(display, self.color, self.rect)
        pygame.draw.polygon(display, self.color, [(self.rect.x, self.rect.y), (self.rect.x + self.width, self.rect.y), (self.rect.x + self.width // 2, self.rect.y + self.height)])
    def move(self):
        self.rect.y += valanga_speed
        if self.rect.top > HEIGHT:
            self.rect.y = random.randint(-200, -50)
            self.rect.x = random.randint(0, distanza_ostacoli * WIDTH - self.width)
    # def move(self):
        # self.recty += valanga_speed
        # self.y = self.recty
        # if (self.y-self.height//2) > HEIGHT:
        #     self.recty = random.randint(-200, -50)
        #     self.y = self.recty
        #     self.rectx = random.randint(0, distanza_ostacoli * WIDTH - self.width)
        #     self.x = self.rectx


# Inizializza oggetti
omino = Omino()
spits = [Spit() for _ in range(5)]
arrivo = Arrivo()
ostacoli = [Ostacolo() for _ in range(3)]
barriere = []

while len(barriere) == 0:
    barriera_temp = Barriera()
    if not any(barriera_temp.rect.colliderect(spit.rect) for spit in spits):
        barriere.append(barriera_temp)

# Variabili di gioco
score = 0
livello = 1
running = True
distanza_ostacoli = 5
valanga_speed = 4
ultimo_spit = None
spits_raggiunti =[]
spits_raggiunti.append((omino.x, omino.y))
ultima_x = omino.x
ultima_y = omino.y

def animate_fall(omino):
    for _ in range(10):
        velocita = (HEIGHT - omino.rect.y) // 10 - 5
        omino.rect.y += velocita
        display.fill(WHITE)
        omino.draw()
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, RED)
        display.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 - 50))
        pygame.display.flip()
        clock.tick(15)
    for rotola in range(10):
        display.fill(WHITE)
        # Disegna il corpo diviso in pezzi
        pygame.draw.rect(display, omino.color, (omino.rect.x- 15, omino.rect.y, omino.body_width, omino.body_height // 2))
        pygame.draw.rect(display, omino.color, (omino.rect.x + 15, omino.rect.y + omino.body_height // 2 + 10, omino.body_width, omino.body_height // 2))
        pygame.draw.circle(display, omino.color_head, (omino.rect.centerx + rotola * 15, omino.rect.top - omino.head_radius), omino.head_radius)
        pygame.draw.line(display, omino.color, (omino.rect.left, omino.rect.y), (omino.rect.left - 35, omino.rect.centery - 20 - omino.sxdx), 3)
        pygame.draw.line(display, omino.color, (omino.rect.right, omino.rect.y), (omino.rect.right + 33, omino.rect.centery - 20 + omino.sxdx), 3)
        pygame.draw.line(display, omino.color, (omino.rect.left, omino.rect.bottom), (omino.rect.left - 17, omino.rect.bottom + 34 + omino.sxdx), 2)
        pygame.draw.line(display, omino.color, (omino.rect.right, omino.rect.bottom), (omino.rect.right + 14, omino.rect.bottom + 34 - omino.sxdx), 2)
        pygame.display.flip()
        clock.tick(15)


def game_over_screen(score):
    animate_fall(omino)

    display.fill(WHITE)
    

    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, RED)
    display.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 - 50))
    
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Punteggio: {score}", True, BLACK)
    display.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - score_text.get_height() // 2 + 20))
    
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            highscore = int(file.read())
    else:
        highscore = 0
    if score > highscore:
        with open("highscore.txt", "w") as file:
            file.write(str(score))
        font = pygame.font.Font(None, 36)
        record_text = font.render(f"Nuovo record!", True, BLACK)
        display.blit(record_text, (WIDTH // 2 - record_text.get_width() // 2, HEIGHT // 2 - record_text.get_height() // 2 + 80))
    pygame.display.flip()

    time.sleep(3)


def next_level_screen(level):
    display.fill(WHITE)
    font = pygame.font.Font(None, 74)
    text = font.render("Bravo, continua!", True, RED)
    display.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 - 50))
    
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Prossimo livello: {level+1}", True, BLACK)
    display.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - score_text.get_height() // 2 + 20))
    
    pygame.display.flip()
    time.sleep(3)

# Ciclo principale del gioco
while running:
    clock.tick(FPS)

    # Eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimento omino
    keys = pygame.key.get_pressed()
    omino.move(keys)
    for barriera in barriere:
        if omino.rect.colliderect(barriera.rect):
            omino.barriera(keys)
    #print(keys)
    # if omino.rect.colliderect(barriera.rect):
    #     #print("Hai perso!")
    #     game_over_screen(score)
    #     time.sleep(1)
    #     running = False
    # Controllo collisioni
    for spit in spits[:]:
        if omino.rect.colliderect(spit.rect):
            spits.remove(spit)
            ultimo_spit = spit  # Memorizza l'ultimo spit raggiunto
            ultima_y = spit.y
            ultima_x = spit.x
            spits_raggiunti.append((spit.x, spit.y))
            score += 10
            # Mostra schermata di "Game Over" e punteggio


            # Controllo collisioni con ostacoli

    for ostacolo in ostacoli:
        if omino.rect.colliderect(ostacolo.rect):
            print("Hai perso!")
            game_over_screen(score)
            time.sleep(1)
            running = False

    if omino.rect.colliderect(arrivo.rect):
        if len(spits) == 0:

            score += 50
            livello += 1
            distanza_ostacoli -= 1
            if distanza_ostacoli == 0:
                distanza_ostacoli = 1
            valanga_speed += 1
            next_level_screen(livello-1)
            
            omino = Omino()
            spits = []
            for _ in range(5):
                spits.append(Spit())
            arrivo = Arrivo()
            ostacoli = [Ostacolo() for _ in range(3)]
            barriere = []
            while len(barriere) < np.min([livello, 8]):
                new_barriera = Barriera()
                if not any(new_barriera.rect.colliderect(spit.rect) for spit in spits):
                    barriere.append(new_barriera)

            #èer disegnare la corda nel nuovo livello
            ultimo_spit = None  # Resetta l'ultimo spit
            spits_raggiunti = []  # Resetta la lista
            spits_raggiunti.append((omino.x, omino.y))
            ultima_x = omino.x
            ultima_y = omino.y


    # Movimento ostacoli
    for ostacolo in ostacoli:
        ostacolo.move()

    # Disegna lo schermo
    display.fill(WHITE)
    omino.draw()
    arrivo.draw()
    for spit in spits:
        spit.draw()
    for ostacolo in ostacoli:
        ostacolo.draw()
    for barriera in barriere:
        barriera.draw()
    # Disegna la linea verso l'ultimo spit
    pygame.draw.line(
            display, BLACK,
            omino.rect.center,
            (ultima_x, ultima_y),
            2
        )

    # Disegna la linea tra gli spit raggiunti
    if ultimo_spit:
        pygame.draw.lines(display, BLACK, False, spits_raggiunti, 3)

    # Mostra punteggio
    font = pygame.font.Font(None, 36)
    text = font.render(f"Punteggio: {score}", True, BLACK)
    display.blit(text, (10, 10))

    # Mostra livello
    font = pygame.font.Font(None, 36)
    text2 = font.render(f"Level: {livello}", True, BLACK)
    display.blit(text2, (10, 40))

    # Mostra highscore
    font = pygame.font.Font(None, 36)
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            highscore = int(file.read())
    else:
        highscore = 0
    text3 = font.render(f"Highscore: {highscore}", True, BLACK)
    display.blit(text3, (10, 70))
    pygame.display.flip()
