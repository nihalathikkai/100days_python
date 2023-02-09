from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class Car(Turtle):
    def __init__(self, x_pos: int, y_pos):
        super().__init__(shape='square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(COLORS))
        self.penup()
        self.goto(x_pos, y_pos)
        self.setheading(180)


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        for _ in range(randint(10,15)):
            new_car = Car(randint(-300,300),randint(-240,240))
            self.all_cars.append(new_car)
    
    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
            
    def add_car(self):
        new_car = Car(295,randint(-240,240))
        self.all_cars.append(new_car)

    def ckeck_collision(self, y_cor):
        for car in self.all_cars:
            if (car.xcor()-32 < 0 < car.xcor()+20) and (car.ycor()-27 < y_cor < car.ycor()+19):
                return True
            
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT