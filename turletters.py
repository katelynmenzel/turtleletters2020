import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
	    pass
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	    pass
    elif letter == "F":
	    pass
    elif letter == "G":
	    pass		
    elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
	 tur.setheading(0)
        tur.pd
        tur.right(90)
        tur.fd(50)
        tur.left(90)
        tur.fd (50)
    elif letter == "M":
	tur.setheading(0)
        tur.pd
        tur.right(90)
        tur.fd(50)
        tur.left(180)
        tur.fd(50)
        tur.right(135)
        tur.fd(70)
        tur.left(135)
        tur.fd(50)
        tur.right(135)
        tur.fd(70)
    elif letter == "N":
	tur.setheading(0)
        tur.pd
        tur.right(90)
        tur.fd(50)
        tur.left(180)
        tur.fd(50)
        tur.right(135)
        tur.fd(70)
        tur.left(135)
        tur.fd(50)
        
    
    elif letter == "O":
	tur.setheading(0)
        tur.pd
        tur.fd(50)
        tur.right(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(50)
    elif letter == "P":
	tur.setheading(0)
        tur.pd
        tur.fd(25)
        tur.right(90)
        tur.fd(25)
        tur.right(90)
        tur.fd(25)
        tur.right(90)
        tur.fd(25)
        tur.left(180)
        tur.fd(50)
        tur.left(180)
        tur.fd(50)
        tur.right(90)
        tur.fd(25)		
    elif letter == "Q":
	    pass
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
	    tur.right(45)
	    tur.fd(100)
	    tur.left(90)
	    tur.fd(100)
	    tur.right(45)
	
    elif letter == "W":
	    tur.right(45)
	    tur.fd(100)
	    tur.left(90)
	    tur.fd(50)
	    tur.right(90)
	    tur.fd(50)
	    tur.left(90)
	    tur.fd(100)
	    tur.right(45)
	    
	    
    elif letter == "X":
	    tur.right(45)
	    tur.fd(150)
	    tur.right(135)
	    tur.penup()
	    tur.fd(75)
	    tur.right(135)
	    tur.fd(150)
	    tur.right(45)
	    
	    
    elif letter == "Y":
	    tur.right(45)
	    tur.fd(50)
	    tur.right(45)
	    tur.fd(100)
	    tur.right(180)
	    tur.fd(100)
	    tur.right(45)
	    tur.fd(50)
	    tur.right(45)
	    
    elif letter == "Z":
	    tur.fd(100)
	    tur.right(135)
	    tur.fd(150)
	    tur.left(135)
	    tur.fd(100)
        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        #handles space, punctuation, and anything else
        tur.forward(40)
	
if __name__ == "__main__":
    window = turtle.Screen()
    tur = turtle.Turtle()
    tur.speed(1)
    #turtleLetter("box",tur)
    turtleLetter("A",tur)


    window.exitonclick()
