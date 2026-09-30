import os, json, numpy as np
import testB_protocol as B
for m in B.models.values(): m.cap = 1e5
out = []
for g in [10.0, 30.0]:
    for nm in ['3 shifted by 2', '6 correlated 1+0.5 sA sB']:
        out.append(B.analyse(nm, B.starts[nm], gamma=g))
json.dump(out, open('testE2_results.json', 'w'), indent=1)
