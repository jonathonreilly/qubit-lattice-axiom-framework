"""E3 (a4): precision of the quasicrystal mean stiffness, and is a small value protected or accidental?
(1) truncation check: same window offset gamma, patches Rp = 7 and Rp = 9; per-site e'' of common points vs distance to
    the Rp = 7 edge.  (2) 12 generic patches (Rp = 9) for each kernel range R = 1.8 (R3's) and R = 2.2; boson m2 = 1.
    Pooled interior mean per channel with patch-to-patch SE.  A protected zero must survive the change of kernel.
usage: python3 E3_a4_qc_precision.py check | python3 E3_a4_qc_precision.py run R"""
import numpy as np, sys, time
import E3_a_core as q, e23_core as c
rng = np.random.default_rng(2024)
def gen_gamma():
    while True:
        v = rng.uniform(-0.6, 0.6, 3)
        if np.linalg.norm(v) < 0.6:
            return v
if sys.argv[1] == 'check':
    gam = gen_gamma()
    X7, _ = q.ico_patch(7.0, gam); X9, _ = q.ico_patch(9.0, gam)
    _, a = q.local_stiffness(X7); _, b = q.local_stiffness(X9)
    from scipy.spatial import cKDTree
    d, idx = cKDTree(X9).query(X7); assert d.max() < 1e-9
    diff = np.abs(a - b[idx]); edge = 7.0 - np.linalg.norm(X7, axis=1)
    for buf in [1.5, 2.0, 2.5, 3.0, 3.5]:
        m = edge > buf
        print(f"buffer {buf}: n={m.sum():4d}  max|de''| {diff[m].max():.2e}  mean|de''| {diff[m].mean():.2e}  bias of mean {np.abs((a[m]-b[idx][m]).mean(0)).max():.2e}")
else:
    c.R_PD = float(sys.argv[2])
    for k in range(12):
        t0 = time.time(); gam = gen_gamma()
        X, perp = q.ico_patch(9.0, gam); e1, e2 = q.local_stiffness(X)
        np.savez(f"E3_a4_R{c.R_PD}_{k}.npz", X=X, perp=perp, e1=e1, e2=e2, Rp=9.0, buf=2.5, gamma=gam)
        print(f"R={c.R_PD} patch {k} N={len(X)} [{time.time()-t0:.0f}s]", flush=True)
