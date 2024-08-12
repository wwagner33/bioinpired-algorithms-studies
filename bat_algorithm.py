# Explanation:
# 1. Bats: Move around the screen, adjusting direction based on their pulse frequency.
# 2. Echolocation: Bats locate targets based on distance and adjust their direction to chase them, simulating hunting behavior.
# 3. Targets: Randomly distributed on the screen, representing prey that bats attempt to capture.


import pygame
import random
import math

# Configurações iniciais
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUM_BATS = 20
NUM_TARGETS = 5

# Classe para morcego
class Bat:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.velocity = random.uniform(1, 3)
        self.frequency = random.uniform(0.5, 2.0)
        self.loudness = random.uniform(0.5, 1.0)
        self.angle = random.uniform(0, 2 * math.pi)
        self.target = None

    def move(self):
        self.x += self.velocity * math.cos(self.angle)
        self.y += self.velocity * math.sin(self.angle)

        # Mantém o morcego dentro da tela
        if self.x < 0: self.x = 0
        if self.x > SCREEN_WIDTH: self.x = SCREEN_WIDTH
        if self.y < 0: self.y = 0
        if self.y > SCREEN_HEIGHT: self.y = SCREEN_HEIGHT

        # Ajuste de direção baseado na frequência
        if random.random() < self.frequency:
            self.angle += random.uniform(-math.pi / 4, math.pi / 4)

    def echolocate(self, targets):
        for target in targets:
            distance = math.hypot(target.x - self.x, target.y - self.y)
            if distance < self.loudness * 100:  # alcance baseado na amplitude do som
                self.target = target
                self.angle = math.atan2(target.y - self.y, target.x - self.x)
                break

# Classe para alvo (presa)
class Target:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.radius = 5

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)

# Inicializa pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bat Algorithm Simulation')

# Criação de morcegos e alvos
bats = [Bat() for _ in range(NUM_BATS)]
targets = [Target() for _ in range(NUM_TARGETS)]

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Movimenta morcegos e ecolocaliza alvos
    for bat in bats:
        bat.move()
        bat.echolocate(targets)
        pygame.draw.circle(screen, BLACK, (int(bat.x), int(bat.y)), 3)

    # Desenha alvos
    for target in targets:
        target.draw(screen)

    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()
