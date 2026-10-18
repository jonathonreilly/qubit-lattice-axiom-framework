#!/usr/bin/env python3
r"""C9 fresh-context check, part (a)/L3: gap form of the arc lemma.

Different route from C9's H2 (an 8-point Lam_2 grid): exact lex-Groebner ELIMINATION of every
structure constant except the Lam_n, n in S \ {0,+-1}, giving the full projection of the variety,
compared with the set predicted by the gap-arc lemma (partitions of S \ {0,+-1} into runs of
consecutive momenta inside {2..L-2}; Lam_n/Lam_1 = n - centre).  New code.
Normalisation Lam_1 = 1 (rescaling c is a symmetry); (S) via t*c(1,-1) = 1.  No (Z).
"""
import sys, time, itertools
import sympy as sp

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += ok; FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}"); sys.stdout.flush()

def arc_partitions(seq):
    """all partitions of the sorted integer list seq into runs of consecutive integers"""
    if not seq:
        yield []
        return
    for k in range(1, len(seq) + 1):
        head = seq[:k]
        if any(head[i + 1] != head[i] + 1 for i in range(k - 1)):
            break
        for rest in arc_partitions(seq[k:]):
            yield [head] + rest

def predicted(L, S):
    rest = sorted(n for n in S if n not in (0, 1, L - 1))
    out = set()
    for part in arc_partitions(rest):
        lam = {}
        for arc in part:
            centre = sp.Rational(arc[0] + arc[-1], 2)
            for n in arc:
                lam[n] = sp.Rational(n) - centre
        out.add(tuple(lam[n] for n in rest))
    return rest, out

def variety_projection(L, S):
    S = sorted(S)
    Sset = set(S)
    var = {}
    def c(a, b):
        a %= L; b %= L
        if a == b or (a + b) % L not in Sset or a not in Sset or b not in Sset:
            return 0
        if a < b:
            if (a, b) not in var:
                var[(a, b)] = sp.Symbol(f"c_{a}_{b}")
            return var[(a, b)]
        return -c(b, a)
    eqs = []
    for a, b, cc in itertools.combinations(S, 3):
        eqs.append(sp.expand(c(a, b) * c(a + b, cc) + c(b, cc) * c(b + cc, a) + c(cc, a) * c(cc + a, b)))
    # triples with repeats: (a,a,b) cyclic sums vanish identically by antisymmetry? keep them anyway
    for a, b in itertools.permutations(S, 2):
        eqs.append(sp.expand(c(a, a) * c(2 * a, b) + c(a, b) * c(a + b, a) + c(b, a) * c(a + b, a)))
    t = sp.Symbol("t")
    eqs.append(c(0, 1) - 1)
    eqs.append(t * c(1, L - 1) - 1)
    eqs = [e for e in eqs if e != 0]
    rest = sorted(n for n in S if n not in (0, 1, L - 1))
    lams = [c(0, n) for n in rest]
    others = [v for v in var.values() if v not in lams] + [t]
    G = sp.groebner(eqs, *others, *lams, order="lex")
    if list(G.exprs) == [1]:
        return rest, set(), G
    elim = [g for g in G.exprs if not (g.free_symbols & set(others))]
    sols = sp.solve(elim, lams, dict=True)
    pts = set()
    for s in sols:
        if all(l in s for l in lams):
            pts.add(tuple(sp.nsimplify(s[l]) for l in lams))
        else:
            pts.add(("positive-dimensional",))
    return rest, pts, G

if __name__ == "__main__":
    cases = [(6, [0, 1, 2, 4, 5]), (7, [0, 1, 2, 4, 5, 6]), (7, [0, 1, 2, 3, 5, 6]),
             (8, [0, 1, 2, 3, 5, 6, 7]), (7, [0, 1, 2, 3, 4, 5, 6]), (8, [0, 1, 2, 4, 5, 7]),
             (9, [0, 1, 2, 3, 6, 7, 8])]
    for L, S in cases:
        t0 = time.time()
        rest, pts, G = variety_projection(L, S)
        rest2, pred = predicted(L, S)
        ok = pts == pred
        check(f"gap_projection_L{L}_S{''.join(map(str, S))}", ok,
              f"projection to (Lam_n, n in {rest}) = {sorted(pts)}; gap-arc prediction {sorted(pred)} ({time.time()-t0:.1f}s)")
        lam2 = sorted({p[0] for p in pred}) if rest and rest[0] == 2 else None
        if lam2 is not None:
            check(f"gap_lam2_nonpos_L{L}_S{''.join(map(str, S))}", all(x <= 0 for x in lam2), f"Lam_2/Lam_1 in {lam2}")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
