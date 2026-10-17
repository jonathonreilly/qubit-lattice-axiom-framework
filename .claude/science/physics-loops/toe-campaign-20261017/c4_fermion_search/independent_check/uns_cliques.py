import sys, pickle, time, numpy as np, networkx as nx
W = '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4/'
t0 = time.time()
A = np.load(W + 'uns_adj.npy'); N = len(A)
G = nx.Graph(); G.add_nodes_from(range(N)); G.add_edges_from(zip(*np.nonzero(np.triu(A))))
cl = []
for c in nx.find_cliques(G):
    cl.append(tuple(sorted(c)))
    if len(cl) % 200000 == 0: print(len(cl), '%.0fs' % (time.time() - t0)); sys.stdout.flush()
print('maximal cliques', len(cl), 'time %.1fs' % (time.time() - t0))
from collections import Counter; print(sorted(Counter(len(c) for c in cl).items()))
pickle.dump(cl, open(W + 'uns_cliques.pkl', 'wb'))
