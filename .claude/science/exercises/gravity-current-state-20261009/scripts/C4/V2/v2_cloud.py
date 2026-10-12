"""V2 (b3): where the vacuum's virtual 4-particle cloud lives in momentum space, and how large the 2<->2 Ward
defect is on it.  The cloud is S|0> = T|0>, T = -(1/24) sum_{K=0} prod_l alpha(k_l) a+^4 / sum_l w(k_l)
(Kato/V1 first-order dressing).  Its weight on (k1..k4), K = 0:  p ~ prod_l 1/(2 w_l) / (sum_l w_l)^2.
If the dropped scattering-sector part is referenced to the FREE vacuum (not to Omega_h), the leading feedback into
the vacuum energy is the cloud diagram  lambda^2 <0_h| T^+ Delta T |0_h>  (Delta = split-convention difference,
O(lambda eps)), i.e. two cloud legs scatter through the defect.  This script measures, on the cloud,
  (i)   <1 - cos k_x>         (lattice-scale or not)
  (ii)  the Ward-defect numerator |f(k1)+f(k2)-f(k3')-f(k4')| for a 2->2 sub-scattering of legs (1,2)
        relative to |f(k1)+f(k2)|: we use the exact identity |DeltaP| = |2 sin(Q/2)(cos kap - cos kap')| with
        kap' a random elastic re-direction of the pair (same pair energy), as in v2_defect.py.
Uniform MC over the BZ with importance weight p.
"""
import numpy as np
from scipy.optimize import brentq
rng = np.random.default_rng(5)
def w(k, m): return np.sqrt(m**2 + np.sum(4*np.sin(k/2)**2, axis=-1))
for m in [1.0, 0.3]:
    n = 400000
    k = rng.uniform(-np.pi, np.pi, (n, 3, 3)); k4 = -(k.sum(1))
    K = np.concatenate([k, k4[:, None, :]], axis=1)
    W = w(K, m)
    p = np.prod(1/(2*W), axis=1)/W.sum(1)**2; p /= p.sum()
    c = np.cos(K[:, 0, 0])
    print(f'm={m}: cloud <1-cos k_x> = {np.sum(p*(1-c)):.3f}  (uniform-BZ value 1.000); '
          f'<|k|> = {np.sum(p*np.linalg.norm(np.angle(np.exp(1j*K[:,0,:])),axis=1)):.3f}; '
          f'P(|k_leg| < 0.3) = {np.sum(p*(np.linalg.norm(np.angle(np.exp(1j*K[:,0,:])),axis=1)<0.3)):.4f}')
    # sub-scattering defect of pair (1,2) on cloud samples (importance resampling)
    idx = rng.choice(n, size=3000, p=p)
    rel = []; umk = 0
    for i in idx:
        k1, k2 = K[i, 0], K[i, 1]; E = w(k1, m) + w(k2, m)
        Q = k1 + k2; d = rng.normal(size=3); d /= np.linalg.norm(d)
        g = lambda t: w(Q/2 + t*d, m) + w(Q/2 - t*d, m) - E
        ts = np.linspace(0, np.pi*np.sqrt(3), 200); gv = np.array([g(t) for t in ts])
        j = np.where(np.sign(gv[:-1]) != np.sign(gv[1:]))[0]
        if len(j) == 0: continue
        t = brentq(g, ts[j[0]], ts[j[0]+1]); kp = t*d
        k3, k4 = Q/2 + kp, Q/2 - kp
        dP = np.sin(k1) + np.sin(k2) - np.sin(k3) - np.sin(k4)
        Pin = np.linalg.norm(np.sin(k1) + np.sin(k2))
        rel.append(np.linalg.norm(dP)/max(Pin, 1e-12))
        if np.max(np.abs(Q)) > np.pi: umk += 1   # out pair written about the un-reduced Q/2: flag lattice-scale Q
    rel = np.array(rel)
    print(f'      2->2 sub-scattering of two cloud legs: |DeltaP|/|P_pair| median {np.median(rel):.3f}, '
          f'25-75% [{np.percentile(rel,25):.3f}, {np.percentile(rel,75):.3f}]  (cf. 0.037 (ka)^2 at low k); '
          f'fraction with |Q_i| > pi: {umk/len(rel):.2f}')
