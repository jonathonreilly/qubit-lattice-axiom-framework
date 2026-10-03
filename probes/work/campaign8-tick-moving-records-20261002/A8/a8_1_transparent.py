"""A8 check 1: transparent (volume) absorbers on exact Z^3 -- additivity, lapse weighting, crossover.

Model (lane G 3.8a, supplied toy): carriers may visit every record; record i captures with odds q per visit
(relative to hop odds), so capture at i is sigma_i = q * N_i with N_i = u_i/u_inf = 1 + Phi_i and Phi = -G sigma.
  => sigma = (G_BB + I/q)^{-1} 1,  Q = sum sigma.
Checks:
 A. identity Q = q * sum_i N_i (lapse-weighted count) and the exact bounds
       q N / (1 + q gbar) <= Q <= min(q N, Cap(B)),   gbar = 1'G1/N,  Cap(B) = 1'G^{-1}1.
 B. one-parameter collapse: Q/(qN) against t = qN/Cap(B) compared with the continuum uniform ball
       F(t) = (1/t) (1 - tanh(sqrt(3t))/sqrt(3t))      (exact for a uniform continuum ball)
    and the crossover q_c (qN = Cap) against the continuum R_c = sqrt(3/(q n)).
 C. dilute sublattice balls (filling 1/d^3): defect 1 - Q/(qN) against t.
"""
import os
for k in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[k] = "1"
import time
import numpy as np
from scipy.optimize import brentq
from a8_lib import G, Gmat, cube, ball, sub_ball

t0 = time.time()


def F(t):
    x = np.sqrt(3 * t)
    return (1 - np.tanh(x) / x) / t


def lump_data(B):
    M = Gmat(B)
    n = len(B)
    one = np.ones(n)
    cap = one @ np.linalg.solve(M, one)
    gbar = one @ M @ one / n
    return M, cap, gbar


def Qof(M, q):
    n = M.shape[0]
    sig = np.linalg.solve(M + np.eye(n) / q, np.ones(n))
    return sig


print("== A. identity Q = q*sum(N_i) and bounds (jammed cube s=5, N=125) ==")
B = cube(5)
M, cap, gbar = lump_data(B)
N = len(B)
worst_id = 0.0
for q in [1e-3, 1e-2, 0.1, 1.0, 10.0]:
    sig = Qof(M, q)
    Q = sig.sum()
    Ni = 1 - M @ sig
    ident = abs(Q - q * Ni.sum()) / Q
    worst_id = max(worst_id, ident)
    lo, hi = q * N / (1 + q * gbar), min(q * N, cap)
    print(f"  q={q:7.3g}: Q={Q:10.5f}  q*sum N_i={q*Ni.sum():10.5f}  rel.diff={ident:.1e}  "
          f"bounds [{lo:9.4f}, {hi:9.4f}] ok={lo <= Q * (1 + 1e-12) and Q <= hi * (1 + 1e-12)}  "
          f"N_i range [{Ni.min():.3f},{Ni.max():.3f}]")
print(f"  Cap={cap:.4f}  gbar={gbar:.4f}  N/Cap={N/cap:.4f} (Cauchy-Schwarz: gbar >= N/Cap)")

print("\n== B. jammed lumps: Q/(qN) vs t = qN/Cap against continuum ball F(t); crossover q_c ==")
print(" lump        N    Cap      Reff   q_c(qN=Cap)  3/Reff^2   N_i(mean) at q_c  | Q/(qN) - F(t) at t=0.1,0.3,1,3,10")
lumps = [("cube2", cube(2)), ("cube3", cube(3)), ("cube4", cube(4)), ("cube6", cube(6)), ("cube8", cube(8)),
         ("ball2", ball(2.0)), ("ball3", ball(3.0)), ("ball4", ball(4.0)), ("ball5", ball(5.0))]
maxdev = {}
for name, B in lumps:
    M, cap, gbar = lump_data(B)
    N = len(B)
    reff = (3 * N / (4 * np.pi)) ** (1 / 3)
    qc = cap / N
    sig = Qof(M, qc)
    Nmean = (1 - M @ sig).mean()
    devs = []
    for t in [0.1, 0.3, 1.0, 3.0, 10.0]:
        q = t * cap / N
        Q = Qof(M, q).sum()
        devs.append(Q / (q * N) - F(t))
    maxdev[name] = max(abs(d) for d in devs)
    print(f" {name:7s} {N:5d} {cap:8.3f} {reff:7.3f}   {qc:9.4f}   {3/reff**2:9.4f}   {Nmean:8.3f}         | "
          + " ".join(f"{d:+.3f}" for d in devs))
print(" F(t) values:", " ".join(f"{F(t):.4f}" for t in [0.1, 0.3, 1.0, 3.0, 10.0]))
print(f" continuum: at crossover t=1, Q/(qN)=F(1)={F(1.0):.4f}; surface lapse tanh(x)/x at x=sqrt3: {np.tanh(np.sqrt(3))/np.sqrt(3):.4f}")

print("\n== C. dilute sublattice balls (each record isolated): defect 1-Q/(qN) vs t=qN/Cap ==")
print(" d   R    N    Cap     gbar    | q=0.01: t   defect  F-defect | q=0.1: t   defect  F-defect | q=1: t   defect  F-defect")
for d, R in [(2, 6.0), (3, 9.0), (3, 12.0), (4, 12.0)]:
    B = sub_ball(R, d)
    M, cap, gbar = lump_data(B)
    N = len(B)
    out = f" {d}  {R:4.1f} {N:4d} {cap:7.3f} {gbar:7.3f}   |"
    for q in [0.01, 0.1, 1.0]:
        Q = Qof(M, q).sum()
        t = q * N / cap
        out += f" {t:7.3f} {1-Q/(q*N):7.4f} {1-F(t):7.4f} |"
    print(out)
print(f"\nelapsed {time.time()-t0:.1f} s; distinct G values {len(__import__('a8_lib')._cache)}")
