from turtle import*
import random
import math




sc=Screen()
sc.bgcolor("cyan")
sc.title("Space Invador Game")
sc.setup(1000,600)

gun=Turtle()
gun.up()
gun.goto(0,-250)
gun.shapesize(5)
gun.color("red")
gun.setheading(90)

bl=Turtle()
bl.up()
bl.goto(0,-245)
bl.color("blue")
bl.shape("circle")
bl.shapesize(.5)


bd=Turtle()
bd.up()
bd.goto(-500,-240)
bd.down()
bd.fd(1000)
bd.hideturtle()

num_of_enemies=5

enemyspeed = 2

enemies=[]

bulletspeed=50
bulletstate="ready"

for enimy in range(num_of_enemies):
    enemies.append(Turtle())

for e in enemies:
    e.speed(0)
    e.up()
    e.goto(random.randint(-250,200),random.randint(100,250))
    e.down()
    e.shape("square")
    e.shapesize(1)

def left():
    x=gun.xcor()
    x=x-10
    gun.setx(x)

    if gun.xcor()<-300:
        gun.setx(0)
def right():
    x=gun.xcor()
    x=x+10
    gun.setx(x)
    if gun.xcor()>300:
        gun.setx(0)

def shoot():
    global bulletstate
    
    if bulletstate == "ready":
        bulletstate="fire"
        y=bl.ycor()
        y=y+10
        bl.sety(y)
    # if bl.ycor()>270:
    #     bl.goto(0,-240)
def collision (x1,x2):
    distance=math.sqrt(math.pow(x1.xcor(),-x2.xcor(),2)+math.pow(x1.ycor()-x2.ycor(),2))

sc.listen()
sc.onkeypress(left,"Left")
sc.onkeypress(right,"Right")
sc.onkeypress(shoot,"space")

while True:
    sc.update()
    for e in enemies:
        x=e.xcor()
        x=x+enemyspeed
    
        if e.xcor()<-300:
            for i in enemies:
                y=i.ycor()
                y=y-20
                i.sety(y)

                enemyspeed *= -1

        if e.xcor()>300:
            for i in enemies:
                y=i.ycor()
                y=y-20
                i.sety(y)   

                enemyspeed *= -1



sc.mainloop()