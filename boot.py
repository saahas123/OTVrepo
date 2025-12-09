from enes100 import enes100
import time
from Motors import turnLeft, turnRight, move_forward, stop_all
from machine import Pin, time_pulse_us
import Sensors
import math


enes100.begin("TheDropouts", "Material", 247, 1120)

# Confirm connection
while not enes100.is_connected():
    print("Waiting for connection to Vision System...")
    time.sleep(1)

enes100.print("Connected to Vision System!")
print("Connected to Vision System!")





def navigateStage1():
    if(CheckPositionStart() == "top"):
             turnLeftTo(180)
             moveUntilObj()
             completeMission()
             turnLeftTo(90);
             
    else:
        turnLeftTo(360)
        moveUntilObj()
        completeMission()
        turnRightTo(90);
        
    
def navigateStage3():
    if(checkLog == false):
        turnLeftTo(90)
        moveUntilLog()
        turnRightTo(90)
        moveEnd()
    else:
        moveEnd()
def moveUntilObstacle():
    while(Sensors.getUltra1() > 15 or Sensors.getUltra2()>15):
        move_forward(40)
    stop_all()
def move_until_row2UP():
    while(enes100.y != 1.12):
        move_forward(30)
    stop_all()
def move_until_row2DOWN():
    while(enes100.y != 0.82):
        move_forward(30)
    stop_all()
def move_until_row3():
    while(enes100.y != 5):
        move_forward(30)

    stop_all()

def checkRowStart():
    if(enes100.y > .9):
        return 1
    else:
        return 3
    
def checkRow():
    if(enes100.y > 1.52):
        return 1
    elif(enes100.y < 1.52 and enes100.y > 0.42):
        return 2
    else:
        return 3
    

def move_until_row2():
    while abs(enes100.y - 1.0) > 0.05:
        move_forward(40)
        time.sleep(0.1)  # small delay to prevent CPU overload
    stop_all()
def move_until_row1():
    while abs(enes100.y - 1.5) > 0.05:
        move_forward(40)
        time.sleep(0.1)
    stop_all()
def move_until_row3():
    while abs(enes100.y - 0.5) > 0.05:
        move_forward(40)
        time.sleep(0.1)
    stop_all()


def normalize_angle(theta):
    # Keeps angle between -pi and +pi
    return math.atan2(math.sin(theta), math.cos(theta))

def turnRightTo(targetTheta):
    tolerance = 0.07  # radians (~3 degrees)

    # Normalize target
    targetTheta = normalize_angle(targetTheta)

    # Read current angle
    currentTheta = normalize_angle(enes100.theta)

    while abs(normalize_angle(currentTheta - targetTheta)) > tolerance:
        turnRight(30)  # negative = turn right
        time.sleep(0.05)
        currentTheta = normalize_angle(enes100.theta)

    stop_all()
    time.sleep(0.05)
def turnLeftTo(targetTheta):
    tolerance = 0.07

    targetTheta = normalize_angle(targetTheta)
    currentTheta = normalize_angle(enes100.theta)
    turnLeft(30)

    while abs(normalize_angle(currentTheta - targetTheta)) > tolerance:
        time.sleep(0.05)
        currentTheta = normalize_angle(enes100.theta)
    

    stop_all()
    time.sleep(0.05)
    
def navigateStage2():
    l = 1.68     
    a = 2.85      
    prevRow = None

    # -----------------------------
    # PART 1: Move until reaching x < l
    # -----------------------------
    row = checkRowStart()
    
    while enes100.x < l:
        moveUntilObstacle()

        
        enes100.print("starting nav")

        if row == 1:
            turnRightTo(90)
            move_until_row2UP()
            turnLeftTo(0)
            prevRow = 1
            enes100.print("turn to 2")
            row = 2
        elif row == 2:
            if prevRow == 1:
                turnRightTo(90)
                move_until_row3()
                turnLeftTo(0)
                row = 3
                enes100.print("starting turn")


            elif prevRow == 3:
                turnLeftTo(270)
                move_until_row1()
                turnRightTo(0)
                row = 1
                enes100.print(" turn to 1")


            else:
                turnLeftTo(270)
                move_until_row1()
                turnRightTo(0)
                row = 1
                enes100.print("starting turn 1")


        else:  # row == 3
            turnLeftTo(270)
            move_until_row2DOWN()
            turnRightTo(0)
            prevRow = 3
            row = 2
            enes100.print("starting 2")



    # -----------------------------
    # PART 2: Move until x < a
    # -----------------------------
    prevRow = None
    enes100.print("part 2")

    while enes100.x < a:
        moveUntilObstacle()


        if row == 1:
            turnRightTo(90)
            move_until_row2UP()
            turnLeftTo(0)
            prevRow = 1

        elif row == 2:
            if prevRow == 1:
                turnRightTo(90)
                move_until_row3()
                turnLeftTo(0)

            elif prevRow == 3:
                turnLeftTo(270)
                move_until_row1()
                turnRightTo(0)

            else:
                turnLeftTo(270)
                move_until_row1()
                turnRightTo(0)

        else:  # row == 3
            turnLeftTo(270)
            move_until_row2DOWN()
            turnRightTo(0)
            prevRow = 3

        
    
enes100.print("starting turn")
navigateStage2()
