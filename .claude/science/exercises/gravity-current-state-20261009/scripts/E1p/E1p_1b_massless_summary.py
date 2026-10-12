"""Summary of massless runs: Fano vs s/D, link sigma distribution (arrival offset law), duration dependence."""
import glob, numpy as np
from math import pi, sqrt
rows = []
print(" s    D       s/D     Ts    n     Nbar(quad)  <N>sim   Fano(flat)  se     Var/diag(gauss)  rel.noise/realiz(flat)  law sqrt((1+F-1)/Nbar)")
for f in sorted(glob.glob("../out/massless_[AB]_*.npz")):
    d = np.load(f); NF = d["NF"]; FG = d["FG"]; n = len(NF)
    s, D, Ts = float(d["s"]), float(d["D"]), float(d["Ts"])
    m1f = float(d["m1f"]); m2g = float(d["m2g"])
    F = NF.var(ddof=1) / m1f
    # standard error of variance estimate via bootstrap-free formula: Var(s^2) ~ (mu4 - s^4 (n-3)/(n-1))/n
    mu4 = np.mean((NF - NF.mean())**4); s2 = NF.var(ddof=1)
    se = np.sqrt(max(mu4 - s2 * s2 * (n - 3) / (n - 1), 0) / n) / m1f
    rows.append((s, D, Ts, F, se))
    print(f"{s:4.0f} {D:7.0f} {s/D:8.4f} {Ts:5.1f} {n:5d}  {m1f:9.3f}  {NF.mean():8.3f}   {F:6.3f}   {se:.3f}   {FG.var(ddof=1)/m2g:6.3f}"
          f"            {NF.std(ddof=1)/NF.mean():.4f}               {sqrt(F/m1f):.4f}")
sl = np.vstack([np.load(f)["sig_links"] for f in glob.glob("../out/massless_[AB]_*.npz") if np.load(f)["sig_links"].shape[0] > 0])
print(f"\nlink sigma = tau_xy^2 (ell^2) over {len(sl)} links: mean {sl[:,0].mean():.4f} (EXACT 12/(pi sqrt6) = {12/(pi*sqrt(6)):.4f}), "
      f"sd {sl[:,0].std():.4f} (EXACT {sqrt(12/pi-(12/(pi*sqrt(6)))**2):.4f})")
