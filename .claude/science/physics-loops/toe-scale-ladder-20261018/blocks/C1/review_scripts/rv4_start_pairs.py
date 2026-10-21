#!/usr/bin/env python3
"""Reviewer check R4: recompute the start-consistency chi2 of NOTE 5.3 (10 pairs, V=0, L>=8, E_mix/N_p per chain,
values typed from data/per_chain.md) and the L=6 T=12 three-start scatter."""
import numpy as np
RES = []
def check(n, ok, d=""):
    RES.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {n}" + (f" :: {d}" if d else ""), flush=True)
P = {  # (L,T,W): [(E, se), (E, se)]
 (8,16,0): [(-0.28893,0.00006),(-0.28885,0.00008)], (8,16,1): [(-0.28883,0.00008),(-0.28874,0.00009)],
 (8,32,0): [(-0.28904,0.00009),(-0.28886,0.00011)], (8,32,1): [(-0.28872,0.00008),(-0.28876,0.00009)],
 (10,20,0): [(-0.28884,0.00006),(-0.28874,0.00007)], (10,20,1): [(-0.28867,0.00005),(-0.28885,0.00006)],
 (10,40,0): [(-0.28888,0.00007),(-0.28889,0.00010)], (10,40,1): [(-0.28895,0.00007),(-0.28872,0.00008)],
 (12,24,0): [(-0.28884,0.00007),(-0.28883,0.00006)], (12,24,1): [(-0.28872,0.00007),(-0.28869,0.00007)]}
tot = 0; zs = {}
for k, ((a, sa), (b, sb)) in P.items():
    z = (a - b) / np.hypot(sa, sb); zs[k] = z; tot += z * z
print("[INFO] pair z:", {k: round(v, 2) for k, v in zs.items()})
print(f"[INFO] with the 5-decimal per_chain.md inputs: chi2 = {tot:.2f}/10 (rounding moves z by ~0.1-0.2)")
import json, os
rows = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "summary.json")))
Q = {}
for r in rows:
    if r["V"] == 0.0 and r["L"] >= 8:
        Q.setdefault((r["L"], r["T"], int(r["seed"] >= 100)), []).append(r["E_mix_per_plaq"][:2])
zz = {k: (v[0][0] - v[1][0]) / np.hypot(v[0][1], v[1][1]) for k, v in Q.items() if len(v) == 2}
t2 = sum(z * z for z in zz.values())
big = sorted(zz.items(), key=lambda kv: -abs(kv[1]))[:2]
check("NOTE 5.3: 10 start pairs total chi2 12.8/10, two largest tensions W=1 L=10 at 2.1 and 2.0 sigma (full-precision summary.json)",
      len(zz) == 10 and abs(t2 - 12.8) < 0.05 and all(k[0] == 10 and k[2] == 1 for k, _ in big),
      f"chi2 = {t2:.2f}/{len(zz)}; largest {[(k, round(v, 2)) for k, v in big]}")
e = np.array([-0.28938, -0.28905, -0.28942]); s = np.array([0.00013, 0.00011, 0.00012])
m = (e / s**2).sum() / (1 / s**2).sum(); c2 = (((e - m) / s) ** 2).sum()
print(f"[INFO] L=6 T=12 W=0 three starts: chi2 = {c2:.2f}/2 (per-chain binned errors); spread {1e4*(e.max()-e.min()):.1f}e-4 per plaquette "
      f"= {(e.max()-e.min())*648:.2f} total, vs dE(L=6) = 0.44")
print(f"TOTAL: PASS={sum(RES)} FAIL={len(RES)-sum(RES)}")
