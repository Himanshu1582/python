from turtle import*
import random

sc=Screen()
sc.bgcolor("black")
sc.title("good night theme")
sc.setup(1000,600)

moon=Turtle()
moon.speed(0)
moon.hideturtle()

star=Turtle()
star.speed(0)
star.hideturtle()

text=Turtle()
text.hideturtle()
count=0

def moon_func(pos,colour,mooncolor):
    x,y=pos
    moon.color(colour)
    moon.up()
    moon.goto(x,y)
    moon.down()
    moon.begin_fill()
    moon.circle(50)
    moon.fillcolor(mooncolor)
    moon.end_fill()

moon_func((-300,200),"white","white") 
moon_func((-270,220),"black","black")

def star_func(pos,length,colours):
    global count
    x,y=pos
    star.up()
    star.goto(x,y)
    star.down()
    star.color(colours)
    star.begin_fill()
    for i in range(5):
        star.fd(length)
        star.rt(144)
        star.fd(length)
    star.end_fill()
    count=count+1
    text.up()
    text.goto(310,-190)
    text.down()
    text.color(colour)
    text.write("Good night",font=("arial",10,"bold"))

colours=["red","blue","green","yellow","grey"]

def random_pos():
    return(random.randint(-300,300),random.randint(-250,250))
def random_length():
    return(random.randint(10,25))





while True:
    sc.update()
    colour=random.choice(colours)
    pos=random_pos()
    length=random_length()
    star_func(pos,length,colour)
    


sc.mainloop()
    
    


