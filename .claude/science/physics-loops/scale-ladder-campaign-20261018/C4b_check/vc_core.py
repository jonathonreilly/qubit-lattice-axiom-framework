"""C4b_check core: an independent POSITION-SPACE engine (no kb.py, no c4b_core).

Fields are sympy Functions of (x0, x1, x2).  Local functionals are densities; Poisson brackets are computed from
Euler-Lagrange (variational) derivatives:
    gravity  {h_ij(x), P_kl(y)} = delta_(ij),(kl) delta(x-y) on the 6 independent components; with densities written
             using the symmetric matrices h, P summed over ALL (i, j), the canonical momentum of h_ij (i<j) is 2 P_ij,
             so {F, G} = sum_{i<=j} (1/w_ij)(E_hij F E_Pij G - E_Pij F E_hij G), w_ii = 1, w_ij = 2.
    spinor   {chi_al(x), chibar_be(y)} = -i delta_al,be delta(x-y), chi = (c0, c1), chibar = (d0, d1) treated as
             independent fields: {F, G} = -i sum_al (E_cal F E_dal G - E_dal F E_cal G).
A density r linear in a test field N is a total divergence iff E_N(r) = 0 identically; equations are the
coefficients of E_N(r) as a polynomial in all field-jet atoms (split into real and imaginary parts).
"""
from __future__ import annotations
import itertools, time
import sympy as sp

X = sp.symbols("x0:3", real=True)
R3 = range(3)
I = sp.I
F_ = lambda name: sp.Function(name)(*X)


def hf(i, j):
    return F_(f"h{min(i, j)}{max(i, j)}")


def Pf(i, j):
    return F_(f"P{min(i, j)}{max(i, j)}")


Hm = sp.Matrix(3, 3, lambda i, j: hf(i, j))
Pm = sp.Matrix(3, 3, lambda i, j: Pf(i, j))
HCOMP = [(i, j) for i in R3 for j in R3 if i <= j]
c = [F_("c0"), F_("c1")]
d = [F_("d0"), F_("d1")]
N, M = F_("N"), F_("M")
xi = [F_(f"xi{k}") for k in R3]
eta = [F_(f"eta{k}") for k in R3]
th = [F_(f"th{k}") for k in R3]
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
ONE2 = sp.eye(2)
EPS = lambda a, b, cc: sp.LeviCivita(a, b, cc)
D = lambda e, k: sp.diff(e, X[k])


def euler(L, u):
    """variational derivative E_u(L) = sum_alpha (-D)^alpha dL/d(D^alpha u)."""
    L = sp.expand(L)
    ders = {a for a in L.atoms(sp.Derivative) if a.expr == u}
    out = sp.diff(L, u)
    for a in ders:
        t = sp.diff(L, a)
        vs = [v for v, n in a.variable_count for _ in range(n)]
        out += (-1) ** len(vs) * sp.diff(t, *vs)
    return sp.expand(out)


def pb(f, g, grav=True, ferm=True):
    out = 0
    if ferm:
        for al in range(2):
            Ecf, Edf = euler(f, c[al]), euler(f, d[al])
            Ecg, Edg = euler(g, c[al]), euler(g, d[al])
            out += -I * (Ecf * Edg - Edf * Ecg)
    if grav:
        for (i, j) in HCOMP:
            w = 1 if i == j else 2
            hu, pu = hf(i, j), Pf(i, j)
            Ehf, Epf = euler(f, hu), euler(f, pu)
            Ehg, Epg = euler(g, hu), euler(g, pu)
            if (Ehf == 0 or Epg == 0) and (Epf == 0 or Ehg == 0):
                continue
            out += sp.Rational(1, w) * (Ehf * Epg - Epf * Ehg)
    return sp.expand(out)


def is_h(a):
    f = a.expr if isinstance(a, sp.Derivative) else a
    return isinstance(f, sp.core.function.AppliedUndef) and f.func.__name__.startswith("h")


def hdeg_filter(expr, k):
    """keep the monomials of degree k in the h fields."""
    out = 0
    for t in sp.Add.make_args(sp.expand(expr)):
        n = 0
        for fac in sp.Mul.make_args(t):
            b, e = fac.as_base_exp()
            if is_h(b):
                n += int(e)
        if n == k:
            out += t
    return out


def jet_atoms(e):
    at = set(a for a in e.atoms(sp.Derivative))
    at |= set(a for a in e.atoms(sp.core.function.AppliedUndef))
    return sorted(at, key=str)


def coeff_eqs(e):
    e = sp.expand(e)
    if e == 0:
        return []
    gens = jet_atoms(e)
    out = []
    for cf in sp.Poly(e, *gens).coeffs():
        cf = sp.expand(cf)
        re, im = sp.expand(sp.re(cf)), sp.expand(sp.im(cf))
        for z in (re, im):
            if z != 0:
                out.append(z)
    return out


def div_eqs(r, test):
    """equations for the density r (linear in the test field `test`) to be a total divergence."""
    return coeff_eqs(euler(r, test))


# ---------------------------------------------------------------- matter
def bil(A, op=None):
    """chibar A chi for a 2x2 matrix A (multiplication)."""
    return sp.expand(sum(d[a] * A[a, b] * c[b] for a in range(2) for b in range(2)))


def walker(Lp, E, v=1):
    """int chibar 1/2{Lp E_aj sigma_a, p_j} chi, p_j = -i d_j, written out directly."""
    out = 0
    for a in R3:
        for j in R3:
            co = Lp * E[a, j]
            for al in range(2):
                for be in range(2):
                    s = SIG[a][al, be]
                    if s == 0:
                        continue
                    out += d[al] * (-I / 2) * (co * s * D(c[be], j) + D(co * s * c[be], j))
    return sp.expand(v * out)


def kosmann(vec, lam, w, kap):
    """lam int chibar i (vec.d + w div vec + i kap curl vec . sigma) chi."""
    div = sum(D(vec[k], k) for k in R3)
    curl = [sum(EPS(cc, k, j) * D(vec[j], k) for k in R3 for j in R3) for cc in R3]
    out = 0
    for al in range(2):
        out += d[al] * I * (sum(vec[k] * D(c[al], k) for k in R3) + w * div * c[al])
        for be in range(2):
            out += d[al] * I * (I * kap * sum(curl[cc] * SIG[cc][al, be] for cc in R3)) * c[be]
    return sp.expand(lam * out)


def spinrot(u, lam=1):
    """lam int chibar (u . sigma) chi  (u a vector of expressions)."""
    return sp.expand(lam * sum(u[k] * bil(SIG[k]) for k in R3))


# ---------------------------------------------------------------- gravity
def LieDelta(vec):
    return sp.Matrix(3, 3, lambda i, j: D(vec[j], i) + D(vec[i], j))


def LieH(vec, H=None):
    H = Hm if H is None else H
    return sp.Matrix(3, 3, lambda i, j: sum(vec[k] * D(H[i, j], k) + H[k, j] * D(vec[k], i) + H[i, k] * D(vec[k], j)
                                            for k in R3))


def Pdot(Xm):
    return sp.expand(sum(Pm[i, j] * Xm[i, j] for i in R3 for j in R3))


def sqrtgR_series(order=2):
    """[sqrt(g) R](n) for g = delta + t h, n = 1..order, computed from Christoffel symbols (own code)."""
    t = sp.Symbol("t")
    tr = lambda e: sp.expand(sp.series(e, t, 0, order + 1).removeO()) if e.has(t) else e
    def trunc(e):
        e = sp.expand(e)
        return sum(e.coeff(t, k) * t ** k for k in range(order + 1))
    H = Hm
    g = sp.eye(3) + t * H
    gi = sp.eye(3) - t * H + t ** 2 * H * H
    gi = gi.applyfunc(trunc)
    dg = [[[D(g[i, j], k) for k in R3] for j in R3] for i in R3]
    Gam = [[[trunc(sum(gi[k, l] * (dg[l][j][i] + dg[l][i][j] - dg[i][j][l]) for l in R3) / 2) for j in R3] for i in R3]
           for k in R3]   # Gam[k][i][j] = Gamma^k_ij
    Ric = [[trunc(sum(D(Gam[k][i][j], k) - D(Gam[k][i][k], j) for k in R3)
                  + sum(Gam[k][k][l] * Gam[l][i][j] - Gam[k][j][l] * Gam[l][i][k] for k in R3 for l in R3))
            for j in R3] for i in R3]
    R = trunc(sum(gi[i, j] * Ric[i][j] for i in R3 for j in R3))
    trh = sum(H[k, k] for k in R3)
    trhh = sum(H[i, j] * H[j, i] for i in R3 for j in R3)
    sg = 1 + t * trh / 2 + t ** 2 * (trh ** 2 / 8 - trhh / 4)
    sR = trunc(sg * R)
    return [sp.expand(sR.coeff(t, k)) for k in range(1, order + 1)]


# ---------------------------------------------------------------- frames
def frame_sym(a, order):
    """(delta + a h)^(-1/2) to `order` in h."""
    E = sp.eye(3) - a * Hm / 2
    if order >= 2:
        E += sp.Rational(3, 8) * a ** 2 * Hm * Hm
    return E.applyfunc(sp.expand)


def inv_series(E, order):
    Xd = E - sp.eye(3)
    Ei, term = sp.eye(3), sp.eye(3)
    for _ in range(order):
        term = (-term * Xd).applyfunc(sp.expand)
        Ei += term
    return Ei


RES = {"pass": 0, "fail": 0}
T0 = time.time()


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} [{time.time() - T0:.0f}s] {msg}", flush=True)


def total():
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}  ({time.time() - T0:.0f}s)", flush=True)


def vsolve(eqs, unk):
    """sp.solve, then back-substitute into EVERY equation: sympy silently drops equations that involve only parameters
    (found in this check), so a solution is kept only if all equations vanish on it."""
    sols = sp.solve(eqs, unk, dict=True)
    good = []
    for s_ in sols:
        if all(sp.simplify(sp.expand(e.subs(s_))) == 0 for e in eqs):
            good.append(s_)
        else:
            print(f"   [vsolve] rejected spurious solution {s_}", flush=True)
    return good
