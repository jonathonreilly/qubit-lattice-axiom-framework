#!/usr/bin/env python3
"""C3 / Theorem B certificate by an independent route (Groebner bases over Q), small L.

Abstract object.  The L-periodic sector of ANY translation-covariant, injective relabelling map xi -> G[xi]
(1D, scalar xi, or the e_1-component of a cubic-covariant d-dim map restricted to xi = xi(x_1) e_1) that closes is an
L-dimensional complex Lie algebra g = span{X_n : n in Z_L}, X_n = G[exp(2 pi i n x / L)], graded by lattice momentum:
      [X_a, X_b] = c(a,b) X_{a+b},   c(b,a) = -c(a,b),   c(0,n) =: Lam_n   ([D, X_n] = Lam_n X_n, D = X_0 = uniform).
Jacobi:  c(a,b)c(a+b,e) + c(b,e)c(b+e,a) + c(e,a)c(e+a,b) = 0  for all a,b,e in Z_L.

Hypotheses tested (normalisations WLOG by rescaling D and X_{+-1}):
  (S)  Lam_1 = 1, c(1,-1) = 1       (continuum: [e^{ipx}d, e^{-ipx}d] = -2ip d != 0, [d, e^{ipx}d] = ip e^{ipx}d)
  (W)  Lam_2 = 2                    (continuum ratio at the second-longest wavelength)
  (Z)  Lam_n != 0 for all n != 0    (optional; Rabinowitsch variable)
Theorem B (proved in the hand-back by sl2 weight theory) predicts: (S)+(Z) => 2 Lam_n/Lam_1 odd for n not in {0,+-1};
hence (S)+(W)+(Z) is inconsistent for every L >= 4.  Here: Groebner basis == [1] certifies inconsistency over C.
Positive controls (must be consistent): L=3 sl2;  L=5 affine sl2 (sl2 |x C^2) with Lam_{+-2} = -+1/2;
L=4 sl2 (+) C X_2 with Lam_2 = 0 (violates (Z)).
"""
import sys
import time
from itertools import product

import sympy as sp

RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


def system(L, lam_fixed, require_Z=True):
    """Return (equations, variables) for the graded Lie algebra on Z_L."""
    cvar = {}
    lam = {}
    for n in range(1, L):
        lam[n] = sp.Rational(lam_fixed[n]) if n in lam_fixed else sp.Symbol(f"lam{n}")
    for a in range(1, L):
        for b in range(a + 1, L):
            cvar[(a, b)] = sp.Symbol(f"c{a}_{b}")
    cvar[(1, L - 1)] = sp.Integer(1)  # (S): c(1,-1) = 1

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
    for a, b, e in product(range(L), repeat=3):
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
        vars_ = vars_ + [t]
        vars_ = sorted(set(vars_) | {s for s in prod_.free_symbols}, key=str)
    return eqs, vars_


def inconsistent(L, lam_fixed, require_Z=True):
    eqs, vars_ = system(L, lam_fixed, require_Z)
    if not vars_:
        return any(e != 0 for e in eqs), 0, 0.0
    t0 = time.time()
    G = sp.groebner(eqs, *vars_, order="grevlex", domain="QQ")
    return (list(G.exprs) == [1]), len(vars_), time.time() - t0


if __name__ == "__main__":
    Lmax = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    # positive controls
    ok, nv, dt = inconsistent(3, {1: 1, 2: -1})
    check("PC1", not ok, f"L=3, Lam=(1,-1): sl2 is a consistent graded Lie algebra (control; {nv} vars, {dt:.1f}s)")
    ok, nv, dt = inconsistent(5, {1: 1, 4: -1, 2: sp.Rational(-1, 2), 3: sp.Rational(1, 2)})
    check("PC2", not ok, f"L=5, Lam_(+-2) = -+1/2: affine sl2 (sl2 |x C^2) consistent -> Theorem B's half-odd weights are attained (sharpness control; {nv} vars, {dt:.1f}s)")
    ok, nv, dt = inconsistent(4, {1: 1, 3: -1, 2: 0}, require_Z=False)
    check("PC3", not ok, f"L=4, Lam_2 = 0 (violates (Z)): sl2 (+) C X_2 consistent (control; {nv} vars, {dt:.1f}s)")
    # Theorem B instances
    for L in range(4, Lmax + 1):
        ok, nv, dt = inconsistent(L, {1: 1, 2: 2})
        check(f"B_L{L}", ok, f"L={L}: (S)+(W)+(Z) with all other Lam_n FREE -> Groebner basis = [1] (no such Lie algebra over C; {nv} vars, {dt:.1f}s)")
    # without (Z), small L: what survives?
    for L in range(5, min(Lmax, 8) + 1):
        ok, nv, dt = inconsistent(L, {1: 1, 2: 2}, require_Z=False)
        check(f"BnoZ_L{L}", ok, f"L={L}: (S)+(W) WITHOUT (Z) also inconsistent ({nv} vars, {dt:.1f}s)")
    # continuum-like spectrum Lam_n = nbar (SLAC-like), L odd: inconsistent for L >= 5 even without (Z) being separately imposed
    for L in [l for l in (5, 7, 9) if l <= Lmax]:
        lf = {n: (n if n <= L // 2 else n - L) for n in range(1, L)}
        ok, nv, dt = inconsistent(L, lf, require_Z=False)
        check(f"SLAC_L{L}", ok, f"L={L}: Lam_n = nbar (the SLAC/continuum spectrum on the whole zone) -> inconsistent ({nv} vars, {dt:.1f}s)")
    # half-odd quantisation check at L=5: Lam_2 free, (S)+(Z): eliminate to the univariate polynomial in lam2
    eqs, vars_ = system(5, {1: 1, 4: -1})
    lam2 = sp.Symbol("lam2")
    others = [v for v in vars_ if v != lam2]
    G = sp.groebner(eqs, *others, lam2, order="lex", domain="QQ")
    uni = [g for g in G.exprs if g.free_symbols <= {lam2}]
    roots = sorted(set(sp.solve(uni[0], lam2))) if uni else None
    check("Q_L5", uni and set(roots) <= {sp.Rational(1, 2), sp.Rational(-1, 2)},
          f"L=5, (S)+(Z), Lam_2 free: elimination ideal in lam2 = {uni[0] if uni else None} -> 2*Lam_2/Lam_1 in {{+-1}} (odd), as Theorem B predicts")
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
