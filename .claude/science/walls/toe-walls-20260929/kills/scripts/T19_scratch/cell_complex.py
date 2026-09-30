"""Test C: Z^3 nearest-neighbour graph read as the cell complex of the cubic lattice 2Z^3 (roles by parity)."""
import itertools, collections
N = 8  # periodic 8x8x8 window (even) so every site has full neighbourhood
role = {(0,0,0): 'vertex', (1,0,0): 'edge', (0,1,0): 'edge', (0,0,1): 'edge',
        (1,1,0): 'face', (1,0,1): 'face', (0,1,1): 'face', (1,1,1): 'cube'}
def R(c): return role[tuple(x % 2 for x in c)]
nbrs = lambda c: [tuple((c[i] + s * (j == i)) % N for i in range(3)) for i in range(3) for s in (1, -1) for j in [i]]
cnt = collections.Counter(R(c) for c in itertools.product(range(N), repeat=3))
print("role counts per site:", {k: v / N**3 for k, v in cnt.items()})
adj = collections.defaultdict(collections.Counter)
for c in itertools.product(range(N), repeat=3):
    for d in nbrs(c): adj[R(c)][R(d)] += 1
    # 6 neighbours each
for k in ('vertex', 'edge', 'face', 'cube'):
    n_k = cnt[k]
    print(k, "neighbours per site:", {j: v / n_k for j, v in adj[k].items()})
# geometric incidence check: neighbours of an edge site (1,0,0): vertices (0,0,0),(2,0,0); faces (1,+-1,0),(1,0,+-1)
c = (3, 2, 4)  # edge site: odd,even,even
assert R(c) == 'edge'
print("edge site", c, "-> neighbours", [(d, R(d)) for d in nbrs(c)])
# modes: vertices; edge qubits per mode = 3 edges per vertex-cell
print("mode density (vertices per site) =", cnt['vertex'] / N**3, "; edge qubits per mode =", cnt['edge'] / cnt['vertex'])
# translation covariance: shifting by e_x maps roles
shift = lambda c: ((c[0] + 1) % N, c[1], c[2])
print("role permutation under translation by e_x:", {R(c): R(shift(c)) for c in [(0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)]})
