import random

number = random.randint(1, 10)
Tries = 1


uname = input("Hello, What is your username?\n" )

print("Hello", uname + ".","\n")

question = input("Would you like to play a game [Y/N]\n" )
if question == "n":
	print("Oh...Okay.\n")
if question == "y":
	print("I'm thinking of a number between 1 and 10.\n")
	guess = int(input("Have a guess: "))
	if guess < number:
		print("Guess higher\n")
	if guess > number:
		print("Guess lower\n")
	if guess == number:
		print("You're right, You win! The number was", number, \
			"and it only took", Tries, "tries.")
while guess != number:
	Tries += 1
	guess = int(input("Guess again: "))
	if guess < number:
		print("Guess higher\n")
	if guess > number:
		print("Guess lower\n")
	if guess == number:
		print("You're right, You win! The number was", number, \
			"and it only took", Tries, "tries.")
#delay = input("Press Enter To Play")

#Space Invaders

import turtle
import os

#Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
#Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

#Create player turtle
player = turtle.Turtle()
player.color("white")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

#Side to side
playerspeed = 15

#Create enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed = 2

#Create the player's bullet
#bullet = turtle.Turtle()
#bullet.color("yellow")
#bullet.shape("triangle")
#bullet.penup()
#bullet.speed(0)
#bullet.setheading(90)
#bullet.shapesize(0.5, 0.5)
#bullet.hideturtle()

#bulletspeed = 20

#Define bullet state
#Ready - ready to fire
#Fire - bullet is firing
#bulletstate = "ready"

#Move left and right
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = -280
	player.setx(x)

def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)

#def fire_bullet():
	#Declare bulletstate as global is need changed
#	global bulletstate
#	if bulletstate == "ready":
#		bulletstate = "fire"
#		#Move the bullet to above player
#		x = player.xcor()
#		y = player.ycor()
#		bullet.setposition(x, y + 10)
#		bullet.showturtle()


#Main Game Loop
while True:

	#Move the enemy
#	x = enemy.xcor()
#	x += enemyspeed
#	enemy.setx(x)

	#Move the enemy back and down
#	if enemy.xcor() > 280:
#		y = enemy.ycor()
#		y -= 40
#		enemyspeed *= -1
#		enemy.sety(y)

#	if enemy.xcor() < -280:
#		y = enemy.ycor()
#		y -= 40
#		enemyspeed *= -1
#		enemy.sety(y)

	#Move the bullet
#	if bulletstate == "fire":
#		y = bullet.ycor()
#		y += bulletspeed
#		bullet.sety(y)

	#Check to see if bullet hit top
#	if bullet.ycor() > 275:
#		bullet.hideturtle()
#		bulletstate = "ready"

#Keyboard bindings	
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
#turtle.onkey(fire_bullet, "space")