from turtle import*
import datetime
import time

sc=Screen()
sc.bgcolor("cyan")
sc.title("Digital watch")
sc.setup(1000,600)

box=Turtle()
box.hideturtle()

digitalWatch=Turtle()
digitalWatch.hideturtle()
digitalWatch.up()
digitalWatch.goto(-20,40)
digitalWatch.down()

def rect_box():
    box.up()
    box.goto(-10,30)
    box.down()
    for i in range(2):
        box.fd(70)
        box.rt(90)
        box.fd(50)
        box.rt(90)

clock=Turtle()
clock.hideturtle()
clock.up()
clock.goto(0,0)
clock.down()
clock.color("black")

hr=datetime.datetime.now().hour
mint=datetime.datetime.now().minute
sec=datetime.datetime.now().second

while True:
    clock.clear()
    tm=(str(hr).zfill(2)+":"+str(hr).zfill(2)+":"+str(sec).zfill(2))
    clock.write(tm,font=("arial",10,"bold"))
    time.sleep(1)

    sec=sec+1

    if sec>59:
        sec=0
        mint=mint+1

    if mint>59:
        mint=0
        hr=hr+1
    
    if hr>23:
        hr=0
    digitalWatch.write("DigitalWatch",font=("arial",10,"bold"))
    rect_box()









