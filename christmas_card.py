import turtle
t=turtle.Turtle()
t.speed(50) # makes the turtle draw faster


# this portion of code creates the black background color
def background_color(side_lenght):
  t.penup()
  t.goto(-400,400)
  t.fillcolor("Black")  
  t.pendown()
  t.begin_fill()
 
  for side_lenght in range(4):
    t.forward(800)
    t.right(90)
  t.end_fill()

background_color(4)

#this piece of code creates the snow
import time
import random 
snow_list=[]
def snow_flake(radius):
  x= random.randrange(-400,400) # this randomly pics the positon of the x aixs
  y=random.randrange(-400,400)# this randomlly pics the position of the y axis
  snow_list.append([x, y])
  t.pencolor("white")
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.fillcolor("white")
  t.begin_fill()
  t.circle(radius)
  t.end_fill()

 # this daws the snow until there is more than 300 snow flakes
while len(snow_list)<300 :
   for i in range(150):
       snow_flake(5)
    
# this portion of code create the shape of the diamonds
def diamond_shape(side_lenght):
  t.setheading(60)
  t.fillcolor("green")
  t.begin_fill()
  t.forward(side_lenght)
  t.setheading(-60)
  t.forward(side_lenght)
  t.right(60)
  t.forward(side_lenght)
  t.right(120)
  t.forward(side_lenght)
  t.setheading(0)
  t.end_fill()
  t.penup()
  t.forward(side_lenght)
  t.pendown()

t.penup()
t.goto(-100,-100)
t.pendown()
diamonds=0

# this portion of code creates the christmas tree
xcor=-100
ycor=-100

list=[8,15,21,26,30,33,35] # this is the list so that every time there is one less diamond in the tree

while diamonds < 36:
  diamond_shape(20)
  diamonds=diamonds+1
  for item in list:
    if diamonds== item:
      t.penup()
      t.goto(xcor+10,ycor+20)
      t.pendown()
      xcor=xcor+10
      ycor=ycor+20
# this writtes merry christmas on top of the drawings in the color pink
t.penup()
t.pencolor("Pink")
t.goto(0,200)
t.pendown()
message= "Merry Christmas :)"
t.write(message, move=False, align="center", font=("Arial",35,"bold"))

# this portion of code creates the  shape of a star 

def star(star_lenght):
  t.fillcolor("yellow")
  t.pencolor("yellow")
  t.forward(star_lenght)
  t.right(144)

# this piece of code draws the star on top of the tree
t.penup()
t.goto(-35,70)
t.pendown()
t.begin_fill()
for i in range(5):
  star(30)
t.end_fill()

# this piece of code creates the decoration of boxes in the tree

def square(side_lenght):
  t.begin_fill()
  for i in range(4):
    t.forward(side_lenght)
    t.right(90)
  t.end_fill()

def rectangle(side_lenght):
  t.begin_fill()
  for i in range(2):
    t.forward(60)
    t.right(90)
    t.forward(side_lenght)
    t.right(90)
  t.end_fill()

  # this creates the tree trunk
def tree_trunk():
  t.penup()
  t.goto(-50,-100)
  t.fillcolor("brown")
  t.pencolor("brown")
  t.pendown()
  rectangle(45)

tree_trunk()
boxes=0
t.penup()
xcor=-100
ycor=-100
t.goto(xcor,ycor)
t.pencolor("yellow")
t.fillcolor("red")
t.pendown()
while boxes<8:
  square(20)
  t.penup()
  t.forward(20)
  t.pendown()
  boxes=boxes+1



#this will create the ornaments

xcor= -90
ycor= -90

ornaments=0



list_2=[8,15,21,26,30,33]
list_colors=["pink", "yellow","red","blue","gray","purple","orange","white","brown","pink", "yellow","red","blue","gray","purple","orange","white","brown","pink", "yellow","red","blue","gray","purple","orange","white","brown","pink", "yellow","red","blue","gray","purple","orange","white","brown"]
t.penup()
t.goto(xcor,ycor)
t.pendown() 

def ornament_shape(radius):
  t.begin_fill()
  t.circle(radius)
  t.end_fill()
  t.penup()
  t.forward(20)
  t.pendown()

# this puts the ornaments in the tree
while ornaments < 35:
  color_of_ornaments= random.choice(list_colors)# this makes random colors appear for the ornaments, it pciks color from the list of colors
  list_colors.remove(color_of_ornaments)
  t.fillcolor(color_of_ornaments)
  ornament_shape(5)
  ornaments= ornaments +1
  for item in list_2:
    if ornaments == item:
      t.penup()
      t.goto(xcor+10,ycor+20)
      t.pendown()
      xcor=xcor+10
      ycor=ycor+20

# this allows for the user to type a message in and for the message to appear on the screen
your_message=input("What message do you want to put inside your christmas card?, 10 words/less")

t.penup()
t.pencolor("Pink")
t.goto(-20,-240)
t.pendown()
message= your_message
t.write(message, move=False, align="center", font=("Arial",20,"bold"))

# this will create a snowman on the side of the christmas tree
xcor= -200
ycor=-150
#snowman body

rad=40
def snow_man_body():
  t.penup()
  t.pencolor("Black")
  t.fillcolor("White")
  t.goto(xcor,ycor)
  t.pendown()
  t.circle(rad)
  
  
for i in range(3):
  t.begin_fill()
  snow_man_body()
  t.end_fill()
  t.penup()
  ycor=ycor+40
  t.goto(xcor,ycor)
  rad=rad-10

#eyes of snowman

xcor=-208
ycor=-50
t.penup()
t.goto(xcor,ycor)

def eyes():
  t.fillcolor("black")
  t.pendown()
  t.circle(3)
  t.penup()
  t.forward(15)
  t.pendown()

for i in range(2):
  t.begin_fill()
  eyes()
  t.end_fill()

# snowman buttons

ycor=-120
xcor=-203
t.penup()
t.goto(xcor,ycor)
t.pendown()
  

for i in range(5):
  t.pendown()
  t.begin_fill()
  t.circle(3)
  t.end_fill()
  t.penup()
  t.goto(xcor,ycor+10)
  ycor=ycor+10


# left arm of snowman
t.penup()
t.goto(xcor+40,ycor-20)
t.left(45)
t.pendown()
t.pencolor("brown")
t.fillcolor("brown")
t.begin_fill()
t.forward(25)
t.right(90)
t.forward(5)
t.right(90)
t.forward(35)
t.end_fill()

xcor=-240
#right arm
t.penup()
t.goto(xcor,ycor-30)
t.right(90)
t.pendown()
t.fillcolor("brown")
t.pencolor("brown")
t.begin_fill()
t.forward(25)
t.right(90)
t.forward(5)
t.right(90)
t.forward(35)
t.end_fill()
 # the 2nd snowman
xcor= 130
ycor=-150
rad=40
#snowman body

def snow_man_body_2():
  t.penup()
  t.pencolor("Black")
  t.fillcolor("White")
  t.goto(xcor,ycor)
  t.pendown()
  t.circle(rad)
  
  
for i in range(3):
  t.begin_fill()
  snow_man_body_2()
  t.end_fill()
  t.penup()
  ycor=ycor+40
  xcor=xcor+5
  t.goto(xcor,ycor)
  rad=rad-10

#eyes of snowman

xcor=148
ycor=-58
t.penup()
t.fillcolor("black")
t.goto(xcor,ycor)
t.setheading(0)
for i in range(2):
  t.begin_fill()
  eyes()
  t.end_fill()

# snowman buttons


ycor=-125
xcor=155
t.penup()
t.goto(xcor,ycor)
t.pendown()
  
t.fillcolor("black")
for i in range(5):
  t.pendown()
  t.begin_fill()
  t.circle(3)
  t.end_fill()
  t.penup()
  t.goto(xcor,ycor+10)
  ycor=ycor+10

xcor=180
ycor=-70
t.setheading(-60)
# left arm of snowman
t.penup()
t.goto(xcor+40,ycor-20)
t.right(90)
t.pendown()
t.pencolor("brown")
t.fillcolor("brown")
t.begin_fill()
t.forward(30)
t.right(90)
t.forward(5)
t.right(90)
t.forward(35)
t.end_fill()

xcor=105
ycor=-60
#right arm
t.penup()
t.goto(xcor,ycor-30)
t.pendown()
t.pencolor("brown")
t.setheading(-45)
t.begin_fill()
t.forward(25)
t.right(90)
t.forward(5)
t.right(90)
t.forward(35)
t.end_fill()
 # dont touch, this allows for you to see the art
wn = turtle.Screen()
wn.mainloop()
