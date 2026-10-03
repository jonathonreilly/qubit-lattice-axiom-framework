"""A30 q1_2d_packet: wave packet on a recorded disk, Option R per-tick capture (supplied toy).

Periodic 128x128 lattice, recorded disk radius 8 at the centre (removed sites = walls).
Packet: uniform in y (k_y = 0), Gaussian in x (s_x = 12), momentum k0 toward the disk.
Two dynamics:
  rate  : exp(-i H_eff T), H_eff = H - i Gam/2 sum_capture |j><j|
  tick  : each tick psi <- K exp(-i H tau) psi, K = 1 - kap on capture sites,
          kap = 1 - exp(-Gam tau / 2) (rate-matched per-tick chance f = 1 - exp(-Gam tau))
Captured probability P = 1 - |psi(T)|^2 is compared with the stationary prediction
  P_pred = (1/N_y) sum_m w(m) sigma_abs(k_m)   (same lattice, absorbing-frame solver).
Times are short enough that nothing scattered reaches a periodic image of the disk.
Usage: python3 q1_2d_packet.py M0 GAM   (k0 = 2 pi M0 / 128)
"""
import signal
import sys
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import splu, expm_multiply

signal.alarm(55)
t = 1.0
N = 128
m0 = int(sys.argv[1]) if len(sys.argv) > 1 else 32
Gam = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0
a = 8
X, Y = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')
dist = np.sqrt((X - N // 2) ** 2 + (Y - N // 2) ** 2)
rec = dist <= a
free = ~rec
nfree = int(free.sum())
lab = -np.ones((N, N), dtype=np.int64)
lab[free] = np.arange(nfree)
rows, cols = [], []
nrec = np.zeros((N, N), dtype=np.int64)
for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    Xn = (X + dx) % N; Yn = (Y + dy) % N
    m = free & free[Xn, Yn]
    rows.append(lab[m]); cols.append(lab[Xn[m], Yn[m]])
    nrec += free & rec[Xn, Yn]
rows = np.concatenate(rows); cols = np.concatenate(cols)
H = sp.csr_matrix((-t * np.ones(len(rows)), (rows, cols)), shape=(nfree, nfree))
cap = (free & (nrec > 0))[free]
k0 = 2 * np.pi * m0 / N
v = 2 * t * np.sin(k0)
sx = 12.0
x0 = N // 2 - a - 3 * sx - 4
dxp = (np.arange(N) - x0 + N / 2) % N - N / 2          # periodic (minimal-image) distance
g = np.exp(-(dxp ** 2) / (4 * sx * sx)) * np.exp(1j * k0 * np.arange(N))
g /= np.linalg.norm(g)
psi2d = np.outer(g, np.ones(N)) / np.sqrt(N)
psi = psi2d[free]
lost_on_disk = 1 - np.linalg.norm(psi) ** 2          # packet tail initially on recorded sites
psi = psi / np.linalg.norm(psi)
T = (N // 2 - x0 + a + 3 * sx) / v
w = np.abs(np.fft.fft(g)) ** 2
w /= w.sum()

# --- rate dynamics
Heff = (H + sp.diags(np.where(cap, -0.5j * Gam, 0.0))).tocsr()
out = expm_multiply(-1j * Heff * T, psi)
P_rate = 1 - np.linalg.norm(out) ** 2

# --- per-tick dynamics
tau = 0.05
nt = int(round(T / tau))
kap = 1 - np.exp(-Gam * tau / 2)
ps = psi.copy()
Kdiag = np.where(cap, 1 - kap, 1.0)
for _ in range(nt):
    ps = expm_multiply(-1j * H * tau, ps)
    ps *= Kdiag
P_tick = 1 - np.linalg.norm(ps) ** 2

# --- stationary prediction (absorbing frame W=36, Wmax=1.5, as validated in q1_2d flat)
Wf, Wmax = 36, 1.5
dxe = np.minimum(X, N - 1 - X); dye = np.minimum(Y, N - 1 - Y); de = np.minimum(dxe, dye)
frame = np.where(de < Wf, Wmax * ((Wf - de) / Wf) ** 2, 0.0)


def sigma_abs(k):
    E = -2 * t * (np.cos(k) + 1.0)
    phi = np.exp(1j * k * X)
    src = np.zeros((N, N), dtype=complex)
    for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        Xn = (X + dx) % N; Yn = (Y + dy) % N
        mr = free & rec[Xn, Yn]
        src[mr] += t * phi[Xn[mr], Yn[mr]]
    gam = np.where(free & (nrec > 0), Gam, 0.0)
    V = -0.5j * gam
    src = src + V * phi
    A = sp.diags(E - V[free] + 0.5j * frame[free]) - H
    s = splu(A.tocsc()).solve(src[free])
    psi_t = phi[free] + s
    return np.sum(gam[free] * np.abs(psi_t) ** 2) / (2 * t * np.sin(k))


P_pred = 0.0
used = 0.0
for m in range(m0 - 4, m0 + 5):
    P_pred += w[m % N] * sigma_abs(2 * np.pi * m / N) / N
    used += w[m % N]
print(f"k0={k0:.4f} (m0={m0}) Gam={Gam} disk a={a}: T={T:.1f}, ticks={nt} (tau={tau}), "
      f"packet weight on the 9 grid momenta used = {used:.6f}, initial tail on disk {lost_on_disk:.1e}")
print(f"  captured: rate dynamics {P_rate:.6f} | per-tick Option R {P_tick:.6f} | stationary prediction {P_pred:.6f}")
print(f"  rate/pred = {P_rate/P_pred:.4f}, tick/pred = {P_tick/P_pred:.4f};  sigma_abs(k0) = {sigma_abs(k0):.3f} vs 2a = {2*a}")
