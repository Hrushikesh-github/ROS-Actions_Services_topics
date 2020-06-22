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

### Screenshots
![turtlebot1](https://user-images.githubusercontent.com/56476887/85292699-f0325000-b4b9-11ea-9b09-855d5650c013.png)

![turtle_proj2](https://user-images.githubusercontent.com/56476887/85292707-f4f70400-b4b9-11ea-8234-f303ca52837e.png)



![ardrone](https://user-images.githubusercontent.com/56476887/85292666-e3156100-b4b9-11ea-9258-681043405400.png)


Another project I have worked on was based on the Parrot AR Drone. The drone which is ROS compatible take-off and lands by publishing to two different topics and it's motion is controlled by another topic(/cmd_val). 
Under this project, I have done the following:
Created a package which takeoffs the AR Drone, moves it with a velocity of 1m/s for 5 seconds and then lands it. Additionally a server and an action with a custom action message was created. The purpose of the server is to compute the distance covered by the drone and the action server called 'RecordOdom' when called by a client, records the postion of the drone for 20 seconds and after the end of the period prints the last pose the drone is in. Both the server and the action run throughout the motion of the ardrone as expected.

![drone_motion](https://user-images.githubusercontent.com/56476887/85292688-e9a3d880-b4b9-11ea-9569-3fb1026796e2.gif)
