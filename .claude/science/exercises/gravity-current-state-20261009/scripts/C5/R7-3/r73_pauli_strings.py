"""R7-3 script 2 (checked, exact GF(2) algebra): Kitaev spin strings on the brick-wall subgraph of Z^2
(one qubit per site; vertical bond (X,Y)-(X,Y+1) iff X+Y even).  Bond operator K_ab = s^a_a s^a_b,
type z = vertical, x = A(X,Y)-B(X+1,Y), y = A(X,Y)-B(X-1,Y)  (A: X+Y even).
In the flux-free sector the string S_gamma(i,j) = prod of K along a path gamma equals (phase) x i c_i c_j.
Checks (Pauli strings as GF(2) vectors; phases dropped; commutation via the symplectic form):
  (a) S_gamma and S_gamma' (two different random paths, same endpoints) differ by a product of
      plaquette operators W_p  -> equal on the W_p = +1 sector (path independence);
  (b) commutation of strings = Majorana-bilinear rule: [c_i c_j, c_k c_l] = 0 iff |{i,j} & {k,l}| even;
  (c) every string commutes with every W_p (flux sectors are conserved by every string-built law);
  (d) a single-site s^z_j anticommutes with exactly the two W_p sharing j's z-bond (a local operator
      creates the static vison pair)."""
import numpy as np, random
random.seed(7); np.random.seed(7)
LX, LY = 14, 12
sites = [(X, Y) for X in range(LX) for Y in range(LY)]
sid = {s: i for i, s in enumerate(sites)}
n = len(sites)
def isA(X, Y): return (X + Y) % 2 == 0
bonds = {}  # frozenset -> type
for (X, Y) in sites:
    if isA(X, Y):
        if (X+1, Y) in sid: bonds[frozenset([(X, Y), (X+1, Y)])] = 'x'
        if (X-1, Y) in sid: bonds[frozenset([(X, Y), (X-1, Y)])] = 'y'
        if (X, Y+1) in sid: bonds[frozenset([(X, Y), (X, Y+1)])] = 'z'
adj = {s: [] for s in sites}
for b in bonds:
    a, c = tuple(b); adj[a].append(c); adj[c].append(a)
def pauli(site, t):
    v = np.zeros(2*n, dtype=np.uint8); i = sid[site]
    if t in 'xy': v[i] = 1          # x-part
    if t in 'yz': v[n+i] = 1        # z-part
    return v
def Kvec(a, c):
    t = bonds[frozenset([a, c])]; return pauli(a, t) ^ pauli(c, t)
def string(path):
    v = np.zeros(2*n, dtype=np.uint8)
    for a, c in zip(path[:-1], path[1:]): v ^= Kvec(a, c)
    return v
def sym(u, v):  # 0 commute, 1 anticommute
    return int((u[:n] @ v[n:] + u[n:] @ v[:n]) % 2)
plaq = []
for (X, Y) in sites:
    if isA(X, Y) and (X+2, Y+1) in sid:
        loop = [(X, Y), (X+1, Y), (X+2, Y), (X+2, Y+1), (X+1, Y+1), (X, Y+1), (X, Y)]
        plaq.append(string(loop))
P = np.array(plaq)
def gf2_rank(M):
    M = M.copy() % 2; r = 0; rows, cols = M.shape
    for c in range(cols):
        piv = [i for i in range(r, rows) if M[i, c]]
        if not piv: continue
        M[[r, piv[0]]] = M[[piv[0], r]]
        for i in range(rows):
            if i != r and M[i, c]: M[i] ^= M[r]
        r += 1
        if r == rows: break
    return r
rP = gf2_rank(P)
def in_span(v):
    return gf2_rank(np.vstack([P, v])) == rP
def rand_path(a, b):  # randomized BFS-like walk: shortest path in a randomly reweighted graph
    import heapq
    w = {}
    dist = {a: 0.0}; prev = {}; pq = [(0.0, a)]
    while pq:
        d, u = heapq.heappop(pq)
        if u == b: break
        if d > dist[u]: continue
        for v in adj[u]:
            key = frozenset([u, v]); w.setdefault(key, 1 + 3*random.random())
            nd = d + w[key]
            if nd < dist.get(v, 1e18): dist[v] = nd; prev[v] = u; heapq.heappush(pq, (nd, v))
    path = [b]
    while path[-1] != a: path.append(prev[path[-1]])
    return path[::-1]
inner = [s for s in sites if 1 <= s[0] < LX-1 and 1 <= s[1] < LY-1]
# (a) path independence modulo plaquettes
okA = 0; NA = 200
for _ in range(NA):
    a, b = random.sample(inner, 2)
    p1, p2 = rand_path(a, b), rand_path(a, b)
    okA += in_span(string(p1) ^ string(p2))
print("(a) path independence mod W_p: %d/%d pairs of random paths differ by a product of plaquettes (#plaquettes=%d, GF2 rank %d)" % (okA, NA, len(plaq), rP))
# (b) Majorana commutation rule
okB = 0; NB = 3000; cnt = {0: 0, 1: 0, 2: 0}
for _ in range(NB):
    a, b = random.sample(inner, 2)
    r = random.random()
    if r < 0.3: c, d = random.sample([s for s in inner if s not in (a, b)], 2)
    elif r < 0.7: c = random.choice([a, b]); d = random.choice([s for s in inner if s not in (a, b)])
    else: c, d = b, a
    ov = len({a, b} & {c, d}); cnt[ov] += 1
    s1 = string(rand_path(a, b)); s2 = string(rand_path(c, d))
    okB += (sym(s1, s2) == (ov % 2))
print("(b) commutation = Majorana-bilinear rule: %d/%d (overlap counts 0/1/2: %s)" % (okB, NB, cnt))
# (c) strings commute with all plaquettes
okC = 0; NC = 300
for _ in range(NC):
    a, b = random.sample(inner, 2); s = string(rand_path(a, b))
    okC += all(sym(s, p) == 0 for p in plaq)
print("(c) strings commute with every W_p: %d/%d" % (okC, NC))
# (d) single-site s^z on an A site anticommutes with exactly two plaquettes (those sharing its z bond)
res = []
for s in [x for x in sites if isA(*x) and 3 <= x[0] <= LX-4 and 3 <= x[1] <= LY-4]:
    v = pauli(s, 'z'); res.append(sum(sym(v, p) for p in plaq))
print("(d) number of W_p flipped by a single s^z_j (interior A sites): %s" % sorted(set(res)))
# Pauli weight of a straight-ish string vs distance (locality bookkeeping)
for dX in [2, 6, 10]:
    a = (1, 2); b = (1 + dX, 2 + (dX % 2))
    if b in sid:
        s = string(rand_path(a, b)); w = int(np.sum((s[:n] | s[n:]) > 0))
        print("    string (1,2)->%s: Pauli weight %d" % (str(b), w))
