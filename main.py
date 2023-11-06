import pygame
import numpy as np
import random


def dist(pointA, pointB):
    return np.sqrt((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2)


def near_points(point):
    count = random.randint(2, 5)
    points_array = []
    for i in range(count):
        x = random.randint(-20, 20)
        y = random.randint(-20, 20)
        points_array.append((point[0] + x, point[1] + y))
    return points_array


if __name__ == '__main__':
    RED = 'red'
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.fill(color="#FFFFFF")
    pygame.display.update()
    is_active = True
    is_pressed = False
    points = []
    count_of_keyup = 0
    while (is_active):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_pressed = True
                if event.button == 1:
                    is_pressed = True
                    coord = event.pos
                    points.append(coord)
                    pygame.draw.circle(screen, color=RED, center=coord, radius=5)
            if event.type == pygame.MOUSEBUTTONUP:
                is_pressed = False
            if event.type == pygame.MOUSEMOTION:
                if is_pressed:
                    if dist(event.pos, points[-1]) > 20:
                        coord = event.pos
                        pygame.draw.circle(screen, color=RED, center=coord, radius=5)
                        for nearP in near_points(coord):
                            pygame.draw.circle(screen, color=RED, center=nearP, radius=5)
                            points.append(nearP)
                        points.append(coord)
            if event.type == pygame.KEYUP:
                if event.key == 13:
                    count_of_keyup = count_of_keyup + 1
                    if count_of_keyup == 1:
                        pass
                    else:
                        pass

        pygame.display.update()
