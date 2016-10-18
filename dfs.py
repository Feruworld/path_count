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

def dfs(vertex, used, path):
    global count, len_count
    if vertex == goal_vertex:
        count += 1
        len_count[len(path)] += 1
        return
    linked = np.where(adjacent[vertex] == 1)[0]
    nodes = np.setdiff1d(linked,used)
    for node in nodes:
        dfs(node, np.append(used, vertex), np.append(path, node))

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
len_count = np.zeros(vertex_num+1)
dfs(start_vertex,np.array([start_vertex]), np.array([start_vertex]))
for i,l in enumerate(len_count):
    if l != 0:
        print i, ":", int(l)
print "total :", count
