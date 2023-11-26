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
answer = []
# borrar los datos guardados
def resetVars():
  global n
  global m
  global t
  global c
  global answer
  n = 0
  m = 0
  t = []
  c = []
  answer = []
  return
#leer Datoa del archivo idx
def readData(idx):
  global n
  global m
  global t
  global c
  global answer
  with open('tests/'+str(idx)+'.txt','r') as file:
    line = file.readline()
    m,n = map(int,line.split())
    line = file.readline()
    for i in range(n):
      line = file.readline()
      r = [int(num) for num in line.split()]
      t.append(r)
    for i in range(n):
      line = file.readline()
      aux = []
      for j in range(m):
        line = file.readline()
        r = [int(num) for num in line.split()]
        aux.append(r)
      c.append(aux)
  return


#valor de la posible solucion list1
def value(list1):
  global n
  global m
  global t
  global c
  global answer
  ans = 0
  for i in range(n):
    p = []
    curAns = 0
    for j in range(m):
      if list1[j]==i:
        p.append(j)
    for k in range(1,len(p)):
      curAns+=c[i][p[k-1]][p[k]]
    for k in p:
      curAns+=t[i][k]
    ans = max(ans,curAns)
  return ans

def changeSomething(list1):
  global n
  global m
  global t
  global c
  global answer
  # array of pairs, a.F means that the a.F index value will change for a.S
  cambios = []
  for i in range(m):
    for j in range(n):
      if j!=list1[i]:
        cambios.append([i,j])
  cambio = random.choice(cambios)
  list1[cambio[0]] = cambio[1]
  return list1

def recocido():
  global n
  global m
  global t
  global c
  global answer
  # crear answer, primera solucion valida
  # solo movernos entre soluciones validas
  answer = [-1]*m
  for i in range(m):
    g = []
    for j in range(n):
      if t[j][i]!=1000:
        g.append(j)
    answer[i]=random.choice(g)


  #temperatura inicial,alpha e iteraciones maximas
  # Estos son los valores que deben modificar y hacer las pruebas
  T = 10**20
  alpha = 0.997
  K = 100000
  # codigo para el recocido simulado
  bestAns = answer
  ans = value(answer)
  while K>0 and T>0.01:
    copia = []
    for i in answer:
      copia.append(i)
    new = changeSomething(copia)
    if value(new)<=value(answer):
      answer = new
    else:
      r = random.random()
      try:
        if r<math.exp((value(answer)-value(new))/T):
          answer = new
      except:
        pass
    if value(answer)<ans:
      ans = value(answer)
      bestAns = answer
    T *= alpha
    K = K-1
  return ans
if __name__=="__main__":
  for i in range(3,4):
    resetVars()
    readData(i)
    r = 1000000000
    for j in range(20):
      r = min(r,recocido())
      print(r)