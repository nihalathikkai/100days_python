from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
RIGHT, UP, LEFT, DOWN = (0, 90, 180, 270)

class Segment(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.color('white')
        self.penup()

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] 
        
    def create_snake(self):
        for pos in STARTING_POSITIONS:
            new_segment = Segment()
            new_segment.goto(pos)
            self.segments.append(new_segment)
            
    def add_segment(self):
        new_segment = Segment()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)
        
    def get_positions(self):
        return [segment.position() for segment in self.segments]
        
    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            new_pos = self.segments[i-1].position()
            self.segments[i].goto(new_pos)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)