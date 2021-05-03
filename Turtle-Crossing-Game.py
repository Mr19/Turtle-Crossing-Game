import time
from turtle import Screen, Turtle
import random

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("Courier", 24, "normal")
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.left(90)
        self.start_position()

    def start_position(self):
        self.goto(STARTING_POSITION)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        return self.ycor() > FINISH_LINE_Y


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-230, 260)
        self.color("black")
        self.hideturtle()
        self.level = 1
        self.display_update()

    def display_update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_update(self):
        self.level += 1
        self.display_update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        choice = random.randint(1, 6)
        if choice == 3:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            y_cor = random.randint(-250, 250)
            car.goto(300, y_cor)
            self.cars.append(car)

    def car_move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def next_level(self):
        self.car_speed += MOVE_INCREMENT


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    score = Scoreboard()
    car_object = CarManager()

    screen.listen()
    screen.onkey(player.move_forward, "Up")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_object.create_car()
        car_object.car_move()

        # Collision detection with the car and the player
        for car in car_object.cars:
            if car.distance(player) < 20:
                game_is_on = False
                score.game_over()

        # Player level up. Successful completion.
        if player.finish_line():
            player.start_position()
            car_object.next_level()
            score.level_update()

    screen.exitonclick()


if __name__ == '__main__':
    main()
