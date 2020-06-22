#!/usr/bin/env python

import rospy
import actionlib
from geometry_msgs.msg import Pose
from path_exam.msg import RecordOdomAction,RecordOdomResult,RecordOdomGoal
import time
from my_listener import listener

class CustomActionMsgClass():
    def __init__(self):
        self._as = actionlib.SimpleActionServer("/rec_pose_as", RecordOdomAction, self.goal_callback, False)
        self._as.start()
        self.result   = RecordOdomResult()
        self.ear=listener()
        #rospy.loginfo("inside init")
    def goal_callback(self,goal):
        i=0
        #rospy.loginfo("inside call")
        while i<20:
         #   rospy.loginfo("inside loop")
            self.result.arr.poses.append(self.ear.pose_value())
            i+=1
            time.sleep(1)
        #rospy.loginfo("outoff call")
        self._as.set_succeeded(self.result)
        #rospy.loginfo("HERE?")
        self.get_value()
    def get_value(self):
        #rospy.loginfo("HERE in value")
        print("Last Pose")
        print(self.result.arr.poses[-1])

        return self.result.arr
if __name__ == '__main__':
    rospy.init_node('my_action')
 # rospy.loginfo("inside node")
    some_object=CustomActionMsgClass()
  #rospy.loginfo("reached here?")
  #rospy.loginfo(some_object.get_value())
    rospy.spin()