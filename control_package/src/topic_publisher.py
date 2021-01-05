#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist


def publish_message():
  rospy.init_node('move_robot_node', anonymous=False)
  pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
  rate = rospy.Rate(2)
  move = Twist()
  move.linear.x = 0.5 #Move the robot with a linear velocity in the x axis

  while not rospy.is_shutdown(): 
    pub.publish(move)
    rate.sleep()



if __name__=='__main__':
  try:
    publish_message()
  except rospy.ROSInterruptException:
    pass


