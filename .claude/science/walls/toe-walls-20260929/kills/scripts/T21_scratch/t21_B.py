"""Test B: walker H + c n_x on typical Gibbs arrangements of the record gas."""
import sys, time
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from t21_common import *

L = int(sys.argv[1]); nsamp = int(sys.argv[2]); cs = [float(x) for x in sys.argv[3].split(',')]
gs = [float(x) for x in sys.argv[4].split(',')]
N = L ** 3
nb = neighbours(L)
eps = eps_array(L).astype(np.int8)
H0 = walker_H0(L)
print(f"L={L} N={N} dim={2*N}  samples={nsamp}  c={cs}  g={gs}")
# reference: ideal chessboard
for c in cs:
    E = spectrum(H0, (1 + eps) // 2, c)
    print(f"ideal chessboard c={c}: w_max/c={gap_metrics(E,c)[0]:.6f} f_in={gap_metrics(E,c)[1]:.4f} dmin={gap_metrics(E,c)[2]:.6f} (c/2={c/2})")
    sys.stdout.flush()
for g in gs:
    K = np.log(1.0 / g) / 4.0
    pbond = 1.0 - np.exp(-2.0 * K)
    seed_numba(1234 + int(1000 * g))
    sig = np.ones(N, dtype=np.int8)
    wolff_steps(sig, nb, pbond, 500, 0)
    samples = []
    for _ in range(nsamp):
        wolff_steps(sig, nb, pbond, 40, 0)
        s = sig.copy()
        if s.sum() < 0:
            s = -s       # fix the A sector (translate by one site)
        samples.append(s)
    for c in cs:
        w = []; f = []; d = []; M = []
        t0 = time.time()
        for s in samples:
            n = (1 + eps * s) // 2
            E = spectrum(H0, n, c)
            a, b, e = gap_metrics(E, c)
            w.append(a); f.append(b); d.append(e); M.append(s.mean())
        w, f, d = map(np.array, (w, f, d))
        print(f"g={g:.3f} c={c:.1f} <M>={np.mean(M):.3f} | w_max/c med={np.median(w):.3f} min={w.min():.3f} max={w.max():.3f} | "
              f"f_in med={np.median(f):.4f} max={f.max():.4f} | dmin/(c/2) med={np.median(d)/(c/2):.3f} min={d.min()/(c/2):.3f}   ({time.time()-t0:.0f}s)")
        sys.stdout.flush()
