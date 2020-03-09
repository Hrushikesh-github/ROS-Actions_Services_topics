#!/usr/bin/env python
import rosopy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry
import time

class my_topics():
    def __init__(self):
        self.pub_vel=rospy.Publisher('/cmd_vel',Twist,queue_size=1)
        self.sub_odom=rospy.Subscriber('/odom',Odometry,callback_odom)
        self.sub_Imu=rospy.Subscriber('/sphero/imu/data3',Imu,callback_imu)
        self.move_sphero()
    def callback_imu(self,data):
        print(data)
    def callback_odom(self,data):
        print(data)
    def move_sphero(self):
        rospy.loginfo("sending vel")
        vel=Twist()
        vel.linear.x=0.3
        pub_vel.publish(vel)
        time.sleep(2)
        vel.linear.x=0
        vel.angular.z=0.2
        pub_vel.publish(vel)
        time.sleep(2)
        vel.angular.z=0
        vel.linear.x=-0.3
        pub_vel.publish(vel)
        time.sleep(2)
        vel.linear.x=0
        pub_vel.publish(vel)
if __name__ == '__main__':
  rospy.init_node('moving sphero')
  my_topics()

