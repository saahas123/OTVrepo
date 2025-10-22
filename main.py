ultrasonic1 = #sdasd
ultrasonic2 = #asd
x,y = #global
def navigateStage1():
    if(CheckPositionStart() == "top"):
             turnLeft(180)
             moveUntilObj()
             completeMission()
             turnLeft(90);
             
    else:
        turnLeft(360)
        moveUntilObj()
        completeMission()
        turnRight(90);
        
def navigateStage2:
    l = #middle
    prevRow = #asd
    a = #end
    while(x < l):
        moveUntilObstacle()
        if(checkrow() == 1):
            turnright(90)
            moveUntilRow2()
            turnLeft(90)
            prevRow = 1
        else if(checkrow() == 2):
            if(prevRow == 1):
                turnright(90)
                moveUntilRow3()
                turnLeft(90)
            else if(prevRow == 3):
                turnLeft(90)
                moveUntilRow1()
                turnRight(90)
            else:
                turnLeft(90)
                moveUntilRow1()
                turnRight(90)
                
        else:
            turnLeft(90)
            moveUntilRow2()
            turnRight(90)
            prevRow = 3
            
    prevrow = null
    while(x < a):
        moveUntilObstacle()
        if(checkrow() == 1):
            turnright(90)
            moveUntilRow2()
            turnLeft(90)
            prevrow = 1
        else if(checkrow() == 2):
            if(prevrow == 1):
                turnright(90)
                moveUntilRow3()
                turnLeft(90)
            else if(prevRow == 3):
                turnLeft(90)
                moveUntilRow1()
                turnRight(90)
            else:
                turnLeft(90)
                moveUntilRow1()
                turnRight(90)
                
        else:
            turnLeft(90)
            moveUntilRow2()
            turnRight(90)
            prevrow = 3
        
    
def navigateStage3:
    if(checkLog == false):
        turnLeft(90)
        moveUntilLog()
        turnRight(90)
        moveEnd()
    else:
        moveEnd()
def moveUntilObstacle:
    while(ultrasonic1 > 10 || ultrasonic2>10):
        moveforward()