"""2D sector Sigma2 = {h_xx,h_yy,h_zz (sites), h_xy (faces)}; fields depend on (x,y); lapses N,M on sites (x,y)."""
import itertools
from fractions import Fraction as F
from engine2 import *

K = F(1)
ALPHA = F(1)
CC = F(1, 2)
XX, YY, ZZ, XY = 0, 1, 2, 3
SITE = (XX, YY, ZZ)


def pos(c, i, j):
    """Doubled-coordinate position of component c anchored at lattice cell (i,j) (face XY: lower-left corner (i,j))."""
    return (2 * i + 1, 2 * j + 1) if c == XY else (2 * i, 2 * j)


def hv(c, i, j):
    return ('h', c, pos(c, i, j))


def Pv(c, i, j):
    return ('P', c, pos(c, i, j))


def Lv(L, i, j):
    return (L, 0, (2 * i, 2 * j))


def madd(d, vs, coef):
    add(d, tuple(vs), coef)


def lap_terms(L, i, j, dx, dy):
    """second difference of lapse: list of (variable, coef): Delta_x if dx else Delta_y at site (i,j)."""
    if dx:
        return [(Lv(L, i + 1, j), 1), (Lv(L, i, j), -2), (Lv(L, i - 1, j), 1)]
    return [(Lv(L, i, j + 1), 1), (Lv(L, i, j), -2), (Lv(L, i, j - 1), 1)]


def C1(L, k=K):
    out = {}
    # h_xx * (-Delta_y L), h_yy * (-Delta_x L), h_zz * (-(Delta_x+Delta_y) L) at site (0,0)
    for (c, dxs) in ((XX, (0,)), (YY, (1,)), (ZZ, (0, 1))):
        for dxflag in dxs:
            for var, cf in lap_terms(L, 0, 0, bool(dxflag), not bool(dxflag)):
                madd(out, [var, hv(c, 0, 0)], -k * cf)
    # faces: h_xy(0,0) * 2 * mixed[L](0,0)
    for (di, dj, cf) in ((0, 0, 1), (1, 0, -1), (0, 1, -1), (1, 1, 1)):
        madd(out, [Lv(L, di, dj), hv(XY, 0, 0)], 2 * k * cf)
    return out


def T2(L, alpha=ALPHA, c=CC):
    out = {}
    pre = 1 / (4 * alpha)
    for a in SITE:
        madd(out, [Lv(L, 0, 0), Pv(a, 0, 0), Pv(a, 0, 0)], pre * (1 - c))
    for a, b in itertools.combinations(SITE, 2):
        madd(out, [Lv(L, 0, 0), Pv(a, 0, 0), Pv(b, 0, 0)], pre * (-2 * c))
    # face term: mean4(L)(y) P_xy(y)^2 / (8 alpha)
    for (di, dj) in ((0, 0), (1, 0), (0, 1), (1, 1)):
        madd(out, [Lv(L, di, dj), Pv(XY, 0, 0), Pv(XY, 0, 0)], F(1, 4) / (8 * alpha))
    return out


def R2_2D():
    """Real-space quadratic form of the b62 symbol R2 (p = (p_x,p_y,0)); returned as class-sum functional."""
    out = {}
    # (a) -1/4 sum_l sum_comp c_comp (D_l h_comp)^2, c = 1 (diag), 2 (xy)
    for c, cc in ((XX, 1), (YY, 1), (ZZ, 1), (XY, 2)):
        for (di, dj) in ((1, 0), (0, 1)):
            # (h(i+di,j+dj) - h(i,j))^2
            madd(out, [hv(c, di, dj), hv(c, di, dj)], -F(1, 4) * cc)
            madd(out, [hv(c, 0, 0), hv(c, 0, 0)], -F(1, 4) * cc)
            madd(out, [hv(c, di, dj), hv(c, 0, 0)], F(2, 4) * cc)
    # (b) 1/2 sum over x-bonds (hp)_x^2 + y-bonds (hp)_y^2
    # (hp)_x(x+1/2,y) = h_xx(x+1,y) - h_xx(x,y) + h_xy(x,y) - h_xy(x,y-1)
    terms_x = [(hv(XX, 1, 0), 1), (hv(XX, 0, 0), -1), (hv(XY, 0, 0), 1), (hv(XY, 0, -1), -1)]
    # (hp)_y(x,y+1/2) = h_xy(x,y) - h_xy(x-1,y) + h_yy(x,y+1) - h_yy(x,y)
    terms_y = [(hv(XY, 0, 0), 1), (hv(XY, -1, 0), -1), (hv(YY, 0, 1), 1), (hv(YY, 0, 0), -1)]
    for terms in (terms_x, terms_y):
        for (v1, c1), (v2, c2) in itertools.product(terms, terms):
            madd(out, [v1, v2], F(1, 2) * c1 * c2)
    # (c) -1/2 * (p^T h p)(x) * trh(x),  (p^T h p)(x) = -Delta_x h_xx - Delta_y h_yy - 2 B(x),
    #     B(x) = h_xy(x) - h_xy(x-e_x) - h_xy(x-e_y) + h_xy(x-e_x-e_y)
    pthp = []
    for var, cf in lap_terms('h', 0, 0, True, False):
        pass
    def hsite(c, i, j):
        return hv(c, i, j)
    pth = [(hsite(XX, 1, 0), -1), (hsite(XX, 0, 0), 2), (hsite(XX, -1, 0), -1),
           (hsite(YY, 0, 1), -1), (hsite(YY, 0, 0), 2), (hsite(YY, 0, -1), -1),
           (hv(XY, 0, 0), -2), (hv(XY, -1, 0), 2), (hv(XY, 0, -1), 2), (hv(XY, -1, -1), -2)]
    tr = [(hsite(XX, 0, 0), 1), (hsite(YY, 0, 0), 1), (hsite(ZZ, 0, 0), 1)]
    for (v1, c1), (v2, c2) in itertools.product(pth, tr):
        madd(out, [v1, v2], -F(1, 2) * c1 * c2)
    # (d) 1/4 sum_l (D_l trh)^2
    for (di, dj) in ((1, 0), (0, 1)):
        d = [(hsite(c, di, dj), 1) for c in SITE] + [(hsite(c, 0, 0), -1) for c in SITE]
        for (v1, c1), (v2, c2) in itertools.product(d, d):
            madd(out, [v1, v2], F(1, 4) * c1 * c2)
    return out


def G1_of_xi(xi_x, xi_y):
    """xi_x: dict of raw monomials for the x-bond from site (0,0); xi_y for the y-bond from (0,0). Returns G1 functional."""
    out = {}
    for m, c in xi_x.items():
        add(out, m + (Pv(XX, 0, 0),), 2 * c)
        add(out, m + (Pv(XX, 1, 0),), -2 * c)
        add(out, m + (Pv(XY, 0, -1),), c)
        add(out, m + (Pv(XY, 0, 0),), -c)
    for m, c in xi_y.items():
        add(out, m + (Pv(YY, 0, 0),), 2 * c)
        add(out, m + (Pv(YY, 0, 1),), -2 * c)
        add(out, m + (Pv(XY, -1, 0),), c)
        add(out, m + (Pv(XY, 0, 0),), -c)
    return out


def xi0_xy(k=K, alpha=ALPHA):
    xx, yy = {}, {}
    raw_add(xx, [Lv('N', 1, 0), Lv('M', 0, 0)], k / (4 * alpha))
    raw_add(xx, [Lv('N', 0, 0), Lv('M', 1, 0)], -k / (4 * alpha))
    raw_add(yy, [Lv('N', 0, 1), Lv('M', 0, 0)], k / (4 * alpha))
    raw_add(yy, [Lv('N', 0, 0), Lv('M', 0, 1)], -k / (4 * alpha))
    return xx, yy


def A_of_xi(xi):
    """Linear gauge variation delta_xi h on sample fields: xi = dict {('x'|'y',i,j): value}. Returns dict {(c,i,j): value}."""
    out = {}
    def g(j, i0, j0):
        return xi.get((j, i0, j0), 0)
    cells = set()
    for (dirn, i, j) in xi:
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                cells.add((i + di, j + dj))
    for (i, j) in cells:
        out[(XX, i, j)] = 2 * (g('x', i, j) - g('x', i - 1, j))
        out[(YY, i, j)] = 2 * (g('y', i, j) - g('y', i, j - 1))
        out[(ZZ, i, j)] = 0
        out[(XY, i, j)] = g('y', i + 1, j) - g('y', i, j) + g('x', i, j + 1) - g('x', i, j)
    return out


def eval_functional(fun, field):
    """Evaluate a quadratic/linear functional in h only (class-sum over translations) on a periodic field {(c,i,j): value}, torus Lx*Ly."""
    raise NotImplementedError
