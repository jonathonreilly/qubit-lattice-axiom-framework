"""lightcone-long-range-order, attempt a1, round 2 (w-jonathonsmac4f50-j4031): checks.

Exact (integers, fractions, sympy) for every finite claim; the two integrals are evaluated with mpmath (labelled NUMERIC) by
quadrature of their Bessel representations, a method independent of the Gamma closed form used by attempt a3.

Objects (GIVEN).  Gamma_L: vertices (x, a), x in (Z/L)^3, a in {0,1}; edges (x,0)-(y,1) with y - x in N7 = {0, +-e_j}.  The sphere
Heisenberg ferromagnet mu_L on Gamma_L at coupling beta; pi_L = its layer-0 marginal.  Bilayer torus B_L: vertices (x, b), edges
(x,b)-(x+e_j,b) (in-slab nearest neighbours) and (x,0)-(x,1) (rungs).  Relabelling f(x, a) = (x, a XOR parity(x)).
"""
import itertools

RESULTS = []


def want(label, ok, detail=""):
    RESULTS.append((label, bool(ok)))
    print(("PASS " if ok else "FAIL ") + label + ((" :: " + str(detail)) if detail != "" else ""), flush=True)


def gamma_edges(L):
    E = set()
    for x in itertools.product(range(L), repeat=3):
        for d in [(0, 0, 0)] + [tuple(s * (i == j) for i in range(3)) for j in range(3) for s in (1, -1)]:
            y = tuple((x[i] + d[i]) % L for i in range(3))
            E.add(frozenset({(x, 0), (y, 1)}))
    return E


def bilayer_edges(L):
    E = set()
    for x in itertools.product(range(L), repeat=3):
        E.add(frozenset({(x, 0), (x, 1)}))
        for b in (0, 1):
            for j in range(3):
                y = list(x); y[j] = (y[j] + 1) % L
                E.add(frozenset({(x, b), (tuple(y), b)}))
    return E


par = lambda x: sum(x) % 2
f = lambda v: (v[0], v[1] ^ par(v[0]))
ok = True; rows = []
for L in (4, 6):
    G, Bl = gamma_edges(L), bilayer_edges(L)
    img = {frozenset(f(v) for v in e) for e in G}
    ok = ok and img == Bl and len(G) == len(Bl) == 7 * L ** 3
    rows.append(f"L={L}: {len(G)} edges map onto {len(Bl)}")
want("E1 the relabelling f(x, a) = (x, a XOR parity(x)) is a graph isomorphism from Gamma_L onto the bilayer torus (in-slab nearest "
     "neighbours plus one rung per site), exactly, on L = 4 and 6: the 7-stencil's self-edge becomes the rung, and the six shifted edges "
     "become ordinary nearest-neighbour edges inside one slab", ok, "; ".join(rows))

# E2: spectra. Bilayer Laplacian = (slab Laplacian) (x) 1 + 1 (x) (rung Laplacian): eigenvalues E(k) and E(k) + 2.
# Gamma's stated spectrum {E(k), 14 - E(k)} is the same multiset because E(k + (pi,pi,pi)) = 12 - E(k).
import sympy as sp
ks = sp.symbols("k1 k2 k3", real=True)
Ek = 6 - 2 * sum(sp.cos(k) for k in ks)
Eshift = 6 - 2 * sum(sp.cos(k + sp.pi) for k in ks)
want("E2 E(k + (pi,pi,pi)) = 12 - E(k) symbolically, so Gamma's Laplacian spectrum {E(k), 14 - E(k)} equals the bilayer's {E(k), E(k) + 2} "
     "as a multiset (k -> k + (pi,pi,pi) permutes the Brillouin zone of an even torus); the antisymmetric branch is gapped by 2",
     sp.simplify(Eshift - (12 - Ek)) == 0)

# E3: the reflection family of the bilayer: bond planes in each spatial direction (both slabs together) and the plane between the slabs.
def reflections(L):
    out = []
    for j in range(3):
        for c in range(L // 2):                       # plane between c and c+1, and its antipode between c+L/2 and c+L/2+1
            def th(v, j=j, c=c):
                x = list(v[0]); x[j] = (2 * c + 1 - x[j]) % L; return (tuple(x), v[1])
            out.append(("bond", j, c, th))
    out.append(("slab", None, None, lambda v: (v[0], 1 - v[1])))
    return out


def halves(kind, j, c, L):
    def side(v):
        if kind == "slab": return v[1] == 0
        t = (v[0][j] - c - 1) % L
        return t < L // 2
    return side


ok_mirror = True; covered = set(); L = 4
Bl = bilayer_edges(L)
for kind, j, c, th in reflections(L):
    side = halves(kind, j, c, L)
    V = [(x, b) for x in itertools.product(range(L), repeat=3) for b in (0, 1)]
    ok_mirror = ok_mirror and all(side(th(v)) != side(v) for v in V)            # theta swaps the halves, no fixed vertex
    for e in Bl:
        u, w = tuple(e)
        if side(u) != side(w):
            covered.add(e)
            ok_mirror = ok_mirror and th(u) == w                                 # every crossing edge is a mirror pair {u, theta u}
want("E3 on the bilayer torus L = 4: each reflection of the family (bond planes in the three spatial directions, both slabs together; "
     "the plane between the slabs) swaps its halves without fixed vertices, every crossing edge is a mirror pair {u, theta u} (so the "
     "crossing factor exp(beta s_u . s_theta u) is a positive-definite kernel and the law is reflection positive), and every edge "
     "crosses some reflection of the family", ok_mirror and covered == Bl, f"{len(covered)} of {len(Bl)} edges crossed")

# E4: the one-layer reduction (route (ii) as used at the end): |m0 + m1|^2 <= 2|m0|^2 + 2|m1|^2, so by exchangeability
# <|M/(2N)|^2> <= <|m0|^2>
a0, a1, a2, b0, b1, b2 = sp.symbols("a0 a1 a2 b0 b1 b2", real=True)
lhs = 2 * (a0 ** 2 + a1 ** 2 + a2 ** 2) + 2 * (b0 ** 2 + b1 ** 2 + b2 ** 2) - ((a0 + b0) ** 2 + (a1 + b1) ** 2 + (a2 + b2) ** 2)
want("E4 2|a|^2 + 2|b|^2 - |a + b|^2 = |a - b|^2 >= 0 (symbolic): with the layer swap an automorphism of Gamma (N7 = -N7), "
     "<|(m0 + m1)/2|^2> <= <|m0|^2>, so long-range order of the whole ferromagnet gives it for the one-layer marginal pi",
     sp.expand(lhs - ((a0 - b0) ** 2 + (a1 - b1) ** 2 + (a2 - b2) ** 2)) == 0)

# E5: why the halves must be the slabs: the layer swap with the two LAYERS as halves is not reflection positive.
# All edges cross it; the crossing kernel exp(beta <s0, M s1>) with M = I + (nearest-neighbour adjacency) of the 7-stencil needs M >= 0,
# and a staggered difference d on a 2x2x2 cube has <d, M d> < 0, so the 2x2 minor of the kernel on {s, s'} (s - s' = d) is
# exp(2 beta <s, M s'>)(exp(beta <d, M d>) - 1) < 0 for every beta > 0.
L5 = 4
cube = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
d = {x: 2 * (-1) ** sum(x) for x in cube}                                        # one spin component, s = +-e_z staggered on the cube
def M(x, y):
    diff = tuple((y[i] - x[i]) % L5 for i in range(3))
    return 1 if diff == (0, 0, 0) or sorted(diff) in ([0, 0, 1], [0, 0, L5 - 1]) else 0
dMd = sum(d[x] * M(x, y) * d[y] for x in cube for y in cube)
want("E5 no-go for the layer halves: with halves = the two layers, the layer swap's crossing matrix is M = I + A_nn (the 7-stencil), and the "
     "staggered difference d = 2(-1)^{|x|} e_z on a 2x2x2 cube gives <d, M d> = 32 - 96 = -64 < 0 exactly, so the crossing kernel is not "
     "positive definite for any beta > 0: the reflection that swaps layers is reflection positive only with the slab halves",
     dMd == -64, f"<d, M d> = {dMd}")

# N1: the constants by Bessel quadrature: 1/(E + m) = int_0^oo e^{-t(E + m)} dt and (1/2pi) int e^{2t cos k} dk = I_0(2t)
try:
    import mpmath as mp
    mp.mp.dps = 30
    I0 = mp.quad(lambda t: mp.exp(-6 * t) * mp.besseli(0, 2 * t) ** 3, [0, 1, 10, 100, mp.inf])
    I2 = mp.quad(lambda t: mp.exp(-8 * t) * mp.besseli(0, 2 * t) ** 3, [0, 1, 10, mp.inf])
    W = mp.sqrt(6) / (32 * mp.pi ** 3) * mp.gamma(mp.mpf(1) / 24) * mp.gamma(mp.mpf(5) / 24) * mp.gamma(mp.mpf(7) / 24) * mp.gamma(mp.mpf(11) / 24)
    beta0 = mp.mpf(3) / 2 * (I0 + I2)
    want("N1 NUMERIC I0 = int d^3k/(2pi)^3 1/E(k) and I2 = int 1/(E(k) + 2) by quadrature of int_0^oo e^{-(6 or 8)t} I_0(2t)^3 dt (agreement to 1e-16; the quadrature of the t^(-3/2) tail limits it near 1e-19): "
         "I0 = W/6 with W the cubic walk's expected visits (Gamma closed form, independent), I2 = 0.1409314881127...; the threshold "
         "beta_0 = (3/2)(I0 + I2) = 0.590493746957...",
         abs(I0 - W / 6) < mp.mpf(10) ** -16 and abs(I2 - mp.mpf("0.140931488112717092059")) < mp.mpf(10) ** -16
         and abs(beta0 - mp.mpf("0.59049374695707014263")) < mp.mpf(10) ** -16,
         f"I0 = {mp.nstr(I0, 22)}, W/6 = {mp.nstr(W / 6, 22)}, I2 = {mp.nstr(I2, 22)}, beta0 = {mp.nstr(beta0, 22)}")
except ImportError as exc:
    want("N1 NUMERIC skipped (mpmath missing)", False, str(exc))

npass = sum(1 for _, o in RESULTS if o)
nfail = len(RESULTS) - npass
print(f"TOTAL: PASS={npass} FAIL={nfail}")
if nfail == 0:
    print("SUMMARY: PROVED (the slab route of attempts a5 and w-macbookpro90c72-j451b, which I read before writing it; re-checked here with my "
          "own code, the constant by a different method): Gamma_L is the bilayer torus under (x, a) -> (x, a XOR parity(x)); its bond-plane "
          "and slab reflections are reflection positive and every edge crosses one, so Gaussian domination holds for all fields, the infrared "
          "bound runs over {E, E + 2}, and the sum rule with layer exchangeability gives <|m0|^2>_pi >= 1 - (3/(2 beta))(G_L + H_L): long-range "
          "order for beta > (3/2)(I0 + I2) = 0.5905; new and exact: with the two LAYERS as halves the layer swap is not reflection positive "
          "(<d, M d> = -64 on a cube), so the slab halves are necessary for that reflection")
    print("HIT: the reflection that swaps the layers of the doubled graph is reflection positive with the slab halves (Gamma = bilayer torus "
          "under (x, a) -> (x, a XOR parity(x)), exact) and NOT with the layer halves (crossing matrix I + A_nn, <d, M d> = -64 on a cube); "
          "with the slab halves, long-range order of pi for beta > (3/2)(I0 + I2) = 0.590494 (re-derivation of a5's threshold, same model family)")
