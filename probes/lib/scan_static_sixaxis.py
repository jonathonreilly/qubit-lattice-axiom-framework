# Six-axis static law on a periodic L^3 lattice at (p, q, r) = (p, 1, 2): heat-bath (Gibbs) checkerboard sweeps; the fraction of the
# majority value after equilibration, from an aligned start and from a random start.
import numpy as np, sys, time
_argv = sys.argv[:]
QR = (1.0, 2.0)
if '--qr' in _argv:
    i = _argv.index('--qr'); QR = (float(_argv[i + 1]), float(_argv[i + 2])); del _argv[i:i + 3]
sys.argv = _argv
L, sweeps = int(sys.argv[1]), int(sys.argv[2]); ps = [float(x) for x in sys.argv[3:]]
rng = np.random.default_rng(2)
idx = np.indices((L, L, L)).sum(0) % 2
print(f"six-axis static law at (p,1,2), L={L}, sweeps={sweeps}; order = mean fraction of the majority value over the last half (aligned start | random start)")
for p in ps:
    q, r = QR
    phi = np.full((6, 6), r)
    for v in range(6):
        phi[v, v] = p; phi[v, v ^ 1] = q
    res = []
    for start in ("aligned", "random"):
        s = np.zeros((L, L, L), dtype=np.int64) if start == "aligned" else rng.integers(0, 6, (L, L, L))
        ords = []; t0 = time.time()
        for sw in range(sweeps):
            for par in (0, 1):
                W = np.ones((6, L, L, L))
                for ax in range(3):
                    for sh in (1, -1):
                        W = W * phi[:, np.roll(s, sh, ax)]
                C = np.cumsum(W / W.sum(0, keepdims=True), axis=0)
                new = np.minimum((rng.random((L, L, L))[None] > C).sum(0), 5)
                s = np.where(idx == par, new, s)
            if sw >= sweeps // 2:
                counts = np.bincount(s.ravel(), minlength=6); ords.append(counts.max() / L**3)
        res.append(np.mean(ords))
    print(f"  p={p:5.2f}: order {res[0]:.4f} | {res[1]:.4f}   ({time.time()-t0:.0f}s per start)")
