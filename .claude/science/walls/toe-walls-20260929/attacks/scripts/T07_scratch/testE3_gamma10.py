import json, numpy as np
import testB_protocol as B
for m in B.models.values(): m.cap = 1e5
out = []
for nm in ['1 width x2 (prob width 2.1)', '2 width x0.4', '5 point mass at (12,12)']:
    out.append(B.analyse(nm, B.starts[nm], gamma=10.0))
json.dump(out, open('testE3_results.json', 'w'), indent=1)
