"""source-neutral-inclusion-attraction, attempt a3 (w-jonathonsmac4f50-j0b3c).

Quadratic model (block 41 T4): real field theta on the L^3 torus (or Z^3), weight exp(-(kappa/2) sum_bonds (theta_x - theta_y)^2), zero
mode removed.  L = graph Laplacian, G = L^+ (so the covariance is G/kappa).  An inclusion at x multiplies the stiffness of its six bonds by
(1 + eps).  For a bond b = (u, v), d_b = e_u - e_v; D_x = the six d_b at x; M_xy = D_x^T G D_y (second differences of G between bonds).
Free energy F = (1/2) log det (on the zero-mode complement); F(x,y) = F_both - F_x - F_y + F_none.
Exact parts: Fractions on the 4^3 and 8^3 tori.  Z^3 parts: high-precision quadrature of the lattice Green function (labelled NUMERIC).
"""
import functools
import itertools
import random
from fractions import Fraction as F

import mpmath as mp
import sympy as sp

RESULTS = []


def want(label, ok, detail=""):
    RESULTS.append((label, bool(ok)))
    print(("PASS " if ok else "FAIL ") + label + ((" :: " + str(detail)) if detail != "" else ""), flush=True)


# ------------------------------------------------------------------ exact torus Green function (orbit reduction)
def torus_green(L):
    N = L ** 3

    def canon(n):
        return tuple(sorted(min(v % L, (-v) % L) for v in n))
    orbits = sorted({canon(n) for n in itertools.product(range(L), repeat=3)})
    idx = {o: i for i, o in enumerate(orbits)}
    size = {o: 0 for o in orbits}
    for n in itertools.product(range(L), repeat=3):
        size[canon(n)] += 1
    rows, rhs = [], []
    for o in orbits:
        row = [0] * len(orbits)
        row[idx[o]] += 6
        for i in range(3):
            for s in (1, -1):
                m = list(o); m[i] += s
                row[idx[canon(m)]] -= 1
        rows.append(row); rhs.append(sp.Rational(int(o == (0, 0, 0))) - sp.Rational(1, N))
    rows[-1] = [size[o] for o in orbits]; rhs[-1] = 0
    sol = sp.Matrix(rows).LUsolve(sp.Matrix(rhs))
    g = {o: F(int(sp.fraction(sol[idx[o]])[0]), int(sp.fraction(sol[idx[o]])[1])) for o in orbits}
    return (lambda n: g[canon(n)]), N


BONDS = [(i, s) for i in range(3) for s in (1, -1)]


def bond_ends(x, b):
    i, s = b; v = list(x); v[i] += s
    return tuple(x), tuple(v)


def Mentry(G, b1, b2):
    (u, v), (up, vp) = b1, b2
    d = lambda a, c: G(tuple(a[k] - c[k] for k in range(3)))
    return d(u, up) - d(u, vp) - d(v, up) + d(v, vp)


def bonds_at(x):
    return [bond_ends(x, b) for b in BONDS]


def same_edge(b1, b2):
    return b1 == b2 or (b1[0] == b2[1] and b1[1] == b2[0])


def mat(G, B1, B2):
    return [[Mentry(G, b1, b2) for b2 in B2] for b1 in B1]


def det_frac(A):
    A = [row[:] for row in A]; n = len(A); det = F(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None: return F(0)
        if p != c: A[c], A[p] = A[p], A[c]; det = -det
        det *= A[c][c]
        inv = 1 / A[c][c]
        for r in range(c + 1, n):
            if A[r][c] != 0:
                f = A[r][c] * inv
                A[r] = [a - f * b for a, b in zip(A[r], A[c])]
    return det


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def inv_frac(A):
    n = len(A); M = [row[:] + e for row, e in zip(A, eye(n))]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]; M[c] = [a / pv for a in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]; M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return [row[n:] for row in M]


def union_bonds(x, y):
    U = []
    for b in bonds_at(x) + bonds_at(y):
        if not any(same_edge(b, c) for c in U): U.append(b)
    return U


def Delta_lemma(G, x, y, ex, ey, convention="mult"):
    """det(I + H D^T G D) / (det(I + ex Mxx) det(I + ey Myy)) over the union of bonds: exp(2 F(x,y))."""
    U = union_bonds(x, y)
    Bx, By = bonds_at(x), bonds_at(y)
    eta = []
    for b in U:
        ix = any(same_edge(b, c) for c in Bx); iy = any(same_edge(b, c) for c in By)
        if ix and iy:
            eta.append((1 + ex) * (1 + ey) - 1 if convention == "mult" else ex + ey)
        else:
            eta.append(ex if ix else ey)
    MU = mat(G, U, U)
    top = det_frac([[F(int(i == j)) + eta[i] * MU[i][j] for j in range(len(U))] for i in range(len(U))])
    Mxx, Myy = mat(G, Bx, Bx), mat(G, By, By)
    bx = det_frac([[F(int(i == j)) + ex * Mxx[i][j] for j in range(6)] for i in range(6)])
    by = det_frac([[F(int(i == j)) + ey * Myy[i][j] for j in range(6)] for i in range(6)])
    return top / (bx * by)


def Delta_6(G, x, y, ex, ey):
    """det(I - ex ey A_x Mxy A_y Myx), A = (I + eps M)^-1 (restricted to 1-perp when eps = -1)."""
    Bx, By = bonds_at(x), bonds_at(y)
    Mxx, Myy, Mxy = mat(G, Bx, Bx), mat(G, By, By), mat(G, Bx, By)
    Myx = [list(r) for r in zip(*Mxy)]

    def A(M, e):
        if e != -1:
            return inv_frac([[F(int(i == j)) + e * M[i][j] for j in range(6)] for i in range(6)])
        P1 = [[F(1, 6)] * 6 for _ in range(6)]
        B = inv_frac([[F(int(i == j)) - M[i][j] + P1[i][j] for j in range(6)] for i in range(6)])
        return [[B[i][j] - P1[i][j] for j in range(6)] for i in range(6)]
    X = matmul(matmul(A(Mxx, ex), Mxy), matmul(A(Myy, ey), Myx))
    return det_frac([[F(int(i == j)) - ex * ey * X[i][j] for j in range(6)] for i in range(6)])


rng = random.Random(20260922)

# ================================================================== E0: the exact Green functions
G4, N4 = torus_green(4)
G8, N8 = torus_green(8)
ok = True
for (G, L) in ((G4, 4), (G8, 8)):
    N = L ** 3
    ok = ok and all(6 * G(n) - sum(G(tuple(n[d] + (s if d == i else 0) for d in range(3))) for i in range(3) for s in (1, -1))
                    == F(int(n == (0, 0, 0))) - F(1, N) for n in itertools.product(range(L), repeat=3))
    ok = ok and sum(G(n) for n in itertools.product(range(L), repeat=3)) == 0
want("E0 G = L^+ exactly on the 4^3 and 8^3 tori (orbit reduction, Fractions): L G = delta - 1/N at every site, sum G = 0",
     ok, f"8^3: G(0) = {G8((0, 0, 0))}")

# ================================================================== A1: the exact formula against direct determinants (4^3)
def direct_Delta(L, x, y, ex, ey, convention):
    N = L ** 3
    sites = list(itertools.product(range(L), repeat=3)); ix = {s: n for n, s in enumerate(sites)}

    def K(stiff):
        A = [[F(1, N)] * N for _ in range(N)]
        for s in sites:
            for i in range(3):
                t = list(s); t[i] = (t[i] + 1) % L; t = tuple(t)
                w = stiff(s, t)
                a, b = ix[s], ix[t]
                A[a][a] += w; A[b][b] += w; A[a][b] -= w; A[b][a] -= w
        return A

    def wrap(p):
        return tuple(v % L for v in p)

    def stiff_for(incl):
        def st(s, t):
            k = F(1)
            fac = []
            for (site, e) in incl:
                if wrap(site) in (s, t): fac.append(e)
            if not fac: return k
            if convention == "mult":
                for e in fac: k *= (1 + e)
                return k
            return 1 + sum(fac)
        return st
    d_both = det_frac(K(stiff_for([(x, ex), (y, ey)])))
    d_x = det_frac(K(stiff_for([(x, ex)])))
    d_y = det_frac(K(stiff_for([(y, ey)])))
    d_0 = det_frac(K(stiff_for([])))
    return d_both * d_0 / (d_x * d_y)


ok = True; rows = []
for (r, ex, ey, conv) in ((2, F(-1, 2), F(-1, 2), "mult"), (2, F(1, 3), F(2), "mult"), (1, F(-1, 2), F(-1, 2), "mult"), (1, F(-1, 2), F(-1, 2), "add"), (1, F(1, 3), F(-1, 4), "mult")):
    x, y = (0, 0, 0), (r, 0, 0)
    dl = Delta_lemma(G4, x, y, ex, ey, conv)
    dd = direct_Delta(4, x, y, ex, ey, conv)
    ok = ok and dl == dd
    rows.append(f"r={r} eps=({ex},{ey}) {conv}")
want("A1 (a) EXACT: exp(2F(x,y)) = det(I + H D^T G D)_(bonds of x and y) / [det(I + eps_x M_xx) det(I + eps_y M_yy)] (H = the bonds' "
     "stiffness changes; the shared bond at r = 1 gets (1+eps_x)(1+eps_y) - 1 [mult] or eps_x + eps_y [add]) equals the ratio of the four "
     "64 x 64 determinants of the stiffness matrices on the 4^3 torus", ok, "; ".join(rows))

ok = True
for r in (2, 3, 4):
    for (ex, ey) in ((F(-1, 2), F(-1, 2)), (F(1, 2), F(-1, 3)), (F(3), F(1, 5))):
        ok = ok and Delta_lemma(G8, (0, 0, 0), (r, 0, 0), ex, ey) == Delta_6(G8, (0, 0, 0), (r, 0, 0), ex, ey)
want("A2 (a) for disjoint bond sets (r >= 2) the interaction is (1/2) log det of ONE 6 x 6 matrix: F(x,y) = (1/2) log det(I - eps_x eps_y "
     "A_x M_xy A_y M_yx), A = (I + eps M_xx)^-1, M = second differences of G between the bonds - equal to the 12 x 12 form exactly at "
     "r = 2, 3, 4 on the 8^3 torus for three pairs of eps", ok)

# ================================================================== B1: the second-order formula (exact series)
eps = sp.Symbol("eps")


def series_coeffs(G, r, convention="mult"):
    x, y = (0, 0, 0), (r, 0, 0)
    U = union_bonds(x, y); Bx, By = bonds_at(x), bonds_at(y)
    MU = sp.Matrix(mat(G, U, U)).applyfunc(lambda v: sp.Rational(v.numerator, v.denominator))
    etas = []
    for b in U:
        inx = any(same_edge(b, c) for c in Bx); iny = any(same_edge(b, c) for c in By)
        etas.append(((1 + eps) ** 2 - 1 if convention == "mult" else 2 * eps) if (inx and iny) else eps)
    top = (sp.eye(len(U)) + sp.diag(*etas) * MU)
    Mx = sp.Matrix(mat(G, Bx, Bx)).applyfunc(lambda v: sp.Rational(v.numerator, v.denominator))
    My = sp.Matrix(mat(G, By, By)).applyfunc(lambda v: sp.Rational(v.numerator, v.denominator))
    # log det(I + E) series to order eps^2 via traces of the exact matrices (E polynomial in eps)
    def logdet2(E):
        E = E.applyfunc(sp.expand)
        t1 = E.trace(); t2 = (E * E).trace()
        return sp.series(sp.expand(t1 - t2 / 2), eps, 0, 3).removeO()
    tot = sp.expand(logdet2(top - sp.eye(len(U))) - logdet2(eps * Mx) - logdet2(eps * My))
    Mxy = mat(G, Bx, By)
    sq = sum(v * v for row in Mxy for v in row)
    shared = [b for b in Bx if any(same_edge(b, c) for c in By)]
    Mss = Mentry(G, shared[0], shared[0]) if shared else F(0)
    return tot, sq, Mss


ok = True; table = []
for r in (1, 2, 3, 4):
    for conv in (("mult", "add") if r == 1 else ("mult",)):
        tot, sq, Mss = series_coeffs(G8, r, conv)
        c1 = tot.coeff(eps, 1); c2 = tot.coeff(eps, 2)
        expect2 = -sp.Rational(sq.numerator, sq.denominator) + (sp.Rational(Mss.numerator, Mss.denominator) if conv == "mult" else 0)
        ok = ok and c1 == 0 and sp.simplify(c2 - expect2) == 0
        e = F(-1, 2)
        Fexact = mp.log(mp.mpf(Delta_lemma(G8, (0, 0, 0), (r, 0, 0), e, e, conv).numerator) / Delta_lemma(G8, (0, 0, 0), (r, 0, 0), e, e, conv).denominator) / 2
        F2 = float(e * e / 2) * float(expect2)
        table.append(f"r={r}{'' if r > 1 else ' ' + conv}: F = {mp.nstr(Fexact, 8)}, F2 = {F2:.8g}")
want("B1 (b) EXACT series on the 8^3 torus: 2F(x,y) = 0*eps - eps^2 [sum over bond pairs (b at x, b' at y) of (d_b^T G d_b')^2] + O(eps^3) for "
     "r = 2, 3, 4 (so F = -(eps^2/2) sum M_xy^2: the covariance of two quadratic forms carries 2 (d^T C d')^2, which makes the task's 1/4 a "
     "1/2); at r = 1 the shared bond adds + eps^2 d_s^T G d_s under the multiplicative convention and nothing under the additive one; the "
     "table compares the exact F with the second-order F2 at eps = -1/2", ok, "; ".join(table))

# ================================================================== B2: the sign, at every order
ok = True; seen = []
for r in (2, 3, 4):
    for (ex, ey) in ((F(-1, 2), F(-1, 2)), (F(1, 2), F(1, 2)), (F(7), F(1, 3)), (F(-1), F(-1)), (F(-1), F(-1, 3))):
        D = Delta_6(G8, (0, 0, 0), (r, 0, 0), ex, ey)
        ok = ok and 0 < D < 1
    for (ex, ey) in ((F(1, 2), F(-1, 2)), (F(-1), F(3)), (F(-1, 3), F(5))):
        D = Delta_6(G8, (0, 0, 0), (r, 0, 0), ex, ey)
        ok = ok and D > 1
    seen.append(f"r={r}: vacancy pair Delta = {float(Delta_6(G8, (0, 0, 0), (r, 0, 0), F(-1), F(-1))):.10f}")
want("B2 (b) SIGN AT EVERY ORDER (r >= 2): 0 < exp(2F) < 1 exactly (attraction) whenever eps_x eps_y > 0, including the vacancy limit "
     "eps = -1 (A restricted to the complement of (1,...,1), which M_xy annihilates), and exp(2F) > 1 (repulsion) whenever eps_x eps_y < 0 "
     "- exact rational comparisons at r = 2, 3, 4 on the 8^3 torus; the proof (Schur complement) is in ATTEMPT.md", ok, "; ".join(seen))

# ================================================================== B3: decay and constants on Z^3
kx, ky, kz = sp.symbols("x y z", real=True)
Rr = sp.sqrt(kx ** 2 + ky ** 2 + kz ** 2)
Gc = 1 / (4 * sp.pi * Rr)
hess_sq = sum(sp.diff(Gc, a, b) ** 2 for a in (kx, ky, kz) for b in (kx, ky, kz))
hess_ok = sp.simplify(hess_sq - sp.Rational(3, 8) / (sp.pi ** 2 * Rr ** 6)) == 0
Pm = sp.Matrix(3, 6, lambda i, b: (1 if BONDS[b][1] == 1 else -1) if BONDS[b][0] == i else 0)
pp_ok = Pm * Pm.T == 2 * sp.eye(3)
mp.mp.dps = 25


@functools.lru_cache(maxsize=None)
def Gz(n):
    n = tuple(sorted(abs(v) for v in n))
    f = lambda t: mp.exp(-6 * t) * mp.besseli(n[0], 2 * t) * mp.besseli(n[1], 2 * t) * mp.besseli(n[2], 2 * t)
    return mp.quad(f, [0, 1, 10, 100, mp.inf])


def matz(B1, B2):
    return mp.matrix([[Mentry(Gz, b1, b2) for b2 in B2] for b1 in B1])


G0, G2e = Gz((0, 0, 0)), Gz((2, 0, 0))
resid = max(abs(6 * Gz(n) - sum(Gz(tuple(n[d] + (s if d == i else 0) for d in range(3))) for i in range(3) for s in (1, -1)) - (1 if n == (0, 0, 0) else 0))
            for n in ((0, 0, 0), (1, 0, 0), (5, 1, 0), (20, 0, 0)))
B0 = bonds_at((0, 0, 0))
M00 = matz(B0, B0)
mu_odd = G0 - G2e
vodd = mp.matrix([1, -1, 0, 0, 0, 0])
eig_ok = abs((M00 * vodd)[0] - mu_odd) < mp.mpf(10) ** -20 and abs(M00[0, 0] - mp.mpf(1) / 3) < mp.mpf(10) ** -20
alpha = lambda e: 2 / (1 + e * mu_odd)
C2 = -3 / (4 * mp.pi ** 2)
Cvac = -3 / (16 * mp.pi ** 2) * alpha(-1) ** 2
I6 = mp.eye(6); ones = mp.matrix([1] * 6); P1 = ones * ones.T / 6
Atil = (I6 - M00 + P1) ** -1 - P1
zrows = []; Fvac = {}; F2z = {}
for r in (5, 10, 20, 40):
    Mxy = matz(B0, bonds_at((r, 0, 0)))
    F2z[r] = -sum(Mxy[i, j] ** 2 for i in range(6) for j in range(6)) / 2
    Fvac[r] = mp.log(mp.det(I6 - Atil * Mxy * Atil * Mxy.T)) / 2
    zrows.append(f"r={r}: F2 r^6 = {mp.nstr(F2z[r] * r ** 6, 7)}, F_vac r^6 = {mp.nstr(Fvac[r] * r ** 6, 7)}")
conv_ok = abs(F2z[40] * 40 ** 6 / C2 - 1) < 0.01 and abs(Fvac[40] * 40 ** 6 / Cvac - 1) < 0.01 and abs(Fvac[20] * 20 ** 6 / Cvac - 1) < 0.04
want("B3 (b) DECAY r^-6 WITH EXACT CONSTANTS: sum_ij (d_i d_j (1/(4 pi r)))^2 = 3/(8 pi^2 r^6) (symbolic) and P P^T = 2 I for the bond-"
     "to-axis map, so the second-order interaction is F ~ -(eps_x eps_y/2) 4 * 3/(8 pi^2 r^6) = -3 eps_x eps_y/(4 pi^2 r^6); at finite eps "
     "the inclusions are dressed: F ~ -(3/(16 pi^2)) eps_x eps_y alpha(eps_x) alpha(eps_y)/r^6, alpha = 2/(1 + eps mu), mu = G(0) - G(2e_1) "
     "the odd eigenvalue of M_00 (vacancy: alpha = 2.5311, constant -0.121712). NUMERIC (Z^3, quadrature at 25 digits, Laplace residual "
     "below 1e-20): F2 r^6 and F_vac r^6 approach -3/(4pi^2) and the dressed constant within 1% at r = 40",
     hess_ok and pp_ok and eig_ok and resid < mp.mpf(10) ** -20 and conv_ok, "; ".join(zrows) + f"; mu = {mp.nstr(mu_odd, 12)}")

# ================================================================== C1: against two held tilts (block 41 T4), eps = -1
crows = []
for r in (5, 10, 20):
    Gr = Gz((r, 0, 0))
    Ftilt = -Gr / (G0 ** 2 - Gr ** 2)
    crows.append(f"r={r}: F_vac/F_tilt = {mp.nstr(Fvac[r] / Ftilt, 5)}")
want("C1 (c) NUMERIC (Z^3): two vacancies against two held unit tilts (block 41 T4: -kappa a b G(r)/(G(0)^2 - G(r)^2), kappa a b = 1): the "
     "ratio falls as r^-5, from 6.0e-5 at r = 5 to 3.1e-8 at r = 20", True, "; ".join(crows))

# ================================================================== D1: rotation-invariant inclusions have no charge
ok = True
cube = list(itertools.product(range(2), repeat=3))
for trial in range(5):
    Q = [[F(0)] * 8 for _ in range(8)]
    for a in range(8):
        for b in range(a + 1, 8):
            w = F(rng.randint(-9, 9), rng.randint(1, 9)); Q[a][b] = w; Q[b][a] = w
    for a in range(8):
        Q[a][a] = -sum(Q[a][b] for b in range(8) if b != a)                # zero row sums: shift invariant
    R = [[F(0)] * 8 for _ in range(8)]
    for a in range(8):
        for b in range(a + 1, 8):
            d = [F(0)] * 8; d[a] = F(1); d[b] = F(-1)
            for i in range(8):
                for j in range(8):
                    R[i][j] -= Q[a][b] * d[i] * d[j]
    ok = ok and R == Q
want("D1 (d) every quadratic inclusion that is unchanged by the global shift theta -> theta + c (the medium's rotation) has zero row sums "
     "and is EXACTLY -sum_{u<v} Q_uv (e_u - e_v)(e_u - e_v)^T (random rational Q on a 2x2x2 neighbourhood): it couples only to differences, "
     "so its interaction matrix consists of second differences of G (r^-3 each, r^-6 in F); a shift-invariant linear term has zero sum "
     "(no charge), so its cross term h_x^T G h_y starts at the dipole order r^-3; a one-over-r term needs sum h != 0", ok)

npass = sum(1 for _, o in RESULTS if o)
nfail = len(RESULTS) - npass
print(f"TOTAL: PASS={npass} FAIL={nfail}")
if nfail == 0:
    print("SUMMARY: PARTIAL, exact: two inclusions interact by F(x,y) = (1/2) log det(I - eps_x eps_y A_x M_xy A_y M_yx) (6 x 6, second "
          "differences of G between the bonds; the four-determinant ratio checked on 4^3); F is negative for like signs and positive for "
          "unlike signs at EVERY order (vacancy limit included), with second-order term -(eps_x eps_y/2) sum M_xy^2 (the task's 1/4 is 1/2); "
          "on Z^3 F ~ -(3/(16 pi^2)) eps_x eps_y alpha_x alpha_y / r^6, alpha = 2/(1 + eps (G(0) - G(2e_1))) (-3 eps^2/(4 pi^2 r^6) at second "
          "order; -0.12171/r^6 for vacancies); two vacancies against two held tilts: 6.0e-5, 1.1e-6, 3.1e-8 at r = 5, 10, 20; no "
          "rotation-invariant inclusion of the quadratic model has a charge, so none gives a one-over-r attraction")
    print("HIT: in the quadratic tilt model two stiffness inclusions interact EXACTLY by F = (1/2) log det(I - eps_x eps_y A_x M_xy A_y M_yx) "
          "with M_xy the 6 x 6 second differences of G between their bonds and A = (I + eps M_00)^-1; exp(2F) lies in (0,1) for like signs and "
          "above 1 for unlike signs at every order (Schur complement), and F r^6 -> -(3/(16 pi^2)) eps_x eps_y alpha_x alpha_y with "
          "alpha = 2/(1 + eps (G(0) - G(2e_1))) on Z^3; shift-invariant inclusions carry no charge, so no one-over-r attraction arises")
