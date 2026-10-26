#!/usr/bin/env python3
"""T36 P4: (a) how much can one-loop SM running change Yukawa singular-value ratios between M_Pl and m_t?
(b) price of the registered-data reading under an O(1) anarchic ensemble (reading, not a derivation).
Pre-registration: PREREGISTRATION.md."""
import numpy as np
rng = np.random.default_rng(29092026)
pi16 = 16*np.pi**2
def rhs(t, y, n):
    Yu = y[:9*n].reshape(n,3,3) if False else None
def unpack(y):
    Yu = (y[0:9]+1j*y[9:18]).reshape(3,3); Yd=(y[18:27]+1j*y[27:36]).reshape(3,3); Ye=(y[36:45]+1j*y[45:54]).reshape(3,3)
    g = y[54:57]
    return Yu, Yd, Ye, g
def pack(Yu,Yd,Ye,g):
    return np.concatenate([Yu.real.ravel(),Yu.imag.ravel(),Yd.real.ravel(),Yd.imag.ravel(),Ye.real.ravel(),Ye.imag.ravel(),g])
b = np.array([41/10, -19/6, -7.0])
def f(y):
    Yu,Yd,Ye,g = unpack(y)
    H = lambda A: A.conj().T
    T = np.trace(3*Yu@H(Yu) + 3*Yd@H(Yd) + Ye@H(Ye)).real
    Gu = 17/20*g[0]**2 + 9/4*g[1]**2 + 8*g[2]**2
    Gd = 1/4*g[0]**2 + 9/4*g[1]**2 + 8*g[2]**2
    Ge = 9/4*g[0]**2 + 9/4*g[1]**2
    dYu = (1.5*Yu@H(Yu)@Yu - 1.5*Yd@H(Yd)@Yu + T*Yu - Gu*Yu)/pi16
    dYd = (1.5*Yd@H(Yd)@Yd - 1.5*Yu@H(Yu)@Yd + T*Yd - Gd*Yd)/pi16
    dYe = (1.5*Ye@H(Ye)@Ye + T*Ye - Ge*Ye)/pi16
    dg = b*g**3/pi16
    return pack(dYu,dYd,dYe,dg)
def rk4(y, t0, t1, n=400):
    h = (t1-t0)/n
    for _ in range(n):
        k1=f(y); k2=f(y+h/2*k1); k3=f(y+h/2*k2); k4=f(y+h*k3); y = y + h/6*(k1+2*k2+2*k3+k4)
        if not np.all(np.isfinite(y)) or np.abs(y).max()>50: return None
    return y
sv = lambda A: np.sort(np.linalg.svd(A, compute_uv=False))[::-1]
def randY(scale):
    return scale*(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))/np.sqrt(2)
t_UV, t_IR = np.log(1.22e19), np.log(173.0)
g0 = np.array([0.61, 0.50, 0.49])
N = 3000; amps = []; kept = 0; ratios = []
for _ in range(N):
    Yu = randY(rng.uniform(0.3,1.2)); Yd = randY(rng.uniform(0.3,1.2)); Ye = randY(0.5)
    if sv(Yu)[0] > 2.5 or sv(Yd)[0] > 2.5: continue
    y1 = rk4(pack(Yu,Yd,Ye,g0), t_UV, t_IR, n=300)
    if y1 is None: continue
    Yu1,Yd1,_,_ = unpack(y1)
    su0, su1, sd0, sd1 = sv(Yu), sv(Yu1), sv(Yd), sv(Yd1)
    kept += 1
    for (s0,s1) in ((su0,su1),(sd0,sd1)):
        for (i,j) in ((1,0),(2,0),(2,1)):
            amps.append((s1[i]/s1[j])/(s0[i]/s0[j]))
            ratios.append((s0[i]/s0[j], s1[i]/s1[j]))
amps = np.array(amps)
print(f"(a) RUNNING: {kept} perturbative UV samples kept (all singular values <= 2.5 at M_Pl, no Landau blow-up).")
print(f"    ratio-of-ratios IR/UV over all sector/pair combinations: min {amps.min():.3f}, 1st pct {np.percentile(amps,1):.3f}, "
      f"median {np.median(amps):.3f}, 99th pct {np.percentile(amps,99):.3f}, max {amps.max():.3f}")
print(f"    share of samples with amplification > 10 (either direction): {np.mean((amps>10)|(amps<0.1)):.4f}")
# targeted: hierarchical start, does running create/destroy decades?
Yu = np.diag([3e-6, 3e-3, 1.0]).astype(complex); Yd=np.diag([1e-5,2e-4,2e-2]).astype(complex); Ye=np.diag([3e-6,6e-4,1e-2]).astype(complex)
y1 = rk4(pack(Yu,Yd,Ye,g0), t_UV, t_IR, n=800); Yu1,Yd1,_,_ = unpack(y1)
print("    hierarchical start (up: 3e-6, 3e-3, 1): IR singular values", sv(Yu1), " ratios", sv(Yu1)[1]/sv(Yu1)[0], sv(Yu1)[2]/sv(Yu1)[0])
# strongest running: y_t large at the pole edge
Yu = np.diag([1.0,1.0,2.9]).astype(complex); Yd=np.zeros((3,3),dtype=complex); Ye=np.zeros((3,3),dtype=complex)
y1 = rk4(pack(Yu,Yd,Ye,g0), t_UV, t_IR, n=800)
if y1 is not None:
    Yu1,_,_,_=unpack(y1); s=sv(Yu1); print("    extreme start diag(1,1,2.9): IR ratios (2nd/3rd, 1st/3rd) =", s[1]/s[0], s[2]/s[0], " (UV: 0.345, 0.345)")

# (b) anarchic price: probability that a Haar-type O(1) 3x3 complex Gaussian gives the observed up-type window
M = 2_000_000
A = (rng.normal(size=(M,3,3))+1j*rng.normal(size=(M,3,3)))/np.sqrt(2)
s = np.linalg.svd(A, compute_uv=False)     # descending
r21 = s[:,1]/s[:,0]; r31 = s[:,2]/s[:,0]
obs = (7.4e-3, 7.5e-6)                       # m_c/m_t, m_u/m_t at the weak scale (order of magnitude, PDG-like)
inwin = (r21 < obs[0]*3) & (r31 < obs[1]*3)
print(f"(b) ANARCHY PRICE (reading): {M} complex-Gaussian 3x3 draws: median sv2/sv1 = {np.median(r21):.3f}, median sv3/sv1 = {np.median(r31):.4f};")
print(f"    fraction with sv2/sv1 < {3*obs[0]:.3g} AND sv3/sv1 < {3*obs[1]:.3g}: {np.mean(inwin):.2e}  ({inwin.sum()} of {M})")
print(f"    fraction with sv2/sv1 < 0.022 alone: {np.mean(r21<0.022):.2e};   sv3/sv1 < 2.3e-5 alone: {np.mean(r31<2.3e-5):.2e}")
# analytic scaling: P(s3/s1 < x) ~ x^2 for 3x3 complex? print fit from data
for x in (1e-1,3e-2,1e-2,3e-3):
    print(f"      P(sv3/sv1 < {x:g}) = {np.mean(r31<x):.2e}")
