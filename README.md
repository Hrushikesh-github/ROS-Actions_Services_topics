# ROS-Actions_Services_topics
Packages related to ROS Action, Services and topics.

I have created various services, action clients. action servers and w

As part of a project https://rds.theconstructsim.com/tc_projects/use_project_share_link/4bcc0470-4192-4649-b354-8cfdd450ae8f?utm_source=books&utm_medium=basics&utm_campaign=turtle
where the goal is to get the turtlebot out of the maze without any collision but without using any global or local map. 
The turtlebot has odometry sensors and a 180 degree laser scan which can provide details such as in the near environment
but restircted to 180 degrees.

The following were done to get the turtlebot out of the maze:
1. Identify all the topics that are necessary, and can be useful.
2. Subscribe to the odometry data and the laser scan data through ros topics.
3. Created a service that, when called, tells if the robot is about to hit an obstacle, through the laser data .
   Safe distance taken was 5m. It also returns the direction that the robot should move in case of possible collision. 
   Trigger.srv service message type was used for this purpose
4. Created an action, that, when called, will start to save odometry data and check if the robot has exited the maze. The action
   also stops and generates a warning message when certain time limit is exceeded( 35 sec here). 
   A new action message type was created for this purpose: 
   #goal, empty                
   ---                             
   #result, Odometry array             
   nav_msgs/Odometry[] result_odom_array                
   ---                             
   #feedback, empty
