#!/usr/bin/env python3
"""W2 extras: enclosures at scaled offsets, and P_infinity at z = 0 for the L = 1 test."""
import json, os
import near_flux as nf
here = os.path.dirname(os.path.abspath(__file__))
out = []
print("P_infinity(0) Fourier", nf.fourier((0, 0, 0, 0)), flush=True)
for rho in (2, 3):
    for base in ((3, 3, 2, 2), (3, 3, 2, 4)):
        z = tuple(rho * a for a in base)
        lo, hi = nf.enclosure(z)
        fo = nf.fourier(z)
        out.append(dict(z=z, lo=float(lo), hi=float(hi), fourier=fo, inside=bool(lo <= fo <= hi)))
        print(out[-1], flush=True)
with open(os.path.join(here, "near_scaled.json"), "w") as f:
    json.dump(out, f, indent=1)
