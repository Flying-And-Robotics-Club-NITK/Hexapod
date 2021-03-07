#! /usr/bin/env python2
import rospy
# import command sending libraries
from std_msgs.msg import Float64
import future
from geometry_msgs.msg import Point
import math

m=-1
n=0
def  legparams(x):
    y=x
    z=x
    g=x
    h=x
    global m,n
    if(x>=0.78):
        m+=1
    if(x<=0.1):
        n+=1
    t=m%2
    p=n%2
    
    print(x,m,n)
    return y,z


#define fns to pub to all joints
def main():
    i=0
    j=0
    x=0
    rospy.init_node("walk2")
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
    for j in range(0,20):
        i=0.05*j*math.pi/2
        x=(math.sin(i))

        pleg1.publish(x)
        pleg2.publish(-1*x)
        pleg3.publish(x)
        pleg4.publish(-1*x)
        pleg5.publish(x)
        pleg6.publish(x)
        pfemur1.publish(-x)
        pfemur2.publish(-1*x)
        pfemur3.publish(-1*x)
        pfemur4.publish(x)
        pfemur5.publish(-1*x)
        pfemur6.publish(x)
        rate.sleep()

    while not rospy.is_shutdown():
        
        i=0.05*j*math.pi/2
        x=(math.sin(i))
        y=(math.sin(i))**2
        g=-1*(math.sin(i))*0.785
        h=x*0.785
        p,z=legparams(x)
        #leg1
        pfemur1.publish(-0.785)
        pleg1.publish(0.785)
        #leg2
        pfemur2.publish(-x)
        pleg2.publish(-x)
        #leg3
        pfemur3.publish(-0.785)
        pleg3.publish(0.785)
        #leg4
        pfemur4.publish(-x)
        pleg4.publish(-x)
        #leg5
        pfemur5.publish(-0.785)
        pleg5.publish(0.785)
        #leg6
        pfemur6.publish(x)
        pleg6.publish(y)
        
        j+=1
        rate.sleep()
if __name__ == "__main__":
    main()
