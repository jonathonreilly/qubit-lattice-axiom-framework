"""B13 analysis: tabulate forward-walking DMC curvatures vs L and V, add exact 2^3 values, run consistency checks.
Exploratory worker code; no claim.  Prints PASS/FAIL per check.
"""
import os, sys, json, glob
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B6_maxwell_winding"))
sys.path.insert(0, HERE)
import ringlib as R
import pqmclib as Q

NPASS = NFAIL = 0


def check(name, ok, detail=""):
    global NPASS, NFAIL
    NPASS += bool(ok); NFAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)


runs = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(HERE, "results", "*.json")))]
main = {(r["L"], r["V"]): r for r in runs if r["N"] == 4000}
Vs = sorted({k[1] for k in main})
Ls = sorted({k[0] for k in main})

# exact 2^3
T = R.Torus((2, 2, 2)); lat = Q.Lattice((2, 2, 2))
codes = R.sector_states(T, (0, 0, 0)); inv, sizes, _ = R.split_components(T, codes)
comp = R.Component(T, codes[inv == np.argmax(sizes)])
C = np.array([lat.fourier_dirs((0, 0, 0), 0)[0]] + lat.coexact_dirs((np.pi, 0, 0)))
ex = {}
for V in Vs:
    E0, g, gap = comp.ground(V)
    Hs, _ = comp.hessian(V, C)
    ex[V] = dict(E0=E0 / 24, chi_h=Hs[0, 0], KT=Hs[1, 1], gap=gap)

print("\n  V     L   E/plaq             chi_harm (q=0)      K_T(q_min=2pi/L)")
table = []
for V in Vs:
    print(f"{V:+.2f}   2   {ex[V]['E0']:.5f} (exact)   {ex[V]['chi_h']:.4f} (exact)      {ex[V]['KT']:.4f} (exact, q=pi)")
    for L in Ls:
        r = main.get((L, V))
        if r is None:
            continue
        print(f"{V:+.2f}   {L}   {r['E_per_plaq'][0]:.5f}+-{r['E_per_plaq'][1]:.5f}   {r['chi_harm'][0]:.4f}+-{r['chi_harm'][1]:.4f}     "
              f"{r['KT_qmin'][0]:.4f}+-{r['KT_qmin'][1]:.4f}")
        table.append(dict(V=V, L=L, E=r["E_per_plaq"], chi_harm=r["chi_harm"], KT=r["KT_qmin"]))

# ---------------- checks --------------------------------------------------------------------
for (L, V), r in sorted(main.items()):
    h = np.array([c[0] for c in r["chi"][:3]]); he = np.array([c[1] for c in r["chi"][:3]])
    chi2 = (((h - r["chi_harm"][0]) / he) ** 2).sum()
    k = np.array([c[0] for c in r["chi"][3:]]); ke = np.array([c[1] for c in r["chi"][3:]])
    chi2k = (((k - r["KT_qmin"][0]) / ke) ** 2).sum()
    check(f"L={L} V={V:+.2f}: three harmonic orientations agree (chi2={chi2:.1f}, 2 dof, < 13.8)", chi2 < 13.8)
    check(f"L={L} V={V:+.2f}: six coexact q_min sources agree (chi2={chi2k:.1f}, 5 dof, < 20.5)", chi2k < 20.5)
repo = {4: (-0.2926, 0.0003), 6: (-0.2883, 0.0003), 8: (-0.2871, 0.0002)}  # repo projector cache, V=0 (guide-dependent)
for L, (e, de) in repo.items():
    r = main.get((L, 0.0))
    if r:
        d = abs(r["E_per_plaq"][0] - e)
        check(f"L={L} V=0: energy/plaquette within 0.002 of the repo projector value {e} (repo notes a guide dependence)", d < 0.002,
              f"{r['E_per_plaq'][0]:.5f} diff {d:.5f}")
small = [r for r in runs if r["N"] == 1000 and r["L"] == 6 and r["V"] == 0.0]
if small and (6, 0.0) in main:
    a, b = small[0], main[(6, 0.0)]
    for key in ("chi_harm", "KT_qmin"):
        d = abs(a[key][0] - b[key][0]); s = np.hypot(a[key][1], b[key][1])
        check(f"population 1000 vs 4000 at L=6 V=0: {key} agrees within 3 sigma", d < 3 * s,
              f"{a[key][0]:.4f}+-{a[key][1]:.4f} vs {b[key][0]:.4f}+-{b[key][1]:.4f}")
    d = abs(a["E_per_plaq"][0] - b["E_per_plaq"][0]); s = np.hypot(a["E_per_plaq"][1], b["E_per_plaq"][1])
    check("population 1000 vs 4000 at L=6 V=0: energy agrees within 3 sigma + 2e-4", d < 3 * s + 2e-4, f"diff {d:.5f}")
json.dump(dict(exact2=ex, table=table), open(os.path.join(HERE, "b13_analyze_results.json"), "w"), indent=1, default=float)
print(f"PASS={NPASS} FAIL={NFAIL}")
