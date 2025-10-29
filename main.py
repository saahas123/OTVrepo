from enes100 import enes100
import time
from Motors import turnLeft, turnRight
from machine import Pin, time_pulse_us

#ultra1
TRIG1 = Pin(12, Pin.OUT)
ECHO1 = Pin(14, Pin.IN)

# --- Ultrasonic Sensor 2 Pins ---
TRIG2 = Pin(27, Pin.OUT)
ECHO2 = Pin(26, Pin.IN)

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




# --- Get distance from Ultrasonic Sensor 1 ---
def get_distance_ultra1():
    TRIG1.off()
    time.sleep_us(2)
    TRIG1.on()
    time.sleep_us(10)
    TRIG1.off()
    
    duration = time_pulse_us(ECHO1, 1, 30000)  # timeout 30ms
    distance = (duration * 0.0343) / 2  # cm
    return distance

# --- Get distance from Ultrasonic Sensor 2 ---
def get_distance_ultra2():
    TRIG2.off()
    time.sleep_us(2)
    TRIG2.on()
    time.sleep_us(10)
    TRIG2.off()
    
    duration = time_pulse_us(ECHO2, 1, 30000)
    distance = (duration * 0.0343) / 2
    return distance
