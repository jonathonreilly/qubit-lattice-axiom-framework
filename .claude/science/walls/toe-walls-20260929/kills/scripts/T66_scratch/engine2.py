"""2D version of the engine. Positions are pairs (px,py) in DOUBLED coordinates (unit lattice step = 2);
site-type components live on (even,even), the xy face component on (odd,odd). Translations are by EVEN vectors only."""
from fractions import Fraction as F
from collections import defaultdict

CONJ = {'h': 'P', 'P': 'h'}


def canon(mono):
    if not mono:
        return ()
    mx = min(v[2][0] for v in mono)
    my = min(v[2][1] for v in mono)
    sx = mx - (mx % 2)
    sy = my - (my % 2)
    return tuple(sorted((k, c, (p[0] - sx, p[1] - sy)) for (k, c, p) in mono))


def shift(mono, u):
    return tuple(sorted((k, c, (p[0] + u[0], p[1] + u[1])) for (k, c, p) in mono))


def add(d, mono, coef):
    if coef == 0:
        return
    key = canon(mono)
    d[key] = d.get(key, F(0)) + coef
    if d[key] == 0:
        del d[key]


def raw_add(d, vs, coef):
    key = tuple(sorted(vs))
    d[key] = d.get(key, F(0)) + coef
    if d[key] == 0:
        del d[key]


def fadd(A, B, s=F(1)):
    out = dict(A)
    for k, v in B.items():
        out[k] = out.get(k, F(0)) + s * v
        if out[k] == 0:
            del out[k]
    return out


def fscale(A, s):
    return {k: v * s for k, v in A.items()} if s != 0 else {}


def _mult(v, mono):
    return sum(1 for w in mono if w == v)


def _remove_one(mono, v):
    l = list(mono)
    l.remove(v)
    return tuple(l)


def bracket_mono(f, g):
    out = defaultdict(F)
    fv = set(v for v in f if v[0] in 'hP')
    for v in fv:
        cv = (CONJ[v[0]], v[1], v[2])
        mg = _mult(cv, g)
        if mg == 0:
            continue
        mf = _mult(v, f)
        sign = 1 if v[0] == 'h' else -1
        rest = tuple(sorted(_remove_one(f, v) + _remove_one(g, cv)))
        out[rest] += sign * mf * mg
    return out


def bracket(A, B):
    out = {}
    for f, cf in A.items():
        for g, cg in B.items():
            us = set()
            for a in f:
                if a[0] in 'hP':
                    for b in g:
                        if b[0] == CONJ[a[0]] and b[1] == a[1]:
                            us.add((a[2][0] - b[2][0], a[2][1] - b[2][1]))
            for u in us:
                gs = shift(g, u)
                for mono, c in bracket_mono(f, gs).items():
                    add(out, mono, cf * cg * c)
    return out


def restrict_uniform_M(A):
    out = {}
    for mono, c in A.items():
        add(out, tuple(v for v in mono if v[0] != 'M'), c)
    return out


def substitute_uniform(A, lapse):
    out = {}
    for mono, c in A.items():
        add(out, tuple(v for v in mono if v[0] != lapse), c)
    return out
