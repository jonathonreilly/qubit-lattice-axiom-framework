#!/usr/bin/env python3
"""lane954 analysis: tables of R_J per sector, C4 (two K values), gap floors (Lemma GAP-R), scaling fits,
seed thresholds.  Reads library/guide/lane954/out/*.json.  GUIDE only.  Claude Opus 5.5 (max), 2026-11-14.
Usage: python3 -I analyze954.py <out dir>"""
import sys, json, glob, os, math
import numpy as np

RSTAR = {2.3: {30: 0.232, 40: 0.305, 60: 0.446, 100: 0.714, 200: 1.350},
         2.6: {30: 0.205, 40: 0.269, 60: 0.393, 100: 0.630, 200: 1.189}}


def plateau(g, taus=(1, 2, 3)):
    e = [g["Eeff"][t] for t in taus if t < len(g["Eeff"])]
    s = [g["Eeff_err"][t] for t in taus if t < len(g["Eeff_err"])]
    ok = [(a, b) for a, b in zip(e, s) if np.isfinite(a) and np.isfinite(b) and b > 0 and a > 0]
    if not ok:
        return float("nan"), float("nan")
    w = np.array([1/b**2 for _, b in ok])
    v = np.array([a for a, _ in ok])
    return float((w*v).sum()/w.sum()), float(1/math.sqrt(w.sum()))


def fit(Ls, R, E):
    x = np.log(Ls)
    y = np.log(R)
    s = np.array(E)/np.array(R)
    w = 1/s**2
    A = np.vstack([np.ones_like(x), x]).T
    Cov = np.linalg.inv(A.T @ (A*w[:, None]))
    b = Cov @ (A.T @ (w*y))
    chi2 = float((w*(y-A @ b)**2).sum())
    return float(b[1]), float(math.sqrt(Cov[1, 1])), chi2, len(Ls)-2


def main(d):
    runs = {}
    for f in sorted(glob.glob(os.path.join(d, "*.json"))):
        nm = os.path.basename(f)[:-5]
        if nm.startswith(("c1_", "c2_", "c5_", "t_")):
            continue
        r = json.load(open(f))
        a = r["args"]
        runs[(a["group"], a["beta"], a["L"])] = r
    groups = sorted(set((g, b) for (g, b, _) in runs))
    for (g, b) in groups:
        Ls = sorted(L for (gg, bb, L) in runs if (gg, bb) == (g, b))
        print(f"\n=== {g} beta {b}")
        print("L | nmeas | sector tops (raw +- err; bias-corr) | R_J^top (sector) | C4 extra-pair top of that sector | E_wind | floor 1/(2 beta E_wind) | E_plaq(0), E_plaq(1) | E c_p")
        tops = []
        for L in Ls:
            r = runs[(g, b, L)]
            S = r["sectors"]
            X = r.get("sectors_extra") or {}
            best = max(S, key=lambda k: S[k]["top"])
            sec = "; ".join(f"{k} {v['top']:.4f}+-{v['err']:.4f} ({v['top_bc']:.4f})" for k, v in S.items())
            c4 = X.get(best, {})
            c4s = f"{c4.get('top', float('nan')):.4f}+-{c4.get('err', float('nan')):.4f}" if c4 else "-"
            ew, ewe = plateau(r["gaps"]["wind"])
            fl = 1/(2*b*ew) if ew > 0 else float("nan")
            fle = fl*ewe/ew if ew > 0 else float("nan")
            gp = r["gaps"]["plaq0"]
            print(f"{L} | {r['nmeas']} | {sec} | {S[best]['top']:.4f}+-{S[best]['err']:.4f} ({best}) | {c4s} | "
                  f"{ew:.4f}+-{ewe:.4f} | {fl:.3f}+-{fle:.3f} | {gp['Eeff'][0]:.3f}+-{gp['Eeff_err'][0]:.3f}, "
                  f"{gp['Eeff'][1]:.3f}+-{gp['Eeff_err'][1]:.3f} | {r['stats_mean'][0]:.4f}")
            tops.append((L, best, S[best]["top"], S[best]["err"], S[best]["top_bc"]))
            # C4 for every sector
            dev = []
            for k in S:
                if k in X:
                    dz = (S[k]["top"]-X[k]["top"])/math.hypot(S[k]["err"], X[k]["err"])
                    dev.append(f"{k} {dz:+.1f}")
            print(f"     C4 (central K' vs extra K), deviation in combined errors: {', '.join(dev)}")
            if g == "u1":
                gb = r["gaps"]["Bkmin"]
                om = 2*math.asinh(math.sin(math.pi/L))
                print(f"     photon: E_B(kmin) tau=0,1,2: " + ", ".join(f"{e:.3f}+-{s:.3f}" for e, s in zip(gb['Eeff'][:3], gb['Eeff_err'][:3]))
                      + f"; free omega_min {om:.4f}; free 1/c {1/(b*(math.exp(om)-1)):.4f}; U1s/free {S['U1s']['top']*(b*(math.exp(om)-1)):.3f}")
        # fits over L >= 6
        sel = [t for t in tops if t[0] >= 6]
        if len(sel) >= 3:
            k, ke, chi2, dof = fit([t[0] for t in sel], [t[2] for t in sel], [t[3] for t in sel])
            print(f"  fit R_J^top ~ L^kappa over L >= 6: kappa = {k:.3f} +- {ke:.3f} (chi2 {chi2:.1f}/{dof})")
            first = [t for t in sel if t[0] == 6][0]
            last = sel[-1]
            print(f"  R(L_max) - R(6) = {last[2]-first[2]:+.4f} +- {math.hypot(last[3], first[3]):.4f}")
        for secname in runs[(g, b, Ls[0])]["sectors"]:
            pts = [(L, runs[(g, b, L)]["sectors"][secname]["top"], runs[(g, b, L)]["sectors"][secname]["err"]) for L in Ls if L >= 6]
            if len(pts) >= 3:
                k, ke, chi2, dof = fit([p[0] for p in pts], [p[1] for p in pts], [p[2] for p in pts])
                print(f"  sector {secname}: kappa = {k:.3f} +- {ke:.3f} (chi2 {chi2:.1f}/{dof}); values " +
                      ", ".join(f"L{p[0]} {p[1]:.4f}" for p in pts))
        if g == "su2" and b in RSTAR:
            for (L, best, top, err, bc) in tops:
                ref = [a for a, rs in RSTAR[b].items() if top-3*err > rs]
                print(f"  S3 on the {L}^3 box: R_J^top - 3 err = {top-3*err:.3f} exceeds R*_a for a in {ref}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "out"))
