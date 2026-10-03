"""A14 check N2b: first-order (single-wall) forward T-matrix of the 2D conveyor walk.

One wall at the centre of an L x L torus (density 1/L^2).  For t < L/2,
  h(t) = <chi_k|U_1^t|chi_k> e^{i w0 t} = 1 + sigma(t)/L^2 + O(L^-4),
and for t past the near-field transient sigma(t) ~ sigma0 - i s_k t, so that at
density rho (independent walls, Foldy) the coherent wave has
  dw/rho = Re s_k  (quasi-energy shift per unit wall density)
  G/rho  = -2 Im s_k (extinction per unit wall density)
  ln Z / rho = Re sigma0 (immediate weight loss).
Usage: L T r m
"""
import sys, time, signal
import numpy as np
import w2d_walls as W

signal.alarm(58)
L = int(sys.argv[1]); T = int(sys.argv[2]); r = complex(sys.argv[3]); m = float(sys.argv[4])
t0 = time.time()
Wm = np.zeros((L, L)); Wm[L // 2, L // 2] = 1.0
F = 1.0 - Wm
xs = np.arange(L)
nlist = [4, 6, 8, 12, 16, 24, 32]          # k = 2 pi n / L along x
kd = [4, 8, 16]                             # diagonal (n, n)
klist = [(n, 0) for n in nlist] + [(n, n) for n in kd]
print(f"L={L} T={T} r={r} m={m}")
print("  (nx,ny)   |k|      w0     Re s=dw/rho  -2Im s=G/rho  Re sig0   [slope from t in (T/2,T)]  drift")
for batch in (klist[:5], klist[5:]):
    nk = len(batch)
    psi = np.zeros((nk, 2, L, L), complex); om0 = np.zeros(nk)
    for j, (nx, ny) in enumerate(batch):
        kx, ky = 2*np.pi*nx/L, 2*np.pi*ny/L
        om0[j], v = W.upper(kx, ky, m)
        ph = np.exp(1j * (kx * xs[:, None] + ky * xs[None, :]))
        psi[j, 0] = v[0] * ph * F; psi[j, 1] = v[1] * ph * F
        psi[j] /= np.sqrt(np.sum(np.abs(psi[j])**2))
    chi = psi.copy()
    sig = np.zeros((nk, T + 1), complex)
    for t in range(1, T + 1):
        psi = W.step(W.mass(psi, m), F, Wm, r)
        g = np.sum(np.conj(chi) * psi, axis=(1, 2, 3))
        sig[:, t] = (g * np.exp(1j * om0 * t) - 1.0) * L * L
    tt = np.arange(T + 1)
    for j, (nx, ny) in enumerate(batch):
        sel = tt >= T // 2
        a = np.polyfit(tt[sel], sig[j, sel], 1)       # complex slope
        s = 1j * a[0]
        # drift check: slope over first vs second half of the window
        h1 = (tt >= T//2) & (tt < 3*T//4); h2 = tt >= 3*T//4
        s1 = 1j*np.polyfit(tt[h1], sig[j, h1], 1)[0]; s2 = 1j*np.polyfit(tt[h2], sig[j, h2], 1)[0]
        kk = 2*np.pi*np.hypot(nx, ny)/L
        print(f"  ({nx:2d},{ny:2d})  {kk:.4f}  {om0[j]:.4f}   {s.real:+9.3f}     {-2*s.imag:8.3f}    {a[1].real:+8.2f}       re {s1.real:+.3f}/{s2.real:+.3f}")
print(f"elapsed {time.time()-t0:.1f}s")
