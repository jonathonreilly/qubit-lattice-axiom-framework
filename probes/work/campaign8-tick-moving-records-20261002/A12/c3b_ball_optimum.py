"""C3b: best single-tick, single-mode formation weight of reach R in the 3D half-filled staggered sea.
eps_opt(R) = lambda_min of P_- restricted to the Euclidean ball of radius R (= least vacuum occupation of
any mode supported in the ball). Compared with A9's truncated upper-band mode P_+ e_0 cut to the ball
(eps_A9(R) ~ R^-3) and with the infrared weight of the single-site spectral measure below |E| = 1/R.
Massless staggered fermions on an antiperiodic L^3 torus (A9's construction, P_+ = (1 + H|H|^-1)/2 by FFT)."""
import os, sys
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np

L = int(sys.argv[1]) if len(sys.argv) > 1 else 32
Rmax = int(sys.argv[2]) if len(sys.argv) > 2 else 6
x = np.arange(L)
X1, X2, X3 = np.meshgrid(x, x, x, indexing="ij")
eta = [np.ones((L, L, L)), (-1.0) ** X1, (-1.0) ** (X1 + X2)]
k = np.pi * (2 * x + 1) / L
s2 = np.sin(k) ** 2
Einv = 1.0 / np.sqrt(s2[:, None, None] + s2[None, :, None] + s2[None, None, :])
tw = np.exp(-1j * np.pi * x / L)
TW = tw[:, None, None] * tw[None, :, None] * tw[None, None, :]


def absH_inv(v):
    return np.fft.ifftn(Einv * np.fft.fftn(v * TW)) / TW


def shift(v, mu, d):
    out = np.roll(v, -d, axis=mu)
    idx = [slice(None)] * 3
    idx[mu] = slice(L - 1, L) if d == 1 else slice(0, 1)
    out[tuple(idx)] *= -1
    return out


def H(v):
    out = np.zeros_like(v)
    for mu in range(3):
        out += 0.5j * eta[mu] * (shift(v, mu, -1) - shift(v, mu, 1))
    return out


def Pminus(v):
    return 0.5 * (v - H(absH_inv(v)))


c = L // 2
dist = np.sqrt((X1 - c) ** 2 + (X2 - c) ** 2 + (X3 - c) ** 2)
ball_all = np.argwhere(dist <= Rmax + 1e-9)
order = np.argsort(dist[tuple(ball_all.T)], kind="stable")
ball_all = ball_all[order]
dsorted = dist[tuple(ball_all.T)]
cols = np.empty((len(ball_all), len(ball_all)), complex)
for j, (a, b, cc) in enumerate(ball_all):
    e = np.zeros((L, L, L), complex); e[a, b, cc] = 1
    cols[:, j] = Pminus(e)[tuple(ball_all.T)]
herm = np.abs(cols - cols.conj().T).max()
e0 = np.zeros((L, L, L), complex); e0[c, c, c] = 1
wfull = e0 - Pminus(e0)                                 # P_+ e_0
print(f"L={L}: ball up to R={Rmax} has {len(ball_all)} sites; hermiticity err {herm:.1e}")
print(f"{'R':>3} {'sites':>6} {'eps_opt (lambda_min)':>21} {'#eig<1e-6':>9} {'eps_A9 (cut P+e0)':>18}")
prev = None
for R in range(1, Rmax + 1):
    n = int((dsorted <= R + 1e-9).sum())
    sub = cols[:n, :n]
    lam = np.linalg.eigvalsh(0.5 * (sub + sub.conj().T))
    wR = np.where(dist <= R + 1e-9, wfull, 0); wR /= np.linalg.norm(wR)
    epsA9 = np.vdot(wR, Pminus(wR)).real
    rate = "" if prev is None else f"   d ln eps_opt/dR = {np.log(max(lam[0],1e-300)/prev):+.2f}"
    print(f"{R:3d} {n:6d} {lam[0]:21.3e} {(lam < 1e-6).sum():9d} {epsA9:18.3e}{rate}")
    prev = max(lam[0], 1e-300)
