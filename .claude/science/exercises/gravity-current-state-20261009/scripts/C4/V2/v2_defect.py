"""V2 (b1): size of the on-shell 2<->2 Ward defect of the dressed momentum, vs momentum scale.

The defect is basis-free: on an elastic 2->2 shell (k1,k2 -> k3,k4; k1+k2 = k3+k4 (mod 2pi); w1+w2 = w3+w4)
it is Delta P = sum f(in) - sum f(out) (the matrix element of P_in - P_out = [S-matrix, P] per unit T-matrix),
for the free momentum symbol f.  Under uniform strain h the transported lab momenta then violate lab-momentum
conservation by eps*hhat.DeltaP, so the local coupling must scatter into momenta off the transported ones by
delta q = eps*hhat.DeltaP: relative size |DeltaP|/|P_in|.

Exact identity (normal process, Q = k1+k2 = k3+k4 exactly, k1,2 = Q/2 +- kap, k3,4 = Q/2 +- kap'), f = sin:
   DeltaP_i = 2 sin(Q_i/2) (cos kap_i - cos kap'_i)                      (per axis, exact)
Umklapp (k3+k4 = k1+k2 + 2 pi n): the Q/2 of the out pair shifts by pi n, the sign flips: O(1) defect.
Improved symbol f2 = (4/3) sin k - (1/6) sin 2k = k - k^5/30 + ...  (defect pushed to higher order).
Sampling: k1,k2 uniform in the ball |k| < s; kap' = t d with random unit d, t from the energy shell (brentq).
"""
import numpy as np, sys
from scipy.optimize import brentq
rng = np.random.default_rng(11)
def w(k, m): return np.sqrt(m**2 + np.sum(4*np.sin(k/2)**2, axis=-1))
f1 = np.sin
def f2(k): return (4/3)*np.sin(k) - (1/6)*np.sin(2*k)
def ball(s):
    while True:
        v = rng.uniform(-s, s, 3)
        if np.linalg.norm(v) < s: return v
def sample(m, s, n=3000):
    rows = []
    while len(rows) < n:
        k1, k2 = ball(s), ball(s); Q = k1 + k2; kap = (k1 - k2)/2; E = w(k1, m) + w(k2, m)
        d = rng.normal(size=3); d /= np.linalg.norm(d)
        g = lambda t: w(Q/2 + t*d, m) + w(Q/2 - t*d, m) - E
        if g(0.0) > 0: continue
        tmax = 4*s + 0.5
        if g(tmax) < 0: continue
        t = brentq(g, 0.0, tmax, xtol=1e-15, rtol=1e-15)
        kp = t*d; k3, k4 = Q/2 + kp, Q/2 - kp
        if np.linalg.norm(kp - kap) < 1e-3*s or np.linalg.norm(kp + kap) < 1e-3*s: continue  # trivial
        res = abs(g(t))
        D1 = f1(k1) + f1(k2) - f1(k3) - f1(k4)
        Dident = 2*np.sin(Q/2)*(np.cos(kap) - np.cos(kp))
        D2 = f2(k1) + f2(k2) - f2(k3) - f2(k4)
        Pin1 = np.linalg.norm(f1(k1) + f1(k2)); Pin2 = np.linalg.norm(f2(k1) + f2(k2))
        # natural normalisation at low k: |Q| * |kappa|^2 (relative defect / (ka)^2)
        rows.append((np.linalg.norm(D1)/Pin1, np.linalg.norm(D2)/Pin2, np.max(np.abs(D1 - Dident)), res,
                     np.linalg.norm(D1)/(np.linalg.norm(Q)*max(np.linalg.norm(kap), np.linalg.norm(kp))**2)))
    return np.array(rows)
for m in [1.0, 0.3]:
    print(f'--- m = {m} (normal processes; momenta in a ball of radius s = k_max a)')
    prev = None
    for s in [0.01, 0.03, 0.1, 0.3, 1.0]:
        R = sample(m, s)
        med1, med2 = np.median(R[:, 0]), np.median(R[:, 1])
        line = (f's={s:5.2f}: rel defect |dP|/|P_in| (f=sin): median {med1:.3e}, 90pct {np.percentile(R[:,0],90):.3e}, '
                f'median/s^2 {med1/s**2:.4f} | improved f2: median {med2:.3e}, median/s^4 {med2/s**4:.4f} | '
                f'|dP|/(|Q| kap^2) median {np.median(R[:,4]):.4f} | identity err {R[:,2].max():.1e}, shell resid {R[:,3].max():.1e}')
        if prev is not None:
            line += f' | local slope (f=sin) {np.log(med1/prev[0])/np.log(s/prev[1]):.3f}'
        prev = (med1, s)
        print(line); sys.stdout.flush()
# Physical translation: relative momentum mismatch per collision in a field of strain eps: eps*(k a)^2/c
print('--- physical (a = l_P = 1.616e-35 m; E_P = 1.22e19 GeV): rel. defect ~ c*(E/E_P)^2 with c ~ median/s^2 above')
for name, E in [('nuclear Fermi momentum 0.25 GeV', 0.25), ('LHC parton 6.5e3 GeV', 6.5e3), ('UHECR 1e11 GeV (1e20 eV)', 1e11)]:
    ka = E/1.22e19
    print(f'  {name}: ka = {ka:.2e}, (ka)^2 = {ka**2:.2e}; times strain eps ~ 7e-10 (Earth surface) -> {7e-10*ka**2:.1e}')
