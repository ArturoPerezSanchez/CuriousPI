import pygame
import random
import time
import math

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH = 1600
HEIGHT = 400

# Colores
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (50, 50, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Numero de colisiones
collisions = 0
background = pygame.image.load('images/background.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Tamaños de fuentes
mass_text_font = pygame.font.Font(None, 30)
speed_text_font = pygame.font.Font(None, 25)
score_font = pygame.font.Font(None, 40)
final_font = pygame.font.Font(None, 90)

class Block:
    def __init__(self, x=0, y=0, size=20, color=(255, 255, 255), speed=0, mass=1, minX=0):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed
        self.mass = mass
        self.minX = minX

    def move(self):

        self.x += self.speed / 3

    def draw(self, window):
        # Dibuja el cuadrado con transparencia
        s = pygame.Surface((self.size, self.size))  # Tamaño del rectángulo
        s.set_alpha(64)
        s.fill(self.color)  # Rellena toda la superficie
        window.blit(s, (int(max(self.x, self.minX)), int(self.y)))  # Coordenadas superiores izquierdas

        # Dibuja el borde del cuadrado sin transparencia
        pygame.draw.rect(window, self.color, (int(max(self.x, self.minX)), int(self.y), self.size, self.size), 2)

        # Dibuja el texto de la masa
        mass_text_value = f"{format(self.mass, '' if self.mass < 1e5 else '.2e')} kg"
        mass_text = mass_text_font.render(mass_text_value, True, BLACK)
        mass_text_rect = mass_text.get_rect(center=(max(self.x, self.minX) + self.size / 2, self.y + self.size / 3))
        window.blit(mass_text, mass_text_rect)

        # Dibuja el texto de la velocidad
        speed_text_value = f"{self.speed:.3f} m/s"
        speed_text = speed_text_font.render(speed_text_value, True, BLACK)
        speed_text_rect = speed_text.get_rect(center=(max(self.x, self.minX) + self.size / 2, self.y + 2 * self.size / 3))
        window.blit(speed_text, speed_text_rect)

def collide(b1, b2):
    # Cantidad de movimiento
    quantity_of_movement = b1.mass * b1.speed + b2.mass * b2.speed

    # Diferencia de velocidades
    r = b1.speed - b2.speed

    b1_new_speed = (quantity_of_movement - b2.mass * r) / (b1.mass + b2.mass)
    b2_new_speed = r + b1_new_speed

    return b1_new_speed, b2_new_speed

# Creación de la ventana
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulación de Bloques")

# Creación de los bloques
block_size = 85
block_blue = Block(x=3 * WIDTH / 4, y=HEIGHT - block_size, size=block_size, color=BLUE, speed=0, mass=10)
block_red = Block(x=WIDTH - block_size, y=HEIGHT - block_size * 2, size=block_size * 2, color=RED, speed=-1, mass=1e5, minX=block_blue.size)


# Cuenta atras final
final_countdown = 3000

# Bucle principal del juego
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del bloque rojo
    block_red.move()

    # Colisión entre los bloques
    if block_blue.x + block_blue.size >= block_red.x:
        collisions += 1
        block_blue.speed, block_red.speed = collide(block_blue, block_red)

    # Cambio de dirección del bloque azul
    if block_blue.x <= 0:
        collisions += 1
        block_blue.speed *= -1

    # Movimiento del bloque azul
    block_blue.move()

    # Dibujo en la pantalla
    window.fill(GRAY)

    window.blit(background, (0, 0))
    collisions_text = f"Number of collisions = {collisions}"
    collisions_text_render = score_font.render(collisions_text, True, WHITE)
    collisions_text_rect = collisions_text_render.get_rect(center=(WIDTH // 2, 20))
    window.blit(collisions_text_render, collisions_text_rect)  # Dibujar el cuadro de texto

    pi_text = f"Pi approximation = {collisions / (10 ** (len(str(collisions)) - 1))}"
    pi_text_render = score_font.render(pi_text, True, WHITE)
    pi_text_rect = pi_text_render.get_rect(center=(WIDTH // 2, 50))
    window.blit(pi_text_render, pi_text_rect)  # Dibujar el cuadro de texto

    block_blue.draw(window)
    block_red.draw(window)
    

    if(block_blue.speed > 0 and block_red.speed > block_blue.speed):
        final_text = f"π = {collisions / (10 ** (len(str(collisions)) - 1))}"
        final_text_render = final_font.render(final_text, True, BLACK)
        final_text_rect = final_text_render.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        window.blit(final_text_render, final_text_rect)  # Dibujar el cuadro de texto
        
        final_countdown -=1
        if(final_countdown < 0):
            running = False

    pygame.display.flip()

    time.sleep(0.001)  # Limita la velocidad de fotogramas

# Cierre de la ventana y finalización de Pygame
pygame.quit()
