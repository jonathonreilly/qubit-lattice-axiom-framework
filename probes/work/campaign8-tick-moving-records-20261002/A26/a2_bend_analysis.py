"""A26 a2_bend_analysis: deflection angles from t2_bend2d trajectories vs exact-dispersion ray prediction.
Ray (eikonal, first order in U0): delta(b') = -(d omega/dU) (d2 omega/dKy2) / vx^2 * I(b'),
I(b') = int dU/dy dx = -2 sqrt(pi) U0 (b'/w) exp(-b'^2/w^2); averaged over a Gaussian of impact parameters with the
packet's measured transverse std when its centroid passes the bump.  Usage: a2_bend_analysis.py TAG MU Q0 RULES..."""
import os, sys, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(58)
import numpy as np
from rs2d import bloch_batch

tag, mu, q0 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
rules = sys.argv[4:]
import json
meta = json.load(open("bend_%s_meta.json" % tag))
th0, U0, w, xb, b = meta['th0'], meta['U0'], meta['w'], meta['xb'], meta['b']


def omega(K, U, rule):
    kw = dict(mu=mu)
    if rule == 'field':
        kw.update(N=1 - U, fx=1 - U, fy=1 - U)
    elif rule == 'lapse':
        kw.update(N=1 - U)
    elif rule == 'frame':
        kw.update(fx=1 - U, fy=1 - U)
    Um = bloch_batch(np.array([K]), th0, **kw)[0]
    om = np.sort(-np.angle(np.linalg.eigvals(Um)))
    return om[2:].mean()                       # mean of the two upper bands


fl = np.load("bend_%s_flat.npy" % tag)
K0 = np.array([np.pi + q0, np.pi])
dK, dU = 1e-4, 1e-5
vx = (omega(K0 + [dK, 0], 0, 'flat') - omega(K0 - [dK, 0], 0, 'flat')) / (2 * dK)
d2y = (omega(K0 + [0, dK], 0, 'flat') - 2 * omega(K0, 0, 'flat') + omega(K0 - [0, dK], 0, 'flat')) / dK ** 2
i_b = np.argmin(np.abs(fl[:, 1] - xb))
sy_b = fl[i_b, 4]
bs = b + sy_b * np.linspace(-4, 4, 801)
wts = np.exp(-0.5 * ((bs - b) / sy_b) ** 2); wts /= wts.sum()
Ib = -2 * np.sqrt(np.pi) * U0 * (bs / w) * np.exp(-bs ** 2 / w ** 2)
late = fl[:, 1] > xb + 3 * w
sl_flat = np.polyfit(fl[late, 1], fl[late, 2], 1)[0]
early = fl[:, 1] < xb - 3.5 * w
sl_flat_e = np.polyfit(fl[early, 1], fl[early, 2], 1)[0]
print("tag %s mu=%.3f q0=%.2f: group velocity vx = %.5f cells/cycle (light cone sin th0 = %.5f); packet y-std at bump %.2f cells;"
      " flat slopes early %.2e late %.2e" % (tag, mu, q0, vx, np.sin(th0), sy_b, sl_flat_e, sl_flat))
res = {}
for rule in rules:
    tr = np.load("bend_%s_%s.npy" % (tag, rule))
    lt = tr[:, 1] > xb + 3 * w
    sl = np.polyfit(tr[lt, 1], tr[lt, 2], 1)[0] - sl_flat
    dodU = (omega(K0, dU, rule) - omega(K0, -dU, rule)) / (2 * dU)
    pred_point = -dodU * d2y / vx ** 2 * (-2 * np.sqrt(np.pi) * U0 * (b / w) * np.exp(-b ** 2 / w ** 2))
    pred_avg = -dodU * d2y / vx ** 2 * np.sum(wts * Ib)
    res[rule] = sl
    print("   %-6s measured deflection %.5f rad ; ray prediction (point b) %.5f, (averaged over impact spread) %.5f ;"
          " measured/averaged %.4f ; d omega/dU = %.5f" % (rule, sl, pred_point, pred_avg, sl / pred_avg, dodU))
if 'field' in res and 'lapse' in res:
    print("   deflection ratio field/lapse = %.4f  ->  measured (1 + gamma) for these packets" % (res['field'] / res['lapse']))
    om0 = omega(K0, 0, 'flat')
    v = vx / np.sin(th0)
    print("   eikonal expectation of the ratio: massless 2 ; massive (1+v^2) with v = %.4f c -> %.4f; exact symbol ratio %.4f"
          % (v, 1 + v ** 2, ((omega(K0, dU, 'field') - omega(K0, -dU, 'field')) / (omega(K0, dU, 'lapse') - omega(K0, -dU, 'lapse')))))
