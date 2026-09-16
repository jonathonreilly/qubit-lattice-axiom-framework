# The six-axis formation law in level time at the sphere weight restricted to the axes: (p, q, r) = (e^beta, e^-beta, 1).
# Values 0..5 = +e1,-e1,+e2,-e2,+e3,-e3; phi(v,v') = p same, q antipodal, r orthogonal. Periodic L x L plane, aligned start (value 0).
import numpy as np, sys, time
beta = float(sys.argv[1]); L = int(sys.argv[2]); T = int(sys.argv[3])
p, q, r = np.exp(beta), np.exp(-beta), 1.0
phi = np.full((6, 6), r)
for v in range(6):
    phi[v, v] = p; phi[v, v ^ 1] = q
rng = np.random.default_rng(7)
s = np.zeros((L, L), dtype=np.int64)
rec = max(1, T // 40); t0 = time.time()
print(f"six-axis beta={beta} (p,q,r)=({p:.4g},{q:.4g},{r}) L={L} T={T}")
for t in range(1, T + 1):
    p1, p2, p3 = s, np.roll(s, 1, axis=0), np.roll(s, 1, axis=1)
    W = phi[:, p1] * phi[:, p2] * phi[:, p3]          # shape (6, L, L)
    W = W / W.sum(axis=0, keepdims=True)
    C = np.cumsum(W, axis=0)
    U = rng.random((L, L))
    s = (U[None, :, :] > C).sum(axis=0)
    s = np.minimum(s, 5)
    if t % rec == 0:
        print(f"  t={t:6d}  frac(value 0)={np.mean(s == 0):.5f}")
print(f"({time.time()-t0:.0f}s)")
