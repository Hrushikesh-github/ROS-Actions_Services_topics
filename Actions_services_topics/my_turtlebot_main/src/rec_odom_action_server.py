'''
This program creates an action server which reads the odometry data and if the odometry data is greater than a certain value the action server is completed. That certain value is chosen depending on the size of the maze to ensure that the robot has exited the maze.Also a new action message type was created which has empty arguments for goal and feedback but returns an array of odometry data in results.The action server also quits if time exceeds 80 seconds.It also uses a class 'odom_reader' which subscribers to /odom topic
'''

#! /usr/bin/env python
import rospy
import time
import actionlib
from my_turtlebot_actions.msg import record_odomResult,record_odomAction,record_odomFeedback
from nav_msgs.msg import Odometry
from odom_read import odom_reader
class my_action():
    def __init__(self):
    # creates the action server
        self._as = actionlib.SimpleActionServer("action_custom_msg_as", record_odomAction, self.goal_callback, False)
        self._as.start()
        rospy.loginfo("action server started")
        self._result   = record_odomResult()
        self._feedback=record_odomFeedback()
        self.stack=record_odomResult()
        self.my_reader=odom_reader()
        self.rate=rospy.Rate(1)
    def goal_callback(self, goal):
        i=0
        self._as.publish_feedback(self._feedback)
        while i<80:
            self.odom_reading=self.my_reader.get_data()#this keeps updating
            #rospy.loginfo(self.odom_reading)
            self.stack.result_odom_array.append(self.odom_reading)
            if self.odom_reading.pose.pose.position.y<-10:
                rospy.loginfo("you have exited")
                break
            rospy.loginfo(i)
            self.rate.sleep()
            if i==79:
                rospy.logwarn("Exceeding time limit")
            i+=1
        self._result = self.stack
        self._as.set_succeeded(self._result)
        rospy.loginfo("Done running")
if __name__=="__main__":
    rospy.init_node('record_odom_action_server_node')
    my_object=my_action()
    rospy.spin()
