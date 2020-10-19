#! /usr/bin/env python2
import rospy
# import command sending libraries
from std_msgs.msg import Float64
import future
from geometry_msgs.msg import Point
import math

m=0
n=0
def  legparams(x):
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


#define fns to pub to all joints
def main():
    i=0
    j=0
    x=0
    rospy.init_node("walk")
    prev1=rospy.Publisher('/improvedesign/Rev1_position_controller/command', Float64, queue_size=1)
    prev2=rospy.Publisher('/improvedesign/Rev2_position_controller/command', Float64, queue_size=1)
    prev3=rospy.Publisher('/improvedesign/Rev3_position_controller/command', Float64, queue_size=1)
    prev4=rospy.Publisher('/improvedesign/Rev4_position_controller/command', Float64, queue_size=1)
    prev5=rospy.Publisher('/improvedesign/Rev5_position_controller/command', Float64, queue_size=1)
    prev6=rospy.Publisher('/improvedesign/Rev6_position_controller/command', Float64, queue_size=1)
    prev7=rospy.Publisher('/improvedesign/Rev7_position_controller/command', Float64, queue_size=1)
    prev8=rospy.Publisher('/improvedesign/Rev8_position_controller/command', Float64, queue_size=1)
    prev9=rospy.Publisher('/improvedesign/Rev9_position_controller/command', Float64, queue_size=1)
    prev10=rospy.Publisher('/improvedesign/Rev10_position_controller/command', Float64, queue_size=1)
    prev11=rospy.Publisher('/improvedesign/Rev11_position_controller/command', Float64, queue_size=1)
    prev12=rospy.Publisher('/improvedesign/Rev12_position_controller/command', Float64, queue_size=1)
    rate = rospy.Rate(20)
    for j in range(0,20):
        i=0.05*j*math.pi/2
        x=(math.sin(i)**2)*0.5
        prev1.publish(-1*x)
        prev2.publish(-1*x)
        prev3.publish(-1*x)
        prev4.publish(x)
        prev5.publish(x)
        prev6.publish(x)
        prev7.publish(x)
        prev8.publish(x)
        prev9.publish(-1*x)
        prev10.publish(x)
        prev11.publish(-1*x)
        prev12.publish(-1*x)
        rate.sleep()

    while not rospy.is_shutdown():
        i=0.05*j*math.pi/2
        x=(math.sin(i)**2)*0.78
        y,z=legparams(x)
        #leg4
        prev10.publish(z)
        prev6.publish(y)
        #leg6
        prev9.publish(-1*y)
        prev1.publish(-1*z)
        #leg2
        prev8.publish(y)
        prev4.publish(z)

        j+=1
        rate.sleep()
if __name__ == "__main__":
    main()
