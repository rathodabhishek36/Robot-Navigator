#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def create_callback(publisher):
    
    
    def callback(data):
        """
        Called when we get a message of the laser reading
        """
        wall_distance = data.ranges[319] # get the wall distance
        if wall_distance < 0.5:
            move = Twist()
            move.angular.z = 0.5
            publisher.publish(move)


    return callback

def wall_avoider():
    """
    A node to tell the turtle bot to avoid walls
    """

    rospy.init_node('avoid_wall_node', anonymous=False)

    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)    
    
    rospy.Subscriber("/scan", LaserScan, create_callback(pub))
    


    rospy.spin()
    # rate = rospy.Rate(2)

    # while not rospy.is_shutdown(): # continuously send messages till the master is running


if __name__ == "__main__":
    wall_avoider()