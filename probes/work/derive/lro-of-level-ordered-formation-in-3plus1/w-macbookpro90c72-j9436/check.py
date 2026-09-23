#!/usr/bin/env python3
"""J:derive:lro-of-level-ordered-formation-in-3plus1:a1 -- exact checks for ATTEMPT.md (Fractions, integers, sympy).

The level-ordered law K on the torus (Z/L)^3 (probes/lib/formation_levelplane.py, dim = 3, sphere menu): the record at x on
level t+1 has density prop. to exp(beta r.S_x(s)) on S^2, with S_x(s) = sum_{d in N4} s_{x-d}, N4 = {0, e1, e2, e3}.
The light-cone law uses N7 = {0, +-e1, +-e2, +-e3}.  Doubled graph Gamma^N_L: vertices (x, a), a in {0, 1}; edges
(y, 0)-(x, 1) with x - y in N.  Inversion: (i s)_x = s_{-x}.  Sfwd_x(s) = sum_{d in N4} s_{x+d}.
Floating point appears only in the lines marked 'note' (the linear theory's lattice sums), never in a checked claim.
"""
import itertools, math, sys, time
from collections import Counter
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components

T0 = time.time()
FAILS = []


def ok(tag, cond, msg=""):
    print(("ok   " if cond else "FAIL ") + tag + (": " + msg if msg else ""))
    if not cond:
        FAILS.append(tag)


E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
N4 = [(0, 0, 0)] + E3
N7 = [(0, 0, 0)] + E3 + [tuple(-c for c in e) for e in E3]


def sites(L):
    return list(itertools.product(range(L), repeat=3))


def add(x, d, L, s=1):
    return tuple((a + s * b) % L for a, b in zip(x, d))


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]


def vsum(vs):
    return tuple(sum(v[i] for v in vs) for i in range(3))


def S(s, x, L, N=N4, sign=-1):             # sign -1: backward sum S_x; +1: forward sum Sfwd_x
    return vsum([s[add(x, d, L, sign)] for d in N])


def B(s2, s, L, N=N4):                     # B(s', s) = sum_x s'_x . S_x(s): the exponent of the level-ordered kernel
    return sum(dot(s2[x], S(s, x, L, N)) for x in s)


def inv(s, L):
    return {x: s[tuple((-c) % L for c in x)] for x in s}


def runit(rng):                            # rational point of S^2 (inverse stereographic projection)
    a = Fr(rng.randint(-9, 9), rng.randint(1, 9))
    b = Fr(rng.randint(-9, 9), rng.randint(1, 9))
    n = a * a + b * b + 1
    return (2 * a / n, 2 * b / n, (a * a + b * b - 1) / n)


rng = __import__("random").Random(20260923)

# ---------------------------------------------------------------- G: the level-ordered doubled graph is the diamond lattice
def edges(L, N):
    return {((add(x, d, L, -1), 0), (x, 1)) for x in sites(L) for d in N}


def adjacency(E):
    adj = {}
    for u, v in E:
        adj.setdefault(u, set()).add(v)
        adj.setdefault(v, set()).add(u)
    return adj


def girth_at(adj, root):                   # shortest cycle through root: min over root edges of 1 + dist in G - edge
    best = None
    for w in adj[root]:
        dist = {root: 0}
        frontier = [root]
        while frontier and w not in dist:
            nxt = []
            for u in frontier:
                for v in adj[u]:
                    if (u, v) in ((root, w), (w, root)) or v in dist:
                        continue
                    dist[v] = dist[u] + 1
                    nxt.append(v)
            frontier = nxt
        if w in dist:
            best = dist[w] + 1 if best is None else min(best, dist[w] + 1)
    return best


good = True
for L in (4, 6):
    Eo, El = edges(L, N4), edges(L, N7)
    ao, al = adjacency(Eo), adjacency(El)
    good &= all(len(v) == 4 for v in ao.values()) and all(len(v) == 7 for v in al.values())
    good &= girth_at(ao, ((0, 0, 0), 0)) == 6 and girth_at(ao, ((0, 0, 0), 1)) == 6
    good &= girth_at(al, ((0, 0, 0), 0)) == 4
    par = lambda x: sum(x) % 2
    img = {frozenset(((y, a ^ par(y)), (x, b ^ par(x)))) for (y, a), (x, b) in Eo}
    stag = {frozenset(((x, 0), (x, 1))) for x in sites(L)}
    stag |= {frozenset(((y, par(y)), (add(y, e, L), par(y)))) for y in sites(L) for e in E3}
    good &= img == stag
    good &= Eo <= El
v = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
Acol = [tuple(v[0][i] - v[j][i] for i in range(3)) for j in (1, 2, 3)]          # A e_j = v0 - v_j
Amap = lambda x: tuple(sum(Acol[j][i] * x[j] for j in range(3)) for i in range(3))
bond = {tuple(Amap(tuple(-c for c in d))[i] + v[0][i] for i in range(3)) for d in N4}  # bottom(x-d) - top(x), top = A x - v0
good &= bond == set(v) and all(dot(v[i], v[j]) == (3 if i == j else -1) for i in range(4) for j in range(4))
good &= sorted(Acol) == [(0, 2, 2), (2, 0, 2), (2, 2, 0)]
ok("G.diamond", good, "level-ordered doubled graph (L=4,6): 4-regular, girth 6, onto the staggered bilayer by (x,a)->(x,a+|x|); "
   "embedding A e_j=v0-v_j has bond vectors (1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1) on the FCC lattice; a subgraph of the "
   "light-cone doubled graph (7-regular, girth 4)")
phi4 = lambda t, x: (t - sum(x),) + tuple(x)
ok("G.spacetime", {phi4(-1, tuple(-c for c in d)) for d in N4} == {(-1, 0, 0, 0), (0, -1, 0, 0), (0, 0, -1, 0), (0, 0, 0, -1)},
   "(t,x)->(t-|x|,x) sends the level-ordered predecessors to the four negative unit vectors of Z^4")

# ---------------------------------------------------------------- R: K = Q then inversion, with Q reversible for rho_L
good = True
for L in (3, 4, 5):
    for _ in range(2):
        s = {x: runit(rng) for x in sites(L)}
        s2 = {x: runit(rng) for x in sites(L)}
        good &= B(inv(s, L), inv(s2, L), L) == B(s2, s, L)
        good &= B(s2, s, L) == sum(dot(s[y], S(s2, y, L, sign=+1)) for y in sites(L))
ok("R.bilinear", good, "B(i s, i s') = B(s', s) and B(s', s) = sum_y s_y.Sfwd_y(s') for random rational records (L=3,4,5)")

good = True
for L in (2, 3, 4, 5, 6):
    ez, ex, ey = (0, 0, 1), (1, 0, 0), (0, 1, 0)
    c0 = {x: ez for x in sites(L)}
    c1 = dict(c0); c1[(0, 0, 0)] = ex
    c2 = dict(c0); c2[add((0, 0, 0), E3[0], L)] = ey
    cyc = [c0, c1, c2]
    for N, want in ((N4, 1 if L >= 3 else 0), (N7, 0)):
        tot = sum(B(cyc[(i + 1) % 3], cyc[i], L, N) - B(cyc[i], cyc[(i + 1) % 3], L, N) for i in range(3))
        good &= tot == want
ok("R.cycle", good, "3-cycle (aligned; e_x at 0; e_y at e1): sum of B(next,prev)-B(prev,next) = 1 for N4, L=3..6 (Kolmogorov "
   "ratio e^beta), 0 for N7 and for L=2")

# ---------------------------------------------------------------- M: rho_L is not inversion-invariant, for every beta > 0
good = True
for L in range(3, 9):
    Fl = {(0, 0, 0), add((0, 0, 0), E3[0], L, -1), add((0, 0, 0), E3[1], L, -1)}
    s = {x: ((0, 0, -1) if x in Fl else (0, 0, 1)) for x in sites(L)}
    bw = Counter(dot(S(s, x, L), S(s, x, L)) for x in s)
    fw = Counter(dot(S(s, x, L, sign=+1), S(s, x, L, sign=+1)) for x in s)
    n = L ** 3
    good &= bw == Counter({4: 10, 16: n - 10}) and fw == Counter({0: 3, 4: 6, 16: n - 9})
    good &= sum(q * q for q in fw.elements()) - sum(q * q for q in bw.elements()) == 192
ok("M.counts", good, "records -e_z on {0,-e1,-e2}: backward |S|^2 {4:10, 16:N-10}, forward {0:3, 4:6, 16:N-9}, sum |S|^4 "
   "differs by 192 (L=3..8)")
x_, b_ = sp.symbols("x beta", positive=True)
Zf = lambda q: sp.sinh(q) / q
ok("M.ratio", sp.simplify((Zf(4 * b_) / Zf(2 * b_) ** 4 - (2 * b_) ** 3 * sp.cosh(2 * b_) / sp.sinh(2 * b_) ** 3).rewrite(sp.exp)) == 0,
   "rho(i s)/rho(s) = Z(4b)Z(0)^3/Z(2b)^4 = u^3 cosh u / sinh^3 u with u = 2 beta, Z(q) = sinh q / q")
lz = sp.simplify((sp.sinh(x_) ** 3 - (sp.sinh(3 * x_) - 3 * sp.sinh(x_)) / 4).rewrite(sp.exp)) == 0
s1 = sp.series(sp.sinh(x_) ** 3, x_, 0, 16).removeO()
s2_ = sp.series(x_ ** 3 * sp.cosh(x_), x_, 0, 16).removeO()
lz &= all(s1.coeff(x_, j) == (sp.Rational(3 ** j - 3, 4) / sp.factorial(j) if j % 2 else 0) for j in range(1, 16))
lz &= all(s2_.coeff(x_, j) == (1 / sp.factorial(j - 3) if (j % 2 and j >= 3) else 0) for j in range(1, 16))
lz &= all(Fr(3 ** m - 3, 4) >= m * (m - 1) * (m - 2) for m in range(3, 200, 2))
lz &= [m for m in range(3, 200, 2) if Fr(3 ** m - 3, 4) == m * (m - 1) * (m - 2)] == [3, 5]
nn, mm = sp.symbols("n m")
pstep = sp.expand(9 * nn * (nn - 1) * (nn - 2) + 6 - (nn + 2) * (nn + 1) * nn)
lz &= sp.Poly(sp.expand(pstep.subs(nn, 7 + mm)), mm).all_coeffs() == [8, 138, 772, 1392]
ok("M.lazarevic", lz, "sinh^3 x - x^3 cosh x = sum_{n odd} [(3^n-3)/4 - n(n-1)(n-2)] x^n/n!: zero for n=3,5, positive for "
   "7<=n<=199, induction step 8n^3-30n^2+16n+6 > 0 on n>=7; so the ratio is < 1 for every beta > 0")
good = True
for L in (3, 4, 5):
    s = {x: runit(rng) for x in sites(L)}
    good &= sum(dot(S(s, x, L), S(s, x, L)) for x in s) == sum(dot(S(s, x, L, sign=+1), S(s, x, L, sign=+1)) for x in s)
lr = sp.log((2 * b_) ** 3 * sp.cosh(2 * b_) / sp.sinh(2 * b_) ** 3)
good &= sp.series(lr, b_, 0, 6).removeO() == -sp.Rational(16, 15) * b_ ** 4
ok("M.gauss", good, "sum_x |S_x|^2 = sum_x |Sfwd_x|^2 for all records (random rational, L=3,4,5): rho and rho o i agree at "
   "order beta^2; at the flip configuration log ratio = -16 beta^4/15 + O(beta^6)")

# ---------------------------------------------------------------- C: reflections of the doubled graphs
def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def aff(N):                                 # all (M, delta), M in GL(3,Z), with M N + delta = N
    Ns, out = set(N), []
    for dl in N:
        for imgs in itertools.product(N, repeat=3):
            M = tuple(tuple(imgs[j][i] - dl[i] for j in range(3)) for i in range(3))
            if abs(det3(M)) != 1:
                continue
            if {tuple(sum(M[i][j] * d[j] for j in range(3)) + dl[i] for i in range(3)) for d in N} == Ns:
                out.append((M, dl))
    return out


def reflection_census(L, N):
    X = np.array(sites(L))
    n, V = L ** 3, 2 * L ** 3
    idx = lambda Y: (Y[:, 0] * L + Y[:, 1]) * L + Y[:, 2]
    E = np.concatenate([np.stack([idx((X - np.array(d)) % L), n + idx(X)], 1) for d in N])
    enc = lambda F: np.sort(np.minimum(F[:, 0], F[:, 1]) * V + np.maximum(F[:, 0], F[:, 1]))
    code, ident = enc(E), np.arange(V)
    A = aff(N)
    naut = ninv = nfree = nweak = nstrict = 0
    cover = np.zeros(len(E), bool)
    for M, dl in A:
        Mn = np.array(M)
        for swap in (0, 1):
            Ml = -Mn if swap else Mn        # swap type: (-Ml, c0 - c1) in Aff(N); keep type: (Ml, c1 - c0) in Aff(N)
            for c0 in itertools.product(range(L), repeat=3):
                c0 = np.array(c0)
                c1 = (c0 - np.array(dl)) % L if swap else (c0 + np.array(dl)) % L
                b, t = idx((X @ Ml.T + c0) % L), idx((X @ Ml.T + c1) % L)
                th = np.concatenate([b + (n if swap else 0), t + (0 if swap else n)])
                if not np.array_equal(enc(th[E]), code):
                    continue
                naut += 1
                if not np.array_equal(th[th], ident):
                    continue
                ninv += 1
                if np.any(th == ident):
                    continue
                nfree += 1
                mirror = th[E[:, 0]] == E[:, 1]
                inM = np.zeros(V, bool)
                inM[E[mirror, 0]] = True
                inM[E[mirror, 1]] = True
                inner = ~(inM[E[:, 0]] & inM[E[:, 1]])   # a PSD crossing matrix forces these edges inside one half
                g = coo_matrix((np.ones(int(inner.sum())), (E[inner, 0], E[inner, 1])), shape=(V, V))
                lab = connected_components(g, directed=False)[1]
                if not np.any(lab[th] == lab):
                    nweak += 1
                    cover |= mirror
                    g2 = coo_matrix((np.ones(int((~mirror).sum())), (E[~mirror, 0], E[~mirror, 1])), shape=(V, V))
                    lab2 = connected_components(g2, directed=False)[1]
                    nstrict += int(not np.any(lab2[th] == lab2))   # halves whose crossing edges are all mirror pairs
    return len(A), naut, ninv, nfree, nweak, int(cover.sum()), len(E), nstrict


res = {(nm, L): reflection_census(L, N) for nm, N in (("ord", N4), ("lc", N7)) for L in (4, 6)}
ok("C.aff", [res[("ord", L)][0] for L in (4, 6)] == [24, 24] and [res[("lc", L)][0] for L in (4, 6)] == [48, 48]
   and all(r[1] == 2 * r[0] * L ** 3 for (nm, L), r in res.items()),
   "affine symmetries of the stencil: 24 for N4, 48 for N7; every one of the 2|Aff|L^3 layer-keeping/swapping maps is an automorphism")
ok("C.reflections", [res[("lc", L)][4:8] for L in (4, 6)] == [(7, 448, 448, 7), (10, 1512, 1512, 10)]
   and [res[("ord", L)][4:6] for L in (4, 6)] == [(0, 0), (0, 0)],
   "fixed-point-free affine involutions with halves crossed only by mirror pairs: light-cone 7 of %d (L=4), 10 of %d (L=6), "
   "covering every edge; level-ordered: 0 of %d (L=4), 0 of %d (L=6) pass even the necessary condition for a PSD crossing matrix "
   "(involutions with fixed vertices: %d, %d)"
   % (res[("lc", 4)][3], res[("lc", 6)][3], res[("ord", 4)][3], res[("ord", 6)][3],
      res[("ord", 4)][2] - res[("ord", 4)][3], res[("ord", 6)][2] - res[("ord", 6)][3]))

# ---------------------------------------------------------------- K: the one-record update is not monotone in the z-order
k_ = sp.symbols("k", positive=True)
Aq = sp.coth(k_) - 1 / k_
conc = sp.simplify((sp.diff(Aq, k_, 2) - 2 * (k_ ** 3 * sp.cosh(k_) - sp.sinh(k_) ** 3) / (k_ ** 3 * sp.sinh(k_) ** 3)).rewrite(sp.exp)) == 0
conc &= sp.simplify((sp.diff(sp.log(sp.sinh(k_) / k_), k_) - Aq).rewrite(sp.exp)) == 0
u, w = (Fr(4, 5), Fr(0), Fr(3, 5)), (Fr(-4, 5), Fr(0), Fr(3, 5))
St, Ss = vsum([u] * 4), vsum([u, u, w, w])
conc &= dot(u, u) == 1 and dot(St, St) == 16 and Ss == (0, 0, Fr(12, 5))
ok("K.concave", conc, "A = (log Z)' has A'' = 2(k^3 cosh k - sinh^3 k)/(k^3 sinh^3 k) < 0; predecessors u,u,u,u vs u,u,w,w with "
   "equal z-components (3/5) give mean z A(4b)(3/5) < A(12b/5)")

# ---------------------------------------------------------------- L: the linear theory is the lazy FCC walk
z1, z2, z3 = sp.symbols("z1 z2 z3", nonzero=True)
zs = [z1, z2, z3]
ph, phb = (1 + z1 + z2 + z3) / 4, (1 + 1 / z1 + 1 / z2 + 1 / z3) / 4
lam = (sum(z + 1 / z for z in zs) + sum(zs[i] / zs[j] for i in range(3) for j in range(3) if i != j)) / 12
fcc = sp.simplify(sp.together(1 - ph * phb - sp.Rational(3, 4) * (1 - lam))) == 0
diffs = Counter(tuple(a - b for a, b in zip(d1, d2)) for d1 in N4 for d2 in N4)
fcc &= diffs[(0, 0, 0)] == 4 and len(diffs) == 13 and all(c == 1 for key, c in diffs.items() if key != (0, 0, 0))
ok("L.fcc", fcc, "1 - |phi(k)|^2 = (3/4)(1 - lambda_FCC(k)), phi = (1 + sum e^{ik_j})/4; N4 - N4 = 4 x {0} + the 12 FCC vectors")

# ---------------------------------------------------------------- T: a twisted history with m = 0 and no defect at resolution 53 deg
L = 8
tt = [Fr(0), Fr(1, 2), Fr(1), Fr(2)]
ring = [(2 * t / (1 + t * t), Fr(0), (1 - t * t) / (1 + t * t)) for t in tt]
ring += [tuple(-c for c in q) for q in ring]
s = {x: ring[x[0]] for x in sites(L)}
good = vsum(list(s.values())) == (0, 0, 0) and all(dot(q, q) == 1 for q in ring)
for x in sites(L):
    k0, k1 = x[0], (x[0] - 1) % L
    c = dot(ring[k0], ring[k1])
    Sx = S(s, x, L)
    good &= dot(s[x], Sx) == 3 + c and dot(Sx, Sx) == 10 + 6 * c and c >= Fr(3, 5)
ok("T.twist", good, "static twist u_{k+4} = -u_k on L=8 (rational ring, steps with cos >= 3/5): m = 0 exactly; s.S = 3 + cos, "
   "|S|^2 = 10 + 6 cos at every site")

# ---------------------------------------------------------------- notes (floating point, not claims)
def W(L):
    g = 2 * np.pi * np.arange(L) / L
    k1, k2, k3 = np.meshgrid(g, g, g, indexing="ij")
    den = 1 - np.abs((1 + np.exp(1j * k1) + np.exp(1j * k2) + np.exp(1j * k3)) / 4) ** 2
    den[0, 0, 0] = np.inf
    return float(np.sum(1 / den) / L ** 3)


Winf = 12 * math.gamma(1 / 3) ** 6 / (2 ** (14 / 3) * math.pi ** 4)
Ws = {L: W(L) for L in (16, 32, 64)}
print("note: W_L = (1/N) sum_{k!=0} 1/(1-|phi|^2) = " + ", ".join("%.5f (L=%d)" % (Ws[L], L) for L in Ws)
      + "; (4/3) G_FCC(0) = 12 Gamma(1/3)^6/(2^(14/3) pi^4) = %.6f; L (W_inf - W_L) = " % Winf
      + ", ".join("%.3f" % (L * (Winf - Ws[L])) for L in Ws))
Af = lambda q: 1 / math.tanh(q) - 1 / q
print("note: linear plateau 1 - sigma^2 W_inf, sigma^2 = A(4b)/(4b): %.4f (b=2), %.4f (b=3) vs executed 0.732, 0.835; linear 1/L slope "
      "sigma^2 x 1.4595 = %.3f, %.3f vs executed about 0.19, 0.12 (L=16..96)"
      % (1 - Af(8) / 8 * Winf, 1 - Af(12) / 12 * Winf, Af(8) / 8 * 1.4595, Af(12) / 12 * 1.4595))

print("runtime %.1f s" % (time.time() - T0))
if FAILS:
    print("CHECK FAIL: " + ", ".join(FAILS))
    print("SUMMARY: ROUTE FAILS AT a failed exact check (" + ", ".join(FAILS) + ")")
    sys.exit(1)
HITS = [
    "HIT: the level-ordered law K is Q followed by the inversion x -> -x, where Q is reversible with stationary law "
    "rho_L(s) ~ prod_x Z(beta|S_x(s)|), the layer marginal of the Heisenberg model on the level-ordered doubled graph, which "
    "is the diamond lattice; the alternating law (K, then its mirror image) is Q.Q, local and reversible for rho_L.",
    "HIT: for every beta > 0 and L >= 3, rho_L differs from its mirror image (three flipped records; density ratio "
    "u^3 cosh u/sinh^3 u < 1, u = 2 beta); so K has no inversion-symmetric stationary law, its stationary law is not rho_L, "
    "and the 3-cycle ratio is e^beta.",
    "HIT: route obstructions: no fixed-point-free affine involution of the diamond doubled graph (L = 4, 6) has halves with a "
    "PSD crossing matrix (the light-cone graph has 7, 10), so the light-cone route to Gaussian domination, and to the infrared "
    "bound that would turn the linear theory's 1/L into a bound, has no reflection to use; the linear theory is the lazy FCC "
    "walk and is inversion-symmetric; zero-noise tilted islands spread and never erode.",
]
print("SUMMARY: PARTIAL K = (reversible Q with the diamond-lattice marginal rho_L) then inversion; rho_L is not inversion-"
      "symmetric for any beta > 0, so each of the four routes fails at an identified exact step (no proof of long-range order)")
print("\n".join(HITS))
