"""Claim (2): soldered extended class. Alphabet split, maximal commuting sets containing an outsider."""
import sys, pickle, time, itertools, numpy as np, networkx as nx
sys.path.insert(0, '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4')
from sitecore import *
W = '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4/'
t0 = time.time()
orbs = pickle.load(open(W + 'orbs_soldered_C2z_C2xy_C4z_C3.pkl', 'rb'))
idS = (0,)*7
orbs = [(S, d) for S, d, ok in orbs if ok and S != idS]
print('nonidentity sign-consistent orbits', len(orbs))
Galpha = {code_of(l) for l in itertools.product((0, 1), (0, 2), (0, 3))}
isG = [all(c in Galpha for T in d for c in T) for S, d in orbs]
print('G-alphabet orbits', sum(isG), 'outsider orbits', len(orbs) - sum(isG))
# sanity: is the G alphabet abelian and its own commutant?
print('G abelian:', all(COMM[a, b] == 0 for a in Galpha for b in Galpha),
      ' commutant size', sum(all(COMM[c, a] == 0 for a in Galpha) for c in range(64)))
N = len(orbs)
def orbit_comm(u, v):
    S = orbs[u][0]
    return all(comm_translates(S, T) for T in orbs[v][1])
out = [u for u in range(N) if not isG[u]]
nbr = {}
for u in out:
    nbr[u] = set(v for v in range(N) if v != u and orbit_comm(u, v))
# symmetry check
for u in out:
    for v in out:
        if v != u: assert (v in nbr[u]) == (u in nbr[v])
print('outsider neighbourhood sizes', sorted(len(nbr[u]) for u in out), '%.1fs' % (time.time() - t0))
# maximal cliques of full graph containing an outsider: maximal cliques of N[u] U {u} for each outsider u,
# with adjacency G-G always true.
def adj(a, b):
    if isG[a] and isG[b]: return True
    if not isG[a]: return b in nbr[a]
    return a in nbr[b]
cl = set()
for u in out:
    nodes = sorted(nbr[u] | {u})
    H = nx.Graph(); H.add_nodes_from(nodes)
    H.add_edges_from((a, b) for a, b in itertools.combinations(nodes, 2) if adj(a, b))
    for c in nx.find_cliques(H):
        if u in c: cl.add(tuple(sorted(c)))
# keep only globally maximal (any vertex adjacent to all?)
def maximal(c):
    cs = set(c)
    cand = set.intersection(*[nbr[x] for x in c if not isG[x]]) if any(not isG[x] for x in c) else set(range(N))
    return not any(all(adj(w, x) for x in c) for w in cand - cs)
cl = [c for c in cl if maximal(c)]
print('maximal commuting sets containing an outsider:', len(cl), 'sizes', sorted(len(c) for c in cl))
for c in sorted(cl, key=len):
    print('  size', len(c), 'outsiders', sum(not isG[x] for x in c), 'G-orbits', sum(isG[x] for x in c))
print('outsiders covered', len(set(x for c in cl for x in c if not isG[x])))
pickle.dump({'orbs': orbs, 'isG': isG, 'cliques': cl}, open(W + 'sold_sets.pkl', 'wb'))
print('time %.1fs' % (time.time() - t0))
