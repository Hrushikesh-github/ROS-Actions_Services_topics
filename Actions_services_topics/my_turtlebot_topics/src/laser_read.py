#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
import time

class laser_reader(object):
    def __init__(self):
        self.sub=rospy.Subscriber('/kobuki/laser/scan',LaserScan ,self.callback)
        self.laserdata=LaserScan()
        rospy.loginfo("initiated!!")
    def callback(self,data):
        self.laserdata=data
    def get_data(self):
        #since the callback keeps on running,the variable self.laserdata keeps on updating
        return self.laserdata

if __name__=="__main__":
    rospy.init_node('read_laser')
    rospy.loginfo("here!")
    reader=laser_reader()
    rate=rospy.Rate(0.5)
    while not rospy.is_shutdown():
        value=reader.get_data()
        rospy.loginfo(value)
        rate.sleep()


