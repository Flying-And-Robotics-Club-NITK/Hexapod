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
    if(x==0):
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
    rospy.init_node("oneleg")
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


    while not rospy.is_shutdown():
        i=0.05*j*math.pi/2
        x=(math.sin(i)**2)*0.78
        y,z=legparams(x)
        #leg4
        prev8.publish(z)
        prev4.publish(y)


        j+=1
        rate.sleep()
if __name__ == "__main__":
    main()
