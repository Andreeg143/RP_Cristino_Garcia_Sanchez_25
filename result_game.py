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
from rp_Cristino_Garcia_Sanchez_25.srv import GetUserScore   # ajusta el nombre del paquete si hace falta


class ResultGameSub(object):
    def __init__(self):
        self.score = None
        self.name = "none"
        self.age = 0
        self.username = "None"
        self.__sub_game = rospy.Subscriber("result_information", Int64, self.callback_game)
        self.__sub_user = rospy.Subscriber("user_information", user_msg, self.callback_user) 

        # Cliente del servicio user_score
        rospy.loginfo("[RESULT_GAME] Waiting for service 'user_score'...")
        rospy.wait_for_service("user_score")
        self.user_score_client = rospy.ServiceProxy("user_score", GetUserScore)
        rospy.loginfo("[RESULT_GAME] Connected to service 'user_score'.")


    def callback_game(self, msg):
        self.score = msg.data
        self.result_printed = False  # hay nuevo resultado, se puede volver a imprimir
        rospy.loginfo("Received message - score game: %d", msg.data) 
        self.print_result()

    def callback_user(self, msg):
        #self.name = msg.name
        #self.age = msg.age
        self.username = msg.username
        self.result_printed = False
        rospy.loginfo("Received message")
        rospy.loginfo("Username: %s", msg.username)
        self.print_result()
    
    def print_result(self):
        if self.result_printed:
            return  # ya hemos impreso este resultado

        if self.score is None or self.username is None:
            # todavía falta información
            return

        try:
            resp = self.user_score_client(self.username)
            self.percentage = resp.percentage
            rospy.loginfo("[RESULT_GAME] Service user_score: %s -> %.1f%%", self.username, self.percentage)
        except rospy.ServiceException as e:
            rospy.logwarn("Failed to call service user_score: %s", str(e))
            self.percentage = None

    
        rospy.loginfo("========================================")
        rospy.loginfo(" FINAL RESULT ")
        #rospy.loginfo("   Name    : %s", self.name)
        rospy.loginfo("   Username: %s", self.username)
        #rospy.loginfo("   Age     : %d", self.age)
        rospy.loginfo("   Score   : %d", self.score)
        if self.percentage is not None:
            rospy.loginfo("   Percentage : %.1f%%", self.percentage)
        rospy.loginfo("========================================")

        self.result_printed = True


        

if __name__ == "__main__":
    try:
        rospy.init_node("result_game")#preguntar que poner aqui
        rospy.loginfo("Node result game has started")
        robot = ResultGameSub()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass