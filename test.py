import igraph as ig
import random
import os

ONE_EDGE_WEIGHT = 40
BRANCH_WEIGHT = 20
LOOP_WEIGHT = 20

node_types = ["one_edge", "branch", "loop"]
weights = [ONE_EDGE_WEIGHT, BRANCH_WEIGHT, LOOP_WEIGHT]
nodes_number = int(input())

graph_nodes = random.choices(node_types, weights, k=nodes_number - 3)
graph_nodes.append("one_edge")
graph_nodes.insert(0, "one_edge")
print(graph_nodes)

edges_list = []
for i in range(nodes_number - 1):
    match graph_nodes[i]:
        case "one_edge":
            edges_list.append([i, i + 1])
        case "branch":
            edges_list.extend([[i, i + 1], [i, i + 2]])
        case "loop":
            if i <= 5:
                prev = random.randint(1, i)
            else:
                prev = random.randint(1, 5)
            edges_list.extend([[i, i + 1], [i, i - prev]])


g = ig.Graph(n=2, edges=edges_list, directed=True)

dot_file = "graph1.dot"
file_name = dot_file[:-4]
dot = g.write_dot(dot_file)
os.system("dot " + dot_file + " -Tpng -o " + file_name + ".png")
