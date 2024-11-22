#State space search - Decantation problem (Water Jug problem)

import copy

class jar(object):
    __slots__ = ['cur', 'max']

    def __init__(self, cur, max):
        self.cur = cur
        self.max = max

    def __eq__(self, other):
        if self.cur == other.cur and self.max == other.max:
            return True
        return False

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return str(self.cur)

    def __hash__(self):
        return hash((self.cur, self.max))

    def isFull(self):
        return self.cur == self.max

    def spaceLeft(self):
        return self.max - self.cur


class state(object):
    __slots__ = ['jars', 'parent']

    def __init__(self, jars, parent=None):
        self.jars = jars
        self.parent = parent

    def __eq__(self, other):
        flag = True
        for i in range(2):
            if self.jars[i] != other.jars[i]:
                flag = False
                break

        return flag

    def __str__(self):
        s = "("
        for jar in self.jars:
            s += str(jar) + ', '
        s = s[:-2]
        s += ')'
        return s

    def __hash__(self):
        return hash(self.jars)


initial_state = state((jar(0, 4), jar(0, 3)))
goal_state1 = state((jar(2, 4), jar(3, 3)))
goal_state2 = state((jar(2, 4), jar(0, 3)))

def next_states(curr_state):
    next = []
    for i in range(len(curr_state.jars)):
        for j in range(len(curr_state.jars)):
            if i == j:
                continue
            jars_temp = copy.deepcopy(curr_state.jars)

            #No capacity left to transfer from jar 'i'
            if jars_temp[i].cur <= 0:
                jars_temp[i].cur = jars_temp[i].max
                next.append(state(jars_temp, parent=curr_state))
                continue
            #pour to other jar
            if jars_temp[j].spaceLeft() > 0:
                avail = jars_temp[j].spaceLeft()

                if jars_temp[i].cur < avail:
                    jars_temp[j].cur += jars_temp[i].cur
                    jars_temp[i].cur = 0
                    next.append(state(jars_temp, parent=curr_state))
                    continue

                else:
                    jars_temp[j].cur += avail
                    jars_temp[i].cur -= avail
                    next.append(state(jars_temp, parent=curr_state))
                    continue
            #drain
            draintemp = jars_temp[i].cur
            jars_temp[i].cur = 0
            next.append(state(jars_temp, parent=curr_state))
            jars_temp[i].cur = draintemp
            jars_temp[j].cur = 0
            next.append(state(jars_temp, parent=curr_state))
    return next


print("______")

def print_steps(current_state):

    #Base case, this is the root state
    if current_state.parent is None:
        print(current_state)
        return

    #Recursive step
    print_steps(current_state.parent)
    print(current_state)

b1 = []

def bfs(initial_state, goal_state, trace=False):
    print("Tracing the queue contents: ")
    visited = set()

    states = []
    states.append(initial_state)
    b1.append(initial_state)

    while len(states) != 0:
        if trace:
            for s in states:
                print(s, end=' ')
            print()

        current_state = states.pop(0)
        if current_state == goal_state:
            print("Found Goal State!\n")
            #print_steps(current_state)
            break
        successors = next_states(current_state)

        b1.append(initial_state)
        for new_state in successors:
            if new_state not in visited:
                visited.add(new_state)
                states.append(new_state)
                b1.append(new_state)
            else:
                #Duplicate state
                pass
        
              
def dfs(initial_state, goal_state, trace=False):
    visited = set()

    states = []
    states.append(initial_state)

    while len(states) != 0:
        current_state = states.pop(0)
        if current_state == goal_state:
            
            print_steps(current_state)
            print("Found Goal State!")
            break
        successors = next_states(current_state)

        for new_state in successors:
            if new_state not in visited:
                visited.add(new_state)
                states.append(new_state)
            else:
                #Duplicate state
                pass

def dls(initial_state, goal_state, limit, trace=False):
    visited = set()
    states = []
    states.append(initial_state)
    count = 0

    while ((len(states) != 0) and count < limit):
        current_state = states.pop(0)
        if current_state == goal_state:
            print_steps(current_state)
            print("Found Goal State!")
            break
        successors = next_states(current_state)
        count += 1

        for new_state in successors:
            if new_state not in visited:
                visited.add(new_state)
                states.append(new_state)
            else:
                #Duplicate state
                pass

def ids(L,gs):
  print(initial_state)
  for m in L:
    if m == initial_state:
      continue
    print(m)
    if m == gs:
      print("Goal state found!\n")
      break
              
#trace = True for queue contents
print("BFS: ")
bfs(initial_state, goal_state1, trace=True)
print("_______")
b2 = []
b2 = b1
b1 = []
bfs(initial_state, goal_state2, trace=True)
print("_______")

print("DFS: ")
dfs(initial_state, goal_state1, trace=True)
print("_______")
dfs(initial_state, goal_state2, trace=True)
print("_______")

print("\nDLS: ")
dls(initial_state, goal_state1, limit = 6, trace=True)
print("_______")
dls(initial_state, goal_state2, limit = 6, trace=True)
print("_______")

print("\nIDS: ")
ids(b1,goal_state1)
print("_______")
ids(b1,goal_state2)
print("_______")