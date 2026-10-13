"""R19-6 shared machinery (written from scratch; imports nothing from earlier C5 runners).
One plane-wave phase theta = k z - w t.  Fields are A*cos(theta) + B*sin(theta), represented with symbols C, S.
d_t -> -w d/dtheta, d_z -> k d/dtheta.  Phase average: <C^2> = <S^2> = 1/2, <CS> = 0 (and 4th moments, unused at O(2)).
Second-order expansion of the contravariant weight-w Einstein density  Y_w^{mu nu} = (-g)^{w/2} g^{mu a} g^{nu b} G_ab
and of the lower-index weight-0 G_mu nu.  G = c = 1; Einstein eq  G_mu nu = 8 pi T_mu nu.
"""
import sympy as sp

C, S, eps = sp.symbols('C S epsilon')
eta = sp.diag(-1, 1, 1, 1)
N = 4


def make_D(w, k):
    def dth(f):
        f = sp.expand(f)
        return sp.diff(f, C) * (-S) + sp.diff(f, S) * C

    def D(mu, f):
        if mu == 0:
            return -w * dth(f)
        if mu == 3:
            return k * dth(f)
        return sp.Integer(0)
    return D


MOM = {(0, 0): 1, (2, 0): sp.Rational(1, 2), (0, 2): sp.Rational(1, 2), (1, 1): 0,
       (4, 0): sp.Rational(3, 8), (0, 4): sp.Rational(3, 8), (2, 2): sp.Rational(1, 8)}


def avg(e):
    e = sp.expand(e)
    if e == 0:
        return sp.Integer(0)
    p = sp.Poly(e, C, S)
    out = 0
    for (i, j), cf in p.terms():
        if i % 2 == 0 and j % 2 == 0:
            out += cf * MOM[(i, j)]
    return sp.expand(out)


def trunc(e, top=2):
    e = sp.expand(e)
    return sum(e.coeff(eps, p) * eps**p for p in range(1, top + 1))


def einstein_lower(h, D):
    """G_mu nu[eta + eps h] to O(eps^2), lower indices."""
    g = eta + eps * h
    ginv = eta - eps * eta * h * eta + eps**2 * eta * h * eta * h * eta
    dg = [[[D(l, g[m, q]) for l in range(N)] for q in range(N)] for m in range(N)]
    Gam = [[[0] * N for _ in range(N)] for _ in range(N)]
    for al in range(N):
        for m in range(N):
            for q in range(m, N):
                v = sum(ginv[al, b] * (dg[b][m][q] + dg[b][q][m] - dg[m][q][b]) for b in range(N)) / 2
                v = trunc(v)
                Gam[al][m][q] = v
                Gam[al][q][m] = v
    Ric = sp.zeros(N, N)
    for m in range(N):
        for q in range(m, N):
            v = 0
            for al in range(N):
                v += D(al, Gam[al][m][q]) - D(q, Gam[al][m][al])
                for b in range(N):
                    v += Gam[al][al][b] * Gam[b][m][q] - Gam[al][q][b] * Gam[b][m][al]
            v = trunc(v)
            Ric[m, q] = v
            Ric[q, m] = v
    R = trunc(sum(ginv[m, q] * Ric[m, q] for m in range(N) for q in range(N)))
    G = sp.zeros(N, N)
    for m in range(N):
        for q in range(N):
            G[m, q] = trunc(Ric[m, q] - g[m, q] * R / 2)
    return G, ginv


def density_factor(h, w):
    """(-g)^{w/2} to O(eps^2): ln(-g) = eps trM - eps^2 tr(M^2)/2, M = eta h."""
    M = eta * h
    t1 = M.trace()
    t2 = (M * M).trace()
    L = eps * t1 - eps**2 * t2 / 2
    hw = sp.sympify(w) / 2   # exact: avoid int/int floats
    return sp.expand(1 + hw * L + hw**2 * L**2 / 2)


def einstein_upper_density(G, ginv, h, w):
    """Y_w^{mu nu} = (-g)^{w/2} g^{mu a} g^{nu b} G_ab, truncated at O(eps^2)."""
    f = density_factor(h, w)
    Gu = ginv * G * ginv
    return Gu.applyfunc(lambda e: trunc(sp.expand(f * trunc(e))))


def order(e, p):
    return sp.expand(e).coeff(eps, p)
