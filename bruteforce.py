import numpy as np

'''
size = 2
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
'''

vertex_num = 4
edges = np.array([[0,1],[0,2],[1,2],[1,3],[2,3],[0,3]])
start_vertex = 0
goal_vertex = 3

def brute_force(edge, use, degree, comp):
    global count
    edge += 1
    if edge == edge_num:
        #judge if there is one path 
        if degree[start_vertex] != 1 or degree[goal_vertex] != 1:
            return # degree of s or g is not 1
        if degree.max() > 2:
            return # degree must be 0 or 2 except s and g
        if len(np.where(degree == 1)[0]) != 2:
            return # vertex whose degree is 0 are onle two
        comp_count = np.zeros(vertex_num)
        for i in range(vertex_num):
            comp_count[comp[i]] += 1
        if len(np.where(comp_count >= 2)[0]) != 1:
            return # there are circles
        print use
        count += 1
        return
    use_new = use.copy() 
    degree_new = degree.copy()
    comp_new = comp.copy()
    brute_force(edge, use_new, degree_new, comp_new)
    use_new[edge] = 1
    v, w = edges[edge][0], edges[edge][1]
    degree_new[v] += 1
    degree_new[w] += 1
    comp_min, comp_max = min(comp[v], comp[w]), max(comp[v], comp[w])
    comp_new[v] = comp_min
    comp_new[w] = comp_min
    comp_new[comp_new == comp_max] = comp_min
    brute_force(edge, use_new, degree_new, comp_new)

degrees = np.zeros(vertex_num)
comp = np.zeros(vertex_num)
for i in range(vertex_num):
    comp[i] = i

edge_num = edges.shape[0]
adjacent = np.zeros([vertex_num, vertex_num])

for edge in edges:
    adjacent[edge[0]][edge[1]] = 1
    adjacent[edge[1]][edge[0]] = 1

count = 0
brute_force(-1, np.zeros(edge_num), degrees, comp)
print count
