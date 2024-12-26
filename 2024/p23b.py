#!/usr/bin/python3

import networkx as nx
print(",".join(sorted(nx.algorithms.max_weight_clique(nx.read_edgelist("p23.txt", delimiter="-"), None)[0])))
