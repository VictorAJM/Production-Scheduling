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
    R = (n-m%n)%n
    print(R)
    for i in range(n):
      line = file.readline()
      r = [int(num) for num in line.split()]
      for _ in range(R):
        r.append(0)
      t.append(r)

    for i in range(n):
      line = file.readline()
      aux = []
      for j in range(m):
        line = file.readline()
        r = [int(num) for num in line.split()]
        for _ in range(R):
          r.append(0)
        aux.append(r)
      for _ in range(R):
        r = []
        for __ in range(m+R):
          if __ <= _+m:
            r.append(1000)
          else:
            r.append(0)
        aux.append(r)
      c.append(aux)
    m += R
  print(n,m)   
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
def value2(list1):
  global n
  global m
  global t
  global c
  global answer
  ans = 0
  r = 0
  for i in range(n):
    z = 0
    for j in list1:
      if j==i:
        z += 1
    r = max(z,r)
  return r
def changeSomething(list1):
  global n
  global m
  global t
  global c
  global answer
  # array of pairs, a.F means that the a.F index value will change for a.S
  q = random.randint(0,m-1)
  w = random.randint(0,m-1)
  while q==w:
    w = random.randint(0,m-1)
  list1[q],list1[w] = list1[w],list1[q]
  return list1
def validate(list1):
  global n
  global m
  global t
  global c
  for i in range(m):
    if t[list1[i]][i]==1000:
      return False
  return True
def fixing(list1):
  q = random.randint(0,m-1)
  w = random.randint(0,m-1)
  while q==w:
    w = random.randint(0,m-1)
  list1[q],list1[w] = list1[w],list1[q]
  while validate(list1)==False:
    q = random.randint(0,m-1)
    w = random.randint(0,m-1)
    while q==w:
      w = random.randint(0,m-1)
  return list1
def G():
  global n
  global m
  global t
  global c
  gg = []
  for i in range(m):
    gg.append(i%n)
  while validate(gg)==False:
    gg = fixing(gg)
  return gg

def recocido():
  global n
  global m
  global t
  global c
  global answer
  # crear answer, primera solucion valida
  # solo movernos entre soluciones validas
  answer = G()



  #temperatura inicial,alpha e iteraciones maximas
  # Estos son los valores que deben modificar y hacer las pruebas
  T = 10**30
  alpha = 0.99
  K = 100000
  # codigo para el recocido simulado
  bestAns = answer
  ans = value(answer)
  while K>0 and T>0.01:
    copia = []
    for i in answer:
      copia.append(i)
    new = changeSomething(copia)
    if value(new)<value(answer) or (value2(new)<=value2(answer) and value(new)==value(answer)):
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
  return bestAns
if __name__=="__main__":
  for i in range(1,11):
    resetVars()
    readData(i)
    r = 10203120321
    finalAnswer = []
    for j in range(10):
      answer = recocido()
      if value(answer)<r:
        r = value(answer)
        finalAnswer = answer
        print('for case ',i,' ',r,finalAnswer)
