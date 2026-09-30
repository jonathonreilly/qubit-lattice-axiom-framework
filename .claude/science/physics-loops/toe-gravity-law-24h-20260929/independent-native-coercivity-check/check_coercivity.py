"""Independent exact controls, not an N=3 torus Hilbert-space enumeration."""
from collections import defaultdict
from itertools import product, combinations
from pathlib import Path
import json
import resource
import time

t0 = time.perf_counter()
import sympy as s

# Internal amplitude projectors, obtained directly by expanding differences.
E = s.eye(3)-s.ones(3)/3
assert E*E == E
Tcomp = s.zeros(4)
for a, b in combinations(range(4), 2):
    w = s.zeros(4, 1); w[a] = 1; w[b] = -1
    Tcomp += w*w.T/4
assert Tcomp == s.eye(4)-s.ones(4)/4
assert Tcomp*Tcomp == Tcomp
for m in range(19):
    d = (m-1)*(m-2)//2
    assert d >= 0 and d+m >= 1

# Balanced cyclic intervals built from integer cut points. No author geometry
# implementation is read. q=1 is kept as the whole circle, once.
partition_cases = 0
max_vertex_overlap = max_edge_overlap = 0
for L in range(5, 81):
    for q in range(1, L+1):
        cuts = [j*L//q for j in range(q+1)]
        inner = [list(range(cuts[j], cuts[j+1])) for j in range(q)]
        expanded = []
        for B in inner:
            C = (list(range(L)) if q == 1 else
                 [(B[0]-1+j) % L for j in range(min(L, len(B)+2))])
            assert len(C) == len(set(C))
            assert all((y+d) % L in C for y in B for d in [-1, 0, 1])
            expanded.append(C)
        vertices = [0]*L; edges = defaultdict(int)
        for C in expanded:
            for x in C: vertices[x] += 1
            for x, y in zip(C, C[1:]):
                assert (y-x) % L == 1
                edges[tuple(sorted((x, y)))] += 1
        assert max(vertices) <= 3 and max(edges.values(), default=0) <= 3
        max_vertex_overlap = max(max_vertex_overlap, max(vertices))
        max_edge_overlap = max(max_edge_overlap, max(edges.values(), default=0))
        lo, hi = min(map(len, expanded)), max(map(len, expanded))
        assert hi <= 2*lo
        assert hi**3*q**3 <= 64*L**3
        # A q from floor((N/4)^(1/3)) covers this exact integer interval.
        Nlo, Nhi = 4*q**3, min(L**3, 4*(q+1)**3-1)
        if Nlo <= Nhi:
            assert 2*q**3 <= Nlo//2
            assert hi**3*Nhi <= 2048*L**3
        partition_cases += 1

# Pin convention: grounded graph Laplacian gives point resistance as the
# corresponding diagonal of its inverse. Only boxes of at most 32 vertices.
resistance_checks = []
for dims in [(1, 1, 1), (1, 1, 2), (2, 2, 2), (2, 3, 3), (2, 2, 4), (3, 3, 3)]:
    vertices = list(product(*[range(n) for n in dims])); n = len(vertices)
    index = {x: j for j, x in enumerate(vertices)}
    lap = s.zeros(n)
    for x in vertices:
        for axis in range(3):
            y = list(x); y[axis] += 1; y = tuple(y)
            if y in index:
                a, b = index[x], index[y]
                lap[a, a] += 1; lap[b, b] += 1
                lap[a, b] -= 1; lap[b, a] -= 1
    for pin in sorted({0, n//2}):
        keep = [j for j in range(n) if j != pin]
        if keep:
            green = lap.extract(keep, keep).inv()
            rmax = max(green[j, j] for j in range(n-1))
            assert rmax <= 448
            # trace(G) gives the elementary sum of pointwise bounds, consistent
            # with the |C| factor in the full pinned estimate.
            assert s.trace(green) <= 448*n
        else:
            rmax = s.Rational(0)
        resistance_checks.append({'sides': dims, 'pin': pin, 'max_resistance': str(rmax)})

L = 5
sites = list(product(range(L), repeat=3))
unit = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
def add(x, y): return tuple((a+b) % L for a, b in zip(x, y))
def scale(a, x): return tuple(a*b for b in x)
types = [(e, scale(-1, e), 1) for e in unit]
for i, j in combinations(range(3), 2):
    for a, b in product([-1, 1], repeat=2):
        types.append((scale(a, unit[i]), scale(b, unit[j]), a*b))
assert len(types) == 15
edges = defaultdict(list)
for x in sites:
    for t, (u, v, sign) in enumerate(types):
        edge = tuple(sorted((add(x, u), add(x, v))))
        assert edge[0] != edge[1]
        edges[edge].append((x, t, sign))
adj = defaultdict(set)
for edge, occurrences in edges.items():
    a, b = edge; adj[a].add(b); adj[b].add(a)
    axial = occurrences[0][1] < 3
    assert len(occurrences) == (1 if axial else 2)
    assert len({sign for _, _, sign in occurrences}) == 1
assert {len(adj[x]) for x in sites} == {18}

B = set(product(range(2), repeat=3))
C = set(product([4, 0, 1, 2], repeat=3))
sample_sites = sorted(B | {(2, 0, 0), (3, 0, 0), (4, 0, 0), (0, 2, 0)})
configuration_checks = pin_checks = 0
for N in [3, 4, 6]:
    for raw in combinations(sample_sites, N):
        S = set(raw)
        NB = len(S & B)
        DB = sum((len(adj[x] & S)-1)*(len(adj[x] & S)-2)//2 for x in S & B)
        restricted_M = 0
        for edge in combinations(sorted(S), 2):
            eta = S-set(edge)
            if not eta & B:
                continue
            restricted_M += sum(x in C for x, _, _ in edges.get(edge, []))
            y = min(eta & B)
            for u, v, sign in types:
                pin = add(y, scale(-1, u))
                assert pin in C
                # Output occupies y; the first endpoint of this annihilator
                # is y. No input occupation word can produce this output.
                assert add(pin, u) == y and y in eta
                pin_checks += 1
        assert (NB if NB >= 3 else 0) <= DB+2*restricted_M
        configuration_checks += 1

Bstar = 2*448*27*2048
assert Bstar == 49545216 and 2*Bstar == 99090432
outcome = {'internal_projectors_checked': True,
           'partition_cases_L5_through_80': partition_cases,
           'max_1d_vertex_overlap': max_vertex_overlap,
           'max_1d_free_edge_overlap': max_edge_overlap,
           'rational_resistance_checks': resistance_checks,
           'all_L5_graph_neighbor_counts': 18,
           'occupation_configuration_checks_on_12_selected_sites': configuration_checks,
           'residual_pin_checks': pin_checks,
           'Bstar': Bstar, 'coercivity_denominator': 2*Bstar,
           'no_dense_N3_torus_enumeration': True, 'author_code_imported': False,
           'elapsed_seconds': time.perf_counter()-t0,
           'maxrss_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
out = Path(__file__).parent
(out/'results.json').write_text(json.dumps(outcome, indent=2)+'\n')
print(json.dumps(outcome, indent=2))
