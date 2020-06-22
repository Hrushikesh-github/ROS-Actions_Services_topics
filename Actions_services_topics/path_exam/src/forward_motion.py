#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
import time
class take_off_and_move_straight():
    @staticmethod
    def move():
        pub=rospy.Publisher('/drone/takeoff',Empty,queue_size=1)
        cmd=rospy.Publisher('/cmd_vel',Twist,queue_size=1)
        land=rospy.Publisher('/drone/land',Empty,queue_size=1)
        a=Empty()
        vel=Twist()
        vel.linear.x=1
        zero_vel = Twist()
        start_time = time.time()
        for i in range(0,2):
            pub.publish(a)
            time.sleep(1)
        
        for j in range(0,5):
            cmd.publish(vel)
            time.sleep(1)
        
        for i in range(0,4):
            cmd.publish(zero_vel)
        
        for i in range(0,4):
            land.publish(a)
            time.sleep(1)
            i+=1
        end_time = time.time()
        #print("Total time elapsed is (should be around 11):", end_time-start_time)

if __name__ == '__main__':
    rospy.init_node("take_off_and_move_please")
    #rate = rospy.Rate(1)
    take_off_and_move_straight.move()
    

