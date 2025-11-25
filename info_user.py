#!/usr/bin/env python3
# info_user.py -> publisher de la info del usuario
# info_user.py -> topic -> user_information
# info_user.py -> msg_type -> user_msg
# Belongs to phase 1

import rospy
import time

from std_msgs.msg import String
from flappy_info_msgs.msg import user_msg  # -> msg_type
# mirar el msg_type en el package.xml y preguntar a sara, al hacer catkin_make
# nos da error porque tenemos dos carpetas de tipo de mensaje


class InfoUserPub(object):
    def __init__(self):
        self.__pub = rospy.Publisher("user_information", user_msg, queue_size=10)

        time.sleep(2)
        self.main()

    def get_user_info(self):
        while not rospy.is_shutdown():
            try:
                name = input("Enter your name: ")
                username = input("Enter your username: ")
                age = input("Enter your age: ")
                return name, username, age
            except KeyboardInterrupt:
                break

    def main(self):
        user = user_msg()
        name, username, age = self.get_user_info()
        user.name = name
        user.username = username

        # convertir edad
        try:
            user.age = int(age)
        except ValueError:
            rospy.logwarn("Age is not a number")
            user.age = 0

        rospy.loginfo(
            "User Information: Name = %s, Username = %s, Age = %d",
            user.name, user.username, user.age
        )

        rospy.sleep(1)
        self.__pub.publish(user)


if __name__ == "__main__":
    try:
        rospy.init_node("info_user")
        rospy.loginfo("Node Publisher User Info has started")
        user = InfoUserPub()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
