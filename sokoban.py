"""
Author: Jesus Bautista Hernandez
Grupo: TI22
      #0 = muñeco - 
      #1 = espacio
      #2 = caja - 
      #3 = paredes
      #4 = metas
      #5 = muñeco_meta
      #6 = caja_meta

      intrucciones
      d-Derecha
      i-Izquierda
      a-Arriba
      h-Abajo
      q-Salir
"""
  # Librerias nesesarias para la funcion clear 
import platform
import os
  # Libreria numpy que nos permite trabajar con arrays de manera mas sencilla
import  numpy as np
class Sokoban:
  # Iniciacilizacion de variables usadas en las funciones siguientes 
  archivo = ""
  columnas = 0
  filas = 0
  mapa = []
  nivel = 'level0.txt'
  complet = False
  
  # Metodo constructor 
  def __init__(self):
        """_summary_: Constructor"""
        pass
    
  # Metodo responsale de la carga del archivo de texto  
  def loadFile(self):
    # Obtenemos el numero de columnas o el largo que tiene la primera fila de nuestro archivo
    with open(self.nivel) as f:
      colum = f.readline().rstrip()
    self.columnas = len(colum)
    
  # Metodo encontrar filas, devuelve el numero de filas de nuestro archivo
  def findColumnasFilas(self):
    fichero = open(self.nivel, 'r') 
    fichero.readline()
    fichero.seek(0)
    self.filas = len(fichero.readlines())
    
  # Metodo convertirFile, este metodo convierte nuestro archivo.txt en un aray
  def convertirFile(self):
  # Cargar Archivo
    self.archivo = open(self.nivel, 'r')
    self.hola = self.archivo.read()
    texto=[]
    # Obtenemos los valores del archivo y se los asignamos a la lista texto, asu ves que convertimos los valores a int
    for i in self.hola:
      texto+=i.rstrip()
    for k in range(len(texto)):
      texto[k] = int(texto[k])
    # Conversion de la variable texto a array con la funcion numpy, pasandole como limtes: filas, columnas  
    self.mapa = np.array(texto).reshape(self.filas,self.columnas)

  # Metodo findPositon, devuelve la posicion de nuestro personaje en el mapa
  def findPosition(self):
    result = np.where(self.mapa == 0)
    self.muneco_fila=result[0]
    self.muneco_columna=result[1]
    
  # Metodo printMao, imprime el mapa segun las condiciones incicadas
  def printMap(self):
    # Inicialisamos la variable contador, esta variable contara el numero de 2/cajas del mapa con el fin de ayudarnos a detectar si el nivel esta completado
    contador = 0
    for j in range(self.filas):
      for i in range(self.columnas):
        if self.mapa[j][i] == 0: # Si encuentra un numero 0 -  personaje
          print("🤖", end = "")
        elif self.mapa[j][i] == 1: # Si encuentra un numero 1 -  espacio
          print("  ", end = "")
        elif self.mapa[j][i] == 2: # Si encuentra un numero 2-  caja
          # cada que se encuentre un 2 en el mapa, contador incrementa su valor
          contador+=1
          print("🧰", end = "") 
        elif self.mapa[j][i] == 3: # Si encuentra un numero 3 - pared
          print("🔳", end = "")
        elif self.mapa[j][i] == 4: # Si encuentra un numero 4 - meta
          print("⛳", end = "")  
        elif self.mapa[j][i] == 5: # Si encuentra un numero 5 - muneco_meta
          print("🔰", end = "")
        elif self.mapa[j][i] == 6: # Si encuentra un numero 6 -  persojae_meta
          print("🏆", end = "")      
        else: # Si no se cumplen las condiciones anteriores, imprime el valor de la posicion
          print(self.mapa[j][i], end=" ")
      print() # Imprime una linea vacia 
    print() # Imprime una linea vacia 

    # Si contador es igual a 0; devuelve True
    if contador == 0:
      self.complet = True
    else: # Si no es el caso; devuelve False
      self.complet = False

  # Metodo limpiarPantalla, este metodo nos hace una limpieza de la pantalla/terminal
  def limpiarPantalla(self):
    if platform.system()=='Windows':
      os.system('cls')
    else:
      os.system('clear')

  # Metodo moverDerecha
  def moverDerecha(self):
    #5.- Personaje, espacio 
    if self.mapa[self.muneco_fila,self.muneco_columna]== 0 and self.mapa[self.muneco_fila,self.muneco_columna+1]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila,self.muneco_columna+1]=0
      self.muneco_columna+=1
     #6.-Personaje, meta    
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila,self.muneco_columna+1]=5
      self.muneco_columna+=1
      #7.-Personaje, caja, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==2 and self.mapa[self.muneco_fila,self.muneco_columna+2]==1 :
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila,self.muneco_columna+1]=0
      self.mapa[self.muneco_fila,self.muneco_columna+2]=2
      self.muneco_columna+=1
      #8.-Personaje, caja, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==2 and self.mapa[self.muneco_fila,self.muneco_columna+2]==4 :
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila,self.muneco_columna+1]=0
      self.mapa[self.muneco_fila,self.muneco_columna+2]=6
      self.muneco_columna+=1
      #9.-Personaje, caja_meta, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==6 and self.mapa[self.muneco_fila,self.muneco_columna+2]==1 :
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila,self.muneco_columna+1]=5
      self.mapa[self.muneco_fila,self.muneco_columna+2]=2
      self.muneco_columna+=1
      #10.-Personaje, caja_meta, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==6 and self.mapa[self.muneco_fila,self.muneco_columna+2]==4 :
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila,self.muneco_columna+1]=5
      self.mapa[self.muneco_fila,self.muneco_columna+2]=6
      self.muneco_columna+=1
      #11.-Personaje_meta, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila,self.muneco_columna+1]=0
      self.muneco_columna+=1
      #12.-Personaje_meta, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila,self.muneco_columna+1]=5
      self.muneco_columna+=1
      #13.-Personaje_meta, caja, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==2 and self.mapa[self.muneco_fila,self.muneco_columna+2]==1 :
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila,self.muneco_columna+1]=0
      self.mapa[self.muneco_fila,self.muneco_columna+2]=2
      self.muneco_columna+=1
      #14.-Personaje_meta, caja, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==2 and self.mapa[self.muneco_fila,self.muneco_columna+2]==4 :
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila,self.muneco_columna+1]=0
      self.mapa[self.muneco_fila,self.muneco_columna+2]=6
      self.muneco_columna+=1
  
      #15.-Personaje_meta, caja_meta, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==6 and self.mapa[self.muneco_fila,self.muneco_columna+2]==1 :
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila,self.muneco_columna+1]=5
      self.mapa[self.muneco_fila,self.muneco_columna+2]=2
      self.muneco_columna+=1
        #16.-Personaje_meta, caja_meta, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==6 and self.mapa[self.muneco_fila,self.muneco_columna+2]==4 :
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila,self.muneco_columna+1]=5
      self.mapa[self.muneco_fila,self.muneco_columna+2]=6
      self.muneco_columna+=1

  # Metodo moverIzquierda     
  def moverIzquierda(self):
    if self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==1:
      self.mapa[self.muneco_fila,self.muneco_columna-1]=0
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.muneco_columna-=1
    #18.- Personaje, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==4:
      self.mapa[self.muneco_fila,self.muneco_columna-1]=5
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.muneco_columna-=1
    #19.-Personaje, caja, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==2 and self.mapa[self.muneco_fila,self.muneco_columna-2]==1 :
      self.mapa[self.muneco_fila,self.muneco_columna-1]=0
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila,self.muneco_columna-2]=2
      self.muneco_columna-=1
     #20.-Personaje, caja, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==2 and self.mapa[self.muneco_fila,self.muneco_columna-2]==4 :
      self.mapa[self.muneco_fila,self.muneco_columna-1]=0
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila,self.muneco_columna-2]=6
      self.muneco_columna-=1
    #21.-Personaje, caja_meta, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==6 and self.mapa[self.muneco_fila,self.muneco_columna-2]==1 :
      self.mapa[self.muneco_fila,self.muneco_columna-1]=5
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila,self.muneco_columna-2]=2
      self.muneco_columna-=1
    #22.-Personaje, caja_meta, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==6 and self.mapa[self.muneco_fila,self.muneco_columna-2]==4 :
      self.mapa[self.muneco_fila,self.muneco_columna-1]=5
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila,self.muneco_columna-2]=6
      self.muneco_columna-=1
    #23.-Personaje_meta, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==1:
      self.mapa[self.muneco_fila,self.muneco_columna-1]=0
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.muneco_columna-=1
    #24.-Personaje_meta, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==4:
      self.mapa[self.muneco_fila,self.muneco_columna-1]=5
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.muneco_columna-=1
    #25.-Personaje_meta, caja, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==2 and self.mapa[self.muneco_fila,self.muneco_columna-2]==1 :
      self.mapa[self.muneco_fila,self.muneco_columna-1]=0
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila,self.muneco_columna-2]=2
      self.muneco_columna-=1
    #26.-Personaje_meta, caja, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]==5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==2 and self.mapa[self.muneco_fila,self.muneco_columna-2]==4 :
      self.mapa[self.muneco_fila,self.muneco_columna-1]=0
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila,self.muneco_columna-2]=6
      self.muneco_columna-=1
    #27.-Personaje_meta, caja_meta, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==6 and self.mapa[self.muneco_fila,self.muneco_columna-2]==1 :
      self.mapa[self.muneco_fila,self.muneco_columna-1]=5
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila,self.muneco_columna-2]=2
      self.muneco_columna-=1
    #28.-Personaje_meta, caja_meta, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==6 and self.mapa[self.muneco_fila,self.muneco_columna-2]==4 :
      self.mapa[self.muneco_fila,self.muneco_columna-1]=5
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila,self.muneco_columna-2]=6
      self.muneco_columna-=1

  # Metodo moverArriba
  def moverArriba(self):
    #29.- Espacio
        #Personaje 
    if self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila-1,self.muneco_columna]=0
      self.muneco_fila-=1
    #30.- Meta
        #Personaje 
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila-1,self.muneco_columna]=5
      self.muneco_fila-=1
    #31.- Espacio
        #Caja
        #Personaje
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==2 and  self.mapa[self.muneco_fila-2,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila-1,self.muneco_columna]=0
      self.mapa[self.muneco_fila-2,self.muneco_columna]=2
      self.muneco_fila-=1
    #32.- Meta
        #Caja
        #Personaje
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==2 and  self.mapa[self.muneco_fila-2,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila-1,self.muneco_columna]=0
      self.mapa[self.muneco_fila-2,self.muneco_columna]=6
      self.muneco_fila-=1
    #33.- Espacio
        #Caja_meta
        #Personaje
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==6 and  self.mapa[self.muneco_fila-2,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila-1,self.muneco_columna]=5
      self.mapa[self.muneco_fila-2,self.muneco_columna]=2
      self.muneco_fila-=1
    #34.- Meta
        #Caja_meta
        #Personaje
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==6 and  self.mapa[self.muneco_fila-2,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila-1,self.muneco_columna]=5
      self.mapa[self.muneco_fila-2,self.muneco_columna]=6
      self.muneco_fila-=1
    #35.- Espacio
        #Personaje_meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila-1,self.muneco_columna]=0
      self.muneco_fila-=1
   #36.- Meta
        #Personaje_meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila-1,self.muneco_columna]=5
      self.muneco_fila-=1
    #37.- Espacio
        #Caja
        #Personaje_meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==2 and  self.mapa[self.muneco_fila-2,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila-1,self.muneco_columna]=0
      self.mapa[self.muneco_fila-2,self.muneco_columna]=2
      self.muneco_fila-=1
    #38.- Meta
        #Caja
        #Personaje_meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==2 and  self.mapa[self.muneco_fila-2,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila-1,self.muneco_columna]=0
      self.mapa[self.muneco_fila-2,self.muneco_columna]=6
      self.muneco_fila-=1     
    #39.- Espacio
        #Caja_meta
        #Personaje_meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==6 and  self.mapa[self.muneco_fila-2,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila-1,self.muneco_columna]=5
      self.mapa[self.muneco_fila-2,self.muneco_columna]=2
      self.muneco_fila-=1         
    #40.- Meta
        #Caja_meta
        #Personaje_meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==6 and  self.mapa[self.muneco_fila-2,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila-1,self.muneco_columna]=5
      self.mapa[self.muneco_fila-2,self.muneco_columna]=6
      self.muneco_fila-=1     

  # Metodo moverAbajo
  def moverAbajo(self):
    #41.- Espacio
        #Personaje 
    if self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila+1,self.muneco_columna]=0
      self.muneco_fila+=1 
    #42.- Personaje
        #Meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila+1,self.muneco_columna]=5
      self.muneco_fila+=1  
   #43.- Personaje
        #Caja
        #Espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==2 and  self.mapa[self.muneco_fila+2,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila+1,self.muneco_columna]=0
      self.mapa[self.muneco_fila+2,self.muneco_columna]=2
      self.muneco_fila+=1       
   #44.- Personaje
        #Caja
        #Meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==2 and  self.mapa[self.muneco_fila+2,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila+1,self.muneco_columna]=0
      self.mapa[self.muneco_fila+2,self.muneco_columna]=6
      self.muneco_fila+=1 
   #45.- Personaje
        #Caja_meta
        #Espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==6 and  self.mapa[self.muneco_fila+2,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila+1,self.muneco_columna]=5
      self.mapa[self.muneco_fila+2,self.muneco_columna]=2
      self.muneco_fila+=1 
   #46.- Personaje
        #Caja_meta
        #Meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==6 and  self.mapa[self.muneco_fila+2,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila+1,self.muneco_columna]=5
      self.mapa[self.muneco_fila+2,self.muneco_columna]=6
      self.muneco_fila+=1       
    #47.- Personaje_meta
        #Espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila+1,self.muneco_columna]=0
      self.muneco_fila+=1         
    #48.- Personaje_meta
        #Meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila+1,self.muneco_columna]=5
      self.muneco_fila+=1  
   #49.- Personaje_meta
        #Caja
        #Espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==2 and  self.mapa[self.muneco_fila+2,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila+1,self.muneco_columna]=0
      self.mapa[self.muneco_fila+2,self.muneco_columna]=2
      self.muneco_fila+=1            
    #50.- Personaje_meta
        #Caja
        #Meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==2 and  self.mapa[self.muneco_fila+2,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila+1,self.muneco_columna]=0
      self.mapa[self.muneco_fila+2,self.muneco_columna]=6
      self.muneco_fila+=1        
     #51.- Personaje_meta
        #Caja_meta
        #Espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==6 and  self.mapa[self.muneco_fila+2,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila+1,self.muneco_columna]=5
      self.mapa[self.muneco_fila+2,self.muneco_columna]=2
      self.muneco_fila+=1         
    #52.- Personaje_meta
        #Caja_meta
        #Meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==6 and  self.mapa[self.muneco_fila+2,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila+1,self.muneco_columna]=5
      self.mapa[self.muneco_fila+2,self.muneco_columna]=6
      self.muneco_fila+=1
      
  # Metodo play  
  def play(self):
    self.loadFile() # Llmado a la funcion loadFile()
    self.findColumnasFilas() # Llmado a la funcion cindColumnasFilas()
    self.convertirFile() # Llmado a la funcion convertirFile()
    self.findPosition() # Llmado a la funcion findPosition()

    # Bucle para jugar n veces
    while True:
      print()
      print(" ---- Nivel Actual: "+self.nivel+" ----")
      print()
      intrucciones = " d - Derecha\n i - Izquierda\n r - Arriba\n a - Abajo\n q - Salir" #Instrucciones
      print(intrucciones)
      print()

      level = 1
      if self.complet == True:
        print("Level Complete")  # Print the level complete
        input("Press Enter to continue...")   
        nivel_nuevo = 'level1.txt'
        self.nivel = nivel_nuevo
        self.loadFile()
        self.findColumnasFilas()
        self.convertirFile()
        self.findPosition()
        level+=1
        
      self.printMap()
      movimientos = input(" Mover a: ") # Lee el movimiento
      if movimientos == 'd': # Si es d - mover a la derecha
        juego.moverDerecha() # Llamdo a la funcion moverDerecha()
        juego.limpiarPantalla() # Llamdo a la funcion limpiarPantalla()
      elif movimientos == 'i': # Si es i - mover a la izquierda
        juego.moverIzquierda() # Llamdo a la funcion moverIzquierda()
        juego.limpiarPantalla() # Llamdo a la funcion limpiarPantalla()
      elif movimientos == 'r': # Si es r - mover a arriba
        juego.moverArriba() # Llamdo a la funcion moverArriba()
        juego.limpiarPantalla() # Llamdo a la funcion limpiarPantalla()
      elif movimientos == 'a': # Si es a - mover a abajo
        juego.moverAbajo() # Llamdo a la funcion moverAbajo()
        juego.limpiarPantalla() # Llamdo a la funcion limpiarPantalla()
      elif movimientos == "q": # Si es q-salir
        print(" Saliste del juego") 
        break # Rompe el ciclo while
    
# Creamos un objeto de la clase Sokoban()
juego = Sokoban()
# Llamado a la funcion play()  
juego.play()
