import random
import math
# numero de maquinas
n = 0
# numero de trabajos
m = 0
# t[i][j] tiempo que tarda el trabajo j en la maquina i
t = []
# c[i][j][k] tiempo que tarda cargar el trabajo k despues del trabajo j en la maquina i
c = []

# borrar los datos guardados
def resetVars():
  n = 0
  m = 0
  t = []
  c = []
  return
#leer Datoa del archivo idx
def readData(idx):
  with open('tests/'+str(idx)+'.txt','r') as file:
    line = file.readline()
    M,N = map(int,line.split())
    line = file.readline()
    for i in range(N):
      line = file.readline()
      r = [int(num) for num in line.split()]
      t.append(r)
    for i in range(N):
      line = file.readline()
      aux = []
      for j in range(M):
        line = file.readline()
        r = [int(num) for num in line.split()]
        aux.append(r)
      c.append(aux)
  return


if __name__=="__main__":
  for i in range(1,11):
    resetVars()
    readData(i)