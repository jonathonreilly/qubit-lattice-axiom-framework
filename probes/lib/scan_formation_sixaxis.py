# Six-axis formation law (level automaton) at (p, q, r) = (p, 1, 2): memory of the aligned plane after T levels, scanning p.
import numpy as np, sys, time
_argv = sys.argv[:]
QR = (1.0, 2.0)
if '--qr' in _argv:
    i = _argv.index('--qr'); QR = (float(_argv[i + 1]), float(_argv[i + 2])); del _argv[i:i + 3]
sys.argv = _argv
L, T = int(sys.argv[1]), int(sys.argv[2]); ps = [float(x) for x in sys.argv[3:]]
rng = np.random.default_rng(1)
print(f"six-axis formation law at (p,1,2), L={L}, T={T}, aligned start; memory = fraction of the initial value at levels T/2..T (mean), and at T")
for p in ps:
    q, r = QR
    phi = np.full((6, 6), r)
    for v in range(6):
        phi[v, v] = p; phi[v, v ^ 1] = q
    s = np.zeros((L, L), dtype=np.int64); fr = []
    t0 = time.time()
    for t in range(1, T + 1):
        W = phi[:, s] * phi[:, np.roll(s, 1, 0)] * phi[:, np.roll(s, 1, 1)]
        C = np.cumsum(W / W.sum(0, keepdims=True), axis=0)
        s = np.minimum((rng.random((L, L))[None] > C).sum(0), 5)
        if t > T // 2: fr.append(np.mean(s == 0))
    print(f"  p={p:6.1f}: memory mean {np.mean(fr):.4f}  final {np.mean(s == 0):.4f}   ({time.time()-t0:.0f}s)")
