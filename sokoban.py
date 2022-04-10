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
import platform
import os
import  numpy as np
class Sokoban:
  archivo = ""
  columnas = 0
  filas = 0
  mapa = []
  nivel = 'level0.txt'

  def __init__(self):
        """_summary_: Constructor"""
        pass
    
  def loadFile(self):
    # Columnas
    with open(self.nivel) as f:
      colum = f.readline().rstrip()
    self.columnas = len(colum)
   
  def findColumnasFilas(self):
    # Filas
    fichero = open(self.nivel, 'r') 
    fichero.readline()
    fichero.seek(0)
    self.filas = len(fichero.readlines())
  
  def convertirFile(self):
  # Cargar Archivo
    self.archivo = open(self.nivel, 'r')
    self.hola = self.archivo.read()
    texto=[]
    for i in self.hola:
      texto+=i.rstrip()
    for k in range(len(texto)):
      texto[k] = int(texto[k])
      
    self.mapa = np.array(texto).reshape(self.filas,self.columnas)


  def findPosition(self):
    result = np.where(self.mapa == 0)
    map = self.mapa
    self.muneco_fila=result[0]
    self.muneco_columna=result[1]

  def printMap(self):
    """_summary_: Print the map"""
    for j in range(self.filas):
      for i in range(self.columnas):
        if self.mapa[j][i] == 0:
            #Si encuentra un numero 1 -  espacio
            #for a in range(len(self.mapa[0])):
            print("🤖", end = "")#Cambiar un 1 por un ""
        elif self.mapa[j][i] == 1:
            #Si encuentra un numero 1 -  espacio
            #for a in range(len(self.mapa[0])):
            print("  ", end = "")#Cambiar un 1 por un ""
        elif self.mapa[j][i] == 2: #3-pared
            #for a in range(len(self.mapa)):
            print("🧰", end = "")#Cambia un 3 por un simbolo  
        elif self.mapa[j][i] == 3: #3-pared
            #for a in range(len(self.mapa)):
            print("🔳", end = "")#Cambia un 3 por un simbolo
        elif self.mapa[j][i] == 4: #3-pared
            #for a in range(len(self.mapa)):
            print("⛳", end = "")#Cambia un 3 por un simbolo  
        elif self.mapa[j][i] == 5: #3-pared
            #for a in range(len(self.mapa)):
            print("🔰", end = "")#Cambia un 3 por un simbolo
        elif self.mapa[j][i] == 6: #3-pared
            #for a in range(len(self.mapa)):
            print("🏆", end = "")#Cambia un 3 por un simbolo       
        else:
            print(self.mapa[j][i], end=" ")
      print()
    print() #Imprime una linea vacia 
    
  def limpiar_pantalla(self):
    if platform.system()=='Windows':
      os.system('cls')
    else:
      os.system('clear')

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

   
juego = Sokoban()#Crea un objeto para jugar
juego.loadFile()
juego.findColumnasFilas()
juego.convertirFile()
juego.findPosition()
juego.limpiar_pantalla

while True:#Bucle para jugar N veces
  intrucciones = "d-Derecha\ni-Izquierda\nr-Arriba\na-Abajo\nq-Salir" #Instrucciones
  print(intrucciones)
  print()
  juego.printMap()#Imprime el mapa
  movimientos = input("mover a: ")#Lee el movimiento
  if movimientos == 'd':#si es d - mover a la derecha
    juego.moverDerecha()#mueve el muñeco  a la derecha
    juego.limpiar_pantalla()
  elif movimientos == 'i': #si es a - mover a la izquierda
    juego.moverIzquierda()#mueve el muñeco  a la izquierda
    juego.limpiar_pantalla()
  elif movimientos == 'r': #si es r - mover a arriba
    juego.moverArriba()#mueve el muñeco  a arriba
    juego.limpiar_pantalla()
  elif movimientos == 'a': #si es l - mover a abajo
    juego.moverAbajo()#mueve el muñeco  a abajo
    juego.limpiar_pantalla()
  elif movimientos == "q":#si es q-salir
    print("Saliste del juego")#Imprmir mensaje
    break #Rompe el ciclo while

