#!/usr/bin/env python3
"""Cheap independent geometry checks using only this checker's literal hops."""
from check import ROOT, VAC, neighbors2, adjacent, pair_operator, gauss, OUT
from collections import Counter
import json

counts=Counter(); diagonal_sum=0
for c in neighbors2(ROOT):
    shared=len(set(adjacent(ROOT))&set(adjacent(c)))
    p=Counter()
    for m,w in pair_operator(VAC,(),ROOT,c):
        assert m==VAC and gauss(m,w)
        p[w]+=1
    assert p[()]==36-shared
    nonzero={w:n for w,n in p.items() if w}
    assert len(nonzero)==shared*(shared-1)
    assert all(n==1 and len(w)==4 and all(abs(v)==1 for e,v in w)
               for w,n in nonzero.items())
    for w,n in nonzero.items():
        assert nonzero[tuple((e,-v) for e,v in w)]==n
    counts[shared]+=1;diagonal_sum+=p[()]
assert dict(counts)=={1:6,2:12}
assert diagonal_sum==618
r={'partners_by_shared_B':dict(counts),'diagonal_sum_per_A':diagonal_sum,
   'H4_pre_scalar_over_N':-diagonal_sum,'unoriented_plaquettes_per_N':6,
   'edges_per_N':6,'plaquette_incidence_per_edge':4,
   'norm_V_upper_over_N':24}
(OUT/'prebirth_geometry.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
