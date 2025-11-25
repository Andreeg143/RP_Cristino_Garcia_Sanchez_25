#!/usr/bin/env python3
#result_game.py -> suscriber del game_node -> topic -> result_information
#result_game.py -> suscriber del info_user -> topic -> user_information
#result_game.py -> msg_type -> std_msgs/int64 y user_msg
#imprime username and score
#Belongs to phase 2

import rospy
import time
from std_msgs.msg import Int64
from flappy_info_msgs.msg import user_msg   #-> msg_type


class ResultGameSub(object):
    def __init__(self):
        self.score = None
        self.name = "none"
        self.age = 0
        self.username = "None"
        self.__sub_game = rospy.Subscriber("result_information", Int64, self.callback_game)
        self.__sub_user = rospy.Subscriber("user_information", user_msg, self.callback_user) 

    def callback_game(self, msg):
        self.score = msg.data
        rospy.loginfo("Received message - score game: %d", msg.data) 
        self.print_result()

    def callback_user(self, msg):
        #self.name = msg.name
        #self.age = msg.age
        self.username = msg.username
        rospy.loginfo("Received message")
        rospy.loginfo("Username: %s", msg.username)
        self.print_result()
    
    def print_result(self):
        if self.score is not None and self.username != "unknown":
            rospy.loginfo("========================================")
            rospy.loginfo(" FINAL RESULT ")
            #rospy.loginfo("   Name    : %s", self.name)
            rospy.loginfo("   Username: %s", self.username)
            #rospy.loginfo("   Age     : %d", self.age)
            rospy.loginfo("   Score   : %d", self.score)
            rospy.loginfo("========================================")

        

if __name__ == "__main__":
    try:
        rospy.init_node("result_game")#preguntar que poner aqui
        rospy.loginfo("Node result game has started")
        robot = ResultGameSub()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass