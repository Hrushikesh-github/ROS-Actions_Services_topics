#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time

class move_turtlebot():
    def __init__(self):
        self.pub=rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.vel=Twist()
        rospy.loginfo("initiated!!")

    def move(self,message):

        if message=="LEFT":
            self.vel.linear.x=0
            self.vel.linear.y=0
            self.vel.angular.z=0.4
            rospy.loginfo("inside left")
        elif message=="RIGHT":
            self.vel.linear.x=0
            self.vel.linear.y=0
            self.vel.angular.z=-0.4
            rospy.loginfo("inside right")
        elif message=="FORWARD":
            self.vel.linear.x=0.2
            self.vel.linear.y=0
            self.vel.angular.z=0
            rospy.loginfo("inside forward")
        else:
            rospy.loginfo("inside stop")
            self.vel=Twist()
        self.pub.publish(self.vel)
if __name__=="__main__":
    rospy.init_node('move_turtlebot')
    rospy.loginfo("here!")
    while not rospy.is_shutdown():
        ahead=move_turtlebot()
        ahead.move(input("Which way"))