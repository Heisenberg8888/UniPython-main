import math
from re import I

#1 dijstra's algorithm

#shortrul.at/rEFOY

graph =  [
    [0,5,3,4,None,None],
    [5,0,1,None,3, None],
    [3,1,0,1,10,None],
    [4,None,1,0,6,None],
    [None,3,10,6,0,None],
    [None,None,None,None,None,None],
]

# return number of nodes of a graph
def node_count(graph):
    return len(graph)

# returns a smallest element in the list an its index, 
def smallest_index(list, visited):
    s = math.inf
    index = -1

    for i in range(len(list)):
        if (visited[i] != True) and (s > list[i]):
            index = i 
            s = list[i]  

    return index

def dijkstra_algorithm(graph, start_node):
    big = math.inf  
    count = node_count(graph)
    current_values = [big] * count
    current_values[start_node] = 0

    # array that says whether the node has been visited or not
    # at the start, everything apart from start_node is set to False
    visited = [False] * len(graph)

    while smallest_index(current_values,visited) != -1:
        min_index = smallest_index(current_values, visited)
        current_neighbours = graph[min_index]

        for i in range(count):
            if current_neighbours[i] != None:
                current_values[i] = min(current_values[i], current_values[min_index] + current_neighbours[i])

        visited[min_index] = True

    return current_values

# returns distance from a starting point to destination point
def dijkstra_dest(graph, start, dest):
    return dijkstra_algorithm(graph, start)[dest]

#tests
print(dijkstra_algorithm(graph, 0))
print("Test 1 expects: 3")
print("Test 1 gets:    " + str(dijkstra_dest(graph, 0, 2)))
print("Test 2 expects: 5")
print("Test 2 gets:    " + str(dijkstra_dest(graph, 3, 4)))
print("Test 3 expects: 7")
print("Test 3 gets:    " + str(dijkstra_dest(graph, 0, 4)))
print("Test 4 expects: inf")
print("Test 4 gets:    " + str(dijkstra_dest(graph, 0, 5)))
