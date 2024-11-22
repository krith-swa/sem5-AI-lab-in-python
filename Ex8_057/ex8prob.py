#Inference using Bayesian Network - Joint probability distribution

import networkx as nx
from matplotlib import pyplot as plt

#tables
ex_lvl = [0.7,0.3]
iq = [0.8,0.2]
marks = [[0.6,0.4],[0.9,0.1],[0.5,0.5],[0.8,0.2]]
admission = [[0.60,0.40],[0.9,0.1]]
apt_score = [[0.75,0.25],[0.4,0.6]]

#print tables
print("\n   EXAM LEVEL: \n")
print("|  e0  |  e1  |")
print("+-------------+")
for i in ex_lvl:
  print("| ",i,end=" ")
print("|")

print("\n\n   IQ LEVEL: \n")
print("|  i0  |  i1  |")
print("+-------------+")
for i in iq:
  print("| ",i,end=" ")
print("|")

print( "\n\n     MARKS: \n")
print("          |   m0  |   m1  |")
print("+-------------------------+")
k=0
sl=["i0,e0","i0,e1","i1,e0","i1,e1"]
for i in marks:
  print("| ",sl[k]," | ",i[0]," | ",i[1]," |")
  k+=1

print("\n\n       ADMISSION: \n")
print("       |   a0  |   a1  |")
print("+----------------------+")
k=0
sl=["m0","m1"]
for i in admission:
  print("| ",sl[k]," | ",i[0]," | ",i[1]," |")
  k+=1

print("\n\n     APTITUDE SCORE: \n")
print("       |   s0  |   s1   |")
print("+-----------------------+")
k=0
sl=["i0","i1"]
for i in apt_score:
  print("| ",sl[k]," |  {a:.2f} |  {b:.2f}  |".format(a=i[0],b=i[1]))
  k+=1

#DAG Representation
g1 = nx.DiGraph()
g1.add_edges_from([("Exam level","Marks"), ("IQ level","Marks"),("IQ level","Aptitude score"),("Marks","Admission")])
plt.tight_layout()
nx.draw_networkx(g1, arrows=True)
plt.show()
  
#Formula
print("\n\nFormula: P[a=1, m=1, i=1, e=1, s=1] = P(a=1 | m=1) . P(m=1 | i=1, e=1) . P(i=1) . P(e=1) . P(s=1 | i=1)")
print("\nP(a=1 | m=1) = {a:.2f}\nP(m=1 | i=1, e=1) = {b:.2f}\nP(i=1) = {c:.2f} \nP(e=1) = {d:.2f}\nP(s=1 | i=1) = {g:.2f}\n\nP[a=1, m=1, i=1, e=1, s=1] = ".format(a=admission[1][1],b=marks[3][1],c=iq[1],d=ex_lvl[1],g=apt_score[1][1]),end=" ")
print(round(admission[1][1]*marks[3][1]*iq[1]*ex_lvl[1]*apt_score[1][1],5))

