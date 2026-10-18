"""NT-2 T22: pools and hill-climb searches for a negative RP eigenvalue of the pure-gauge hard-plaquette crossing kernel.
Members are gauge-invariant coordinates m = (p00, p10, p01, X0, Y0). Kernel exact (closed form, V0-validated).
Usage: python t22_search.py MODE SEED [K STEPS DELTA]
 MODE: rand (P1, admissible, random holonomies) | w0 (P2, X0=Y0=0) | unres (R1 power ref: plaquettes up to pi-0.05)
"""
import sys, time, resource, numpy as np
from t22lib import *

mode = sys.argv[1]; seed = int(sys.argv[2])
K = int(sys.argv[3]) if len(sys.argv) > 3 else 24
STEPS = int(sys.argv[4]) if len(sys.argv) > 4 else 400
delta = float(sys.argv[5]) if len(sys.argv) > 5 else 0.6
rng = np.random.default_rng(seed)
m = (np.pi - 0.05) if mode == 'unres' else (delta - 0.05)

def inv_from(M):
    p00, p10, p01, X0, Y0 = M.T
    return dict(p00=wrap(p00), p10=wrap(p10), p01=wrap(p01), p11=wrap(-(p00 + p10 + p01)),
                X0=wrap(X0), Y0=wrap(Y0), X1=wrap(X0 - p00 - p10), Y1=wrap(Y0 + p00 + p01))

def kmat(M):
    I = inv_from(M)
    return kernel_closed_inv({k: v[:, None] for k, v in I.items()}, {k: v[None, :] for k, v in I.items()}, delta)

def admissible(M):
    I = inv_from(M)
    return max(np.abs(I[k]).max() for k in ('p00', 'p10', 'p01', 'p11')) <= m + 1e-12

def new_member(n):
    if mode == 'unres':
        P = rng.uniform(-m, m, (n, 3)); P = P[np.abs(wrap(-(P.sum(1)))) <= m]
        while len(P) < n:
            Q = rng.uniform(-m, m, (n, 3)); P = np.vstack([P, Q[np.abs(wrap(-Q.sum(1))) <= m]])
        P = P[:n]
    else:
        P = sample_plaq(n, m, rng)
    if mode == 'w0':
        H = np.zeros((n, 2))
    else:
        H = rng.uniform(-np.pi, np.pi, (n, 2))
    return np.hstack([P, H])

def perturb(x, s):
    for _ in range(2000):
        y = x.copy(); y[:3] += rng.normal(0, s, 3)
        if mode != 'w0':
            y[3:] = wrap(y[3:] + rng.normal(0, s, 2))
        if admissible(y[None, :]):
            return y
    return x.copy()

def obj(M):
    Km = kmat(M)
    d = np.sqrt(np.diag(Km)); Kn = Km / d[:, None] / d[None, :]
    return np.linalg.eigvalsh(Kn)[0]

t0 = time.time()
M = new_member(K)
start = obj(M); cur = start
for step in range(STEPS):
    i = rng.integers(K)
    cands = list(new_member(4)) + [perturb(M[i], s) for s in (0.02, 0.05, 0.1, 0.2)]
    best = None
    for c in cands:
        T = M.copy(); T[i] = c; v = obj(T)
        if best is None or v < best[0]:
            best = (v, T)
    if best[0] < cur:
        cur, M = best
    if step % 100 == 99:
        print(f"step {step+1}: obj {cur:+.4e}", flush=True)
Km = kmat(M); ev = np.linalg.eigvalsh(Km)
# independent builder on explicit links with random gauge
Lk = build_links(M[:, 0], M[:, 1], M[:, 2], M[:, 3], M[:, 4], rng=rng)
Ki = kernel_matrix_indep(Lk, delta); evi = np.linalg.eigvalsh(Ki)
E = K * np.abs(Km - Ki).max() + K * 1e-15 * np.abs(Km).max()
I = inv_from(M)
print(f"RESULT mode={mode} seed={seed} K={K} steps={STEPS} delta={delta}: start obj {start:+.4e} end obj {cur:+.4e} | "
      f"lam_min {ev[0]:+.4e} lam_max {ev[-1]:.4e} min/max {ev[0]/ev[-1]:+.3e} | indep lam_min {evi[0]:+.4e} | E {E:.1e} | "
      f"neg-converged {ev[0] < -10*E and ev[0]/ev[-1] < -1e-9} | max|plaq| {max(np.abs(I[k]).max() for k in ('p00','p10','p01','p11')):.4f} | "
      f"{time.time()-t0:.1f}s RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20:.0f}MB")
np.save(f"pool_T22_{mode}_{seed}_d{delta}.npy", M)
