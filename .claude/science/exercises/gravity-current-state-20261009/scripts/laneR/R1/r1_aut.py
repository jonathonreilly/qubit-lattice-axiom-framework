# R1 check: adjacency-preserving bijections of the cubic torus C_L^3 are global (count = 48 L^3), L=5.
import networkx as nx, itertools, time
from networkx.algorithms.isomorphism import GraphMatcher
L=5; G=nx.grid_graph(dim=[L,L,L], periodic=True)
t=time.time(); n=0; nonglobal=0
for m in GraphMatcher(G,G).isomorphisms_iter():
    n+=1
    # global test: m(x) - m(0) must be a signed-permutation image of x (mod L)
print('L=%d automorphisms counted: %d ; 48 L^3 = %d ; time %.1fs'%(L,n,48*L**3,time.time()-t))
