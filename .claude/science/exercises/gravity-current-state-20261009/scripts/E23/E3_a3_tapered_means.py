"""E3 (a3): interior means of the local stiffness density with a sharp ball and with smooth tapers
phi = (1 - r^2/Ri^2)_+^n, n = 2, 4, 8 (smooth weights converge much faster on quasiperiodic sets; on a Z^3 ball every
choice returns the exact crystal value).  usage: python3 E3_a3_tapered_means.py files..."""
import numpy as np, sys
import e23_core as c
for f in sys.argv[1:]:
    d = np.load(f); X, e2, Rp, buf = d['X'], d['e2'], float(d['Rp']), float(d['buf'])
    Ri = Rp - buf; r2 = np.einsum('ij,ij->i', X, X) / Ri**2
    row = [f"{f:28s}"]
    for n in [0, 2, 4, 8]:
        phi = (r2 < 1).astype(float) if n == 0 else np.clip(1 - r2, 0, None)**n
        mu = (phi[:, None] * e2).sum(0) / phi.sum()
        row.append(f"n={n}: E_g {mu[c.CH['E_g']].mean():+.5f} T_2g {mu[c.CH['T_2g']].mean():+.5f} dir-spread {mu.std():.5f}")
    print(" | ".join(row))
