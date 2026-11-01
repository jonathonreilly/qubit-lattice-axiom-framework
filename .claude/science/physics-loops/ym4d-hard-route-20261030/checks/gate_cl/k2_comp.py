#!/usr/bin/env python3
"""K2 of CRITERIA.md: (COMP)(ii) ratio from the logged runs of checks/gate_ex. Reads JSON only."""
import glob, json, os
here = os.path.dirname(os.path.abspath(__file__))
for fn in sorted(glob.glob(os.path.join(here, "..", "gate_ex", "y_2_3_2_*.json"))):
    r = json.load(open(fn))["rows"]
    top = r[-1]
    I = top["a"] + top["f"] * top["E"]
    if I == 0:
        continue
    out = {len(r) - 1 - lev: row["a"] * 9.0 ** (len(r) - 1 - lev) / I for lev, row in enumerate(r)}
    print(os.path.basename(fn), {m: round(v, 3) for m, v in sorted(out.items())}, "f_top", round(top["f"], 4))
