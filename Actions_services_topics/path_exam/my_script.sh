#!/bin/bash
rostopic pub /rec_pose_as/goal path_exam/RecordOdomActionGoal "header:
  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: ''
goal_id:
  stamp:
    secs: 0
    nsecs: 0
  id: ''
goal: {}"

