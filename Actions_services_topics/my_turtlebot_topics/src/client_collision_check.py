#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from laser_read import laser_reader
from std_srvs.srv import Trigger,TriggerRequest

rospy.init_node('call_server')
rospy.wait_for_service('/detector')
my_connector=rospy.ServiceProxy('/detector',Trigger, False)
result=my_connector()#no need to pass arguments
print(result)