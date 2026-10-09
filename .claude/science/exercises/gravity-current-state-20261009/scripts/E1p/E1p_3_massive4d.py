"""E1' (c): per-realization Johnston massive path sum on 4D Poisson diamonds.
Bottom tip y = source (point-to-point K(top,y)); smeared source J = Euclidean Gaussian (width w) centred at
t_c = 3w on the axis; observation point = top tip (a single element).
Saves per-realization arrays to ../out/massive4d_T{T}.npz.
Usage: python E1p_3_massive4d.py T nreal seed
"""
import sys, time, os
import numpy as np
from e1p_core import sprinkle4d_diamond, past_links, path_sums, two_link_count, A4

T = float(sys.argv[1]); nreal = int(sys.argv[2]); seed = int(sys.argv[3])
mT = np.array([0.0, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0])
m = mT / T
avec = np.full(len(m), A4); bvec = -m**2
w = 1.5; tc = 3.0 * w
rng = np.random.default_rng(seed)
Kt = np.zeros((nreal, len(m))); KJt = np.zeros((nreal, len(m)))
L2 = np.zeros(nreal, np.int64); Nel = np.zeros(nreal, np.int64); nlk = np.zeros(nreal, np.int64)
t0 = time.time()
for r in range(nreal):
    P = sprinkle4d_diamond(T, rng)
    J = np.exp(-((P[:, 0] - tc)**2 + (P[:, 1:]**2).sum(1)) / (2 * w * w))
    J[0] = 0.0; J[-1] = 0.0
    ip, ix = past_links(P)
    K, KJ = path_sums(ip, ix, 0, J, avec, bvec)
    top = len(P) - 1
    Kt[r] = K[top]; KJt[r] = KJ[top]
    L2[r] = two_link_count(ip, ix, top, 0)
    Nel[r] = len(P); nlk[r] = ip[top + 1] - ip[top]
    if r % max(1, nreal // 10) == 0:
        print(f"T={T} r={r} N={len(P)} L2={L2[r]} elapsed={time.time()-t0:.1f}s", flush=True)
os.makedirs("../out", exist_ok=True)
np.savez(f"../out/massive4d_T{int(T)}_s{seed}.npz", T=T, mT=mT, m=m, Kt=Kt, KJt=KJt, L2=L2, Nel=Nel, nlk=nlk, w=w, tc=tc)
print("done", time.time() - t0)
