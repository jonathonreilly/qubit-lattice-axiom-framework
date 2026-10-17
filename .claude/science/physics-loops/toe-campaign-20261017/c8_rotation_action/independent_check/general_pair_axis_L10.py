"""General pair test for the 12 axis C2's (order-4 codes) with separation 4,
which needs L = 10 under minimal-image distances (at L = 8, axis-C2 pairs
have separation 2 or the ambiguous 4)."""
import sys
sys.argv = ["general_pair_test.py", "10"]
import json
from collections import Counter
import general_pair_test as gp
from pauli_bksf import Code, edge_perm, matvec, order_of, permute_pauli, rotations

lat = gp.lat
reps = [tuple(r) for r in json.load(open("reps_L4.json"))]
summary = Counter()
from pauli_bksf import Lattice, Span
lat4 = Lattice(4)
def has_axis_c2(r):
    c4 = Code(lat4, r); g4 = [g for _, g in c4.generators()]; s4 = Span(g4, lat4.n)
    return any(order_of(M) == 2 and all(abs(M[i][i]) == 1 for i in range(3)) and
               all(s4.decompose(permute_pauli(g, edge_perm(lat4, M))) is not None for g in g4[:1] + g4[lat4.nv:lat4.nv + 3])
               for M in rotations())
for ci, r in enumerate(reps):
    if not has_axis_c2(r):
        continue
    code = Code(lat, r)
    labels, gens, plaq_c, sp, sectors = gp.setup(code)
    base = [0, lat.nv, lat.nv + 1, lat.nv + 2]
    for M in rotations():
        if order_of(M) != 2 or not all(abs(M[i][i]) == 1 for i in range(3)):
            continue
        perm = edge_perm(lat, M)
        if not all(sp.decompose(permute_pauli(gens[i], perm)) is not None for i in base):
            continue
        res = Counter()
        for x in [(0, 2, 0), (0, 0, 2), (2, 0, 0), (1, 2, 1), (1, -2, 1), (2, 1, 1), (-1, 1, 2)]:
            Rx = matvec(M, x)
            if gp.dinf(x, Rx) != 4:
                continue
            out = gp.run_case(code, gens, labels, sp, plaq_c, sectors, M, (0, 0, 0), x, nsamples=4)
            if out is None:
                res["nosol"] += 1; continue
            lam, d, nn = out
            for sname, cnt in lam.items():
                for k, v in cnt.items():
                    res[(sname, d, k)] += v
        print(ci, r, M, dict(res), flush=True)
        for k, v in res.items():
            summary[k] += v
print("SUMMARY axis C2, L=10, separation 4:", dict(summary))
