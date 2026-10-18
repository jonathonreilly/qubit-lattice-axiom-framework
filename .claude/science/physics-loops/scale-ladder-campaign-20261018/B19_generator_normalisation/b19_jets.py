"""B19 minimal 3D jet calculus (written fresh for B19; does not import B14/B16 code).

Jets J(f, alpha) are sympy symbols standing for d^alpha f.  D = total derivative, euler = Euler operator.
A local functional int f vanishes identically (periodic/compact support, f with no field-independent part)
iff its Euler derivative in every phase-space field vanishes.
"""
from __future__ import annotations

import sympy as sp

DIM = 3
JET: dict = {}
KEY: dict = {}


def J(f, alpha=(0, 0, 0)):
    k = (f, tuple(alpha))
    if k not in JET:
        s = sp.Symbol(f + "_" + "".join(map(str, alpha)))
        JET[k] = s
        KEY[s] = k
    return JET[k]


def e_(k):
    return tuple(1 if i == k else 0 for i in range(DIM))


def D(expr, k):
    expr = sp.expand(expr)
    out = 0
    for s in expr.free_symbols:
        if s in KEY:
            f, a = KEY[s]
            b = list(a)
            b[k] += 1
            out += sp.diff(expr, s) * J(f, b)
    return sp.expand(out)


def Dalpha(expr, alpha):
    for k in range(DIM):
        for _ in range(alpha[k]):
            expr = D(expr, k)
    return expr


def euler(expr, field):
    expr = sp.expand(expr)
    out = 0
    for s in list(expr.free_symbols):
        if s in KEY and KEY[s][0] == field:
            a = KEY[s][1]
            out += (-1) ** sum(a) * Dalpha(sp.diff(expr, s), a)
    return sp.expand(out)


def fields_of(expr):
    return {KEY[s][0] for s in sp.expand(expr).free_symbols if s in KEY}


def bracket(f, g, conj):
    """density of {int f, int g}, {q,p}=1, conj = {q: p}."""
    out = 0
    ff, gg = fields_of(f), fields_of(g)
    for q, p in conj.items():
        if (q in ff and p in gg) or (p in ff and q in gg):
            out += euler(f, q) * euler(g, p) - euler(f, p) * euler(g, q)
    return sp.expand(out)


def degree_part(expr, names, d):
    """terms of total degree d in the jets of the fields `names`."""
    expr = sp.expand(expr)
    out = []
    for t in sp.Add.make_args(expr):
        deg = 0
        for b, e in t.as_powers_dict().items():
            if b in KEY and KEY[b][0] in names:
                deg += int(e)
        if deg == d:
            out.append(t)
    return sp.Add(*out)


def functional_zero_eqs(expr, phase_fields):
    """coefficient equations for int expr == 0 (Euler derivative in each phase field vanishes)."""
    eqs = []
    for u in phase_fields:
        e = euler(expr, u)
        if e == 0:
            continue
        jets = [s for s in e.free_symbols if s in KEY]
        eqs += [sp.expand(c) for c in sp.Poly(e, *jets).coeffs()]
    return [q for q in eqs if q != 0]


def is_zero_functional(expr, phase_fields):
    return not functional_zero_eqs(expr, phase_fields)
