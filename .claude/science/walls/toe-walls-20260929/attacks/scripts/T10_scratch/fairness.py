"""Fairness checks: (1) beam redundancy with the same window cap as the sea scan (<=8, <=12);
(2) sea: how information in windows adjacent to the pointer (pointer site excluded) grows with window length (m up to 12)."""
import json
import numpy as np
import beam_vs_sea as b
from gauss import holevo
from gauss_trunc import holevo_trunc

out = {}
# (1) beam, proj g=20, windows capped
L = 300; h = b.chain_h(L); j0 = 110
for NB in (1, 2, 3, 4):
    Phi0 = b.packets(L, j0, NB, sigma=2.0, spacing=12, first=8)
    Pu = b.evolve(h, j0, 20.0, Phi0, 44.0); Pd = b.evolve(h, j0, 0.0, Phi0, 44.0)
    Du, Dd = b.corr(Pu), b.corr(Pd)
    for cap in (8, 12, 18):
        tab = {}
        for i in range(1, L - 20):
            for m in range(1, cap + 1):
                a, c = Du[i:i+m, i:i+m], Dd[i:i+m, i:i+m]
                if np.linalg.norm(a - c) < 1e-7: tab[(i, m)] = 0.0; continue
                chi, lost = holevo_trunc(a, c, K=4, maxpart=10)
                if lost < 1e-6: tab[(i, m)] = chi
        r5 = len(b.disjoint_count(tab, 0.5)); r9 = len(b.disjoint_count(tab, 0.9)); r3 = len(b.disjoint_count(tab, 0.3))
        out[f"beam NB={NB} cap={cap}"] = dict(R0_9=r9, R0_5=r5, R0_3=r3, maxchi=round(max(tab.values()), 3))
        print(f"beam NB={NB} cap={cap}: R(.9)={r9} R(.5)={r5} R(.3)={r3} max chi={max(tab.values()):.3f}", flush=True)
# (2) sea growth of adjacent windows
L = 120; j0 = 60; h = b.chain_h(L)
e, U = np.linalg.eigh(h); Phi0 = U[:, :L // 2]
for g, coup in ((20.0, "proj"), (3.0, "proj")):
    Vu, Vd = (g, 0.0)
    Pu = b.evolve(h, j0, Vu, Phi0, 15.0); Pd = b.evolve(h, j0, Vd, Phi0, 15.0)
    Du, Dd = b.corr(Pu), b.corr(Pd)
    row = {}
    for m in (2, 4, 6, 8, 10, 12):
        right = holevo(Du[j0+1:j0+1+m, j0+1:j0+1+m], Dd[j0+1:j0+1+m, j0+1:j0+1+m])
        left = holevo(Du[j0-m:j0, j0-m:j0], Dd[j0-m:j0, j0-m:j0])
        row[m] = (round(left, 3), round(right, 3))
    out[f"sea g={g} adjacent windows (left,right) by length"] = row
    print(f"sea g={g} adjacent windows (left,right) chi by length:", row, flush=True)
json.dump(out, open("fairness_results.json", "w"), indent=1)
