#!/usr/bin/env python3
"""C4 step 6: radius-2 extension (images of single-site Paulis supported in {-2..2}^3, 125 sites)
for the O-covariant classification under the soldered actions (axis, full) and sign-f.
Exhaustive by the split enumerator (exact F2 elimination + exact filters); conditions over all
translates t in {-4..4}^3.  The trivial and sign actions are not run at radius 2 (dim 40, and
they already admit spreading QCAs at radius 1)."""
import os
import sys
import time
os.environ['C4_RADIUS'] = '2'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c4lib as L

P = F = 0


def check(name, ok):
    global P, F
    if ok:
        P += 1
        print('PASS', name, flush=True)
    else:
        F += 1
        print('FAIL', name, flush=True)


D = L.D
check('radius 2 geometry: 125 sites, 729 shifts', L.NC == 125 and len(L.SHIFTS) == 729)
OG = L.SUBGROUPS['O']
Hf = L.G([[-1, 0, 0], [0, 0, 1], [0, 1, 0]])
REP = {a: tuple(L.menu_hom(a)) for a in ('axis', 'full')}
REP['sign-f'] = tuple(L.ID if L.perm_sign(L.O[R]) == 1 else Hf for R in range(24))
for nm in os.environ.get('C4_ACTIONS', 'full,axis,sign-f').split(','):
    h = REP[nm]
    B = L.covariance_space(h, h, OG)
    t0 = time.time()
    uns = L.enumerate_solutions_split(B)
    dt = time.time() - t0
    Ms = [L.matrix_of(s) for s in uns]
    check(f'r2/{nm}: all {len(uns)} solutions symplectic with det 1', all(L.is_symplectic(M) and L.det(M) == L.ONE for M in Ms))
    signed = [(s, sx, sz) for s in uns for sx in (1, -1) for sz in (1, -1)
              if L.signed_covariant(L.pstr_from_vec(s[:D], sx), L.pstr_from_vec(s[D:], sz), h, h, OG)]
    onsite = sum(all(e == (0, 0, 0) for i in range(2) for j in range(2) for e in M[i][j]) for M in Ms)
    ntr = sum(L.trace(M) not in (L.ZERO, L.ONE) for M in Ms)
    print(f'  r2/{nm}: dim W = {B.shape[0]}, unsigned {len(uns)}, signed {len(signed)}, on-site {onsite}, '
          f'nonconstant trace {ntr}  ({dt:.0f}s)')
    if nm in ('axis', 'full'):
        check(f'r2/{nm}: the only O-covariant radius-2 one-qubit Clifford QCA is the identity',
              len(uns) == 1 and onsite == 1 and len(signed) == 1 and signed[0][1:] == (1, 1))
    else:
        check(f'r2/{nm}: no solution has nonconstant trace (all periodic)', ntr == 0)
print(f'TOTAL: PASS={P} FAIL={F}')
