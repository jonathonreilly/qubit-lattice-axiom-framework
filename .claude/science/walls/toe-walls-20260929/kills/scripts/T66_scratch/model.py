"""Planar sector S1 = {h_xx,h_yy,h_zz}: pieces of the constraint algebra and the unknown families of test A1."""
import itertools
from fractions import Fraction as F
from engine import *

K = F(1)
ALPHA = F(1)
CC = F(1, 2)  # c = beta/(alpha+3beta); beta=-alpha  <=> c=1/2
XX, YY, ZZ = 0, 1, 2
COMPS = (XX, YY, ZZ)


def V(kind, c, p):
    return (kind, c, p)


def mono_add(d, vs, coef):
    add(d, tuple(sorted(vs)), coef)


def raw_add(d, vs, coef):
    """Add WITHOUT translating to canonical position (bond/site-anchored densities)."""
    key = tuple(sorted(vs))
    d[key] = d.get(key, F(0)) + coef
    if d[key] == 0:
        del d[key]


def C1(L, k=K):
    """C1[L] = k * sum_n (-Delta_x L)(n) (h_yy + h_zz)(n)."""
    out = {}
    for c in (YY, ZZ):
        mono_add(out, [V(L, 0, 1), V('h', c, 0)], -k)
        mono_add(out, [V(L, 0, 0), V('h', c, 0)], 2 * k)
        mono_add(out, [V(L, 0, -1), V('h', c, 0)], -k)
    return out


def T2(L, alpha=ALPHA, c=CC):
    out = {}
    pre = 1 / (4 * alpha)
    for a in COMPS:
        mono_add(out, [V(L, 0, 0), V('P', a, 0), V('P', a, 0)], pre * (1 - c))
    for a, b in itertools.combinations(COMPS, 2):
        mono_add(out, [V(L, 0, 0), V('P', a, 0), V('P', b, 0)], pre * (-2 * c))
    return out


def R2_S1():
    out = {}
    mono_add(out, [V('h', YY, 0), V('h', ZZ, 0)], F(1))
    mono_add(out, [V('h', YY, 1), V('h', ZZ, 0)], F(-1, 2))
    mono_add(out, [V('h', YY, 0), V('h', ZZ, 1)], F(-1, 2))
    return out


def G1_of_xi(xi_monos):
    """G1[xi] = sum_n 2 P_xx(n) (xi(n) - xi(n-1)); xi_monos = {mono: coef} for the bond between sites 0 and 1."""
    out = {}
    for m, c in xi_monos.items():
        add(out, m + (V('P', XX, 0),), 2 * c)
        add(out, m + (V('P', XX, 1),), -2 * c)
    return out


def xi0(k=K, alpha=ALPHA):
    out = {}
    raw_add(out, [V('N', 0, 1), V('M', 0, 0)], k / (4 * alpha))
    raw_add(out, [V('N', 0, 0), V('M', 0, 1)], -k / (4 * alpha))
    return out


def fmul_mono(xi_monos, extra):
    """xi(bond0) * extra-variable-tuple."""
    out = {}
    for m, c in xi_monos.items():
        add(out, m + tuple(extra), c)
    return out


def spread_ok(positions, R):
    return max(positions) - min(positions) <= R


# ------------------------------------------------------------------ unknown families
def enum_V2(R):
    hv = [V('h', c, p) for c in COMPS for p in range(R + 1)]
    lv = [p for p in range(R + 1)]
    res = []
    for pair in itertools.combinations_with_replacement(hv, 2):
        for lp in lv:
            vs = [pair[0], pair[1], V('N', 0, lp)]
            if min(v[2] for v in vs) == 0:
                res.append(tuple(sorted(vs)))
    return sorted(set(res))


def enum_T3(R):
    hv = [V('h', c, p) for c in COMPS for p in range(R + 1)]
    Pv = [V('P', c, p) for c in COMPS for p in range(R + 1)]
    res = []
    for pp in itertools.combinations_with_replacement(Pv, 2):
        for h in hv:
            for lp in range(R + 1):
                vs = [pp[0], pp[1], h, V('N', 0, lp)]
                if min(v[2] for v in vs) == 0:
                    res.append(tuple(sorted(vs)))
    return sorted(set(res))


def enum_G2(R):
    """G2 unknowns: xi(bond 0) * P_c(i) h_d(j) with spread of {0,1,i,j} <= R."""
    res = []
    rng = range(-R, R + 2)
    for c in COMPS:
        for d in COMPS:
            for i in rng:
                for j in rng:
                    if spread_ok([0, 1, i, j], R):
                        res.append((c, d, i, j))
    return res


def enum_xi1(R):
    """xi1 unknowns: [N(a)M(b) - N(b)M(a)] h_e(k), a<b, spread of {0,1,a,b,k} <= R."""
    res = []
    rng = range(-R, R + 2)
    for a in rng:
        for b in rng:
            if a >= b:
                continue
            for e in COMPS:
                for k in rng:
                    if spread_ok([0, 1, a, b, k], R):
                        res.append((a, b, e, k))
    return res


def enum_chi(R):
    """chi unknowns: [N(a)M(b) - N(b)M(a)] P_e(k), a<b, spread of {0,a,b,k} <= R."""
    res = []
    rng = range(-R, R + 1)
    for a in rng:
        for b in rng:
            if a >= b:
                continue
            for e in COMPS:
                for k in rng:
                    if spread_ok([0, a, b, k], R):
                        res.append((a, b, e, k))
    return res


def V2_of(mono, L):
    """A V2 unknown monomial (built with kind 'N') as functional with lapse kind L."""
    return {tuple(sorted((L if v[0] == 'N' else v[0], v[1], v[2]) for v in mono)): F(1)}


def T3_of(mono, L):
    return V2_of(mono, L)


def col_V2(mono, alpha=ALPHA, c=CC):
    vm = V2_of(mono, 'M')
    vn = V2_of(mono, 'N')
    return fadd(bracket(T2('N', alpha, c), vm), bracket(vn, T2('M', alpha, c)))


def col_T3(mono, k=K):
    tm = T3_of(mono, 'M')
    tn = T3_of(mono, 'N')
    return fadd(bracket(C1('N', k), tm), bracket(tn, C1('M', k)))


def col_G2(u, k=K, alpha=ALPHA):
    c, d, i, j = u
    return fmul_mono(xi0(k, alpha), [V('P', c, i), V('h', d, j)])


def xi1_monos(u):
    a, b, e, k = u
    out = {}
    raw_add(out, [V('N', 0, a), V('M', 0, b), V('h', e, k)], F(1))
    raw_add(out, [V('N', 0, b), V('M', 0, a), V('h', e, k)], F(-1))
    return out


def col_xi1(u):
    return G1_of_xi(xi1_monos(u))


def chi_monos(u):
    a, b, e, k = u
    out = {}
    raw_add(out, [V('N', 0, a), V('M', 0, b), V('P', e, k)], F(1))
    raw_add(out, [V('N', 0, b), V('M', 0, a), V('P', e, k)], F(-1))
    return out


def col_chi(u, k=K):
    """C1[chi] = k sum_n (-Delta_x chi)(n) (h_yy+h_zz)(n)."""
    out = {}
    for m, cf in chi_monos(u).items():
        for c in (YY, ZZ):
            add(out, shift(m, 1) + (V('h', c, 0),), -k * cf)
            add(out, m + (V('h', c, 0),), 2 * k * cf)
            add(out, shift(m, -1) + (V('h', c, 0),), -k * cf)
    return out
