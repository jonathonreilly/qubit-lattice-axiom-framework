#!/usr/bin/env python3
"""Print a markdown table of R(f) from lane946/out/*.json (row 946). GUIDE only."""
import json, sys, glob, os
here = os.path.dirname(os.path.abspath(__file__))
files = sys.argv[1:] or sorted(glob.glob(os.path.join(here, "out", "*.json")))
print("| run | f | R | err (jackknife) | R + 3 err | exact | num | den | outer lag1 |")
print("|---|---|---|---|---|---|---|---|---|")
for fn in files:
    d = json.load(open(fn))
    tag = d["args"]["tag"]
    for name, e in d["R"].items():
        ex = "%.5g" % e["exact"] if "exact" in e else ""
        lag = "%.2f" % e["outer_lag1"] if e.get("outer_lag1") is not None else ""
        print(f"| {tag} | {name} | {e['R']:.4g} | {e['err']:.2g} | {e['R'] + 3 * e['err']:.4g} | {ex} | "
              f"{e['num']:.4g} | {e['den']:.4g} | {lag} |")
    print(f"| {tag} | tau_inner | {d['tau_inner']} | | | | | | |")
