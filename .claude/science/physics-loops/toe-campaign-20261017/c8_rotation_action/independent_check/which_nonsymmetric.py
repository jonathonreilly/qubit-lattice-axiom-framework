"""Which (code, stabilizing C2) admit an ordering in the class whose plaquette
generators are permuted exactly by P_R (needed for the fermionic computation)?
Classified by orbit type and C2 type. L = 4."""
import itertools
from collections import Counter
from pauli_bksf import *
lat = Lattice(4)
classes = {}
for order in itertools.permutations(range(6)):
    code = Code(lat, order)
    key = Span([g for _, g in code.generators()], lat.n).canonical_basis()
    classes.setdefault(key, []).append(order)
res = Counter()
for orders in classes.values():
    code0 = Code(lat, orders[0]); gens0 = [g for _, g in code0.generators()]; sp0 = Span(gens0, lat.n)
    stab = [M for M in rotations() if all(sp0.decompose(permute_pauli(g, edge_perm(lat, M))) is not None for g in gens0[:1] + gens0[lat.nv:lat.nv + 3])]
    otype = {6: 'D3', 4: 'order4', 2: 'C2only'}[len(stab)]
    for M in stab:
        if order_of(M) != 2: continue
        perm = edge_perm(lat, M)
        ctype = 'axisC2' if all(abs(M[i][i]) == 1 for i in range(3)) else 'edgeC2'
        nsym = 0
        for o in orders:
            gens = [g for _, g in Code(lat, o).generators()]
            supp = set((g[0], g[1]) for g in gens)
            if all((lambda im: (im[0], im[1]) in supp)(permute_pauli(g, perm)) for g in gens[:1] + gens[lat.nv:lat.nv + 3]):
                nsym += 1
        res[(otype, ctype, 'has symmetric ordering' if nsym else 'NO symmetric ordering')] += 1
for k, v in sorted(res.items()):
    print(v, k)
