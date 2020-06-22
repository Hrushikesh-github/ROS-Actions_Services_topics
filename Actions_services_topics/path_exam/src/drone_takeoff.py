#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty
import time
from geometry_msgs.msg import Twist
rospy.init_node("take_off")
pub=rospy.Publisher('/drone/takeoff',Empty,queue_size=1)
a=Empty()
i=0
while i<4:
    pub.publish(a)
    time.sleep(1)
    i+=1
cmd=rospy.Publisher('/cmd_vel',Twist,queue_size=1)
vel=Twist()
cmd.publish(vel)