"""A26 t4_shear2d: real-space response of massless packets to a uniform static TT shear in the x-y plane
(the local action of a z-travelling TT wave), for three fixed couplings (supplied toy).
Metric prediction: group velocity v^i ~ g^ij q_j, g^ij = delta - h  ->  for q along x: tilt angle atan(-h_xy);
for q along the diagonal (1,1) with plus shear h_xx = -h_yy = hp: tilt = atan((1+hp)/(1-hp)) - pi/4.
Usage: t4_shear2d.py CASE [TASTE]; CASE in flatx, BLx, P2x, FRx, flatd, BLd ; TASTE in +, - (taste-resolved packets)."""
import os, sys, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(58)
import numpy as np
from rs2d import Walk2D, packet, centroid

case = sys.argv[1]
taste = None if len(sys.argv) < 3 else (1 if sys.argv[2] == '+' else -1)
Lx, Ly, th0, T, sig, h = 400, 400, 0.4, 320, 10.0, 0.1
one = np.ones((Lx, Ly))
diag = case.endswith('d')
K0 = (0.5 / np.sqrt(2), 0.5 / np.sqrt(2)) if diag else (0.5, 0.0)
c0 = (40, 40) if diag else (40, 100)
kw = {}
if case.startswith('BL') and not diag:
    kw = dict()                                         # h_xy enters no axis-bond length: coupling sees nothing
elif case.startswith('BL') and diag:
    kw = dict(hxx=h * one, hyy=-h * one)                # plus shear through bond lengths
elif case.startswith('P2'):
    kw = dict(imx=-h / 2, imy=-h / 2)
elif case.startswith('FR'):
    kw = dict(beta=0.5 * np.arcsin(h) * one)
W = Walk2D(Lx, Ly, th0, **kw)
pk = dict(imx=kw.get('imx', 0.0), imy=kw.get('imy', 0.0))
if 'beta' in kw:
    pk['beta'] = 0.5 * np.arcsin(h)
if 'hxx' in kw:
    pk.update(fx=1 - h / 2, fy=1 + h / 2)
psi = packet(Lx, Ly, c0, K0, sig, th0, taste=taste, **pk)
xs, ys = [], []
for t in range(T + 1):
    if t % 10 == 0:
        cx, cy, _ = centroid(psi); xs.append(cx / 2); ys.append(cy / 2)
    psi = W.step(psi)
xs, ys = np.array(xs), np.array(ys)
np.save("shear_%s_%s.npy" % (case, 'mix' if taste is None else sys.argv[2]), np.column_stack([xs, ys]))
sl = np.polyfit(xs, ys, 1)[0]
print("%-6s taste %-3s: travelled (%.1f, %.1f) cells; direction angle %.5f rad (slope dy/dx %.5f)"
      % (case, 'mix' if taste is None else sys.argv[2], xs[-1] - xs[0], ys[-1] - ys[0], np.arctan2(ys[-1] - ys[0], xs[-1] - xs[0]), sl))
