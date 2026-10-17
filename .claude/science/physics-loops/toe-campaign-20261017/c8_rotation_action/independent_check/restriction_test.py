"""Is the restriction P_R|_D (permutation of the qubits inside an R-invariant
ball D around the fixed vertex, identity outside) a symmetry of the vacuum?
Count signed generators g whose image P_R|_D(g) is not in the signed group.
If the count is nonzero, P_R|_D creates excitations on the boundary of D, so
it is not a valid symmetry localization and '(P_R|_D)^n = 1' carries no
information about eta_f without a boundary repair. L = 8, flux-0 sector."""
import itertools
from collections import Counter
from pauli_bksf import *
from pair_test import signed_sign
L = 8; lat = Lattice(L)
import json
reps = [tuple(r) for r in json.load(open('reps_L4.json'))]
res = Counter()
for r in reps[:60:5]:
    code = Code(lat, r)
    G = code.generators(); labels = [l for l, _ in G]
    hs = code.hop_signs(); h = tuple(next(iter(hs[c])) for c in range(3))
    s0 = tuple(0 if h[c] == 1 else 1 for c in range(3))
    G = code.generators(s0); gens = [g for _, g in G]
    plaq_c = [l[2] if l[0] == 'P' else -1 for l in labels]
    sp = Span([g for _, g in code.generators()], lat.n)
    for M in rotations():
        if order_of(M) != 2: continue
        perm = edge_perm(lat, M)
        if not all(sp.decompose(permute_pauli(gens[i], perm)) is not None for i in [0, lat.nv, lat.nv + 1, lat.nv + 2]):
            continue
        def dist(v): return max(min(c % L, L - c % L) for c in v)
        Dv = set(lat.vid(v) for v in lat.verts() if dist(v) <= 2)
        pD = list(range(lat.n))
        for v in lat.verts():
            for a in range(3):
                e = lat.edge(v, a)
                if lat.vid(v) in Dv and lat.vid(lat.add(v, a)) in Dv:
                    pD[e] = perm[e]
        assert sorted(pD) == list(range(lat.n))
        bad = 0
        for g in gens:
            im = permute_pauli(g, pD)
            cb = sp.decompose(im)
            if cb is None:
                bad += 1; continue
            sg, _ = signed_sign(sp, cb, plaq_c, s0)
            if sg != sign_vs_canonical(im):
                bad += 1
        res[('generators not preserved by P_R|_D', bad)] += 1
print(dict(res))
