import time

import pygame
import random

# Inizializza pygame
pygame.init()

# Costanti
WIDTH, HEIGHT = 800, 600
FPS = 60
OMINO_SPEED = 5
SPIT_RADIUS = 10

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


# Classe per gli spit
class Spit:
    def __init__(self):
        self.x = random.randint(0, WIDTH - SPIT_RADIUS * 2)
        self.y = random.randint(0, HEIGHT // 2)
        self.color = GRAY
        self.radius = SPIT_RADIUS
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)

    def draw(self):
        pygame.draw.circle(display, self.color, (self.x + self.radius, self.y + self.radius), self.radius)

# Classe per arrivo
class Arrivo:
    def __init__(self):
        self.x = random.randint(0, WIDTH - SPIT_RADIUS * 2)
        self.y = + SPIT_RADIUS * 2
        self.color = RED
        self.radius = SPIT_RADIUS
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)

    def draw(self):
        pygame.draw.circle(display, self.color, (self.x + self.radius, self.y + self.radius), self.radius)

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
        pygame.draw.rect(display, self.color, self.rect)

    def move(self):
        self.rect.y += valanga_speed
        if self.rect.top > HEIGHT:
            self.rect.y = random.randint(-200, -50)
            self.rect.x = random.randint(0, distanza_ostacoli * WIDTH - self.width)


# Inizializza oggetti
omino = Omino()
spits = [Spit() for _ in range(5)]
arrivo = Arrivo()
ostacoli = [Ostacolo() for _ in range(3)]

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

    # Controllo collisioni
    for spit in spits[:]:
        if omino.rect.colliderect(spit.rect):
            spits.remove(spit)
            ultimo_spit = spit  # Memorizza l'ultimo spit raggiunto
            ultima_y = spit.y
            ultima_x = spit.x
            spits_raggiunti.append((spit.x, spit.y))
            score += 10

    for ostacolo in ostacoli:
        if omino.rect.colliderect(ostacolo.rect):
            print("Hai perso!")
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
            time.sleep(2)
            omino = Omino()
            spits = [Spit() for _ in range(5)]
            arrivo = Arrivo()
            ostacoli = [Ostacolo() for _ in range(3)]

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

    pygame.display.flip()
