#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
import time

class odom_reader():
    def __init__(self):
        self.sub=rospy.Subscriber('/odom',Odometry ,self.callback)
        self.odomdata=Odometry()
        rospy.loginfo("initiated!!")
    def callback(self,data):
        self.odomdata=data
    def get_data(self):
        return self.odomdata

if __name__=="__main__":
    rospy.init_node('read_odometry')
    rospy.loginfo("here!")
    reader=odom_reader()
    rate=rospy.Rate(0.5)
    while not rospy.is_shutdown():
        value=reader.get_data()
        rospy.loginfo(value)
        rate.sleep()


