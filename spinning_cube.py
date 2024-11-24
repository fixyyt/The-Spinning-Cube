import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spinning Cube")

DARK = (1, 1, 1)
BRIGHT = (200, 200, 200)
TEXT_COLOR = (255, 255, 255)

clock = pygame.time.Clock()
FPS = 60

font = pygame.font.Font(None, 36)

# 3D Cube vertices and edges
cube_vertices = [
    [-1, -1, -1], [-1, -1, 1], [-1, 1, -1], [-1, 1, 1],
    [1, -1, -1], [1, -1, 1], [1, 1, -1], [1, 1, 1]
]

cube_edges = [
    (0, 1), (1, 3), (3, 2), (2, 0),
    (4, 5), (5, 7), (7, 6), (6, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

def project_3d_to_2d(point):
    scale = 400 / (point[2] + 5)  # Perspective scaling
    x = int(point[0] * scale + WIDTH // 2)
    y = int(-point[1] * scale + HEIGHT // 2)
    return x, y

def rotate(point, angle_x, angle_y):
    # Rotation around X axis
    x, y, z = point
    cos_x, sin_x = math.cos(angle_x), math.sin(angle_x)
    y, z = y * cos_x - z * sin_x, y * sin_x + z * cos_x

    # Rotation around Y axis
    cos_y, sin_y = math.cos(angle_y), math.sin(angle_y)
    x, z = x * cos_y + z * sin_y, -x * sin_y + z * cos_y

    return [x, y, z]

running = True
angle_x, angle_y = 0, 0

while running:
    screen.fill(DARK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rotate cube
    angle_x += 0.02
    angle_y += 0.03

    # Draw edges
    rotated_vertices = [rotate(vertex, angle_x, angle_y) for vertex in cube_vertices]
    projected_vertices = [project_3d_to_2d(vertex) for vertex in rotated_vertices]

    for edge in cube_edges:
        start, end = edge
        pygame.draw.line(screen, BRIGHT, projected_vertices[start], projected_vertices[end], 2)

    text_surface = font.render("The Spinning Cube by Fixy", True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 50)) 
    screen.blit(text_surface, text_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
