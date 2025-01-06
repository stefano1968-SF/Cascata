import time

import pygame
import random
import numpy as np
import os

# Inizializza pygame
pygame.init()

# Costanti
WIDTH, HEIGHT = 800, 600
FPS = 30
OMINO_SPEED = 10
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
        self.dxsx = 1
        self.color_head = BLACK
        self.rect = pygame.Rect(self.x - self.body_width // 2, self.y - self.body_height // 2, self.body_width,
                                self.body_height)

    def draw(self):
        # Disegna il corpo rettangolare
        # pygame.draw.rect(display, self.color, self.rect)

        # # Disegna la testa
        # head_center = (self.rect.centerx, self.rect.top - self.head_radius)
        # pygame.draw.circle(display, self.color_head, head_center, self.head_radius)
        # Carica l'immagine
        torso_head_image = pygame.image.load('images/torso_head.png')
        torso_head_image = pygame.transform.scale(torso_head_image, (self.body_width*1.85, (self.body_height + self.head_radius * 2)*1.35))

        # Calcola la posizione dell'immagine
        image_rect = torso_head_image.get_rect(center=(self.rect.centerx, self.rect.centery - self.head_radius+ 17))

        # Disegna l'immagine
        display.blit(torso_head_image, image_rect)
        # Disegna le braccia
        pygame.draw.line(display, self.color, (self.rect.left, self.rect.y),
                         (self.rect.left - 30 - self.dxsx, self.rect.centery - 30 - self.sxdx), 3)
        pygame.draw.line(display, self.color, (self.rect.right, self.rect.y),
                         (self.rect.right + 30 - self.dxsx, self.rect.centery - 30 + self.sxdx), 3)

        # Disegna le gambe
        pygame.draw.line(display, self.color, (self.rect.left, self.rect.bottom),
                         (self.rect.left - 10 - self.dxsx, self.rect.bottom + 30 + self.sxdx), 2)
        pygame.draw.line(display, self.color, (self.rect.right, self.rect.bottom),
                         (self.rect.right + 10 + self.dxsx, self.rect.bottom + 30 - self.sxdx), 2)

    def move(self, keys):
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left > 0:
            self.rect.x -= OMINO_SPEED
            self.sxdx = 1
            if self.dxsx == 20:
                self.dxsx = 11
            elif self.dxsx == 11:
                self.dxsx = 1
            elif self.dxsx == 1:
                self.dxsx = -10
            elif self.dxsx == -10:
                self.dxsx = -20
            elif self.dxsx == -20:
                self.dxsx = -11
            elif self.dxsx == -11:
                self.dxsx = -1
            elif self.dxsx == -1:
                self.dxsx = 10
            elif self.dxsx == 10:
                self.dxsx = 20
            

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right < WIDTH:
            self.rect.x += OMINO_SPEED
            self.sxdx = 1
            if self.dxsx == 20:
                self.dxsx = 11
            elif self.dxsx == 11:
                self.dxsx = 1
            elif self.dxsx == 1:
                self.dxsx = -10
            elif self.dxsx == -10:
                self.dxsx = -20
            elif self.dxsx == -20:
                self.dxsx = -11
            elif self.dxsx == -11:
                self.dxsx = -1
            elif self.dxsx == -1:
                self.dxsx = 10
            elif self.dxsx == 10:
                self.dxsx = 20
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.rect.top > 0:
            self.rect.y -= OMINO_SPEED
            self.dxsx = 1
            if self.sxdx == 30:
                self.sxdx = 21
            elif self.sxdx == 21:
                self.sxdx = 11
            elif self.sxdx == 11:
                self.sxdx = 1
            elif self.sxdx == 1:
                self.sxdx = -10
            elif self.sxdx == -10:
                self.sxdx = -20
            elif self.sxdx == -20:
                self.sxdx = -30
            elif self.sxdx == -30:
                self.sxdx = -21
            elif self.sxdx == -21:
                self.sxdx = -11
            elif self.sxdx == -11:
                self.sxdx = -1
            elif self.sxdx == -1:
                self.sxdx = 10
            elif self.sxdx == 10:
                self.sxdx = 20
            elif self.sxdx == 20:
                self.sxdx = 30

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.rect.bottom < HEIGHT:
            self.rect.y += OMINO_SPEED
            self.dxsx = 1
            if self.sxdx == 30:
                self.sxdx = 21
            elif self.sxdx == 21:
                self.sxdx = 11
            elif self.sxdx == 11:
                self.sxdx = 1
            elif self.sxdx == 1:
                self.sxdx = -10
            elif self.sxdx == -10:
                self.sxdx = -20
            elif self.sxdx == -20:
                self.sxdx = -30
            elif self.sxdx == -30:
                self.sxdx = -21
            elif self.sxdx == -21:
                self.sxdx = -11
            elif self.sxdx == -11:
                self.sxdx = -1
            elif self.sxdx == -1:
                self.sxdx = 10
            elif self.sxdx == 10:
                self.sxdx = 20
            elif self.sxdx == 20:
                self.sxdx = 30

    def barriera(self, keys):
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left > 0:
            self.rect.x += OMINO_SPEED
            self.sxdx = 1
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right < WIDTH:
            self.rect.x -= OMINO_SPEED
            self.sxdx = 1
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.rect.top > 0:
            self.rect.y += OMINO_SPEED
            if self.sxdx == 30:
                self.sxdx = 21
            elif self.sxdx == 21:
                self.sxdx = 11
            elif self.sxdx == 11:
                self.sxdx = 1
            elif self.sxdx == 1:
                self.sxdx = -10
            elif self.sxdx == -10:
                self.sxdx = -20
            elif self.sxdx == -20:
                self.sxdx = -30
            elif self.sxdx == -30:
                self.sxdx = -21
            elif self.sxdx == -21:
                self.sxdx = -11
            elif self.sxdx == -11:
                self.sxdx = -1
            elif self.sxdx == -1:
                self.sxdx = 10
            elif self.sxdx == 10:
                self.sxdx = 20
            elif self.sxdx == 20:
                self.sxdx = 30

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.rect.bottom < HEIGHT:
            self.rect.y -= OMINO_SPEED
            if self.sxdx == 30:
                self.sxdx = 21
            elif self.sxdx == 21:
                self.sxdx = 11
            elif self.sxdx == 11:
                self.sxdx = 1
            elif self.sxdx == 1:
                self.sxdx = -10
            elif self.sxdx == -10:
                self.sxdx = -20
            elif self.sxdx == -20:
                self.sxdx = -30
            elif self.sxdx == -30:
                self.sxdx = -21
            elif self.sxdx == -21:
                self.sxdx = -11
            elif self.sxdx == -11:
                self.sxdx = -1
            elif self.sxdx == -1:
                self.sxdx = 10
            elif self.sxdx == 10:
                self.sxdx = 20
            elif self.sxdx == 20:
                self.sxdx = 30

    def bump(self, xx, yy):
        self.rect.x += 20 * OMINO_SPEED * xx
        self.rect.y += 20 * OMINO_SPEED * yy


# Classe per gli spit
class Spit:
    def __init__(self):
        self.x = random.randint(0, WIDTH - SPIT_RADIUS * 2)
        self.y = random.randint(int(HEIGHT * 0.1), int(HEIGHT // 1.2))
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
        # self.y = random.randint(HEIGHT*0.2, HEIGHT *0.8)
        self.width = random.randint(50, 100)
        self.height = random.randint(10, 40)
        self.color = BLACK
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(display, self.color, self.rect)


# Classe per le valanghe e le stalattiti
class Ostacolo:
    def __init__(self, speed, distanza):
        self.x = random.randint(0, WIDTH - 20)
        self.y = random.randint(-200, -50)
        self.width = 20
        self.height = 50
        self.color = GRAY
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.valanga_speed = speed
        self.distanza_ostacoli = distanza

    def draw(self):
        # pygame.draw.rect(display, self.color, self.rect)
        pygame.draw.polygon(display, self.color, [(self.rect.x, self.rect.y), (self.rect.x + self.width, self.rect.y),
                                                  (self.rect.x + self.width // 2, self.rect.y + self.height)])

    def move(self):
        self.rect.y += self.valanga_speed
        if self.rect.top > HEIGHT:
            self.rect.y = random.randint(-200, -50)
            self.rect.x = random.randint(0, self.distanza_ostacoli * WIDTH - self.width)


# Classe per Capretti
class Capretto:
    def __init__(self, speed):
        self.x = random.randint(0, WIDTH - 30)
        self.y = random.randint(-200, HEIGHT - 60)
        self.width = 40
        self.height = 10
        self.color_head = BLUE
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.capra_speed = speed
        self.dx = 1

    def draw(self):
        # Disegna il corpo rettangolare
        pygame.draw.rect(display, self.color_head, self.rect)

        # Disegna la testa
        head_center = (self.rect.x, self.rect.top - 10)
        pygame.draw.circle(display, self.color_head, head_center, 10)
        # Carica l'immagine
        capra_image = pygame.image.load('images/capra.png')
        if self.dx == 1:
            capra_image = pygame.transform.flip(capra_image, True, False)
        capra_image = pygame.transform.scale(capra_image, (self.width * 2, (self.height + 20)*2))

        # Calcola la posizione dell'immagine
        image_rect = capra_image.get_rect(center=(self.rect.centerx, self.rect.centery - 10))

        # Disegna l'immagine
        display.blit(capra_image, image_rect)
        # Disegna le gambe
        pygame.draw.line(display, BLACK, (self.rect.left, self.rect.bottom),
                         (self.rect.left - 5, self.rect.bottom + 20), 2)
        pygame.draw.line(display, BLACK, (self.rect.left, self.rect.bottom),
                         (self.rect.left + 5, self.rect.bottom + 20), 2)
        pygame.draw.line(display, BLACK, (self.rect.right, self.rect.bottom),
                         (self.rect.right - 5, self.rect.bottom + 20), 2)
        pygame.draw.line(display, BLACK, (self.rect.right, self.rect.bottom),
                         (self.rect.right + 5, self.rect.bottom + 20), 2)

    def move(self, ominox, ominoy):
        self.rect.x += self.capra_speed * - np.sign(self.rect.x - ominox)
        self.rect.y += self.capra_speed * - np.sign(self.rect.y - ominoy)
        self.dx = 1* np.sign(self.rect.x - ominox)
    def bump(self, xx, yy):
        self.rect.x += -20 * OMINO_SPEED * xx
        self.rect.y += -20 * OMINO_SPEED * yy


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
    for rotola in range(20):
        display.fill(WHITE)
        # Disegna il corpo diviso in pezzi
        pygame.draw.rect(display, omino.color, (
        omino.rect.x - 15 + rotola * 6, omino.rect.y - 144 + (rotola - 12) ** 2, omino.body_width,
        omino.body_height // 2))
        pygame.draw.rect(display, omino.color, (
        omino.rect.x + 15 - rotola * 13, omino.rect.y + omino.body_height // 2 + 10 - 64 + (rotola - 8) ** 2,
        omino.body_width, omino.body_height // 2))
        pygame.draw.circle(display, omino.color_head, (
        omino.rect.centerx + rotola * 15, omino.rect.top - 100 + (rotola - 10) ** 2 - omino.head_radius),
                           omino.head_radius)
        pygame.draw.line(display, omino.color, (omino.rect.left - rotola * 2, omino.rect.y + rotola * 10),
                         (omino.rect.left - 35 - rotola * 2, omino.rect.centery - 20 - omino.sxdx + rotola * 10), 3)
        pygame.draw.line(display, omino.color, (omino.rect.right + rotola * 30, omino.rect.y + rotola * 10),
                         (omino.rect.right + 33 + rotola * 30, omino.rect.centery - 20 + omino.sxdx + rotola * 10), 3)
        pygame.draw.line(display, omino.color, (omino.rect.left - rotola * 12, omino.rect.bottom + rotola * 10),
                         (omino.rect.left - 17 - rotola * 12, omino.rect.bottom + 34 + omino.sxdx + rotola * 10), 2)
        pygame.draw.line(display, omino.color, (omino.rect.right + rotola * 4, omino.rect.bottom + rotola * 10),
                         (omino.rect.right + 14 + rotola * 4, omino.rect.bottom + 34 - omino.sxdx + rotola * 10), 2)
        pygame.display.flip()
        clock.tick(15)


def game_over_screen(score, omino):
    animate_fall(omino)

    display.fill(WHITE)

    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, RED)
    display.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 - 50))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Punteggio: {score}", True, BLACK)
    display.blit(score_text,
                 (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - score_text.get_height() // 2 + 20))

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
        display.blit(record_text,
                     (WIDTH // 2 - record_text.get_width() // 2, HEIGHT // 2 - record_text.get_height() // 2 + 80))
    pygame.display.flip()

    time.sleep(3)


def next_level_screen(level):
    display.fill(WHITE)
    font = pygame.font.Font(None, 74)
    text = font.render("Bravo, continua!", True, RED)
    display.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 - 50))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Prossimo livello: {level + 1}", True, BLACK)
    display.blit(score_text,
                 (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - score_text.get_height() // 2 + 20))

    pygame.display.flip()
    time.sleep(3)


def main():
    # Inizializza oggetti
    omino = Omino()
    spits = [Spit() for _ in range(5)]
    arrivo = Arrivo()
    ostacoli = [Ostacolo(4, 5) for _ in range(3)]
    barriere = []
    capretti = []

    while len(barriere) == 0:
        barriera_temp = Barriera()
        if not any(barriera_temp.rect.colliderect(spit.rect) for spit in spits):
            barriere.append(barriera_temp)

    # Variabili di gioco
    score = 0
    livello = 1
    running = True
    distanza_ostacoli = 5
    valanga_speed = 8
    capra_speed = 2
    ultimo_spit = None
    spits_raggiunti = []
    spits_raggiunti.append((omino.x, omino.y))
    ultima_x = omino.x
    ultima_y = omino.y

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

        # Controllo collisioni

        for capretto in capretti[:]:
            if omino.rect.colliderect(capretto.rect):
                direzione_x = np.sign(omino.rect.x - capretto.rect.x)
                direzione_y = np.sign(omino.rect.y - capretto.rect.y)
                omino.bump(direzione_x, direzione_y)
                capretto.bump(direzione_x, direzione_y)

        for spit in spits[:]:
            if omino.rect.colliderect(spit.rect):
                spits.remove(spit)
                ultimo_spit = spit  # Memorizza l'ultimo spit raggiunto
                ultima_y = spit.y
                ultima_x = spit.x
                spits_raggiunti.append((spit.x, spit.y))
                score += 10

        # Controllo collisioni con ostacoli
        for ostacolo in ostacoli:
            if omino.rect.colliderect(ostacolo.rect):
                game_over_screen(score, omino)
                time.sleep(1)
                while True:
                    for event in pygame.event.get():
                        display.fill(WHITE)

                        font = pygame.font.Font(None, 36)
                        score_text = font.render("Schiaccia Q per uscire or R per ricominciare", True, BLACK)
                        display.blit(score_text, (
                        WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - score_text.get_height() // 2 + 20))
                        pygame.display.flip()
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                main()  # Restart the game
                            if event.key == pygame.K_q:
                                pygame.quit()
                                exit()
                running = False

        if omino.rect.colliderect(arrivo.rect):
            if len(spits) == 0:
                score += 50
                livello += 1
                distanza_ostacoli -= 1
                if distanza_ostacoli == 0:
                    distanza_ostacoli = 1
                valanga_speed += 1
                next_level_screen(livello - 1)

                omino = Omino()
                spits = []
                for _ in range(5):
                    spits.append(Spit())
                arrivo = Arrivo()
                ostacoli = [Ostacolo(valanga_speed, distanza_ostacoli) for _ in range(3)]

                barriere = []
                while len(barriere) < np.min([livello, 8]):
                    new_barriera = Barriera()
                    if not any(new_barriera.rect.colliderect(spit.rect) for spit in spits):
                        barriere.append(new_barriera)

                capretti = []
                while len(capretti) < np.min([livello - 3, 1]):

                    capretti.append(Capretto(capra_speed))

                # Per disegnare la corda nel nuovo livello
                ultimo_spit = None  # Resetta l'ultimo spit
                spits_raggiunti = []  # Resetta la lista
                spits_raggiunti.append((omino.x, omino.y))
                ultima_x = omino.x
                ultima_y = omino.y

            # Movimento ostacoli
        for ostacolo in ostacoli:
            ostacolo.move()

            # Movimento capretto
        for capretto in capretti:
            capretto.move(omino.rect.x, omino.rect.y)

        # Disegna lo schermo
        display.fill(WHITE)
        omino.draw()
        arrivo.draw()
        for capretto in capretti:
            capretto.draw()
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
        font = pygame.font.Font(None, 24)
        text = font.render(f"Punteggio: {score}", True, BLACK)
        display.blit(text, (10, 10))

        # Mostra livello
        font = pygame.font.Font(None, 24)
        text2 = font.render(f"Level: {livello}", True, BLACK)
        display.blit(text2, (10, 35))

        # Mostra highscore
        font = pygame.font.Font(None, 24)
        if os.path.exists("highscore.txt"):
            with open("highscore.txt", "r") as file:
                highscore = int(file.read())
        else:
            highscore = 0
        text3 = font.render(f"Highscore: {highscore}", True, BLACK)
        display.blit(text3, (10, 60))
        pygame.display.flip()


def entry_screen():
    running_start = True
    omino = Omino()
    omino.x = WIDTH // 2
    omino.rect.y = HEIGHT // 2 - 40
    omino.sxdx = 30
    print(omino.y)
    spits = [Spit() for _ in range(5)]
    arrivo = Arrivo()
    while running_start:
        clock.tick(FPS)
        display.fill(WHITE)
        font = pygame.font.Font(None, 36)

        title_text = font.render("Aiuta Leonardo a completare la scalata sulle cascate di ghiaccio", True, BLACK)
        display.blit(title_text,
                     (WIDTH // 2 - title_text.get_width() // 2, -120 + HEIGHT // 2 - title_text.get_height() // 2 + 20))
        font = pygame.font.Font(None, 36)
        help_text = font.render("Raggiungi tutti i rinvii, fino a quello rosso in alto", True, BLACK)
        display.blit(help_text,
                     (WIDTH // 2 - help_text.get_width() // 2, +40 + HEIGHT // 2 - help_text.get_height() // 2 + 20))
        help2_text = font.render("Muoviti usando le frecce ed evita le stalattiti che cadono dall'alto", True, BLACK)
        display.blit(help2_text,
                     (WIDTH // 2 - help2_text.get_width() // 2, +80 + HEIGHT // 2 - help2_text.get_height() // 2 + 20))
        via_text = font.render("Premi N per proseguire", True, BLACK)
        display.blit(via_text,
                     (WIDTH // 2 - via_text.get_width() // 2, 180 + HEIGHT // 2 - via_text.get_height() // 2 + 20))

        omino.draw()
        arrivo.draw()
        for spit in spits:
            spit.draw()

        # Disegna la linea tra gli spit raggiunti

        keys = pygame.key.get_pressed()
        omino.move(keys)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    main()  # via
                if event.key == pygame.K_q:
                    running_start = False

        keys = pygame.key.get_pressed()
        omino.move(keys)


if __name__ == "__main__":
    entry_screen()


