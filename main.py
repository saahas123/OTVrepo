from enes100 import enes100
import time
from Motors import turnLeft, turnRight, move_forward, stop_all
from machine import Pin, time_pulse_us
import Sensors
import math

enes100.begin("TheDropouts", "Material", 522, 1120)

# Confirm connection
while not enes100.is_connected():
    print("Waiting for connection to Vision System...")
    time.sleep(1)

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
        
def navigateStage2():
    l = #middle
    prevRow = #asd
    a = #end
    while(x < l):
        moveUntilObstacle()
        if(checkrow() == 1):
            turnRightTo(90)
            moveUntilRow2()
            turnLeftTo(90)
            prevRow = 1
        else if(checkrow() == 2):
            if(prevRow == 1):
                turnRightTo(90)
                moveUntilRow3()
                turnLeft(90)
            else if(prevRow == 3):
                turnLeftTo(90)
                moveUntilRow1()
                turnRightTo(90)
            else:
                turnLeftTo(90)
                moveUntilRow1()
                turnRightTo(90)
                
        else:
            turnLeftTo(90)
            moveUntilRow2()
            turnRightTo(90)
            prevRow = 3
            
    prevrow = null
    while(x < a):
        moveUntilObstacle()
        if(checkrow() == 1):
            turnRightTo(90)
            moveUntilRow2()
            turnLeftTo(90)
            prevrow = 1
        else if(checkrow() == 2):
            if(prevrow == 1):
                turnRightTo(90)
                moveUntilRow3()
                turnLeftTo(90)
            else if(prevRow == 3):
                turnLeftTo(90)
                moveUntilRow1()
                turnRightTo(90)
            else:
                turnLeftTo(90)
                moveUntilRow1()
                turnRightTo(90)
                
        else:
            turnLeftTo(90)
            moveUntilRow2()
            turnRightTo(90)
            prevrow = 3
        
    
def navigateStage3():
    if(checkLog == false):
        turnLeftTo(90)
        moveUntilLog()
        turnRightTo(90)
        moveEnd()
    else:
        moveEnd()
def moveUntilObstacle():
    while(Sensors.getUltra1 > 0.1 || Sensors.getUltra2>0.1):
        moveforward(40)

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

def turnRightTo(targetTheta, speed=20):
    tolerance = 0.05  # radians (~3 degrees)

    # Normalize target
    targetTheta = normalize_angle(targetTheta)

    # Read current angle
    currentTheta = normalize_angle(enes100.theta)

    while abs(normalize_angle(currentTheta - targetTheta)) > tolerance:
        turnLeft(-speed)  # negative = turn right
        time.sleep(0.05)
        currentTheta = normalize_angle(enes100.theta)

    stopMotors()
    time.sleep(0.05)
def turnLeftTo(targetTheta, speed=20):
    tolerance = 0.05

    targetTheta = normalize_angle(targetTheta)
    currentTheta = normalize_angle(enes100.theta)

    while abs(normalize_angle(currentTheta - targetTheta)) > tolerance:
        turnLeft(speed)
        time.sleep(0.05)
        currentTheta = normalize_angle(enes100.theta)

    stopMotors()
    time.sleep(0.05)



