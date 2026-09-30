"""Kill-check extension (planar S1 sector): add the lapse-momentum bracket {G[xi],C[N]} = C[xi |> N] at the orders where G2, V2, T3 enter,
to the attack's degree-2 {C,C} identity, with the ADM-matched continuum limit. The map's A1 does not ask for this; it is the natural companion
and it uses the SAME unknowns (G2, V2, T3), so it shows whether the pass survives once G2 is tied to relabelling covariance.
Equations (all strict, sign fixed by {C[N],G[xi]} = -C[xi N'] for a density; control: opposite sign must fail):
  P^0 h^1 sector :  {G2[xi],C1[N]} + {G1[xi],V2[N]} = C1[xi|>N]
  P^2 h^0 sector :  {G2[xi],T2[N]} + {G1[xi],T3[N]} = T2[xi|>N]
  (xi|>N)(n) = sum_ab ell_ab xi(n+a) N(n+b), matched to xi N' : sum_b ell_ab = 0 for all a ; sum_ab b*ell_ab = s (s=+1)
"""
import sys, time
import numpy as np
from fractions import Fraction as F
import solve, solve2, model
from model import *
from solve import to_mod, rref_mod, PRIMES

def Xv(p): return ('X', 0, p)

def G1X():
    out = {}
    add(out, (Xv(0), V('P', XX, 0)), F(2)); add(out, (Xv(-1), V('P', XX, 0)), F(-2))
    return out

def G2X(u):
    c, d, i, j = u
    return {canon((Xv(0), V('P', c, i), V('h', d, j))): F(1)}

def Y_terms(a, b):
    """(xi|>N) anchored at n=0: xi(a) N(b)"""
    return [(Xv(a), V('N', 0, b))]

def C1_of_Y(a, b, k=K):
    out = {}
    for (xa, nb) in Y_terms(a, b):
        base = (xa, nb)
        for c in (YY, ZZ):
            add(out, shift_generic(base, 1) + (V('h', c, 0),), -k)
            add(out, base + (V('h', c, 0),), 2 * k)
            add(out, shift_generic(base, -1) + (V('h', c, 0),), -k)
    return out

def shift_generic(mono, u):
    return tuple(sorted((k, c, p + u) for (k, c, p) in mono))

def T2_of_Y(a, b, alpha=ALPHA, c=CC):
    out = {}
    pre = 1 / (4 * alpha)
    base = (Xv(a), V('N', 0, b))
    for aa in COMPS:
        add(out, base + (V('P', aa, 0), V('P', aa, 0)), pre * (1 - c))
    import itertools
    for aa, bb in itertools.combinations(COMPS, 2):
        add(out, base + (V('P', aa, 0), V('P', bb, 0)), pre * (-2 * c))
    return out

def build_GC(R, s=1, gc_norm=True):
    cols, rows, entries, b = solve.build(R, 'full')
    nc0 = len(cols)
    rows = dict(rows); entries = list(entries); b = dict(b)
    def rid(key):
        if key not in rows: rows[key] = len(rows)
        return rows[key]
    G1 = G1X()
    T2N = T2('N'); C1N = C1('N')
    # existing unknown columns contribute to GC rows
    for j, (lab, d) in enumerate(cols):
        fam, u = lab
        gc = {}
        if fam == 'G2':
            # note: in solve.build the G2 column was scaled by -1 (moved to LHS); the physical G2 coefficient = +x_u
            g2 = G2X(u)
            gc = fadd(bracket(g2, C1N), bracket(g2, T2N))
        elif fam == 'V2':
            gc = bracket(G1, V2_of(u, 'N'))
        elif fam == 'T3':
            gc = bracket(G1, T3_of(u, 'N'))
        for mono, cf in gc.items():
            entries.append((rid(('GC', mono)), j, cf))
    # ell columns
    ell = [(a, bb) for a in range(-R, R + 1) for bb in range(-R, R + 1)]
    jbase = nc0
    for k_, (a, bb) in enumerate(ell):
        gc = fadd(C1_of_Y(a, bb), T2_of_Y(a, bb))
        for mono, cf in gc.items():
            entries.append((rid(('GC', mono)), jbase + k_, -cf))
    # ell continuum conditions (rows)
    for a in range(-R, R + 1):
        r = rid(('ELL0', a))
        for k_, (aa, bb) in enumerate(ell):
            if aa == a: entries.append((r, jbase + k_, F(1)))
    r = rid(('ELL1',))
    for k_, (aa, bb) in enumerate(ell):
        if bb != 0: entries.append((r, jbase + k_, F(bb)))
    b[r] = F(s)
    cols2 = cols + [(('ell', (a, bb)), None) for (a, bb) in ell]
    return cols2, rows, entries, b, nc0

def solve_sys(cols, rows, entries, b, match=True, verbose=True, fams=('V2', 'T3', 'G2', 'xi1', 'chi')):
    nr0 = len(rows)
    entries = list(entries); b = dict(b)
    if match:
        mrows = solve2.match_rows([c for c in cols if c[1] is not None or c[0][0] != 'ell'], fams)
        for r, (row, rhs) in enumerate(mrows):
            ri = nr0 + r
            for j, v in row.items(): entries.append((ri, j, v))
            if rhs != 0: b[ri] = rhs
        nr = nr0 + len(mrows)
    else:
        nr = nr0
    nc = len(cols)
    A = np.zeros((nr, nc)); bb = np.zeros(nr)
    for i, j, c in entries: A[i, j] += float(c)
    for i, c in b.items(): bb[i] = float(c)
    sol = np.linalg.lstsq(A, bb, rcond=None)
    resid = float(np.linalg.norm(A @ sol[0] - bb))
    M = np.zeros((nr, nc + 1), dtype=np.int64)
    p = PRIMES[0]
    for i, j, c in entries:
        M[i, j] = (M[i, j] + (c.numerator % p) * pow(c.denominator % p, -1, p)) % p
    for i, c in b.items():
        M[i, nc] = (c.numerator % p) * pow(c.denominator % p, -1, p) % p
    rk, cons, piv, Mred = rref_mod(M, p, nc)
    return dict(rows=nr, cols=nc, float_resid=resid, bnorm=float(np.linalg.norm(bb)), rank_mod=rk, mod_consistent=cons)

if __name__ == '__main__':
    R = int(sys.argv[1]); t0 = time.time()
    for s, label in ((1, 's=+1 (expected sign)'), (-1, 's=-1 (control: opposite sign)')):
        cols, rows, entries, b, nc0 = build_GC(R, s=s)
        print(f"R={R} {label}: GC-augmented, identity+GC rows only (no ADM match):", solve_sys(cols, rows, entries, b, match=False), round(time.time() - t0, 1), flush=True)
        print(f"R={R} {label}: GC-augmented WITH ADM match:", solve_sys(cols, rows, entries, b, match=True), round(time.time() - t0, 1), flush=True)
