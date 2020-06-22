cmake_minimum_required(VERSION 2.8.3)
project(path_exam)


find_package(catkin REQUIRED COMPONENTS
  actionlib_msgs
  geometry_msgs
  std_msgs
  message_generation
)



## Generate messages in the 'msg' folder
# add_message_files(
#   FILES
#   Message1.msg
#   Message2.msg
# )

## Generate services in the 'srv' folder
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

## Generate actions in the 'action' folder
 add_action_files(
   FILES
   RecordOdom.action
#   Action2.action
)

## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
	# Or other packages containing msgs
   actionlib_msgs
   geometry_msgs
   std_msgs
 )

catkin_package(
  CATKIN_DEPENDS 
  rospy
  message_runtime
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)



