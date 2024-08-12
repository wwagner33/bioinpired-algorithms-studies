# Explanation:
# 1. Wolves: There is an alpha wolf that leads the hunt toward the prey. The following wolves adjust their positions by following the alpha.
# 2. Prey: The prey is positioned at a fixed point on the screen. The wolves' behavior is to encircle the prey as they approach.
# 3. Collective Movement: The algorithm shows the group's hunting behavior, with wolves following the alpha's lead to encircle and capture the prey.


import pygame
import random
import math

# Configurações iniciais
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUM_WOLVES = 10
PREY_X = 400
PREY_Y = 300

# Classe para lobo
class Wolf:
    def __init__(self, is_alpha=False):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.is_alpha = is_alpha
        self.speed = 2 if is_alpha else 1.5
        self.angle = random.uniform(0, 2 * math.pi)

    def move_towards_prey(self, prey_x, prey_y):
        self.angle = math.atan2(prey_y - self.y, prey_x - self.x)
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def follow_alpha(self, alpha_wolf):
        self.angle = math.atan2(alpha_wolf.y - self.y, alpha_wolf.x - self.x)
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

# Inicializa pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Grey Wolf Algorithm Simulation')

# Criação de lobos (um alfa e outros seguidores)
wolves = [Wolf(is_alpha=True)] + [Wolf() for _ in range(NUM_WOLVES - 1)]

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Movimenta o lobo alfa em direção à presa
    alpha_wolf = wolves[0]
    alpha_wolf.move_towards_prey(PREY_X, PREY_Y)
    pygame.draw.circle(screen, RED, (int(alpha_wolf.x), int(alpha_wolf.y)), 5)  # Lobo alfa

    # Outros lobos seguem o alfa
    for wolf in wolves[1:]:
        wolf.follow_alpha(alpha_wolf)
        pygame.draw.circle(screen, BLACK, (int(wolf.x), int(wolf.y)), 4)  # Lobos seguidores

    # Desenha a presa
    pygame.draw.circle(screen, GREEN, (PREY_X, PREY_Y), 8)  # Presa

    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()
