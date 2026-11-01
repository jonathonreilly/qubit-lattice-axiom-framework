"""Analyze SU(2) MC scan (evidence only, Wilson action, small volumes)."""
import json, glob, math
import numpy as np
from scipy.special import iv
def jk(x, f=np.mean, nb=20):
    x = np.asarray(x); n = len(x)//nb*nb; b = x[:n].reshape(nb, -1, *x.shape[1:])
    full = f(x[:n]); reps = np.array([f(np.concatenate([b[k] for k in range(nb) if k != i])) for i in range(nb)])
    return full, math.sqrt((nb-1)*np.mean((reps-reps.mean(0))**2))
rows = []
for fn in sorted(glob.glob("data/su2_L*_b*_*.json")):
    d = json.load(open(fn)); L, b = d["L"], d["beta"]; R = d["recs"]
    P = np.array([r["plaq"] for r in R]); Np = 6*L**4
    p, dp = jk(P)
    chi, dchi = jk(P, lambda x: Np*np.var(x))
    row = {"L": L, "beta": b, "start": d["start"], "sec": round(d["seconds"]), "P": p, "dP": dp,
           "dPdbeta=NpVar": chi, "d_dPdbeta": dchi, "u=I2/I1": float(iv(2, b)/iv(1, b)), "1-3/(4b)": 1-3/(4*b),
           "poly": float(np.mean([r["poly"] for r in R]))}
    W = {k: np.array([r["W"][k] for r in R]) for k in R[0]["W"]}
    if "2x2" in W:
        cr = lambda idx: (lambda z: -math.log(z) if z > 0 else float("nan"))(W["2x2"][idx].mean()*W["1x1"][idx].mean()/W["1x2"][idx].mean()**2)
        idx = np.arange(len(P)); full = cr(idx); nb = 20; m = len(P)//nb
        reps = [cr(np.concatenate([idx[:i*m], idx[(i+1)*m:]])) for i in range(nb)]
        row["creutz22"] = full; row["d_creutz22"] = math.sqrt((nb-1)*np.var(reps)) if np.all(np.isfinite(reps)) else float("nan")
    Ot = np.array([r["Ot"] for r in R])
    def meff(x):
        x = x - x.mean(); C = np.array([np.mean(x*np.roll(x, -t, axis=1)) for t in range(3)])
        return np.log(C[1]/C[2]) if C[2] > 0 and C[1] > 0 else np.nan
    try:
        mm, dm = jk(Ot, meff); row["m0pp_eff(t=1)"] = float(mm); row["d_m0pp"] = dm
    except Exception: pass
    rows.append(row)
json.dump(rows, open("data/mc_summary.json", "w"), indent=1)
hdr = f"{'L':>2} {'beta':>5} {'start':>5} {'<P>':>16} {'u=I2/I1':>8} {'1-3/4b':>7} {'dP/db':>14} {'creutz22':>15} {'m0++(1)':>14} {'|Poly|':>7}"
print(hdr)
for r in sorted(rows, key=lambda r: (r["L"], r["beta"], r["start"])):
    cz = f"{r['creutz22']:.3f}({r['d_creutz22']:.3f})" if "creutz22" in r else ""
    me = f"{r.get('m0pp_eff(t=1)', float('nan')):.2f}({r.get('d_m0pp', float('nan')):.2f})"
    print(f"{r['L']:>2} {r['beta']:>5} {r['start']:>5} {r['P']:.5f}({r['dP']:.5f}) {r['u=I2/I1']:.5f} {r['1-3/(4b)']:.4f} {r['dPdbeta=NpVar']:.4f}({r['d_dPdbeta']:.4f}) {cz:>15} {me:>14} {r['poly']:.4f}")
print("total CPU s (sum of runs):", sum(r["sec"] for r in rows))
