import pygame
# Inicialización de Pygame
pygame.init()
import os #Para poder buscar en el sistema

ANCHO_PANTALLA, ALTO_PANTALLA = 1200, 680
PANTALLA = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Paintxel")

FPS = 120


# Crear una fuente para mostrar el número
font = pygame.font.Font(None, 20)

#Lineas de la cuadrícula:
LINEAS_CUADRICULA = True

#Permite ver la matriz numérica, es decir los valores del 0 al 9 según el color y su intensidad.
VER_MATRIZ_NUMERICA = False

#Permite convertir todos los valores números en caracteres para hacer ASCII_ART
VER_MODO_ASCII_ART = False

#Permite activar la función que intercambia los valores según corresponda para así dar efecto de Alto Contraste
VER_ALTOCONTRASTE = False

#Permite activar la función encagada de dar el efecto Negativo
VER_NEGATIVO = False

#-------------------------- Paleta de Colores(Inicio)--------------------------
BLANCO = (255, 255, 255)
ROSADO = (231, 33, 216)
VERDE = (0,255,0)
ROJO = (255,0,0)
AMARILLO = (253, 240, 36)
NARANJA = (211, 84, 0)
TURQUESA = (13, 216, 142)
CELESTE = (4, 249, 253)
AZUL = (0,0,255)
NEGRO = (0,0,0)
CAFE  = (139, 61, 0)
GRIS = (117, 116, 113)
COLORFONDO = (216, 215, 213)
#-------------------------- Paleta de Colores(Final)--------------------------

# Variables de color actual
ColorDeDibujado_Actual = ROJO

# Definir el tamaño de la matriz (Controlable 100%)
ROWS = COLS = 120  # Número de filas y columnas
CELL_SIZE = 6      # Tamaño de cada celda en píxeles


# Nivel de zoom inicial
zoom_level = 1
def calcular_matriz_centrada():
    global MatrizCentradaenX, MatrizCentradaenY
    ancho_matriz = COLS * CELL_SIZE * zoom_level
    alto_matriz = ROWS * CELL_SIZE * zoom_level
    MatrizCentradaenX = (ANCHO_PANTALLA - ancho_matriz) // 2
    MatrizCentradaenY = (ALTO_PANTALLA - alto_matriz) // 2

calcular_matriz_centrada()