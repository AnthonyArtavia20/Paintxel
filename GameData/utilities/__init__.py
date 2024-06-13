#Importamos todas las configuraciones iniciales de los todos los subarhivos:
#Esto con la finalidad de hacer un paquete que tenga todo junto, de manera que 
#lo llamemos al Main y todo llegue junto ahí.

from .settings import * #Importamos todas las configuraciones iniciales
from .buttons import * #Importamos todos los botones y sus funciones
from .Editor import * #Importamos toda la configuración del Editor, es decir, como se dibuja su matriz


#Inicializamos pygame
import pygame
pygame.init()
pygame.font.init()


