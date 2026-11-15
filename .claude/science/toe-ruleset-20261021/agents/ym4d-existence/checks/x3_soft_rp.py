"""Check x3 (criteria: x3_criteria.md, written first).
A: RP of a soft-blocked clock ring across a block-boundary plane (must be PSD).
B: site-plane Gram matrices, normalised (B1, informational) and unnormalised (B2) kernel.
C: Lemma KN algebraic core on random SU(2), SU(3) instances.
Exact sums; numpy only; reads no external files."""
import itertools, numpy as np

rng = np.random.default_rng(20261027)

def joint(q, Q, beta, kappa, blocks, normalised=True):
    ang = 2*np.pi*np.arange(q)/q
    phis = 2*np.pi*np.arange(Q)/Q
    configs = np.array(list(itertools.product(range(q), repeat=6)))
    s = ang[configs]
    w = np.exp(beta*np.sum(np.cos(s - np.roll(s, -1, axis=1)), axis=1))
    ks = []
    for b in blocks:
        M = np.mean(np.exp(1j*s[:, b]), axis=1)
        e = np.exp(kappa*np.real(np.exp(-1j*phis)[None, :]*M[:, None]))
        if normalised:
            e = e/np.sum(e, axis=1, keepdims=True)
        ks.append(e)
    P = w[:, None, None]*ks[0][:, :, None]*ks[1][:, None, :]
    P = P/np.sum(P)
    return P.reshape((q,)*6 + (Q, Q))

def minrel(G):
    ev = np.linalg.eigvalsh((G + G.T)/2)
    return ev.min()/ev.max(), np.abs(G - G.T).max()

out = []
grid = [(b, k) for b in (0.3, 1.0, 2.5) for k in (0.5, 2.0, 6.0)]
# ---- A
A_pass = True
for q in (3, 5):
    Q = 4
    worst = (1.0, 0.0)
    for beta, kappa in grid:
        P = joint(q, Q, beta, kappa, [[0, 1, 2], [3, 4, 5]])
        # axes: s0..s5, phi1, phi2 ; rows (s5,s4,s3,phi2), cols (s0,s1,s2,phi1)
        G = np.transpose(P, (5, 4, 3, 7, 0, 1, 2, 6)).reshape(q**3*Q, q**3*Q)
        r, asym = minrel(G)
        worst = (min(worst[0], r), max(worst[1], asym))
        if r < -1e-12 or asym > 1e-12:
            A_pass = False
    out.append(f"A q={q}: min eig/max eig = {worst[0]:.3e}, max|G-G^T| = {worst[1]:.2e}")
out.append(f"A: {'PASS' if A_pass else 'FAIL'}")

# ---- B (site plane through sites 0 and 3; theta x = -x mod 6)
q, Q = 3, 4
for label, norm in (("B1 normalised", True), ("B2 unnormalised", False)):
    worst = 1.0
    for beta, kappa in grid:
        P = joint(q, Q, beta, kappa, [[5, 0, 1], [2, 3, 4]], normalised=norm)
        # positive vars b = (s0,s1,s2,s3,phiA,phiB); reflected a = (s0,s5,s4,s3,phiA,phiB)
        dim = q**4*Q*Q
        G = np.zeros((dim, dim))
        idx = lambda t: np.ravel_multi_index(t, (q, q, q, q, Q, Q))
        for t in itertools.product(range(q), range(q), range(q), range(q), range(q), range(q), range(Q), range(Q)):
            s0, s1, s2, s3, s4, s5, pa, pb = t
            G[idx((s0, s5, s4, s3, pa, pb)), idx((s0, s1, s2, s3, pa, pb))] += P[s0, s1, s2, s3, s4, s5, pa, pb]
        r, asym = minrel(G)
        worst = min(worst, r)
    out.append(f"{label}: worst min eig/max eig over grid = {worst:.3e}")

# ---- C
def rand_su(N, opnorm):
    H = rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N))
    H = (H + H.conj().T)/2
    H -= np.trace(H)/N*np.eye(N)
    ev = np.linalg.eigvalsh(H)
    return 1j*H*opnorm/np.max(np.abs(ev))

def expm_ah(X):  # X anti-Hermitian
    ev, U = np.linalg.eigh(-1j*X)
    return (U*np.exp(1j*ev)) @ U.conj().T

def haar(N):
    Z = (rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N)))/np.sqrt(2)
    Qm, Rm = np.linalg.qr(Z)
    Qm = Qm*(np.diag(Rm)/np.abs(np.diag(Rm)))
    return Qm/np.linalg.det(Qm)**(1.0/N)

C_pass = True
for N in (2, 3):
    maxratio, minslack = 0.0, np.inf
    for _ in range(2000):
        S = haar(N)
        delta = rng.uniform(1e-3, 0.25)
        n = rng.integers(4, 13)
        Xs = [rand_su(N, delta*rng.uniform(1e-3, 1.0)) for _ in range(n)]
        wts = rng.dirichlet(np.ones(n))
        T = [S @ expm_ah(X) for X in Xs]
        Mbar = sum(w*t for w, t in zip(wts, T))
        Xbar = sum(w*X for w, X in zip(wts, Xs))
        Wp = S @ expm_ah(Xbar)
        R = Wp.conj().T @ Mbar - np.eye(N)
        ratio = np.linalg.norm(R, 2)/delta**2
        maxratio = max(maxratio, ratio)
        if ratio > 3 + 1e-12:
            C_pass = False
        for V in (haar(N), Wp @ expm_ah(rand_su(N, rng.uniform(0, 0.5)))):
            lhs = np.real(np.trace((Wp.conj().T - V.conj().T) @ Mbar))
            x = np.linalg.norm(V - Wp)
            slack = lhs - (0.5*x**2 - 3*np.sqrt(N)*delta**2*x)
            minslack = min(minslack, slack)
            if slack < -1e-12:
                C_pass = False
    out.append(f"C SU({N}): max ||R||_op/delta^2 = {maxratio:.4f}, min slack of inequality = {minslack:.3e}")
out.append(f"C: {'PASS' if C_pass else 'FAIL'}")
print("\n".join(out))
