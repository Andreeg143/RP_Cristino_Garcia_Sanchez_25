#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class GameNode(object):
    def __init__(self):
        # Suscriber a las teclas del control_node
        self.sub_control = rospy.Subscriber(
            "keyboard_control",
            String,
            self.callback_control
        )

        rospy.loginfo("Game node waiting for SPACE key presses...")

    def callback_control(self, msg):
        """
        Callback para recibir 'SPACE'
        """
        rospy.loginfo("Received control message")
        rospy.loginfo("Key Pressed: %s", msg.data)

        # Debug simple: solo imprimir SPACE
        if msg.data == "SPACE":
            rospy.loginfo(">>> SPACE received! (DEBUG OK)")

if __name__ == "__main__":
    rospy.init_node("game_node")
    rospy.loginfo("Game node has started")

    node = GameNode()
    rospy.spin()