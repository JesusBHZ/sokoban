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
     
  def printMap(self):
    """_summary_: Print the map"""
    mapa = np.loadtxt('level0.txt', dtype=int)
    for j in range(7):
      for i in range(11):
        if mapa[j][i] == 0:
            #Si encuentra un numero 1 -  espacio
            #for a in range(len(self.mapa[0])):
            print("🤖", end = "")#Cambiar un 1 por un ""
        elif mapa[j][i] == 1:
            #Si encuentra un numero 1 -  espacio
            #for a in range(len(self.mapa[0])):
            print("  ", end = "")#Cambiar un 1 por un ""
        elif mapa[j][i] == 2: #3-pared
            #for a in range(len(self.mapa)):
            print("🧰", end = "")#Cambia un 3 por un simbolo  
        elif mapa[j][i] == 3: #3-pared
            #for a in range(len(self.mapa)):
            print("🔳", end = "")#Cambia un 3 por un simbolo
        elif mapa[j][i] == 4: #3-pared
            #for a in range(len(self.mapa)):
            print("⛳", end = "")#Cambia un 3 por un simbolo  
        elif mapa[j][i] == 5: #3-pared
            #for a in range(len(self.mapa)):
            print("🎖", end = "")#Cambia un 3 por un simbolo
        elif mapa[j][i] == 6: #3-pared
            #for a in range(len(self.mapa)):
            print("🏆", end = "")#Cambia un 3 por un simbolo       
        else:
            print(mapa[j][i], end=" ")
      print()
    print() #Imprime una linea vacia   
  



    
