# Implementation of Minimax algorithm

import math
from binarytree import Node
from binarytree import build

def left(seq,index):
  return seq[2*index+1]

def right(seq,index):
  return seq[2*index+2]


level = int(input("\nEnter level limit: "))
ht = level+1

seq = [i for i in range(1,2**ht)]
tree = build(seq)
print(tree)
nodes = tree.values
print("Nodes:",nodes)

# Recursive DFS for Minimax algorithm

value = None
for l in range(level-1,-1,-1):
  num = 2**l
  for i in range(num-1,num*2-1):
    if (l%2 == 0):
      value = max(left(nodes,i), right(nodes,i))
    else:
      value = min(left(nodes,i), right(nodes,i))
    nodes[i] = value

answerTree = build(nodes)
print(answerTree)

print("Answer:", value)