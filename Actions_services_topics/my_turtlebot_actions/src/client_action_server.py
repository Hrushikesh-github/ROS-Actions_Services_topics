#! /usr/bin/env python
import rospy
import actionlib
from my_turtlebot_actions.msg import record_odomResult,record_odomAction,record_odomGoal
from nav_msgs.msg import Odometry

def feedback_callback(feedback):
    rospy.loginfo("Rec Odom Feedback feedback ==>"+str(feedback))
rospy.init_node('client_node')
client = actionlib.SimpleActionClient('action_custom_msg_as', record_odomAction)
rospy.loginfo("client waiting")
client.wait_for_server()
goal=record_odomGoal()
client.send_goal(goal,feedback_cb=feedback_callback)