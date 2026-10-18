#!/usr/bin/env python3
"""No translation-covariant lattice relabelling algebra of any range closes like the continuum (arc lemma), and the
uniform-lapse bracket needs a non-local Leibniz rule.

Companion runner of
docs/NO_TRANSLATION_COVARIANT_LATTICE_RELABELLING_ALGEBRA_OF_ANY_RANGE_CLOSES_LIKE_THE_CONTINUUM_AND_THE_UNIFORM_LAPSE_BRACKET_NEEDS_A_NON_LOCAL_LEIBNIZ_RULE_BOUNDED_THEOREM_NOTE_2026-10-18.md

Self-contained (Python 3, sympy, numpy). Consolidates the scale-ladder campaign block C3 scripts
(c3_graded_algebra_groebner.py, c3_relabelling_closure_numerics.py, c3_gc_leibniz.py, c3_sine_algebra_2d.py) and
its check scripts (chk_thmB_arcs.py, chk_thmC_ffz.py). Both Groebner routes (worker's and checker's equation
generators) are kept. Part B4 (explicit realisation of every arc partition) and the exact rewrites of the SLAC,
window, Leibniz and sine-algebra checks are new to this consolidation. Same model family throughout: re-running
this runner is not an independent check.

Every gating test is exact (sympy over QQ, Fraction, integer exponent arithmetic in Z[omega]) except those whose
name starts with "F_" (floating point, numpy; machine-precision identities on the stated finite tori; labelled).

Objects (nothing adopted, no physical identification):
  graded algebra : basis X_n, n in Z_L, [X_a, X_b] = c(a,b) X_{a+b}, c antisymmetric, Lam_n := c(0,n), D := X_0.
  (S)            : Lam_1 = 1, c(1,-1) = 1 (WLOG by rescaling X_0 and X_{-1}); Lam_{-1} left free.
  (W)            : Lam_2 = 2 (continuum ratio at the second-longest wavelength).
  (Z)            : Lam_n != 0 for n != 0 (optional; Rabinowitsch variable; worker's route only).
  SLAC / no-wrap : Y_p(w) e_k = (kbar + w pbar) e_{k+p} if |kbar + pbar| <= L//2 else 0 (L odd);
                   the physical generator is X_p = i (2 pi / L) Y_p, which rescales every identity uniformly.

Parts
  B  Theorem B and the arc lemma (Groebner over QQ, two equation generators; explicit realisations).
  A  Theorem A (uniform-vs-non-uniform sub-bracket): local symbols on Z; SLAC no-wrap exact; aliased fails;
     band-limited window exact, band edge fails, window not invariant; SLAC no-wrap full closure fails (B instance).
  C  Theorem C (uniform part of {G, C} is a lattice Leibniz rule): exact nullspaces; SLAC no-wrap solution;
     the B14 / companion-note pi-pi monomial at uniform xi; F_ floating-point bracket checks.
  S  2D sine (Fairlie-Fletcher-Zachos) algebra: exact closure in Z[omega]; Weyl-basis constant 2i sin(pi s/N);
     O(1/N) raw vs O(1/N^2) Weyl (series); no additive weight (no uniform translation can be adjoined).
Default: TOTAL PASS=103 in about 80 s. --slow adds the checker's L = 8 grid (about 1.5 min) and the worker's
L = 10 (S)+(W)+(Z) certificate (about 1.5 min): TOTAL PASS=105 in about 4 min.
"""
from __future__ import annotations

import itertools
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix

PASS = FAIL = 0
T0 = time.time()
SLOW = "--slow" in sys.argv


def check(name, ok, detail=""):
    global PASS, FAIL
    ok = bool(ok)
    PASS += ok
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""), flush=True)


def nbar(n, L):
    """representative of n mod L in (-L/2, L/2]."""
    r = n % L
    return r - L if r > L // 2 else r


# =====================================================================================================
# Part B engines
# =====================================================================================================
def jacobi_checker(L, fixed=None):
    """Checker's generator: 'ad is a representation',
    c(a,b) c(a+b,e) = c(b,e) c(a,b+e) - c(a,e) c(b,a+e) for all a, b, e (coefficient of X_{a+b+e})."""
    fixed = dict(fixed or {})
    sym = {}
    for a in range(L):
        for b in range(a + 1, L):
            sym[(a, b)] = sp.Symbol(f"l{b}" if a == 0 else f"k{a}_{b}")
    sym[(0, 1)] = sp.Integer(1)
    sym[(1, L - 1)] = sp.Integer(1)
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
    return list(eqs), vars_


def checker_consistent(L, fixed):
    eqs, vars_ = jacobi_checker(L, fixed)
    if any(q.is_number and q != 0 for q in eqs):
        return False
    if not vars_:
        return True
    G = sp.groebner(eqs, *vars_, order="grevlex", domain="QQ")
    return list(G.exprs) != [1]


def jacobi_worker(L, lam_fixed, require_Z=True):
    """Worker's generator: cyclic Jacobi c(a,b)c(a+b,e) + c(b,e)c(b+e,a) + c(e,a)c(e+a,b) = 0, optional (Z)."""
    cvar, lam = {}, {}
    for n in range(1, L):
        lam[n] = sp.Rational(lam_fixed[n]) if n in lam_fixed else sp.Symbol(f"lam{n}")
    for a in range(1, L):
        for b in range(a + 1, L):
            cvar[(a, b)] = sp.Symbol(f"c{a}_{b}")
    cvar[(1, L - 1)] = sp.Integer(1)

    def c(a, b):
        a, b = a % L, b % L
        if a == b:
            return sp.Integer(0)
        if a == 0:
            return lam[b]
        if b == 0:
            return -lam[a]
        return cvar[(a, b)] if a < b else -cvar[(b, a)]
    eqs = set()
    for a, b, e in itertools.product(range(L), repeat=3):
        J = sp.expand(c(a, b) * c(a + b, e) + c(b, e) * c(b + e, a) + c(e, a) * c(e + a, b))
        if J != 0:
            eqs.add(J)
    eqs = list(eqs)
    vars_ = sorted({s for e in eqs for s in e.free_symbols}, key=str)
    if require_Z:
        t = sp.Symbol("t_aux")
        prod_ = sp.Integer(1)
        for n in range(1, L):
            prod_ *= lam[n]
        eqs.append(sp.expand(t * prod_ - 1))
        vars_ = sorted(set(vars_) | {t} | set(prod_.free_symbols), key=str)
    return eqs, vars_


def worker_inconsistent(L, lam_fixed, require_Z=True):
    eqs, vars_ = jacobi_worker(L, lam_fixed, require_Z)
    if not vars_:
        return any(e != 0 for e in eqs), 0
    G = sp.groebner(eqs, *vars_, order="grevlex", domain="QQ")
    return list(G.exprs) == [1], len(vars_)


def arc_partitions(L):
    """all cuts of the path 2..L-2 into consecutive arcs (list of lists)."""
    path = list(range(2, L - 1))
    out = []
    if not path:
        return [[]]
    for cuts in itertools.product([0, 1], repeat=len(path) - 1):
        arcs, cur = [], [path[0]]
        for i in range(1, len(path)):
            if cuts[i - 1]:
                arcs.append(cur)
                cur = [path[i]]
            else:
                cur.append(path[i])
        arcs.append(cur)
        out.append(arcs)
    return out


def arc_lams(L, arcs):
    lam = {}
    for arc in arcs:
        centre = Fr(arc[0] + arc[-1], 2)
        for n in arc:
            lam[n] = Fr(n) - centre
    return lam


def arc_algebra(L, arcs):
    """sl2 |x (sum of irreducibles V_m, abelian), one irreducible per arc, X_n weight vectors.
    sl2: D = X_0, E = X_1, F = 2 X_{-1}, [X_1, X_{-1}] = X_0 (so Lam_1 = 1, c(1,-1) = 1).
    V_m on arc [n0, n0+m]: v_j <-> X_{n0+m-j}, H v_j = (m-2j) v_j, E v_j = (m-j+1) v_{j-1}, F v_j = (j+1) v_{j+1}.
    Returns the antisymmetric structure-constant dict c[(a,b)] (residues), zero entries omitted."""
    c = {}

    def put(a, b, v):
        a, b = a % L, b % L
        if v != 0:
            c[(a, b)] = Fr(v)
            c[(b, a)] = -Fr(v)
    put(0, 1, 1)
    put(0, -1, -1)
    put(1, -1, 1)
    for arc in arcs:
        n0, m = arc[0], len(arc) - 1
        for j in range(m + 1):
            n = n0 + m - j
            put(0, n, Fr(m - 2 * j, 2))
            if j >= 1:
                put(1, n, m - j + 1)
            if j <= m - 1:
                put(-1, n, Fr(j + 1, 2))
    return c


def cyclic_jacobi_ok(L, c):
    g = lambda a, b: c.get((a % L, b % L), Fr(0))
    for a, b, e in itertools.product(range(L), repeat=3):
        if g(a, b) * g(a + b, e) + g(b, e) * g(b + e, a) + g(e, a) * g(e + a, b) != 0:
            return False
    return True


def part_B():
    print("\n=== Part B: Theorem B and the arc lemma (exact) ===", flush=True)
    # ---- B0 (checker route): (S) alone forces Lam_{-1} = -Lam_1
    for L in (4, 5, 6, 7):
        eqs, vars_ = jacobi_checker(L)
        G = sp.groebner(eqs, *vars_, order="grevlex", domain="QQ")
        check(f"B0_L{L}", G.contains(sp.Symbol(f"l{L-1}") + 1),
              f"(S) + Jacobi => Lam_(-1) + Lam_1 in the ideal (Groebner membership, checker generator, {len(vars_)} vars)")
    # ---- B1 (checker route): consistent Lam_2 on a rational grid = arc prediction (no (Z))
    grid = [Fr(j, 2) for j in range(-8, 9)] + [Fr(1, 3), Fr(-2, 3), Fr(7, 4)]
    Ls = [4, 5, 6, 7] + ([8] if SLOW else [])
    for L in Ls:
        t = time.time()
        pred = {Fr(-m, 2) for m in range(0, L - 3)}
        cons = {v for v in grid if checker_consistent(L, {(0, 2): sp.Rational(v.numerator, v.denominator)})}
        check(f"B1_L{L}", cons == (pred & set(grid)) and Fr(2) not in cons and all(v <= 0 for v in cons),
              f"consistent Lam_2/Lam_1 on a 20-point grid = {sorted(map(str, cons))} = arc prediction "
              f"{{0,...,-(L-4)/2}} on the grid; 2 excluded; all <= 0 ({time.time()-t:.1f}s)")
    # ---- B2 (checker route): exact projection of the variety to (Lam_2..Lam_{L-2}) = arc partitions
    for L in (4, 5, 6, 7):
        t = time.time()
        eqs, vars_ = jacobi_checker(L)
        lams = [sp.Symbol(f"l{n}") for n in range(2, L)]
        ks = [v for v in vars_ if v not in lams]
        G = sp.groebner(eqs, *ks, *lams, order="lex", domain="QQ")
        elim = [g for g in G.exprs if g.free_symbols <= set(lams)]
        sols = sp.solve(elim, lams, dict=True) if elim else []
        got, finite = set(), True
        for s in sols:
            if any(l not in s or not s[l].is_number for l in lams):
                finite = False
                continue
            got.add(tuple(Fr(str(s[sp.Symbol(f'l{n}')])) for n in range(2, L - 1)))
        pred = {tuple(arc_lams(L, arcs)[n] for n in range(2, L - 1)) for arcs in arc_partitions(L)}
        check(f"B2_L{L}", finite and got == pred,
              f"lex elimination: projection of (S)+Jacobi to (Lam_2..Lam_{L-2}) is finite, {len(got)} points "
              f"= the {len(pred)} arc partitions ({time.time()-t:.1f}s)")
    # ---- B3 (worker route): certificates and controls
    ok, nv = worker_inconsistent(3, {1: 1, 2: -1})
    check("B3_PC1", not ok, "control: L = 3, Lam = (1,-1) is consistent (sl2 itself: the L = 3 exception)")
    ok, nv = worker_inconsistent(5, {1: 1, 4: -1, 2: sp.Rational(-1, 2), 3: sp.Rational(1, 2)})
    check("B3_PC2", not ok, "control: L = 5, Lam_(+-2) = -+1/2 consistent: sl2 |x C^2 (special affine); (i) is sharp")
    ok, nv = worker_inconsistent(4, {1: 1, 3: -1, 2: 0}, require_Z=False)
    check("B3_PC3", not ok, "control: L = 4, Lam_2 = 0 consistent (sl2 (+) C X_2; violates (Z))")
    for L in range(4, 10):
        t = time.time()
        ok, nv = worker_inconsistent(L, {1: 1, 2: 2})
        check(f"B3_Z_L{L}", ok, f"(S)+(W)+(Z), other Lam free: Groebner basis = [1] ({nv} vars, {time.time()-t:.1f}s)")
    for L in range(4, 10):
        t = time.time()
        ok, nv = worker_inconsistent(L, {1: 1, 2: 2}, require_Z=False)
        check(f"B3_noZ_L{L}", ok, f"(S)+(W) without (Z): Groebner basis = [1] ({nv} vars, {time.time()-t:.1f}s)")
    for L in (5, 7, 9):
        lf = {n: nbar(n, L) for n in range(1, L)}
        ok, nv = worker_inconsistent(L, lf, require_Z=False)
        check(f"B3_SLAC_L{L}", ok, f"SLAC/continuum spectrum Lam_n = nbar on the whole zone: inconsistent ({nv} vars)")
    eqs, vars_ = jacobi_worker(5, {1: 1, 4: -1})
    lam2 = sp.Symbol("lam2")
    G = sp.groebner(eqs, *[v for v in vars_ if v != lam2], lam2, order="lex", domain="QQ")
    uni = [g for g in G.exprs if g.free_symbols <= {lam2}]
    roots = set(sp.solve(uni[0], lam2)) if uni else None
    check("B3_Q_L5", bool(uni) and roots <= {sp.Rational(1, 2), sp.Rational(-1, 2)},
          f"L = 5, (S)+(Z), Lam_2 free: elimination ideal {uni[0] if uni else None} (2 Lam_2/Lam_1 odd)")
    if SLOW:
        t = time.time()
        ok, nv = worker_inconsistent(10, {1: 1, 2: 2})
        check("B3_Z_L10", ok, f"(S)+(W)+(Z) at L = 10: Groebner basis = [1] ({nv} vars, {time.time()-t:.1f}s)")
    # ---- B4 (consolidation, new path): every arc partition is realised; the phi-fixed set is the sl2
    for L in range(3, 13):
        parts = arc_partitions(L)
        all_ok, lam2s = True, set()
        for arcs in parts:
            c = arc_algebra(L, arcs)
            lam = {n: c.get((0, n), Fr(0)) for n in range(L)}
            pred = arc_lams(L, arcs)
            ok = cyclic_jacobi_ok(L, c) and all(lam[n] == pred[n] for n in pred)
            ok = ok and lam[1] == 1 and lam[L - 1] == -1 and c.get((1, L - 1)) == 1
            w = {n: 2 * lam[n] for n in range(L)}
            ok = ok and all(x.denominator == 1 for x in w.values())
            fixed = {n for n in range(L) if (int(w[n]) - 2 * n) % (2 * L) == 0}
            ok = ok and fixed == {0, 1, L - 1}
            dl = {n: (int(w[n]) - 2 * n) % (2 * L) for n in range(L)}
            ok = ok and all((dl[a] + dl[b] - dl[(a + b) % L]) % (2 * L) == 0 for (a, b) in c)
            all_ok &= ok
            if L >= 4:
                lam2s.add(lam[2])
        exp2 = {Fr(-m, 2) for m in range(0, L - 3)} if L >= 4 else set()
        check(f"B4_L{L}", all_ok and len(parts) == (2 ** (L - 4) if L >= 4 else 1) and lam2s == exp2,
              f"all {len(parts)} arc partitions realised as sl2 |x (sum V_m): exact Jacobi, Lam_n = n - centre, "
              f"integer weights, phi-fixed momenta = {{0,+-1}}, delta additive; Lam_2 set = {sorted(map(str, lam2s))}")


# =====================================================================================================
# Part A: Theorem A, SLAC sub-brackets, band-limited window (exact)
# =====================================================================================================
def Y_ops(L, w, wrap="none"):
    """dict p -> sparse matrix {(row, col): Fraction}, momentum basis, residues."""
    m = L // 2
    ops = {}
    for p in range(L):
        M = {}
        for k in range(L):
            kb, pb = nbar(k, L), nbar(p, L)
            if wrap == "none" and abs(kb + pb) > m:
                continue
            v = Fr(kb) + Fr(w) * pb
            if v != 0:
                M[((k + p) % L, k)] = v
        ops[p] = M
    return ops


def mm(A, B):
    out = {}
    for (i, k), a in A.items():
        for (k2, j), b in B.items():
            if k == k2:
                out[(i, j)] = out.get((i, j), 0) + a * b
    return {key: v for key, v in out.items() if v != 0}


def comm(A, B):
    P, Q = mm(A, B), mm(B, A)
    out = dict(P)
    for key, v in Q.items():
        out[key] = out.get(key, 0) - v
    return {key: v for key, v in out.items() if v != 0}


def proportional(A, B):
    """is A = c B for some scalar c (exact)? returns (bool, c)."""
    if not A:
        return True, Fr(0)
    if not B:
        return False, None
    keys = set(A) | set(B)
    c = None
    for key in keys:
        a, b = A.get(key, 0), B.get(key, 0)
        if b == 0:
            if a != 0:
                return False, None
            continue
        r = Fr(a) / b
        if c is None:
            c = r
        elif r != c:
            return False, None
    return True, c


def apply_vec(A, k):
    return {i: v for (i, j), v in A.items() if j == k}


def part_A():
    print("\n=== Part A: Theorem A, SLAC sub-brackets, band-limited window (exact) ===", flush=True)
    # ---- A1: local (finite-range) transports on Z: d(zy) - d(z) is not constant in z while f(zy, z) != 0
    z, y, C = sp.symbols("z y C")
    fams = {
        "B14_central": {(0, 1): Fr(1, 2), (0, 0): Fr(-1, 2), (1, 1): Fr(1, 2), (1, 0): Fr(-1, 2)},
        "imp4": {},
        "rand_r3": {},
    }
    for (r, c_, v) in [(0, 1, Fr(9, 8)), (0, 0, Fr(-9, 8)), (0, 2, Fr(-1, 24)), (0, -1, Fr(1, 24))]:
        for rr in (r, r + 1):
            fams["imp4"][(rr, c_)] = fams["imp4"].get((rr, c_), 0) + v / 2
    rng = np.random.default_rng(20261018)
    A = {}
    for r in (-1, 0, 1, 2):
        for c_ in (-1, 0, 1, 2):
            if r != c_:
                A[(r, c_)] = Fr(int(rng.integers(-5, 6)), 7)
    for r in (-1, 0, 1, 2):  # annihilate constants: sum_c A[r, c] = 0, fixed on column 0
        s = sum(v for (rr, _), v in A.items() if rr == r and _ != 0)
        A[(r, 0)] = -s
    fams["rand_r3"] = A
    for nm, A in fams.items():
        # (X_xi phi)_x = sum_b xi_b sum_{r,c} A[r,c] [x = b + r] phi_{b+c};  f(k'+p, k') = sum A (zy)^(-r) z^c
        f = sum(sp.Rational(v.numerator, v.denominator) * (z * y) ** (-r) * z ** c_ for (r, c_), v in A.items())
        d = lambda zz: sum(sp.Rational(v.numerator, v.denominator) * zz ** (c_ - r) for (r, c_), v in A.items())
        g = sp.expand(d(z * y) - d(z))
        def zcoeffs(e):
            P = sp.Poly(sp.expand(e * z ** 8), z)
            return {mon[0] - 8: sp.expand(co) for mon, co in zip(P.monoms(), P.coeffs())}
        varying = any(e != 0 and co != 0 for e, co in zcoeffs(g).items())
        dnz = any(e != 0 and co != 0 for e, co in zcoeffs(d(z)).items())
        check(f"A1_{nm}", sp.expand(f) != 0 and varying and dnz,
              "finite range on Z: f(zy,z) is a nonzero Laurent polynomial and d(zy)-d(z) has a nonconstant z-part, so "
              "f [d(zy)-d(z)-C(y)] = 0 has no solution C(y) for y != 1: [D, X_p] not in span X_p")
    # ---- A2/A3: SLAC no-wrap sub-bracket exact; aliased (full-support f) fails
    for L in (5, 7, 9):
        for w in (Fr(0), Fr(1, 2), Fr(-1)):
            Y = Y_ops(L, w)
            ok = all(proportional(comm(Y[0], Y[p]), Y[p]) == (True, Fr(nbar(p, L))) or (not Y[p])
                     for p in range(1, L))
            check(f"A2_L{L}_w{w}", ok, "SLAC no-wrap: [Y_0, Y_p] = pbar Y_p exactly for every p (Theorem A sub-bracket closes)")
        Ya = Y_ops(L, Fr(0), wrap="alias")
        bad = [p for p in range(1, L) if not proportional(comm(Ya[0], Ya[p]), Ya[p])[0]]
        check(f"A3_L{L}", len(bad) == L - 1, f"aliased SLAC (f kept on the wrap set): [Y_0, Y_p] not in span Y_p for all {len(bad)} p != 0")
    # ---- A4: band-limited window, exact
    for (L, nL) in [(9, 1), (13, 2), (17, 3), (25, 4)]:
        m = L // 2
        for w in (Fr(0), Fr(1, 2), Fr(-1)):
            Y = Y_ops(L, w)
            ok_in, bad_edge = True, False
            for a in range(-nL, nL + 1):
                for b in range(-nL, nL + 1):
                    Dm = comm(Y[a % L], Y[b % L])
                    rhs = {key: (b - a) * v for key, v in Y[(a + b) % L].items()}
                    diff = dict(Dm)
                    for key, v in rhs.items():
                        diff[key] = diff.get(key, 0) - v
                    diff = {key: v for key, v in diff.items() if v != 0}
                    for k in range(L):
                        col = apply_vec(diff, k)
                        if abs(nbar(k, L)) <= m - 2 * nL and col:
                            ok_in = False
                        if abs(nbar(k, L)) == m and col:
                            bad_edge = True
            # window not invariant: some Y_a (|a| <= nL) maps a window vector outside the window
            leaves = any(abs(nbar(i, L)) > m - 2 * nL
                         for a in range(-nL, nL + 1) for k in range(L) if abs(nbar(k, L)) <= m - 2 * nL
                         for i in apply_vec(Y[a % L], k))
            check(f"A4_L{L}_n{nL}_w{w}", ok_in and bad_edge and leaves,
                  f"|a|,|b| <= {nL}: [Y_a,Y_b] e_k = (b-a) Y_(a+b) e_k exactly for |k| <= {m-2*nL}; fails for some band-edge k; "
                  f"window not invariant")
    # ---- A5: Theorem B instance -- SLAC no-wrap transport: (S) and Lam_2 = 2 Lam_1 hold, full closure fails
    for L in (5, 7, 9):
        for w in (Fr(0), Fr(1, 2), Fr(-1)):
            Y = Y_ops(L, w)
            l1 = proportional(comm(Y[0], Y[1]), Y[1])[1]
            l2 = proportional(comm(Y[0], Y[2]), Y[2])[1]
            s11 = comm(Y[1], Y[L - 1])
            fails = [(p, q) for p in range(1, L) for q in range(1, L)
                     if p != q and not proportional(comm(Y[p], Y[q]), Y[(p + q) % L])[0]]
            check(f"A5_L{L}_w{w}", l1 == 1 and l2 == 2 and bool(s11) and len(fails) > 0,
                  f"Lam_1 = 1, Lam_2 = 2, [Y_1,Y_-1] != 0; {len(fails)} ordered pairs (p,q) with [Y_p,Y_q] not in span Y_(p+q)")
    Y = Y_ops(3, Fr(-1))
    ok = all(proportional(comm(Y[p], Y[q]), Y[(p + q) % 3])[0] for p in range(3) for q in range(3))
    check("A5_L3_wm1", ok and bool(comm(Y[1], Y[2])), "L = 3, w = -1: closes exactly, [Y_1,Y_-1] != 0 (the sl2 exception)")
    Y = Y_ops(3, Fr(0))
    ok = all(proportional(comm(Y[p], Y[q]), Y[(p + q) % 3])[0] for p in range(3) for q in range(3))
    check("A5_L3_w0", ok and not comm(Y[1], Y[2]), "L = 3, w = 0: closes only degenerately, [Y_1,Y_-1] = 0 ((S) fails)")


# =====================================================================================================
# Part C: Theorem C (exact) and floating-point bracket checks
# =====================================================================================================
def leibniz_nullspace(L, allowed):
    rows = []
    for k1 in range(L):
        for k2 in range(L):
            if allowed(k1, k2):
                r = [0] * (2 * L)
                r[k1] += 1
                r[k2] += 1
                r[L + (k1 + k2) % L] -= 1
                rows.append(r)
    return sp.Matrix(rows).nullspace()


def part_C():
    print("\n=== Part C: Theorem C, the uniform part of {G, C} is a lattice Leibniz rule ===", flush=True)
    for L in (4, 5, 6, 7, 8, 9):
        ns = leibniz_nullspace(L, lambda a, b: True)
        v = ns[0] if len(ns) == 1 else None
        ok = v is not None and all(v[j] == v[0] for j in range(L)) and all(v[L + j] == 2 * v[0] for j in range(L))
        check(f"C1_L{L}", ok, f"full support: lam(k1)+lam(k2) = lam'(k1+k2) for all k1,k2 has solution space "
              f"span{{lam = 1, lam' = 2}} (dim {len(ns)}); lam(0) = 0 (D kills constants) => lam = 0")
    for L in (5, 7, 9):
        m = L // 2
        allowed = lambda a, b: abs(nbar(a, L)) <= m and abs(nbar(b, L)) <= m and abs(nbar(a, L) + nbar(b, L)) <= m
        ns = leibniz_nullspace(L, allowed)
        M = sp.Matrix.hstack(*ns)
        slac = sp.Matrix([nbar(j, L) for j in range(L)] + [nbar(j, L) for j in range(L)])
        in_span = M.rank() == sp.Matrix.hstack(M, slac).rank()
        check(f"C2_L{L}", len(ns) == 2 and in_span,
              f"no-wrap (anti-aliased) support: solution space dim {len(ns)} = span{{const, kbar}}, contains SLAC lam = lam' = kbar")
    # ---- C3: the B14 / companion-note pi-pi monomial at uniform xi (1D reduction, exact)
    L = 5
    ph = sp.symbols(f"phi0:{L}")
    pi = sp.symbols(f"pi0:{L}")
    N = sp.symbols(f"N0:{L}")
    G1 = sum((ph[(x + 1) % L] - ph[x]) * (pi[x] + pi[(x + 1) % L]) / 2 for x in range(L))
    Hpp = sum(N[x] * pi[x] ** 2 / 2 for x in range(L))
    br = sp.expand(sum(sp.diff(G1, ph[y]) * sp.diff(Hpp, pi[y]) - sp.diff(G1, pi[y]) * sp.diff(Hpp, ph[y]) for y in range(L)))
    target = sp.expand(sum((N[(x + 1) % L] - N[x]) * pi[x] * pi[(x + 1) % L] / 2 for x in range(L)))
    ob = sp.expand(-sum((N[(x + 1) % L] - N[x]) * (pi[(x + 1) % L] - pi[x]) ** 2 for x in range(L)) / 4)
    offdiag = lambda e: sp.expand(e - sum(sp.Poly(e, *pi).coeff_monomial(pi[x] ** 2) * pi[x] ** 2 for x in range(L)))
    ok = br == target and offdiag(ob) == target and offdiag(br) != 0
    check("C3_B14_uniform", ok,
          "1D, L = 5: {G_m[xi=1], (1/2) sum N pi^2} = (1/2) sum (N_(x+1)-N_x) pi_x pi_(x+1), whose off-diagonal part equals "
          "that of the companion note's ob at xi = 1; H_m(N') has no pi_x pi_(x+1) term, and at uniform xi G_g and every "
          "coupling vanish, so the uniform part fails (full-support pi product, D = central != 0: Theorem C)")
    # ---- F_C4 (floating point): SLAC + anti-aliased density closes with N' = +D N; local or ultralocal fails
    rng = np.random.default_rng(1018)

    def slac(L):
        k = np.array([2 * np.pi * nbar(n, L) / L for n in range(L)])
        F = np.exp(-1j * np.outer(np.arange(L), np.arange(L)) * 2 * np.pi / L) / np.sqrt(L)
        return (F.conj().T @ np.diag(1j * k) @ F).real

    def product_form(L, N, kind):
        if kind == "ultralocal":
            return np.diag(N)
        F = np.exp(-1j * np.outer(np.arange(L), np.arange(L)) * 2 * np.pi / L) / L
        Nt = np.array([sum(N[x] * np.exp(2j * np.pi * K * x / L) for x in range(L)) for K in range(L)])
        W = np.zeros((L, L), complex)
        for a in range(L):
            for b in range(L):
                if abs(nbar(a, L) + nbar(b, L)) <= L // 2:
                    W[a, b] = Nt[(a + b) % L]
        M = (F.T @ W @ F).real
        return (M + M.T) / 2

    def Hform(L, N, Dg, c, kind):
        M = product_form(L, N, kind)
        Z = np.zeros((L, L))
        return np.block([[c * Dg.T @ M @ Dg, Z], [Z, M]])

    def pb(A, B):
        L = A.shape[0] // 2
        J = np.block([[np.zeros((L, L)), np.eye(L)], [-np.eye(L), np.zeros((L, L))]])
        return A @ J @ B - B @ J @ A

    def lsq(target, cols):
        iu = np.triu_indices(target.shape[0])
        A = np.stack([c_[iu] for c_ in cols], axis=1)
        sol, *_ = np.linalg.lstsq(A, target[iu], rcond=None)
        return np.linalg.norm(A @ sol - target[iu]) / np.linalg.norm(target[iu]), sol

    for L in (7, 9, 11):
        Ds = slac(L)
        Dc = np.roll(np.eye(L), -1, axis=0) * .5 - np.roll(np.eye(L), 1, axis=0) * .5
        Dfw = np.roll(np.eye(L), -1, axis=0) - np.eye(L)
        res = {}
        for nm, D, Dg, kind in (("SLAC_antialiased", Ds, Ds, "antialiased"), ("SLAC_ultralocal", Ds, Ds, "ultralocal"),
                                ("central_ultralocal", Dc, Dfw, "ultralocal"), ("central_antialiased", Dc, Dc, "antialiased")):
            N = 1 + 0.3 * rng.normal(size=L)
            Z = np.zeros((L, L))
            G = np.block([[Z, D.T], [D, Z]])
            tgt = pb(G, Hform(L, N, Dg, 0.7, kind))
            r, sol = lsq(tgt, [Hform(L, np.eye(L)[x], Dg, 0.7, kind) for x in range(L)])
            res[nm] = (r, np.linalg.norm(sol - D @ N) / np.linalg.norm(D @ N))
        ok = res["SLAC_antialiased"][0] < 1e-10 and res["SLAC_antialiased"][1] < 1e-8 and \
            all(res[k][0] > 1e-3 for k in ("SLAC_ultralocal", "central_ultralocal", "central_antialiased"))
        check(f"F_C4_L{L}", ok, "float: {P, H(N)} = H(N') closes for SLAC + anti-aliased density with N' = +D_SLAC N "
              f"(residual {res['SLAC_antialiased'][0]:.1e}, |N'-DN| {res['SLAC_antialiased'][1]:.1e}); fails for SLAC + "
              f"ultralocal ({res['SLAC_ultralocal'][0]:.2f}) and central D ({res['central_ultralocal'][0]:.2f}, "
              f"{res['central_antialiased'][0]:.2f})")


# =====================================================================================================
# Part S: the 2D sine algebra (exact in Z[omega])
# =====================================================================================================
def zw_zero(vec, N):
    """element sum_j vec[j] omega^j of Z[omega], omega primitive N-th root, N prime: zero iff all entries equal."""
    return all(v == vec[0] for v in vec)


def part_S():
    print("\n=== Part S: the 2D sine (Fairlie-Fletcher-Zachos) algebra ===", flush=True)
    for N in (5, 7):
        # monomial matrices: (perm, exps) with M e_j = omega^{exps[j]} e_{perm[j]}; exponents mod N
        def mono_mul(A, B):
            pa, ea = A
            pb_, eb = B
            return (tuple(pa[pb_[j]] for j in range(N)), tuple((eb[j] + ea[pb_[j]]) % N for j in range(N)))
        g = (tuple((j + 1) % N for j in range(N)), (0,) * N)
        h = (tuple(range(N)), tuple(j for j in range(N)))
        I = (tuple(range(N)), (0,) * N)

        def power(M, k):
            out = I
            for _ in range(k % N):
                out = mono_mul(out, M)
            return out
        J = {(a, b): mono_mul(power(g, a), power(h, b)) for a in range(N) for b in range(N)}
        ok_rel = True
        for p in J:
            for q in J:
                r = ((p[0] + q[0]) % N, (p[1] + q[1]) % N)
                lhs = mono_mul(J[p], J[q])
                ph = (p[1] * q[0]) % N
                rhs = (J[r][0], tuple((e + ph) % N for e in J[r][1]))
                ok_rel &= lhs == rhs
        check(f"S0_N{N}", ok_rel, "exact monomial matrices: J_p J_q = omega^(p2 q1) J_(p+q) for all p, q in Z_N^2")
        # structure constants c(p,q) = omega^A - omega^B, A = p2 q1, B = p1 q2 (exponents mod N); cyclic Jacobi exactly
        cs = {(p, q): ((p[1] * q[0]) % N, (p[0] * q[1]) % N) for p in J for q in J}
        add = lambda p, q: ((p[0] + q[0]) % N, (p[1] + q[1]) % N)
        ok_j = True
        keys = list(J)
        for p in keys:
            for q in keys:
                pq = add(p, q)
                for e in keys:
                    t = [0] * N
                    for (A1, B1), (A2, B2) in ((cs[(p, q)], cs[(pq, e)]), (cs[(q, e)], cs[(add(q, e), p)]),
                                               (cs[(e, p)], cs[(add(e, p), q)])):
                        if A1 == B1 or A2 == B2:
                            continue
                        t[(A1 + A2) % N] += 1
                        t[(A1 + B2) % N] -= 1
                        t[(B1 + A2) % N] -= 1
                        t[(B1 + B2) % N] += 1
                    if not zw_zero(t, N):
                        ok_j = False
        check(f"S1_N{N}", ok_j, f"exact closure: [X_p, X_r] = kappa c(p,r) X_(p+r) (Jacobi in Z[omega], all {N**6} triples)")
        # Weyl basis J'_m = zeta^{m1 m2} J_m (zeta = e^{i pi/N}; exponents mod 2N), small momenta, no wrap
        def lift(M):  # exponents mod N -> mod 2N via omega = zeta^2
            return (M[0], tuple((2 * e) % (2 * N) for e in M[1]))

        def mono_mul2(A, B):
            pa, ea = A
            pb_, eb = B
            return (tuple(pa[pb_[j]] for j in range(N)), tuple((eb[j] + ea[pb_[j]]) % (2 * N) for j in range(N)))

        def Jw(m):
            M = lift(J[(m[0] % N, m[1] % N)])
            return (M[0], tuple((e + m[0] * m[1]) % (2 * N) for e in M[1]))
        small = [(a, b) for a in range(-1, 2) for b in range(-1, 2)]
        ok_w = True
        for p in small:
            for q in small:
                r = (p[0] + q[0], p[1] + q[1])
                s = p[1] * q[0] - p[0] * q[1]
                lhs = mono_mul2(Jw(p), Jw(q))
                rhs = (Jw(r)[0], tuple((e + s) % (2 * N) for e in Jw(r)[1]))
                ok_w &= lhs == rhs
        check(f"S2_N{N}", ok_w, "Weyl basis: J'_p J'_q = zeta^s J'_(p+q), s = p2 q1 - p1 q2, so [J'_p, J'_q] = 2i sin(pi s/N) "
              "J'_(p+q) (exact, |p_i|,|q_i| <= 1)")
        # no additive weight: Lam(p)+Lam(q) = Lam(p+q) whenever c(p,q) != 0 (p, q, p+q != 0) has only Lam = 0
        nz = [p for p in J if p != (0, 0)]
        idx = {p: i for i, p in enumerate(nz)}
        rows = []
        for p in nz:
            for q in nz:
                r = add(p, q)
                if r == (0, 0) or (p[1] * q[0] - p[0] * q[1]) % N == 0:
                    continue
                row = [0] * len(nz)
                row[idx[p]] += 1
                row[idx[q]] += 1
                row[idx[r]] -= 1
                rows.append(row)
        rows = [list(r) for r in sorted(set(map(tuple, rows)))]
        rk = DomainMatrix([[QQ(v) for v in r] for r in rows], (len(rows), len(nz)), QQ).rank()
        check(f"S4_N{N}", rk == len(nz), f"Jacobi with an adjoined diagonal D, (Lam(p)+Lam(q)-Lam(p+q)) c(p,q) = 0, has rank "
              f"{rk} = {len(nz)} unknowns: Lam = 0, so no uniform translation can be adjoined")
    # ---- S3: continuum limit of the structure constants (series in eps = 1/N)
    eps = sp.Symbol("eps", positive=True)
    p, q = (1, 2), (2, -1)
    s = p[1] * q[0] - p[0] * q[1]
    raw = (sp.exp(2 * sp.pi * sp.I * eps * p[1] * q[0]) - sp.exp(2 * sp.pi * sp.I * eps * p[0] * q[1])) / (2 * sp.pi * sp.I * eps)
    weyl = sp.sin(sp.pi * eps * s) / (sp.pi * eps)
    sr = sp.series(raw, eps, 0, 3).removeO()
    sw = sp.series(weyl, eps, 0, 3).removeO()
    c1r = sp.simplify(sr.coeff(eps, 1))
    c1w = sp.simplify(sw.coeff(eps, 1))
    c2w = sp.simplify(sw.coeff(eps, 2))
    check("S3", sp.simplify(sr.coeff(eps, 0) - s) == 0 and c1r != 0 and c1w == 0 and sp.simplify(c2w + sp.pi ** 2 * s ** 3 / 6) == 0,
          f"p = (1,2), q = (2,-1), s = {s}: raw basis kappa c = s + ({c1r}) eps + ... (O(a)); Weyl basis "
          f"(N/pi) sin(pi s/N) = s - pi^2 s^3 eps^2/6 + ... (O(a^2)); the O(a) is a basis artefact")
    # ---- F_S5 (floating point): non-locality of a site-localised stream function (worker E4)
    for N in (5, 7):
        w = np.exp(2j * np.pi / N)
        g = np.roll(np.eye(N), 1, axis=0)
        h = np.diag(w ** np.arange(N))
        Jm = {(a, b): np.linalg.matrix_power(g, a) @ np.linalg.matrix_power(h, b) for a in range(N) for b in range(N)}
        keys = sorted(Jm)
        idx = {m: i for i, m in enumerate(keys)}
        kappa = N / (2j * np.pi)
        Xf = np.zeros((N * N, N * N), complex)
        for pp in keys:
            for qq in keys:
                r = ((pp[0] + qq[0]) % N, (pp[1] + qq[1]) % N)
                cc = w ** ((pp[1] * qq[0]) % N) - w ** ((pp[0] * qq[1]) % N)
                Xf[idx[r], idx[qq]] += kappa * cc / (N * N)
        F = np.exp(-2j * np.pi * np.outer(np.arange(N), np.arange(N)) / N) / np.sqrt(N)
        F2 = np.kron(F, F)
        Xr = F2.conj().T @ Xf @ F2
        rng_max = 0
        for out in range(N * N):
            for inn in range(N * N):
                if abs(Xr[out, inn]) > 1e-10:
                    for st in (out, inn):
                        rng_max = max(rng_max, max(abs(nbar(st // N, N)), abs(nbar(st % N, N))))
        check(f"F_S5_N{N}", rng_max == N // 2, f"float: the relabelling generated by a site-localised stream function reaches "
              f"torus distance {rng_max} = N//2 (non-local)")


if __name__ == "__main__":
    part_B()
    part_A()
    part_C()
    part_S()
    print(f"\n[runtime {time.time()-T0:.1f}s{'; --slow' if SLOW else ''}]")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    sys.exit(0 if FAIL == 0 else 1)
