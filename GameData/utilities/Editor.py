#Le importamos todas las configuraciones iniciales del archivo configuraciones
from .settings import *
from tkinter import filedialog

"#Clase editor creada para poder pasarle en un futuro todos los atributos para sus diversos métodos"
class Editor:
    #------------------------------------Atributos a usar:-------------------------------------------
    def __init__(self,matrix,Creador,Estado_Programa,filaname,zoom_level):
        self.matrix = matrix
        self.Creador = Creador
        self.Estado_Programa = Estado_Programa
        self.filaname = filaname
        self.zoom_level = zoom_level

    #Encargada de dibujar la pantalla en el medio de la pantalla
    def draw_grid(matrix):
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(PANTALLA, matrix[row][col], 
                                 (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                if LINEAS_CUADRICULA:            
                    pygame.draw.rect(PANTALLA, NEGRO, 
                                     (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
                if VER_MATRIZ_NUMERICA:
                    if matrix[row][col] == CELESTE:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("0", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    elif matrix[row][col] == AZUL:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("1", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    elif matrix[row][col] == VERDE:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("2", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    elif matrix[row][col] == TURQUESA:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("3", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    elif matrix[row][col] == ROSADO:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("4", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    elif matrix[row][col] == AMARILLO:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("5", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    elif matrix[row][col] == NARANJA:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("6", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    elif matrix[row][col] == ROJO:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("7", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    elif matrix[row][col] == CAFE:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("8", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    elif matrix[row][col] == NEGRO:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("9", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                
                elif VER_MODO_ASCII_ART:
                    if matrix[row][col] == CELESTE:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    elif matrix[row][col] == AZUL:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render(".", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    elif matrix[row][col] == VERDE:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render(":", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    elif matrix[row][col] == TURQUESA:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("-", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    elif matrix[row][col] == ROSADO:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("=", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    elif matrix[row][col] == AMARILLO:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("¡", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    elif matrix[row][col] == NARANJA:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("&", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    elif matrix[row][col] == ROJO:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("$", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    elif matrix[row][col] == CAFE:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("%", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    elif matrix[row][col] == NEGRO:
                        pygame.draw.rect(PANTALLA, BLANCO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("@", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)

                elif VER_ALTOCONTRASTE:
                    #--------------------Colores entre 0 y 4 convertidos a 1(Inicio)----------------------------
                    if matrix[row][col] == CELESTE:
                        pygame.draw.rect(PANTALLA, AZUL, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    
                    elif matrix[row][col] == AZUL:
                        pygame.draw.rect(PANTALLA, AZUL, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    
                    elif matrix[row][col] == VERDE:
                        pygame.draw.rect(PANTALLA, AZUL, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    
                    elif matrix[row][col] == TURQUESA:
                        pygame.draw.rect(PANTALLA, AZUL, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    
                    elif matrix[row][col] == ROSADO:
                        pygame.draw.rect(PANTALLA, AZUL, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    #--------------------Colores entre 0 y 4 convertidos a 1(End)----------------------------

                    #--------------------Colores entre 5 y 9 en 9(Inicio)------------------------------------
                    elif matrix[row][col] == AMARILLO:
                        pygame.draw.rect(PANTALLA, NEGRO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    
                    elif matrix[row][col] == NARANJA:
                        pygame.draw.rect(PANTALLA, NEGRO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    
                    elif matrix[row][col] == ROJO:
                        pygame.draw.rect(PANTALLA, NEGRO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    
                    elif matrix[row][col] == CAFE:
                        pygame.draw.rect(PANTALLA, NEGRO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

                    elif matrix[row][col] == NEGRO:
                        pygame.draw.rect(PANTALLA, NEGRO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    #--------------------Colores entre 5 y 9 en 9(End)------------------------------------

                #Nos encargamos de cambiar el valor actual por su contra parte, para poder mostrar el negativo.
                elif VER_NEGATIVO:
                    #De 9 a 0
                    if matrix[row][col] == NEGRO:
                        pygame.draw.rect(PANTALLA, CELESTE, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    #De 8 a 1
                    elif matrix[row][col] == CAFE:
                        pygame.draw.rect(PANTALLA, AZUL, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    #De 7 a 2
                    elif matrix[row][col] == ROJO:
                        pygame.draw.rect(PANTALLA, VERDE, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    #De 6 a 3
                    elif matrix[row][col] == NARANJA:
                        pygame.draw.rect(PANTALLA, TURQUESA, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    #De 5 a 4
                    elif matrix[row][col] == AMARILLO:
                        pygame.draw.rect(PANTALLA, ROSADO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    #De 4 a 5
                    elif matrix[row][col] == ROSADO:
                        pygame.draw.rect(PANTALLA, AMARILLO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    #De 3 a 6
                    elif matrix[row][col] == TURQUESA:
                        pygame.draw.rect(PANTALLA, NARANJA, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    #De 2 a 7
                    elif matrix[row][col] == VERDE:
                        pygame.draw.rect(PANTALLA, ROJO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    #De 1 a 8
                    elif matrix[row][col] == AZUL:
                        pygame.draw.rect(PANTALLA, CAFE, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)
                    #De 0 a 9
                    elif matrix[row][col] == CELESTE:
                        pygame.draw.rect(PANTALLA, NEGRO, (MatrizCentradaenX + col * CELL_SIZE, MatrizCentradaenY + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        text_surface = font.render("", True, NEGRO)
                        text_rect = text_surface.get_rect(center=(MatrizCentradaenX + col * CELL_SIZE + CELL_SIZE // 2, MatrizCentradaenY + row * CELL_SIZE + CELL_SIZE // 2))
                        PANTALLA.blit(text_surface, text_rect)

    def Guardar_Matriz(self,matrix, filename='matrix.txt'):
        with open(filename, 'w') as file:
            for row in matrix:
                file.write(' '.join([f'{cell[0]},{cell[1]},{cell[2]}' for cell in row]) + '\n')

    #Función encargada de activar el método "Ver matriz numérica"
    def Ver_Matriz_Numerica():
        global VER_MATRIZ_NUMERICA
        # Invertir el valor de la variable VER_MATRIZ_NUMERICA "Si recibe True, lo convierte en False y viceversa"
        VER_MATRIZ_NUMERICA = not VER_MATRIZ_NUMERICA
        return VER_MATRIZ_NUMERICA

    def Cerrar_Imagen(self):
        # Crear una matriz vacía del mismo tamaño que la matriz principal
        matriz_vacia = [[(223, 222, 219) for _ in range(COLS)] for _ in range(ROWS)]
        # Actualizar la matriz principal del editor con la matriz vacía
        self.matrix = matriz_vacia
        # Devolver la matriz vacía (aunque esto podría no ser necesario dependiendo de cómo se use esta función)
        return matriz_vacia

    def RotarDerecha(self,matrix):
        # Transponer la matriz y luego invertir cada fila
        matrix = [list(row)[::-1] for row in zip(*matrix)]
        return matrix

    def RotarIzquierda(self,matrix):
        # Transponer la matriz
        transposed = list(zip(*matrix))
        # Invertir el orden de las filas transpuestas
        rotated = transposed[::-1]
        # Convertir las tuplas en listas nuevamente
        rotated = [list(row) for row in rotated]
        # Actualizar la matriz actual con la rotación
        matrix = rotated
        return rotated

    def ReflejoHorizontal(self,matrix):    
        return matrix[::-1]

    def ReflejoVertical(self,matrix):    
        return [row[::-1] for row in matrix]

    def AltoContraste(self):
        global VER_ALTOCONTRASTE
        VER_ALTOCONTRASTE = not VER_ALTOCONTRASTE
        return VER_ALTOCONTRASTE

    def Negativo(self):
        global VER_NEGATIVO
        VER_NEGATIVO = not VER_NEGATIVO
        return VER_NEGATIVO

    def ASCII_ART():
        global VER_MODO_ASCII_ART
        # Invertir el valor de la variable VER_MATRIZ_NUMERICA "Si recibe True, lo convierte en False y viceversa"
        VER_MODO_ASCII_ART = not VER_MODO_ASCII_ART
        return VER_MODO_ASCII_ART

    def ZoomInyOUT(self, zoom_in, mouse_pos):
        global CELL_SIZE, MatrizCentradaenX, MatrizCentradaenY

        # Coordenadas del mouse respecto a la matriz
        mouseX, mouseY = mouse_pos
        matriz_mouseX = (mouseX - MatrizCentradaenX) / CELL_SIZE
        matriz_mouseY = (mouseY - MatrizCentradaenY) / CELL_SIZE

        # Ajustar el tamaño de las celdas
        if zoom_in and CELL_SIZE < 10:
            CELL_SIZE += 1
        elif not zoom_in and CELL_SIZE > 6:
            CELL_SIZE -= 1

        # Recalcular la posición centrada de la matriz
        calcular_matriz_centrada()

        # Ajustar la posición de la matriz para que el punto bajo el mouse permanezca fijo
        MatrizCentradaenX = mouseX - matriz_mouseX * CELL_SIZE
        MatrizCentradaenY = mouseY - matriz_mouseY * CELL_SIZE
    
    #Esta función se encarga de preguntar por la existencia de un archivo y si existe, lo carga.
    def pedir_y_cargar_archivo(self):
        # Mostrar un cuadro de diálogo para seleccionar el archivo
        archivo = filedialog.askopenfilename(title="Seleccionar archivo",
                                             initialdir=r'C:\Users\Anthony\Desktop\ProyectoV2',
                                             filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
        
        #Iteramos sobre el archivo, creamos una  nueva matriz, la retornamos, 
        #y en el bucle principal la igualamos a la actual para actualizar.
        if archivo:
            # Verificar si el archivo existe
            if os.path.exists(archivo):
                # Procesar el archivo seleccionado
                with open(archivo, 'r') as file:
                    new_matrix = []
                    for line in file:
                        new_row = []
                        for cell in line.strip().split(' '):
                            r, g, b = map(int, cell.split(','))
                            new_row.append((r, g, b))
                        new_matrix.append(new_row)
                return new_matrix
            else:
                print(f"El archivo {archivo} no existe.")
        else:
            print("No se seleccionó ningún archivo.")

    def permitirLineasCuadricula(self):
        global LINEAS_CUADRICULA
        LINEAS_CUADRICULA = not LINEAS_CUADRICULA
        return LINEAS_CUADRICULA