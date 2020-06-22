#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Pose

class listener():
    def __init__(self):
 #       rospy.loginfo('listening')
        self.sub_pose = rospy.Subscriber('/drone/gt_pose',Pose,self.sub_callback)
        #self.coordinate=Float64()
    def sub_callback(self,data):
        self.coordinate=data
        self.x_coordinate=data.position.x
    def my_value(self):
        value=self.x_coordinate
        return(value)
    def pose_value(self):
        value=self.coordinate
        return(value)
        #rospy.loginfo(self.coordinate)
if __name__=='__main__':
    rospy.init_node('my_listener')
    obje=listener()
   # print(obje.my_value())
    rospy.spin()

    #rospy.loginfo(obje)
