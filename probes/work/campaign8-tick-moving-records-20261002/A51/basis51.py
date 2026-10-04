"""A51 basis51: (i) soldered images of dual class sums are covariant under the 24 exact soldered turns; (ii) class tables;
(iii) estimator timing per sample.  Usage: basis51.py"""
import sys, signal, time, numpy as np
signal.alarm(280)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a51lib import *
t0 = time.time()
worst = 0.
for k in [(0, 0, 1), (0, 1, 1), (0, 0, 2), (1, 1, 1), (0, 1, 2), (1, 1, 2), (1, 2, 3), (0, 3, 3), (2, 2, 3), (1, 3, 4), (0, 2, 5)]:
    op = soldered_class_op(k); dv = cov_defect(op); ga = gavg(op)
    dd = max(abs(ga.get(q, 0) - v) for q, v in op.items()); worst = max(worst, dv, dd)
    print(f"class {k}: {len(op)} strings, cov defect {dv:.1e}, |gavg - op| {dd:.1e}")
print(f"worst covariance defect {worst:.1e}")
# (1,0,0) image equals A49's dual J1 = -J1 + 2 K1 (unnormalized)
B2 = {nm: op for nm, c, op in bilinear_basis()}
o1 = normalize(soldered_class_op((0, 0, 1)))
dJ1 = normalize({q: -B2["J1"].get(q, 0) * 3 + 2 * B2["K1"].get(q, 0) * np.sqrt(3) for q in set(B2["J1"]) | set(B2["K1"])})
print("dual-J1 match:", max(abs(o1.get(q, 0) - dJ1.get(q, 0)) for q in set(o1) | set(dJ1)))
for L in (6, 8, 10):
    cl = cube(L); ks, K, m = class_matrix(cl, L)
    assert m.sum() == cl.N - 1 and (K == K.T).all()
    print(f"L={L}: {len(ks)} classes, sum m_c = {m.sum()} = N-1; shells |d|^2: {sorted(set(sum(c*c for c in k) for k in ks))}")
print(f"tables {time.time()-t0:.1f}s")
for L in (8, 10):
    cl = cube(L); ks, K, m = class_matrix(cl, L); N = cl.N
    Phi, gap = mf_state(cl); rows0 = 2 * np.arange(N); rng = np.random.default_rng(1)
    s = rng.permutation(np.r_[np.zeros(N // 2, int), np.ones(N // 2, int)]); Q = np.linalg.inv(Phi[rows0 + s])
    t1 = time.time(); E = class_estimators(Phi, Q, s, K.ravel(), len(ks), rows0); dt = time.time() - t1
    print(f"L={L}: one class-estimator call {dt*1e3:.0f} ms; Casimir check sum_c E_c = {E.sum():.6f} vs -3N/2 = {-1.5*N}")
