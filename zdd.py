import sys
import numpy as np

if len(sys.argv) != 2:
    print "argument error"
    quit()

size = int(sys.argv[1])
vertex_num = (size+1)**2
edges = np.empty((0,2), int)
for i in range(size+1): # horizontal edge
    for j in range(size):
        edges = np.append(edges, np.array([[(size+1)*i+j, (size+1)*i+j+1]]), axis=0)

for i in range(size+1): # vertical edge
    for j in range(size):
        edges = np.append(edges, np.array([[i+j*(size+1), i+(j+1)*(size+1)]]), axis=0)
start_vertex = 0
goal_vertex = (size+1)**2 - 1

def zdd(edge, use, degree, comp):
    global count
    if edge == edge_num - 1:
        if len(np.where(degree == 1)[0]) != 2 or True in (degree > 2): return
        comp_count = np.zeros(vertex_num)
        if degree[start_vertex] != 1 or degree[goal_vertex] != 1:
           return
        for i in range(vertex_num):
            comp_count[comp[i]] += 1
        if len(np.where(comp_count >= 2)[0]) != 1:
            return # there are circles
        print use,comp
        count += 1
        return

    edge += 1
    use_new = use.copy()
    degree_new = degree.copy()
    comp_new = comp.copy()
    '''
    0-branch
    not use edges[edge]
    '''
    #check start and goal node's degree is 0
    #if (edge >= start_adjacent_max and degree[start_vertex] == 0) or (edge >= goal_adjacent_max and degree[goal_vertex] == 0):
    #  return
    #check path is devided

    zdd(edge, use, degree, comp)
    '''
    1-branch
    use edges[edge]
    '''
    use_new[edge] = 1

    #update degree
    update_list = edges[edge]
    degree_new[update_list] += 1

    #check start and goal node
    if degree_new[start_vertex] >= 2 or degree_new[goal_vertex] >= 2:
        return
    #check if there are nodes whose degree is over 2
    if True in (degree >= 3):
        return
    #check if there are cycle
    if comp[edges[edge][0]] == comp[edges[edge][1]]:
        return

    comp_min = min(comp[edges[edge][0]], comp[edges[edge][1]])
    comp_new[edges[edge][0]], comp_new[edges[edge][1]] = comp_min, comp_min

    zdd(edge, use_new, degree_new, comp_new)

degree = np.zeros(vertex_num)
comp = np.zeros(vertex_num)
for i in range(vertex_num):
    comp[i] = i

edge_num = edges.shape[0]
adjacent = np.zeros([vertex_num, vertex_num])

for edge in edges:
    adjacent[edge[0]][edge[1]] = 1
    adjacent[edge[1]][edge[0]] = 1

start_adjacent_max = np.where(adjacent[start_vertex]==1)[0].max()
goal_adjacent_max = np.where(adjacent[goal_vertex]==1)[0].max()

count = 0
zdd(-1, np.zeros(edge_num), degree, comp)
print count
