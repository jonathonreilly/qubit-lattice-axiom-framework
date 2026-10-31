#!/usr/bin/env python3
"""Lemma EX Step 1 says the hypercubic average leaves the sum unchanged. With a comb of one fixed axis order the block map is not covariant under axis permutations.
Measure: e(V) against e(g V), g a permutation of axes, on constant links; the spread over the 24 permutations, against f E. Report only: no pass or fail registered."""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ex_core import *
L = 3
base = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
for a in [0.2, 0.08]:
    es = []
    for perm in itertools.permutations(range(4)):
        V = constant_links([base[p] for p in perm], a)
        ch = Chain(1, L, 4, 1)
        pb = Problem(ch, V)
        U, lam, gn, rn = pb.solve(pb.initial())
        es.append(float(wilson(U) - wilson(V)))
    f, E = flux_stats(V)
    es = np.array(es)
    print(f"a={a} f={f:.5f} e mean={es.mean():.6e} spread={es.max()-es.min():.3e} spread/e={(es.max()-es.min())/es.mean():.4f} spread/(f E)={(es.max()-es.min())/(f*E):.5f} spread/(f^2 E)={(es.max()-es.min())/(f*f*E):.4f}", flush=True)
