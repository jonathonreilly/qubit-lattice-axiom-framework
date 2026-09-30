"""T42 census: licence (V) supports, pseudoscalar carriers, closure, record-Gibbs range.
Exact, deterministic.  Pre-registration: PREREG.md (tests A-D)."""
import itertools, sys
from itertools import product, permutations

# ---------------------------------------------------------------- lattice helpers
def add(p, q): return tuple(a + b for a, b in zip(p, q))
def sub(p, q): return tuple(a - b for a, b in zip(p, q))
def dist(p, q): return sum(abs(a - b) for a, b in zip(p, q))
def unit(n, mu, s=1):
    v = [0] * n; v[mu] = s; return tuple(v)

def link_ends(l):
    base, mu = l
    return base, add(base, unit(len(base), mu))

def plaq_links(base, mu, nu):
    n = len(base)
    return [(base, mu), (add(base, unit(n, mu)), nu), (add(base, unit(n, nu)), mu), (base, nu)]

def compat(l1, l2):
    a, b = link_ends(l1); c, d = link_ends(l2)
    ok12 = all(min(dist(p, a), dist(p, b)) <= 1 for p in (c, d))
    ok21 = all(min(dist(p, c), dist(p, d)) <= 1 for p in (a, b))
    return ok12 and ok21

def licensed(S):
    S = list(S)
    return all(compat(S[i], S[j]) for i in range(len(S)) for j in range(i, len(S)))

def affine_dim(S):
    pts = set()
    for l in S:
        pts.update(link_ends(l))
    pts = list(pts)
    if len(pts) <= 1: return 0
    import numpy as np
    M = np.array([sub(p, pts[0]) for p in pts[1:]])
    return int(np.linalg.matrix_rank(M))

# hyperoctahedral group, for shape canonicalisation
def group(n):
    els = []
    for perm in permutations(range(n)):
        for signs in product([1, -1], repeat=n):
            els.append((perm, signs))
    return els

def gmap_point(g, x):
    perm, signs = g
    y = [0] * len(x)
    for mu in range(len(x)):
        y[perm[mu]] = signs[mu] * x[mu]
    return tuple(y)

def gmap_link(g, l):
    perm, signs = g
    base, mu = l
    n = len(base)
    gb = gmap_point(g, base)
    d = perm[mu]
    if signs[mu] == 1:
        return (gb, d)
    return (sub(gb, unit(n, d)), d)

def canon_shape(S, G):
    best = None
    for g in G:
        im = [gmap_link(g, l) for l in S]
        mn = tuple(min(l[0][i] for l in im) for i in range(len(im[0][0])))
        t = tuple(sorted((sub(l[0], mn), l[1]) for l in im))
        if best is None or t < best: best = t
    return best

# ---------------------------------------------------------------- Bron-Kerbosch
def maximal_cliques(nodes, adj):
    out = []
    def bk(R, P, X):
        if not P and not X:
            out.append(R); return
        piv = max(P | X, key=lambda u: len(adj[u] & P))
        for v in list(P - adj[piv]):
            bk(R | {v}, P & adj[v], X & adj[v])
            P = P - {v}; X = X | {v}
    bk(set(), set(nodes), set())
    return out

def links_in_C1(n, l0):
    a, b = link_ends(l0)
    sites = set()
    for c in (a, b):
        sites.add(c)
        for mu in range(n):
            for s in (1, -1):
                sites.add(add(c, unit(n, mu, s)))
    L = set()
    for p in sites:
        for mu in range(n):
            q = add(p, unit(n, mu))
            if q in sites: L.add((p, mu))
    return sorted(L), sites

def testA(n):
    print(f"\n=== A. licence census in Z^{n} ===")
    l0 = ((0,) * n, 0)
    L, sites = links_in_C1(n, l0)
    print(f"|C_1(l0)| = {len(sites)} sites, {len(L)} links among them")
    idx = {l: i for i, l in enumerate(L)}
    adj = {i: set() for i in range(len(L))}
    for i, j in itertools.combinations(range(len(L)), 2):
        if compat(L[i], L[j]): adj[i].add(j); adj[j].add(i)
    i0 = idx[l0]
    cand = adj[i0]
    cl = maximal_cliques(cand, adj)
    cl = [c | {i0} for c in cl]
    G = group(n)
    shapes = {}
    for c in cl:
        S = [L[i] for i in c]
        sh = canon_shape(S, G)
        shapes.setdefault(sh, 0)
        shapes[sh] += 1
    print(f"maximal licensed supports containing l0: {len(cl)}; distinct shapes up to translation+O_h: {len(shapes)}")
    for sh, k in shapes.items():
        S = list(sh)
        verts = set()
        for l in S: verts.update(link_ends(l))
        # star? plaquette?
        common = None
        for l in S:
            e = set(link_ends(l)); common = e if common is None else common & e
        is_star = bool(common)
        is_plaq = (len(S) == 4 and affine_dim(S) == 2 and len(verts) == 4)
        print(f"  shape with {len(S)} links, {len(verts)} vertices, affine dim {affine_dim(S)}, "
              f"star={is_star}, plaquette={is_plaq}  (x{k} in the l0-rooted list)")
    return shapes

# ---------------------------------------------------------------- B. carriers
def support_of(objs):
    S = set()
    for o in objs:
        if o[0] == 'L': S.add(o[1])
        else: S.update(plaq_links(o[1], o[2], o[3]))
    return S

def all_objects(n, t_win):
    """objects rooted at origin (for first) or any translation in window"""
    Ls = [('L', (t, mu)) for t in product(range(-t_win, t_win + 1), repeat=n) for mu in range(n)]
    Ps = [('P', t, mu, nu) for t in product(range(-t_win, t_win + 1), repeat=n)
          for mu in range(n) for nu in range(mu + 1, n)]
    return Ls, Ps

def testB():
    print("\n=== B. marginal pseudoscalar carriers ===")
    n = 3; w = 3
    o = (0, 0, 0)
    # (link, plaquette) with link normal to plaquette (Hamiltonian E.B)
    tot = lic = 0
    for i in range(3):
        j, k = [a for a in range(3) if a != i]
        for t in product(range(-w, w + 1), repeat=3):
            S = support_of([('L', (o, i)), ('P', t, j, k)])
            tot += 1; lic += licensed(S)
    print(f"E.B family: link normal to plaquette, |t|_inf<={w}: {lic} licensed of {tot}")
    # (link, link) displaced along the third axis (E . curl E): E_i at 0, E_k at t, i!=k, t_j != 0
    tot = lic = 0
    for i in range(3):
        for k in range(3):
            if i == k: continue
            j = 3 - i - k
            for t in product(range(-w, w + 1), repeat=3):
                if t[j] == 0: continue
                S = support_of([('L', (o, i)), ('L', (t, k))])
                tot += 1; lic += licensed(S)
    print(f"E.curl E family: E_i at 0, E_k at t with t_j != 0 (j the third axis): {lic} licensed of {tot}")
    # any two-object support that is licensed and spans 3 axes
    Ls, Ps = all_objects(3, 2)
    objs1 = [('L', (o, m)) for m in range(3)] + [('P', o, m, nn) for m in range(3) for nn in range(m + 1, 3)]
    cnt = {}
    for a in objs1:
        for b in Ls + Ps:
            S = support_of([a, b])
            if licensed(S):
                key = (a[0] + b[0], affine_dim(S))
                cnt[key] = cnt.get(key, 0) + 1
    print("licensed two-object supports (object types, affine dimension): count")
    for k in sorted(cnt): print("   ", k, cnt[k])
    print("  -> any licensed two-object support with affine dimension 3?", any(k[1] == 3 for k in cnt))
    # three-object supports: minimal factor count with affine dimension 3
    cnt3 = {}
    Lt = [('L', (o, m)) for m in range(3)]
    for a in Lt:
        for b in Ls + Ps:
            for c in Ls + Ps:
                S = support_of([a, b, c])
                if licensed(S) and affine_dim(S) == 3:
                    key = ''.join(x[0] for x in (a, b, c))
                    cnt3[key] = cnt3.get(key, 0) + 1
    print("licensed three-object supports spanning 3 axes, by types (window |t|<=2):", cnt3)
    # 4D clover: plaquettes in complementary planes
    n = 4; w = 3
    tot = lic = 0
    pairs = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
    for (p1, p2) in pairs:
        for t in product(range(-w, w + 1), repeat=4):
            S = support_of([('P', (0,) * 4, *p1), ('P', t, *p2)])
            tot += 1; lic += licensed(S)
    print(f"clover F.Ftilde family (Z^4), complementary planes, |t|_inf<={w}: {lic} licensed of {tot}")
    # sanity: same-plane and all-plane plaquette pairs in Z^3 (prior art: zero two-plaquette unions pass)
    tot = lic = 0
    for p1 in [(0, 1), (0, 2), (1, 2)]:
        for p2 in [(0, 1), (0, 2), (1, 2)]:
            for t in product(range(-w, w + 1), repeat=3):
                if t == (0, 0, 0) and p1 == p2: continue
                S = support_of([('P', (0, 0, 0), *p1), ('P', t, *p2)])
                tot += 1; lic += licensed(S)
    print(f"sanity (06-11 note: two-plaquette unions): {lic} licensed of {tot} two-plaquette pairs in Z^3")

# ---------------------------------------------------------------- C. closure
def testC():
    print("\n=== C. closure of the licence under unions ===")
    n = 3; o = (0, 0, 0)
    star = {(o, 0), (o, 1), (o, 2), ((-1, 0, 0), 0), ((0, -1, 0), 1), ((0, 0, -1), 2)}
    print("vertex star licensed:", licensed(star))
    plaqs = []
    for (mu, nu) in [(0, 1), (0, 2), (1, 2)]:
        for s1 in (0, -1):
            for s2 in (0, -1):
                b = [0, 0, 0]; b[mu] = s1; b[nu] = s2
                plaqs.append((tuple(b), mu, nu))
    nb = 0; nl = 0; contains_EB = 0
    for (b, mu, nu) in plaqs:
        P = set(plaq_links(b, mu, nu))
        U = star | P
        nb += 1; nl += licensed(U)
        # does the union contain a link normal to the plaquette together with the plaquette?
        normal = 3 - mu - nu
        if any(l in star and l[1] == normal for l in U): contains_EB += 1
    print(f"star(v) U plaquette through v: {nl} licensed of {nb}; "
          f"{contains_EB} of {nb} unions contain a link normal to the plaquette (an E.B support)")
    # second-order support generated by two licensed terms sharing a link: two plaquettes sharing an edge
    P1 = set(plaq_links(o, 0, 1)); P2 = set(plaq_links(o, 0, 2))
    print("two plaquettes sharing the link (0,0,0)-(1,0,0): union licensed?", licensed(P1 | P2))

# ---------------------------------------------------------------- D. record-Gibbs range
def testD():
    print("\n=== D. record-Gibbs range (site language) ===")
    a, b, c, d = (0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)
    sites = [a, b, c, d]
    nadj = lambda p, q: dist(p, q) == 1
    n_clique = 0; n_orders = 0
    for order in permutations(sites):
        pos = {s: i for i, s in enumerate(order)}
        edges = set()
        for p, q in itertools.combinations(sites, 2):
            if nadj(p, q): edges.add(frozenset((p, q)))
        # recorded set of x: neighbours (inside the plaquette) before x; outside sites cannot co-record two plaquette sites
        for x in sites:
            A = [y for y in sites if nadj(x, y) and pos[y] < pos[x]]
            for p, q in itertools.combinations(A, 2): edges.add(frozenset((p, q)))
        clique = all(frozenset((p, q)) in edges for p, q in itertools.combinations(sites, 2))
        n_orders += 1; n_clique += clique
    # common neighbours of the two diagonals are inside the plaquette only:
    def commonN(p, q):
        return [s for s in itertools.product(range(-2, 4), repeat=3) if dist(s, p) == 1 and dist(s, q) == 1]
    print("common neighbours of diagonal (b,c):", commonN(b, c), " of (a,d):", commonN(a, d))
    print(f"plaquette is a clique of G_sigma in {n_clique} of {n_orders} orders")
    # E.B 5-site set: the far corner and the normal link's tip are at graph distance 3
    v = (0, 0, 0)
    S5 = [v, (1, 0, 0), (0, 1, 0), (1, 1, 0), (0, 0, 1)]
    print("E.B site set: max pairwise distance =", max(dist(p, q) for p, q in itertools.combinations(S5, 2)),
          "(G_sigma edges join sites at distance <= 2)")
    # star: centre last -> all leaves pairwise co-recorded
    ctr = (0, 0, 0)
    leaves = [add(ctr, unit(3, m, s)) for m in range(3) for s in (1, -1)]
    ok = all(dist(p, q) <= 2 for p, q in itertools.combinations(leaves, 2))
    print("closed unit neighbourhood (centre formed last) is a clique:", ok)

    print("\n--- doubled lattice: edge sites = exactly one odd coordinate ---")
    n = 3; l0 = ((0, 0, 0), 0)
    L, sites_ = links_in_C1(n, l0)
    idx = {l: i for i, l in enumerate(L)}
    adj = {i: set() for i in range(len(L))}
    for i, j in itertools.combinations(range(len(L)), 2):
        if compat(L[i], L[j]): adj[i].add(j); adj[j].add(i)
    i0 = idx[l0]
    cl = [c | {i0} for c in maximal_cliques(adj[i0], adj)]
    toedge = lambda l: add(tuple(2 * x for x in l[0]), unit(3, l[1]))
    famV = {frozenset(toedge(L[i]) for i in c) for c in cl}
    e0 = toedge(l0)
    famN = set()
    win = range(-3, 6)
    def isedge(s): return sum(x % 2 for x in s) == 1
    for y in product(win, repeat=3):
        if dist(y, e0) != 1: continue
        N = {add(y, unit(3, m, s)) for m in range(3) for s in (1, -1)} | {y}
        E = frozenset(s for s in N if isedge(s))
        famN.add(E)
    # keep maximal
    famN = {E for E in famN if not any(E < F for F in famN)}
    print(f"maximal licensed link sets through l0, as edge-site sets: {len(famV)}; "
          f"maximal edge-site sets inside a closed unit neighbourhood N(y) through the same site: {len(famN)}")
    print("families identical:", famV == famN)
    # E.B on the doubled lattice
    ctrs = product(range(-4, 6), repeat=3)
    EB = {toedge(l) for l in plaq_links((0, 0, 0), 0, 1)} | {toedge(((0, 0, 0), 2))}
    hit = [y for y in product(range(-4, 6), repeat=3)
           if all(dist(y, s) <= 1 for s in EB)]
    print("E.B edge-site set inside some N(y):", bool(hit))

if __name__ == "__main__":
    testA(3)
    testA(4)
    testB()
    testC()
    testD()
