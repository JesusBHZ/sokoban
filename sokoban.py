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
class Sokoban:
  def __init__(self):
        """_summary_: Constructor"""
        pass
  def loadMapa(self):
    archivo = open("level0.txt","r")
    
  mapa = archivo   
  def printMap(self):
        """_summary_: Print the map"""
        # TODO: Print the map
        for row in archivo:  # For each row in map
            print(row)  # Print the row
juego = Sokoban()#Crea un objeto para jugar
juego.imprimirMapa()#Imprime el mapa