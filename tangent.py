from math import sqrt, asin, atan2, sin, cos

"""
    Finds tangent point from starting point and circle.

    point_x (float) : starting point x coordinate;
    point_y (float) : starting point y coordinate;
    circle_x (float) : circle center point x coordinate;
    circle_y (float) : circle center point y coordinate;
    circle_r (float) : circle radius;
    alt (bool) : find the second tangent.

    (tangent_x, tangent_y) (tuple) : tangent point x and y coordinates.
"""
def find_tangent(point_x, point_y, circle_x, circle_y, circle_r, alt=True):
    point_to_center = sqrt((circle_x - point_x)**2 + (circle_y - point_y)**2)
    try:
        point_to_tangent = sqrt(point_to_center**2 - circle_r**2)
    except ValueError:
        raise ValueError("Point has to be outside of circle.") from None
    tangent_angle = asin(circle_r / point_to_center) * (alt * 2 - 1) - atan2(circle_y - point_y, circle_x - point_x)

    tangent_x = point_x + point_to_tangent * cos(tangent_angle)
    tangent_y = point_y - point_to_tangent * sin(tangent_angle)

    return (tangent_x, tangent_y)





if __name__ == "__main__":
    class Circle:
        def __init__(self, x, y, r):
            self.x = x
            self.y = y
            self.r = r

            self.line_width = 1

        def draw(self, surf):
            pygame.draw.circle(surf,
                               (255, 255, 255),
                               (self.x, self.y),
                               self.r,
                               self.line_width)


    class Point:
        def __init__(self, x, y, color):
            self.x = x
            self.y = y
            self.color = color

            self.size = 4

        def draw(self, surf):
            pygame.draw.circle(surf,
                               self.color,
                               (self.x, self.y),
                               self.size)


    import pygame
    pygame.init()

    WIN_SIZE = (500, 500)
    win = pygame.display.set_mode(WIN_SIZE)

    font = pygame.font.SysFont("arial", 24)
    label = font.render("Press LMB to switch tangent",
                        True,
                        (255, 255, 255))

    circle = Circle(250, 250, 80)
    start = Point(50, 250, (0, 255, 0))

    alt = True

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    alt = not alt

        mouse_pos = pygame.mouse.get_pos()
        start.x = mouse_pos[0]
        start.y = mouse_pos[1]
        tangent_coords = find_tangent(start.x,
                                      start.y,
                                      circle.x,
                                      circle.y,
                                      circle.r,
                                      alt)
        tangent = Point(tangent_coords[0], tangent_coords[1], (255, 0, 0))
                    
        win.fill((0, 0, 0))
        win.blit(label, (10, 10))
        circle.draw(win)
        pygame.draw.line(win,
                         (255, 0, 0),
                         (start.x + (start.x - tangent.x) * 1000,
                          start.y + (start.y - tangent.y) * 1000),
                         (tangent.x + (tangent.x - start.x) * 1000,
                          tangent.y + (tangent.y - start.y) * 1000),
                         2)
        start.draw(win)
        tangent.draw(win)
        pygame.display.update()

    pygame.quit()
