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
   
juego = Sokoban()#Crea un objeto para jugar
juego.loadFile()
juego.findColumnasFilas()
juego.convertirFile()
juego.findPosition()
juego.printMap()
juego.limpiar_pantalla
