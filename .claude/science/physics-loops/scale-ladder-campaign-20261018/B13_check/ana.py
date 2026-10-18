"""Analysis of B13_check runs: energies, forward-walking slopes (plain and population-control reweighted),
twisted-energy curvatures, 1/N extrapolation.  Independent checker code; no claim."""
import os, sys, glob, re, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)


def load(fn):
    d = dict(np.load(fn))
    m = re.match(r"results/L(\d+)_V([+-][\d.]+)_N(\d+)_e([\d.]+)_(\w+)_dt([\d.]+)_s(\d+)\.npz", fn)
    d.update(L=int(m[1]), V=float(m[2]), N=int(m[3]), eta=float(m[4]), init=m[5], dt=float(m[6]), seed=int(m[7]))
    d["np"] = 3 * d["L"] ** 3
    return d


def jk_err(vals):
    vals = np.asarray(vals); n = len(vals)
    return np.sqrt((n - 1) / n * ((vals - vals.mean()) ** 2).sum())


def energy(d, P=0, nbin=20):
    """mixed energy (total); P>0: UNR population-control reweighting with the last P step factors."""
    E = d["EM"].ravel(); LM = d["LM"].ravel()
    ok = ~np.isnan(E)
    if P > 0:
        c = np.concatenate([[0.0], np.cumsum(LM)])
        lw = c[1:] - c[np.maximum(np.arange(1, len(LM) + 1) - P, 0)]
        lw = lw - lw[ok].max()
        w = np.exp(lw)
    else:
        w = np.ones_like(LM)
    t = np.flatnonzero(ok); t = t[t >= P]
    E, w = E[t], w[t]
    n = len(E) // nbin * nbin
    Eb = (E[:n] * w[:n]).reshape(nbin, -1).sum(1); Wb = w[:n].reshape(nbin, -1).sum(1)
    est = Eb.sum() / Wb.sum()
    jk = [(Eb.sum() - Eb[i]) / (Wb.sum() - Wb[i]) for i in range(nbin)]
    return est, jk_err(jk)


def fw_chi(d, P=0, tmin=8.0):
    M2 = d["M2"].mean(2)  # average of the 3 harmonic orientations, (nb, nst)
    nb_, nst = M2.shape
    tau = d["tau"]; sel = tau >= tmin
    LM = d["LM"]
    if P > 0:
        flat = LM.ravel(); c = np.concatenate([[0.0], np.cumsum(flat)])
        W = np.zeros((nb_, nst))
        for b in range(nb_):
            s0 = b * nst
            lo = s0 - P
            if lo < 0:
                W[b] = -np.inf
                continue
            W[b] = c[s0 + np.arange(1, nst + 1)] - c[lo]
        W = np.exp(W - W[np.isfinite(W)].max())
    else:
        W = np.ones((nb_, nst))
    def slope(idx):
        num = (W[idx] * M2[idx]).sum(0); den = W[idx].sum(0)
        return np.polyfit(tau[sel], (num / den)[sel], 1)[0]
    allb = np.arange(nb_)
    est = slope(allb)
    jk = [slope(np.delete(allb, b)) for b in range(nb_)]
    return est, jk_err(jk)


runs = [load(f) for f in sorted(glob.glob("results/*.npz"))]
out = {"fw": [], "tw": []}
print("FW runs (eta=0):  L V N init : E/plaq (plain) | E/plaq (UNR P=100) | chi_FW (plain) | chi_FW (UNR P=100) | N/ESS")
for d in sorted([r for r in runs if r["eta"] == 0], key=lambda r: (r["L"], r["V"], r["init"], r["dt"], r["N"])):
    e0 = energy(d); e1 = energy(d, P=100)
    c0 = fw_chi(d); c1 = fw_chi(d, P=100)
    npl = d["np"]
    tm = [fw_chi(d, tmin=t)[0] for t in (4.0, 12.0, 16.0)]
    print(f"  L={d['L']} V={d['V']:+.2f} N={d['N']:5d} {d['init']:6s} dt={d['dt']} tmin4/12/16={tm[0]:.3f}/{tm[1]:.3f}/{tm[2]:.3f}: {e0[0]/npl:.6f}({e0[1]/npl*1e6:.0f}e-6) | {e1[0]/npl:.6f}({e1[1]/npl*1e6:.0f}e-6) | "
          f"{c0[0]:.4f}({c0[1]:.4f}) | {c1[0]:.4f}({c1[1]:.4f}) | {d['IESS'].mean():.2f}  [{float(d['secs']):.0f}s]")
    out["fw"].append(dict(L=d["L"], V=d["V"], N=d["N"], init=d["init"], E=e0, E_unr=e1, chi=c0, chi_unr=c1, iess=float(d["IESS"].mean()), np=npl))
print("Twisted runs: L V N eta : E_mix total, growth")
for d in sorted([r for r in runs if r["eta"] > 0], key=lambda r: (r["L"], r["V"], r["eta"])):
    e0 = energy(d)
    g = d["ET"] - d["LM"].mean() / d["dt"]
    print(f"  L={d['L']} V={d['V']:+.2f} N={d['N']} eta={d['eta']}: Emix={e0[0]:.4f}({e0[1]:.4f}) growth={g:.4f}")
    out["tw"].append(dict(L=d["L"], V=d["V"], N=d["N"], eta=d["eta"], E=e0, growth=float(g)))
json.dump(out, open("ana_out.json", "w"), indent=1, default=float)

print("Twisted curvature fits (same N; E(eta)-E(0) = -chi eta^2/2 + d eta^4 ; single-eta estimates -2dE/eta^2):")
from collections import defaultdict
grp = defaultdict(dict)
for r in runs:
    grp[(r["L"], r["V"], r["N"], r["init"], r["dt"])][r["eta"]] = energy(r)
for k, g in sorted(grp.items()):
    if 0.0 not in g or len(g) < 2:
        continue
    e0, s0 = g[0.0]
    etas = sorted(e for e in g if e > 0)
    singles = [(eta, -2 * (g[eta][0] - e0) / eta ** 2, 2 * np.hypot(g[eta][1], s0) / eta ** 2) for eta in etas]
    line = f"  L={k[0]} V={k[1]:+.2f} N={k[2]} {k[3]}: " + " ".join(f"eta={a}: {b:.4f}({c:.4f})" for a, b, c in singles)
    if len(etas) >= 2:
        x = np.array([0.0] + etas); y = np.array([e0] + [g[e][0] for e in etas]); s = np.array([s0] + [g[e][1] for e in etas])
        A = np.vstack([np.ones_like(x), -x ** 2 / 2, x ** 4]).T / s[:, None]
        cov = np.linalg.inv(A.T @ A); p = cov @ A.T @ (y / s)
        line += f" | quad+quartic fit chi={p[1]:.4f}({np.sqrt(cov[1, 1]):.4f})"
        out.setdefault("twfit", []).append(dict(L=k[0], V=k[1], N=k[2], chi=float(p[1]), err=float(np.sqrt(cov[1, 1])), singles=singles))
    print(line)
json.dump(out, open("ana_out.json", "w"), indent=1, default=float)
