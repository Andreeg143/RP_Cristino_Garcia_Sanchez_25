#!/usr/bin/env python3

# Fase 2: game
# - Suscriber a "keyboard_control" (std_msgs/String)
# - Usa los mensajes para controlar el juego de Pygame en game.py

import rospy
from std_msgs.msg import String, Int64

import pygame
from game import FlappyBirdGame, GameState   # game.py en el mismo directorio

class GameNode(object):
    def __init__(self):
        # Nodo del juego de Flappy Bird
        self.game = FlappyBirdGame()

        # Bandera para indicar que ha llegado un SPACE por ROS
        self.jump_requested = False

        # (Fase 3 en el futuro) publisher del resultado
        self.pub_result = rospy.Publisher("result_information", Int64, queue_size=10)

        # Suscriptor al control del teclado (viene de control_node.py)
        self.sub_control = rospy.Subscriber(
            "keyboard_control",
            String,
            self.callback_control
        )

        rospy.loginfo("Game node listo. Controla el pájaro con SPACE desde control_node.")

    def callback_control(self, msg):
        """
        Callback que recibe mensajes del topic 'keyboard_control'.
        Espera cadenas tipo 'SPACE'.
        """
        rospy.loginfo("Mensaje de control recibido: %s", msg.data)

        if msg.data == "SPACE":
            # En vez de tocar el juego aquí (hilo de callback),
            # marcamos una bandera y lo aplicamos en el bucle principal.
            self.jump_requested = True

    def main_loop(self):
        """
        Bucle principal del juego:
        - Gestiona eventos de Pygame (cerrar ventana).
        - Aplica las órdenes recibidas por ROS.
        - Actualiza y dibuja el juego.
        """
        rate = rospy.Rate(60)  # 60 Hz, a juego con el clock del juego
        running = True

        while not rospy.is_shutdown() and running:
            # Gestionar eventos de Pygame (cerrar ventana, etc.)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rospy.loginfo("Ventana cerrada, saliendo del juego.")
                    running = False

            # Aplicar el SPACE que llegó por ROS
            if self.jump_requested:
                if self.game.game_state == GameState.START_SCREEN:
                    rospy.loginfo("SPACE -> Start game")
                    self.game.start_game()
                elif self.game.game_state == GameState.PLAYING:
                    rospy.loginfo("SPACE -> Jump")
                    self.game.bird.jump()
                elif self.game.game_state == GameState.GAME_OVER:
                    rospy.loginfo("SPACE -> Restart game")
                    self.game.restart_game()

                # Consumimos la orden
                self.jump_requested = False

            # Actualizar lógica del juego y dibujar
            self.game.update()
            self.game.draw()
            self.game.clock.tick(60)  # asegurar 60 FPS

            rate.sleep()

        # Si salimos del bucle
        pygame.quit()
        rospy.loginfo("Game node terminado.")

if __name__ == "__main__":
    rospy.init_node("game_node")
    rospy.loginfo("Game node ha arrancado.")
    node = GameNode()
    node.main_loop()