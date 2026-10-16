"""Part 2c: decompose the k=0 effective velocity operator h_j (on one G_{3/2} level) into the two
T1 operators of a spin-3/2 multiplet: h = alpha J + beta T, T_j = J_j^3 - (41/20) J_j (orthogonal to J).
Method: find unitary basis change identifying the level with spin-3/2 by matching the D action
(after phase twist) with SU(2) spin-3/2 matrices: solve intertwiner equation numerically.
Then fit alpha, beta by least squares over the 3 components. Isotropic iff beta = 0 (then speeds
3|alpha|/2 and |alpha|/2 in block units)."""
import numpy as np, sys
from walks import *
from part2_cone import quat, eff_h, Q, Wk, dirs
from part1_decompose import su2, spin_rep, parity_O, lift_to_twoO
from scipy.optimize import minimize

D3 = class_D(3)
Dg = {k: v.astype(float) for k, v in D3.items()}
# 2O lift for class 3: twist 1; homomorphism D(R)->(+-)U(R)
_, phi = lift_to_twoO(D3, None)
pairs = []
for kk, U in phi.items():
    M = np.frombuffer(kk, dtype=np.complex128).reshape(8, 8)
    pairs.append((M, spin_rep(U, 3)))
j = 1.5; m = np.arange(j, -j - 1, -1)
Jz = np.diag(m); Jp = np.zeros((4, 4))
for i in range(1, 4): Jp[i - 1, i] = np.sqrt(j * (j + 1) - m[i] * (m[i] + 1))
J = [(Jp + Jp.T) / 2, (Jp - Jp.T) / (2j), Jz]
T = [Ji @ Ji @ Ji - 41 / 20 * Ji for Ji in J]
for a in range(3): assert abs(np.trace(J[a] @ T[a])) < 1e-12

def intertwiner(P):
    """P: 8x4 isometry onto a D-invariant subspace carrying G3/2.  Find 4x4 unitary Y with
    P^dag M P = Y S(U) Y^dag for all group elements."""
    # solve  (P^dag M P) Y - Y S = 0  for all pairs
    rows = []
    for M, S in pairs:
        A = P.conj().T @ M @ P
        rows.append(np.kron(A, np.eye(4)) - np.kron(np.eye(4), S.T))
    u, s, vh = np.linalg.svd(np.vstack(rows))
    assert s[-1] < 1e-8 and s[-2] > 1e-6, s[-3:]
    Y = vh[-1].conj().reshape(4, 4)
    Y = Y / np.sqrt(np.trace(Y.conj().T @ Y).real / 4)
    assert np.allclose(Y.conj().T @ Y, np.eye(4), atol=1e-8)
    return Y

def alpha_beta(qA, qB):
    res = []
    for lam, P, hs in eff_h(qA, qB):
        Y = intertwiner(P)
        hsp = [Y.conj().T @ h @ Y for h in hs]   # in spin-3/2 basis
        # fit hsp_a = alpha J_a + beta T_a
        Am = np.array([[np.vdot(J[a], J[a]).real, np.vdot(J[a], T[a]).real], [np.vdot(T[a], J[a]).real, np.vdot(T[a], T[a]).real]])
        rhs = np.array([sum(np.vdot(J[a], hsp[a]) for a in range(3)).real, sum(np.vdot(T[a], hsp[a]) for a in range(3)).real]) / 3
        al, be = np.linalg.solve(Am, rhs)
        resid = max(np.abs(hsp[a] - al * J[a] - be * T[a]).max() for a in range(3))
        res.append((-np.angle(lam), al, be, resid))
    return res

if __name__ == "__main__":
    rng = np.random.default_rng(5)
    for t in range(4):
        qA = quat(rng.normal(size=4)); qB = quat(rng.normal(size=4))
        for w0, al, be, r in alpha_beta(qA, qB):
            print(f"trial {t}: omega0 {w0:+.4f}  alpha {al:+.5f} beta {be:+.5f}  fit residual {r:.1e}")
    sys.stdout.flush()
    # search for isotropic point: cheap objective = mismatch of velocity spectra along 100,111,110,random
    nd = dirs(6, seed=3)
    def obj(x):
        qA = quat(x[:4]); qB = quat(x[4:])
        lam, P, hs = eff_h(qA, qB)[0]
        sps = [np.sort(np.linalg.eigvalsh(sum(n[j] * hs[j] for j in range(3)))) for n in nd]
        sc = np.mean(np.abs(sps[0])) + 1e-9
        return sum(np.sum((s - sps[0]) ** 2) for s in sps[1:]) / sc ** 2
    best = None
    for s in range(12):
        x0 = rng.normal(size=8)
        r = minimize(obj, x0, method="Nelder-Mead", options=dict(xatol=1e-12, fatol=1e-18, maxiter=6000, maxfev=6000))
        print("  start", s, "obj", r.fun); sys.stdout.flush()
        if best is None or r.fun < best.fun: best = r
    qA = quat(best.x[:4]); qB = quat(best.x[4:])
    print("best obj", best.fun, "alpha,beta:", alpha_beta(qA, qB))
    print("qA coeffs", best.x[:4] / np.linalg.norm(best.x[:4]), "qB coeffs", best.x[4:] / np.linalg.norm(best.x[4:]))
