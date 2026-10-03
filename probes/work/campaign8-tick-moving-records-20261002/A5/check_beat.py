#!/usr/bin/env python3
"""Lane T check D: visibility of a global beat in record formation.

(1) Two linked sites, independent geometric waits (chance p per tick, T >= 1):
      P(T1 = T2) = p/(2-p);  P(|T1-T2| = d) = 2p(1-p)^d/(2-p), d >= 1;  E[(-1)^T] = -p/(2-p).
    Exact series (fractions) + Monte Carlo (fixed seed).
(2) Seam toy: site A ticks at integer times, its linked neighbour B ticks twice as often (half-integer and integer
    times), both with chance p per own tick. Coincidence only at shared times:
      P = p^2 (1-p) / (1 - (1-p)^3)   (-> p/3 for small p, vs p/(2-p) -> p/2 in the bulk).
(3) Triggered formation (a site forms only when a recorded neighbour calls for it, each recorded neighbour
    independently with chance p per tick). Sites at lattice distance n can be recorded at tick n only through chains
    of immediate formations = oriented bond percolation. Survival of such chains to depth T from one seed
    (flat facet of the recorded region at exactly the cone speed) for p below/above threshold, 2D and 3D.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
from fractions import Fraction
import numpy as np

rng = np.random.default_rng(20261002)

print("== (1) coincidence of two independent geometric waits")
for p in (Fraction(1, 50), Fraction(1, 10), Fraction(1, 2), Fraction(9, 10)):
    q = 1 - p
    # exact partial sums to n=400 (tail bounded by q^(2*400))
    s = sum(p * p * q ** (2 * (n - 1)) for n in range(1, 401))
    closed = p / (2 - p)
    print("   p=%s  series(n<=400)=%.15f  p/(2-p)=%.15f  diff=%.1e  E[(-1)^T] closed=%+.6f" % (
        p, float(s), float(closed), float(closed - s), float(-p / (2 - p))))
for p in (0.02, 0.1, 0.5, 0.9):
    M = 2_000_000
    T1 = rng.geometric(p, M)
    T2 = rng.geometric(p, M)
    f = np.mean(T1 == T2)
    se = np.sqrt(f * (1 - f) / M)
    alt = np.mean((-1.0) ** T1)
    d1 = np.mean(np.abs(T1 - T2) == 1)
    print("   p=%.2f  MC P(T1=T2)=%.5f +- %.5f  exact %.5f (z=%+.2f) | MC E[(-1)^T]=%+.5f exact %+.5f | MC P(|D|=1)=%.5f exact %.5f" % (
        p, f, se, p / (2 - p), (f - p / (2 - p)) / se, alt, -p / (2 - p), d1, 2 * p * (1 - p) / (2 - p)))

print("\n== visibility of a frequency theta (per tick) after averaging over geometric formation ticks: |E e^{i theta T}|")
for p in (0.01, 0.1, 0.5):
    q = 1 - p
    vis = lambda th: p / np.sqrt(1 - 2 * q * np.cos(th) + q * q)
    lam = -np.log(q)
    visc = lambda th: lam / np.sqrt(lam * lam + th * th)
    print("   p=%.2f  theta=0.01: %.4f | pi/2: %.4f | pi: %.4f (=p/(2-p)=%.4f) | 2pi: %.4f   [continuous-time exp. waits: pi: %.4f, 2pi: %.4f]" % (
        p, vis(0.01), vis(np.pi / 2), vis(np.pi), p / (2 - p), vis(2 * np.pi), visc(np.pi), visc(2 * np.pi)))

print("\n== (2) seam toy: rate ratio 2")
for p in (Fraction(1, 50), Fraction(1, 5), Fraction(1, 2)):
    q = 1 - p
    s = sum(p * q ** (n - 1) * p * q ** (2 * n - 1) for n in range(1, 400))
    closed = p * p * q / (1 - q ** 3)
    print("   p=%s  series=%.12f  closed=%.12f  bulk p/(2-p)=%.6f  seam/bulk=%.4f" % (
        p, float(s), float(closed), float(p / (2 - p)), float(closed / (p / (2 - p)))))
p = 0.2
M = 2_000_000
TA = rng.geometric(p, M)
TB = rng.geometric(p, M)
f = np.mean(TB == 2 * TA)
print("   MC p=0.2: %.5f +- %.5f  closed %.5f" % (f, np.sqrt(f * (1 - f) / M), p * p * (1 - p) / (1 - (1 - p) ** 3)))

print("\n== (3) triggered formation: survival of immediate-formation chains (oriented bond percolation) to depth T")


def survive_2d(p, T, trials):
    # level n has positions j=0..n (x=j, y=n-j) in the first quadrant; site (n,j) fed by (n-1,j-1) via +x and (n-1,j) via +y
    alive = np.zeros((trials, T + 2), bool)
    alive[:, 0] = True
    for n in range(1, T + 1):
        bx = rng.random((trials, n + 1)) < p
        by = rng.random((trials, n + 1)) < p
        prev = alive[:, :n + 1].copy()
        fromx = np.zeros((trials, n + 1), bool)
        fromx[:, 1:] = prev[:, :n]
        fromy = prev.copy()
        fromy[:, n] = False
        new = (fromx & bx) | (fromy & by)
        alive[:, :n + 1] = new
        alive[:, n + 1:] = False
    return alive.any(axis=1).mean()


def survive_3d(p, T, trials):
    # level n: (i,j) with i+j<=n, site (x,y,z)=(i,j,n-i-j); fed by (i-1,j) [+x], (i,j-1) [+y], (i,j) [+z, needs n-1-i-j>=0]
    S = T + 2
    alive = np.zeros((trials, S, S), bool)
    alive[:, 0, 0] = True
    ii, jj = np.meshgrid(np.arange(S), np.arange(S), indexing='ij')
    for n in range(1, T + 1):
        prev = alive.copy()
        valid_prev = (ii + jj) <= n - 1
        prev &= valid_prev[None]
        fx = np.zeros_like(prev)
        fx[:, 1:, :] = prev[:, :-1, :]
        fy = np.zeros_like(prev)
        fy[:, :, 1:] = prev[:, :, :-1]
        fz = prev
        valid = (ii + jj) <= n
        new = ((fx & (rng.random(prev.shape) < p)) | (fy & (rng.random(prev.shape) < p)) | (fz & (rng.random(prev.shape) < p)))
        alive = new & valid[None]
    return alive.reshape(trials, -1).any(axis=1).mean()


for p in (0.55, 0.62, 0.68, 0.75, 0.85):
    print("   2D (threshold ~0.6447)  p=%.2f  surviving to depth 400: %.3f" % (p, survive_2d(p, 400, 300)))
for p in (0.30, 0.35, 0.42, 0.50):
    print("   3D (threshold ~0.3822)  p=%.2f  surviving to depth 80:  %.3f" % (p, survive_3d(p, 80, 60)))
