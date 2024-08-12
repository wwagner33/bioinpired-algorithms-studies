import pygame
import random
import math

# Configurações iniciais
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUM_FIREFLIES = 30

# Classe para vagalume
class Firefly:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.intensity = random.uniform(0.5, 1.0)
        self.speed = 2

    def move(self):
        self.x += random.uniform(-1, 1) * self.speed
        self.y += random.uniform(-1, 1) * self.speed
        
        # Mantém o vagalume dentro da tela
        if self.x < 0: self.x = 0
        if self.x > SCREEN_WIDTH: self.x = SCREEN_WIDTH
        if self.y < 0: self.y = 0
        if self.y > SCREEN_HEIGHT: self.y = SCREEN_HEIGHT

    def attract(self, other):
        if self.intensity > other.intensity:
            angle = math.atan2(self.y - other.y, self.x - other.x)
            other.x += self.speed * math.cos(angle)
            other.y += self.speed * math.sin(angle)

# Inicializa pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Firefly Algorithm Simulation')

# Criação de vagalumes
fireflies = [Firefly() for _ in range(NUM_FIREFLIES)]

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Movimenta vagalumes e simula atração
    for i, firefly in enumerate(fireflies):
        firefly.move()
        for j, other in enumerate(fireflies):
            if i != j:
                firefly.attract(other)
        pygame.draw.circle(screen, (int(255 * firefly.intensity), 255, 0), (int(firefly.x), int(firefly.y)), 5)

    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()
