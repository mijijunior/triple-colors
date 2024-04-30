from turtle import *
import pyautogui
import time
from PIL import Image
import pygame
pygame.mixer.init()
i = Image.open("txt1.gif")
i.resize((460,60)).save("txt1.gif")
wnx, wny = pyautogui.size()
pygame.init()
h=Image.open("txt1.gif")
w,h = h.size
print(w,h)

people = ["beginner.gif","medium.gif","reset.gif","expert.gif","inverted.gif","combat.gif","red.gif","blue.gif","yellow.gif","idk.gif","home1.gif","home2.gif","home3.gif","btn.gif"]

x = 0

b=Image.open("txt2.gif")
w1,h1 = b.size




e = Image.open("red.gif")
e.rotate(0).save("red.gif")



state = "login"

wn = Screen()
wn.bgcolor("black")
wn.setup(wnx, wny)
wn.tracer(60)
poax,poay = pyautogui.position()
poax,poay = 0,0
canvas = wn.getcanvas()



for g in people:
   wn.addshape(g)
def play(loop):
   pygame.mixer.music.load("song.mp3")
   pygame.mixer.music.play(loops=loop)

x1,y1 = 0,-100
draw = Turtle()
draw.pu()
wn.addshape("txt1.gif")
draw.shape("txt1.gif")
draw.color("red")
draw.goto(x1, y1)
x3,y3 = 0,100
x2,y2 = -100,-200

det = Turtle()
det.shape("idk.gif")
det.goto(-wnx/2 + 330,wny/2 - 130)
det.pu()


prof = Turtle()
prof.shape("beginner.gif")
prof.pu()
prof.goto(-wnx/2 + 130,wny/2 - 130)


draw12 = Turtle()
draw12.pu()
draw12.shape("txt1.gif")
draw12.goto(x3, y3)

draw2 = draw.clone()
wn.addshape("txt2.gif")
draw2.shape("txt2.gif")
draw2.goto(x2, y2)

draw3 = draw2.clone()
draw3.goto(100, -200)

draw4 = draw3.clone()
draw4.shape("txt1.gif")
draw4.goto(0,100)

draw5 = draw4.clone()
draw5.goto(0,0)

draw6 = draw5.clone()
draw6.goto(0,-100)

trace = Turtle()
trace.color("red")
trace.shape("square")
trace.pu()
trace.goto(0, 0)
trace.shapesize(0.1, 0.1)

trac = []

p1 = Turtle()
wn.addshape("red.gif")
p1.shape("red.gif")
p1.ht()
p1.pu()
p1.speed(0)
p1.goto(0, 0)
p1.shapesize(2, 2)

clik = trace.clone()
wn.addshape("idk2.gif")
clik.shape("idk2.gif")
clik.ht()
clik.goto(-200, 100)

clik1 = clik.clone()
clik1.st()
clik1.goto(-200, 100)

pen1 = p1.clone()
pen1.ht()
pen1.color("white")
pen1.goto(-70, 130)
pen2 = pen1.clone()
pen2.goto(80, -210)
pen3 = pen2.clone()
pen3.goto(-200, 80)
pen4 = pen3.clone()
pen4.goto(-200,-120)
pen5 = pen4.clone()
pen5.goto(-40,80)

dr = pen5.clone()
dr.shape("home1.gif")
dr.pu()
dr.goto(-wnx/2 - 200,wny/2 + 200)

shop = Turtle()
shop.shape("btn.gif")
shop.pu()
shop.goto(-wnx/2+170,-wny/2+100)

pen6 = pen5.clone()
pen6.goto(-wnx/2 - 200,wny/2 + 200)

writing = False
writing1 = False
txt = ""
txt1 = ""

counter = 0

def fd():
  
  if state == "play":
    trace.goto(p1.xcor(), p1.ycor())
    trace.stamp()
    p1.fd(3)
    dr.fd(6)
    trace.goto(p1.xcor() + 1, p1.ycor() + 1)
    
    trace.stamp()

def lt():
  
  if state == "play":

    p1.lt(45)
    dr.lt(45)
    trace.lt(45)

def rt():
  if state == "play":
    p1.rt(45)
    dr.rt(45)
    trace.rt(45)

def click(x, y):
    global writing, writing1,x1,y1,x2,y2,txt,txt1,state
    
    if state == "login":
     if y > y3 - h /2 and y < y3 + h /2 and x > x3 - (w + 150)/2 and x < x3 + (w + 150)/2:
        writing = True
        writing1 = False
        clik.goto(-200, 100)
        print("hi")
        
     # Check if the click is within the boundaries of draw11if y > y3 - 20 and y < y3 + 20 and x > x3 - w/2 and x < x3 + w/2:
     elif y1 - h/2 < y < y1 + h /2 and x1 - (w + 150)/2 < x < x1 + (w + 150)/2:
        writing1 = True
        writing = False
        print("hij")
        clik.st()
        clik.goto(-200, -100)
     elif y > y2 - h1/2 and y < y2 + h1/2 and x > x2 - w1/2 and x < x2 + w1/2:
      print("hihi")
      
      if txt.strip() != "" and txt1.strip() != "":
        state = "menu"
        with open("triple.txt", "w") as f:
            f.write(f"{txt}:{txt1}")
      else:
        print("Either txt or txt1 is empty or consists only of spaces.")
    elif state == "menu":
      if y > draw4.ycor() - h/2 and y < draw4.ycor() + h/2 and x > draw4.ycor() - (w + 150)/2 and x < draw4.ycor() + (w + 150)/2:
         print("hitgtgt")
         state = "play"
         
       

 

def f(key):
    global writing, txt, writing1, txt1
    if state == "login":
     if writing:
        if key == "BackSpace":
            clik.setx(clik.xcor() - 36)
            txt = txt[:-1] if len(txt) > 0 else txt
        elif key == "Return":
            writing = False
            print("jo")
        elif len(txt) < 23:
            clik.setx(clik.xcor() + 10)
            txt += key

        pen3.clear()
        pen3.write(txt, font=("Akrobat-ExtraBold", 30))
        
     elif writing1:
        if key == "BackSpace":
            txt1 = txt1[:-1] if len(txt1) > 0 else txt1
        elif key == "Return":
            writing1 = False
        elif len(txt1) < 23:
            clik.setx(clik.xcor() + 18)
            txt1 += key
        pen4.clear()
        pen4.write(txt1, font=("Akrobat-ExtraBold", 30))
    

wn.listen()
wn.onclick(click)

for letter in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",".","!","@","$", "_", "BackSpace","Return"]:
 if state == "login":
    wn.onkeypress(lambda x=letter: f(x), letter)

wn.onkeypress(fd, "Up")
wn.onkeypress(lt, "Left")
wn.onkeypress(rt, "Right")

clik_showing = False
play(10000)
def update():
    
    posx, posy = pyautogui.position()

    global counter, clik_showing
    
    if state == "login":
     if writing:
        counter += 1
        if counter % 4 == 0:
            if not clik_showing:
                clik.st()
                clik_showing = True
        else:
            if clik_showing:
                clik.ht()
                clik_showing = False
    if state == "login":
     draw.st()
     draw12.st()
     draw2.st()
     draw3.st()
     clik.st()
     pen1.goto(-70, 130)
     pen1.write("Username", font=("Akrobat-ExtraBold", 30))
     pen1.goto(-70, -50)
     pen1.write("Password", font=("Akrobat-ExtraBold", 30))
     pen1.goto(-200, 250)
     pen1.write("Triple Colors", font=("Akrobat-ExtraBold", 70))
     pen1.goto(-150, -210)
     pen1.write("Register", font=("Akrobat-ExtraBold", 20))
     pen2.write("login", font=("Akrobat-ExtraBold", 20))
    else:
       draw.ht()
       draw12.ht()
       draw2.ht()
       draw3.ht()
       clik.ht()
       pen1.clear()
       pen2.clear()
       pen3.clear()
       pen4.clear()

    if state == "play":
       

       p1.st()
       trace.st()
    else:
       p1.ht()
       trace.ht()
    if state == "menu":
       pen5.goto(-40,80)
       pen5.color("red")
       pen5.write("play",font = ("Akrobat-ExtraBold",30))
       pen5.goto(-40,-20)
       pen5.color("blue")
       pen5.write("training",font = ("Akrobat-ExtraBold",30))
       pen5.goto(-40,-120)
       pen5.color("yellow")
       pen5.write("setting",font = ("Akrobat-ExtraBold",30))
       
       det.st()
       prof.st()
       draw6.st()
       draw5.st()
       draw4.st()
    else:
       det.ht()
       prof.ht()
       draw6.ht()
       draw5.ht()
       draw4.ht()
       pen5.clear()
    wn.update()
    wn.ontimer(update, 1)

update()
wn.mainloop()
