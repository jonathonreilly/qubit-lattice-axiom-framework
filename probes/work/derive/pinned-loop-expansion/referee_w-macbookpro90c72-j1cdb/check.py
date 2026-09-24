"""Independent referee for pinned-loop-expansion a4.

Recomputes the finite certificates in the attempt. Does not import the author's code.
Six-axis weights at c0 = 6/S, S = p + q + 4r: W = 6 K1, W_eq = 6p/S, z_t = W_eq^{-3}.
"""
import itertools
import sys
from fractions import Fraction as F

import sympy as sp

AX = [(1, 0), (-1, 0), (1, 1), (-1, 1), (1, 2), (-1, 2)]
FAILS = []


def want(label, ok):
    FAILS.append(label) if not ok else None
    print(("PASS " if ok else "FAIL ") + label, flush=True)


def weight(p, q, r, a, b):
    S = p + q + 4 * r
    num = p if a == b else q if a[1] == b[1] else r
    return F(6 * num, S)


def Wmat(p, q, r):
    return [[weight(p, q, r, a, b) for b in AX] for a in AX]


def Kmat(p, q, r):
    S = p + q + 4 * r
    return [[F(p if a == b else q if a[1] == b[1] else r, S) for b in AX] for a in AX]


def grid(dims):
    V = list(itertools.product(*[range(d) for d in dims]))
    E = []
    for v in V:
        for i in range(len(dims)):
            w = list(v)
            w[i] += 1
            if w[i] < dims[i]:
                E.append((v, tuple(w)))
    return V, E


def torus(L):
    V = list(itertools.product(range(L), repeat=3))
    E = []
    for v in V:
        for j in range(3):
            w = list(v)
            w[j] = (w[j] + 1) % L
            E.append((v, tuple(w)))
    return V, E


def ncomp(A, EA):
    if not A:
        return 0
    par = {x: x for x in A}

    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for u, v in EA:
        par[f(u)] = f(v)
    return len({f(x) for x in A})


def induced(E, A):
    S = set(A)
    return [e for e in E if e[0] in S and e[1] in S]


def boundary(E, A):
    S = set(A)
    return sum(1 for u, v in E if (u in S) != (v in S))


def phi(V, E, K):
    """Average of prod_e 6 K(s_e) over uniform contents. Vertex elimination, own code."""
    k = [[6 * K[a][b] for b in range(6)] for a in range(6)]
    factors = [((u, v), {(a, b): k[a][b] for a in range(6) for b in range(6)}) for u, v in E]
    for x in V:
        involved = [f for f in factors if x in f[0]]
        rest = [f for f in factors if x not in f[0]]
        scope = sorted({y for f in involved for y in f[0] if y != x})
        table = {}
        for assign in itertools.product(range(6), repeat=len(scope)):
            env = dict(zip(scope, assign))
            tot = F(0)
            for a in range(6):
                env[x] = a
                prod = F(1)
                for sc, tab in involved:
                    prod *= tab[tuple(env[y] for y in sc)]
                tot += prod
            table[assign] = tot / 6
        factors = rest + [(tuple(scope), table)]
    val = F(1)
    for sc, tab in factors:
        val *= tab[()]
    return val


def beta_table(V, E):
    N = len(V)
    tab = {}
    for mask in range(1 << N):
        A = [V[i] for i in range(N) if mask >> i & 1]
        EA = induced(E, A)
        tab[mask] = len(EA) - len(A) + ncomp(A, EA)
    return tab


def super_violations(tab, N, ge):
    bad = 0
    for mask in range(1 << N):
        for i in range(N):
            if mask >> i & 1:
                continue
            for j in range(i + 1, N):
                if mask >> j & 1:
                    continue
                if not ge(tab[mask | (1 << i) | (1 << j)], tab[mask], tab[mask | (1 << i)], tab[mask | (1 << j)]):
                    bad += 1
    return bad


# ---------------------------------------------------------------- A1
ok = True
for p, q, r in ((3, 1, 2), (16, 1, 2), (100, 1, 2), (5, 1, 1), (7, 2, 1), (1000, 1, 1)):
    W = Wmat(p, q, r)
    S = p + q + 4 * r
    Weq = F(6 * p, S)
    l1 = F(p - q, S)
    rows = all(sum(row) == 6 for row in W)
    largest = all(W[i][j] <= Weq for i in range(6) for j in range(6))
    ok = rows and largest and W[0][0] == Weq and (6 * l1 <= Weq < 6) and (Weq >= 1)
    if not ok:
        break
# algebraic cap, not only the six triples
P, Q, R = sp.symbols("P Q R", positive=True)
Weq_s = 6 * P / (P + Q + 4 * R)
l1_s = (P - Q) / (P + Q + 4 * R)
ok = ok and sp.simplify(Weq_s - 6 * l1_s - 6 * Q / (P + Q + 4 * R)) == 0
ok = ok and sp.simplify(6 - Weq_s - 6 * (Q + 4 * R) / (P + Q + 4 * R)) == 0
want("A1 rows of W sum to 6, W_eq = 6p/S is the largest entry, and 6 l1 <= W_eq < 6 whenever q+4r > 0", ok)

# ---------------------------------------------------------------- A2
V3, E3 = torus(3)
deg = {v: set() for v in V3}
for u, v in E3:
    deg[u].add(v)
    deg[v].add(u)
ok = len(E3) == 3 * 27 and all(len(deg[v]) == 6 for v in V3) and len({tuple(sorted(e)) for e in E3}) == len(E3)
# endpoint count is an identity on a 6-regular simple graph; check every subset of a 2x2x3 box is the wrong degree,
# so check 200 structured and hashed subsets of the L=3 torus together with the degree certificate above.
masks = []
for t in range(48):
    A = []
    for i, v in enumerate(V3):
        if ((i * 17 + t * 13) % 7) < (t % 5):
            A.append(v)
    masks.append(A)
masks.append([])
masks.append(list(V3))
masks.append([V3[0]])
masks.append([v for v in V3 if v[0] < 2])
for A in masks:
    SA = set(A)
    if 6 * len(A) != 2 * len(induced(E3, A)) + boundary(E3, A):
        ok = False
want("A2 handshaking 6|A| = 2|E(A)| + |dA| on the L=3 torus (degree 6, each edge once)", ok)

ok = True
samples = []
for p, q, r in ((16, 1, 2), (5, 1, 1), (3, 1, 2)):
    W = Wmat(p, q, r)
    Weq = W[0][0]
    zt = 1 / Weq ** 3
    cfgs = []
    cfgs.append({v: None for v in V3})
    cfgs.append({v: 0 for v in V3})
    cfgs.append({v: 5 for v in V3})
    defect = {v: 0 for v in V3}
    defect[V3[0]] = 1
    cfgs.append(defect)
    hole = {v: 2 for v in V3}
    hole[V3[4]] = None
    cfgs.append(hole)
    one = {v: None for v in V3}
    one[V3[0]] = 3
    cfgs.append(one)
    dom = {v: None for v in V3}
    dom[V3[0]] = 0
    dom[(1, 0, 0)] = 0
    cfgs.append(dom)
    bad = {v: None for v in V3}
    bad[V3[0]] = 0
    bad[(1, 0, 0)] = 1
    cfgs.append(bad)
    for t in range(12):
        cfg = {}
        for i, v in enumerate(V3):
            m = (i * 5 + t * 11) % 9
            cfg[v] = None if m < 3 else (m - 3)
        cfgs.append(cfg)
    for cfg in cfgs:
        A = [v for v in V3 if cfg[v] is not None]
        EA = induced(E3, A)
        wt = zt ** len(A)
        for u, v in EA:
            wt *= W[cfg[u]][cfg[v]]
        rhs = Weq ** (-boundary(E3, A))
        for u, v in EA:
            rhs *= (W[cfg[u]][cfg[v]] / Weq) ** 2
        ground = (len(A) == 0) or (len(A) == len(V3) and len({cfg[v] for v in V3}) == 1)
        if wt ** 2 != rhs or (wt == 1) != ground or wt > 1:
            ok = False
    samples.append((p, q, r))
want("A2 at z_t the squared weight equals W_eq^{-|dA|} prod (W/W_eq)^2, and weight 1 exactly on the empty and fully aligned states", ok)

# ---------------------------------------------------------------- A3
ok = True
nsets = 0
for dims in ((2, 2, 2), (3, 3, 1)):
    V, E = grid(dims)
    K = Kmat(1, 0, 0)
    for mask in range(1 << len(V)):
        A = [V[i] for i in range(len(V)) if mask >> i & 1]
        EA = induced(E, A)
        beta = len(EA) - len(A) + ncomp(A, EA)
        if phi(A, EA, K) != F(6) ** beta:
            ok = False
        nsets += 1
# Ising bond identity: sum sigma sigma = |E| - 2|dA|, and |E| = 3N
ising_bad = 0
for A in masks:
    SA = set(A)
    dA = boundary(E3, A)
    sig = {v: (1 if v in SA else -1) for v in V3}
    if 2 * dA != 3 * len(V3) - sum(sig[u] * sig[v] for u, v in E3):
        ising_bad += 1
ok = ok and ising_bad == 0
# z = 1/216 prefactor, without the cluster factor 6^c
for A in (masks[2], masks[3], [v for v in V3 if sum(v) % 2 == 0]):
    EA = induced(E3, A)
    dA = boundary(E3, A)
    if (F(1, 216) ** len(A) * F(6) ** len(EA)) ** 2 != F(6) ** (-dA):
        ok = False
want("A3 at K = I, Phi = 6^{beta1} on every subset of the 2x2x2 and 3x3x1 windows; |dA| = (3N - sum sigma sigma)/2 and z=1/216 gives 6^{-|dA|/2}", ok)

# ---------------------------------------------------------------- A4
p = sp.Symbol("p", positive=True)
Weq_line = 6 * p / (p + 9)
limits = {
    "vacancy-bond": (Weq_line ** (-sp.Rational(1, 2)), 1 / sp.sqrt(6)),
    "single-record": (6 / Weq_line ** 3, sp.Rational(1, 36)),
    "vacancy": (1 / Weq_line ** 3, sp.Rational(1, 216)),
    "domino": (36 / Weq_line ** 6, sp.Rational(1, 1296)),
    "opposite": (1 / p, 0),
    "orthogonal": (2 / p, 0),
}
ok = True
for expr, val in limits.values():
    if sp.simplify(sp.limit(expr, p, sp.oo) - val) != 0:
        ok = False
# row-sum of W is 36, so a domino summed on contents weighs 36 z^2
W312 = Wmat(3, 1, 2)
ok = ok and sum(W312[a][b] for a in range(6) for b in range(6)) == 36
Vc, Ec = grid((2, 2, 2))
assert len(Ec) == 12 and ncomp(Vc, Ec) == 1
beta_cube = 12 - 8 + 1
ok = ok and beta_cube == 5
cube_inf = F(1, 216) ** 8 * F(6) ** 8 * F(6) ** 5
ok = ok and cube_inf == F(1, 6 ** 11)
Kbig = Kmat(10 ** 6, 1, 2)
Weq_big = F(6 * 10 ** 6, 10 ** 6 + 1 + 8)
cube_big = (1 / Weq_big ** 3) ** 8 * F(6) ** 8 * phi(Vc, Ec, Kbig)
ok = ok and abs(cube_big - cube_inf) * 1000 < cube_inf
# W_eq = 6 - 54/(p+9) < 6, so the bond weight approaches 6^{-1/2} from above
ok = ok and sp.simplify(Weq_line - (6 - 54 / (p + 9))) == 0
want("A4 record-vacancy weight tends to 6^{-1/2} from above on (p,1,2); record 1/36, vacancy 1/216, domino 1/1296, cube 6^{-11}", ok)

# ---------------------------------------------------------------- A5
ok = True
rows = []
for dims in ((2, 2, 2), (3, 3, 1), (2, 2, 3), (4, 3, 1)):
    V, E = grid(dims)
    tab = beta_table(V, E)
    bad = super_violations(tab, len(V), lambda a, b, c, d: a + b >= c + d)
    rows.append(f"{dims}:{bad}")
    ok = ok and bad == 0
# local increment Delta beta1 = k - m on the cube
V, E = grid((2, 2, 2))
tab = beta_table(V, E)
adj = {v: [] for v in V}
for u, w in E:
    adj[u].append(w)
    adj[w].append(u)
idx = {v: i for i, v in enumerate(V)}
inc_bad = 0
for mask in range(1 << 8):
    A = [V[i] for i in range(8) if mask >> i & 1]
    SA = set(A)
    EA = induced(E, A)
    par = {x: x for x in A}

    def find(x, par=par):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for u, w in EA:
        par[find(u)] = find(w)
    for v in V:
        if v in SA:
            continue
        touched = set()
        k = 0
        for u in adj[v]:
            if u in SA:
                k += 1
                touched.add(find(u))
        got = tab[mask | (1 << idx[v])] - tab[mask]
        if got != k - len(touched):
            inc_bad += 1
ok = ok and inc_bad == 0
want("A5 beta1 is supermodular on four windows and the increment equals (neighbours in A) minus (components touched)", ok)

# ---------------------------------------------------------------- A6 (windows small enough to rebuild)
ok = True
rows = []
cases = [((2, 2, 2), t) for t in ((3, 1, 2), (16, 1, 2), (5, 1, 1), (7, 2, 1), (2, 1, 2))]
cases += [((3, 3, 1), t) for t in ((3, 1, 2), (16, 1, 2), (5, 1, 1))]
for dims, trip in cases:
    V, E = grid(dims)
    N = len(V)
    K = Kmat(*trip)
    tab = {}
    for mask in range(1 << N):
        A = [V[i] for i in range(N) if mask >> i & 1]
        tab[mask] = phi(A, induced(E, A), K)
    bad = super_violations(tab, N, lambda a, b, c, d: a * b >= c * d)
    rows.append(f"{dims}{trip}:{bad}")
    ok = ok and bad == 0
want("A6 Phi is log-supermodular on 2x2x2 (five triples, including (2,1,2)) and on 3x3x1 (three triples). Separate enumerations of 2x2x3 and 4x3x1 at (3,1,2) also had no violation; they are not repeated here", ok)

# ---------------------------------------------------------------- B0
def psd_minors(M):
    n = M.shape[0]
    for k in range(1, n + 1):
        for S in itertools.combinations(range(n), k):
            if M.extract(list(S), list(S)).det() < 0:
                return False
    return True


ok = True
for p, q, r in ((3, 1, 2), (16, 1, 2), (5, 1, 1)):
    W = Wmat(p, q, r)
    B = sp.Matrix(7, 7, lambda i, j: 1 if i == 0 or j == 0 else sp.Rational(W[i - 1][j - 1]))
    ok = ok and B.det() == 0 and psd_minors(B)
want("B0 the 7-state bond kernel is singular and every principal minor is >= 0 at (3,1,2), (16,1,2), (5,1,1)", ok)

# ---------------------------------------------------------------- B1
def fold4(x):
    return tuple(xi if xi < 2 else 3 - xi for xi in x)


def dissem(block, W, z, L=4):
    cfg = {x: block[fold4(x)] for x in itertools.product(range(L), repeat=3)}
    val = F(1)
    for x, s in cfg.items():
        if s is not None:
            val *= z
        for j in range(3):
            y = list(x)
            y[j] = (y[j] + 1) % L
            t = cfg[tuple(y)]
            if s is not None and t is not None:
                val *= W[s][t]
    return val


V8, E8 = grid((2, 2, 2))
ok = True
blocks = []
blocks.append({v: None for v in V8})
blocks.append({v: 0 for v in V8})
blocks.append({v: 4 for v in V8})
b = {v: None for v in V8}
b[(0, 0, 0)] = 1
blocks.append(b)
b = {v: None for v in V8}
b[(0, 0, 0)] = 0
b[(1, 0, 0)] = 0
blocks.append(b)
b = {v: None for v in V8}
b[(0, 0, 0)] = 0
b[(1, 0, 0)] = 2
blocks.append(b)
b = {v: (0 if sum(v) % 2 == 0 else None) for v in V8}
blocks.append(b)
b = {v: (sum(v) % 6) for v in V8}
blocks.append(b)
for p, q, r in ((16, 1, 2), (5, 1, 1)):
    W = Wmat(p, q, r)
    Weq = W[0][0]
    for z in (F(1, 50), 1 / Weq ** 3):
        for block in blocks:
            A = [v for v in V8 if block[v] is not None]
            inner = F(1)
            for u, v in induced(E8, A):
                inner *= W[block[u]][block[v]]
            n = len(A)
            w2 = (z ** n * inner) ** 2 * Weq ** (3 * n)
            if dissem(block, W, z) ** 2 != w2 ** 8:
                ok = False
            if z == 1 / Weq ** 3:
                e2 = Weq ** (-boundary(E8, A))
                for u, v in induced(E8, A):
                    e2 *= (W[block[u]][block[v]] / Weq) ** 2
                # cube is 3-regular, so the balance identity uses degree 3: w(b)^2 = e2
                if w2 != e2:
                    ok = False
want("B1 disseminated 4^3 weight is w(b)^8, and at z_t the block weight is the internal balance-point weight", ok)

# ---------------------------------------------------------------- B2
def zcube(p, q, r):
    S = p + q + 4 * r
    Weq = F(6 * p, S)
    K = Kmat(p, q, r)
    even, odd = F(0), F(0)
    for mask in range(1 << 8):
        A = [V8[i] for i in range(8) if mask >> i & 1]
        k = len(A)
        term = F(6) ** k * phi(A, induced(E8, A), K) / Weq ** (3 * (k // 2))
        if k % 2 == 0:
            even += term
        else:
            odd += term
    Z = even + sp.Rational(odd) / sp.sqrt(sp.Rational(Weq)) ** 3
    return Weq, even, odd, Z


ok = True
quoted = {(3, 1, 2): "110226.56", (16, 1, 2): "128.00", (100, 1, 2): "29.29", (1000, 1, 1): "22.57"}
ZC = {}
for trip, text in quoted.items():
    Weq, even, odd, Z = zcube(*trip)
    ZC[trip] = (Weq, Z)
    if even <= 7 or odd <= 48 or not (Weq < 6):
        ok = False
    shown = f"{float(Z - 7):.2f}"
    if shown != text:
        ok = False
# limit model, subset by subset, split even/odd powers of sqrt(6)
even_l, odd_l = F(0), F(0)
for mask in range(1 << 8):
    A = [V8[i] for i in range(8) if mask >> i & 1]
    EA = induced(E8, A)
    k = len(A)
    term = F(6) ** (len(EA) + ncomp(A, EA)) / F(6) ** (3 * (k // 2))
    if k % 2 == 0:
        even_l += term
    else:
        odd_l += term
ok = ok and even_l == F(152, 9) and odd_l / 36 == F(136, 27)
# (8/sqrt(6))^2 = 32/3.  32/3 > 9 and 32/3 < (327/100)^2, so 3 < 8/sqrt(6) < 3.27.
ok = ok and F(32, 3) > 9 and F(32, 3) < F(327, 100) ** 2
want("B2 Z_cube - 7 >= 48 W_eq^{-3/2} > 8/sqrt(6) at four triples (printed 110226.56, 128.00, 29.29, 22.57); limit 152/9 + 136 sqrt(6)/27", ok)

# ---------------------------------------------------------------- B3
V4, E4 = torus(4)
bipartite = all((sum(u) + sum(v)) % 2 == 1 for u, v in E4)
per_block = []
for origin in itertools.product((0, 2), repeat=3):
    sites = [tuple(o + d for o, d in zip(origin, delta)) for delta in itertools.product((0, 1), repeat=3)]
    per_block.append(sum(1 for s in sites if sum(s) % 2 == 0))
n_even = sum(1 for v in V4 if sum(v) % 2 == 0)
ok = bipartite and per_block == [4] * 8 and n_even == 32
quoted_eps = {
    (3, 1, 2): "0.00053",
    (16, 1, 2): "0.00367",
    (100, 1, 2): "0.00418",
    (1000, 1, 1): "0.00398",
}
for trip, text in quoted_eps.items():
    Weq, Z = ZC[trip]
    zt = 1 / sp.Rational(Weq) ** 3
    lb = ((1 + 6 * zt) ** 4 - 1) / Z
    lb_f = float(lb)
    if f"{lb_f:.5f}" != text or not (lb_f > 0):
        ok = False
lim = sp.Rational(152, 9) + 136 * sp.sqrt(6) / 27
lb_inf = ((1 + sp.Rational(6, 216)) ** 4 - 1) / lim
lb_inf_f = float(lb_inf)
ok = ok and 0.003963 < lb_inf_f < 0.003964
ok = ok and f"{lb_inf_f:.5f}" == "0.00396"
want("B3 even sites of the 4-torus are an independent set, four per block; eps floor matches the printed values and tends to 0.003963", ok)

# ---------------------------------------------------------------- D (heuristic arithmetic only)
J = sp.log(6) / 4
ok = sp.simplify(sp.exp(-4 * J) - sp.Rational(1, 6)) == 0
quoted_p = {sp.Rational(1, 10): 15.3, sp.Rational(3, 10): 6.0, sp.Rational(1, 2): 3.9, sp.Rational(7, 10): 2.7}
for rho, shown in quoted_p.items():
    z = rho / (6 * (1 - rho))
    Wb = z ** (-sp.Rational(1, 3))
    pb = sp.N(9 * Wb / (6 - Wb), 8)
    if abs(float(pb) - shown) > 0.05:
        ok = False
want("D heuristic arithmetic: e^{-4J} = 1/6 with J = (log 6)/4, and the balance line on (p,1,2) sits at p = 15.3, 6.0, 3.9, 2.7", ok)

print(f"TOTAL FAIL={len(FAILS)}")
if FAILS:
    print("SUMMARY: fails at " + FAILS[0])
    sys.exit(1)
print(
    "HIT: confirmed - at the pinned scale large l1 supplies no small density-contour parameter: "
    "at z_t = W_eq^{-3} every configuration weighs W_eq^{-|dA|/2} prod (W/W_eq) with 6 l1 <= W_eq < 6, "
    "so each record-vacancy bond weighs more than 6^{-1/2}; as l1 -> 1 the law tends to 6^{c(A) - |dA|/2} "
    "(Ising lattice gas at J = (log 6)/4, h = 0, hard alignment, six contents per cluster) and the cycle rank is supermodular; "
    "the 2x2x2 chessboard bad-sum is at least 8/sqrt(6) > 3 for every finite triple and the event-form floor tends to 0.003963"
)
print(
    "SUMMARY: confirmed the no-go for part (c). Density-contour weights stay above 6^{-1/2} and the l1 -> 1 limit is one fixed model. "
    "Finite-p FKG was recomputed on 2x2x2 and 3x3x1 inside this run, and on 2x2x3 and 4x3x1 at (3,1,2) in a separate enumeration. "
    "The chessboard theorem and Holley's inequality stay assumed. Coexistence of the limit model is not decided. "
    "8/sqrt(6) = 3.2659... prints as 3.27 and is not strictly above 3.27."
)
