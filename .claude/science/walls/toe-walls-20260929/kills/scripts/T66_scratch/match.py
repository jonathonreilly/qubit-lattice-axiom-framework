"""Continuum-limit (ADM frame) matching rows for the lattice unknowns.

Symbol of a class-sum monomial with variables (label, position p_j): homogeneous degree-D part on the hyperplane sum k_j = 0
is (sum_j k_j p_j)^D / D!  (common factor i^D dropped), symmetrised over slots carrying the same label.
Continuum term c * prod d^{n_j} f_j has symbol c * prod k_j^{n_j} (same i^D dropped), symmetrised likewise.
"""
import itertools, random
import sympy as sp
from fractions import Fraction as F
from math import factorial
from collections import defaultdict


def sym_lattice(slots, ks, D):
    """slots: list of (label, pos Fraction); ks: list of Fractions (same length, sum 0). Average over perms of identical labels."""
    groups = defaultdict(list)
    for i, (lab, p) in enumerate(slots):
        groups[lab].append(i)
    # permutations within each group
    perms_per_group = [list(itertools.permutations(idx)) for idx in groups.values()]
    idx_groups = list(groups.values())
    total = F(0)
    count = 0
    for combo in itertools.product(*perms_per_group):
        assign = [None] * len(slots)
        for g, perm in zip(idx_groups, combo):
            for slot_i, k_i in zip(g, perm):
                assign[slot_i] = ks[k_i]
        s = sum(assign[i] * slots[i][1] for i in range(len(slots)))
        total += s ** D / factorial(D)
        count += 1
    return total / count


def sym_cont(coef, slots, ks):
    """slots: list of (label, n_derivs)."""
    groups = defaultdict(list)
    for i, (lab, n) in enumerate(slots):
        groups[lab].append(i)
    perms_per_group = [list(itertools.permutations(idx)) for idx in groups.values()]
    idx_groups = list(groups.values())
    total = F(0)
    count = 0
    for combo in itertools.product(*perms_per_group):
        assign = [None] * len(slots)
        for g, perm in zip(idx_groups, combo):
            for slot_i, k_i in zip(g, perm):
                assign[slot_i] = ks[k_i]
        v = F(1)
        for i in range(len(slots)):
            v *= assign[i] ** slots[i][1]
        total += v
        count += 1
    return coef * total / count


def hyperplane_points(m, npts, seed=0, lo=-6, hi=6):
    rnd = random.Random(seed)
    pts = []
    while len(pts) < npts:
        ks = [rnd.randint(lo, hi) for _ in range(m - 1)]
        pts.append([F(k) for k in ks] + [F(-sum(ks))])
    return pts


def sympy_terms(expr, fmap):
    """Expand a sympy polynomial-in-jets expression to a list of (coef Fraction, slots[(label,nderiv)])."""
    x = sp.Symbol('x', positive=True)
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
            if exp.is_Integer and exp >= 1 and not base.is_Symbol and not fac.is_number:
                pass
            reps = int(exp) if exp.is_Integer else 1
            if isinstance(base, sp.Derivative):
                f = base.expr
                n = base.derivative_count
            else:
                f = base
                n = 0
            if f in fmap:
                for _ in range(reps):
                    slots.append((fmap[f], n))
            elif base.is_Symbol:
                # a numeric symbol such as K or a: caller must have substituted
                raise ValueError("unsubstituted symbol " + str(base))
            else:
                raise ValueError("unknown factor " + str(fac))
        out.append((coef, slots))
    return out
