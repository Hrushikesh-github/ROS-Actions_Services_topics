#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.

from geometry_msgs.msg import Twist
var=Twist()
def my_callback(request):
    global var
    var.linear.x=0.5
    var.angular.z=0.5
    pub=rospy.Publisher('/cmd_vel',Twist,queue_size=1)
    pub.publish(var)
    print "My_callback has been called"
    return EmptyResponse() # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split()))

rospy.init_node('service_server')
my_service = rospy.Service('/move_bb8_in_circle', Empty , my_callback) # create the Service called my_service with the defined callback
rospy.spin() # maintain the service open.
