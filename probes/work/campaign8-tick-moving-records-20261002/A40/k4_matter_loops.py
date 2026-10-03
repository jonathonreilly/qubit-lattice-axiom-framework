"""A40 k4: generalized Theorem S for matter living on some roles only.
Supplied toy geometry.  Layout s = 0; its symmetry group G = O (24 proper turns about a vertex site)
semidirect 2Z^3.  Matter on a union M of roles, hops between M-sites at Euclidean length in HOPSET.
For each minimal loop (triangle, or chordless square) through the origin cell:
  - find every g in G that maps the loop onto itself reversing its orientation;
  - if such a g fixes two loop sites (no loop bond fixed), then
       exactly-kept real signs force the loop's sign product to +1 (Theorem S argument), and
       the state-level parity route gives flux sign p(x)p(c): forced +1 if x, c have the same role
       (they differ by a 2Z^3 translation along g's axis), allowed -1 if their roles differ;
  - otherwise the loop is unconstrained by reversal ('free').
Then the coarse lattice with a dynamical link field: uniform W = -1 on every plaquette is mapped by
every turn to a configuration with the same holonomies; the gauge function is found explicitly.
"""
import itertools, signal
import numpy as np
signal.alarm(28)
ROLES = ['V', 'E', 'F', 'C']
def role(y):
    w = sum(c % 2 for c in y)
    return 'V' if w == 0 else 'E' if w == 1 else 'F' if w == 2 else 'C'
def rolefull(y):
    r = tuple(c % 2 for c in y); w = sum(r)
    if w in (0, 3): return role(y)
    return role(y) + 'xyz'[r.index(1 if w == 1 else 0)]
ROT = []
for P in itertools.permutations(range(3)):
    for s in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, P[i]] = s[i]
        if round(np.linalg.det(M)) == 1: ROT.append(M)
assert len(ROT) == 24
def d2(a, b): return sum((a[k] - b[k]) ** 2 for k in range(3))

def loops(M, hop2):
    box = [y for y in itertools.product(range(-2, 4), repeat=3) if role(y) in M]
    S = set(box)
    nb = {x: [y for y in box if 0 < d2(x, y) and d2(x, y) in hop2] for x in box}
    base = [y for y in itertools.product((0, 1), repeat=3) if role(y) in M]
    tri, sq = set(), set()
    for a in base:
        for b in nb[a]:
            for c in nb[b]:
                if c != a and a in nb[c]:
                    tri.add(frozenset((a, b, c)))
                for d in nb[c]:
                    if d not in (a, b) and c != a and a in nb[d] and c not in nb[a] and d not in nb[b]:
                        sq.add((a, b, c, d))
    sqs = {}
    for q in sq:
        key = frozenset(q)
        sqs.setdefault(key, q)
    return [tuple(t) for t in tri], list(sqs.values())

def classify(loop):
    pts = [np.array(p) for p in loop]
    n = len(loop)
    cent2 = sum(pts)  # n * centroid
    best = 'free'
    for R in ROT:
        t2 = cent2 - R @ cent2           # n * t
        if np.any(t2 % n): continue
        t = t2 // n
        if np.any(t % 2): continue
        img = [tuple(R @ p + t) for p in pts]
        if set(img) != set(loop): continue
        idx = [loop.index(q) for q in img]
        fwd = all((idx[(i + 1) % n] - idx[i]) % n == 1 for i in range(n))
        if fwd: continue                  # orientation kept
        fixed = [loop[i] for i in range(n) if idx[i] == i]
        if len(fixed) == 2 and n % 2 == 0:
            same = role(fixed[0]) == role(fixed[1])
            tag = 'forced0' if same else 'parity'
            if tag == 'forced0' or best == 'free': best = tag
    return best

HOPSETS = {'len1': {1}, 'len<=sqrt2': {1, 2}, 'len<=2 (all star-local)': {1, 2, 4}}
print("matter set | hops | triangles: free/parity/forced0 | chordless squares: free/parity/forced0")
for k in range(1, 5):
    for Mset in itertools.combinations(ROLES, k):
        M = set(Mset)
        for hname, h2 in HOPSETS.items():
            tri, sq = loops(M, h2)
            if not tri and not sq: continue
            ct = [classify(list(t)) for t in tri]; cs = [classify(list(q)) for q in sq]
            f = lambda c: f"{c.count('free')}/{c.count('parity')}/{c.count('forced0')}"
            print(f"{''.join(Mset):5s} | {hname:24s} | tri {f(ct):9s} | sq {f(cs)}")

# ---- coarse lattice (matter on V only) with a dynamical U(1) link field: uniform pi flux
L = 4   # coarse torus, sites = 2Z^3 / 2L  (coarse coordinates)
def ks(x, a):   # KS signs: eta_x = 1, eta_y = (-1)^x, eta_z = (-1)^(x+y)
    return [1, (-1) ** x[0], (-1) ** (x[0] + x[1])][a]
E = np.eye(3, dtype=int)
def plaq(eta, x, a, b):
    xa = tuple((np.array(x) + E[a]) % L); xb = tuple((np.array(x) + E[b]) % L)
    return eta[(x, a)] * eta[(xa, b)] * eta[(xb, a)] * eta[(x, b)]
sites = list(itertools.product(range(L), repeat=3))
eta = {(x, a): ks(x, a) for x in sites for a in range(3)}
print("KS on coarse 4^3 torus: all plaquettes -1:", all(plaq(eta, x, a, b) == -1 for x in sites for a in range(3) for b in range(a + 1, 3)))
ok_all = True
for R in ROT:
    eta2 = {}
    for x in sites:
        for a in range(3):
            y = tuple(R @ np.array(x) % L); v = R @ E[a]
            ax = int(np.nonzero(v)[0][0])
            if v[ax] > 0: eta2[(y, ax)] = eta[(x, a)]
            else: eta2[(tuple((np.array(y) - E[ax]) % L), ax)] = eta[(x, a)]
    flux_ok = all(plaq(eta2, x, a, b) == -1 for x in sites for a in range(3) for b in range(a + 1, 3))
    # explicit gauge g(x) in {+-1}: eta2(x,a) = g(x) eta(x,a) g(x+a)
    g = {(0, 0, 0): 1}; todo = [(0, 0, 0)]; cons = True
    while todo:
        x = todo.pop()
        for a in range(3):
            xa = tuple((np.array(x) + E[a]) % L)
            val = g[x] * eta2[(x, a)] * eta[(x, a)]
            if xa in g:
                cons &= (g[xa] == val)
            else:
                g[xa] = val; todo.append(xa)
    ok_all &= flux_ok and cons
print("each of the 24 turns about a coarse site maps KS to a gauge-equivalent pattern (all plaquettes -1, explicit gauge):", ok_all)
