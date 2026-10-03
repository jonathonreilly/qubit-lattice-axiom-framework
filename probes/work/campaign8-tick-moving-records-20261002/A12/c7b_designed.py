"""C7b: designed (impedance-matched) register schedule, massless 1D step (R content passes x once).
Register amplitude r_T = sum_t w_eff(t) a_t with w_eff(t) = sin(th_t) prod_{s>t} cos(th_s).
Invert backwards for a target w_eff = Chebyshev taps scaled to sum w_eff^2 = Q (capture fraction)."""
import numpy as np, runpy

src = open("c7_register.py").read().split("for m in (0.0, 0.3):")[0]
g = {}; exec(src, g)
U, Vl = g["build"](0.0)
for T in (16, 32, 48):
    for Q in (0.5, 0.9, 0.99):
        tgt = g["cheb_taps"](T, np.sqrt(2.0)); tgt = tgt / np.linalg.norm(tgt) * np.sqrt(Q)
        th = np.empty(T); C = 1.0
        for t in range(T - 1, -1, -1):
            th[t] = np.arcsin(tgt[t] / C); C *= np.cos(th[t])
        nv, ne, em = g["respond"](U, Vl, th, 1.0, 0.0)     # w = th, g = 1  -> angles th_t
        print(f"T={T:3d} capture Q={Q:<5}: P(form|vac)={nv:.3e}  P(form|matched particle)={ne:.4f}  "
              f"ratio={nv/(ne-nv):.3e}  single-mode eps={em:.3e}  max angle={np.abs(th).max():.3f}")
