import math

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

# testing matrix props
'''
print(graph_matrix[0])
graph_matrix[0][0] = 10
print(graph_matrix[0])
'''

# return number of nodes of a graph
def node_count(graph):
    return len(graph)

# returns a smallest element in the list an its index, 
def smallest_index(list):
    s = math.inf
    index = 0
    for i in range(len(list)):
        if (list[i] != None):
            if list[i] < s:
                s = list[i]
                index = i
    return [s, index]

# returns index of a smallest value
def s_index(list):
    return smallest_index(list)[1]

# returns smallest value
def s_value(list):
    return smallest_index(list)[0]
    
# as long as element isn't None, it will be ovewritten by element from reference list
def update_list(updated, reference):
    for i in range(len(updated)):
        if updated[i] != None:
            updated[i] = reference[i]
    return updated

def is_empty(list):
    check = True
    for i in range(len(list)):
        if not ((list[i] == None) or (list[i] == math.inf)):
            return False
    return True


#function testing
#print(smallest_index([3,4,None, 9,1, None]))

def dijkstra_algorithm(graph, start_node):
    big = math.inf  
    count = node_count(graph)
    current_values = [big] * count
    current_values[start_node] = 0

    # array that says whether the node has been visited or not
    # at the start, everything apart from start_node is set to False, --redundant--
    '''
    visited = []
    for i in range(node_count(graph)):
        if i == start_node:
            visited += True
        else:
            visited += False
    '''

    # copy of current values, which serves as a check whether we went through all nodes or not
    working_list = current_values.copy()
    # goes through unvisited nodes
    # the loops stops when working_list only contains None or inf:
        # 1) None means that this node has been visited 
        # 2) if there are only Nones and ifs, if means that node is unreachable
    # s_value, s_index are functions the can find smallest value and index of
    # list that contains None and inf
    while not (is_empty(working_list)):
        min_value = s_value(working_list)
        min_index = s_index(working_list)
        current_neighbours = graph[min_index]

        for i in range(count):
            if current_neighbours[i] != None:
                current_values[i] = min(current_values[i], min_value + current_neighbours[i])

        working_list[min_index] = None
        working_list = update_list(working_list, current_values)

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
