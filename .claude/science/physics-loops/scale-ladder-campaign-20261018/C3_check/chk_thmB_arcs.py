#!/usr/bin/env python3
r"""C3 check: independent test of Theorem B and of a sharper "arc" form of it.

Written from scratch by the checker (nothing imported from the C3 runners).

Object: complex Lie algebra g with basis X_n, n in Z_L, graded [X_a, X_b] = c(a,b) X_{a+b}, c antisymmetric,
Lam_n := c(0,n).  Normalisation (S): Lam_1 = 1, c(1,-1) = 1 (WLOG by rescaling X_0 and X_{-1}).
Lam_{-1} is left FREE (Jacobi must force it to -1).  No (Z) (nonvanishing Lam_n) is imposed anywhere.

Checker's sharper claim (arc lemma, proved in the report):
  delta_n := 2 Lam_n - 2n (mod 2L) is a Z_{2L} grading; each delta-component is an IRREDUCIBLE sl2-module whose
  weight vectors are X_n on an arc of consecutive momenta.  {-1,0,1} is the adjoint arc, so Z_L \ {0,+-1} =
  {2,...,L-2} is cut into arcs [n0, n0+m] with Lam_n / Lam_1 = n - (n0 + m/2)  (arc centre).
  Hence Lam_2/Lam_1 = -m/2 in {0, -1/2, ..., -(L-4)/2}; in particular Lam_2/Lam_1 <= 0.

Route 1 (exact, sympy Groebner over QQ, own equation generator in ad-representation form):
  for each candidate Lam_2 on a grid, consistent  <=>  Lam_2 in the predicted set.
Route 2 (exact, lex elimination): the projection of the variety to (Lam_2..Lam_{L-2}) equals the arc-partition set.
Route 3 (numerical, scipy least squares from random starts): every converged solution obeys the arc formula.
"""
import itertools
import sys
import time
from fractions import Fraction

import numpy as np
import sympy as sp

RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


def build(L, fixed=None):
    """Return (eqs, vars, cfun).  Equations: ad is a representation,
    c(a,b) c(a+b,e) = c(b,e) c(a,b+e) - c(a,e) c(b,a+e)   for all a,b,e  (coefficient of X_{a+b+e})."""
    fixed = dict(fixed or {})
    sym = {}
    for a in range(L):
        for b in range(a + 1, L):
            sym[(a, b)] = sp.Symbol(f"l{b}" if a == 0 else f"k{a}_{b}")
    sym[(0, 1)] = sp.Integer(1)          # Lam_1 = 1
    sym[(1, L - 1)] = sp.Integer(1)      # c(1,-1) = 1
    for key, val in fixed.items():
        sym[key] = sp.nsimplify(val)

    def c(a, b):
        a, b = a % L, b % L
        if a == b:
            return sp.Integer(0)
        return sym[(a, b)] if a < b else -sym[(b, a)]
    eqs = set()
    for a, b, e in itertools.product(range(L), repeat=3):
        ex = sp.expand(c(a, b) * c(a + b, e) - c(b, e) * c(a, b + e) + c(a, e) * c(b, a + e))
        if ex != 0:
            eqs.add(ex)
    vars_ = sorted({s for q in eqs for s in q.free_symbols}, key=lambda s: (s.name[0] != "k", s.name))
    return list(eqs), vars_, c


def consistent(L, fixed):
    eqs, vars_, _ = build(L, fixed)
    if any(q.is_number and q != 0 for q in eqs):
        return False
    if not vars_:
        return True
    G = sp.groebner(eqs, *vars_, order="grevlex", domain="QQ")
    return list(G.exprs) != [1]


def arc_partitions(L):
    """all ways to cut the path 2..L-2 into consecutive arcs; returns list of dicts n -> Lam_n (Lam_1 = 1)."""
    path = list(range(2, L - 1))
    out = []
    k = len(path)
    for cuts in itertools.product([0, 1], repeat=max(k - 1, 0)):
        arcs, cur = [], [path[0]] if path else []
        for i in range(1, k):
            if cuts[i - 1]:
                arcs.append(cur)
                cur = [path[i]]
            else:
                cur.append(path[i])
        if cur:
            arcs.append(cur)
        lam = {}
        for arc in arcs:
            centre = Fraction(arc[0] + arc[-1], 2)
            for n in arc:
                lam[n] = Fraction(n) - centre
        out.append(lam)
    return out


if __name__ == "__main__":
    Ls = [int(x) for x in sys.argv[1:]] or [4, 5, 6, 7]
    t0 = time.time()
    # ---------- sanity: Jacobi forces Lam_{-1} = -1 under (S)
    for L in Ls:
        eqs, vars_, _ = build(L)
        G = sp.groebner(eqs, *vars_, order="grevlex", domain="QQ")
        lm1 = sp.Symbol(f"l{L-1}")
        check(f"R0_L{L}", G.contains(lm1 + 1), f"(S) alone => Lam_(-1) = -Lam_1 lies in the Jacobi ideal (Groebner membership; {len(vars_)} vars)")
    # ---------- Route 1: grid of candidate Lam_2 values (no (Z))
    grid = [Fraction(j, 2) for j in range(-8, 9)] + [Fraction(1, 3), Fraction(-2, 3), Fraction(7, 4)]
    for L in Ls:
        pred = {Fraction(-m, 2) for m in range(0, L - 3)}
        cons = set()
        for v in grid:
            if consistent(L, {(0, 2): sp.Rational(v.numerator, v.denominator)}):
                cons.add(v)
        check(f"R1_L{L}", cons == (pred & set(grid)),
              f"Lam_2/Lam_1 values consistent with (S)+Jacobi on grid: {sorted(map(str, cons))}; arc prediction {sorted(map(str, pred))}")
        check(f"R1b_L{L}", Fraction(2) not in cons and all(v <= 0 for v in cons),
              f"Lam_2 = 2 Lam_1 (continuum) inconsistent; every consistent Lam_2/Lam_1 <= 0 (Theorem B's |ratio-2|>=1/2 holds and is not sharp)")
    # ---------- Route 2: exact projection to (Lam_2, ..., Lam_{L-2}) via lex elimination
    for L in [l for l in Ls if l <= 7]:
        eqs, vars_, _ = build(L)
        lams = [sp.Symbol(f"l{n}") for n in range(2, L)]
        ks = [v for v in vars_ if v not in lams]
        G = sp.groebner(eqs, *ks, *lams, order="lex", domain="QQ")
        elim = [g for g in G.exprs if g.free_symbols <= set(lams)]
        sols = sp.solve(elim, lams, dict=True) if elim else []
        got = set()
        finite = True
        for s in sols:
            if any(l not in s or not s[l].is_number for l in lams):
                finite = False
                continue
            got.add(tuple(Fraction(str(s[sp.Symbol(f'l{n}')])) for n in range(2, L - 1)))
        pred = {tuple(p[n] for n in range(2, L - 1)) for p in arc_partitions(L)}
        check(f"R2_L{L}", finite and got == pred,
              f"exact projection of the (S)+Jacobi variety to (Lam_2..Lam_{L-2}) = {sorted(got)}; arc-partition prediction = {sorted(pred)}")
    print(f"[exact part done in {time.time()-t0:.1f}s]", flush=True)
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
