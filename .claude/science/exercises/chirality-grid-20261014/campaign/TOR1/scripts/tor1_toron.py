"""TOR-1 (b3, b''-i): toron-torus data vs size: winding of Gam_t, base holonomies, spread of Gam_t (the size of Luscher's
finite-volume connection S on the toron torus: max|S_t| = spread/2pi).  usage: python3 tor1_toron.py L1 L2 ... (square tori) [Lx:Lt]"""
import sys, time
import numpy as np
from tor1_lib import *
t0 = time.time(); rows = []
for arg in sys.argv[1:]:
    Lx, Lt = (int(a) for a in arg.split(':')) if ':' in arg else (int(arg), int(arg))
    S = Torus(Lx, Lt, light=True)
    for model in ('11112', 'L1'):
        out = {}
        for nl in (256, 512):
            tor = Toron(S, model); g = 2 * np.pi * np.arange(257) / 256
            gam = np.unwrap(Richardson_loop(tor, g, nl)); wind = (gam[-1] - gam[0]) / (2 * np.pi)
            hx0 = Richardson_loop(tor, np.array([0.0]), nl, which='x')[0]
            spread = np.ptp(gam - wind * g)
            # also Gam_x(wt): the w_x-cycle holonomy as a function of wt (the other orientation)
            gx = np.unwrap(Richardson_loop(tor, g, nl, which='x')); windx = (gx[-1] - gx[0]) / (2 * np.pi)
            out[nl] = (wind, windx, np.angle(np.exp(1j * gam[0])), np.angle(np.exp(1j * hx0)), spread, np.ptp(gx - windx * g))
        a, b = out[256], out[512]
        print(f"Lx={Lx} Lt={Lt} {model:5s}: wind_t {b[0]:+.6f} wind_x {b[1]:+.6f} | h_t(0) {b[2]:+.2e} h_x(0) {b[3]:+.2e} | spread Gam_t {b[4]:.6e} "
              f"(nloop change {abs(a[4]-b[4]):.1e}) spread Gam_x {b[5]:.6e} [{time.time()-t0:.0f}s]", flush=True)
        rows.append((Lx, Lt, model == 'L1', b[0], b[1], b[2], b[3], b[4], b[5]))
np.save('toron_scaling_' + '_'.join(a.replace(':', 'x') for a in sys.argv[1:]) + '.npy', np.array(rows))
