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
      h-Abajo\
      q-Salir
"""
import  numpy as np
class Sokoban:
  def __init__(self):
        """_summary_: Constructor"""
        pass
  def loadMapa(self):
    self.mapa = np.loadtxt('level0.txt', dtype=int)
     
  


    
