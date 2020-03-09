#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist
var=Twist()
done=BB8CustomServiceMessageResponse()
done.success=False
def my_callback(request):
    global var
    global done
    i=0
    print ("duration given was:")
    while i<request.duration:
        var.linear.x=0.5
        var.angular.z=0.5
        rate.sleep()
        pub.publish(var)
        i+=1
    var.linear.x=0
    var.angular.z=0
    pub.publish(var)
    done.success=True
    print "My_callback has been called"
    return done # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split()))

rospy.init_node('service_server')
pub=rospy.Publisher('/cmd_vel',Twist,queue_size=1)
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage , my_callback) # create the Service called my_service
rate=rospy.Rate(1)
rospy.spin() # maintain the service open.

