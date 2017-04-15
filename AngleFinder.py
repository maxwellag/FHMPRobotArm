import ArmMovement
from Constants import *
import math


class AngleFinder:
#The constants below can be found in the constants.py file.
    segment1 = ARM_1_LENGTH
    segment2 = ARM_2_LENGTH
    maxDistance = segment1+segment2
    pi = math.pi

    def angle_calculator1(self,x,y,z):
        p = math.sqrt(x*x+y*y)
        if math.sqrt(p*p+z*z)>AngleFinder.maxDistance:
            raise Exception('Coordinate is beyond arms reach.')
        D = (-p*p +-z*z + AngleFinder.segment1*AngleFinder.segment1 + AngleFinder.segment2*AngleFinder.segment2)/(2*AngleFinder.segment1*AngleFinder.segment2)
        return 180 - math.acos(D)*180.0/AngleFinder.pi



    def angle_calculator2(self,x,y,z):
        p = math.sqrt(x*x+y*y)
        if math.sqrt(p*p+z*z)>AngleFinder.maxDistance:
            raise Exception('Coordinate is beyond arms reach.')
        beta = math.atan2(z, p)
        alpha = math.acos(((-AngleFinder.segment2*AngleFinder.segment2)+(p*p+z*z)+(AngleFinder.segment1*AngleFinder.segment1))/(2*(math.sqrt(p*p+z*z))*AngleFinder.segment1))
        if p <0:
            return 180 - (beta-alpha)*180.0/AngleFinder.pi
        else:
            return (beta+alpha) * 180.0 / AngleFinder.pi


    def rotational_calculator(self,x,y):
        print 'Base Angle: ' + str(math.atan2(y,x)*180/AngleFinder.pi)
        return math.atan2(y,x)*180/AngleFinder.pi



