#! /usr/bin/env python
import rospy
import time
import actionlib
from my_turtlebot_actions.msg import record_odomResult,record_odomAction,record_odomFeedback
from nav_msgs.msg import Odometry
from odom_read2 import odom_reader
class my_action():
    def __init__(self):
    # creates the action server
        self._as = actionlib.SimpleActionServer("action_custom_msg_as", record_odomAction, self.goal_callback, False)
        self._as.start()
        self._result   = record_odomResult()
        self._feedback=record_odomFeedback()
        self.stack=record_odomResult()
        self.my_reader=odom_reader()
        self.rate=rospy.Rate(1)
    def goal_callback(self, goal):
        i=0
        self._as.publish_feedback(self._feedback)
        while i<37:
            self.odom_reading=self.my_reader.get_data()#this keeps updating
            rospy.loginfo(self.odom_reading)
            self.stack.result_odom_array.append(self.odom_reading)
            if self.odom_reading.pose.pose.position.y<-10:
                rospy.loginfo("you have exited")
                break
            rospy.loginfo(i)
            self.rate.sleep()
            if i==36:
                rospy.logwarn("time is up, didn't exit")
            i+=1
        self._result = self.stack
        self._as.set_succeeded(self._result)
if __name__=="__main__":
    rospy.init_node('record_odom_action_server_node')
    my_object=my_action()
    rospy.spin()
