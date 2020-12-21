#! /usr/bin/env python2
import rospy
# import command sending libraries
from std_msgs.msg import Float64
import future
from geometry_msgs.msg import Point
import math

##### Global counter variables #####
m=0
n=0

##### Function for legs #####
def legparams(x):
    y=x
    z=x
    global m,n
    if(x==0.78):
        m+=1
    if(x<=0.1):
        n+=1
    t=m%2
    p=n%2

    if(p==1 and x>0):
        y=0

    if(t==1 and x<0.78):
        z=0.78

    return y,z



def main():
    i=0
    j=0
    x=0
    ##### Define publishers for the joint controllers #####
    rospy.init_node("walk")
    pleg1=rospy.Publisher('/hexa_wexa/leg1_position_controller/command', Float64, queue_size=1)
    pleg2=rospy.Publisher('/hexa_wexa/leg2_position_controller/command', Float64, queue_size=1)
    pleg3=rospy.Publisher('/hexa_wexa/leg3_position_controller/command', Float64, queue_size=1)
    pleg4=rospy.Publisher('/hexa_wexa/leg4_position_controller/command', Float64, queue_size=1)
    pleg5=rospy.Publisher('/hexa_wexa/leg5_position_controller/command', Float64, queue_size=1)
    pleg6=rospy.Publisher('/hexa_wexa/leg6_position_controller/command', Float64, queue_size=1)
    pfemur1=rospy.Publisher('/hexa_wexa/femur1_position_controller/command', Float64, queue_size=1)
    pfemur2=rospy.Publisher('/hexa_wexa/femur2_position_controller/command', Float64, queue_size=1)
    pfemur3=rospy.Publisher('/hexa_wexa/femur3_position_controller/command', Float64, queue_size=1)
    pfemur4=rospy.Publisher('/hexa_wexa/femur4_position_controller/command', Float64, queue_size=1)
    pfemur5=rospy.Publisher('/hexa_wexa/femur5_position_controller/command', Float64, queue_size=1)
    pfemur6=rospy.Publisher('/hexa_wexa/femur6_position_controller/command', Float64, queue_size=1)
    rate = rospy.Rate(20)

    ##### Loop to bring robot in position #####
    for j in range(0,20):
        i=0.05*j*math.pi/2
        x=(math.sin(i)**2)*0.5
        pleg1.publish(-1*x)
        pleg2.publish(-1*x)
        pleg3.publish(-1*x)
        pleg4.publish(x)
        pleg5.publish(x)
        pleg6.publish(x)
        pfemur1.publish(x)
        pfemur2.publish(x)
        pfemur3.publish(-1*x)
        pfemur4.publish(x)
        pfemur5.publish(-1*x)
        pfemur6.publish(-1*x)
        rate.sleep()

    ##### Loop for walking #####
    while not rospy.is_shutdown():
        i=0.05*j*math.pi/2
        x=(math.sin(i)**2)*0.78  ### Modulating the sine sq wave to be between 0 to 0.78 ###
        y,z=legparams(x)
        #leg1
        pfemur1.publish(z)
        pleg1.publish(y)
        #leg3
        pfemur3.publish(-1*y)
        pleg3.publish(-1*z)
        #leg5
        pfemur5.publish(y)
        pleg5.publish(z)

        j+=1
        rate.sleep()


if __name__ == "__main__":
    main()
