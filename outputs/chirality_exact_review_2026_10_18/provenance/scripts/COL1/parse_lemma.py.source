"""Exact constraint checker for token predicates (COL-1).

A predicate is a list of constraints (positions, allowed) where positions is a tuple of lattice
points and allowed a set of bit tuples. Pi = AND of its constraints.

P1(x,y): is Pi_x AND Pi_y satisfiable?  (exact backtracking over the involved positions)
P2(g, Pi_y): Pi_y is constant on the one-hot span of register group g, for all other bits:
   every constraint touching g contains all of g, and its allowed set is closed under moving the
   single 1 inside g (when g holds exactly one 1).
"""
import itertools

def shift(pred, d, add):
    return [(tuple(add(p, d) for p in pos), allowed) for pos, allowed in pred]

def satisfiable(constraints):
    """Exact: backtracking with forward checking; picks the constraint with fewest consistent tuples."""
    cons = [(tuple(pos), list(allowed)) for pos, allowed in constraints]
    assign = {}
    def consistent(c):
        pos, allowed = c
        return [t for t in allowed if all(assign.get(p, v) == v for p, v in zip(pos, t))]
    def rec(remaining):
        if not remaining:
            return True
        best, best_opts = None, None
        for k in remaining:
            opts = consistent(cons[k])
            if not opts:
                return False
            if best is None or len(opts) < len(best_opts):
                best, best_opts = k, opts
        rest = [k for k in remaining if k != best]
        pos = cons[best][0]
        for t in best_opts:
            newly = [p for p, v in zip(pos, t) if p not in assign]
            for p, v in zip(pos, t):
                assign[p] = v
            if rec(rest):
                return True
            for p in newly:
                del assign[p]
        return False
    return rec(list(range(len(cons))))

def colour_blind(group, pred):
    """True if pred is invariant under moving a single excitation within `group`."""
    gset = set(group)
    for pos, allowed in pred:
        inter = gset.intersection(pos)
        if not inter:
            continue
        if inter != gset:
            return False
        idx = [pos.index(p) for p in group]
        for t in allowed:
            ones = [t[i] for i in idx]
            if sum(ones) != 1:
                continue
            for j in range(len(group)):
                t2 = list(t)
                for k, i in enumerate(idx):
                    t2[i] = 1 if k == j else 0
                if tuple(t2) not in allowed:
                    return False
    return True

def onehot_or_empty(n):
    return [tuple(1 if k == j else 0 for k in range(n)) for j in range(n)] + [tuple([0] * n)]
