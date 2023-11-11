import pygame
import numpy as np
import random
from sklearn import svm
import matplotlib.pyplot as plt


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


def create_straight():
    svm_algorithm.fit(points, classes_of_points)

    w = svm_algorithm.coef_[0]

    a = -w[0] / w[1]
    xx = np.linspace(0, 1000, 1500)
    yy = (a * xx - svm_algorithm.intercept_[0] / w[1])
    pygame.draw.line(screen, (0, 0, 0), (xx[0], yy[0]), (xx[len(xx) - 1], yy[len(yy) - 1]), 2)


def compare_with_straight(new_point):
    w = svm_algorithm.coef_[0]
    a = -w[0] / w[1]
    b = -svm_algorithm.intercept_[0] / w[1]

    x_0 = new_point[0]
    y_0 = HEIGHT - new_point[1]

    y_predicted = HEIGHT - (a * x_0 + b)

    if y_0 > y_predicted:
        return 1
    else:
        return -1


def determine_class():
    point = points[0]
    if compare_with_straight_result == compare_with_straight(point) and classes_of_points[0] == 1:
        return 1
    if compare_with_straight_result == compare_with_straight(point) and classes_of_points[0] == 2:
        return 2
    if compare_with_straight_result != compare_with_straight(point) and classes_of_points[0] == 1:
        return 2
    if compare_with_straight_result != compare_with_straight(point) and classes_of_points[0] == 2:
        return 1


if __name__ == '__main__':
    HEIGHT = 400
    RED = 'red'
    BLUE = 'blue'
    pygame.init()
    screen = pygame.display.set_mode((600, HEIGHT))
    screen.fill(color="#FFFFFF")
    pygame.display.update()
    is_active = True
    is_pressed = False
    points = []
    classes_of_points = []
    count_of_keyup = 0
    svm_algorithm = svm.SVC(kernel='linear')
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
                    classes_of_points.append(1)
                    pygame.draw.circle(screen, color=RED, center=coord, radius=5)
                if event.button == 3:
                    is_pressed = True
                    coord = event.pos
                    points.append(coord)
                    classes_of_points.append(2)
                    pygame.draw.circle(screen, color=BLUE, center=coord, radius=5)
                if event.button == 2:
                    is_pressed = True
                    coord = event.pos
                    points.append(coord)
                    compare_with_straight_result = compare_with_straight(coord)
                    determined_class = determine_class()
                    classes_of_points.append(determined_class)
                    pygame.draw.circle(screen, color='black', center=coord, radius=5)
            if event.type == pygame.MOUSEBUTTONUP:
                is_pressed = False
            if event.type == pygame.KEYUP:
                if event.key == 13:
                    count_of_keyup = count_of_keyup + 1
                    if count_of_keyup == 1:
                        create_straight()
                    else:
                        pass

        pygame.display.update()
