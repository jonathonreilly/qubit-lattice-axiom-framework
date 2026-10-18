# Lorentzian shells (k_t = i omega): strain reading of the non-metric null direction vs the metric one
from common import *
from r14 import golden
def svn(k):
    s_ = np.sort(np.linalg.svd(Dc.Q(k), compute_uv=False)); return s_ / s_[-1]
for name, n in {'axis': (1, 0, 0), 'face': (1, 1, 0), 'generic': (3, 1, 2)}.items():
    n = np.array(n, float); n /= np.linalg.norm(n)
    for km in (0.06, 0.03):
        ks = km * n; oms = km * np.linspace(0.998, 1.002, 161); f = np.array([svn(np.array([*ks, 1j * o]))[32] for o in oms])
        mins = [golden(lambda o: svn(np.array([*ks, 1j * o]))[32], oms[i - 1], oms[i + 1]) for i in range(1, 160) if f[i] < f[i - 1] and f[i] < f[i + 1]]
        for w in mins:
            k = np.array([*ks, 1j * w]); _, s_, vh = np.linalg.svd(Dc.Q(k)); s_ = s_[::-1] / s_[0]
            nul = int((s_ < 1e-8).sum()); N = vh[-nul:].conj().T; G = Dc.gauge(k)
            X = N - G @ np.linalg.pinv(G, rcond=1e-9) @ N; X = np.linalg.svd(X)[0][:, :nul - 32]
            A = np.hstack([Dc.line_map(k), G]); PA = A @ np.linalg.pinv(A, rcond=1e-10)
            u, sh, vv = np.linalg.svd(PA @ X); Y = X @ vv.conj().T          # columns ordered: most metric first
            L = strain_metric(Dc, k); hr = np.linalg.norm(L @ Y, axis=0)
            print(f"{name:8s} |k|={km:.2f} alpha={(w*w/km**2-1)/km**2:+.4f} nullity {nul} metric overlaps {np.round(sh,3)} |L x| {np.round(hr,4)} ratio nm/m {hr[-1]/hr[0]:.2e}")
