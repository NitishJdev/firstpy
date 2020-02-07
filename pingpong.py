import turtle
import os

wn=turtle.Screen()
wn.title('first game')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

#score
score_iron=0
score_captain=0

#side1
side_a=turtle.Turtle()
side_a.speed(0)
side_a.shape('square')
side_a.color('red')
side_a.shapesize(stretch_wid=5, stretch_len=1)
side_a.penup()
side_a.goto(-350, 0)
#side2
side_b=turtle.Turtle()
side_b.speed(0)
side_b.shape('square')
side_b.color('blue')
side_b.shapesize(stretch_wid=5, stretch_len=1)
side_b.penup()
side_b.goto(350, 0)
#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('yellow')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = -0.5


#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color('yellow')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Ironman: 0 		Captain: 0', align='center', font=('arial', 24, 'bold'))

#defining function

def side_a_up():
	y = side_a.ycor()
	y += 20
	side_a.sety(y)
def side_a_down():
	y = side_a.ycor()
	y -= 20
	side_a.sety(y)
def side_b_up():
	y = side_b.ycor()
	y += 20
	side_b.sety(y)
def side_b_down():
	y = side_b.ycor()
	y -= 20
	side_b.sety(y)
#keyboard enable
wn.listen()
wn.onkeypress(side_a_up, 'q')
wn.onkeypress(side_a_down, 'w')
wn.onkeypress(side_b_up, 'Up')
wn.onkeypress(side_b_down, 'Down')
#main game loop
while True:
	wn.update()

	#ball movement
	ball.setx(ball.xcor()+ball.dx)
	ball.sety(ball.ycor()+ball.dy)
	#outofline
	if ball.ycor()>290:
		ball.sety(290)
		ball.dy *= -1
		os.system('aplay /home/nitish/Desktop/firstpy4e/Ball_Bounce.wav&')
	if ball.ycor()<-290:
		ball.sety(-290)
		ball.dy *= -1
		os.system('aplay /home/nitish/Desktop/firstpy4e/Ball_Bounce.wav&')
	if ball.xcor()>390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_iron += 1
		pen.clear()
		pen.write('Ironman: {} 		Captain: {}'.format(score_iron, score_captain), align='center', font=('arial', 24, 'bold'))
	if ball.xcor()<-390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_captain += 1
		pen.clear()
		pen.write('Ironman: {} 		Captain: {}'.format(score_iron, score_captain), align='center', font=('arial', 24, 'bold'))
	#side and ball interaction

	if ball.xcor()>330 and ball.xcor()<350 and ball.ycor()<side_b.ycor()+40 and ball.ycor()>side_b.ycor()-40:
		ball.setx(330)
		ball.dx *= -1
		os.system('aplay /home/nitish/Desktop/firstpy4e/Ball_Bounce.wav&')
	if ball.xcor()<-330 and ball.xcor()>-350 and ball.ycor()<side_a.ycor()+40 and ball.ycor()>side_a.ycor()-40:
		ball.setx(-330)
		ball.dx *= -1
		os.system('aplay /home/nitish/Desktop/firstpy4e/Ball_Bounce.wav&')
