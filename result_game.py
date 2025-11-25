#!/usr/bin/env python3
#result_game.py -> suscriber del game_node -> topic -> result_information
#result_game.py -> suscriber del info_user -> topic -> user_information
#result_game.py -> msg_type -> std_msgs/int64 y user_msg
#imprime username and score
#Belongs to phase 2

import rospy
import time
from std_msgs.msg import Int64
#from flappy_info.msg import user_msg #-> msg_type


class ResultGameSub(object):
    def __init__(self):
        self.__sub_game = rospy.Subscriber("result_information", Int64, self.callback_game)
        self.__sub_user = rospy.Subscriber("user_information", user_msg, self.callback_user) #asegurar nombre tipo de mensaje

    def callback_game(self, msg):
        rospy.loginfo("Received message - score game: %i", msg) #revisar

    def callback_user(self, msg):
        rospy.loginfo("Received message")
        rospy.loginfo("Username: %s", msg.username)
        

if __name__ == "__main__":
    try:
        rospy.init_node("result_game")#preguntar que poner aqui
        rospy.loginfo("Node result game has started")
        robot = ResultGameSub()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass