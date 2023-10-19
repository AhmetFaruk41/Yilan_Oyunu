import turtle
import time
hiz = 0.15

pencere = turtle.Screen()
pencere.title('Yılan Oyunu')
pencere.bgcolor('lightgreen')
pencere.setup(width=600,height=600)
pencere.tracer(0)

kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape('square')
kafa.color('black')
kafa.penup()
kafa.goto(0,100)
kafa.direction='stop'

def move():
    if kafa.direction== 'up':
        y = kafa.ycor()
        kafa.sety(y+20)
    if kafa.direction== 'down':
        y = kafa.ycor()
        kafa.sety(y-20)
    if kafa.direction== 'right':
        x = kafa.xcor()
        kafa.setx(x+20)
    if kafa.direction== 'left':
        x = kafa.xcor()
        kafa.setx(x-20)

def goUp():
    if kafa.direction != 'down':
        kafa.direction= 'up'

def goDown():
    if kafa.direction != 'up':
        kafa.direction= 'down'
def goRight():
    if kafa.direction != 'left':
        kafa.direction= 'right'
def goLeft():
    if kafa.direction != 'right':
        kafa.direction= 'left'


pencere.listen()
pencere.onkey(goUp,'Up')
pencere.onkey(goDown,'down')
pencere.onkey(goRight,'right')
pencere.onkey(goLeft,'left')



while True:
    pencere.update()
    time.sleep(hiz)






