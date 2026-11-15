"""q4b (POST HOC to q4): q4 with a Newton-solved SU(N) maximiser W_0. Criteria: checks/q4b_criteria.md.
Identical to checks/q4_kernel_ids.py except W0 (Newton) and the extra P0 / BFGS-difference report."""
import numpy as np
from scipy.linalg import expm, polar
from scipy.optimize import minimize

rng = np.random.default_rng(20261028)


def rand_su(N, scale=1.0):
    A = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    X = (A - A.conj().T) / 2
    X -= np.trace(X) / N * np.eye(N)
    return scale * X / np.linalg.norm(X, 2)


def su_basis(N):
    B = []
    for i in range(N):
        for j in range(i + 1, N):
            E = np.zeros((N, N), complex); E[i, j] = 1; E[j, i] = -1; B.append(E)
            E = np.zeros((N, N), complex); E[i, j] = 1j; E[j, i] = 1j; B.append(E)
    for i in range(N - 1):
        E = np.zeros((N, N), complex); E[i, i] = 1j; E[i + 1, i + 1] = -1j; B.append(E)
    return B


def haar_su(N):
    Z = (rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))) / np.sqrt(2)
    Q, R = np.linalg.qr(Z)
    Q = Q @ np.diag(np.diag(R) / np.abs(np.diag(R)))
    return Q / np.linalg.det(Q) ** (1.0 / N)


def W0_bfgs(M):
    N = M.shape[0]
    U, _ = polar(M)
    U = U / np.linalg.det(U) ** (1.0 / N)
    if N == 2:
        return U
    B = su_basis(N)
    f = lambda c: -np.real(np.trace(expm(-sum(ci * b for ci, b in zip(c, B))) @ U.conj().T @ M))
    best = U
    for _ in range(3):
        r = minimize(f, np.zeros(len(B)), method='BFGS', options={'gtol': 1e-15, 'maxiter': 500})
        best = best @ expm(sum(ci * b for ci, b in zip(r.x, B)))
        U = best
        f = lambda c, U=U: -np.real(np.trace(expm(-sum(ci * b for ci, b in zip(c, B))) @ U.conj().T @ M))
    return best


def stat_F(W, M):
    """traceless anti-Hermitian part of W^{-1} M (SU(N) stationarity residual)"""
    N = M.shape[0]
    A = W.conj().T @ M
    S = (A - A.conj().T) / 2
    return S - np.trace(S) / N * np.eye(N)


P0_RES = [0.0]
DW = [0.0]


def W0(M):
    N = M.shape[0]
    U, _ = polar(M)
    U = U / np.linalg.det(U) ** (1.0 / N)
    if N == 2:
        P0_RES[0] = max(P0_RES[0], np.linalg.norm(stat_F(U, M)))
        return U
    B = su_basis(N)
    G = np.array([[np.real(np.trace(bi.conj().T @ bj)) for bj in B] for bi in B])
    coords = lambda S: np.linalg.solve(G, np.array([np.real(np.trace(b.conj().T @ S)) for b in B]))
    W = U
    for _ in range(30):
        F = stat_F(W, M)
        if np.linalg.norm(F) <= 1e-15:
            break
        f0 = coords(F)
        h = 1e-6
        J = np.zeros((len(B), len(B)))
        for i, b in enumerate(B):
            J[:, i] = (coords(stat_F(W @ expm(h * b), M)) - coords(stat_F(W @ expm(-h * b), M))) / (2 * h)
        dx = np.linalg.solve(J, -f0)
        W = W @ expm(sum(c * b for c, b in zip(dx, B)))
        W = W / np.linalg.det(W) ** (1.0 / N)
    P0_RES[0] = max(P0_RES[0], np.linalg.norm(stat_F(W, M)))
    return W


def phi(M, V):
    N = M.shape[0]
    W = W0(M)
    return (np.real(np.trace(W.conj().T @ M)) - np.real(np.trace(V.conj().T @ M))) / N


def instance(N, eta, s, q=6, p=5):
    links = [[expm(rand_su(N, eta * rng.uniform(0.3, 1.0))) for _ in range(p)] for _ in range(q)]
    w = rng.uniform(0.5, 1.5, size=q); w /= w.sum()
    H = []
    for T in links:
        h = np.eye(N, dtype=complex)
        for u in T:
            h = h @ u
        H.append(h)
    M = sum(wi * h for wi, h in zip(w, H))
    X = rand_su(N, 1.0)
    V = W0(M) @ expm(s * X)
    return links, w, H, M, X, V


def fd(f, h=1e-5):
    return (f(h) - f(-h)) / (2 * h)


res = {k: [] for k in ['K1', 'K2', 'K3', 'K4', 'K5', 'K6']}
for N in (2, 3):
    for eta in (0.02, 0.1):
        for s in (0.0, 0.003, 0.03):
            ninst = 20
            for it in range(ninst):
                links, w, H, M, X, V = instance(N, eta, s)
                W = W0(M)
                if N == 3 and it < 5:
                    DW[0] = max(DW[0], np.linalg.norm(W - W0_bfgs(M), 2))
                Z = W.conj().T - V.conj().T
                ph = phi(M, V)
                a, b = haar_su(N), haar_su(N)
                res['K1'].append(abs(phi(a @ M @ b, a @ V @ b) - ph))
                dl = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
                num = fd(lambda t: phi(M + t * dl, V))
                ana = np.real(np.trace(Z @ dl)) / N
                if s == 0.0:
                    res['K3'].append(max(abs(num), abs(ana)))
                else:
                    res['K2'].append(abs(num - ana) / (1 + abs(ana)))
                # K4: insert e^{t mu} after the first j factors of contours T in a subset S (shared link b)
                mu = rand_su(N, 1.0)
                j = 2
                S = [0, 2, 3]

                def Mt(t):
                    Hs = []
                    for iT, T in enumerate(links):
                        h = np.eye(N, dtype=complex)
                        for jj, u in enumerate(T):
                            if iT in S and jj == j:
                                h = h @ expm(t * mu)
                            h = h @ u
                        Hs.append(h)
                    return sum(wi * hh for wi, hh in zip(w, Hs))
                num = fd(lambda t: phi(Mt(t), V))
                ana = 0.0
                for iT in S:
                    P = np.eye(N, dtype=complex)
                    for u in links[iT][:j]:
                        P = P @ u
                    ana += w[iT] * np.real(np.trace(Z @ (P @ mu @ P.conj().T) @ H[iT])) / N
                res['K4'].append(abs(num - ana) / (1 + abs(ana)))
                # K5: simultaneous left / right multiplications
                e1 = fd(lambda t: phi(expm(t * mu) @ M, expm(t * mu) @ V))
                e2 = fd(lambda t: phi(M @ expm(-t * mu), V @ expm(-t * mu)))
                gV = fd(lambda t: phi(M, expm(t * mu) @ V))
                gM = fd(lambda t: phi(expm(t * mu) @ M, V))
                res['K5'].append(max(abs(e1), abs(e2), abs(gV + gM)))
            # K6 on one instance per (N, eta): gradient/s constant
            links, w, H, M, X, _ = instance(N, eta, 0.0)
            W = W0(M)
            mus = [rand_su(N, 1.0) for _ in range(20)]
            ratios = []
            for sv in (1e-4, 1e-3, 1e-2):
                V = W @ expm(sv * X)
                Z = W.conj().T - V.conj().T
                g = max(abs(np.real(np.trace(Z @ m_ @ M))) / N for m_ in mus)
                ratios.append(g / sv)
            res['K6'].append(max(ratios) / min(ratios) - 1)

thr = {'K1': 1e-12, 'K2': 1e-7, 'K3': 1e-8, 'K4': 1e-7, 'K5': 1e-8, 'K6': 0.05}
ok_all = True
for k in ['K1', 'K2', 'K3', 'K4', 'K5', 'K6']:
    m = max(res[k])
    ok = m <= thr[k]
    ok_all &= ok
    print(f"{k}: n={len(res[k])} max={m:.3e} threshold={thr[k]:.0e} {'PASS' if ok else 'FAIL'}")
p0 = P0_RES[0] <= 1e-13
ok_all &= p0
print(f"P0: max stationarity residual={P0_RES[0]:.3e} threshold=1e-13 {'PASS' if p0 else 'FAIL'}")
print(f"report: max ||W_Newton - W_BFGS||_op (SU(3), first 5 instances per cell) = {DW[0]:.3e}")
print("OVERALL:", "PASS" if ok_all else "FAIL")
