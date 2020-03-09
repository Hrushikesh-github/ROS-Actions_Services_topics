'''
This program moves the robot based on input message.
'''
#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time

class move_turtlebot():
    def __init__(self):
        self.pub=rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.vel=Twist()
        rospy.loginfo("move_turtlebot initiated!!")

    def move(self,message):

        if message=="LEFT":
            self.vel.linear.x=0
            self.vel.linear.y=0
            self.vel.angular.z=0.4
            rospy.loginfo("turning left")
        elif message=="RIGHT":
            self.vel.linear.x=0
            self.vel.linear.y=0
            self.vel.angular.z=-0.4
            rospy.loginfo("turning right")
        elif message=="FORWARD":
            self.vel.linear.x=0.4
            self.vel.linear.y=0
            self.vel.angular.z=0
        else:
            rospy.loginfo("stopping")
            self.vel=Twist()
        self.pub.publish(self.vel)#publish the velocity
        if message=="LEFT" or message=="RIGHT":
            time.sleep(2.1)
#the timing here is small enough so that the robot turns slightly to avoid the obstacle.This ensures that the robot doesn't get struck in a region.This timing has been decided practically and is suitable for the kobuki,. But for others,based on their geometry,it should be changed for effective result.  
            
if __name__=="__main__":
    rospy.init_node('move_turtlebot')
    rospy.loginfo("here!")

