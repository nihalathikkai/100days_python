from turtle import Turtle, Screen
import pandas as pd
from time import sleep

# BACKGROUND_PICTURE = "D:\\python\\100days\\day25_intermediate_pandas\\blank_states_img.gif"
# STATE_LIST = "D:\\python\\100days\\day25_intermediate_pandas\\50_states.csv"
BACKGROUND_PICTURE = "D:\\python\\100days\\day25_intermediate_pandas\\india-state.gif"
STATE_LIST = "D:\\python\\100days\\day25_intermediate_pandas\\india_states.csv"


window = Screen()
# window.setup(width=725, height=491)
window.setup(width=410, height=467)
window.title("India States Game")
window.bgpic(BACKGROUND_PICTURE)

# window.addshape(BACKGROUND_PICTURE)
# tr = Turtle(shape=BACKGROUND_PICTURE)

# def get_mouse_click(x,y):
#     print(x,y)
# window.onscreenclick(get_mouse_click)
tr = Turtle()
tr.hideturtle()
tr.penup()

state_data = pd.read_csv(STATE_LIST)
answer = window.textinput("Guess a State","Enter a State's Name").strip()
counter = 0
while answer:
    answer = answer.title()
    state = state_data[state_data.state == answer]
    if not state.empty:
        counter += 1
        tr.goto(int(state.x), int(state.y))
        tr.write(answer)
    answer = window.textinput(f"{counter}/29 Correct","Enter a State's Name")

window.mainloop()
# window.exitonclick()