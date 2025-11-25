#! /usr/bin/env python3

#Fase 1: welcome -> suscriber de info user con topic user_information y print the info
#Fase 2: game -> control del juego, flechitas, 
#               suscriber de node control_node 
#               topic keyboard_control
#               mensaje std_msgs/String -> Right, left, up, down ALL CAPITAL LETTERS, usamos space
#Fase 3: final -> final score
#                 publisher result_game
#                 topic result_information
#                 mensaje std_msgs/int64


import rospy
import time
from std_msgs.msg import Int64
from std_msgs.msg import String
#from flappy_info.msg import user_msg #-> msg_type

class Game(object):
    def __init__(self):
        self.__pub_result = rospy.Publisher("result_information", Int64, queue_size=10)
        self.__sub_user = rospy.Subscriber("user_information", user_msg, self.callback_user)
        self.__sub_control = rospy.Subscriber("keyboard_control", String, self.callback_control)

        rospy.loginfo("Starting the game")
        time.sleep(5)
        self.main()

    def callback_user(self, msg):
        rospy.loginfo("Received message")
        rospy.loginfo("Name: %s", msg.name)
        rospy.loginfo("Username: %s", msg.username)
        rospy.loginfo("Age: %s", msg.age)

    def callback_control(self, msg):
        rospy.loginfo("Received message")
        rospy.loginfo("Key Pressed: %s", msg.key)

    def phase1(self):
        #WELCOME
        #Welcome message 

        #read user information 

        #print name of the user

    
    def phase2(self):
        #main part of the game, here is where you play
        #control movements with arrow keys
        #read topic keyboard control from control node

        #y usarlo


    def phase3(self):
        #calculate the final score 
        
        #sends the information to the result_node through result_information

    def main(self):
        phase1 = self.phase1()
        phase2 = self.phase2()
        phase3 = self.phase3()
    

if __name__ == "__main__":
    try:
        rospy.init_node("result_game")#preguntar que poner aqui
        rospy.loginfo("Node result game has started")
        robot = ResultGameSub()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass


