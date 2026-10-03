"""A17 check C3b: exact variance of the linear phase predictor (no wave evolution).
ph_pred = -(m/(p(2R+1))) sum_y n(y) [kB - kA](y), n(y) = sum_t e_t(y) ~ Binomial(T, p) iid per site."""
import os
for k in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[k] = "1"
import numpy as np
exec(open('dirac_pacing.py').read().split('rng = np.random.default_rng')[0])   # reuse packet(), L, kk
m, p, T, R = 0.15, 0.05, 200, 200
box = np.zeros(L); box[:R + 1] = 1; box[L - R:] = 1
rng = np.random.default_rng(99)
for D in (600, 100):
    pa = packet(m, 1000, 30.0); pb = packet(m, 1000 + D, 30.0)
    s1 = 2 * np.real(np.conj(pa[0]) * pa[1]); s2 = 2 * np.real(np.conj(pb[0]) * pb[1])
    kA = np.real(np.fft.ifft(np.fft.fft(s1) * np.fft.fft(box))); kB = np.real(np.fft.ifft(np.fft.fft(s2) * np.fft.fft(box)))
    dk = kB - kA
    var_pk = m * m * T * p * (1 - p) / (p * (2 * R + 1)) ** 2 * np.sum(dk ** 2)
    vals = []
    for b in range(10):
        n = rng.binomial(T, p, size=(2000, L)).astype(float)
        vals.append(-(m / (p * (2 * R + 1))) * (n @ dk))
    v = np.concatenate(vals)
    # bootstrap-free s.e. of the variance for 20000 samples
    print(f"D={D}: sample Var(ph_pred) over {v.size} = {v.var():.4f} (s.e. {v.var()*np.sqrt(2/v.size):.4f}); exact {var_pk:.4f}")
