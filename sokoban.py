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
  nivel = 'level2.txt'

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

   
juego = Sokoban()#Crea un objeto para jugar
juego.loadFile()
juego.findColumnasFilas()
juego.convertirFile()
juego.findPosition()
