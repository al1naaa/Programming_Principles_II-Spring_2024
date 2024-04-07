import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    drawing_surface = pygame.Surface(screen.get_size())
    drawing_surface.fill((0, 0, 0))

    mode = 'blue'
    points = []
    drawing = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                # Color selection
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                # Shape selection
                elif event.key == pygame.K_e:
                    mode = 'eraser'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_p:
                    mode = 'rect'
                elif event.key == pygame.K_s:  # Square
                    mode = 'square'
                elif event.key == pygame.K_t:  # Right triangle
                    mode = 'right_triangle'
                elif event.key == pygame.K_q:  # Equilateral triangle
                    mode = 'equilateral_triangle'
                elif event.key == pygame.K_m:  # Rhombus
                    mode = 'rhombus'

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                points = [event.pos]

            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                if mode in ['circle', 'rect', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                    draw_shape(drawing_surface, points[0], event.pos, mode)
                points = []

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if drawing:
                    if mode in ['blue', 'red', 'green', 'eraser']:
                        if len(points) > 0:
                            drawLineBetween(drawing_surface, points[-1], position, 10, mode)
                        points.append(position)
                    elif mode in ['circle', 'rect', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                        points = [points[0], position]

        screen.blit(drawing_surface, (0, 0))

        if drawing and mode in ['circle', 'rect', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus'] and len(points) > 1:
            draw_shape(screen, points[0], points[1], mode, preview=True)

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(surface, start, end, width, color_mode):
    color = (0, 0, 255)
    if color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    elif color_mode == 'eraser':
        color = (0, 0, 0)
    pygame.draw.line(surface, color, start, end, width)

def draw_shape(surface, start, end, shape_mode, preview=False):
    color = (255, 255, 255)
    if shape_mode == 'circle':
        # Draw circle
        center = start
        radius = int(math.hypot(end[0] - start[0], end[1] - start[1]))
        pygame.draw.circle(surface, color, center, radius)
    elif shape_mode in ['rect', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
        # Draw rectangle, square, or other shapes
        if shape_mode == 'rect' or shape_mode == 'square':
            rect = pygame.Rect(*start, end[0] - start[0], end[1] - start[1])
            if shape_mode == 'square':
                size = min(rect.width, rect.height)
                rect.width = rect.height = size
            pygame.draw.rect(surface, color, rect, 0 if not preview else 2)
        elif shape_mode == 'right_triangle':
            pygame.draw.polygon(surface, color, [start, (start[0], end[1]), end], 0 if not preview else 2)
        elif shape_mode == 'equilateral_triangle':
            height = end[1] - start[1]
            pygame.draw.polygon(surface, color, [start, (start[0] + 2 * height / math.sqrt(3), start[1]), (start[0] + height / math.sqrt(3), end[1])], 0 if not preview else 2)
        elif shape_mode == 'rhombus':
            dx = end[0] - start[0]
            pygame.draw.polygon(surface, color, [start, (start[0] + dx / 2, start[1] - dx / 2), end, (start[0] + dx / 2, start[1] + dx / 2)], 0 if not preview else 2)

main()
