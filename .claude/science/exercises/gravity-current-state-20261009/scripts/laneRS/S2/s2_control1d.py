"""1D controls (Coulomb-only staggered QED; no transverse photon in 1D).
(i) generic 1D shells: are there nontrivial 2<->2 resonances (g(t)=eps(t)+eps(K-t) is not unimodal on the reduced circle)?
    odd null space on them.  (ii) the K=pi/2 branch (k,pi/2-k)->(-k,pi/2+k).  (iii) permutation-only rows: null = full
    with abs+rel tolerance (relative-only would report 0).  (iv) Cherenkov bound check: |eps(k)-eps(k')| <= omega(Q) for
    every full-zone Q = k-k' (mod pi-shifts), d=3 random points -> no O(e) pole on + band Moller shells."""
import itertools, numpy as np
from s2_core import *
rng = np.random.default_rng(5)
for m in (0.0, 0.5):
    S1 = Stag(1, m)
    q1 = sample_moller(S1, 400, rng, mode='generic', maxtries=40000)
    B = odd_basis(1, 16)
    tn = np.array([np.linalg.norm(moller_T(S1, *q, include_tr=False)[0]) for q in q1])
    print(f"    d=1 m={m}: shells with |T| > 1e-10: {np.sum(tn > 1e-10)} of {len(q1)} (only these constrain)")
    q1 = [q for q, t in zip(q1, tn) if t > 1e-10]
    A = np.array([np.sin(2*B@k1)+np.sin(2*B@k2)-np.sin(2*B@k3)-np.sin(2*B@k4) for (k1,k2,k3,k4) in q1]).reshape(len(q1), len(B))/np.sqrt(max(1,len(q1)))
    sv = np.linalg.svd(A, compute_uv=False) if len(q1) else np.zeros(0); tn = list(tn)
    print(f"(i) d=1 m={m}: {len(q1)} nontrivial generic shells, |T| median {np.median(tn) if tn else 0:.3e}; odd f R<=16: null dim {nullity(sv, len(B))} of {len(B)}; sv min {sv[-1] if len(sv) else 0:.3e}")
S1 = Stag(1, 0.5); B = odd_basis(1, 8)
rows = []
for kk in rng.uniform(-np.pi/2, np.pi/2, 200):
    k1, k2, k3, k4 = np.array([kk]), wrapr(np.array([np.pi/2-kk])), wrapr(np.array([-kk])), wrapr(np.array([np.pi/2+kk]))
    rows.append(np.sin(2*B@k1)+np.sin(2*B@k2)-np.sin(2*B@k3)-np.sin(2*B@k4))
sv = np.linalg.svd(np.array(rows)/np.sqrt(200), compute_uv=False)
print(f"(ii) d=1 K=pi/2 branch: odd null dim {nullity(sv, len(B))} of {len(B)} (sin 2k fails: row max {np.max(np.abs(np.array(rows)[:,0])):.3f})")
Atriv = np.array([np.sin(2*B*a)+np.sin(2*B*b)-np.sin(2*B*b)-np.sin(2*B*a) for a, b in rng.uniform(-1.5, 1.5, (50, 2))])[:, :, 0]
sv = np.linalg.svd(Atriv, compute_uv=False)
print(f"(iii) permutation-only rows: null dim {nullity(sv, len(B))} of {len(B)}; relative-only rule would give {int(np.sum(sv < 1e-9*sv[0]))}")
worst = -np.inf
for m in (0.0, 0.3, 1.0):
    for t in range(20000):
        k = rng.uniform(-np.pi/2, np.pi/2, 3); kp = rng.uniform(-np.pi/2, np.pi/2, 3)
        for mv in itertools.product(range(2), repeat=3):
            Q = wrapf(k - kp + np.pi*np.array(mv))
            worst = max(worst, abs(eps(k, m) - eps(kp, m)) - omega(Q))
print(f"(iv) max over 480000 (k,k',Q) of |eps(k)-eps(k')| - omega(Q) = {worst:.3e}  (<0: no + band O(e) emission pole)")
