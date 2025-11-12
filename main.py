from enes100 import enes100
import time
from Motors import turnLeft, turnRight, move_forward, stop_all
from machine import Pin, time_pulse_us
import Sensors


enes100.begin("TheDropouts", "Material", 522, 1120)

# Confirm connection
while not enes100.is_connected():
    print("Waiting for connection to Vision System...")
    time.sleep(1)

print("Connected to Vision System!")

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
        
def navigateStage2():
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
        
    
def navigateStage3():
    if(checkLog == false):
        turnLeft(90)
        moveUntilLog()
        turnRight(90)
        moveEnd()
    else:
        moveEnd()
def moveUntilObstacle():
    while(Sensors.getUltra1 > 0.1 || Sensors.getUltra2>0.1):
        moveforward()

    stop_all()

def checkRow():
    if(enes100.y > 1.2):
        return 1;
    else if(enes100.y < 1.2 && enes100.y > 0.65):
        return 2;
    else:
        return 3;
    

def move_until_row2():
    while abs(enes100.y - 1.0) > 0.05:
        move_forward()
        time.sleep(0.1)  # small delay to prevent CPU overload
    stop_all()
def move_until_row1():
    while abs(enes100.y - 1.5) > 0.05:
        move_forward()
        time.sleep(0.1)
    stop_all()
def move_until_row3():
    while abs(enes100.y - 0.5) > 0.05:
        move_forward()
        time.sleep(0.1)
    stop_all()


