"""Search for nontrivial O-covariant unitary walks with a spin-1/2 coin on Z^3.

Support: all v with |v|_inf <= rho (rho = 1: 27 vectors incl. face/body
diagonals; rho = 2: 125 vectors).  Most general covariant coefficient set:
for each O-orbit, A_{v0} lies in the commutant of the stabilizer (spin-1/2
soldered action), and A_{R v0} = U_R A_{v0} U_R^dag.
Unitarity W(k)^dag W(k) = 1 is imposed exactly on a k-grid that resolves all
frequencies of W^dag W (n = 4 rho + 1 points per axis).  A nontriviality
constraint fixes the moving weight  tau = sum_{v != 0} ||A_v||_F^2  (a unitary W
has total weight 2).  Any zero-residual point with tau > 0 is a nontrivial
covariant walk.

usage: python covariant_walk_search.py RHO NSTARTS SEED
"""
import sys
import time
import itertools
import numpy as np
from scipy.optimize import least_squares
from walk_covariance import RS, US, I2, SIG

rho = int(sys.argv[1]) if len(sys.argv) > 1 else 1
nstarts = int(sys.argv[2]) if len(sys.argv) > 2 else 20
seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1
rng = np.random.default_rng(seed)

V = [np.array(v) for v in itertools.product(range(-rho, rho + 1), repeat=3)]
key = lambda v: tuple(int(x) for x in v)
seen, orbits = set(), []
for v in V:
    if key(v) in seen:
        continue
    orb = {}
    for R, U in zip(RS, US):
        w = key(R @ v)
        if w not in orb:
            orb[w] = U
    seen |= set(orb)
    stab = [U for R, U in zip(RS, US) if key(R @ v) == key(v)]
    basis4 = [I2] + SIG
    # commutant of stabilizer: average Ad over stabilizer, take span
    imgs = [sum(U @ B @ U.conj().T for U in stab) / len(stab) for B in basis4]
    M = np.array([m.reshape(-1) for m in imgs])
    u, s, vh = np.linalg.svd(M)
    r = int(np.sum(s > 1e-10))
    inv = [vh[i].reshape(2, 2) for i in range(r)]
    orbits.append((key(v), orb, inv))

n = 4 * rho + 1
grid = np.array(list(itertools.product(range(n), repeat=3))) * (2 * np.pi / n)
cols = []   # each column: W-basis function values on grid, shape (G,2,2)
weights = []  # ||A_v||^2 contribution per unit coefficient (orbit size * ||B||^2)
moving = []
for v0, orb, inv in orbits:
    for B in inv:
        Mk = np.zeros((len(grid), 2, 2), complex)
        for w, U in orb.items():
            Mk += np.exp(-1j * grid @ np.array(w))[:, None, None] * (U @ B @ U.conj().T)[None]
        cols.append(Mk)
        moving.append(v0 != (0, 0, 0))
cols = np.array(cols)  # (P,G,2,2)
P = len(cols)
G = len(grid)
# Gram of basis functions (exact by Parseval on the resolving grid): tr sum_k M_i^dag M_j / G
gram = np.einsum('ikab,jkab->ij', cols.conj(), cols) / G
mov = np.array(moving)
print(f"rho={rho}: {len(V)} vectors, {len(orbits)} orbits, {P} complex parameters, grid {n}^3")
for v0, orb, inv in orbits:
    print(f"   orbit of {v0}: size {len(orb)}, commutant dim {len(inv)}")


def unpack(x):
    return x[:P] + 1j * x[P:]


def resid(x, tau, lam=1.0):
    c = unpack(x)
    W = np.einsum('i,ikab->kab', c, cols)
    D = np.einsum('kba,kbc->kac', W.conj(), W) - I2[None]
    wmov = np.real(c.conj() @ (gram * np.outer(mov, mov)) @ c)
    r = np.concatenate([D.real.ravel(), D.imag.ravel()]) / np.sqrt(G)
    return np.concatenate([r, [lam * (wmov - tau)]])


def jac(x, tau, lam=1.0):
    c = unpack(x)
    W = np.einsum('i,ikab->kab', c, cols)
    # dD/dRe c_i = M_i^dag W + W^dag M_i ; dD/dIm c_i = -i M_i^dag W + i W^dag M_i
    A = np.einsum('ikba,kbc->ikac', cols.conj(), W)
    Bm = np.einsum('kba,ikbc->ikac', W.conj(), cols)
    dRe = A + Bm
    dIm = -1j * A + 1j * Bm
    J = np.zeros((2 * G * 4 + 1, 2 * P))
    for i in range(P):
        J[:-1, i] = np.concatenate([dRe[i].real.ravel(), dRe[i].imag.ravel()]) / np.sqrt(G)
        J[:-1, P + i] = np.concatenate([dIm[i].real.ravel(), dIm[i].imag.ravel()]) / np.sqrt(G)
    Gm = gram * np.outer(mov, mov)
    g = Gm @ c  # d(c^dag Gm c)/d Re c = 2 Re(Gm c), /d Im c = 2 Im(Gm c)
    J[-1, :P] = lam * 2 * np.real(g)
    J[-1, P:] = lam * 2 * np.imag(g)
    return J


t0 = time.time()
best = {}
bestx = {}
found = []
for tau in [0.25, 1.0, 2.0]:
    for s in range(nstarts):
        x0 = rng.normal(size=2 * P) * 0.3
        sol = least_squares(resid, x0, jac=jac, args=(tau,), method='lm', xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
        cost = float(np.sum(sol.fun ** 2))
        if cost < best.get(tau, np.inf):
            best[tau] = cost
            bestx[tau] = sol.x
        if cost < 1e-20:
            found.append((tau, sol.x))
        if time.time() - t0 > 50:
            break
    if time.time() - t0 > 50:
        break
print("min residual^2 per tau:", {k: f"{v:.3e}" for k, v in best.items()})
print("zero-residual nontrivial solutions found:", len(found), f"(time {time.time() - t0:.1f}s)")
np.save(f"best_rho{rho}_seed{seed}.npy", np.array([np.concatenate([[t], bestx[t]]) for t in bestx]))
if found:
    np.save(f"found_rho{rho}_seed{seed}.npy", np.array([f[1] for f in found]))
