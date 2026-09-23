#!/usr/bin/env python3
"""J:derive:the-bond-laws-completion-beyond-second-order:a3 -- worker w-macbookpro90c72-j4e2d.

Block 59's bond-rate law (open PR #8581) completed beyond second order and
balanced against the free sea (block 76, a comparator) on block 89's
alternation family u_b = delta_j (-1)^{x_j} on the bonds of axis j
(block 89, open PR #8678).  See ATTEMPT.md for the statement and the steps.

  A  structure: exact (sympy, integers, Fractions); A7 is a floating spectrum.
  B  decisions: rigorous monotone-quadrature bounds on the Bessel form of the
     sea's gain G(mu) = <sqrt(|s|^2+mu)> - <|s|>, float64 with safety factor
     1e-9 (step S0 of ATTEMPT.md: i0e checked against 30-digit mpmath).
  C  executed numbers (floating point; evidence, not proof).
"""
import itertools
from collections import Counter
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.special import i0e, erf
from scipy.optimize import brentq, minimize, minimize_scalar

NF = 0
NP = 0


def rep(tag, ok, msg):
    global NF, NP
    NF += (not ok)
    NP += bool(ok)
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


# ---------------------------------------------------------------- torus 4^3
L = 4
BONDS = [(x, y, z, j) for x in range(L) for y in range(L) for z in range(L) for j in range(3)]
MID = []
for (x, y, z, j) in BONDS:
    m = [2 * x, 2 * y, 2 * z]
    m[j] += 1
    MID.append(m)                      # doubled midpoint


def classify():
    pairs, per = [], Counter()
    for i in range(len(BONDS)):
        for i2 in range(i + 1, len(BONDS)):
            dd = []
            for a1, a2 in zip(MID[i], MID[i2]):
                t = (a2 - a1) % (2 * L)
                dd.append(t - 2 * L if t > L else t)
            d2 = sum(t * t for t in dd)
            if d2 == 2:
                cls = 'perp'
            elif d2 == 4:
                j = BONDS[i][3]
                assert BONDS[i2][3] == j
                cls = 'coll' if dd[j] != 0 else 'par'
            else:
                continue
            pairs.append((i, i2, cls))
            per[(i, cls)] += 1
            per[(i2, cls)] += 1
    counts = {c: sorted(set(per[(i, c)] for i in range(len(BONDS)))) for c in ('perp', 'coll', 'par')}
    return pairs, counts


PAIRS, COUNTS = classify()
KNUM = {'coll': 2.0, 'perp': 3.0, 'par': 5.0}          # alpha, beta, delta (distinct, exact in float)


def lapK(K=KNUM):
    n = len(BONDS)
    LK = np.zeros((n, n))
    for (i, i2, c) in PAIRS:
        LK[i, i] += K[c]; LK[i2, i2] += K[c]; LK[i, i2] -= K[c]; LK[i2, i] -= K[c]
    return LK


# ------------------------------------------------------------------ A family
def A1():
    lam, kap, inv, d = sp.symbols('lambda kappa inv delta', positive=True)
    sea2 = -sp.Rational(3, 2) * inv * d**2           # block 89 T2 at unit one
    w0 = sp.solve(sp.diff(lam * sea2 + 6 * kap * d**2, d, 2), kap)[0]
    w1 = sp.solve(sp.diff(lam * (sea2 + 6 * kap * d**2), d, 2), kap)[0]
    ok = sp.simplify(w0 - lam * inv / 4) == 0 and sp.simplify(w1 - inv / 4) == 0
    rep("A1 unit", ok, "weight-0 law: threshold lambda<1/|s|>/4 moves with the unit lambda; weight-1 ledger: <1/|s|>/4 at every unit")


def A2():
    n = 6
    u = sp.symbols('u0:%d' % n)
    g0, g1, g2, g3, t = sp.symbols('g0 g1 g2 g3 t')
    f = lambda vp, vm: g0 + g1 * (vp + vm) + g2 * (vp**2 + vm**2) / 2 + g3 * vp * vm
    F = sum(sp.exp(u[b]) * f(u[(b + 1) % n] - u[b], u[(b - 1) % n] - u[b]) for b in range(n))
    hom = sp.expand(F.subs({x: x + t for x in u}, simultaneous=True) - sp.exp(t) * F) == 0
    H = sp.hessian(F, u).subs({x: 0 for x in u})
    rows = all(sp.expand(sum(H[i, j] for j in range(n)) - g0) == 0 for i in range(n))
    rep("A2 no-mass", hom and rows,
        "weight-1 local ledger sum_b c_b f(v_b) (ring, generic f): F(u+t)=e^t F(u); Hessian rows sum to f(0): mass f(0) at every k")


def A3():
    x = sp.symbols('x', real=True)
    g = sp.Function('g')
    S = sp.exp(x / 2) * g(-x) + sp.exp(-x / 2) * g(x)
    even = sp.simplify(S.subs(x, -x) - S) == 0
    a2, a4 = sp.symbols('a2 a4')
    profs = [4 * (sp.cosh(x / 2) - 1), x * sp.sinh(x / 2), a2 * x**2 + a4 * x**4, sp.cosh(sp.Rational(3, 7) * x) - 1]
    back = all(sp.simplify(sp.exp(x / 2) * (ph.subs(x, -x) * sp.exp(-x / 2) / 2)
                           + sp.exp(-x / 2) * (ph * sp.exp(x / 2) / 2) - ph) == 0 for ph in profs)
    c, cp, l = sp.symbols('c cp l', positive=True)
    Psi = lambda ph, c, cp: sp.sqrt(c * cp) * ph.subs(x, sp.log(c / cp))
    hom = all(sp.simplify(sp.expand((Psi(ph, l * c, l * cp) - l * Psi(ph, c, cp)).rewrite(sp.exp))) == 0 for ph in profs[:2])
    n1 = sp.simplify(sp.expand((Psi(profs[0], c, cp) - 2 * (sp.sqrt(c) - sp.sqrt(cp))**2).rewrite(sp.exp))) == 0
    n2 = sp.simplify(sp.expand((Psi(profs[1], c, cp) - (c - cp) * sp.log(c / cp) / 2).rewrite(sp.exp))) == 0
    rep("A3 pairs", even and back and hom and n1 and n2,
        "c_b g(u_b'-u_b)+c_b' g(u_b-u_b') = sqrt(cc') phi(u_b-u_b'), phi even; every even phi arises; weight 1; "
        "phi=4(cosh(x/2)-1) is 2(sqrt c-sqrt c')^2, phi=x sinh(x/2) is (c-c')log(c/c')/2")


def A4():
    ok_counts = COUNTS == {'perp': [8], 'coll': [2], 'par': [4]}
    LK = lapK()
    a, b, dl = KNUM['coll'], KNUM['perp'], KNUM['par']
    c0 = -2 * a - 8 * b - 4 * dl
    worst = 0.0
    for n1, n2, n3 in itertools.product(range(L), repeat=3):
        k = 2 * np.pi * np.array([n1, n2, n3]) / L
        W = np.zeros((len(BONDS), 3), complex)
        for i, bd in enumerate(BONDS):
            W[i, bd[3]] = np.exp(0.5j * np.dot(k, MID[i]))
        B = W.conj().T @ LK @ W / L**3
        M = np.zeros((3, 3))
        for j in range(3):
            M[j, j] = c0 + 2 * a * np.cos(k[j]) + 2 * dl * sum(np.cos(k[l]) for l in range(3) if l != j)
            for l in range(3):
                if l != j:
                    M[j, l] = 4 * b * np.cos(k[j] / 2) * np.cos(k[l] / 2)
        worst = max(worst, np.abs(B + M).max())
    rep("A4 match", ok_counts and worst < 1e-11,
        f"4^3 torus: per bond 8 perp, 2 coll, 4 par; Hessian of sum K sqrt(cc')phi (phi''(0)=1) = -M(k) of block 59 T3 at all 64 k (max dev {worst:.0e})")


def A5():
    A, a, b, dl = sp.symbols('A alpha beta delta_par')
    Bs = sp.symbols('B0:3')
    u, v = sp.symbols('u v')
    e = sp.symbols('e')
    s1 = sp.series(sp.exp(e * u), e, 0, 3).removeO().coeff(e, 2)
    s2 = sp.series(sp.exp(e * (u + v) / 2), e, 0, 3).removeO().coeff(e, 2)
    ok_exp = sp.expand(s1 - u**2 / 2) == 0 and sp.expand(s2 - ((u**2 + v**2) / 4 - (u - v)**2 / 8)) == 0
    n, K = (2, 8, 4), (a, b, dl)
    eqs = [A / 2 + sum(Bs[X] * n[X] for X in range(3)) / 4] + [-Bs[X] / 8 - K[X] / 2 for X in range(3)]
    sol = sp.solve(eqs, [A] + list(Bs), dict=True)
    ok_n1 = len(sol) == 1 and sp.expand(sol[0][A] - 2 * sum(K[X] * n[X] for X in range(3))) == 0 \
        and all(sp.expand(sol[0][Bs[X]] + 4 * K[X]) == 0 for X in range(3))
    gam, KK = sp.symbols('gamma K')
    sec = sp.expand(u * gam * (v - u) + v * gam * (u - v))          # e^u g(v-u)+e^v g(u-v), g linear, 2nd order
    ok_n2 = sp.solve(sp.Eq(sec, KK / 2 * (u - v)**2), gam) == [-KK / 2]
    rng = np.random.default_rng(5)
    uu = rng.normal(0, 0.7, len(BONDS)); cc = np.exp(uu)
    LK = lapK()
    fn2a = 0.5 * cc @ (LK @ uu)
    fn2b = sum(KNUM[c] / 2 * (cc[i] - cc[i2]) * (uu[i] - uu[i2]) for (i, i2, c) in PAIRS)
    nb = {'coll': 2, 'perp': 8, 'par': 4}
    fn1a = 2 * sum(KNUM[c] * (np.sqrt(cc[i]) - np.sqrt(cc[i2]))**2 for (i, i2, c) in PAIRS)
    fn1b = 2 * sum(KNUM[c] * nb[c] for c in nb) * cc.sum() - 4 * sum(KNUM[c] * np.sqrt(cc[i] * cc[i2]) for (i, i2, c) in PAIRS)
    ok_t = abs(fn2a - fn2b) < 1e-9 * abs(fn2a) and abs(fn1a - fn1b) < 1e-9 * abs(fn1a)
    rep("A5 members", ok_exp and ok_n1 and ok_n2 and ok_t,
        "N1: A sum c_b + sum_X B_X sum sqrt(c_b c_b') massless+matched only for A=2 sum K_X n_X, B_X=-4K_X, i.e. 2 sum K(sqrt c-sqrt c')^2; "
        "N2: energy per tick linear in log ratios only with slope -K/2, i.e. F=(1/2)<c,-M log c> (torus identity)")


def A6():
    cnt = Counter()
    for (i, i2, c) in PAIRS:
        k1 = ((-1) ** BONDS[i][BONDS[i][3]], BONDS[i][3])
        k2 = ((-1) ** BONDS[i2][BONDS[i2][3]], BONDS[i2][3])
        cnt[(c, tuple(sorted([k1, k2])))] += 1
    S = L**3
    pred = Counter()
    for j in range(3):
        pred[('coll', ((-1, j), (1, j)))] += S
        pred[('par', ((1, j), (1, j)))] += S
        pred[('par', ((-1, j), (-1, j)))] += S
    for i, j in itertools.combinations(range(3), 2):
        for s, t in itertools.product((1, -1), repeat=2):
            pred[('perp', tuple(sorted([(s, i), (t, j)])))] += S
    ok_ms = cnt == pred
    d = sp.symbols('d0:3', real=True)
    al, be, dp = sp.symbols('alpha beta delta_par', positive=True)
    Kc = {'coll': al, 'perp': be, 'par': dp}
    phi = sp.Function('phi')

    def canon(x):
        x = sp.expand(x)
        for dj in d:
            cf = x.coeff(dj)
            if cf != 0:
                return x if cf > 0 else -x
        return sp.Integer(0)

    def cost(pf):
        return sum(Kc[c] * sp.Rational(m, S) * pf(s1 * d[j1], s2 * d[j2]) for (c, ((s1, j1), (s2, j2))), m in cnt.items())

    gen = cost(lambda u, v: sp.exp((u + v) / 2) * phi(canon(u - v))).subs(phi(0), 0)
    closed = al * sum(phi(2 * dj) for dj in d) + 2 * be * sum(
        sp.cosh((d[i] + d[j]) / 2) * phi(d[i] - d[j]) + sp.cosh((d[i] - d[j]) / 2) * phi(d[i] + d[j])
        for i, j in itertools.combinations(range(3), 2))
    ok_gen = sp.expand((gen - closed).rewrite(sp.exp)) == 0
    kap = al + 2 * be
    n2 = cost(lambda u, v: (sp.exp(u) - sp.exp(v)) * (u - v) / 2)
    ok_n2 = sp.expand((n2 - 2 * kap * sum(dj * sp.sinh(dj) for dj in d)).rewrite(sp.exp)) == 0
    dd = sp.symbols('delta', real=True)
    diag = closed.subs({d[0]: dd, d[1]: dd, d[2]: dd}).subs(phi(0), 0)
    ok_diag = sp.expand(diag - 3 * kap * phi(2 * dd)) == 0
    rep("A6 cost", ok_ms and ok_gen and ok_n2 and ok_diag,
        "exact pair multiset per site on the alternation family; cost = alpha sum phi(2d_j) + 2beta sum_{i<j}[cosh((d_i+d_j)/2)phi(d_i-d_j)"
        "+cosh((d_i-d_j)/2)phi(d_i+d_j)], delta_par absent; diagonal 3 kappa phi(2d); N2: 2 kappa sum d_j sinh d_j")


def A7():
    sig = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
    site = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)

    def H(dl):
        Hm = np.zeros((2 * L**3, 2 * L**3), complex)
        for (x, y, z, j) in BONDS:
            e = [0, 0, 0]; e[j] = 1
            c = np.exp((-1) ** [x, y, z][j] * dl[j])
            a_, b_ = site(x, y, z), site(x + e[0], y + e[1], z + e[2])
            blk = 0.5j * c * sig[j]
            Hm[2 * b_:2 * b_ + 2, 2 * a_:2 * a_ + 2] += blk
            Hm[2 * a_:2 * a_ + 2, 2 * b_:2 * b_ + 2] -= blk
        return Hm
    ks = [2 * np.pi * n / L for n in range(L)]
    worst = 0.0
    for dl in [(0.3, 0, 0), (0.3, 0.5, 0.2), (0.4, 0.4, 0.4), (1.1, 0, 0.7), (0, 0, 0)]:
        ev = np.sort(np.linalg.eigvalsh(H(dl)))
        mu = sum(np.sinh(v)**2 for v in dl)
        E = np.array([np.sqrt(sum(np.sin(q)**2 for q in kk) + mu) for kk in itertools.product(ks, repeat=3)])
        worst = max(worst, np.abs(ev - np.sort(np.concatenate([E, -E]))).max())
    rep("A7 mass", worst < 1e-12,
        f"premise (block 89 T1b) for independent delta_j on 4^3: spectrum = +-sqrt(sum sin^2 k + sum sinh^2 delta_j) (max dev {worst:.0e}); sea gain G(mu), mu = sum sinh^2 delta_j")


def A8():
    z, a, x, y, p = sp.symbols('z a x y p', positive=True)
    i1 = sp.simplify(sp.diff(sp.asinh(z) - z / sp.sqrt(1 + z**2), z) - z**2 / (1 + z**2)**sp.Rational(3, 2)) == 0
    h2 = sp.diff(sp.sqrt(y) * sp.asinh(sp.sqrt(y)), y, 2).subs(y, z**2)
    form = ((z / sp.sqrt(1 + z**2) - sp.asinh(z)) / (2 * z**2) - z / (2 * (1 + z**2)**sp.Rational(3, 2))) / (2 * z)
    i2 = sp.simplify(h2 - form) == 0
    X = lambda ex: sp.simplify(sp.expand(ex.rewrite(sp.exp))) == 0
    f = sp.sinh(a)**3 - 6 * sp.sinh(a) + 6 * a
    i3 = X(sp.diff(f, a) - 3 * (sp.cosh(a) - 1)**2 * (sp.cosh(a) + 2))
    i4 = X(sp.sinh(a)**2 - 2 * (sp.cosh(a) - 1) - (sp.cosh(a) - 1)**2)
    i5 = X((sp.cosh(a) - 1)**2 * (sp.cosh(a) + 1)**2 - sp.sinh(a)**4)
    i6 = X(z * sp.sinh(z) - 2 * (sp.cosh(z) - 1) - 4 * sp.sinh(z / 2) * sp.cosh(z / 2) * (z / 2 - sp.tanh(z / 2)))
    i7 = X(x * sp.sinh(x / 2) - 4 * (sp.cosh(x / 2) - 1) - 2 * ((x / 2) * sp.sinh(x / 2) - 2 * (sp.cosh(x / 2) - 1)))
    i8 = sp.simplify(sp.diff((sp.cosh(p * x) - 1) / p**2, p) - (p * x * sp.sinh(p * x) - 2 * (sp.cosh(p * x) - 1)) / p**3) == 0
    i9 = X(sp.cosh(x) - 1 - x * sp.sinh(x / 2) - sp.sinh(x / 2) * (2 * sp.sinh(x / 2) - x))
    yy = np.linspace(1e-3, 1e3, 200001)
    num = np.diff(np.sqrt(yy) * np.arcsinh(np.sqrt(yy)), 2).max() < 0
    rep("A8 identities", all([i1, i2, i3, i4, i5, i6, i7, i8, i9, num]),
        "h(y)=sqrt(y)asinh(sqrt y) strictly concave; 6(sinh a-a)<=sinh^3 a; sinh^2-2(cosh-1)=(cosh-1)^2; "
        "x sinh(x/2) >= 4(cosh(x/2)-1); d/dp[(cosh px-1)/p^2] >= 0; cosh x-1 >= x sinh(x/2)")


# ------------------------------------------------------- B family (bounds)
SP = np.sqrt(np.pi)
NG = 200000
T1, TT = 1e-9, 1e9
TG = np.geomspace(T1, TT, NG)
DT = np.diff(TG)
K3 = i0e(TG / 2)**3
CK = (np.pi / 2)**3 * np.pi**-1.5          # K3(t) <= CK t^-3/2 (i0e(x) <= (pi/2)/sqrt(2 pi x))
SAFE = 1e-9


def inv_bounds():
    f = K3 * TG**-0.5
    up = np.dot(f[:-1], DT) + 2 * np.sqrt(T1) + CK / TT
    lo = np.dot(f[1:], DT) + K3[0] * 2 * np.sqrt(T1)
    return lo / SP * (1 - SAFE), up / SP * (1 + SAFE)


def G_up(mu):
    g = -np.expm1(-TG * mu) / TG * K3 * TG**-0.5
    return (np.dot(g[:-1], DT) + 2 * mu * np.sqrt(T1) + CK / (2 * TT * TT)) / (2 * SP) * (1 + SAFE)


def G_lo(mu):
    g = -np.expm1(-TG * mu) / TG * K3 * TG**-0.5
    return np.dot(g[1:], DT) / (2 * SP) * (1 - SAFE)


def psi(xv):
    out = np.empty_like(xv)
    s = xv < 1e-3
    xs = xv[s]
    out[s] = 0.5 - xs / 6 + xs**2 / 24 - xs**3 / 120
    xl = xv[~s]
    out[~s] = (xl + np.expm1(-xl)) / xl**2
    return out


def Jn_lo(mu):       # lower bound of J(mu)/mu^2
    p = psi(TG * mu)
    return np.dot(p[1:] * np.sqrt(TG[:-1]) * K3[1:], DT) / (2 * SP) * (1 - SAFE)


def Jn_up(mu):
    p = psi(TG * mu)
    return (np.dot(p[:-1] * np.sqrt(TG[1:]) * K3[:-1], DT) + T1**1.5 / 3 + CK / (mu * TT)) / (2 * SP) * (1 + SAFE)


def B0():
    dec = bool(np.all(np.diff(K3) <= 0))
    mp.mp.dps = 30
    worst = 0.0
    for tv in TG[::100]:
        ex = mp.besseli(0, mp.mpf(tv) / 2) * mp.exp(-mp.mpf(tv) / 2)
        worst = max(worst, abs(float(ex / mp.mpf(i0e(tv / 2))) - 1))
    rep("B0 special fns", dec and worst < 1e-13,
        f"K3=(e^-x I0(x))^3, x=t/2, decreasing on the grid; scipy i0e vs 30-digit mpmath at {len(TG[::100])} grid points: max rel dev {worst:.1e}")
    return worst


def B1():
    lo, up = inv_bounds()
    ok = lo < 0.91067 < up
    rep("B1 threshold", ok, f"<1/|s|> in [{lo:.6f},{up:.6f}], kappa_c=<1/|s|>/4 in [{lo/4:.6f},{up/4:.6f}] (block 89: 0.91067)")
    return lo / 4, up / 4


def B2():
    mp.mp.dps = 40
    r15 = mp.sqrt(mp.mpf(3) / 2)
    wit = []
    for name, ph, kap, dl in [('x^2/2', lambda x: x**2 / 2, 1, 8), ('x^2/2', lambda x: x**2 / 2, 10, 12),
                              ('p=0.45', lambda x: (mp.cosh(mp.mpf('0.45') * x) - 1) / mp.mpf('0.45')**2, 1, 40),
                              ('p=0.45', lambda x: (mp.cosh(mp.mpf('0.45') * x) - 1) / mp.mpf('0.45')**2, 10, 70)]:
        dl = mp.mpf(dl)
        B = 3 * kap * ph(2 * dl) - mp.sqrt(3) * mp.sinh(dl) + r15
        wit.append(B < 0)
    c = mp.sqrt(3) / (6 * mp.mpf('0.2277'))
    rep("B2 growth", all(wit),
        f"G(mu)>=sqrt(mu)-<|s|>, <|s|><=sqrt(3/2): profiles o(e^(|x|/2)) unbounded below at every kappa (witnesses: x^2/2 at kappa 1,10; p=0.45 at 1,10); "
        f"bounded at kappa_c needs liminf phi e^(-x/2) >= sqrt3/(6kappa_c) = {float(c):.3f} (N1: 2, N2: inf)")


def three_regions(tag, klo, khi, mu_of, cost_c, const, mu_s, x_L, label):
    """cost_c(x): cost at kappa=1 along the line; require kappa_c cost_c(x) > G(mu(x)) for all x>0.
    small x<=x_s: J(mu)/mu^2 >= Jn_lo(mu_s) > khi*const (const bounds (2mu-cost_c)/mu^2, exact);
    middle: monotone cells; large x>=x_L: exact inequality (checked separately)."""
    x_s = brentq(lambda x: mu_of(x) - mu_s, 1e-6, 50)
    small = Jn_lo(mu_s) > khi * const
    grid = np.geomspace(x_s, x_L * 1.0001, 700)
    margins = [klo * cost_c(grid[i]) / G_up(mu_of(grid[i + 1])) - 1 for i in range(len(grid) - 1)]
    mid = min(margins) > 0
    rep(tag, small and mid,
        f"{label}: kappa_c cost > G(mu) for all x>0: x<={x_s:.3f} by J/mu^2>={Jn_lo(mu_s):.4f}>{khi*const:.4f}; "
        f"{len(grid)-1} cells on [{x_s:.3f},{x_L:.3f}] min margin {min(margins):.3f}; x>={x_L:.3f} by G<sqrt(mu)")
    return small and mid


def B3(klo, khi):
    return three_regions("B3 N2 one axis", klo, khi, lambda a: np.sinh(a)**2, lambda a: 2 * a * np.sinh(a),
                         1 / 3, 1.0, 1 / (2 * klo), "N2 single axis, cost 2kappa a sinh a")


def B4(klo, khi):
    dL = 2 * np.arctanh(np.sqrt(3) / (12 * klo))
    return three_regions("B4 N1 diagonal", klo, khi, lambda d: 3 * np.sinh(d)**2, lambda d: 12 * (np.cosh(d) - 1),
                         1 / 6, 3.0, dL, "N1 on block 89's diagonal, cost 12kappa(cosh d-1)")


def B5():
    m1, m2 = 1e-6, 1e-5
    lo = (Jn_lo(m1) - Jn_up(m2)) / np.log(10)
    up = (Jn_up(m1) - Jn_lo(m2)) / np.log(10)
    c = 1 / (4 * np.pi**2)
    j0 = 4 * np.pi**2 * 0.5 * (Jn_lo(1e-6) + Jn_up(1e-6)) - np.log(1e6)
    ok = lo < c < up and (up - lo) < 0.02 * c
    rep("B5 Dirac log", ok, f"slope of J/mu^2 in log(1/mu) on [1e-6,1e-5] in [{lo:.5f},{up:.5f}] contains 1/(4pi^2)={c:.5f}; j0 = {j0:.3f}")
    return j0


def B6(klo, khi):
    C = lambda a, r: (1 - 2 * r) * 4 * (np.cosh(a) - 1) + r * (16 * np.cosh(a) - 32 * np.cosh(a / 2) + 16)
    w = G_lo(np.sinh(2.2)**2) / C(2.2, 0.1)
    mp.mp.dps = 30
    a = mp.mpf(12)
    Bn = mp.mpf('0.24') * 4 * (mp.cosh(a) - 1) - (mp.sinh(a) - mp.sqrt(mp.mpf(3) / 2))
    ok = w > khi and Bn < 0
    rep("B6 N1 one axis", ok,
        f"N1, beta/kappa=1/10: at a=2.2 G/cost >= {w:.5f} > kappa_c (uniform not global on [kappa_c,{w:.4f})); "
        f"beta=0, kappa=0.24>kappa_c: B(a=12) <= {float(Bn):.0f} < 0 (unbounded for kappa<1/(4+8beta/kappa))")


# --------------------------------------------------------- C family (executed)
def G_ex(mu):
    """executed G(mu): trapezoid on the grid, exact first cell (K3~1 there); subtracted form for mu>1."""
    if mu <= 1:
        g = -np.expm1(-TG * mu) / TG * K3 * TG**-0.5
        first = 2 * np.sqrt(np.pi * mu) * erf(np.sqrt(mu * T1)) - 2 * (-np.expm1(-mu * T1)) / np.sqrt(T1)
        return (np.dot((g[:-1] + g[1:]) / 2, DT) + first) / (2 * SP)
    g = -np.expm1(-TG * mu) * (1 - K3) * TG**-1.5
    first = 1.5 * (2 * np.sqrt(T1) - np.sqrt(np.pi / mu) * erf(np.sqrt(mu * T1)))
    return np.sqrt(mu) - (np.dot((g[:-1] + g[1:]) / 2, DT) + first) / (2 * SP)


def Gp_ex(mu):
    g = np.exp(-TG * mu) * K3 * TG**-0.5
    first = np.sqrt(np.pi / mu) * erf(np.sqrt(mu * T1))
    return (np.dot((g[:-1] + g[1:]) / 2, DT) + first) / (2 * SP)


def C1(kc):
    Q1 = lambda a: Gp_ex(np.sinh(a)**2) * np.sinh(a) * np.cosh(a) / (np.sinh(a) + a * np.cosh(a))
    Qd = lambda d: Gp_ex(3 * np.sinh(d)**2) * np.sinh(d) * np.cosh(d) / (np.sinh(d) + d * np.cosh(d))
    aa = np.linspace(0.002, 9, 300)
    mono = bool(np.all(np.diff([Q1(x) for x in aa]) < 0) and np.all(np.diff([Qd(x) for x in aa]) < 0))
    rows = []
    for k in [0.227, 0.225, 0.22, 0.21, 0.20, 0.18, 0.15, 0.10, 0.05]:
        a = brentq(lambda x: Q1(x) - k, 1e-5, 60)
        B1 = 2 * k * a * np.sinh(a) - G_ex(np.sinh(a)**2)
        d = brentq(lambda x: Qd(x) - k, 1e-5, 60)
        Bd = 6 * k * d * np.sinh(d) - G_ex(3 * np.sinh(d)**2)
        rows.append((k, a, np.sinh(a), B1, d, np.sqrt(3) * np.sinh(d), Bd))
    rep("C1 N2 minimiser", mono and all(r[3] < r[6] < 0 for r in rows),
        "kappa=Q(a) strictly decreasing on both lines: one minimiser per kappa<kappa_c, on one axis (lower than the diagonal)")
    print("  kappa | a*  m*=sinh a*  B* (one axis) | d*  m=sqrt3 sinh d*  B (diagonal)")
    for r in rows:
        print(f"  {r[0]:.3f} | {r[1]:.4f} {r[2]:.4g} {r[3]:.3g} | {r[4]:.4f} {r[5]:.4g} {r[6]:.3g}")
    return rows


def C2(kc, j0, rows):
    out = []
    for r in rows[:3]:
        k, mu = r[0], r[2]**2
        eps = kc - k
        lead = mu * np.log(1 / mu) / (4 * np.pi**2 * eps)
        refn = mu * (np.log(1 / mu) + j0 - 0.5 - 4 * np.pi**2 * k / 3) / (4 * np.pi**2 * eps)
        out.append((k, lead, refn))
    ok = all(abs(o[2] - 1) < 0.03 for o in out)
    rep("C2 law", ok, "m*^2 log(1/m*^2) / 4pi^2(kappa_c-kappa) = " + ", ".join(f"{o[1]:.2f}" for o in out)
        + "; with the constant j0-1/2-4pi^2 kappa/3: " + ", ".join(f"{o[2]:.3f}" for o in out))


def C3(rows):
    n = 96
    q = (np.arange(n) + 0.5) * (np.pi / 2) / n
    S2 = (np.sin(q)**2)[:, None, None] + (np.sin(q)**2)[None, :, None] + (np.sin(q)**2)[None, None, :]
    s = np.sqrt(S2)
    dev = max(abs((np.sqrt(S2 + mu) - s).mean() / G_ex(mu) - 1) for mu in (0.1, 1.0, 5.0))
    k = 0.2
    B = lambda v: 2 * k * np.sum(v * np.sinh(v)) - G_ex(np.sum(np.sinh(v)**2))
    rng = np.random.default_rng(11)
    best = min((minimize(B, rng.uniform(0.1, 1.5, 3), method='Nelder-Mead',
                         options={'xatol': 1e-7, 'fatol': 1e-12, 'maxiter': 4000}) for _ in range(6)), key=lambda r: r.fun)
    v = np.sort(np.abs(best.x))
    ref = [r for r in rows if abs(r[0] - k) < 1e-12][0]
    ok = dev < 2e-3 and abs(best.fun - ref[3]) < 1e-6 and v[1] < 1e-3 and abs(v[2] - ref[1]) < 1e-3
    rep("C3 controls", ok, f"midpoint zone sums 96^3 vs Bessel G: max rel dev {dev:.1e}; free 3-axis minimisation at kappa=0.2 -> "
        f"({v[2]:.4f},{v[1]:.0e},{v[0]:.0e}), B={best.fun:.5f} (one-axis line {ref[3]:.5f})")


def C4():
    Bq = lambda d, k: 6 * k * d * d - G_ex(3 * np.sinh(d)**2)
    ds = []
    for k in (0.225, 0.22, 0.21, 0.20):
        r = minimize_scalar(lambda d: Bq(d, k), bounds=(1e-3, 1.0), method='bounded', options={'xatol': 1e-8})
        ds.append(r.x)
    rb = minimize_scalar(lambda d: -Bq(d, 0.25), bounds=(1.0, 2.4), method='bounded', options={'xatol': 1e-8})
    cr = brentq(lambda d: Bq(d, 0.25), rb.x, 4)
    ok = all(abs(a - b) < 0.004 for a, b in zip(ds, (0.084, 0.168, 0.312, 0.480))) and abs(rb.x - 1.87) < 0.01 \
        and abs(-rb.fun - 0.82) < 0.01 and abs(cr - 2.51) < 0.01
    rep("C4 block 89", ok, "quadratic law, diagonal: d* = " + ", ".join(f"{x:.3f}" for x in ds)
        + f" (block 89: 0.084, 0.168, 0.312, 0.480); kappa=0.25 barrier {-rb.fun:.2f} at {rb.x:.2f}, below uniform from {cr:.2f}")


def C5(kc):
    C = lambda a, r: (1 - 2 * r) * 4 * (np.cosh(a) - 1) + r * (16 * np.cosh(a) - 32 * np.cosh(a / 2) + 16)

    def isup(r):
        best = (0, 0)
        for lo, hi in [(0.5, 1.5), (1.5, 2.5), (2.5, 4), (4, 7)]:
            res = minimize_scalar(lambda a: -G_ex(np.sinh(a)**2) / C(a, r), bounds=(lo, hi), method='bounded', options={'xatol': 1e-8})
            if -res.fun > best[0]:
                best = (-res.fun, res.x)
        return best
    r0 = brentq(lambda r: isup(r)[0] - kc, 0.1, 0.12, xtol=1e-6)
    g05, g10 = isup(0.05), isup(0.10)
    Cd = lambda d: 12 * (np.cosh(d) - 1)
    rng = np.random.default_rng(3)
    V = rng.uniform(0, 4, (4000, 3))
    V[:1000, 1:] = 0
    worst = {}
    for r in (0.25, 0.5):
        al, be = kc * (1 - 2 * r), kc * r
        def cost(v):
            c = al * sum(4 * (np.cosh(x) - 1) for x in v)
            for i, j in itertools.combinations(range(3), 2):
                c += 2 * be * (np.cosh((v[i] + v[j]) / 2) * 4 * (np.cosh((v[i] - v[j]) / 2) - 1)
                               + np.cosh((v[i] - v[j]) / 2) * 4 * (np.cosh((v[i] + v[j]) / 2) - 1))
            return c
        worst[r] = min(cost(v) / G_ex(np.sum(np.sinh(v)**2)) for v in V[::4] if np.sum(np.sinh(v)**2) > 0.1) - 1
    ok = 0.105 < r0 < 0.115 and g05[0] > kc and g10[0] > kc and min(worst.values()) > 0
    rep("C5 N1 ratio", ok, f"N1 one axis: uniform global above kappa_c iff beta/kappa >= r0 = {r0:.4f}; first order at "
        f"kappa={g05[0]:.4f} (a={g05[1]:.2f}), {g10[0]:.4f} (a={g10[1]:.2f}) for beta/kappa=0.05, 0.1; "
        f"3-axis samples (mu>0.1) at beta/kappa=0.25, 0.5: min cost/G-1 = {worst[0.25]:.3f}, {worst[0.5]:.3f}")


def main():
    A1(); A2(); A3(); A4(); A5(); A6(); A7(); A8()
    B0()
    klo, khi = B1()
    B2()
    b3 = B3(klo, khi)
    b4 = B4(klo, khi)
    j0 = B5()
    B6(klo, khi)
    kc = 0.5 * (klo + khi)
    rows = C1(kc)
    C2(kc, j0, rows)
    C3(rows)
    C4()
    C5(kc)
    print(f"TOTAL: PASS={NP} FAIL={NF}")
    if NF == 0:
        print("SUMMARY: PROVED (a),(b) for weight-one pair ledgers of block 59's law on block 89's alternation family "
              "(S0: float64 bounds, i0e checked against mpmath): one free even profile phi per class; phi = o(e^(|x|/2)), block 89's "
              "quadratic law included, is unbounded below at every kappa; diagonal: phi >= 4(cosh(x/2)-1) suffices (power family iff "
              "p >= 1/2); whole family: phi >= x sinh(x/2) suffices (N2, cost 2kappa sum d_j sinh d_j), N1 fails for beta/kappa below "
              "0.110 (witness at 1/10); transition continuous; (c) executed under N2")
        print("HIT: weight-one pair completions of block 59's law are F = sum K sqrt(c_b c_b') phi(log c_b/c_b'), one even profile per "
              "class; on block 89's alternation family the uniform field is the strict global minimum for every alpha+2beta >= <1/|s|>/4 "
              "when phi >= x sinh(x/2) (rate-weighted law F = (1/2) sum_b c_b (-M log c)_b, cost 2(alpha+2beta) sum_j d_j sinh d_j) and "
              "for no kappa when phi = o(e^(|x|/2)); the transition is then continuous, m^2 log(1/m^2) ~ 4pi^2(kappa_c-kappa), and under "
              "the rate-weighted law the alternation lies along one axis")
    else:
        print(f"SUMMARY: ROUTE FAILS AT {NF} check(s) above")


if __name__ == "__main__":
    main()
