from turtle import *
from PIL import Image
import math
import pyautogui
from tkinter import filedialog
#320 50
wnx, wny = pyautogui.size()

happenin = "nothing"

v = Image.open("txxt.gif")
v.resize((440, 400)).save("txxt.gif")
v = Image.open("txt1.gif")
v.resize((260, 40)).save("txt1.gif")
v = Image.open("txt1.gif")
v.resize((120, 40)).save("txt2.gif")

wn = Screen()
wn.title("mogs playground")
wn.setup(wnx, wny)
wn.bgcolor("black")
wn._root.overrideredirect(10)
wn.tracer(60)

can = wn.getcanvas()

can.config(bd = 0)

class Pen(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.pu()
        self.color(color)
        self.hideturtle()
        self.goto(x, y)

    def draw(self, text, font):
        self.write(text,font = font)

class Platform(Turtle):
    def __init__(self, x, y, image,write):
        super().__init__()
        self.x = x
        self.y = y

        self.image = image
        self.write1 = write
        self.up()
        self.goto(x, y)
        wn.addshape(image)
        self.shape(image)
        self.dx = 0
        self.dy = 0

platforms = []

pen1 = Pen(-60,380,"white")
pen2 = Pen(650 - 30,75,"white")
add1 = Platform(600,400,"add.gif","")
search = Platform(-200,400,"search.gif","")
txtbox = Platform(0,400,"txt.gif","")
idk = Platform(0,400,"idk.gif","")
ask = Platform(500,150,"txxt.gif","")
txt1 = Platform(420,200,"txt1.gif","")
fold = Platform(650,200,"folder.gif","")
txt2 = Platform(650,90,"txt2.gif","")
found = False

idc = "idk"

click1 = 0
idk = ""
txt7 = ""
addin = [ask,txt1]
def click(x, y):
    global happenin,click1,found,idk,idc
    
    if click1 %2 == 0:
     if add1.y - 50/2 <= y <= add1.y + 50/2 and add1.x - 120/2 <= x <= add1.x + 120/2:
        happenin = "add"
        print(happenin)
        click1 += 1
    else:
       if add1.y - 50/2 <= y <= add1.y + 50/2 and add1.x - 120/2 <= x <= add1.x + 120/2: 
        happenin = "nothing"
        click1 += 1
    if txt1.y - 460/2 <= y <= txt1.y + 460/2 and txt1.x - 40/2 <= x <= txt1.x + 40/2:
       
       oi = filedialog.askdirectory()
       idk += oi
       found = True
    elif txt2.y - 40/2 <= y <= txt2.y + 40/2 and txt2.x - 120/2 <= x <= txt2.x + 120/2:
       pen2.clear()
       pen2.goto(650 - 30,75)
       pen2.draw("",("Akrobat-ExtraBold",20))
       idc = "write"
    
def f(key):
   global txt7,idc,happenin,il1
   if happenin == "add":
     if idc == "write":
      txt7 += key
      pen2.clear()
      pen2.goto(650 - il1*4,75)
      pen2.draw(txt7,("Akrobat-ExtraBold",int(20/il1)))
      print("what")

cant = "ni"

wn.listen()
for letter in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
   wn.onkeypress(lambda x = letter:f(x),letter)
wn.onclick(click)
while True:
    c = idk.split("/")
  
    il = len(idk)
    il1 = len(txt7)
    for add in addin:
        if happenin == "add":
            add.showturtle()
            pen1.goto(300,250)
            pen1.draw("folder/directory",("Akrobat-ExtraBold",20))
            if found:
             pen1.goto(420-il*4,190)
             pen1.draw(idk,("Akrobat-ExtraBold",int(20/il)))
            if idc == "idk":
             if il1 > 0:
              pen2.goto(650 - il1*4,75)
              pen2.draw(c[-1],("Akrobat-ExtraBold",int(20/il1 + 1)))
        else:
            pen1.clear()
            add.hideturtle()
    pen1.goto(-60,380)
    pen1.draw("search",("Akrobat-ExtraBold",30))
    pen1.pu()
    pen1.goto(600,385)
    pen1.draw("Add",("Akrobat-ExtraBold",20))
    

    wn.update()
