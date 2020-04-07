import random
import turtle
num_turtles=5
turtles=[]
turtle.colormode(1)
for i in range(num_turtles):
	new_turtle=turtle.Pen()
	new_turtle.pencolor(random.random(),random.random(), random.random())
	turtles.append(new_turtle)
	
def move(tur):
	print('turtle 0')	
	tur.backward(100)
	tur.left(130)
	tur.forward(200)
	tur.right(100)

def move_opposite(ter):
	ter.forward(100)
	ter.right(130)
	ter.backward(200)
	ter.left(100)
	
def forwrd (tor):
	tor.left(90)
	tor.forward(180) 
	
move(turtles[0])
move(turtles[1])
move_opposite(turtles[2])
move_opposite(turtles[4])
forwrd(turtles[3])
