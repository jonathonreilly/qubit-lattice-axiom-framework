"""NT-1' descriptive: x-profile of the Q-part and total response split by distance of the pair from the open time ends,
from saved loc_chi_*.npy (no new physics runs).  usage: python3 nt1p_xprofile_rows.py"""
import numpy as np
from nt1p_lib import Strip
for model in ('11112', 'L1'):
    for Lx in (4, 6, 8):
        T = 4; S = Strip(Lx, T); chi = np.load(f"loc_chi_Lx{Lx}_Lt8_{model}_s301.npy")
        mid = np.array([((l[4] + 0.5, l[5]) if l[2] == 'x' else (l[4], l[5] + 0.5)) for l in S.L])
        dxm = np.abs(mid[:, None, 0] - mid[None, :, 0]); dxm = np.minimum(dxm, Lx - dxm); dtm = np.abs(mid[:, None, 1] - mid[None, :, 1])
        edge = np.minimum(mid[:, 1] - (-T + 1), T - mid[:, 1])          # distance of link midpoint from the nearer open end
        sel = dtm <= 0.5 + 1e-9
        for lab, emin in (('all', -1), ('>=2 from ends', 2.0)):
            ok = sel & (edge[:, None] >= emin) & (edge[None, :] >= emin)
            sv = np.arange(0.5, Lx / 2 + 0.25, 0.5)
            tot = [chi[0][ok & (np.abs(dxm - s) < 1e-9)].max() if np.any(ok & (np.abs(dxm - s) < 1e-9)) else np.nan for s in sv]
            q = [chi[2][ok & (np.abs(dxm - s) < 1e-9)].max() if np.any(ok & (np.abs(dxm - s) < 1e-9)) else np.nan for s in sv]
            print(f"{model:5s} Lx={Lx} [{lab:13s}] s=" + " ".join(f"{s:.1f}" for s in sv) + "\n      total: " + " ".join(f"{v:.2e}" for v in tot) + "\n      Q    : " + " ".join(f"{v:.2e}" for v in q))
