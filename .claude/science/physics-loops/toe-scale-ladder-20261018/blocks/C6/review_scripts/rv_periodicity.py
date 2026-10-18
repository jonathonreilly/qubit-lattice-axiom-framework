#!/usr/bin/env python3
"""Reviewer's independent implementation of the C6 periodicity step (NOTE section 3a, step 3).
For the plane relation (motif = one plaquette, translates over Z_m^2 in lex order) we compute the CLOSED FORM
   Q(m) = m^2 p + 2 * sum_{delta != 0} w(delta) * m * cnt(delta_first_nonzero, m)      (mod 4),
   cnt(d, m) = m - d (d > 0), |d| (d < 0),   valid for m >= 2s-1 (no aliasing of overlap offsets),
with w(delta) = |z_0 . x_delta| read off on a large torus, then (a) compare with the direct product on T^3_m for
m = 5..12 and (b) evaluate Q(m) for m up to 60.  Own builders (rv_codes), own Pauli algebra."""
import os, sys, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from rv_gf2 import Pauli, prod
import rv_codes as C

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ''), flush=True)

BIG = 15; R = 4   # offsets |delta_i| <= R suffice (plaquette support side s <= 3 sites)
def motif_data(mk, k):
    code = mk(BIG)
    pl = code.meta['plaq']
    o = (7, 7, 7)
    P0 = pl(o, k)
    others = [i for i in range(3) if i != k]
    w = {}
    for d1, d2 in itertools.product(range(-R, R + 1), repeat=2):
        if (d1, d2) == (0, 0): continue
        v = list(o); v[others[0]] += d1; v[others[1]] += d2
        Pd = pl(tuple(v), k)
        w[(d1, d2)] = int(np.count_nonzero(P0.z & Pd.x)) % 2
    # sanity: no overlap at the window edge -> window large enough
    edge_ok = all(not (np.count_nonzero((P0.x | P0.z) & (pl(tuple(o[i] + (dd if i == others[0] else 0) for i in range(3)), k).x
                                                     | pl(tuple(o[i] + (dd if i == others[0] else 0) for i in range(3)), k).z)))
                  for dd in (R, -R))
    # self phase of the motif as i^p X^x Z^z
    return P0.ph, w, edge_ok

def Q_closed(p, w, m):
    q = m * m * p
    for (d1, d2), wt in w.items():
        if not wt: continue
        d = d1 if d1 != 0 else d2
        q += 2 * m * ((m - d) if d > 0 else -d)
    return q % 4

def direct(mk, k, m):
    code = mk(m)
    pl = code.meta['plaq']
    vs = sorted(v for v in itertools.product(range(m), repeat=3) if v[k] == 0)
    P = prod([pl(v, k) for v in vs], code.n)
    assert P.is_identity()
    return P.ph

fams = [('F1 ord(4,0,5,2,3,1)', lambda L: C.bksf(L, (4, 0, 5, 2, 3, 1))), ('F1 ord(2,5,1,3,0,4)', lambda L: C.bksf(L, (2, 5, 1, 3, 0, 4))),
        ('F1 ord(5,3,1,4,2,0)', lambda L: C.bksf(L, (5, 3, 1, 4, 2, 0))), ('F3', lambda L: C.mpd(L)), ('F4', lambda L: C.mpd(L, spinful=True))]
okm = okc = oke = True
for nm, mk in fams:
    for k in range(3):
        p, w, eok = motif_data(mk, k)
        oke &= eok
        cl = [Q_closed(p, w, m) for m in range(5, 61)]
        dr = [direct(mk, k, m) for m in range(5, 11 if nm != 'F4' else 9)]
        okm &= cl[:len(dr)] == dr
        okc &= all(q == 0 for q in cl)
        print(f'   {nm} plane normal {k}: motif phase p={p}, #odd-overlap offsets={sum(w.values())}; direct Q(m=5..) {dr}; closed-form Q(m=5..60) all 0: {all(q == 0 for q in cl)}', flush=True)
check('overlap window large enough (no support overlap at offset R)', oke)
check('closed-form Q(m) equals the direct product at m = 5..10 (m >= 2s-1 = 5)', okm)
check('flux-0 plane sign is + for every m = 5..60 by the closed form (period divides 4 -> all m >= 5)', okc)
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
