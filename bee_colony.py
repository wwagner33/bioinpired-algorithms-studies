import pygame
import random
import math

# Configurações iniciais
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUM_BEES = 30
NUM_FLOWERS = 8

# Classe para abelha
class Bee:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = 2
        self.returning = False
        self.target_flower = None

    def move(self):
        if not self.returning:
            self.x += self.speed * math.cos(self.angle)
            self.y += self.speed * math.sin(self.angle)
            if random.random() < 0.1:
                self.angle += random.uniform(-math.pi / 4, math.pi / 4)

            # Mantém a abelha dentro da tela
            if self.x < 0: self.x = 0
            if self.x > SCREEN_WIDTH: self.x = SCREEN_WIDTH
            if self.y < 0: self.y = 0
            if self.y > SCREEN_HEIGHT: self.y = SCREEN_HEIGHT
        else:
            if self.target_flower:
                dx = self.target_flower.x - self.x
                dy = self.target_flower.y - self.y
                self.angle = math.atan2(dy, dx)
                self.x += self.speed * math.cos(self.angle)
                self.y += self.speed * math.sin(self.angle)

                if abs(dx) < 5 and abs(dy) < 5:
                    self.returning = False
                    self.target_flower = None

    def search_flower(self, flowers):
        for flower in flowers:
            distance = math.hypot(flower.x - self.x, flower.y - self.y)
            if distance < 50:
                self.returning = True
                self.target_flower = flower
                break

# Classe para flor
class Flower:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.radius = 5

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 255), (int(self.x), int(self.y)), self.radius)

# Inicializa pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bee Colony Simulation')

# Criação de abelhas e flores
bees = [Bee() for _ in range(NUM_BEES)]
flowers = [Flower() for _ in range(NUM_FLOWERS)]

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Movimenta abelhas e busca flores
    for bee in bees:
        bee.move()
        bee.search_flower(flowers)
        pygame.draw.circle(screen, BLACK, (int(bee.x), int(bee.y)), 3)

    # Desenha flores
    for flower in flowers:
        flower.draw(screen)

    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()
