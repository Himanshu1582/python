from turtle import*
colour=["red","blue","green","yellow""grey"]
def circle1(lenght,colour):
    speed(0)
    for i in range(36):
        color(colour)
        circle(lenght)
        rt(10)


up()
goto(100,0)
down()

circle1(35)
up()
goto(0,-100)
down()

circle1(36)

up()
goto(-100,0)
down()

circle1(37)

up()
goto(0,100)
down()

circle1(38)

up()
goto(0,0)
down()

circle1(39)
