#!/usr/bin/env python3
#control_node.py -> publisher del game_node
#control_node.py -> topic -> keyboard_control
#info_user.py -> msg_type -> std_msgs/String
#Belongs to phase 2

import rospy
import time
import sys, select, termios, tty 
from std_msgs.msg import String

settings = termios.tcgetattr(sys.stdin)

class ControlNodePub(object):
    def __init__(self):
        self.__pub = rospy.Publisher("keyboard_control", String, queue_size=10)
        rospy.loginfo("Wait 5 seconds to start the control")
        time.sleep(5)
        self.main()
    
    def get_key(self):
        #como lo hacemos

    def main(self):
        key = 
        
        rospy.sleep(5)
        self.__pub.publish("Hello control node from the publisher")
        self.__pub.publish(key)
        
if __name__ == "__main__":
    try:
        rospy.init_node("publisher_robot")
        #print("Node has started")
        rospy.loginfo("Node Publisher Keyboard Control Node has started")
        user = ControlNodePub()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass