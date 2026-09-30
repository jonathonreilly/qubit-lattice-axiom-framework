"""Dihedral group D4 of the xy plane acting on functionals of the 2D sector."""
import itertools
from fractions import Fraction as F
from engine2 import canon, add

GROUP = []
for swap in (False, True):
    for s1 in (1, -1):
        for s2 in (1, -1):
            GROUP.append((swap, s1, s2))     # 8 elements


def act_var(g, v):
    swap, s1, s2 = g
    kind, comp, p = v
    px, py = p
    # new position
    if not swap:
        np_ = (s1 * px, s2 * py)
    else:
        np_ = (s2 * py, s1 * px)          # p'_{sigma(0)=1} = s1*px  -> y ; p'_{sigma(1)=0} = s2*py -> x
    sign = 1
    if kind in ('N', 'M'):
        return (kind, comp, np_), 1
    if kind in ('h', 'P'):
        if comp == 0:
            nc = 1 if swap else 0
        elif comp == 1:
            nc = 0 if swap else 1
        elif comp == 2:
            nc = 2
        else:
            nc = 3; sign = s1 * s2
        return (kind, nc, np_), sign
    if kind in ('Xx', 'Xy'):
        # bond variable: comp field unused (0); kind encodes direction
        if kind == 'Xx':
            nk = 'Xy' if swap else 'Xx'; sign = s1
        else:
            nk = 'Xx' if swap else 'Xy'; sign = s2
        return (nk, comp, np_), sign
    raise ValueError(kind)


def act_mono(g, mono):
    sign = 1
    out = []
    for v in mono:
        nv, s = act_var(g, v)
        out.append(nv); sign *= s
    return sign, tuple(sorted(out))


def act_fun(g, fun):
    out = {}
    for mono, c in fun.items():
        s, m = act_mono(g, mono)
        add(out, m, s * c)
    return out


def symmetrize(fun):
    out = {}
    for g in GROUP:
        for mono, c in act_fun(g, fun).items():
            out[mono] = out.get(mono, F(0)) + c / len(GROUP)
    return {k: v for k, v in out.items() if v != 0}
