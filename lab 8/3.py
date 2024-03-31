import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    drawing_surface = pygame.Surface(screen.get_size())  # Create a drawing surface
    drawing_surface.fill((0, 0, 0))  # Fill it with black initially

    radius = 15
    mode = 'blue'  # Default drawing mode is 'blue'
    points = []
    drawing = False  # To check if the mouse is currently drawing

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
                # Tool selection
                elif event.key == pygame.K_e:  # Eraser
                    mode = 'eraser'
                elif event.key == pygame.K_c:  # Circle
                    mode = 'circle'
                elif event.key == pygame.K_t:  # Rectangle
                    mode = 'rect'

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                points = [event.pos]  # Start a new drawing path

            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                if mode in ['circle', 'rect']:
                    draw_shape(drawing_surface, points[0], event.pos, mode)
                points = []

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if drawing:
                    if mode in ['blue', 'red', 'green', 'eraser']:
                        if len(points) > 0:
                            drawLineBetween(drawing_surface, points[-1], position, radius, mode)
                        points.append(position)
                    elif mode in ['circle', 'rect']:
                        points = [points[0], position]  # Update current position for shape drawing

        screen.blit(drawing_surface, (0, 0))  # Copy the drawing surface to the screen

        # Draw the shape being currently drawn on top of everything
        if drawing and mode in ['circle', 'rect'] and len(points) > 1:
            draw_shape(screen, points[0], points[1], mode, preview=True)

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(surface, start, end, width, color_mode):
    color = (0, 0, 255)  # Default to blue
    if color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    elif color_mode == 'eraser':
        color = (0, 0, 0)  # Erase with black

    pygame.draw.line(surface, color, start, end, width)

def draw_shape(surface, start, end, shape_mode, preview=False):
    color = (255, 255, 255)  # Default to white for shapes
    if shape_mode == 'circle':
        center = start
        radius = int(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5)
        pygame.draw.circle(surface, color, center, radius)
    elif shape_mode == 'rect':
        rect = pygame.Rect(*start, end[0] - start[0], end[1] - start[1])
        if not preview:
            pygame.draw.rect(surface, color, rect)
        else:
            # For preview, draw a rectangle outline
            pygame.draw.rect(surface, color, rect, 2)  # Width of 2 for the outline

main()
