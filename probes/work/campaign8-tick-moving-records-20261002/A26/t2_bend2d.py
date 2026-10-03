"""A26 t2_bend2d: 2D packet deflection past a static conformal field bump (supplied toy).
Field: U = U0 exp(-r^2/w^2) (r in cells), lapse N = 1 - U, spatial metric h_ij = 2U delta_ij (A23 D16 form).
Couplings: rule in {flat, field (Nb*eb), lapse (Nb), frame (eb)}; one-site mass mu (0 = massless).
Usage: t2_bend2d.py RULE MU Q0 TAG ; saves centroid trajectory to bend_TAG_RULE.npy
"""
import os, sys, signal, time
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(58)
import numpy as np
from rs2d import Walk2D, packet, centroid

rule, mu, q0, tag = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
T = int(sys.argv[5]) if len(sys.argv) > 5 else 600
import json
U0 = float(os.environ.get("A26_U0", "0.03")); sig = float(os.environ.get("A26_SIG", "10"))
Ly = int(os.environ.get("A26_LY", "320"))
Lx = 640
th0, w = 0.4, 25.0
xb, b = 150.0, 18.0
yb = Ly / 4 - 10.0
json.dump(dict(U0=U0, sig=sig, Ly=Ly, yb=yb, b=b, w=w, xb=xb, th0=th0, mu=mu, q0=q0), open("bend_%s_meta.json" % tag, "w"))
x = np.arange(Lx)[:, None] / 2.0; y = np.arange(Ly)[None, :] / 2.0
U = U0 * np.exp(-((x - xb) ** 2 + (y - yb) ** 2) / w ** 2)
if rule == 'flat':
    W = Walk2D(Lx, Ly, th0, mu=mu)
else:
    W = Walk2D(Lx, Ly, th0, N=1 - U, hxx=2 * U, hyy=2 * U, mu=mu, rule=rule)
psi = packet(Lx, Ly, (40, yb + b), (q0, 0.0), sig, th0, mu=mu)
t0 = time.time()
traj = []
for t in range(T + 1):
    if t % 10 == 0:
        cx, cy, nrm = centroid(psi)
        p = np.abs(psi) ** 2
        sy = np.sqrt(((np.arange(Ly) - cy) ** 2 @ p.sum(0)) / p.sum())
        traj.append((t, cx / 2, cy / 2, nrm, sy / 2))
    psi = W.step(psi)
traj = np.array(traj)
np.save("bend_%s_%s.npy" % (tag, rule), traj)
print("%s %s: %d cycles in %.1f s; final centroid (cells) x=%.2f y=%.3f, norm-1 %.1e, y-std %.2f"
      % (tag, rule, T, time.time() - t0, traj[-1, 1], traj[-1, 2], traj[-1, 3] - 1, traj[-1, 4]))
