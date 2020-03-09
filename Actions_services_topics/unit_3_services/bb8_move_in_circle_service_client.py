#!/usr/bin/env python
import rospy
from std_srvs.srv import Empty, EmptyRequest
# Initialise a ROS node with the name service_client
rospy.init_node('service_client')
# Wait for the service client /trajectory_by_name to be running
rospy.wait_for_service('/move_bb8_in_circle')
# Create the connection to the service
my_connector = rospy.ServiceProxy('/move_bb8_in_circle', Empty)
my_varia=EmptyRequest()
my_connector(my_varia)
print('this is from client function')

