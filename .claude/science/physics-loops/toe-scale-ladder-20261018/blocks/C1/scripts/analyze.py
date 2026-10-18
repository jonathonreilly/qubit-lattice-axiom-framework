#!/usr/bin/env python3
"""Analysis of production npz files -> data/summary.json, data/summary_table.md, applies the WORKLOG criteria.
Errors: per-bin derived quantities (64 bins of consecutive measurements) -> mean, SE = std/sqrt(nb);
a bin-size check is applied by also computing SE from 16 merged bins and taking the larger.
"""
import os, sys, glob, json
import numpy as np

base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
files = sorted(glob.glob(os.path.join(base, "data", "run_L*_V*_T*_s*.npz")))


def mse(x):
    x = np.asarray(x, float)
    nb = len(x)
    se64 = x.std(ddof=1) / np.sqrt(nb)
    y = x[: nb // 4 * 4].reshape(-1, 4).mean(1)
    se16 = y.std(ddof=1) / np.sqrt(len(y))
    return float(x.mean()), float(max(se64, se16)), float(se16 / se64)


def jack_gap(Cb, dtau, j1, j2):
    """effective gap from log-linear fit of C(tau) over j1..j2, jackknife over bins."""
    Cb = np.asarray(Cb)
    nb = len(Cb)

    def fit(C):
        t = dtau * np.arange(j1, j2 + 1)
        y = np.log(np.clip(C[j1:j2 + 1], 1e-12, None))
        return -np.polyfit(t, y, 1)[0]

    full = fit(Cb.mean(0))
    jk = np.array([fit(np.delete(Cb, i, 0).mean(0)) for i in range(nb)])
    se = np.sqrt((nb - 1) / nb * ((jk - jk.mean()) ** 2).sum())
    return float(full), float(se)


rows = []
for f in files:
    z = np.load(f)
    L = int(z["L"])
    V = float(z["V"])
    T = float(z["T"])
    seed = int(z["seed"])
    nv = L ** 3
    npl = 3 * nv
    r = {"L": L, "V": V, "T": T, "seed": seed, "nsweep": int(z["nsweep"]), "file": os.path.basename(f),
         "fails": int(z["gauss_or_path_failures"]), "valid": bool(z["valid_final"])}
    r["E_mix_per_plaq"] = [float(z["Emix"][0]) / npl, float(z["Emix"][1]) / npl]
    r["E_mid_per_plaq"] = [float(z["E_mid"][0]) / npl, float(z["E_mid"][1]) / npl]
    r["nflip_mid_per_plaq"] = [float(z["Nf_mid"][0]) / npl, float(z["Nf_mid"][1]) / npl]
    r["ST1_series"] = [float(z["ST1"][0]), float(z["ST1"][1])]
    if "bd_ST_100" not in z.files:
        r["note"] = "no per-bin derived data (pre-change run)"
        rows.append(r)
        continue
    for k in z.files:
        if k.startswith("bd_ST_") or k.startswith("bd_Sn_") and k != "bd_Sn_max_q" or k == "bd_Sn_max":
            m, s, ratio = mse(z[k])
            r[k[3:]] = [m, s]
    # orientation-resolved maxima over Q in {0,pi}^3 (flippability and E)
    best = (None, -1, 0)
    for k in z.files:
        if k.startswith("bd_Sn0_") or k.startswith("bd_Sn1_") or k.startswith("bd_Sn2_") or k.startswith("bd_SE"):
            m, s, _ = mse(z[k])
            r[k[3:]] = [m, s]
    r["Sn_max_q"] = [int(x) for x in z["bd_Sn_max_q"]]
    # lattice momentum
    k1 = 2 * np.sin(np.pi / L)
    r["K1"] = float(k1)
    r["ST_100_over_K"] = [r["ST_100"][0] / k1, r["ST_100"][1] / k1]
    if "C_bins" in z.files:
        Cb = z["C_bins"]
        dtau = float(z["dtau"])
        J = Cb.shape[1] - 1
        jmax = min(J, int(round(T / 4 / dtau)))
        j1 = max(1, int(round(0.5 / dtau)))
        if jmax > j1 + 1:
            r["gap_fit"] = jack_gap(Cb, dtau, j1, jmax)
            r["gap_window"] = [j1 * dtau, jmax * dtau]
        r["C0"] = [float(Cb[:, 0].mean()), float(Cb[:, 0].std(ddof=1) / np.sqrt(len(Cb)))]
    rows.append(r)

json.dump(rows, open(os.path.join(base, "data", "summary.json"), "w"), indent=1)

# table
lines = ["| L | V | T | seed | sweeps | E_mix/N_p | E_mid/N_p | n_flip/N_p | S_T(k1) | S_T(k1)/K1 | S_T(110) | S_n(pi,pi,pi) | S_n max over {0,pi}^3 | S_n global max (q) | gap(k1) [window] |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]


def fm(v, d=4):
    return f"{v[0]:.{d}f}({v[1]:.{d}f})" if isinstance(v, (list, tuple)) else str(v)


for r in sorted(rows, key=lambda x: (x["V"], x["L"], x["T"], x["seed"])):
    if "ST_100" not in r:
        continue
    snq = {k: v for k, v in r.items() if k.startswith("Sn_") and k not in ("Sn_max", "Sn_max_q")}
    kmax = max(snq, key=lambda k: snq[k][0])
    gap = f"{r['gap_fit'][0]:.3f}({r['gap_fit'][1]:.3f}) [{r['gap_window'][0]:.2f},{r['gap_window'][1]:.2f}]" if "gap_fit" in r else "-"
    lines.append(f"| {r['L']} | {r['V']} | {r['T']:g} | {r['seed']} | {r['nsweep']} | {fm(r['E_mix_per_plaq'])} | {fm(r['E_mid_per_plaq'])} | "
                 f"{fm(r['nflip_mid_per_plaq'])} | {fm(r['ST_100'])} | {fm(r['ST_100_over_K'])} | {fm(r.get('ST_110', ['-', '-'])) if 'ST_110' in r else '-'} | "
                 f"{fm(r['Sn_111'], 3)} | {kmax[3:]}: {fm(snq[kmax], 3)} | {fm(r['Sn_max'], 3)} @ {r['Sn_max_q']} | {gap} |")
open(os.path.join(base, "data", "summary_table.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
