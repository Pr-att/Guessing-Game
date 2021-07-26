import turtle
import pandas
import time
from writer import New
screen = turtle.Screen()
screen.setup(width=725, height=491)
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
t1 = New()
t2 = New()
answer_state_list = []
new_list = []
score = 0
screen.tracer(0)
data = pandas.read_csv('50_states.csv')
end_game = False
state_name = data['state']
new_data = state_name.to_list()
while not end_game:
    time.sleep(0.01)
    screen.update()
    answer_state = screen.textinput(title=f"Guess the state  "
                                          f"{score}/50", prompt="What's another state name?").title()
    if answer_state == 'Exit':
        new_list = [n for n in new_data if n not in answer_state_list]
        remaining_states = pandas.DataFrame(new_list)
        file = remaining_states.to_csv('unknown_states.csv')
        for k in new_list:
            new_ans = data[data['state'] == k]
            x_co = int(new_ans['x'])
            y_co = int(new_ans['y'])
            t2.color('red')
            t2.penup()
            t2.goto(x_co, y_co)
            t2.pendown()
            t2.write(k, font=('Times Nww Roman', 7, 'bold'))
            t2.hideturtle()
        end_game = True
    if answer_state in new_data:
        answer_state_list.append(answer_state)
        score += 1
        ans = data[data['state'] == answer_state]
        x_co = int(ans['x'])
        y_co = int(ans['y'])
        t1.penup()
        t1.goto(x_co, y_co)
        t1.pendown()
        t1.write(answer_state, font=('Times Nww Roman', 7, 'bold'))
        t1.hideturtle()
    if score > 49:
       end_game = True

turtle.mainloop()
