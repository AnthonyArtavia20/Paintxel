#Importamos unas cuantas configuraciones...
import pygame.image
from .settings import *
from .Editor import *
from .assets import *

# Definir los botones a utilizar:
#Proporciones:
button_width, button_height = 75, 75


#---------------------------Botones derecha(Inicio)------------------------------------
#Sub derecha
boton_rosado = pygame.Rect(1100, 50, button_width, button_height)
boton_rojo = pygame.Rect(1100, 150, button_width, button_height)
boton_cafe = pygame.Rect(1100, 250, button_width, button_height)
boton_turquesa = pygame.Rect(1100, 350, button_width, button_height)
boton_negro = pygame.Rect(1100, 450, button_width, button_height)
#Sub izquierda
boton_azul = pygame.Rect(1000, 50, button_width, button_height)
boton_amarillo = pygame.Rect(1000, 150, button_width, button_height)
boton_naranja =pygame.Rect(1000, 250, button_width, button_height)
boton_celeste = pygame.Rect(1000, 350, button_width, button_height)
boton_verde = pygame.Rect(1000, 450, button_width, button_height)
#---------------------------Botones derecha(Fin)------------------------------------

#---------------------------Botones izquierda(Inicio)-------------------------------
#Algunos métedos:
boton_guardar = pygame.Rect(150, 500, button_width, button_height)
boton_cargar = pygame.Rect(50, 500, button_width, button_height)
boton_reflect_x = pygame.Rect(50, 100, button_width, button_height)
boton_reflect_y = pygame.Rect(150, 100, button_width, button_height)
boton_ASCII = pygame.Rect(50, 300, button_width, button_height)
boton_Aplicar_Negativo = pygame.Rect(50, 400, button_width, button_height)

#Botones de Rotación:
boton_rotar_izquierda = pygame.Rect(50, 200, button_width, button_height)
boton_rotar_derecha = pygame.Rect(150, 200, button_width, button_height)

#Boton de limpieza de matriz:
boton_limpiar_matriz = pygame.Rect(1000,550,button_width,button_height)

#Boton para matriz numérica:
boton_ver_MatrizNumerica = pygame.Rect(150,300,button_width,button_height)

#Boton para alto contraste:
boton_Alto_Contraste = pygame.Rect(150,400,button_width,button_height)

#Boton para controlar la aparición de la cuadrícula por pantalla:
boton_lineas_cuadricula = pygame.Rect(1100,550,button_width,button_height)

#---------------------------Botones izquierda(End)-------------------------------

"---------------------------------------------------------------------------------------------"
#Clase encargada de dibujar las imagenes sobre los botones:
# Definición de la clase ImagenBoton
class ImagenBoton:
    def __init__(self, image_path, x, y, width, height):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = pygame.Rect(x, y, width, height)

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect.topleft)



#Lista con lass Imagenes de los botones
botones = [
    ImagenBoton(os.path.join("utilities", "assets", "Save.png"), 150, 500, 75, 75),  # Save
    ImagenBoton(os.path.join("utilities", "assets", "load.PNG"), 50, 500, 75, 75),  # Cargar
    ImagenBoton(os.path.join("utilities", "assets", "voltear horizontal.png"), 150, 100, 75, 75),  # Reflect X
    ImagenBoton(os.path.join("utilities", "assets", "Voltear vertical.png"), 50, 100, 75, 75),  # Reflect Y
    ImagenBoton(os.path.join("utilities", "assets", "ascii.png"), 50, 300, 75, 75),  # ASCII
    ImagenBoton(os.path.join("utilities", "assets", "Negativo.png"), 50, 400, 75, 75),  # Aplicar Negativo
    ImagenBoton(os.path.join("utilities", "assets", "girar izquierda.png"), 50, 200, 75, 75),  # Rotar Izquierda
    ImagenBoton(os.path.join("utilities", "assets", "girar derecha DEF.png"), 150, 200, 75, 75),  # Rotar Derecha
    ImagenBoton(os.path.join("utilities", "assets", "Eraser.png"), 1000, 550, 75, 75),  # Limpiar Matriz
    ImagenBoton(os.path.join("utilities", "assets", "Ver_MatrizNumerica.png"), 150, 300, 75, 75),  # Ver Matriz Numérica
    ImagenBoton(os.path.join("utilities", "assets", "Alto Contraste.png"), 150, 400, 75, 75),  # Alto Contraste
    ImagenBoton(os.path.join("utilities", "assets", "Cuadricula.png"), 1100, 550, 75, 75),  # Alto Contraste


]

# Clase para la imagen del título y el autor
class ImagenTituloYautor:
    def __init__(self, image_path, x, y, width, height):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = pygame.Rect(x, y, width, height)

    def dibujar2(self, pantalla):
        pantalla.blit(self.image, self.rect.topleft)

# Lista con las imágenes del título y el autor
imgs = [
    ImagenTituloYautor(os.path.join("utilities", "assets", "Tittle.png"), 50, 5, 200, 75),  # Titulo
    ImagenTituloYautor(os.path.join("utilities", "assets", "Autor.png"), 12, 600, 270, 75),  # Autor
]




#Esta función es llamada al bucle principal para poder dibujar los botones
def draw_buttons():#Su función principal es la de otorgarle caracteristicas a rectángulos y así utilizarlos como botones.

    #----------------------------------Botones con colores-(Inicio)---------------------------------------------------
    pygame.draw.rect(PANTALLA, ROSADO, boton_rosado)
    pygame.draw.rect(PANTALLA, ROJO, boton_rojo)
    pygame.draw.rect(PANTALLA, CAFE, boton_cafe)
    pygame.draw.rect(PANTALLA, TURQUESA, boton_turquesa)
    pygame.draw.rect(PANTALLA, NEGRO, boton_negro)

    pygame.draw.rect(PANTALLA, AZUL, boton_azul)
    pygame.draw.rect(PANTALLA, AMARILLO, boton_amarillo)
    pygame.draw.rect(PANTALLA, NARANJA, boton_naranja)
    pygame.draw.rect(PANTALLA, CELESTE, boton_celeste)
    pygame.draw.rect(PANTALLA, VERDE, boton_verde)
    #----------------------------------Botones con colores-(Fin)---------------------------------------------------
    #----------------------------------Botones Métodos(Inicio)-----------------------------------------------------
    #Botones con caracteristicas especiales(Métodos)
    pygame.draw.rect(PANTALLA, BLANCO, boton_guardar)
    pygame.draw.rect(PANTALLA, BLANCO, boton_cargar)
    pygame.draw.rect(PANTALLA, BLANCO, boton_reflect_x)
    pygame.draw.rect(PANTALLA, BLANCO, boton_reflect_y)

    # Dibujar botones de zoom
    pygame.draw.rect(PANTALLA, BLANCO, boton_ASCII)
    pygame.draw.rect(PANTALLA, BLANCO, boton_Aplicar_Negativo)

    pygame.draw.rect(PANTALLA, BLANCO, boton_rotar_izquierda)
    pygame.draw.rect(PANTALLA, BLANCO, boton_rotar_derecha)

    #Boton para Alto Contraste:
    pygame.draw.rect(PANTALLA,BLANCO,boton_Alto_Contraste)

    pygame.draw.rect(PANTALLA,BLANCO,boton_limpiar_matriz)

    #Dibujar boton de ver matriz numérica
    pygame.draw.rect(PANTALLA,(234,210,143),boton_ver_MatrizNumerica)

    #Dibujar el botón que controla las lineas de la cuadrícula:
    pygame.draw.rect(PANTALLA,BLANCO,boton_lineas_cuadricula)
    #----------------------------------Botones Métodos(End)-----------------------------------------------------

    #Ciclo encargado de dibujar los botones
    for boton in botones:
        boton.dibujar(PANTALLA)
    
    
    for img in imgs:
        img.dibujar2(PANTALLA)

#Esta clase es meramente decorativa, sinver para decorar los botones con unos bordes.
class cuadros:
    #------------------------------------Atributos a usar:-------------------------------------------
    def __init__(self,x,y,color,ancho,alto,relleno):
        self.x = x
        self.y = y
        self.color = color
        self.ancho = ancho
        self.alto = alto
        self.relleno = relleno
    
    #-----------------------------------Métodos(Acciones) del Editor--------------------------------
    #Igual que anteriormente, esta función crea el botóm para luego poder dibujarlo en el bucle.
    def dibujarenPantalla(self,PANTALLA):
        pygame.draw.rect(PANTALLA,self.color,(self.x,self.y,self.ancho,self.alto),self.relleno)

