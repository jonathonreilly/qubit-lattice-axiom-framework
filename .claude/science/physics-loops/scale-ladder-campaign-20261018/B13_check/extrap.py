"""1/N extrapolations (weighted linear fits) of energy, chi_FW and single-eta twisted chi (beta=c*eta=0.25). No claim."""
import json, numpy as np
d = json.load(open("ana_out.json"))
def fit(x, y, s):
    x, y, s = map(np.asarray, (x, y, s))
    A = np.vstack([np.ones_like(x), x]).T / s[:, None]
    cov = np.linalg.inv(A.T @ A); p = cov @ A.T @ (y / s)
    chi2 = (((A @ p) - y / s) ** 2).sum()
    return p[0], np.sqrt(cov[0, 0]), p[1], chi2, len(x) - 2
for (L, V) in ((4, 0.0), (4, -0.5), (4, 0.5), (6, 0.0), (6, 0.5)):
    fw = sorted([r for r in d["fw"] if r["L"] == L and r["V"] == V and r["init"] == "tiled" and r.get("dt", 0.1) == 0.1], key=lambda r: r["N"])
    if len(fw) < 2: continue
    N = np.array([r["N"] for r in fw]); x = 1 / N
    E = [r["E"][0] / r["np"] for r in fw]; sE = [r["E"][1] / r["np"] for r in fw]
    c = [r["chi"][0] for r in fw]; sc = [r["chi"][1] for r in fw]
    e0 = fit(x, E, sE); c0 = fit(x, c, sc)
    print(f"L={L} V={V:+.1f} N={list(N)}")
    print(f"   E/plaq: {np.round(E, 6).tolist()} -> N=inf {e0[0]:.6f}({e0[1]*1e6:.0f}e-6) chi2/dof={e0[3]:.1f}/{e0[4]}")
    print(f"   chi_FW: {np.round(c, 4).tolist()} -> N=inf {c0[0]:.4f}({c0[1]:.4f}) chi2/dof={c0[3]:.1f}/{c0[4]}")
    tw = [t for t in d["twfit"] if False]
    sing = []
    for r in fw:
        for t in d["tw"]:
            if t["L"] == L and t["V"] == V and t["N"] == r["N"] and abs(t["eta"] * (3 * L ** 3 / 3) ** -0.5 - 0.25) < 0.01:
                ch = -2 * (t["E"][0] - r["E"][0]) / t["eta"] ** 2; s = 2 * np.hypot(t["E"][1], r["E"][1]) / t["eta"] ** 2
                sing.append((r["N"], ch, s))
    if len(sing) >= 2:
        t0 = fit([1 / a for a, _, _ in sing], [b for _, b, _ in sing], [c for _, _, c in sing])
        print(f"   chi_tw(beta=.25): {[(a, round(b, 4), round(c, 4)) for a, b, c in sing]} -> N=inf {t0[0]:.4f}({t0[1]:.4f}) chi2/dof={t0[3]:.1f}/{t0[4]}")
    elif sing:
        print(f"   chi_tw(beta=.25): {sing}")
