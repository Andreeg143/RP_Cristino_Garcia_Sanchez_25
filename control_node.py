#!/usr/bin/env python3
#AUTHORS: 
#ANA CRISTINO PRIETO
#ANDREA GARCIA RUIZ
#PAULA SANCHEZ SANZ

#control_node.py -> publisher in game_node
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
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        key = ''

        if rlist:
            key = sys.stdin.read(1)

        # Restore configuration of the terminal
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key

    def main(self):
        rospy.loginfo("Keyboard control started. Press space to jump")
        rate=rospy.Rate(20)
        
        while not rospy.is_shutdown():
            key = self.get_key()

            # if CTRL+C is pressed, get out of the loop
            if key == '\x03':
                rospy.loginfo("CTRL+C detected, exiting keyboard control loop.")
                break

            # If SPACE key is pressed, topic is published
            if key == ' ':
                msg = String()
                msg.data = "SPACE"  
                self.__pub.publish(msg)
                rospy.loginfo("Published key: %s", msg.data)

            # R -> complete reset of phase 1
            elif key in ('r', 'R'):
                msg = String()
                msg.data = "R"
                self.__pub.publish(msg)
                rospy.loginfo("Published key: %s (reset to phase 1)", msg.data)


            rate.sleep()
        
        rospy.sleep(5)
       
        
if __name__ == "__main__":
    try:
        rospy.init_node("control_node")
        #print("Node has started")
        rospy.loginfo("Node Publisher Keyboard Control Node has started")
        user = ControlNodePub()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    finally:
        # To always restore the terminal
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
