"""Test C: memory of a smooth non-equilibrium modulation vs wavelength (single walker, ring L=160)."""
import numpy as np, scipy.sparse as sp, time
from scipy.integrate import solve_ivp
from common import Ring, kl

L = 160
ring = Ring(L)
x = np.arange(L)
sig = 10.0
g = np.exp(-(x - 80) ** 2 / (2 * sig ** 2))
coin = np.array([1.0, 0.0])
psi0 = (g[:, None] * coin[None, :]).astype(complex)
psi0 /= np.linalg.norm(psi0)
SZ = np.array([1.0, -1.0])

def wave(t):
    U = ring.U4(t)
    return np.einsum('aixj,xj->ai', U, psi0)

def gen(t, gamma=0.0):
    psi = wave(t)
    P = (np.abs(psi) ** 2).sum(1)
    T = np.real((np.roll(psi, -1, axis=0).conj() * SZ[None, :] * psi).sum(1))
    Pinv = np.where(P > 1e-300, 1 / np.maximum(P, 1e-300), 0.0)
    rp = np.maximum(T, 0) * Pinv
    rm = np.maximum(-np.roll(T, 1), 0) * Pinv
    idx = np.arange(L)
    rows = np.concatenate([(idx + 1) % L, (idx - 1) % L, idx])
    cols = np.concatenate([idx, idx, idx])
    vals = np.concatenate([rp, rm, -(rp + rm)])
    return P, sp.csc_matrix((vals, (rows, cols)), shape=(L, L))

def evolve(rho0, Tend, nt=7):
    ts = np.linspace(0, Tend, nt)
    f = lambda t, y: gen(t)[1] @ y
    jac = lambda t, y: gen(t)[1]
    sol = solve_ivp(f, (0, Tend), rho0, method='Radau', jac=jac, t_eval=ts, rtol=1e-10, atol=1e-14)
    return ts, sol.y.T

P0 = wave(0.0); P0 = (np.abs(P0) ** 2).sum(1)
eps = 0.5
res = []
for m in [1, 2, 4, 8, 16]:
    q = 2 * np.pi * m / L
    rho0 = P0 * (1 + eps * np.cos(q * x)); rho0 /= rho0.sum()
    ts, R = evolve(rho0, 30.0)
    D = np.array([kl(R[i], (np.abs(wave(t)) ** 2).sum(1)) for i, t in enumerate(ts)])
    ratio = D[-1] / D[0]
    pred = 1 * 30.0 * (1 - np.cos(q))     # exploratory (not pre-registered): unit-rate Poisson walk, two movers
    res.append((m, q, D[0], D[-1], ratio, -np.log(ratio), pred))
    print(f"m={m:2d} q={q:.4f} D0={D[0]:.4e} D30={D[-1]:.4e} ratio={ratio:.4f} -ln={-np.log(ratio):.4f} exploratory_pred={pred:.4f}", flush=True)
ms = np.array([r[0] for r in res], float); nl = np.array([r[5] for r in res])
sel = ms >= 2
p = np.polyfit(np.log(ms[sel]), np.log(nl[sel]), 1)[0]
print('fit exponent p in -ln ratio ~ m^p (m=2..16):', p)
