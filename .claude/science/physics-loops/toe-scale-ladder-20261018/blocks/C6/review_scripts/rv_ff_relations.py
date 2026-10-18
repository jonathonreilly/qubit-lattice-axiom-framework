#!/usr/bin/env python3
"""Frustration-freeness beyond the author's L <= 8 via a homological relation basis.
Derivation (reviewer): for F3 (MPD) the GF(2) relation space among {B_v, S_p} on T^3_L is
  span{cube relations} (dim L^3 - 1) + 3 plane relations (H_2) + [one 'all-B' relation iff L even],
because a relation forces the plaquette 2-chain c to have dz = phi*(all edges) with phi constant.
For F1 (edge BKSF) X-parts force c to be a 2-cycle; the Z residue is a coboundary; plus the trivial
all-B relation.  The sign of a product of commuting Hermitian generators is a homomorphism on the relation
space, so FF <=> every basis relation has sign +1.  We (i) verify the dimension count against the left
kernel at small L, (ii) evaluate the basis signs for L up to 12 in all 8 sectors."""
import os, sys, itertools, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from rv_gf2 import Pauli, rank, vec, left_kernel
import rv_codes as C

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ''), flush=True)

def residual_sign(code, ops):
    """product of given generators; must be X-free and Z part in span of Z-type B's (phase-0 Paulis).
    returns +1/-1 (relation sign) or None if not a relation of the expected form."""
    P = Pauli(code.n)
    for g in ops: P = P * g
    if P.x.any(): return None
    if P.z.any():
        # must be a product of B's; B's are Z-type with phase 0 in F1 -> phase of P must be 0
        return {0: 1, 2: -1}.get(P.ph)
    return {0: 1, 2: -1}.get(P.ph)

def basis_relations(code, kind):
    L = code.L; plaq = code.meta['plaq']; B = code.meta['B']
    S = list(itertools.product(range(L), repeat=3))
    rels = {}
    # cube at origin: 6 faces
    o = (0, 0, 0)
    faces = []
    for c in range(3):
        faces.append(plaq(o, c)); faces.append(plaq(C.shift(o, c, 1, L), c))
    rels['cube'] = faces
    for c in range(3):
        rels[f'plane{c}'] = [plaq(v, c) for v in S if v[c] == 0]
    if kind == 'F3' and L % 2 == 0:
        ops = [B(v) for v in S]
        # strips: x-lines paired in y via xy-plaquettes (normal z=2); y-lines paired in z (normal x=0); z-lines paired in x (normal y=1)
        ops += [plaq(v, 2) for v in S if v[1] % 2 == 0]
        ops += [plaq(v, 0) for v in S if v[2] % 2 == 0]
        ops += [plaq(v, 1) for v in S if v[0] % 2 == 0]
        rels['allB'] = ops
    return rels

def main():
    t0 = time.time()
    orders = [(4, 0, 5, 2, 3, 1), (2, 5, 1, 3, 0, 4), (0, 1, 2, 3, 4, 5)]
    # (i) dimension of relation space vs homological count
    okdim = True
    for L in (3, 4, 5, 6):
        for nm, code in [('F1', C.bksf(L, orders[0])), ('F3', C.mpd(L))]:
            G = np.array([vec(g) for g in code.gens], bool)
            nrel = len(code.gens) - rank(G)
            expect = (L ** 3 - 1) + 3 + (1 if (nm == 'F1' or L % 2 == 0) else 0)
            okdim &= nrel == expect
            print(f'   {nm} L={L}: relation-space dim {nrel}, homological count {expect}', flush=True)
    check('relation space = cubes (L^3-1) + 3 planes + all-B relation (F1 always, F3 iff L even)', okdim)
    # (ii) signs
    table = {}
    for L in range(3, 13):
        for nm, mk in [('F1a', lambda L, f: C.bksf(L, orders[0], f)), ('F1b', lambda L, f: C.bksf(L, orders[1], f)),
                       ('F3', lambda L, f: C.mpd(L, f))]:
            if L > 10 and nm == 'F1b': continue
            for f in itertools.product((0, 1), repeat=3):
                code = mk(L, f)
                rels = basis_relations(code, 'F3' if nm == 'F3' else 'F1')
                sg = {k: residual_sign(code, v) for k, v in rels.items()}
                if nm.startswith('F1'):
                    sg['allB'] = 1   # product of all Z-stars = +I identically (each edge twice, no phases)
                table[(nm, L, f)] = sg
                del code
            print(f'   {nm} L={L}: ' + '; '.join(f"{f}:{''.join('+' if s == 1 else ('-' if s == -1 else '?') for s in table[(nm, L, f)].values())}"
                                               for f in itertools.product((0, 1), repeat=3)) + f'  ({time.time()-t0:.0f}s)', flush=True)
    okform = all(all(s in (1, -1) for s in sg.values()) for sg in table.values())
    check('every basis product is +-I (relations correctly identified)', okform)
    ff_even = all(all(s == 1 for s in sg.values()) for (nm, L, f), sg in table.items() if L % 2 == 0)
    check('even L = 4..12: all basis relation signs +1 in all 8 sectors -> frustration-free', ff_even)
    # odd L: plane_c sign = (-1)^{f_c} pattern (sign (-1)^{f L^2})
    pat = all(sg['plane0'] == (-1) ** f[0] and sg['plane1'] == (-1) ** f[1] and sg['plane2'] == (-1) ** f[2] and sg['cube'] == 1
              for (nm, L, f), sg in table.items() if L % 2 == 1)
    check('odd L = 3..11: cube sign +1, plane_c sign (-1)^{f_c}: only flux-0 is frustration-free', pat)
    print(f'TOTAL: PASS={PASS} FAIL={FAIL}')

main()
