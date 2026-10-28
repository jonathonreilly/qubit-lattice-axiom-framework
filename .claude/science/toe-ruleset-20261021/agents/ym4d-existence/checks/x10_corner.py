"""x10: the odd corner cumulant O = tr(Y_12[Y_23, Y_31]) under centred Gaussian connections.

Criteria: checks/x10_criteria.md (written before this script).
A: Monte Carlo, i.i.d. Gaussian link logs, exact exponentials and principal logs, antithetic pairs (x, -x)
   (E[O] is the even part; the pair average is unbiased and removes the dominant odd-order noise).
B0: exact order-sigma^4 Wick formula at identity covariance.  B: Feynman-gauge lattice Maxwell covariance.
C: control, linearised plaquette logs, plain (non-antithetic) Monte Carlo.
"""
import os, sys, time, resource
import numpy as np

t_start = time.time()

def basis(N):
    if N == 2:
        s = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
        return np.array([-0.5j * m for m in s])
    lam = []
    E = lambda i, j: np.eye(3)[:, [i]] @ np.eye(3)[[j], :]
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        lam.append(E(i, j) + E(j, i)); lam.append(-1j * E(i, j) + 1j * E(j, i))
    lam.append(np.diag([1, -1, 0]).astype(complex)); lam.append(np.diag([1, 1, -2]).astype(complex) / np.sqrt(3))
    return np.array([-0.5j * m for m in lam])

# links: index -> (position offset, direction); corner plaquettes as signed link lists
LINKS = [((0, 0, 0), 1), ((1, 0, 0), 2), ((0, 1, 0), 1), ((0, 0, 0), 2), ((0, 1, 0), 3), ((0, 0, 1), 2),
         ((0, 0, 0), 3), ((0, 0, 1), 1), ((1, 0, 0), 3)]
PLAQ = [[(0, 1), (1, 1), (2, -1), (3, -1)],   # P12: U1(0) U2(e1) U1(e2)^-1 U2(0)^-1
        [(3, 1), (4, 1), (5, -1), (6, -1)],   # P23: U2(0) U3(e2) U2(e3)^-1 U3(0)^-1
        [(6, 1), (7, 1), (8, -1), (0, -1)]]   # P31: U3(0) U1(e3) U3(e1)^-1 U1(0)^-1

def expm_ah(A):
    w, V = np.linalg.eigh(1j * A)            # A = -iH
    return (V * np.exp(-1j * w)[..., None, :]) @ np.conj(np.swapaxes(V, -1, -2))

def logm_u(U):
    lam, V = np.linalg.eig(U)
    Y = (V * np.log(lam)[..., None, :]) @ np.linalg.inv(V)
    return Y

def tr_comm(Y1, Y2, Y3):
    C = Y2 @ Y3 - Y3 @ Y2
    return np.real(np.einsum('nij,nji->n', Y1, C))

def corner_O(x, T, linear=False):
    # x: (n, 9, dim) real; returns O per sample (and max reconstruction error)
    A = np.einsum('nla,aij->nlij', x, T)
    if linear:
        Ls = []
        for p in PLAQ:
            Ls.append(sum(s * A[:, l] for (l, s) in p))
        return tr_comm(*Ls), 0.0
    E = expm_ah(A)
    Einv = np.conj(np.swapaxes(E, -1, -2))
    Ys, err = [], 0.0
    for p in PLAQ:
        M = None
        for (l, s) in p:
            F = E[:, l] if s > 0 else Einv[:, l]
            M = F if M is None else M @ F
        Y = logm_u(M)
        Y = 0.5 * (Y - np.conj(np.swapaxes(Y, -1, -2)))   # project to anti-Hermitian (removes rounding)
        err = max(err, float(np.max(np.abs(expm_ah(Y) - M))))
        Ys.append(Y)
    return tr_comm(*Ys), err

def mc(N, sig, n, chunk, seed, antithetic=True, linear=False):
    T = basis(N); dim = N * N - 1
    rng = np.random.default_rng(seed)
    vals = []; err = 0.0
    done = 0
    while done < n:
        m = min(chunk, n - done)
        x = sig * rng.standard_normal((m, 9, dim))
        o1, e1 = corner_O(x, T, linear)
        if antithetic:
            o2, e2 = corner_O(-x, T, linear)
            vals.append(0.5 * (o1 + o2)); err = max(err, e1, e2)
        else:
            vals.append(o1); err = max(err, e1)
        done += m
    v = np.concatenate(vals) / sig ** 4
    return v.mean(), v.std(ddof=1) / np.sqrt(len(v)), err

def wick_c4(N, Gam):
    # Gam(l, l') link covariance in units of sigma^2
    K = -0.5 * N * (N * N - 1)
    def gam(l, P):
        return sum(s * Gam(l, l2) for (l2, s) in P)
    tot = 0.0
    for (P, Q, R) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        lst = PLAQ[P]
        for i in range(4):
            for j in range(i + 1, 4):
                (li, si), (lj, sj) = lst[i], lst[j]
                tot += 0.5 * si * sj * (gam(li, PLAQ[Q]) * gam(lj, PLAQ[R]) - gam(li, PLAQ[R]) * gam(lj, PLAQ[Q]))
    return K * tot

def feynman_G(Tn):
    k = 2 * np.pi * np.fft.fftfreq(Tn)
    kh2 = sum(np.meshgrid(*([4 * np.sin(k / 2) ** 2] * 4), indexing='ij'))
    inv = np.zeros_like(kh2); m = kh2 > 0; inv[m] = 1.0 / kh2[m]
    G = np.real(np.fft.ifftn(inv))
    return G

out = []
def pr(s):
    out.append(s); print(s, flush=True)

pr("x10: odd corner cumulant O = tr(Y12[Y23,Y31]) under centred Gaussian connections")
pr("threads: " + ",".join(f"{v}={os.environ.get(v)}" for v in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"]))
sigs = [0.10, 0.15, 0.20, 0.25, 0.30]
NS = {2: 400000, 3: 200000}
res = {}
for N in (2, 3):
    pred = 0.75 * N * (N * N - 1)
    rows = []
    for i, s in enumerate(sigs):
        m, se, err = mc(N, s, NS[N], 20000, 1000 * N + i)
        rows.append((s, m, se, err))
        pr(f"A N={N} sigma={s:.2f}: E[O]/sigma^4 = {m:.5f} +- {se:.5f} (n={NS[N]} antithetic pairs; max |exp(Y)-U| = {err:.1e})")
    S = np.array([r[0] for r in rows]); Mv = np.array([r[1] for r in rows]); SE = np.array([r[2] for r in rows])
    X = np.vstack([np.ones_like(S), S ** 2]).T; Wt = 1 / SE ** 2
    cov = np.linalg.inv(X.T @ (X * Wt[:, None])); beta = cov @ (X.T @ (Wt * Mv))
    c4, c6 = beta; c4se = np.sqrt(cov[0, 0])
    a1 = abs(c4 - pred) <= 3 * c4se + 0.02 * pred
    a2 = all(r[1] > 3 * r[2] for r in rows)
    res[N] = (a1, a2)
    pr(f"A N={N}: fit c4 = {c4:.4f} +- {c4se:.4f}, c6 = {c6:.3f}; prediction 3/4 N(N^2-1) = {pred:.4f}; A1 {'PASS' if a1 else 'FAIL'}; A2 {'PASS' if a2 else 'FAIL'}")

for N in (2, 3):
    c = wick_c4(N, lambda l, l2: 1.0 if l == l2 else 0.0)
    pred = 0.75 * N * (N * N - 1)
    pr(f"B0 N={N}: Wick c4[identity] = {c:.15f}, prediction {pred}; {'PASS' if abs(c - pred) < 1e-12 else 'FAIL'}")

for Tn in (16, 24, 32):
    G = feynman_G(Tn)
    def Gam(l, l2, G=G, Tn=Tn):
        (p, mu), (q, nu) = LINKS[l], LINKS[l2]
        if mu != nu:
            return 0.0
        r = [(p[i] - q[i]) % Tn for i in range(3)]
        return G[0, r[0], r[1], r[2]]   # coordinates (x0; x1, x2, x3): corner in spatial directions 1,2,3
    vals = {N: wick_c4(N, Gam) for N in (2, 3)}
    pr(f"B T={Tn}: G(0) = {G[0,0,0,0]:.6f}; Feynman-gauge c4 = {vals[2]:.6f} (SU(2)), {vals[3]:.6f} (SU(3)); ratio to N(N^2-1): {vals[2]/6:.6f}")

for N in (2, 3):
    ok = True
    for i, s in enumerate(sigs):
        m, se, _ = mc(N, s, 100000, 20000, 5000 + 10 * N + i, antithetic=False, linear=True)
        ok = ok and abs(m) <= 4 * se
        pr(f"C N={N} sigma={s:.2f}: linearised E[O_lin]/sigma^4 = {m:.4f} +- {se:.4f}")
    pr(f"C N={N}: {'PASS' if ok else 'FAIL'}")

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6
pr(f"wall {time.time() - t_start:.1f} s; peak RSS {rss:.0f} MB")
