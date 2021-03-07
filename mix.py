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
s=0
l=0
c=0
##### Function for legs #####
def legparams(x,i):
    y=x
    z=x
    global m,n,s,l,c
    if(x==0.707):
        m+=1
    if(x<=0.1):
        n+=1
    if(x<0.004):
        s+=1
    t=m%2
    p=n%2
    if(p==1 and x>0):
        y=-y
    if(t==1):
        z=0.707
    if(s%2==1 and t==1):#--third quad
        z=(math.sin(i+30)**2)*0.707
        if x>=0.353:
            c+=1
            l=0.707
        print("3rd quad")
    if(s%2==1 and t==0):#--fourth quad
        z=0
        c+=1
        l=0.707
        if(x<=0.689):
            l=(math.sin(c*0.05*(math.pi/2)*1.5)**2)*0.707
        print("4th quad")
    if(s%2==0 and t==0):#--first quad
        l=z
        print("1st Quad")
    elif (s%2==0 and t==1):#--sec quad 
        c=0
        l=z
        print("2nd quad")

    return y,z

def even(y,z,l):
    #leg1
    pfemur1.publish(-l)
    pleg1.publish(l)
    #leg3
    pfemur3.publish(-l)
    pleg3.publish(l)
    #leg5
    pfemur5.publish(-l)
    pleg5.publish(l)

    #leg2
    pfemur2.publish(-1*y)
    pleg2.publish(-1*z)
    #leg4
    pfemur4.publish(-1*y)
    pleg4.publish(-1*z)
    #leg6
    pfemur6.publish(y)
    pleg6.publish(z)

def odd(y,z,l):
    #leg1
    pfemur1.publish(y)
    pleg1.publish(z)
    #leg3
    pfemur3.publish(-1*y)
    pleg3.publish(-1*z)
    #leg5
    pfemur5.publish(y)
    pleg5.publish(z)

    #leg2
    pfemur2.publish(-l)
    pleg2.publish(l)
    #leg4
    pfemur4.publish(-l)
    pleg4.publish(l)
    #leg6
    pfemur6.publish(-l)
    pleg6.publish(l)


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
        # pleg1.publish(-1*x)
        # pleg2.publish(-1*x)
        # pleg3.publish(-1*x)
        # pleg4.publish(x)
        # pleg5.publish(x)
        # pleg6.publish(x)
        # pfemur1.publish(x)
        # pfemur2.publish(x)
        # pfemur3.publish(-1*x)
        # pfemur4.publish(x)
        # pfemur5.publish(-1*x)
        # pfemur6.publish(-1*x)
        # rate.sleep()

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
    n=0
    c=0
    while not rospy.is_shutdown():
        i=0.05*j*math.pi/2       
        x=(math.sin(i)**2)*0.707  ### Modulating the sine sq wave to be between 0 to 0.78 ###
        y,z=legparams(x,i)
        if(j%80==0):
            n=not n
            j=0
        if(n==0): ###odd### 3 - front(pull) , 1,5 - back(push)
            print("cycle 1: " , j)
            #leg1
            pfemur1.publish(y)
            pleg1.publish(z)
            #leg3
            pfemur3.publish(-1*y)
            pleg3.publish(-1*z)
            #leg5
            pfemur5.publish(y)
            pleg5.publish(z)

            #leg2
            pfemur2.publish(-l)
            pleg2.publish(l)
            #leg4
            pfemur4.publish(-l)
            pleg4.publish(l)
            #leg6
            pfemur6.publish(-l*1.3)
            pleg6.publish(l*1.3)

        if(n==1): ###even### 2,4 - front(pull) , 6 - back(push)
            print("cycle 0: " , j)
            #leg1
            pfemur1.publish(-l*0.75)
            pleg1.publish(l*0.75)
            #leg3
            pfemur3.publish(-l*1.1)
            pleg3.publish(l*1.1)
            #leg5
            pfemur5.publish(-l*0.75)
            pleg5.publish(l*0.75)

            #leg2
            pfemur2.publish(-1*y)
            pleg2.publish(-1*z)
            #leg4
            pfemur4.publish(-1*y)
            pleg4.publish(-1*z)
            #leg6
            pfemur6.publish(y*1.1)
            pleg6.publish(z*1.1)
        j+=1
        rate.sleep()
if __name__ == "__main__":
    main()