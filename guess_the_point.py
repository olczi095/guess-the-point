from random import randint
import turtle
from time import sleep


def game():
    """The game of searching point.

    Rules:
    1. At first the program shows coordinates of the rectangle to the user (they are randomly selected),
    then the user has to guess the point from inside the rectangle by enter the coordinates of the point.
    2. The coordinates of the points can be randomized (and guessing) from the range -200:200.
    """

    random_rectangle = Rectangle()
    print("Welcome to the game! Your task is to choose the point that falls in the rectangle.")
    print(f"The coordinates of our rectangle are: {random_rectangle.show_both_points()}\n")
    coordinate_x = Coordinate.validation('first')
    coordinate_y = Coordinate.validation('second')
    random_rectangle.draw_rectangle_and_point(coordinate_x, coordinate_y)
    user_game = Game((coordinate_x, coordinate_y))
    print("\n")
    print(user_game.check_the_point(random_rectangle.show_both_points()))


class Coordinate:

    @staticmethod
    def validation(number_of_coordinate_in_string):
        while True:
            coordinate = input(f"Type {number_of_coordinate_in_string} coordinate from the scope -200:200: ")
            if coordinate.isdigit():
                return int(coordinate)
            else:
                print("You type incorrect value!")


class Rectangle:
    # class for choose two random points of the rectangle

    def __init__(self):
        self.point1 = randint(-200, 200), randint(-200, 200)
        self.point2 = self.setting_point2()

    def setting_point2(self):
        point2_x = randint(-200, 200)
        point2_y = randint(-200, 200)
        while point2_x == self.point1[0]:
            point2_x = randint(-200, 200)
        while point2_y == self.point1[1]:
            point2_y = randint(-200, 200)
        point2 = point2_x, point2_y
        return point2

    def show_both_points(self):
        return self.point1, self.point2

    def draw_rectangle_and_point(self, user_point_x, user_point_y):
        screen = turtle.Screen()
        screen.setup(500, 500)
        screen.title('RECTANGLE')
        t = turtle.Turtle()
        t.hideturtle()
        t.up()
        t.pensize(3)
        point1 = self.point1[0], self.point1[1]
        point2 = self.point2[0], self.point2[1]
        t.goto(point1[0], point1[1])
        t.down()
        t.goto(point2[0], point1[1])
        t.goto(point2[0], point2[1])
        t.goto(point1[0], point2[1])
        t.goto(point1[0], point1[1])
        t.up()
        t.goto(user_point_x, user_point_y)
        t.dot(7, "red")

        sleep(5)


class Game:
    # check if the user's point falls in the selected rectangle, return True or False

    def __init__(self, user_point):  # user_point -> tuple
        self.user_point = user_point

    def check_the_point(self, points):
        point1 = points[0]
        point2 = points[1]
        scope_x = min(point1[0], point2[0]), max(point1[0], point2[0])
        scope_y = min(point1[1], point2[1]), max(point1[1], point2[1])

        if scope_x[0] < self.user_point[0] < scope_x[1] and scope_y[0] < self.user_point[1] < scope_y[1]:
            return True
        else:
            return False


if __name__ == '__main__':
    game()
