"""A30 q1_dirac: does the threshold reflection depend on how the incoming waves disperse?
(supplied 1D toy).

Chain with hopping -t and a staggered mass m(-1)^j: bands E = +-sqrt(m^2 + 4t^2 cos^2 k), a
massive Dirac particle around k = pi/2 (m = 0: massless, the half-filled chain's low-energy
waves).  Wall at 0, capture rate Gam at the surface site 1 (rate model).  Exact transfer
matrices; reflection from flux-normalized Bloch waves.  Upper band, energy E = sqrt(m^2+...)
measured by the particle's speed v/v_light, v_light = 2t (massless speed).
Independent check: a wavepacket run at one energy.
"""
import signal
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import expm_multiply
from scipy.linalg import eigh_tridiagonal

signal.alarm(55)
t = 1.0


def Mstep(Vj, E):
    return np.array([[(Vj - E) / t, -1.0], [1.0, 0.0]], dtype=complex)


def flux(x):
    # x = [psi_{j+1}, psi_j]; probability current from j to j+1 for hopping -t
    return -2 * t * np.imag(np.conj(x[1]) * x[0]) * (-1)


def absorb(E, m, Gam):
    V = lambda j: m * (-1) ** j
    X1 = np.array([((V(1) - 0.5j * Gam - E) * 1.0 - 0.0) / t, 1.0], dtype=complex)   # [psi_2, psi_1]
    C = Mstep(V(3), E) @ Mstep(V(2), E)
    lam, W = np.linalg.eig(C)
    fl = np.array([flux(W[:, i]) for i in range(2)])
    i_in = int(np.argmin(fl)); i_out = 1 - i_in          # incoming moves toward the wall (negative flux)
    coef = np.linalg.solve(W, X1)
    a, b = coef[i_in], coef[i_out]
    R2 = (abs(b) ** 2 * abs(fl[i_out])) / (abs(a) ** 2 * abs(fl[i_in]))
    return 1 - R2, lam


# sanity: m = 0 against closed form A = 2 tGam s/(t^2 + Gam^2/4 + tGam s)
for k in [0.4, 1.0, 1.4]:
    E = 2 * t * np.cos(k)          # upper band E>0 <-> |cos k|
    A, lam = absorb(E, 0.0, 2.0)
    s = np.sin(k)
    print(f"m=0 check k={k}: transfer A={A:.10f}  closed form {2*2*s/(1+1+2*s):.10f}")

print("\nmassless (m=0), Gam=2t: low-energy waves near the band centre are fast; A vs E/(2t):")
rows = []
for Ef in [0.001, 0.01, 0.1, 0.3, 0.6, 0.9, 0.99]:
    E = 2 * t * Ef
    k = np.arccos(Ef)                       # upper band E = 2t|cos k|
    A, _ = absorb(E, 0.0, 2.0)
    rows.append(f"E/2t={Ef}: A={A:.6f} (v/2t={np.sin(k):.3f}; 1-A vs tan^2(d/2)={np.tan(np.arcsin(Ef)/2)**2:.2e}|{1-A:.2e})")
print("  " + "\n  ".join(rows))
print("\nmassive (m>0), upper band near the gap (slow when E -> m), Gam = 2t: A vs speed v/(2t)")
for m in [0.05, 0.2]:
    rows = []
    ks = np.linspace(1e-6, np.pi / 2 - 1e-9, 400001)
    Eks = np.sqrt(m * m + 4 * t * t * np.cos(ks) ** 2)
    vks = 4 * t * t * np.cos(ks) * np.sin(ks) / Eks
    for vfrac in [0.003, 0.01, 0.03, 0.1, 0.3, 0.6, 0.9]:
        cand = np.where(vks >= vfrac * 2 * t)[0]
        if len(cand) == 0:
            rows.append(f"v={vfrac}: n/a"); continue
        i = cand.max()
        A, _ = absorb(Eks[i], m, 2.0)
        rows.append(f"v/2t={vfrac:5.3f}: A={A:.4f} (E-m={Eks[i]-m:.2e})")
    print(f" m={m}: vmax/2t={vks.max()/2:.3f}\n   " + "\n   ".join(rows))

# packet check at one massive, slow point
m, Gam = 0.2, 2.0
M = 2400
diag0 = np.array([m * (-1) ** j for j in range(1, M + 1)], dtype=float)
e, U = eigh_tridiagonal(diag0, -t * np.ones(M - 1))
j = np.arange(1, M + 1)
kp = np.pi / 2 - 0.35
x0, s = M // 2, 60.0
g = np.exp(-((j - x0) ** 2) / (4 * s * s)) * np.exp(1j * kp * j)
c = U.T @ g
c[e < 0] = 0.0                                       # upper band only
psi = U @ c
psi /= np.linalg.norm(psi)
w = np.abs(U.T @ psi) ** 2
Hd = diags([-t * np.ones(M - 1), diag0.astype(complex) + np.where(j == 1, -0.5j * Gam, 0), -t * np.ones(M - 1)], [-1, 0, 1], format='csr')
Ek = np.sqrt(m * m + 4 * t * t * np.cos(kp) ** 2)
vk = 4 * t * t * np.cos(kp) * np.sin(kp) / Ek
T = 1.8 * x0 / vk
out = expm_multiply(-1j * Hd * T, psi)
Pabs = 1 - np.linalg.norm(out) ** 2
pred = sum(w[n] * absorb(e[n], m, Gam)[0] for n in range(M) if w[n] > 1e-12 and e[n] > m + 1e-9)
print(f"\npacket check m={m}, k0={kp:.3f} (v/2t={vk/2:.3f}): packet captured {Pabs:.5f} vs transfer-matrix average {pred:.5f}")
