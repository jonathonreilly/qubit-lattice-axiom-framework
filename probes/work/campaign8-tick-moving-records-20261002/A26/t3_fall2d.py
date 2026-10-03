"""A26 t3_fall2d: 2D fall in a uniform static field gradient along y (supplied toy).
U = g (y - y0) in cells, uniform in x (x periodic, packets may wrap in x).  N = 1 - U, h_ij = 2U delta_ij.
Measures transverse acceleration a_y from a quadratic fit of <y>(t); compares with the exact-dispersion semiclassical
prediction a = -(d omega/dU) (dU/dy) (d2 omega/dKy2) at the carrier, and with c^2 g (Newtonian, c = sin th0).
Cases: one-site masses at rest (two sizes), one-site mass moving at ~0.6c (field vs lapse-only coupling),
two-site x-masses at rest with operator-support (os) vs stress (st) coupling."""
import os, sys, signal, time
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(58)
import numpy as np
from rs2d import Walk2D, packet, centroid, bloch_batch

Lx, th0 = 44, 0.4
g = float(os.environ.get("A26_G", "2e-4")); T = int(os.environ.get("A26_T", "1000")); sig = float(os.environ.get("A26_SIGF", "36"))
Ly = 2 * int(12 * sig)                    # sites: 12 sigma cells wide, 6 sigma margin each side
Q1 = 2 * np.pi / (Lx // 2)          # commensurate carrier for the moving stripe (~0.2856)
y0 = Ly / 4.0
yc = np.ones((Lx, 1)) * (np.arange(Ly)[None, :] / 2.0)
U = g * (yc - y0)
c2g = np.sin(th0) ** 2 * g
which = sys.argv[1:] if len(sys.argv) > 1 else ["rest15", "rest08", "move15", "move15_lapse", "move06", "move06_lapse", "os", "st"]
cases = {
    "rest15": dict(mu=0.15, q0=0.0, rule='field'),
    "rest08": dict(mu=0.08, q0=0.0, rule='field'),
    "move15": dict(mu=0.15, q0=Q1, rule='field'),
    "move15_lapse": dict(mu=0.15, q0=Q1, rule='lapse'),
    "move06": dict(mu=0.06, q0=Q1, rule='field'),
    "move06_lapse": dict(mu=0.06, q0=Q1, rule='lapse'),
    "os": dict(delta=0.075, q0=0.0, rule='field', mode='os'),
    "st": dict(delta=0.075, q0=0.0, rule='field', mode='st'),
}


def om_upper(K, Uu, c):
    kw = dict(mu=c.get('mu', 0.0), delta=c.get('delta', 0.0), mode=c.get('mode', 'os'), N=1 - Uu)
    if c['rule'] == 'field':
        kw.update(fx=1 - Uu, fy=1 - Uu)
    if ALT:
        Um = bloch_batch(np.array([K]), th0, order='alt2', **kw)[0]
        return 0.5 * np.sort(-np.angle(np.linalg.eigvals(Um)))[2:].mean()
    Um = bloch_batch(np.array([K]), th0, **kw)[0]
    return np.sort(-np.angle(np.linalg.eigvals(Um)))[2:].mean()


flat = os.environ.get("A26_FLAT", "0") == "1"
TASTE = {"": None, "+": 1, "-": -1}[os.environ.get("A26_TASTE", "")]
ALT = os.environ.get("A26_ALT", "0") == "1"
for name in which:
    c = cases[name]
    t0 = time.time()
    Uf = 0 * U if flat else U
    W = Walk2D(Lx, Ly, th0, N=1 - Uf, hxx=2 * Uf, hyy=2 * Uf, mu=c.get('mu', 0.0), delta=c.get('delta', 0.0),
               mode=c.get('mode', 'os'), rule=c['rule'])
    W.alt = ALT
    psi = packet(Lx, Ly, (Lx // 4, y0), (c['q0'], 0.0), sig, th0, mu=c.get('mu', 0.0), delta=c.get('delta', 0.0),
                 mode=c.get('mode', 'os'), stripe=True, taste=TASTE, order='alt2' if ALT else 'xy')
    ts, ys = [], []
    for t in range(T + 1):
        if t % 10 == 0:          # even times only (alternating order has period 2)
            ts.append(t); ys.append(centroid(psi)[1] / 2.0)
        psi = W.step(psi)
    a_meas = 2 * np.polyfit(np.array(ts, float), np.array(ys), 2)[0]
    K0 = np.array([np.pi + c['q0'], np.pi])
    dU, dK = 1e-5, 1e-3
    domdU = (om_upper(K0, dU, c) - om_upper(K0, -dU, c)) / (2 * dU)
    d2 = (om_upper(K0 + [0, dK], 0, c) - 2 * om_upper(K0, 0, c) + om_upper(K0 - [0, dK], 0, c)) / dK ** 2
    vx = (om_upper(K0 + [dK, 0], 0, c) - om_upper(K0 - [dK, 0], 0, c)) / (2 * dK)
    a_sc = -domdU * g * d2
    if flat:
        print("%-13s FLAT reference a_y = %.4e (%.1f s)" % (name, a_meas, time.time() - t0)); continue
    print(("alt=%d T3=%s " % (ALT, os.environ.get("A26_TASTE", "mix"))) + "%-13s a_y = %.4e ; semiclassical %.4e (ratio %.4f) ; a_y/(c^2 g) = %.4f ; carrier speed %.3f c ; %.1f s"
          % (name, a_meas, a_sc, a_meas / a_sc, a_meas / c2g, vx / np.sin(th0), time.time() - t0))
