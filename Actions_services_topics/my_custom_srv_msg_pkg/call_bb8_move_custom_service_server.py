#!/usr/bin/env python
import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest

rospy.init_node('call_my_server')
rospy.wait_for_service('/move_bb8_in_circle_custom')
my_connector=rospy.ServiceProxy('/move_bb8_in_circle_custom', MyCustomServiceMessage)
my_duration=MyCustomServiceMessageRequest()
my_duration.duration=10
ITyped=my_connector(my_duration)
print(ITyped)