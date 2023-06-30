from turtle import*

def circle1():
    speed(0)
    for i in range(36):
        circle(35)
        rt(10)


up()
goto(100,0)
down()

circle1()

up()
goto(0,-100)
down()

circle1()

up()
goto(-100,0)
down()

circle1()

up()
goto(0,100)
down()

circle1()

up()
goto(0,0)
down()

circle1()
