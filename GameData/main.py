#Importamos todo el paquete con las configuraciones, botones y demás.
from utilities import *
# Crear una matriz para almacenar los colores de las celdas
#Inicializamos llenando una lista con pequeñas sublistas llenas de un color para representar su color
#Estos fors lo que hacen es inicializar a crear HASTA el límite que son las columnas y filas.
matrix = [[(223, 222, 219) for _ in range(COLS)] for _ in range(ROWS)]

#Instancia del editor para poder pasar la matrix.
editor = Editor(matrix, None, None, None, None) 

#Función encargada de dibujar todo por pantalla
def dibujarCosas(listaconbotones):
    for cuadros in listaconbotones:
        cuadros.dibujarenPantalla(PANTALLA)

ListaConLosBordesDeLosBotones = [
    #Sintanxys de cuadros= X,Y,color,ancho,alto,relleno
    #-----------BOTONES DE COLORES(INICIO)----------
    #Botones que están en la sub derecha:
    cuadros(1095,45,GRIS,85,85,0),
    cuadros(1095,145,GRIS,85,85,0),
    cuadros(1095,245,GRIS,85,85,0),
    cuadros(1095,345,GRIS,85,85,0),
    cuadros(1095,445,GRIS,85,85,0),
    cuadros(1095,545,GRIS,85,85,0),
    #Botones que están en la sub Izquierda:
    cuadros(995,45,GRIS,85,85,0),
    cuadros(995,145,GRIS,85,85,0),
    cuadros(995,245,GRIS,85,85,0),
    cuadros(995,345,GRIS,85,85,0),
    cuadros(995,445,GRIS,85,85,0),
    cuadros(995,545,GRIS,85,85,0),
    #-----------BOTONES DE COLORES(END)----------

    #-----------BOTONES DE MÉTODOS(INICIO)-----------
    #Botones que están en la sub derecha:
    cuadros(145,95,GRIS,85,85,0),
    cuadros(145,195,GRIS,85,85,0),
    cuadros(145,295,GRIS,85,85,0),
    cuadros(145,395,GRIS,85,85,0),
    cuadros(145,495,GRIS,85,85,0),

    #Botones que están en la Sub Izquierda:
    cuadros(45,95,GRIS,85,85,0),
    cuadros(45,195,GRIS,85,85,0),
    cuadros(45,295,GRIS,85,85,0),
    cuadros(45,395,GRIS,85,85,0),
    cuadros(45,495,GRIS,85,85,0),

    #-----------BOTONES DE MÉTODOS(END)-----------
]

# Bucle principal
ejecutar = True
clock = pygame.time.Clock()
while ejecutar:
    clock.tick(FPS)

    #Controlamos los eventos desde aquí:
    for event in pygame.event.get():
        PANTALLA.fill(COLORFONDO)
        if event.type == pygame.QUIT:
            ejecutar = False
        
        #Registramos los clicks del ratón, precisamente el click izquierdo "[0]"
        elif pygame.mouse.get_pressed()[0]:

            #----------------------------------Colores(Inicio)-------------------------------------------------
            mouseX, mouseY = pygame.mouse.get_pos() #Extraemos la posición actual como X y Y, 
            if boton_rojo.collidepoint(mouseX, mouseY):
                ColorDeDibujado_Actual = ROJO
            elif boton_rosado.collidepoint(mouseX,mouseY):
                ColorDeDibujado_Actual = ROSADO
            elif boton_verde.collidepoint(mouseX, mouseY):
                ColorDeDibujado_Actual = VERDE
            elif boton_cafe.collidepoint(mouseX,mouseY):
                ColorDeDibujado_Actual = CAFE
            elif boton_turquesa.collidepoint(mouseX,mouseY):
                ColorDeDibujado_Actual = TURQUESA
            elif boton_negro.collidepoint(mouseX,mouseY):
                ColorDeDibujado_Actual = NEGRO
            elif boton_azul.collidepoint(mouseX,mouseY):
                ColorDeDibujado_Actual = AZUL
            elif boton_amarillo.collidepoint(mouseX,mouseY):
                ColorDeDibujado_Actual = AMARILLO
            elif boton_naranja.collidepoint(mouseX,mouseY):
                ColorDeDibujado_Actual = NARANJA
            elif boton_celeste.collidepoint(mouseX,mouseY):
                ColorDeDibujado_Actual = CELESTE
            #----------------------------------Colores(End)-------------------------------------------------

            #----------------------------------Botones métodos(Inicio)-------------------------------------------------
            elif boton_guardar.collidepoint(mouseX, mouseY):
                Editor.Guardar_Matriz(Editor,matrix)

            elif boton_cargar.collidepoint(mouseX, mouseY):
                matrix = Editor.pedir_y_cargar_archivo(Editor)

            elif boton_reflect_x.collidepoint(mouseX, mouseY):
                matrix = Editor.ReflejoHorizontal(Editor,matrix)

            elif boton_reflect_y.collidepoint(mouseX, mouseY):
                matrix = Editor.ReflejoVertical(Editor,matrix)

            elif boton_Aplicar_Negativo.collidepoint(mouseX, mouseY):
                Editor.Negativo(Editor)

            elif boton_limpiar_matriz.collidepoint(mouseX,mouseY):
                matrix = Editor.Cerrar_Imagen(Editor)
                
            elif boton_rotar_derecha.collidepoint(mouseX,mouseY):
                matrix = Editor.RotarDerecha(Editor,matrix)

            elif boton_ASCII.collidepoint(mouseX,mouseY):
                print("Modo ASCII")
                VER_MODO_ASCII_ART = Editor.ASCII_ART()

            elif boton_ver_MatrizNumerica.collidepoint(mouseX,mouseY):
                print("Modo Matriz númerica")
                VER_MATRIZ_NUMERICA = Editor.Ver_Matriz_Numerica()

            elif boton_rotar_izquierda.collidepoint(mouseX,mouseY):
                matrix = Editor.RotarIzquierda(Editor,matrix)  # Aplicar la rotación izquierda
                
            
            elif boton_Alto_Contraste.collidepoint(mouseX,mouseY):
                VER_ALTOCONTRASTE = Editor.AltoContraste(Editor)
                print(VER_ALTOCONTRASTE)
            
            elif boton_lineas_cuadricula.collidepoint(mouseX,mouseY):
                LINEAS_CUADRICULA = Editor.permitirLineasCuadricula(Editor)

            else:
                #Si no hay colisión con nigún botón, significa que podemos dibujar, entonces estamos dibujando sobre la matriz
                mouseX_matriz = (mouseX - MatrizCentradaenX) * zoom_level
                mouseY_matriz = (mouseY - MatrizCentradaenY) * zoom_level
                columnaActual = mouseX_matriz // (CELL_SIZE * zoom_level)
                filaActual = mouseY_matriz // (CELL_SIZE * zoom_level)
                if 0 <= columnaActual < COLS and 0 <= filaActual < ROWS:
                    matrix[filaActual][columnaActual] = ColorDeDibujado_Actual  # Cambiar el color de la celda al color actual
            #----------------------------------Botones métodos(End)-------------------------------------------------
        #Si se detecta el movimiento de la rueda del ratón, entonces hacemos condicionales para determinar si está decreciendo
        #o incrementando. LLamamos a la función encargada del zoom y le pasamos como parametros la posición del mouse y la condició
        elif event.type == pygame.MOUSEWHEEL:
            mouseX, mouseY = pygame.mouse.get_pos()
            if event.y > 0:  # Rueda hacia arriba
                editor.ZoomInyOUT(True, (mouseX, mouseY))
            elif event.y < 0:  # Rueda hacia abajo
                editor.ZoomInyOUT(False, (mouseX, mouseY))


    Editor.draw_grid(matrix) #Se cargada de dibujar la matriz según las proporciones dadas.
    marco2 = pygame.Rect(0,0,300,800)
    pygame.draw.rect(PANTALLA, (200, 179, 114 ), marco2)
    
    pygame.draw.rect(PANTALLA, NEGRO, (297,40,603,800),6)
    marco2 = pygame.Rect(900,0,300,800)
    pygame.draw.rect(PANTALLA, (200, 179, 114 ), marco2)
    dibujarCosas(ListaConLosBordesDeLosBotones)
    draw_buttons() #Se encuentra en el documento de botones, se encarga de dibujar dichos elementos

    marco1 = pygame.Rect(300,0,1200,40)
    pygame.draw.rect(PANTALLA, (200, 179, 114 ), marco1)
    pygame.display.update()

pygame.quit()
