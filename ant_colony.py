import pygame
import random
import math

# Configurações iniciais
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUM_ANTS = 50
NUM_FOOD = 5

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Classe para formiga
class Ant:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = 2
        self.pheromone = []

    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        
        # Mantém a formiga dentro da tela
        if self.x < 0: self.x = 0
        if self.x > SCREEN_WIDTH: self.x = SCREEN_WIDTH
        if self.y < 0: self.y = 0
        if self.y > SCREEN_HEIGHT: self.y = SCREEN_HEIGHT

        # Simula comportamento de seguir feromônios (simplificado)
        if random.random() < 0.1:
            self.angle += random.uniform(-math.pi/4, math.pi/4)
    
    def drop_pheromone(self):
        self.pheromone.append((self.x, self.y))

# Classe para comida
class Food:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.radius = 5

    def draw(self, screen):
        pygame.draw.circle(screen, GREEN, (int(self.x), int(self.y)), self.radius)

# Inicializa pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ant Colony Simulation')

# Criação de formigas e comida
ants = [Ant() for _ in range(NUM_ANTS)]
foods = [Food() for _ in range(NUM_FOOD)]

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Movimenta formigas e desenha feromônios
    for ant in ants:
        ant.move()
        ant.drop_pheromone()
        for pheromone in ant.pheromone:
            pygame.draw.circle(screen, RED, (int(pheromone[0]), int(pheromone[1])), 2)
        pygame.draw.circle(screen, BLACK, (int(ant.x), int(ant.y)), 3)

    # Desenha comida
    for food in foods:
        food.draw(screen)

    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()
