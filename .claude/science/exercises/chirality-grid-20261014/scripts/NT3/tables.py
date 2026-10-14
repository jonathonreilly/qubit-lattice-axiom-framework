"""Collect primary JSON outputs into the decision tables (PREREG rules U/S/G/O, literal) and D2 scaling."""
import json, glob
import numpy as np
from filters import ring_fvals

R = {}
for fn in sorted(glob.glob("primary_*.json")):
    R.update(json.load(open(fn)))
out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

P("filter L | E0/site | D | singlet(raise) | gap | gap6 | gap_light(pre-reg metric) | S6S(0) | S6M(0) | chi6S/site | chi6M/site | f_near | gap6/f_near^2 | gap6/f_near^4")
for name in ("C1", "F_lo", "F_star", "F_hi"):
    for L in (3, 4, 5, 6, 7):
        k = f"{name}|{L}"
        if k not in R:
            continue
        r = R[k]; fn = ring_fvals(name, L)[1]
        P(f"{name:6s} {L} | {r['E0']/L:.5f} | {int(r['D'])} | {r['raise_norm']:.1e} | {r['gap']:.6f} | {r['gap6']:.6f} | "
          f"{r['gap_light']:.6f} | {r['S6_S_q0']:.4f} | {r['S6_M_q0']:.4f} | {r['chi6_S_perSite']:.3f} | {r['chi6_M_perSite']:.3f} | "
          f"{fn:.4f} | {r['gap6']/fn**2:.4f} | {r['gap6']/fn**4:.4f}")
for name in ("f_NN", "f_F1"):
    k = f"cube|{name}"
    if k in R:
        r = R[k]
        P(f"cube {name} | {r['E0']/8:.5f} | {int(r['D'])} | {r['raise_norm']:.1e} | {r['gap']:.6f} | {r['gap6']:.6f} | - | "
          f"{r['S6_S_q0']:.4f} | {r['S6_M_q0']:.4f} | {r['chi6_S_perSite']:.3f} | {r['chi6_M_perSite']:.3f}")

P("\nLiteral PREREG rules over L = 4..Lmax:")
for name in ("C1", "F_lo", "F_star", "F_hi"):
    Ls = [L for L in (4, 5, 6, 7) if f"{name}|{L}" in R]
    rr = [R[f"{name}|{L}"] for L in Ls]
    U = all(int(r["D"]) == 1 for r in rr)
    S = all(r["raise_norm"] < 1e-8 for r in rr)
    gnl = [r["gap_nl"] for r in rr]
    G = all(g >= 0.1 for g in gnl) and gnl[-1] / gnl[-3] >= 0.6
    s6S = rr[-1]["S6_S_q0"] / rr[0]["S6_S_q0"]; s6M = rr[-1]["S6_M_q0"] / rr[0]["S6_M_q0"]
    cS = rr[-1]["chi6_S_perSite"] / rr[0]["chi6_S_perSite"]; cM = rr[-1]["chi6_M_perSite"] / rr[0]["chi6_M_perSite"]
    g6 = [r["gap6"] for r in rr]
    tower = all(g6[i + 1] < g6[i] for i in range(len(g6) - 1)) and g6[-1] < 0.5 * g6[0]
    O = s6S < 1.4 and s6M < 1.4 and cS < 1.4 and cM < 1.4 and not tower
    P(f"{name}: L={Ls} U={U} S={S} G={G} (gap_nl={np.round(gnl, 5).tolist()}) "
      f"S6 ratios S/M = {s6S:.3f}/{s6M:.3f}; chi ratios S/M = {cS:.3f}/{cM:.3f}; gap6 = {np.round(g6, 5).tolist()} tower={tower} -> O={O}")
    lit = "TG1-SYMMETRIC" if (U and S and G and O) else ("TG1-BROKEN" if (not U or not S or not O or not G) else "OPEN")
    P(f"   literal per-filter reading: {lit}")
open("tables.out", "w").write("\n".join(out) + "\n")
