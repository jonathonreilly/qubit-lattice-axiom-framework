"""T49 Part A2: verify the (3,1,0) invariant independently, then ask whether it
gaps (Majorana-masses) the low-energy KS modes.

1. Build the group element g that reverses the pair (0, d) (rotation C2 about the
   axis perpendicular to d, composed with translation) from the generators, read
   its sign s_g(0) s_g(d).  Predict: NN pair -> +1 (pairing forbidden, hopping
   allowed), d=(3,1,0) -> -1 (pairing allowed, hopping forbidden).
2. Build the invariant pairing matrix Delta for d=(3,1,0) by propagating from the
   union-find components, check M Delta M^T = Delta for all six generators and
   Delta^T = -Delta, Delta != 0.
3. Diagonalise the BdG matrix H = [[h, lam*Delta],[-lam*Delta, -h]] on an L^3 torus
   for several lam and report the smallest |E| (the KS Dirac points are at E = 0
   or at the finite-size level).
"""
import itertools, sys
import numpy as np
sys.argv = [sys.argv[0]] + sys.argv[1:]
L = int(sys.argv[1]) if len(sys.argv) > 1 else 12
N = L ** 3
def idx(x, y, z): return ((x % L) * L + (y % L)) * L + (z % L)
def coords(i): return (i // (L * L), (i // L) % L, i % L)
def eta(a, v):
    x, y, z = v
    return 1 if a == 0 else (-1 if x % 2 else 1) if a == 1 else (-1 if (x + y) % 2 else 1)
hop = {}
for i in range(N):
    v = coords(i)
    for a in range(3):
        w = list(v); w[a] += 1; j = idx(*w); e = eta(a, v)
        hop[(i, j)] = e; hop[(j, i)] = e
def gen_perm(kind):
    f = {"tx": lambda v: (v[0]+1, v[1], v[2]), "ty": lambda v: (v[0], v[1]+1, v[2]),
         "tz": lambda v: (v[0], v[1], v[2]+1), "c4z": lambda v: (-v[1], v[0], v[2]),
         "c4x": lambda v: (v[0], -v[2], v[1]), "c3": lambda v: (v[1], v[2], v[0])}[kind]
    return np.array([idx(*f(coords(i))) for i in range(N)])
def solve_signs(perm):
    s = np.zeros(N, dtype=int); s[0] = 1; stack = [0]
    nb = [[] for _ in range(N)]
    for (i, j) in hop: nb[i].append(j)
    while stack:
        v = stack.pop()
        for w in nb[v]:
            val = s[v] * hop[(v, w)] * hop[(perm[v], perm[w])]
            if s[w] == 0: s[w] = val; stack.append(w)
            else: assert s[w] == val
    return s
gens = {k: (gen_perm(k), None) for k in ["tx", "ty", "tz", "c4z", "c4x", "c3"]}
gens = {k: (p, solve_signs(p)) for k, (p, _) in gens.items()}
def compose(g2, g1):  # apply g1 then g2:  c_v -> s1(v) c_{p1 v} -> s1(v) s2(p1 v) c_{p2 p1 v}
    p1, s1 = g1; p2, s2 = g2
    return (p2[p1], s1 * s2[p1])
def power(g, n):
    out = (np.arange(N), np.ones(N, dtype=int))
    for _ in range(n): out = compose(g, out)
    return out

print("== step 1: sign s_g(i)s_g(j) of the pair-reversing group element ==")
# NN pair: i = 0, j = (1,0,0). C2 about z (c4z^2) then translate by (1,0,0)
def reversing_element(d):
    # choose a proper C2 rotation R with R d = -d among c4z^2, c4x^2, conj by c3/c4
    cands = {"C2z": power(gens["c4z"], 2), "C2x": power(gens["c4x"], 2)}
    # C2y = c3 C2x c3^-1 ; face diagonal axes via c4 conjugation: build all from group closure
    rots = {"C2z": cands["C2z"], "C2x": cands["C2x"], "C2y": compose(gens["c3"], compose(cands["C2x"], power(gens["c3"], 2)))}
    return rots
d = (1, 0, 0)
def test_pair(d):
    i = 0; j = idx(*d)
    rots = reversing_element(d)
    # rotation matrices as maps on coordinates
    mats = {"C2z": np.diag([-1, -1, 1]), "C2x": np.diag([1, -1, -1]), "C2y": np.diag([-1, 1, -1])}
    for name, M in mats.items():
        if tuple(M @ np.array(d)) == tuple(-np.array(d)):
            p, s = rots[name]
            # translation part t = j - R(i) = d (i = origin); translate by d: use tx,ty,tz powers
            g = (p, s)
            for a, kind in enumerate(["tx", "ty", "tz"]):
                dd = d[a]
                for _ in range(abs(dd)):
                    step = gens[kind]
                    if dd < 0:
                        # inverse translation: perm inverse with signs
                        pi = np.argsort(step[0]); si = step[1][pi]
                        step = (pi, si)
                    g = compose(step, g)
            p, s = g
            # check that g swaps i and j
            swaps = (p[i] == j and p[j] == i)
            return name, swaps, int(s[i] * s[j])
    return None, None, None
for d in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 1, 1), (2, 0, 0), (2, 1, 0), (3, 0, 0), (3, 1, 0), (1, 3, 0), (5, 1, 0)]:
    print(f"d = {d}: axis, swaps?, sign s_i s_j =", test_pair(d))

print("\n== step 2: build invariant Delta for the class of d=(3,1,0), verify invariance ==")
rots = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        M = np.zeros((3, 3), dtype=int)
        for r in range(3): M[r, perm[r]] = signs[r]
        if round(np.linalg.det(M)) == 1: rots.append(M)
def class_of(d):
    orb = set(tuple(int(t) for t in M @ np.array(d)) for M in rots)
    return orb | set(tuple(-t for t in o) for o in orb)
def build_invariant(d, kappa=-1):
    cls = class_of(d)
    nodes = []
    for i in range(N):
        v = coords(i)
        for dd in cls:
            j = idx(v[0]+dd[0], v[1]+dd[1], v[2]+dd[2])
            if i < j: nodes.append((i, j))
    nodes = sorted(set(nodes))
    val = {}
    # BFS assignment: x_{pi,pj} = s_i s_j x_{ij}
    start = nodes[0]; val[start] = 1; stack = [start]; ok = True
    while stack:
        (i, j) = stack.pop()
        for kind, (perm, s) in gens.items():
            pi, pj = int(perm[i]), int(perm[j])
            x = s[i] * s[j] * val[(i, j)]
            key = (pi, pj) if pi < pj else (pj, pi)
            x = x if pi < pj else kappa * x
            if key in val:
                if val[key] != x: ok = False
            else:
                val[key] = x; stack.append(key)
    return nodes, val, ok
nodes, val, ok = build_invariant((3, 1, 0), -1)
print("class size (unordered pairs):", len(nodes), " reached by one orbit:", len(val), " consistent:", ok)
Delta = np.zeros((N, N))
for (i, j), x in val.items():
    Delta[i, j] = x; Delta[j, i] = -x
print("antisymmetric:", np.allclose(Delta, -Delta.T), " nonzero entries:", int(np.count_nonzero(Delta)))
worst = 0
for kind, (perm, s) in gens.items():
    Dn = np.zeros((N, N))
    ii, jj = np.nonzero(Delta)
    Dn[perm[ii], perm[jj]] = s[ii] * s[jj] * Delta[ii, jj]
    worst = max(worst, np.abs(Dn - Delta).max())
print("max |g.Delta - Delta| over the six generators:", worst)
# hopping matrix
h = np.zeros((N, N))
for (i, j), e in hop.items(): h[i, j] = e
print("hopping symmetric:", np.allclose(h, h.T))

print("\n== step 3: BdG spectrum of h + lam*Delta, L =", L, "==")
def lowest(lam, extra=None):
    H = np.block([[h, lam * Delta], [-lam * Delta, -h]])
    E = np.linalg.eigvalsh(H)
    a = np.sort(np.abs(E))
    return a[:8]
for lam in [0.0, 0.02, 0.05, 0.1, 0.2, 0.4]:
    print(f"lam={lam:5.2f}  smallest |E| (4 pairs): ", np.round(lowest(lam)[::2], 5))
