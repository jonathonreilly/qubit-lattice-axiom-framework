"""moving-kernel-with-vacancies, attempt a1 (w-jonathonsmac4f50-jaae5): checks.

Exact (fractions, integers, sympy) for every finite claim; the few floating-point items are marked NUMERIC in their
labels and are not used by any exact claim.

Objects.  Site state u = empty or a content s (two-valued menu: s = +1/-1; sphere menu: s on S^2).  Bond kernel
B(empty, .) = 1, B(s, s') = c e^{beta s.s'}.  Records' field sigma_x = n_x s_x.  E(k) = sum_i 2(1 - cos k_i).
c0(g) = 1/cosh g (two-valued), g/sinh g (sphere): the least scale at which the vacancy kernel with coupling g is
positive semidefinite (block 39, T5).  S(k) = <|sigma^(k)|^2>, sigma^(k) = N^{-1/2} sum_x e^{ikx} sigma_x.
"""
import itertools
from fractions import Fraction as F

import sympy as sp

RESULTS = []


def want(label, ok, detail=""):
    RESULTS.append((label, bool(ok)))
    print(("PASS " if ok else "FAIL ") + label + ((" :: " + str(detail)) if detail != "" else ""), flush=True)


# ------------------------------------------------------------------------------------------------ exact log bounds
def log_bounds(num, den, terms):
    """rational (lower, upper) bounds for ln(num/den) > 0: ln x = 2 atanh(q), q = (x-1)/(x+1) = sum 2 q^(2j+1)/(2j+1)."""
    x = F(num, den)
    q = (x - 1) / (x + 1)
    s = F(0)
    for j in range(terms):
        s += 2 * q ** (2 * j + 1) / (2 * j + 1)
    tail = 2 * q ** (2 * terms + 1) / ((2 * terms + 1) * (1 - q * q))
    return s, s + tail


LN2 = log_bounds(2, 1, 30)
LN3 = log_bounds(3, 1, 30)
LN5 = log_bounds(5, 1, 60)
LN20 = (2 * LN2[0] + LN5[0], 2 * LN2[1] + LN5[1])
want("L0 rational log brackets are consistent with each other (ln 20 = 2 ln 2 + ln 5; widths < 1e-12)",
     all(u - l < F(1, 10 ** 12) for l, u in (LN2, LN3, LN5)) and LN20[0] < LN20[1]
     and LN3[0] > F(10986, 10000) and LN3[1] < F(10987, 10000) and LN20[0] > F(29957, 10000),
     f"ln3 in ({float(LN3[0]):.12f}, {float(LN3[1]):.12f}), ln20 in ({float(LN20[0]):.12f}, {float(LN20[1]):.12f})")

# ------------------------------------------------------------------------------------------------ F: the factorization
b, bp, c, t, g = sp.symbols("beta betap c t gamma", positive=True)
# state pairs (n, n', s.s' = t): the Gaussian factor at strength bp times the vacancy kernel at coupling beta - bp
def gauss(n1, n2, tt):
    sq = n1 + n2 - 2 * n1 * n2 * tt           # |sigma - sigma'|^2 for unit contents
    return sp.exp(bp * (n1 + n2) / 2 - bp * sq / 2)


def vac(n1, n2, tt, coupling):
    return c * sp.exp(coupling * tt) if n1 * n2 else sp.Integer(1)


ok = all(sp.simplify(vac(n1, n2, t, b) - gauss(n1, n2, t) * vac(n1, n2, t, b - bp)) == 0
         for n1, n2 in ((0, 0), (0, 1), (1, 0), (1, 1)))
want("F1 B(u,u') = e^{(bp/2)(n+n')} e^{-(bp/2)|sigma-sigma'|^2} R_{beta-bp}(u,u') for all four occupation pairs, symbolic in s.s'", ok)

# F2: the two-valued vacancy kernel with coupling g: explicit expansion with non-negative coefficients iff c cosh g >= 1
states = [(0, 0), (1, 1), (1, -1)]           # (n, s)
kappa = c * sp.cosh(g) - 1
ok = all(sp.simplify(((c * sp.exp(g * s1 * s2) if n1 * n2 else 1)
                      - (1 + kappa * n1 * n2 + c * sp.sinh(g) * n1 * n2 * s1 * s2)).rewrite(sp.exp)) == 0
         for (n1, s1) in states for (n2, s2) in states)
want("F2 R_g = 1 + (c cosh g - 1) n n' + (c sinh g) n n' s s' on all 9 state pairs (two-valued): a sum of products, "
     "coefficients >= 0 exactly when c >= 1/cosh g", ok)
Rm = sp.Matrix(3, 3, lambda i, j: (c * sp.exp(g * states[i][1] * states[j][1]) if states[i][0] * states[j][0] else 1))
comp = sp.Matrix(2, 2, lambda i, j: Rm[i + 1, j + 1] - 1)      # Schur complement of the empty entry
v_const, v_odd = sp.Matrix([1, 1]), sp.Matrix([1, -1])
want("F3 the complement of the empty state has eigenvector (1,1) with eigenvalue 2c cosh g - 2 and (1,-1) with 2c sinh g: the two-valued "
     "kernel is PSD iff c >= 1/cosh g",
     (comp * v_const - (2 * c * sp.cosh(g) - 2) * v_const).applyfunc(lambda e: sp.simplify(e.rewrite(sp.exp))) == sp.zeros(2, 1)
     and (comp * v_odd - 2 * c * sp.sinh(g) * v_odd).applyfunc(lambda e: sp.simplify(e.rewrite(sp.exp))) == sp.zeros(2, 1))

# sphere: Legendre coefficients a_l(g) = (2l+1)/2 int e^{g u} P_l(u) du > 0 (Rodrigues form), a_0 = sinh g / g
u = sp.Symbol("u")
ok = True
for l in range(0, 5):
    direct = (2 * l + 1) * sp.Rational(1, 2) * sp.integrate(sp.exp(g * u) * sp.legendre(l, u), (u, -1, 1))
    rod = (2 * l + 1) * sp.Rational(1, 2) * g ** l / (2 ** l * sp.factorial(l)) * sp.integrate((1 - u ** 2) ** l * sp.exp(g * u), (u, -1, 1))
    ok = ok and sp.simplify(direct - rod) == 0
a0 = sp.Rational(1, 2) * sp.integrate(sp.exp(g * u), (u, -1, 1))
want("F4 sphere: Legendre coefficients of e^{g t} equal their Rodrigues forms (integrand (1-t^2)^l e^{gt} > 0) for l <= 4, "
     "and a_0 = sinh g / g, so the sphere vacancy kernel is PSD iff c >= g/sinh g",
     ok and sp.simplify(a0 - sp.sinh(g) / g) == 0)
dc0 = sp.simplify(sp.diff(g / sp.sinh(g), g) * sp.sinh(g) ** 2)       # = sinh g - g cosh g
want("F5 c0 decreases strictly: d/dg (g/sinh g) = (sinh g - g cosh g)/sinh^2 g < 0 and d/dg (1/cosh g) = -tanh g/cosh g < 0 for g > 0 "
     "(sampled exactly at g = 1/10, 1, 5)",
     sp.simplify(dc0 - (sp.sinh(g) - g * sp.cosh(g))) == 0
     and all(float((sp.sinh(x) - x * sp.cosh(x)).evalf(30)) < 0 for x in (sp.Rational(1, 10), 1, 5)))

# ------------------------------------------------------------------------------------------------ the 2x2x2 torus, exact
SITES = [(a, bb, cc) for a in range(2) for bb in range(2) for cc in range(2)]
IDX = {x: i for i, x in enumerate(SITES)}
BONDS = []
for x in SITES:
    for i in range(3):
        y = list(x); y[i] = (y[i] + 1) % 2
        BONDS.append((IDX[x], IDX[tuple(y)]))
KV = [k for k in itertools.product((0, 1), repeat=3) if any(k)]           # k = pi * KV
SGN = {k: [(-1) ** sum(ki * xi for ki, xi in zip(k, x)) for x in SITES] for k in KV}
EK = {k: 4 * sum(k) for k in KV}                                            # E(pi k) = sum_i 2(1 - cos(pi k_i))

# A1: the all-sites twist's linear term is the plane-wave Laplacian term, configuration by configuration
lap_ok = True
for conf in itertools.product((-1, 0, 1), repeat=8):
    for k in KV:
        psi = SGN[k]
        X = sum((psi[i] - psi[j]) * (conf[i] - conf[j]) for i, j in BONDS)
        if X != EK[k] * sum(p * v for p, v in zip(psi, conf)):
            lap_ok = False
want("A1 2x2x2 torus, all 3^8 configurations and all 7 wavevectors: sum_b (psi_x - psi_y)(sigma_x - sigma_y) = E(k) sum_x sigma_x psi_x "
     "(the twist of every site's field gives the Laplacian term; empty sites included)", lap_ok)

GROUPS = {}
for conf in itertools.product((-1, 0, 1), repeat=8):
    n = [v * v for v in conf]
    al = an = 0
    for i, j in BONDS:
        if n[i] and n[j]:
            if conf[i] == conf[j]:
                al += 1
            else:
                an += 1
    key = (sum(n), al, an)
    gr = GROUPS.setdefault(key, [0, 0, 0, {k: 0 for k in KV}])
    gr[0] += 1; gr[1] += sum(n); gr[2] += al + an
    for k in KV:
        gr[3][k] += sum(s * v for s, v in zip(SGN[k], conf)) ** 2


def torus_stats(w, cc, z):
    """exact rho, rho2 and S(k) on the 2x2x2 torus with e^beta = w (rational), scale cc, fugacity z."""
    Z = F(0); r1 = F(0); r2 = F(0); Sk = {k: F(0) for k in KV}
    for (nocc, al, an), (cnt, occ, oo, sk) in GROUPS.items():
        wt = F(z) ** nocc * F(cc) ** (al + an) * F(w) ** al / F(w) ** an
        Z += cnt * wt; r1 += wt * occ; r2 += wt * oo
        for k in KV:
            Sk[k] += wt * sk[k]
    return r1 / (8 * Z), r2 / (24 * Z), {k: Sk[k] / (8 * Z) for k in KV}


# X1: the full-beta infrared bound fails at the neutral scale
w1, c1n, z1 = 3, F(2 * 3, 3 * 3 + 1), F(1, 8)
rho, rho2, Sk = torus_stats(w1, c1n, z1)
kpi = (1, 1, 1)
lhs_low = Sk[kpi] * EK[kpi] * LN3[0]
want("X1 COUNTEREXAMPLE, 2x2x2 torus, two-valued menu, e^beta = 3, neutral scale c0 = 1/cosh(ln 3) = 3/5, z = 1/8, k = (pi,pi,pi): "
     "S(k) beta E(k) > 1, so <|sigma^(k)|^2> <= 1/(beta E(k)) is false at the neutral scale",
     c1n == F(3, 5) and lhs_low > F(147, 100),
     f"S(k) = {Sk[kpi]} = {float(Sk[kpi]):.6f}, E = 12, S E beta > {float(lhs_low):.6f}; rho = {float(rho):.4f}, rho2 = {float(rho2):.4f}")

# X2: the bond-density form 1/(beta rho2 E) fails at the neutral scale
w2, c2n, z2 = 20, F(2 * 20, 20 * 20 + 1), F(1, 5)
rho_b, rho2_b, Sk_b = torus_stats(w2, c2n, z2)
lhs2 = Sk_b[kpi] * EK[kpi] * rho2_b * LN20[0]
want("X2 COUNTEREXAMPLE, 2x2x2 torus, two-valued menu, e^beta = 20, neutral scale c0 = 40/401, z = 1/5, k = (pi,pi,pi): "
     "S(k) beta rho2 E(k) > 1, so <|sigma^(k)|^2> <= 1/(beta rho2 E(k)) (attempt a3's (b)) is false at the neutral scale",
     c2n == F(40, 401) and lhs2 > F(181, 100),
     f"S(k) = {float(Sk_b[kpi]):.6f}, rho = {float(rho_b):.4f}, rho2 = {float(rho2_b):.4f}, S E beta rho2 > {float(lhs2):.6f}")

# A2: controls of Theorem A on the same torus (upper log brackets): c = 1 and c = 2 with the full beta; the split point
ctrl = True; worst = F(0)
for (w, cc, lnb) in ((3, F(1), LN3), (3, F(2), LN3), (20, F(1), LN20)):
    for z in (F(1, 20), F(1, 8), F(1, 5), F(1, 2), F(1), F(2)):
        _, _, S_ = torus_stats(w, cc, z)
        m = max(S_[k] * EK[k] for k in KV) * lnb[1]
        worst = max(worst, m)
        ctrl = ctrl and m <= 1
want("A2 control of Theorem A (c >= 1, full beta): max_k S(k) beta E(k) <= 1 on the 2x2x2 torus at e^beta in {3, 20}, c in {1, 2}, "
     "six fugacities from 1/20 to 2", ctrl, f"largest value < {float(worst):.6f}")
# split point: e^beta = 20, e^gamma = 4, c = 1/cosh(ln 4) = 8/17, beta - gamma = ln 5
ctrl = True; worst = F(0)
for z in (F(1, 20), F(1, 8), F(1, 5), F(1, 2), F(1), F(2)):
    _, _, S_ = torus_stats(20, F(8, 17), z)
    m = max(S_[k] * EK[k] for k in KV) * LN5[1]
    worst = max(worst, m)
    ctrl = ctrl and m <= 1
want("A3 control of Theorem A below scale 1: e^beta = 20, c = 8/17 = 1/cosh(ln 4), so beta - gamma(c) = ln 5: "
     "max_k S(k) (beta - gamma) E(k) <= 1 at six fugacities", ctrl, f"largest value < {float(worst):.6f}")
# a sharper split control: e^beta = 3, c = 4/5 = 1/cosh(ln 2), beta - gamma = ln(3/2); c < c1(ln 3), so Theorem B does not apply
LN32 = log_bounds(3, 2, 40)
ctrl = True; worst = F(0); fullb = F(0)
for z in (F(1, 20), F(1, 10), F(1, 8), F(1, 5), F(1, 4), F(1, 2), F(1), F(2)):
    _, _, S_ = torus_stats(3, F(4, 5), z)
    m = max(S_[k] * EK[k] for k in KV)
    worst = max(worst, m * LN32[1]); fullb = max(fullb, m * LN3[0])
    ctrl = ctrl and m * LN32[1] <= 1
want("A4 control of Theorem A: e^beta = 3, c = 4/5 = 1/cosh(ln 2), beta - gamma(c) = ln(3/2): max_k S(k) (beta - gamma) E(k) <= 1 at eight "
     "fugacities from 1/20 to 2 (recorded, not claimed: the same maximum with the full beta)", ctrl,
     f"largest value < {float(worst):.6f}; with the full beta > {float(fullb):.6f}")

# X3: attempt a3's twist (bonds with an empty end not twisted) does not produce the Laplacian term
ring = [1, 1, 0, 1]; psi = [1, 0, -1, 0]; Ek = 2                     # 4-ring, k = pi/2
occ_only = sum((psi[i] - psi[(i + 1) % 4]) * (ring[i] - ring[(i + 1) % 4]) for i in range(4) if ring[i] and ring[(i + 1) % 4])
all_sites = sum((psi[i] - psi[(i + 1) % 4]) * (ring[i] - ring[(i + 1) % 4]) for i in range(4))
lap = Ek * sum(p * v for p, v in zip(psi, ring))
want("X3 4-ring, sigma = (+1, +1, empty, +1), k = pi/2: the occupied-bonds-only linear term is 0 while E(k) sum sigma psi = 2 "
     "(the all-sites twist gives 2): twisting only record-record bonds does not give the structure factor of sigma",
     occ_only == 0 and all_sites == 2 and lap == 2, f"occupied-only {occ_only}, all-sites {all_sites}, Laplacian {lap}")

# ------------------------------------------------------------------------------------------------ Theorem B (two-valued): c1
tt = sp.Symbol("tt")
gs = sp.exp(-b * tt ** 2 / 2)
gd1, gd2 = sp.diff(gs, tt), sp.diff(gs, tt, 2)
vecs = [((n, v), d) for (n, v) in ((0, 0), (1, 1), (1, -1)) for d in (0, 1)]


def gram_entry(x, y):
    (n1, v1), d1 = x
    (n2, v2), d2 = y
    D = v1 - v2
    val = {(0, 0): gs, (1, 0): -gd1, (0, 1): gd1, (1, 1): -gd2}[(d1, d2)].subs(tt, D)
    return sp.exp(b * (n1 + n2) / 2) * val


G = sp.Matrix(6, 6, lambda i, j: gram_entry(vecs[i], vecs[j]))
Gee, Geo, Goo = G.extract([0, 1], [0, 1]), G.extract([0, 1], [2, 3, 4, 5]), G.extract([2, 3, 4, 5], [2, 3, 4, 5])
c1_formula = ((1 + b ** 2) * sp.sinh(b) - b * sp.cosh(b)) / (sp.sinh(b) * sp.cosh(b) - b)
Msym = sp.simplify(Goo.inv() * Geo.T * Gee.inv() * Geo)
evsym = list(Msym.eigenvals().keys())
want("B1 infinitesimal twist, two-valued: the limit Gram (values and shift-derivatives) has G_ee = diag(1, beta), and "
     "c1 = ((1+beta^2) sinh beta - beta cosh beta)/(sinh beta cosh beta - beta) is, symbolically, an eigenvalue of G_oo^-1 G_eo^T G_ee^-1 G_eo",
     sp.simplify(Gee - sp.diag(1, b)) == sp.zeros(2, 2)
     and sum(1 for e in evsym if sp.simplify((e - c1_formula).rewrite(sp.exp)) == 0) == 1, f"{len(evsym)} distinct eigenvalues")
ok = True; det_ = []
for bv in (sp.Rational(1, 2), 1, 2, 3, 5, 8):
    evs = [sp.re(sp.N(e.subs(b, bv), 40)) for e in evsym]
    top = max(evs)
    c1v = c1_formula.subs(b, bv).evalf(40)
    c0v = (1 / sp.cosh(bv)).evalf(40)
    ok = ok and abs(top - c1v) < sp.Float("1e-30") and c0v < c1v < 1
    det_.append((str(bv), float(c0v), float(c1v)))
want("B2 c1 is the LARGEST generalized eigenvalue and c0 < c1 < 1 at beta = 1/2, 1, 2, 3, 5, 8 (40-digit evaluation)", ok,
     "(beta, c0, c1) = " + ", ".join(f"({a}, {x:.5f}, {y:.5f})" for a, x, y in det_))


# NUMERIC: the two-shift union at a small finite shift difference reproduces c1 (floating point; not used by exact claims)
def ccrit_float(beta, bpv, D):
    import numpy as np
    pts = [(0, 0, 0.0), (0, 0, D)] + [(1, s, a) for a in (0.0, D) for s in (1, -1)]

    def K(p, q):
        (n1, s1, a1), (n2, s2, a2) = p, q
        gg = np.exp((bpv / 2) * (n1 + n2) - (bpv / 2) * (n1 * s1 - a1 - n2 * s2 + a2) ** 2)
        return gg * (np.exp((beta - bpv) * s1 * s2) if n1 * n2 else 1.0)
    Gm = np.array([[K(p, q) for q in pts] for p in pts])
    return max(np.linalg.eigvals(np.linalg.solve(Gm[2:, 2:], Gm[:2, 2:].T @ np.linalg.solve(Gm[:2, :2], Gm[:2, 2:]))).real)


import math
ok = all(abs(ccrit_float(bv, bv, 1e-3) - float(c1_formula.subs(b, bv))) < 1e-5 for bv in (1.0, 2.0, 3.0))
want("N1 NUMERIC two shifts 0 and 10^-3 apart: the least scale keeping the full-beta twisted kernel PD equals c1 to 1e-5 (beta = 1, 2, 3)", ok)
rows = []
ok = True
for beta in (1.0, 3.0, 5.0):
    c0v = 1 / math.cosh(beta)
    vals = [ccrit_float(beta, bpv, 1e-3) for bpv in (0.01, 0.1, 0.5 * beta)]
    ok = ok and all(v > c0v for v in vals) and vals == sorted(vals)
    rows.append(f"beta={beta}: c0={c0v:.5f}, c_crit(bp=0.01, 0.1, beta/2) = " + ", ".join(f"{v:.5f}" for v in vals))
want("N2 NUMERIC at the neutral scale every partial twist strength bp > 0 fails for small twists: c_crit(0+; bp) > c0(beta), increasing in bp",
     ok, "; ".join(rows))


# NUMERIC: the sphere menu on rings (harmonic sum truncated at l = 40; 40 digits) -- the same two failures at the neutral scale
def sphere_ring(beta, cc, z, N, m, Lmax=40):
    import mpmath as mp
    mp.mp.dps = 40
    lam = lambda l: mp.sqrt(mp.pi / (2 * beta)) * mp.besseli(l + mp.mpf(1) / 2, beta)
    A = mp.matrix([[1, mp.sqrt(z)], [mp.sqrt(z), z * cc * lam(0)]])
    tl = [None] + [z * cc * lam(l) for l in range(1, Lmax + 2)]
    Fq = lambda l, p: ((A ** p)[1, 1] if l == 0 else tl[l] ** p)
    Z = (A ** N)[0, 0] + (A ** N)[1, 1] + sum((2 * l + 1) * tl[l] ** N for l in range(1, Lmax + 1))
    rho = ((A ** N)[1, 1] + sum((2 * l + 1) * tl[l] ** N for l in range(1, Lmax + 1))) / Z
    rho2 = (A[1, 1] * (A ** (N - 1))[1, 1] + sum((2 * l + 1) * tl[l] ** N for l in range(1, Lmax + 1))) / Z
    C = [sum((l + 1) * (Fq(l, N - r) * Fq(l + 1, r) + Fq(l + 1, N - r) * Fq(l, r)) for l in range(0, Lmax)) / Z for r in range(N)]
    k = 2 * mp.pi * m / N
    Sk = sum(mp.cos(k * r) * C[r] for r in range(N))
    return float(C[0] - rho), float(Sk * 2 * (1 - mp.cos(k)) * beta / 3), float(Sk * 2 * (1 - mp.cos(k)) * beta * rho2 / 3)


import mpmath
pts = [(3, 10 ** 0.25, 6, 3), (5, 1.0, 6, 3), (8, 1.0, 16, 8), (8, 10 ** 0.5, 4, 2)]
out = []
for beta, z, N, m in pts:
    cc = beta / math.sinh(beta)
    out.append((beta, z, N, m) + sphere_ring(mpmath.mpf(beta), mpmath.mpf(cc), mpmath.mpf(z), N, m))
want("N3 NUMERIC sphere menu, rings, neutral scale c0 = beta/sinh beta: sum rule C(0) = rho holds; the per-component full-beta bound "
     "<|sigma^e(k)|^2> beta E(k) <= 1 fails at beta = 3, 5, 8; the bond-density form fails at beta = 8 (4-ring)",
     all(abs(o[4]) < 1e-20 for o in out) and out[0][5] > 1 and out[1][5] > 1 and out[2][5] > 1 and out[3][6] > 1,
     "; ".join(f"beta={o[0]} z={o[1]:.4g} N={o[2]} m={o[3]}: S beta E/3 = {o[5]:.4f}, with rho2 = {o[6]:.4f}" for o in out))


# NUMERIC: the sphere's infinitesimal-twist threshold (Legendre basis, m = 0 sector; truncation gives lower bounds, converged)
def c1_sphere(beta, Lm):
    import mpmath as mp
    mp.mp.dps = 50
    n = Lm + 1
    lam = [mp.sqrt(mp.pi / (2 * beta)) * mp.besseli(l + mp.mpf(1) / 2, beta) for l in range(n)]
    E = mp.diag(lam)
    T = mp.zeros(n, n)
    for l in range(n - 1):
        T[l, l + 1] = T[l + 1, l] = (l + 1) / mp.sqrt((2 * l + 1) * (2 * l + 3))
    G00 = E; G01 = beta * (T * E - E * T); G11 = beta * E - beta ** 2 * (T * T * E - 2 * T * E * T + E * T * T)
    Goo_ = mp.zeros(2 * n, 2 * n)
    for i in range(n):
        for j in range(n):
            Goo_[i, j] = G00[i, j]; Goo_[i, n + j] = G01[i, j]; Goo_[n + i, j] = G01[j, i]; Goo_[n + i, n + j] = G11[i, j]
    e0 = mp.zeros(n, 1); e0[0] = 1
    Tq = T * e0; T2q = T * T * e0
    Geo_ = mp.zeros(2, 2 * n)
    for i in range(n):
        Geo_[0, i] = e0[i]; Geo_[0, n + i] = -beta * Tq[i]
        Geo_[1, i] = beta * Tq[i]; Geo_[1, n + i] = beta * e0[i] - beta ** 2 * T2q[i]
    Gee_ = mp.matrix([[1, 0], [0, beta]])
    M = Gee_ ** -1 * Geo_ * (Goo_ ** -1) * Geo_.T
    return max(mp.re(x) for x in mp.eig(M)[0])


rows = []; ok = True
for beta in (1, 3, 5, 8):
    v12, v20 = c1_sphere(mpmath.mpf(beta), 12), c1_sphere(mpmath.mpf(beta), 20)
    c0v = beta / math.sinh(beta)
    ok = ok and abs(v12 - v20) < mpmath.mpf(10) ** -20 and c0v < v20 < 1
    rows.append(f"beta={beta}: c0={c0v:.5f} c1_sphere={float(v20):.6f}")
want("N4 NUMERIC sphere menu: the infinitesimal-twist threshold (m = 0, Legendre truncation l <= 12 and <= 20 agree to 1e-20) "
     "lies strictly between the neutral scale and 1", ok, "; ".join(rows))

npass = sum(1 for _, o in RESULTS if o)
nfail = len(RESULTS) - npass
print(f"TOTAL: PASS={npass} FAIL={nfail}")
if nfail == 0:
    print("SUMMARY: PARTIAL Gaussian domination for the law with vacancies holds with twist strength beta - gamma(c) (gamma/sinh gamma = c, "
          "gamma = 0 for c >= 1; 1/cosh for the two-valued menu), the twist moving every site's field sigma = n s, empty sites included; "
          "infrared bound 1/((beta - gamma(c)) E(k)) with no density dependence, and the full 1/(beta E(k)) for c >= c1(beta) "
          "(two-valued closed form; sphere numerically); at the neutral scale the route closes and both the full-beta bound and "
          "attempt a3's 1/(beta rho2 E(k)) are false (exact 2x2x2 counterexamples)")
    print("HIT: for the law with vacancies <|sigma^e(k)|^2> <= 1/((beta - gamma(c)) E(k)) for every z (so LRO in 3D once "
          "(beta - gamma(c)) rho > 3 G(0), no bond density needed); at the neutral scale c = c0(beta) the infrared bound with beta and "
          "the bond-density bound 1/(beta rho2 E(k)) of attempt a3 both fail (2x2x2 torus, exact: 1.47 and 1.81 > 1)")
