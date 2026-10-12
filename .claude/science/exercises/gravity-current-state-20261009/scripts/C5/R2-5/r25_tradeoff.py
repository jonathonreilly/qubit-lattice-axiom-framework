"""R2-5 check 3: the arrow-length / un-formation trade-off.
Isotropic (ex = et = eps) versus anisotropic (ex = 1, et = eps) laws, same toy as r25_toy_gibbs.
For each law: t90 (arrow length: 90% of net formation over [0, T/2]) and u_bulk (un-formation
per site per step at t = T/2, after the arrow).  Report, for thresholds u* on u_bulk, the
largest t90 found on the grid.  Anisotropic single column at large T checks xi = 1/h and
K(1->0) = c^2/(b-a) with c = eps e^{h/2}, b - a = e^h - 1 (asymptotic Perron kernel).
"""
import numpy as np
from r25_toy_gibbs import run, profile, corr_length

def grid(iso, L, T):
    res = []
    for eps in np.geomspace(0.02, 0.7, 14):
        for h in np.geomspace(1e-3, 3.0, 14):
            r = run(L, h, eps, T, iso=iso)
            res.append((eps, h, r['t90'], r['u_half'], r['f_half'], r['m_half'], r['xi']))
    return res

def frontier(res, label):
    print(f"  {label}:")
    for us in (1e-2, 1e-4, 1e-6, 1e-8):
        ok = [r for r in res if r[3] <= us and r[5] > 0.5 and not np.isnan(r[2])]
        if not ok:
            print(f"    u_bulk <= {us:.0e} and records formed (m>0.5): none on grid"); continue
        b = max(ok, key=lambda r: r[2])
        print(f"    u_bulk <= {us:.0e}, m(T/2)>0.5: max t90 = {b[2]:3d}  at eps={b[0]:.3f} h={b[1]:.4f} (xi={b[6]:.2f}, u={b[3]:.1e})")

if __name__ == "__main__":
    T = 100
    print("== trade-off on a 14x14 grid (eps in [0.02,0.7], h in [1e-3,3]), T=100 ==")
    for L in (6, 8):
        frontier(grid(True, L, T), f"isotropic, L={L}")
    frontier(grid(False, 1, T), "anisotropic single column (L=1)")
    print("== anisotropic single column, large T: xi vs 1/h, kernel K(1->0) vs c^2/(b-a) ==")
    for h, eps in ((0.05, 1e-3), (0.02, 1e-4), (0.01, 1e-5), (0.002, 1e-6)):
        xi, l0, l1 = corr_length(1, h, 1.0, eps)
        a, b, c = 1.0, np.exp(h), eps * np.exp(h / 2)
        Tm = np.array([[a, c], [c, b]])
        lam, vec = np.linalg.eigh(Tm); psi = np.abs(vec[:, -1])
        K10 = c * psi[0] / (lam[-1] * psi[1]); K01 = c * psi[1] / (lam[-1] * psi[0])
        print(f"  h={h:6.3f} eps={eps:.0e}: xi={xi:10.3f} (1/h={1/h:8.1f}); K(0->1)={K01:.3e} (~h={h:.1e}); K(1->0)={K10:.3e} (c^2/(b-a)={c*c/(b-a):.3e})")
