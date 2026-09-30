"""2D continuum-limit matching (ADM frame). Symbols use 2-vectors."""
import itertools, random
from math import factorial
from collections import defaultdict
from fractions import Fraction as F
import sympy as sp


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def sym_lattice2(slots, ks, D):
    groups = defaultdict(list)
    for i, (lab, p) in enumerate(slots):
        groups[lab].append(i)
    idx_groups = list(groups.values())
    perms_per_group = [list(itertools.permutations(idx)) for idx in idx_groups]
    total = F(0); count = 0
    for combo in itertools.product(*perms_per_group):
        assign = [None] * len(slots)
        for g, perm in zip(idx_groups, combo):
            for slot_i, k_i in zip(g, perm):
                assign[slot_i] = ks[k_i]
        sm = sum((dot(assign[i], slots[i][1]) for i in range(len(slots))), F(0))
        total += sm ** D / factorial(D)
        count += 1
    return total / count


def sym_cont2(coef, slots, ks):
    groups = defaultdict(list)
    for i, (lab, n) in enumerate(slots):
        groups[lab].append(i)
    idx_groups = list(groups.values())
    perms_per_group = [list(itertools.permutations(idx)) for idx in idx_groups]
    total = F(0); count = 0
    for combo in itertools.product(*perms_per_group):
        assign = [None] * len(slots)
        for g, perm in zip(idx_groups, combo):
            for slot_i, k_i in zip(g, perm):
                assign[slot_i] = ks[k_i]
        v = F(1)
        for i in range(len(slots)):
            v *= assign[i][0] ** slots[i][1][0] * assign[i][1] ** slots[i][1][1]
        total += v
        count += 1
    return coef * total / count


def hyperplane_points2(m, npts, seed=0, lo=-4, hi=4):
    rnd = random.Random(seed)
    pts = []
    while len(pts) < npts:
        vs = [(F(rnd.randint(lo, hi)), F(rnd.randint(lo, hi))) for _ in range(m - 1)]
        last = (-sum(v[0] for v in vs), -sum(v[1] for v in vs))
        pts.append(vs + [last])
    return pts


def sympy_terms2(expr, fmap, xs, ys):
    out = []
    expr = sp.expand(expr)
    for term in sp.Add.make_args(expr):
        coef = F(1)
        slots = []
        for fac in sp.Mul.make_args(term):
            base, exp = fac.as_base_exp()
            if fac.is_number:
                r = sp.Rational(fac)
                coef *= F(int(r.p), int(r.q))
                continue
            reps = int(exp) if exp.is_Integer else 1
            if isinstance(base, sp.Derivative):
                f = base.expr
                nx = sum(c for v, c in base.variable_count if v == xs)
                ny = sum(c for v, c in base.variable_count if v == ys)
            else:
                f = base; nx = ny = 0
            if f in fmap:
                for _ in range(reps):
                    slots.append((fmap[f], (int(nx), int(ny))))
            else:
                raise ValueError("unknown factor " + str(fac))
        out.append((coef, slots))
    return out
