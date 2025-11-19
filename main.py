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

navigateStage2()

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
    l = 1.0      
    a = 2.0      
    prevRow = None

    # -----------------------------
    # PART 1: Move until reaching x < l
    # -----------------------------
    while enes100.x < l:
        moveUntilObstacle()

        row = checkRow()

        if row == 1:
            turnRightTo(math.radians(90))
            move_until_row2()
            turnLeftTo(math.radians(90))
            prevRow = 1

        elif row == 2:
            if prevRow == 1:
                turnRightTo(math.radians(90))
                move_until_row3()
                turnLeftTo(math.radians(90))

            elif prevRow == 3:
                turnLeftTo(math.radians(90))
                move_until_row1()
                turnRightTo(math.radians(90))

            else:
                turnLeftTo(math.radians(90))
                move_until_row1()
                turnRightTo(math.radians(90))

        else:  # row == 3
            turnLeftTo(math.radians(90))
            move_until_row2()
            turnRightTo(math.radians(90))
            prevRow = 3


    # -----------------------------
    # PART 2: Move until x < a
    # -----------------------------
    prevRow = None

    while enes100.x < a:
        moveUntilObstacle()

        row = checkRow()

        if row == 1:
            turnRightTo(math.radians(90))
            move_until_row2()
            turnLeftTo(math.radians(90))
            prevRow = 1

        elif row == 2:
            if prevRow == 1:
                turnRightTo(math.radians(90))
                move_until_row3()
                turnLeftTo(math.radians(90))

            elif prevRow == 3:
                turnLeftTo(math.radians(90))
                move_until_row1()
                turnRightTo(math.radians(90))

            else:
                turnLeftTo(math.radians(90))
                move_until_row1()
                turnRightTo(math.radians(90))

        else:  # row == 3
            turnLeftTo(math.radians(90))
            move_until_row2()
            turnRightTo(math.radians(90))
            prevRow = 3
            
            
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
    elif(enes100.y < 1.2 && enes100.y > 0.65):
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
        turnRight(speed)  # negative = turn right
        time.sleep(0.05)
        currentTheta = normalize_angle(enes100.theta)

    stop_all()
    time.sleep(0.05)
def turnLeftTo(targetTheta, speed=20):
    tolerance = 0.05

    targetTheta = normalize_angle(targetTheta)
    currentTheta = normalize_angle(enes100.theta)

    while abs(normalize_angle(currentTheta - targetTheta)) > tolerance:
        turnLeft(speed)
        time.sleep(0.05)
        currentTheta = normalize_angle(enes100.theta)

    stop_all()
    time.sleep(0.05)



