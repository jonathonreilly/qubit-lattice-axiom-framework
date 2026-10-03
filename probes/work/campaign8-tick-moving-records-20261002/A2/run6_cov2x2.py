"""Search for NONTRIVIAL 2x2 strictly local steps covariant under the 24 proper cubic rotations
with spin-1/2 soldering:  U(Rk) = D(R) U(k) D(R)^+.  Support: cube {-r..r}^3.
Covariant ansatz: A_{Rv} = D(R) A_v D(R)^+, A_v in the commutant of D(Stab(v)).
Minimize F = sum_grid ||UU^+ - 1||^2; report solutions with F ~ 0 and their non-constant weight.
"""
import sys
import time
import numpy as np
from scipy.optimize import least_squares
from wlib import grid, proper_rotations, spin_half, w3_from, find_nodes_su2

t0 = time.time()
r = int(sys.argv[1]) if len(sys.argv) > 1 else 1
nseed = int(sys.argv[2]) if len(sys.argv) > 2 else 20
Rs = proper_rotations()
Ds = [spin_half(R) for R in Rs]
vs_all = [np.array(v, float) for v in np.ndindex(2 * r + 1, 2 * r + 1, 2 * r + 1)]
vs_all = [v - r for v in vs_all]
# orbits
reps, orbit_of = [], {}
for v in vs_all:
    key = tuple(v.astype(int))
    if key in orbit_of:
        continue
    reps.append(v)
    for R in Rs:
        orbit_of[tuple((R @ v).astype(int))] = len(reps) - 1
# commutant basis for each rep
E = [np.eye(2, dtype=complex)[:, [i]] @ np.eye(2, dtype=complex)[[j], :] for i in range(2) for j in range(2)]
bases = []
for v in reps:
    stab = [D for R, D in zip(Rs, Ds) if np.allclose(R @ v, v)]
    # linear map X -> [D X D^+ - X] for all stab elements; nullspace
    Mlin = np.concatenate([np.array([(D @ Ei @ D.conj().T - Ei).ravel() for Ei in E]).T for D in stab])
    _, s, vh = np.linalg.svd(Mlin)
    null = vh[np.sum(s > 1e-9):].conj()
    bases.append([nb.reshape(2, 2) for nb in null])
npar = sum(len(b) for b in bases)
print(f"r={r}: {len(reps)} orbits, {npar} complex parameters; commutant dims {[len(b) for b in bases]}")
# list of (v, orbit index, D) for every support vector
terms = []
for v in vs_all:
    o = orbit_of[tuple(v.astype(int))]
    for R, D in zip(Rs, Ds):
        if np.allclose(R @ reps[o], v):
            terms.append((v, o, D))
            break
V = np.array([t[0] for t in terms])
Kres = grid(4 * r + 2)
Ph = np.exp(1j * Kres @ V.T)


def coeffs(p):
    c = p[:npar] + 1j * p[npar:]
    Arep, i = [], 0
    for b in bases:
        Arep.append(sum(c[i + j] * b[j] for j in range(len(b))))
        i += len(b)
    return np.array([D @ Arep[o] @ D.conj().T for (v, o, D) in terms])


def resid(p):
    A = coeffs(p).reshape(len(terms), 4)
    U = (Ph @ A).reshape(-1, 2, 2)
    Em = U @ U.conj().transpose(0, 2, 1) - np.eye(2)
    return np.concatenate([Em.real.ravel(), Em.imag.ravel()])


def Ufun_factory(A):
    def f(K):
        P = np.exp(1j * np.atleast_2d(K) @ V.T)
        U = (P @ A.reshape(len(terms), 4)).reshape(-1, 2, 2)
        dU = np.stack([((1j * V[:, j][None, :] * P) @ A.reshape(len(terms), 4)).reshape(-1, 2, 2) for j in range(3)])
        return U, dU
    return f


rng = np.random.default_rng(11)
found = []
for s in range(nseed):
    p0 = rng.normal(size=2 * npar) / np.sqrt(npar)
    sol = least_squares(resid, p0, method="lm", xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=20000)
    A = coeffs(sol.x)
    nonconst = sum(np.linalg.norm(A[i]) ** 2 for i, (v, o, D) in enumerate(terms) if np.any(v != 0))
    F = np.sum(sol.fun ** 2)
    print(f"  seed {s:2d}: F={F:.2e}  nonconstant weight={nonconst:.3e}", flush=True)
    if F < 1e-20 and nonconst > 1e-6:
        found.append(A)
    if 1e-20 <= F < 1e-2:
        f = Ufun_factory(A)
        U, dU = f(grid(24))
        smin = np.linalg.svd(U, compute_uv=False).min()
        w = w3_from(U, dU)[0]
        trim = np.array([[a, b, c] for a in (0, np.pi) for b in (0, np.pi) for c in (0, np.pi)])
        Ut, _ = f(trim)
        # continuous branch of sqrt(det U) along straight paths from Gamma (det has no winding)
        u0 = []
        for kt in trim:
            ts = np.linspace(0, 1, 400)[:, None] * kt[None, :]
            Up, _ = f(ts)
            ph = np.unwrap(np.angle(np.linalg.det(Up)))
            sq = np.exp(0.5j * ph[-1])
            u0.append(round(float((np.trace(Up[-1]) / 2 / sq).real), 3))
        # also: angle of det at Gamma vs global consistency check along a closed loop
        loop = np.linspace(0, 1, 800)[:, None] * np.array([[2 * np.pi, 0, 0]])
        Ul, _ = f(loop)
        wind = (np.unwrap(np.angle(np.linalg.det(Ul)))[-1] - np.angle(np.linalg.det(Ul[0]))) / (2 * np.pi)
        print(f"      det winding along kx loop: {wind:+.3f}")
        print(f"      near-solution: min sing.val={smin:.3f}  W3_GL={w:+.4f}  U/sqrt(det) at TRIM (G,Z,Y,M?,..): {u0}")
    if time.time() - t0 > 40:
        break
print(f"nontrivial exact solutions: {len(found)}")
for A in found[:2]:
    f = Ufun_factory(A)
    # make SU(2): divide by sqrt(det) only if det is constant
    U, dU = f(grid(4 * r + 4))
    det = np.linalg.det(U)
    print(f"  det U constant? spread {np.ptp(np.angle(det/det[0])):.2e}")
    w, _ = w3_from(U, dU, U.conj().transpose(0, 2, 1))
    print(f"  W3 (exact grid) = {w:+.2e}")
    print("  coefficient norms by orbit rep:", [round(float(np.linalg.norm(A[[i for i,t in enumerate(terms) if t[1]==o][0]])),4) for o in range(len(reps))])
print(f"time {time.time()-t0:.1f}s")
np.save("cov2x2_found.npy", np.array(found) if found else np.zeros(0))
