"""Sparse polynomial / Poisson-bracket engine for translation-invariant local functionals on a 1D chain.

Variables are tuples (kind, comp, pos): kind in 'h','P' (canonical pair), 'N','M' (lapse parameters, comp 0).
Positions are in units of ONE SITE (integers). Bonds n->n+1 are not variables: xi is always written through N,M.
A functional is a dict {canonical monomial: Fraction} that stands for sum_s tau_s(monomial); a monomial is a sorted
tuple of variables, translated so its minimum position is 0.
"""
from fractions import Fraction as F
from collections import defaultdict

CONJ = {'h': 'P', 'P': 'h'}


def canon(mono):
    if not mono:
        return ()
    m = min(v[2] for v in mono)
    return tuple(sorted((k, c, p - m) for (k, c, p) in mono))


def shift(mono, u):
    return tuple(sorted((k, c, p + u) for (k, c, p) in mono))


def add(d, mono, coef):
    if coef == 0:
        return
    key = canon(mono)
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


def swap_lapse(A):
    sw = {'N': 'M', 'M': 'N'}
    out = {}
    for mono, c in A.items():
        add(out, tuple((sw.get(k, k), cc, p) for (k, cc, p) in mono), c)
    return out


def _mult(v, mono):
    return sum(1 for w in mono if w == v)


def _remove_one(mono, v):
    l = list(mono)
    l.remove(v)
    return tuple(l)


def bracket_mono(f, g):
    """{f, g} for two monomials with g already positioned; returns dict mono->coef (uncanonicalised)."""
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
    """Poisson bracket of two translation-summed functionals."""
    out = {}
    for f, cf in A.items():
        for g, cg in B.items():
            us = set()
            for a in f:
                if a[0] in 'hP':
                    for b in g:
                        if b[0] == CONJ[a[0]] and b[1] == a[1]:
                            us.add(a[2] - b[2])
            for u in us:
                gs = shift(g, u)
                for mono, c in bracket_mono(f, gs).items():
                    add(out, mono, cf * cg * c)
    return out


def substitute_uniform(A, lapse):
    """Set lapse variables to 1 (uniform lapse): drop them."""
    out = {}
    for mono, c in A.items():
        add(out, tuple(v for v in mono if v[0] != lapse), c)
    return out


def restrict_uniform_M(A):
    """Keep bilinear N,M polynomial but set M = 1 (drop M variables), keep N."""
    out = {}
    for mono, c in A.items():
        add(out, tuple(v for v in mono if v[0] != 'M'), c)
    return out
