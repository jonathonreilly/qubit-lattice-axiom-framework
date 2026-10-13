"""R19-10 checks on r1910_adiabatic.py: (1) ring-size dependence at fixed T; (2) time-step dependence;
(3) the per-event energy-flow identity d<H_B>/dt = i<[K(t), H_B]> used in Lemma S-ins, checked as
    eps_fix(t) >= eps_fix(0) - Gamma_hat t with Gamma_hat = max_t |d eps_fix/dt| (numerical)."""
import numpy as np, time
src = open('r1910_adiabatic.py').read().split('# static delta(g)')[0]
exec(src)
T0 = time.time()
for (T, N, dt) in [(16, 80, 0.05), (16, 160, 0.05), (16, 80, 0.025), (32, 112, 0.05), (32, 224, 0.05)]:
    tot = np.zeros(4)
    for s, w in zip(S_nodes, S_w):
        tot += w*np.array(run(N, 0.0, s, T, dt=dt))
    pr('m=0 T=%d N=%d dt=%.3f: eps_inf = %.4e ; A_fix = %.4e ; A_law = %.4e [%.0fs]' % (T, N, dt, tot[0], tot[1], tot[2], time.time()-T0))
