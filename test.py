import igraph as ig
import os

#g = ig.Graph(n=10, edges=[[0, 1], [0, 5], [8, 1]], directed=True)
#degree_sequence = [1, 1, 1, 2, 1, 3, 1]
#g = ig.Graph.Degree_Sequence(degree_sequence)

g = ig.Graph().Recent_Degree(n=100, power=0.1, m=2, window=10)
dot_file = "graph.dot"
file_name = dot_file[:-4]
dot = g.write_dot(dot_file)
os.system("dot " + dot_file + " -Tpng -o " + file_name + ".png")
