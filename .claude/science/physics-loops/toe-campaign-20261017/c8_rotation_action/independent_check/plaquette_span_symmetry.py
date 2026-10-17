"""Coordinator's caveat check: for each ordering o of each code, which rotations
R in O satisfy span(S^{R o}) = span(S^o) (plaquette generators only, unsigned,
L = 4)? Since P_R S^o P_R^-1 = S^{R o} exactly, this is P_R preserving span(S^o).
Also record the stronger 'exact permutation of plaquette supports'."""
import itertools
from collections import Counter
from pauli_bksf import *
lat = Lattice(4)
ROTS = rotations(); PERMS = [edge_perm(lat, M) for M in ROTS]
classes = {}
for order in itertools.permutations(range(6)):
    code = Code(lat, order)
    key = Span([g for _, g in code.generators()], lat.n).canonical_basis()
    classes.setdefault(key, []).append(order)
def ctype(M):
    o = order_of(M)
    if o == 1: return 'id'
    if o == 2: return 'axisC2' if all(abs(M[i][i]) == 1 for i in range(3)) else 'edgeC2'
    return 'C%d' % o
summary = Counter(); per_class = Counter()
for orders in classes.values():
    c0 = Code(lat, orders[0]); g0 = [g for _, g in c0.generators()]; sp0 = Span(g0, lat.n)
    b0 = g0[:1] + g0[lat.nv:lat.nv + 3]
    stab = [i for i, p in enumerate(PERMS) if all(sp0.decompose(permute_pauli(g, p)) is not None for g in b0)]
    otype = {6: 'D3', 4: 'order4', 2: 'C2only'}[len(stab)]
    c2_hits = Counter()
    for o in orders:
        code = Code(lat, o)
        plaq = [g for lab, g in code.generators() if lab[0] == 'P']
        spP = Span(plaq, lat.n)
        supp = set((g[0], g[1]) for g in plaq)
        pres = []; exact = []
        for i in stab:
            ims = [permute_pauli(g, PERMS[i]) for g in plaq[:3]]  # translation reps suffice
            if all(spP.decompose(im) is not None for im in ims):
                pres.append(ctype(ROTS[i]) + ('' if ctype(ROTS[i]) in ('id',) else str(i)))
            if all((im[0], im[1]) in supp for im in ims):
                exact.append(ctype(ROTS[i]))
        summary[(otype, 'preserving span(S^o)', tuple(sorted(p.rstrip('0123456789') for p in pres)), 'exact perm', tuple(sorted(exact)))] += 1
        for p in pres:
            if p.startswith('edge') or p.startswith('axis'): c2_hits[p] += 1
    per_class[(otype, tuple(sorted(c2_hits.values())))] += 1
for k, v in sorted(summary.items()):
    print(v, 'orderings:', k)
print('per class: (type, how many orderings each preserved C2 serves) -> #classes')
for k, v in sorted(per_class.items()):
    print(' ', v, k)
