# -*- coding: utf-8 -*-
#Base has limited range of about 170 degrees.



import ArmMovement
from Constants import *
import math
from AngleFinder import *
import socket
import time
import re
import subprocess

#This moves the arm to the X, Y, Z coordinates
def moveArm(x, y, z):
    finder = AngleFinder()
    arm = ArmMovement.ArmControl()
    
    global angle2;
    angle2 = (int)(finder.angle_calculator1(x,y,z))
    print 'angle2: ' + str(angle2)
    global angle1;
    angle1 = (int)(finder.angle_calculator2(x,y,z))
    print 'angle1: ' + str(angle1)
    global angle3;
    angle3 = (int)(finder.rotational_calculator(x,y))
    print 'angle3: ' + str(angle3)

    arm.setAngle(CONST_BASE_CHANNEL,180-angle3)
    time.sleep(1)
    arm.setAngle(CONST_JOINT_1_CHANNEL, angle1)
    arm.setAngle(CONST_JOINT_2_CHANNEL, angle2)
    arm.setAngle(CONST_JOINT_3_CHANNEL, 90)
    time.sleep(2)
    arm.setAngle(CONST_GRIPPER_CHANNEL,115)
    arm.close()
    return True;

#This resets the arm back to the neutral position
def resetPosition():
    finder = AngleFinder()
    arm = ArmMovement.ArmControl()
    
    print 'RESET...'
    x = 0.0
    z = 12.00
    y = 7.0
    
    angle1 = (int)(finder.angle_calculator2(x,y,z))
    angle2 = (int)(finder.angle_calculator1(x,y,z))
    angle3 = (int)(finder.rotational_calculator(x,y))
    
    time.sleep(3)
    arm.setAngle(CONST_JOINT_1_CHANNEL, angle1)
    arm.setAngle(CONST_JOINT_2_CHANNEL, angle2)
    arm.setAngle(CONST_JOINT_3_CHANNEL, 90)
    arm.setAngle(CONST_BASE_CHANNEL,180-angle3)
    time.sleep(2)
    arm.setAngle(CONST_GRIPPER_CHANNEL,0)
    arm.close()

#This opens the arm's gripper and releaseses the object
def dropObject():
    finder = AngleFinder()
    arm = ArmMovement.ArmControl()
    
    print 'DROPPING'
	
	#These can be changed later depending on where you want to drop the object.
    x = 0.0
    z = 12.00
    y = 7.0
    
    angle1 = (int)(finder.angle_calculator2(x,y,z))
    angle2 = (int)(finder.angle_calculator1(x,y,z))
    angle3 = (int)(finder.rotational_calculator(x,y))
    
    time.sleep(3)
    arm.setAngle(CONST_JOINT_1_CHANNEL, angle1)
    arm.setAngle(CONST_JOINT_2_CHANNEL, angle2)
    arm.setAngle(CONST_JOINT_3_CHANNEL, 90)
    arm.setAngle(CONST_BASE_CHANNEL,180-angle3)
    time.sleep(2)
    arm.setAngle(CONST_GRIPPER_CHANNEL,0)
    arm.close()
 
x = 5.0
z = 10.0
y = 0
'''
UDP_IP = "192.168.1.103"
'''
#UDP port may need to be changed depending on what you are using. Make sure that both the sending device and receiving device are on the same wireless network.
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', UDP_PORT))
counter = 0;
dropObject()
print 'waiting for data'
data, addr = sock.recvfrom(1024)
arr = data.decode().split(',')
y=float(arr[1])/10.0
x=float(arr[0])/10.0
#The -7 below is to adjust for the height of the arm, since it the base is not level with the ground.
z=float(arr[2])/10.0-7.0
print 'x: ' + str(x)
print 'y: ' + str(y)
print 'z: ' + str(z)
moveArm(x,y,z)
resetPosition()

