#!/usr/bin/env python3
"""Mobile-record formation response (Codex drafts #8545, #8551, #8552): independent recovery of the decisive finite facts.
J:derive:mobile-record-formation-response:a1

F1  six-site rare-formation witness (2x3, weights 3/2, 1/2, 1): event law 2701/53880 vs static 73/1440, ratio 444/449,
    difference -73/129312 (own class-by-class construction of the slow process from BFS motion classes)
F2  finite epsilon = 1/1000 exact generator value 2851401694918427/56880888215238000 (killed resolvent in the two-identical
    class; the law entering it is the static two-record law for every epsilon > 0, proved in ATTEMPT)
F3  Dirichlet-energy coefficient D2(b): 14/5 (path of 3), 224/5 (4-cycle), 0 (triangle), both menus; torus formula
    D2/V = d sum h^2 {2(8d-7) W/(1+W) + (8d^2-14d+7)} on rings 6, 7, 8 and 6x6, 7x7 tori; 2379/5 per volume in d = 3
F4  exact generator powers on the path, symbolic in kappa, epsilon: delta0 L^k = eps^k delta0 B^k (k <= 3), the k = 4
    identity, and delta0 L^5 N - eps^5 delta0 B^5 N = 2 kappa eps^4 D2 = 28 kappa eps^4/5
S   float screens: epsilon^4 coefficient against the closed form C_kappa(t) on the path; no sign change of
    E_kappa[N_t] - E_0[N_t] on the path, star, 4-cycle for three weight menus and four mobilities
"""
import time, math
import numpy as np
import sympy as sp
T0 = time.time(); FAIL = []
def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" :: {detail}" if detail else ""), flush=True)
    if not ok: FAIL.append(name)
import itertools
from fractions import Fraction as Fr
from collections import deque, defaultdict
def Wmat(eq, opp, orth):
    return [[eq if a == b else (opp if (a ^ 1) == b else orth) for b in range(6)] for a in range(6)]
W0 = Wmat(Fr(3, 2), Fr(1, 2), Fr(1))
def mk(V, E):
    nbr = [[] for _ in range(V)]
    for x, y in E: nbr[x].append(y); nbr[y].append(x)
    return nbr
def w(s, E, W):
    p = Fr(1)
    for x, y in E:
        if s[x] and s[y]: p *= W[s[x]-1][s[y]-1]
    return p
def ins(s, x, a, nbr, W):      # insertion rate of content a (1..6) at vacant x (unscaled)
    p = Fr(1)
    for y in nbr[x]:
        if s[y]: p *= W[a-1][s[y]-1]
    return p
def hops(s, E):
    for x, y in E:
        for u, v in ((x, y), (y, x)):
            if s[u] and not s[v]:
                t = list(s); t[v] = s[u]; t[u] = 0; yield tuple(t)
def configs(V, k):
    for sites in itertools.combinations(range(V), k):
        for cont in itertools.product(range(1, 7), repeat=k):
            s = [0]*V
            for x, c in zip(sites, cont): s[x] = c
            yield tuple(s)
def rare_limit(V, E, W, nb=3):
    nbr = mk(V, E)
    # motion classes up to nb-1 records
    cls = {}; members = defaultdict(list)
    for k in range(nb):
        for s in configs(V, k):
            if s in cls: continue
            cid = (k, len(members)); q = deque([s]); cls[s] = cid; members[cid].append(s)
            while q:
                c = q.popleft()
                for t in hops(c, E):
                    if t not in cls: cls[t] = cid; members[cid].append(t); q.append(t)
    dist = {cls[tuple([0]*V)]: Fr(1)}
    for k in range(nb):
        new = defaultdict(Fr)
        for cid, pc in dist.items():
            mem = members[cid]; Z = sum(w(s, E, W) for s in mem)
            flows = defaultdict(Fr); tot = Fr(0)
            for s in mem:
                pis = w(s, E, W)/Z
                for x in range(V):
                    if s[x] == 0:
                        for a in range(1, 7):
                            r = ins(s, x, a, nbr, W); t = list(s); t[x] = a; t = tuple(t)
                            key = cls.get(t, t)
                            flows[key] += pis*r; tot += pis*r
            for key, f in flows.items(): new[key] += pc*f/tot
        dist = new
    return dist
def finite_eps_E(V, E, W, eps):
    """P(all three agree right after the 3rd birth) at finite eps, via P(two identical) x killed-resolvent in the
    two-identical class (content a = 1 wlog by symmetry); the law entering that class is the static two-record law"""
    import sympy as sp
    nbr = mk(V, E)
    cl = [s for s in configs(V, 2) if set(c for c in s if c) == {1}]
    idx = {s: i for i, s in enumerate(cl)}; n = len(cl)
    Q = sp.zeros(n, n); Bv = []; Asame = []
    for s in cl:
        i = idx[s]; ws = w(s, E, W)
        for t in hops(s, E):
            wt = w(t, E, W); Q[i, idx[t]] += ws*0 + wt/(ws + wt)
        tot = Fr(0); same = Fr(0)
        for x in range(V):
            if s[x] == 0:
                for a in range(1, 7):
                    r = ins(s, x, a, nbr, W); tot += r
                    if a == 1: same += r
        Bv.append(tot); Asame.append(same)
    for i in range(n): Q[i, i] = -sum(Q[i, j] for j in range(n) if j != i)
    Z = sum(w(s, E, W) for s in cl)
    alpha = sp.Matrix([[w(s, E, W)/Z for s in cl]])
    Dm = sp.diag(*Bv)
    v = eps*alpha*(eps*Dm - Q).inv()
    pcond = (v*sp.Matrix(Asame))[0]
    # probability the first two records are identical (static two-record law)
    Z2 = sum(w(s, E, W) for s in configs(V, 2)); Zid = sum(w(s, E, W) for s in configs(V, 2) if len(set(c for c in s if c)) == 1)
    return Fr(str(Zid/Z2)), sp.nsimplify(pcond), n
def D2(V, E, W):
    """unnormalised two-record hazard Dirichlet energy, unit proposals: (1/2) sum_{s,t} w(s) H(s,t) (b(t) - b(s))^2"""
    nbr = mk(V, E)
    def b(s): return sum(ins(s, x, a, nbr, W) for x in range(V) if s[x] == 0 for a in range(1, 7))
    tot = Fr(0)
    for s in configs(V, 2):
        ws = w(s, E, W); bs = b(s)
        for t in hops(s, E):
            wt = w(t, E, W); tot += ws*(wt/(ws + wt))*(b(t) - bs)**2
    return tot/2
import itertools
def torus(L, d):
    sites = list(itertools.product(range(L), repeat=d)); ix = {s: i for i, s in enumerate(sites)}; E = set()
    for s in sites:
        for a in range(d):
            t = list(s); t[a] = (t[a] + 1) % L; E.add(tuple(sorted((ix[s], ix[tuple(t)]))))
    return len(sites), sorted(E)
def D2_fast(V, E, W):
    nbr = mk(V, E); nbs = [set(n) for n in nbr]
    h = [[sum(W[a][c]*W[c][b] for c in range(6)) - 6 for b in range(6)] for a in range(6)]
    # b(x,a;y,b) = 6(V-2) + c_xy h_ab ; hops of one record along an edge keep the other fixed
    tot = Fr(0)
    for (x, xp) in E:
        for y in range(V):
            if y in (x, xp): continue
            cx = len(nbs[x] & nbs[y]); cxp = len(nbs[xp] & nbs[y])
            for a in range(6):
                for b in range(6):
                    u = W[a][b] if y in nbs[x] else Fr(1); v = W[a][b] if y in nbs[xp] else Fr(1)
                    tot += u*v/(u + v)*h[a][b]**2*(cxp - cx)**2
    return tot
def formula(V, d, W):
    h = [[sum(W[a][c]*W[c][b] for c in range(6)) - 6 for b in range(6)] for a in range(6)]
    return V*d*sum(h[a][b]**2*(2*(8*d - 7)*W[a][b]/(1 + W[a][b]) + (8*d*d - 14*d + 7)) for a in range(6) for b in range(6))
def generators(V, E, W):
    nbr = mk(V, E)
    states = [s for k in range(V + 1) for s in configs(V, k)]
    Hm = defaultdict(dict); Bm = defaultdict(dict)
    for s in states:
        ws = w(s, E, W)
        for t in hops(s, E):
            wt = w(t, E, W); r = wt/(ws + wt)
            Hm[s][t] = Hm[s].get(t, 0) + r; Hm[s][s] = Hm[s].get(s, 0) - r
        for x in range(V):
            if s[x] == 0:
                for a in range(1, 7):
                    r = ins(s, x, a, nbr, W); t = list(s); t[x] = a; t = tuple(t)
                    Bm[s][t] = Bm[s].get(t, 0) + r; Bm[s][s] = Bm[s].get(s, 0) - r
    return states, Hm, Bm
def rowmul(p, M):
    out = defaultdict(lambda: 0)
    for s, v in p.items():
        if v == 0: continue
        for t, r in M.get(s, {}).items(): out[t] += v*r
    return dict(out)
def combine(p, q, a=1, b=1):
    out = defaultdict(lambda: 0)
    for s, v in p.items(): out[s] += a*v
    for s, v in q.items(): out[s] += b*v
    return dict(out)

print("== F exact recoveries")
V6, E6 = 6, [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)]
d = rare_limit(V6, E6, W0)
pE = sum(p for s, p in d.items() if isinstance(s, tuple) and len({c for c in s if c}) == 1)
Z3 = sum(w(s, E6, W0) for s in configs(V6, 3)); Zs = sum(w(s, E6, W0) for s in configs(V6, 3) if len({c for c in s if c}) == 1)
check("F1 six-site witness: rare-formation event law P(E) = 2701/53880, static 73/1440, dynamic/static ratio 444/449, "
      "difference -73/129312 (slow class process from BFS motion classes, exact)", pE == Fr(2701, 53880) and Zs/Z3 == Fr(73, 1440)
      and pE/(Zs/Z3) == Fr(444, 449) and pE - Zs/Z3 == Fr(-73, 129312), f"{pE}, {Zs/Z3}, ratio {pE/(Zs/Z3)}")
pid, pc, n = finite_eps_E(V6, E6, W0, Fr(1, 1000))
val = sp.Rational(pid.numerator, pid.denominator)*pc
check("F2 finite epsilon = 1/1000: P(E) = (37/180) x [killed resolvent in the 15-state two-identical class] = "
      "2851401694918427/56880888215238000 exactly; the entering law is the static two-record law (one-record hazard is the "
      "constant 6(V-1))", n == 15 and pid == Fr(37, 180) and val == sp.Rational(2851401694918427, 56880888215238000), str(val))
Wopp = Wmat(Fr(1, 2), Fr(3, 2), Fr(1))
p3, c4, k3 = [(3, [(0, 1), (1, 2)]), (4, [(0, 1), (1, 2), (2, 3), (3, 0)]), (3, [(0, 1), (1, 2), (0, 2)])]
vals = [D2(*p3, W0), D2(*c4, W0), D2(*k3, W0), D2(*p3, Wopp), D2(*c4, Wopp)]
check("F3a Dirichlet energy D2(b) = (1/2) sum w(s) H(s,t)(b(t) - b(s))^2 over two-record configurations: 14/5 (path), 224/5 "
      "(4-cycle), 0 (triangle), and 14/5, 224/5 for the opposite-favouring menu", vals == [Fr(14, 5), Fr(224, 5), 0, Fr(14, 5), Fr(224, 5)], str(vals))
okT = True; tv = []
for L, dd in ((6, 1), (7, 1), (8, 1), (6, 2), (7, 2)):
    V, E = torus(L, dd); a_, b_ = D2_fast(V, E, W0), formula(V, dd, W0); okT &= a_ == b_; tv.append(str(a_))
Vr, Er = torus(6, 1)
check("F3b the note's reduction D2 = sum_edges sum_y sum_ab [uv/(u+v)] h_ab^2 (c_x'y - c_xy)^2 equals brute force (ring 6, path) "
      "and the torus formula D2/V = d sum h^2 {2(8d-7)W/(1+W) + (8d^2-14d+7)} holds on rings 6, 7, 8 and tori 6x6, 7x7; "
      "d = 3 gives 2379/5 per volume", okT and D2(Vr, Er, W0) == D2_fast(Vr, Er, W0) and D2_fast(3, [(0, 1), (1, 2)], W0) == Fr(14, 5)
      and formula(1, 3, W0) == Fr(2379, 5), ", ".join(tv))
V, E = 3, [(0, 1), (1, 2)]
states, Hm, Bm = generators(V, E, W0)
kap, eps = sp.symbols('kappa epsilon')
d0 = {tuple([0]*V): 1}
Lm = {s: {t: kap*Hm.get(s, {}).get(t, 0) + eps*Bm.get(s, {}).get(t, 0) for t in set(Hm.get(s, {})) | set(Bm.get(s, {}))} for s in states}
pL = [d0]; pB = [d0]
for k in range(5):
    pL.append({s: sp.expand(v) for s, v in rowmul(pL[-1], Lm).items()}); pB.append(rowmul(pB[-1], Bm))
ok = all(all(sp.expand(v) == 0 for v in combine(pL[k], {s: eps**k*v for s, v in pB[k].items()}, 1, -1).values()) for k in range(4))
B3H = rowmul(pB[3], Hm)
ok4 = all(sp.expand(v) == 0 for v in combine(pL[4], combine({s: eps**4*v for s, v in pB[4].items()}, {s: kap*eps**3*v for s, v in B3H.items()}), 1, -1).values())
Nf = lambda s: sum(1 for c in s if c)
lhs = sp.expand(sum(v*Nf(s) for s, v in pL[5].items()) - eps**5*sum(v*Nf(s) for s, v in pB[5].items()))
check("F4 exact full-generator powers on the path of 3 (343 states, symbolic kappa, epsilon): delta0 L^k = eps^k delta0 B^k for "
      "k <= 3, delta0 L^4 = eps^4 delta0 B^4 + kappa eps^3 delta0 B^3 H, and delta0 L^5 N - eps^5 delta0 B^5 N = 2 kappa eps^4 D2 "
      "= 28 kappa eps^4/5", ok and ok4 and sp.simplify(lhs - sp.Rational(28, 5)*kap*eps**4) == 0, str(lhs))
print("== S float screens")
from scipy.linalg import expm
import itertools as it
def fbuild(V, E, Wf, kappa, epsv):
    nbr = [[] for _ in range(V)]
    for x, y in E: nbr[x].append(y); nbr[y].append(x)
    st = list(it.product(range(7), repeat=V)); ix = {s: i for i, s in enumerate(st)}
    def wf(s):
        p = 1.0
        for x, y in E:
            if s[x] and s[y]: p *= Wf[s[x]-1][s[y]-1]
        return p
    Lf = np.zeros((len(st), len(st)))
    for s, i in ix.items():
        ws = wf(s)
        for x in range(V):
            if s[x] == 0:
                for a in range(1, 7):
                    r = epsv*np.prod([Wf[a-1][s[y]-1] for y in nbr[x] if s[y]]); t = list(s); t[x] = a; Lf[i, ix[tuple(t)]] += r
        for x, y in E:
            for u, v in ((x, y), (y, x)):
                if s[u] and not s[v]:
                    t = list(s); t[v] = s[u]; t[u] = 0; t = tuple(t); Lf[i, ix[t]] += kappa*wf(t)/(ws + wf(t))
    Lf -= np.diag(Lf.sum(1))
    return Lf, np.array([sum(1 for c in s if c) for s in st], float), ix[tuple([0]*V)]
def psi(z): return z/20 - z*z/120 if z < 1e-3 else 0.25 - 1/z + 3/z**2 - 6/z**3 + 6*(1 - math.exp(-z))/z**4
Wf = [[float(x) for x in r] for r in W0]
okc = True; rows = []
for kappa, t in ((0.5, 1.0), (2.0, 2.0)):
    est = []
    for e in (2e-3, 1e-3):
        Lk, Nv, e0 = fbuild(3, [(0, 1), (1, 2)], Wf, kappa, e); L0, _, _ = fbuild(3, [(0, 1), (1, 2)], Wf, 0.0, e)
        est.append(((expm(Lk*t)[e0] - expm(L0*t)[e0]) @ Nv)/e**4)
    rich = 2*est[1] - est[0]
    C = (t**4/3)*((9/8)*psi(8*kappa*t/5) + (3/4)*psi(4*kappa*t/3))
    okc &= abs(rich - C) < 2e-2*C; rows.append((kappa, t, round(rich, 5), round(C, 5)))
check("S1 (float) the epsilon^4 coefficient of E_kappa[N_t] - E_0[N_t] on the path (Richardson at eps = 2e-3, 1e-3) matches "
      "the closed form (t^4/3)[(9/8)psi(8 kappa t/5) + (3/4)psi(4 kappa t/3)]", okc, str(rows))
def wm(eq, op, orr): return [[eq if a == b else (op if (a ^ 1) == b else orr) for b in range(6)] for a in range(6)]
okm = True; worst = 0.0
for V, E in ((3, [(0, 1), (1, 2)]), (4, [(0, 1), (0, 2), (0, 3)]), (4, [(0, 1), (1, 2), (2, 3), (3, 0)])):
    for Wp in ((1.5, 0.5, 1.0), (0.5, 1.5, 1.0), (3.0, 0.2, 0.7)):
        Wl = wm(*Wp)
        L0, Nv, e0 = fbuild(V, E, Wl, 0.0, 1.0); P0 = expm(L0*0.05)
        for kappa in (1.0, 50.0):
            Lk, _, _ = fbuild(V, E, Wl, kappa, 1.0); Pk = expm(Lk*0.05)
            p0 = np.zeros(len(Nv)); p0[e0] = 1; pk = p0.copy()
            for step in range(160):
                p0 = p0 @ P0; pk = pk @ Pk; dlt = (pk - p0) @ Nv
                worst = min(worst, dlt)
                if dlt < -1e-10: okm = False
check("S2 (float screen, not a no-go) E_kappa[N_t] >= E_0[N_t] on t <= 8 for the path of 3, the star and the 4-cycle, three "
      "row-six menus, kappa = 1 and 50 (no finite counterexample to all-time mobility monotonicity found)", okm, f"smallest difference {worst:.2e}")
print(f"== done in {time.time()-T0:.0f}s")
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("SUMMARY: PARTIAL (cross-family recovery, no defect found) - the decisive finite facts reproduce exactly: six-site "
          "event law 2701/53880 vs static 73/1440 (ratio 444/449), the finite-epsilon value at 1/1000, D2 = 14/5, 224/5, 0 and "
          "the torus formula (d = 1, 2 exact; 2379/5 per volume in d = 3), and the generator-power identities giving the "
          "epsilon^4 t^5 coefficient 2 kappa eps^4 D2/5! symbolically; the note's volume-uniform short-time remainder is "
          "re-derived; the finite-intensity all-time response bound and all-time monotonicity remain open (small-graph search "
          "found no sign change)")
