"""F6 sensitivity: loop-1 (U(1)) and loop-4 Hessians as the scalar-edge knob b_s moves (b_s is a tuned root knob fixed by the mu_E row,
rR18-9 sec. 0; this scan is a sensitivity probe, not a branch), and the photon-edge window b_gamma in [2.936, 2.947] (rR18-9 sec. 0 item 2)."""
import numpy as np, time
from f6_lib import *
t00 = time.time()
print('b_s scan (Gph(2.9435), m = 0, 368-node grid, d = 0.0015): d2_t Sig_g/e^2 and d2_t G_s')
G = Phot(CPH)
for bs in (2.30, 2.40, 2.45, 2.50, BS, 2.55, BS0, 2.62, 2.65, 2.70, 2.80):
    S = Phot(bs); x, w = mkgrid(bs, 8, 0.15, 16)
    hg = hess_even(lambda t: sig_gauge(S, G, x, w, t), 0.0015)[3]
    hl = hess_even(lambda t: g_scalar(S, x, w, t), 0.0015)[3]
    print('  b_s = %.6f: gauge %+.6e   G_s %+.6e' % (bs, hg, hl), flush=True)
print('photon window (b_s = R18-9):')
S = Phot(BS)
for bg in (2.936, 2.94, 2.9435, 2.947):
    Gb = Phot(bg)
    br = [BS, bg] + [bg + i*(np.pi - bg)/16 for i in range(1, 16)] + [BS + i*(np.pi - BS)/6 for i in range(1, 6)]
    x, w = panels(br, 8, 0.15)
    hg = hess_even(lambda t: sig_gauge(S, Gb, x, w, t), 0.0015)[3]
    print('  b_gamma = %.4f: gauge %+.6e' % (bg, hg), flush=True)
print('time %.0f s' % (time.time() - t00))
