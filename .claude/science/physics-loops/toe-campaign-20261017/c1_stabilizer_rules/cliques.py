"""Compatibility of single-orbit rules and maximal commuting combinations (trivial and sign actions)."""
import json, itertools, sys
import networkx as nx
from classify import orbit, family_commutes
d = json.load(open('single_orbits.json'))
for action in ('trivial', 'sign'):
    rules = [tuple(g[0]) for g in d[action]]
    orbs = [list(orbit(r, action)) for r in rules]
    G = nx.Graph(); G.add_nodes_from(range(len(rules)))
    for i, j in itertools.combinations(range(len(rules)), 2):
        if family_commutes(orbs[i], orbs[j]): G.add_edge(i, j)
    cl = list(nx.find_cliques(G))
    print(action, 'orbits', len(rules), 'edges', G.number_of_edges(), 'maximal cliques', len(cl), flush=True)
    json.dump({'rules': rules, 'cliques': cl}, open(f'cliques_{action}.json', 'w'))
