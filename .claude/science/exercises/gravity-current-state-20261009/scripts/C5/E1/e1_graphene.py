#!/usr/bin/env python3
"""E1 (C): honeycomb tight-binding under uniform strain (bond hoppings t1, t2, t3), and the
mean-field Hubbard (antiferromagnetic) mass.  Bond vectors (length 1):
  d1 = (0, 1), d2 = (-sqrt3/2, -1/2), d3 = (sqrt3/2, -1/2);  f(k) = sum_j t_j exp(i k.d_j);  E = +-|f|.
(i)  gap = 2 min_k |f|: zero iff the triangle inequality holds (proved: f(K) = 0 <=> t1 + t2 w2 + t3 w3 = 0
     for unit complex w2, w3, i.e. a closed triangle); merging at t1 = t2 + t3.
(ii) Dirac-cone velocity tensor M (|f(K+p)|^2 = p^T M p): eigen-velocities vs strain.
(iii) mean-field AF threshold: 1/U_c = (1/Ncell) sum_k 1/(2|f(k)|)  (comparator: isotropic MF U_c ~ 2.23 t, RECALLED)
Memory: k-grids in rows of N (N <= 2400).
"""
import numpy as np
from scipy.optimize import minimize

d = np.array([[0.0, 1.0], [-np.sqrt(3) / 2, -0.5], [np.sqrt(3) / 2, -0.5]])
a1 = d[0] - d[1]; a2 = d[0] - d[2]                       # Bravais vectors
A = np.array([a1, a2]); B = 2 * np.pi * np.linalg.inv(A).T  # rows: b1, b2

def f(k, t):
    return (t[None, :] * np.exp(1j * (k @ d.T))).sum(axis=1)

def dirac_point(t):
    # solve t1 + t2 e^{i a} + t3 e^{i b} = 0 (triangle) -> phases; then k from k.(d2-d1)=a, k.(d3-d1)=b
    t1, t2, t3 = t
    if not (abs(t2 - t3) <= t1 <= t2 + t3 and abs(t1 - t3) <= t2 <= t1 + t3 and abs(t1 - t2) <= t3 <= t1 + t2):
        return None
    ca = (t3**2 - t1**2 - t2**2) / (2 * t1 * t2)
    al = np.arccos(np.clip(ca, -1, 1))
    z = -(t1 + t2 * np.exp(1j * al)) / t3
    be = np.angle(z)
    M = np.array([d[1] - d[0], d[2] - d[0]])
    return np.linalg.solve(M, np.array([al, be]))

def min_absf(t, ngrid=400):
    u = (np.arange(ngrid) + 0.5) / ngrid
    U1, U2 = np.meshgrid(u, u, indexing='ij')
    K = U1.ravel()[:, None] * B[0] + U2.ravel()[:, None] * B[1]
    af = np.abs(f(K, t)); i = np.argmin(af)
    res = minimize(lambda k: np.abs(f(k[None, :], t))[0] ** 2, K[i], method='Nelder-Mead',
                   options={'xatol': 1e-14, 'fatol': 1e-30, 'maxiter': 20000})
    return np.sqrt(res.fun), res.x

def vel_tensor(t, k0):
    w = (t[:, None] * np.exp(1j * (d @ k0))[:, None] * 1j * d).sum(axis=0)   # df/dk at k0
    M = np.real(np.outer(w, np.conj(w)))
    return np.sqrt(np.linalg.eigvalsh(M))

def inv_Uc(t, N):
    s = 0.0
    u = (np.arange(N) + 0.5) / N
    for i in range(N):
        K = u[i] * B[0][None, :] + u[:, None] * B[1][None, :]
        s += (0.5 / np.abs(f(K, t))).sum()
    return s / N**2

from scipy.special import ellipk, ellipkm1
from scipy.integrate import quad

def inv_Uc_ell(t):
    """1/U_c = (1/2) <1/|f|>.  |f|^2 = P(th1) + R(th1) cos(th2 + psi), th_i = k.a_i:
    inner average = (2/pi) K(m)/sqrt(P+R), m = 2R/(P+R); outer th1 by quad with breakpoints at the
    Dirac th1 values (log singularities)."""
    t1, t2, t3 = t
    def inner(th1):
        # |f|^2 = |w + t3 e^{-i th2}|^2, w = t1 + t2 e^{-i th1}: P+R = (|w|+t3)^2, P-R = (|w|-t3)^2
        w = abs(t1 + t2 * np.exp(-1j * th1))
        p = ((w - t3) / (w + t3)) ** 2          # 1 - m, computed without cancellation
        return (2 / np.pi) * ellipkm1(max(p, 1e-300)) / (w + t3)
    kd = dirac_point(t)
    pts = sorted({(kd @ a1) % (2 * np.pi), (-kd @ a1) % (2 * np.pi)}) if kd is not None else []
    edges = [0.0] + [p for p in pts if 1e-12 < p < 2 * np.pi - 1e-12] + [2 * np.pi]
    tot = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        tot += quad(inner, lo, hi, limit=1000, epsabs=1e-13, epsrel=1e-12)[0]
    return 0.5 * tot / (2 * np.pi), inner

if __name__ == "__main__":
    print("(i) gap and Dirac point under uniaxial bond strain t = (1+2u, 1-u, 1-u) (traceless), merging at u = 1/4")
    for u in (0.0, 0.05, 0.1, 0.2, 0.24, 0.249, 0.26, 0.3, -0.2, -0.4):
        t = np.array([1 + 2 * u, 1 - u, 1 - u])
        g, kmin = min_absf(t)
        kd = dirac_point(t)
        fkd = np.abs(f(kd[None, :], t))[0] if kd is not None else np.nan
        exact = 2 * max(0.0, t[0] - t[1] - t[2]) if t[0] > t[1] + t[2] else 0.0
        print(f"  u={u:+.3f}: 2 min|f| (numeric) = {2*g:.3e};  exact gap = {exact:.3e};  |f(K_D)| = {fkd:.2e}")
    rng = np.random.default_rng(1)
    worst = 0.0; n_in = 0
    for _ in range(200):
        s = rng.normal(size=3); s -= s.mean(); s *= rng.uniform(0, 0.3) / np.abs(s).max()
        t = 1 + s
        kd = dirac_point(t)
        if kd is not None:
            n_in += 1; worst = max(worst, np.abs(f(kd[None, :], t))[0])
    print(f"  200 random traceless strains |s|<=0.3: {n_in} satisfy the triangle rule; max |f(K_D)| = {worst:.2e}")
    print("\n(ii) cone velocities (eigen-velocities of M) vs u; isotropic value 3/2")
    for u in (0.0, 0.01, 0.02, 0.05, 0.1, 0.2, 0.24):
        t = np.array([1 + 2 * u, 1 - u, 1 - u])
        kd = dirac_point(t)
        v = vel_tensor(t, kd)
        print(f"  u={u:.3f}: v = {v[0]:.6f}, {v[1]:.6f};  ln(v_max/v_min)/u = {np.log(v[1]/v[0])/u if u>0 else float('nan'):.5f};  det-velocity v1*v2 = {v[0]*v[1]:.6f};  K_D = ({kd[0]:+.5f},{kd[1]:+.5f})")
    print("\n(iii) mean-field AF threshold U_c(u): elliptic-K inner integral + adaptive outer (midpoint grid N=1200 shown for reference)")
    # check of the inner closed form against brute force at a regular th1
    _, inner = inv_Uc_ell(np.array([1.1, 0.95, 0.95]))
    th2 = (np.arange(200000) + 0.5) * 2 * np.pi / 200000
    tt = np.array([1.1, 0.95, 0.95]); th1 = 1.3
    P = (tt**2).sum() + 2 * tt[0] * tt[1] * np.cos(th1)
    brute = np.mean(1 / np.abs(tt[0] + tt[1] * np.exp(-1j * th1) + tt[2] * np.exp(-1j * th2)))
    print(f"  inner-integral check at th1=1.3: closed form {inner(th1):.12f}  brute {brute:.12f}")
    for u in (0.0, 0.05, 0.1, 0.15, 0.2, 0.24, 0.249, -0.2, -0.4):
        t = np.array([1 + 2 * u, 1 - u, 1 - u])
        r, _ = inv_Uc_ell(t)
        print(f"  u={u:+.3f}: 1/U_c = {r:.8f}  ->  U_c = {1/r:.5f} t   (grid N=1200: {inv_Uc(t, 1200):.5f})")
