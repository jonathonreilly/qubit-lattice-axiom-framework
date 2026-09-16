"""Supervisor control, block 25 sharpening (2026-09-16): the threshold of T6 raised from 1/(2 96^4) to 7/10^6.
(1) Structural facts on every executed explanation tree: at most one arrow to a predecessor per node, the nodes without one are the
noise nodes, forks = n - 1, arrows <= 3(n - 1); and the candidate lemma "every arrow points away from the root", which FAILS (counted).
(2) The subtrees of G containing the origin with <= 4 edges and <= 1 arrow to a predecessor per node, by (arrows, forks); the lift to
the typed tree is injective; each count <= the exact coefficient of the generating-function recursion; direct enumeration of the
admissible subtrees of the typed tree (<= 3 edges) equals the coefficients.  (3) The rational super-solution at (91/1000, 1000/107653)
found along the dominant eigenvector of the Jacobian at the fixed point; R-bar; the bound.  (4) The new p_0 at four weight pairs.
Exploration in floats is allowed here (not in the runner)."""
import sys, os, random
from fractions import Fraction as F
from collections import deque, defaultdict
from itertools import product, combinations
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import supervisor_control_block25_toom_core as core
x = (0, 0, 0)
TYPES = [("down", j) for j in range(3)] + [("up", j) for j in range(3)] + [("fork", (i, j)) for i in range(3) for j in range(3) if i != j]
def step(v, ty):
    kind, d = ty
    if kind == "down": return core.sub(v, core.E[d])
    if kind == "up": return core.add(v, core.E[d])
    return core.add(core.sub(v, core.E[d[1]]), core.E[d[0]])
def reverse(ty):
    kind, d = ty
    return ("up", d) if kind == "down" else ("down", d) if kind == "up" else ("fork", (d[1], d[0]))
# (1)
def facts(nodes, edges, noise_nodes, root):
    nb = {v: [] for v in nodes}
    for e, kind in edges.items():
        a, b = tuple(e); nb[a].append((b, kind)); nb[b].append((a, kind))
    parent = {root: None}; dq = deque([root])
    while dq:
        v = dq.popleft()
        for w, kind in nb[v]:
            if w not in parent: parent[w] = (v, kind); dq.append(w)
    up = sum(1 for w in nodes if w != root and parent[w][1] == "arrow" and w not in core.preds(parent[w][0]))
    downs = {v: sum(1 for w, kind in nb[v] if kind == "arrow" and w in core.preds(v)) for v in nodes}
    a = sum(1 for k in edges.values() if k == "arrow"); f = len(edges) - a; n = len(noise_nodes)
    ok = max(downs.values()) <= 1 and {v for v in nodes if downs[v] == 0} == noise_nodes and f == n - 1 and a <= 3 * (n - 1)
    return ok, up, F(a, max(n - 1, 1))
random.seed(26); sites2 = core.cone(x, 2)
configs = [{z: b for z, b in zip(sites2, bits) if b} for bits in product((0, 1), repeat=len(sites2))]
sites3 = core.cone(x, 3)
for k in range(1, 5):
    for combo in combinations(sites3, k): configs.append({z: 1 for z in combo})
for t in range(1500):
    d = random.choice((3, 4, 5, 6, 7, 8)); dens = random.choice((0.1, 0.2, 0.35, 0.5))
    configs.append({z: 1 for z in core.cone(x, d) if random.random() < dens})
ok_all = True; cases = 0; trees_with_up = 0; maxa = F(0)
for zeta in configs:
    depth = max(-core.level(z) for z in zeta) if zeta else 0
    sites = core.cone(x, max(depth, 1)); eta = core.run_automaton(sites, zeta)
    if eta[x] != 1: continue
    ex = core.Explainer(eta, zeta); nodes, edges, nn, refs = ex.explain(x)
    ok, up, ratio = facts(nodes, edges, nn, x)
    ok_all = ok_all and ok; cases += 1; trees_with_up += (up > 0); maxa = max(maxa, ratio)
print(f"(1) {cases} explained trees: <= 1 arrow to a predecessor per node, marks = nodes without one, forks = n-1, arrows <= 3(n-1): {ok_all}; max arrows/(n-1) = {maxa}")
print(f"(1) candidate lemma 'every arrow points away from the root' FAILS on {trees_with_up} of {cases} trees (a kept pole reached from below through its own arrow)")
# (2)
trees = {frozenset()}; N = {(0, 0): 1}; lifts = set(); inj = True
for _ in range(4):
    nxt = set()
    for T in trees:
        nodes = {x} | {c for (_p, c, _t) in T}; downs = defaultdict(int)
        for (p, c, ty) in T:
            if ty[0] == "down": downs[p] += 1
            if ty[0] == "up": downs[c] += 1
        for v in nodes:
            for ty in TYPES:
                w = step(v, ty)
                if w in nodes or (ty[0] == "down" and downs[v] >= 1): continue
                nxt.add(T | {(v, w, ty)})
    trees = nxt
    for T in trees:
        a = sum(1 for e in T if e[2][0] != "fork"); N[(a, len(T) - a)] = N.get((a, len(T) - a), 0) + 1
        parent = {c: (p, ty) for (p, c, ty) in T}; words = set()
        for v in list(parent) + [x]:
            w = []
            while v in parent:
                p, ty = parent[v]; w.append(ty); v = p
            words.add(tuple(reversed(w)))
        key = frozenset(words); inj = inj and key not in lifts; lifts.add(key)
A, FM = 5, 5
def pmul(P, Q):
    R = defaultdict(int)
    for (a1, f1), c1 in P.items():
        for (a2, f2), c2 in Q.items():
            if a1 + a2 <= A and f1 + f2 <= FM: R[(a1 + a2, f1 + f2)] += c1 * c2
    return dict(R)
def ppow(P, n):
    R = {(0, 0): 1}
    for _ in range(n): R = pmul(R, P)
    return R
def one_plus(P, c, da, df):
    R = {(0, 0): 1}
    for (a, f), v in P.items():
        if a + da <= A and f + df <= FM: R[(a + da, f + df)] = R.get((a + da, f + df), 0) + c * v
    return R
D = U = Fp = {(0, 0): 1}
for _ in range(A + FM + 1):
    xU, xD3, yF = one_plus(U, 1, 1, 0), one_plus(D, 3, 1, 0), one_plus(Fp, 1, 0, 1)
    D, U, Fp = pmul(pmul(ppow(xU, 2), xD3), ppow(yF, 6)), pmul(ppow(xU, 3), ppow(yF, 6)), pmul(pmul(ppow(xU, 3), xD3), ppow(yF, 5))
xU, xD3, yF = one_plus(U, 1, 1, 0), one_plus(D, 3, 1, 0), one_plus(Fp, 1, 0, 1)
Rgf = pmul(pmul(ppow(xU, 3), xD3), ppow(yF, 6))
print(f"(2) trees of G with <= 4 edges: {sum(N.values())}; lift injective: {inj}")
for k in sorted(N): print(f"(2) a={k[0]} f={k[1]}: N = {N[k]} <= coefficient {Rgf.get(k, 0)} {'(equal)' if N[k] == Rgf.get(k, 0) else ''}")
print("(2) all N <= coefficient:", all(N[k] <= Rgf.get(k, 0) for k in N))
def enumerate_T(kmax):
    trees = {frozenset([()])}; counts = defaultdict(int)
    for _ in range(kmax):
        nxt = set()
        for T in trees:
            downs = defaultdict(int)
            for w in T:
                if w and w[-1][0] == "down": downs[w[:-1]] += 1
                if w and w[-1][0] == "up": downs[w] += 1
            for w in T:
                last = w[-1] if w else None
                for ty in TYPES:
                    if (last is not None and ty == reverse(last)) or (ty[0] == "down" and downs[w] >= 1): continue
                    nw = w + (ty,)
                    if nw not in T: nxt.add(T | {nw})
        trees = nxt
        for T in trees:
            a = sum(1 for w in T if w and w[-1][0] != "fork"); counts[(a, len(T) - 1 - a)] += 1
    return counts
cT = enumerate_T(3)
print("(2) direct enumeration of admissible subtrees of the typed tree (<= 3 edges) equals the coefficients:", all(cT.get(k, 0) == Rgf.get(k, 0) for k in set(cT) | {k for k in Rgf if 1 <= sum(k) <= 3}))
# (3) exploration in floats: the edge of the domain and the best t; then the exact certificate
def converges(xx, yy, nit=4000):
    Dv = Uv = Fv = 1.0
    for i in range(nit):
        D2 = (1 + xx * Uv) ** 2 * (1 + 3 * xx * Dv) * (1 + yy * Fv) ** 6; U2 = (1 + xx * Uv) ** 3 * (1 + yy * Fv) ** 6; F2 = (1 + xx * Uv) ** 3 * (1 + 3 * xx * Dv) * (1 + yy * Fv) ** 5
        if max(D2, U2, F2) > 1e6: return False
        if abs(D2 - Dv) < 1e-13 and abs(U2 - Uv) < 1e-13 and abs(F2 - Fv) < 1e-13: return True
        Dv, Uv, Fv = D2, U2, F2
    return True
def yc(xx):
    lo, hi = 0.0, 1.0
    for _ in range(50):
        mid = (lo + hi) / 2
        if converges(xx, mid): lo = mid
        else: hi = mid
    return lo
best = max(((tt ** 3 * yc(tt), tt) for tt in [i / 1000 for i in range(60, 130, 2)]))
print(f"(3) exploration: best t^3 y_c(t) = {best[0]:.4e} at t = {best[1]}; y_c(0.091) = {yc(0.091):.6f} > s = 1000/107653 = {1000/107653:.6f}")
t = F(91, 1000); s = F(1000, 107653); eps0 = t ** 3 * s
Db, Ub, Fb = F(3290957526219, 10 ** 12), F(514547476033, 25 * 10 ** 10), F(943741493637, 25 * 10 ** 10)
rD = (1 + t * Ub) ** 2 * (1 + 3 * t * Db) * (1 + s * Fb) ** 6; rU = (1 + t * Ub) ** 3 * (1 + s * Fb) ** 6; rF = (1 + t * Ub) ** 3 * (1 + 3 * t * Db) * (1 + s * Fb) ** 5
Rbar = (1 + t * Ub) ** 3 * (1 + 3 * t * Db) * (1 + s * Fb) ** 6
print(f"(3) certificate exact: {Db >= rD and Ub >= rU and Fb >= rF}; slacks {[float(u - v) for u, v in ((Db, rD), (Ub, rU), (Fb, rF))]}; R-bar = {float(Rbar):.6f} < 3.91: {Rbar < F(391, 100)}; eps0 = {eps0}; eps0 R-bar = {float(eps0 * Rbar):.4e} <= 3e-5: {eps0 * Rbar <= F(3, 10 ** 5)}")
print(f"(3) partial sum of the recursion over <= 5 edges at (t, s): {float(sum(c * t ** a * s ** f for (a, f), c in Rgf.items())):.6f} (<= R-bar)")
print(f"(3) improvement of the threshold: {float(eps0 * 169869312):.1f}")
# (4)
def eps(p, q, r):
    p, q, r = F(p), F(q), F(r)
    return max(1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3), 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3), 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3))
for (q, r), old in (((1, 2), 339738628), ((1, 1), 169869315), ((2, 4), 679477255), ((1, 3), 509607941)):
    lo, hi = 1, 10 ** 9
    while lo < hi:
        mid = (lo + hi) // 2
        if eps(mid, q, r) <= eps0: hi = mid
        else: lo = mid + 1
    print(f"(4) p_0 at (p,{q},{r}) = {lo} (was {old}); eps(p_0) <= eps0 < eps(p_0 - 1): {eps(lo, q, r) <= eps0 < eps(lo - 1, q, r)}")
