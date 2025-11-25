#!/usr/bin/env python3
#info_user.py -> publisher de la info del usuario
#info_user.py -> topic -> user_information
#info_user.py -> msg_type -> user_msg
#Belongs to phase 1

import rospy
import time

from std_msgs.msg import String
#from flappy_info.msg import user_msg #-> msg_type
#mirar el msg_type en el package.xml y preguntar a sara, al hacer catkin_make nos da error porq tenemos dos carpetas de tipo de mensaje

class InfoUserPub(object):
    def __init__(self):
        self.__pub = rospy.Publisher("user_information", String, queue_size=10)

        time.sleep(5)
        self.main()
    
    def get_user_info(self):
        while not rospy.is_shutdown():
            try:
                name = input("Enter your name: ")
                username = input("Enter your username: ")
                age = input("Enter your age: ")
        return name, username, age

    def main(self):
        user = user_msg()
        name, username, age = self.get_user_info()
        user.name = name
        user.username = username
        user.age = age
        
        rospy.sleep(5)
        self.__pub.publish("Hello from the publisher")
        self.__pub.publish(user)
        
if __name__ == "__main__":
    try:
        rospy.init_node("publisher_robot")
        #print("Node has started")
        rospy.loginfo("Node Publisher User Info has started")
        user = InfoUserPub()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass