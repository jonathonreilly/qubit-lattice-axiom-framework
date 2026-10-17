"""Pair test (C2 eigenvalue lambda of a fermion pair at x, Rx) for EVERY
(code class, stabilizing vertex C2), using, for each, an ordering in the class
whose plaquette generators are mapped exactly onto plaquette generators by P_R
(so that P_R preserves the encoded fermion Fock space / H_sigma is symmetric).
The signed groups are ordering-independent within a class (checked in
check_rep_independence.py), so this is the same code and the same P_R.
lambda = theta_f * eta_f(C2,C2) = -eta_f.  Also translated C2 (axes without
vertices).  L = 6."""
import itertools, json
from collections import Counter, defaultdict
from pauli_bksf import *
from pair_test import path_ops, dagger, signed_sign, axis_type
import pair_test

L = 6; lat = Lattice(L); pair_test.L = L
lat4 = Lattice(4)
classes = {}
for order in itertools.permutations(range(6)):
    code = Code(lat4, order)
    key = Span([g for _, g in code.generators()], lat4.n).canonical_basis()
    classes.setdefault(key, []).append(order)
ROTS = rotations()
summary = Counter()
nosym = []
for ci, orders in enumerate(classes.values()):
    code0 = Code(lat, orders[0])
    gens0 = [g for _, g in code0.generators()]
    sp0 = Span(gens0, lat.n)
    base0 = list(range(lat.nv)) [:1] + [lat.nv + 0, lat.nv + 1, lat.nv + 2]
    stab = [M for M in ROTS if order_of(M) == 2 and all(sp0.decompose(permute_pauli(gens0[i], edge_perm(lat, M))) is not None for i in base0)]
    for M in stab:
        perm = edge_perm(lat, M)
        found = None
        for o in orders:
            code = Code(lat, o)
            G = code.generators((0, 0, 0)); gens = [g for _, g in G]
            supp = set((g[0], g[1]) for g in gens)
            if all((lambda im: (im[0], im[1]) in supp)(permute_pauli(gens[i], perm)) for i in base0):
                found = o; break
        if found is None:
            nosym.append((orders[0], M)); summary[('no symmetric ordering in class',)] += 1; continue
        code = Code(lat, found)
        G = code.generators((0, 0, 0)); labels = [l for l, _ in G]; gens = [g for _, g in G]
        plaq_c = [l[2] if l[0] == 'P' else -1 for l in labels]
        sp = Span(gens, lat.n)
        hs = code.hop_signs(); h = tuple(next(iter(hs[c])) for c in range(3))
        s0 = tuple(0 if h[c] == 1 else 1 for c in range(3)); spi = tuple(1 - t for t in s0)
        for t in itertools.product([0, 1], repeat=3):
            at = axis_type(M, t)
            if at.startswith('screw'): continue
            permt = edge_perm(lat, M, t)
            for sname, s in (('flux0', s0), ('fluxpi', spi)):
                lams = set()
                for x in itertools.product(range(-2, 3), repeat=3):
                    Rx = tuple(matvec(M, x)[i] + t[i] for i in range(3))
                    if all((Rx[i] - x[i]) % L == 0 for i in range(3)): continue
                    if max(abs(((Rx[i] - x[i]) + L // 2) % L - L // 2) for i in range(3)) > 2: continue
                    S = path_ops(code, x, Rx)
                    O = pmul(dagger(S), permute_pauli(S, permt))
                    cb = sp.decompose(O)
                    if cb is None:
                        lams.add('not-in-group'); continue
                    sg, _ = signed_sign(sp, cb, plaq_c, s)
                    lams.add(sign_vs_canonical(O) / sg)
                kind = 'vertex-axis' if 'vertex' in at else at
                summary[(sname, kind, 'axisC2' if sum(abs(M[i][i]) for i in range(3)) == 3 else 'edgeC2', str(sorted(lams, key=str)))] += 1
for k, v in sorted(summary.items(), key=str):
    print(v, k)
print('pairs with no symmetric ordering:', len(nosym))
