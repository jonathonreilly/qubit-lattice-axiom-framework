import sys, time
import numpy as np
from tor1_lib import *
Lx, Lt, P = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
S = Torus(Lx, Lt); rng = np.random.default_rng(1)
th = rng.normal(0, 0.1, (P, S.nl)) + rng.uniform(0, 6, (P, 1)) * S.Ut[None]
t0 = time.time(); M = TorusMeasure(S, '11112', Ns=4, ntor=192, nloop=256, ngam=64); print('init', time.time() - t0)
F, Q, AT, w = S.decompose(th)
t0 = time.time(); V0, _ = M.toron_basis(w); print('toron basis per node ms', (time.time() - t0) / P * 1e3)
t0 = time.time(); g = M.Gam_t(w[:, 0]); print('Gam_t per node ms', (time.time() - t0) / P * 1e3)
t0 = time.time(); r = M.ray(AT, w, V0, 4, need_k=False); print('transport Ns=4 per node ms', (time.time() - t0) / P * 1e3)
t0 = time.time(); r = M.ray(AT, w, V0, 4, need_k=True); print('transport+kbb Ns=4 per node ms', (time.time() - t0) / P * 1e3)
t0 = time.time(); l1, _ = vec_logdet(S, th, 0.0, 1); l2, _ = vec_logdet(S, th, 0.0, 2); print('modulus per node ms', (time.time() - t0) / P * 1e3)
t0 = time.time(); lw = wilson_logdet(S, th, 0.05); print('wilson per node ms', (time.time() - t0) / P * 1e3)
