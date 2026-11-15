"""h1: Lemma PM, Lemma KQ, Lemma RS-lin (b) of HIST.md §3. Criteria: checks/h1_criteria.md (written first)."""
import sys, math, resource, time
import numpy as np

TOL = 1e-11
T0 = time.time()


def opn(A):
    return np.linalg.norm(A, 2)


def haar(N, rng):
    Z = (rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))) / math.sqrt(2)
    Q, R = np.linalg.qr(Z)
    Q = Q @ np.diag(np.diag(R) / np.abs(np.diag(R)))
    return Q / np.linalg.det(Q) ** (1.0 / N)


def expm_ah(X):
    """exp of an anti-Hermitian matrix via eigendecomposition of the Hermitian -iX."""
    w, V = np.linalg.eigh(-1j * X)
    return V @ np.diag(np.exp(1j * w)) @ V.conj().T


def proj_su(Z):
    A = (Z - Z.conj().T) / 2
    N = Z.shape[0]
    return A - np.trace(A) / N * np.eye(N)


def rand_su(N, rng):
    H = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    return proj_su(H)


SIG = [np.eye(2, dtype=complex), 1j * np.array([[0, 1], [1, 0]], complex),
       1j * np.array([[0, -1j], [1j, 0]], complex), 1j * np.array([[1, 0], [0, -1]], complex)]


def f(W, M):
    return np.real(np.trace(W.conj().T @ M))


def maximiser(M, rng, S=None):
    N = M.shape[0]
    if N == 2:
        v = np.array([np.real(np.trace(t.conj().T @ M)) for t in SIG])
        v = v / np.linalg.norm(v)
        return sum(v[a] * SIG[a] for a in range(4))
    starts = [S] if S is not None else []
    starts += [haar(N, rng) for _ in range(20)]
    best, bW = -1e9, None
    for W in starts:
        W = W.copy()
        for it in range(4000):
            G = proj_su(W.conj().T @ M)
            g = opn(G)
            if g < 1e-14:
                break
            W = W @ expm_ah(0.5 * G)
        val = f(W, M)
        if val > best:
            best, bW = val, W
    return bW


def phi(M, W0, V):
    N = M.shape[0]
    return (f(W0, M) - f(V, M)) / N


def delta0(N):
    return min(1.0 / (640 * N), 2.0 / N ** 3)


def rand_E(N, d, rng, adversarial):
    if adversarial:
        E = rand_su(N, rng)
    else:
        E = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    return E * (d / opn(E))


ok = {}
for N in (2, 3):
    rng = np.random.default_rng(100 + N)
    d0 = delta0(N)
    # P1
    p1 = True
    for d in (d0, d0 / 3, d0 / 10, d0 / 100):
        rW, rM = 0.0, 0.0
        for i in range(400):
            S = haar(N, rng)
            M = S @ (np.eye(N) + rand_E(N, d, rng, i >= 300))
            W0 = maximiser(M, rng, S)
            rW = max(rW, opn(W0 - S) / d)
            rM = max(rM, opn(M - W0) / d)
        print(f"P1 N={N} delta={d:.3e}: max|W0-S|/delta = {rW:.4f} (<=3), max|M-W0|/delta = {rM:.4f} (<=4)")
        p1 &= (rW <= 3 + TOL) and (rM <= 4 + TOL)
    ok[f'P1_N{N}'] = p1
    # P2 informational
    for d in (0.01, 0.03, 0.1, 0.3):
        rW = 0.0
        for i in range(200):
            S = haar(N, rng)
            M = S @ (np.eye(N) + rand_E(N, d, rng, i >= 150))
            W0 = maximiser(M, rng, S)
            rW = max(rW, opn(W0 - S) / d)
        print(f"P2 (info) N={N} delta={d}: max|W0-S|/delta = {rW:.4f}")
    # G globality
    g_ok = True
    for i in range(50):
        S = haar(N, rng)
        M = S @ (np.eye(N) + rand_E(N, d0, rng, i % 2 == 0))
        W0 = maximiser(M, rng, S)
        v0 = f(W0, M)
        for _ in range(2000):
            if f(haar(N, rng), M) > v0 + TOL:
                g_ok = False
    print(f"G N={N}: globality {'PASS' if g_ok else 'FAIL'}")
    ok[f'G_N{N}'] = g_ok
    # K1, K2, K3
    k1, k2, k3, mx2 = True, True, True, 0.0
    for i in range(300):
        if i < 150:
            M = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
            M = M / opn(M) * rng.uniform(0.1, 1.0)
        else:
            S = haar(N, rng)
            M = S @ (np.eye(N) + rand_E(N, rng.uniform(0, 0.05), rng, i % 2 == 0))
            M = M / max(1.0, opn(M))
        W0 = maximiser(M, rng, None)
        dM = opn(M - W0)
        for _ in range(10):
            V = haar(N, rng)
            x = opn(V - W0)
            p = phi(M, W0, V)
            if p < x * x / (2 * N) - x * dM - TOL:
                k1 = False
            if p > x + TOL:
                k3 = False
            X = rand_su(N, rng)
            X = X / opn(X) * rng.uniform(1e-4, 1.0)
            V2 = W0 @ expm_ah(X)
            x2 = opn(V2 - W0)
            if x2 > 1 / (4 * N):
                V2 = W0 @ expm_ah(X * (1 / (4 * N)) / x2 * 0.999)
                x2 = opn(V2 - W0)
            p2 = phi(M, W0, V2)
            mx2 = max(mx2, p2 / x2 ** 2)
            if p2 > 2.5 * x2 ** 2 + TOL:
                k2 = False
    print(f"K1 N={N}: {'PASS' if k1 else 'FAIL'}; K2: {'PASS' if k2 else 'FAIL'} (max phi/x^2 = {mx2:.4f} <= 2.5); K3: {'PASS' if k3 else 'FAIL'}")
    ok[f'K1_N{N}'], ok[f'K2_N{N}'], ok[f'K3_N{N}'] = k1, k2, k3
    # R
    r_ok = True
    for e1 in (0.25, 0.5, 1.0):
        Ad = 9
        eq = min(e1 / 18, e1 / (256 * Ad * N), d0 / Ad)
        d = Ad * eq
        mn = 1e9
        for i in range(200):
            S = haar(N, rng)
            M = S @ (np.eye(N) + rand_E(N, d, rng, i % 2 == 0))
            W0 = maximiser(M, rng, S)
            for _ in range(50):
                X = rand_su(N, rng)
                X = X / opn(X)
                lo, hi = 0.0, 4.0
                for _b in range(60):
                    mid = (lo + hi) / 2
                    if opn(S @ expm_ah(mid * X) - S) < e1 / 8:
                        lo = mid
                    else:
                        hi = mid
                V = S @ expm_ah(hi * X)
                p = phi(M, W0, V)
                mn = min(mn, p * 1024 * N / e1 ** 2)
                if p < e1 ** 2 / (1024 * N) - TOL:
                    r_ok = False
        print(f"R N={N} eps1={e1}: eta_q={eq:.3e}, delta={d:.3e}, min phi*1024N/eps1^2 = {mn:.3f} (>=1)")
    ok[f'R_N{N}'] = r_ok

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6
print({k: ('PASS' if v else 'FAIL') for k, v in ok.items()})
print(f"h1: {'PASS' if all(ok.values()) else 'FAIL'}  t {time.time() - T0:.1f}s  peak RSS {rss:.0f} MB")
