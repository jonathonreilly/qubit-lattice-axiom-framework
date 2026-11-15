"""p1: checks for PLD.md §7 (PLD-lin) and Lemma HS. Criteria: checks/p1_criteria.md (written first).
d = 4, L = 3, real abelian 1-forms on periodic tori, each level in its own units."""
import itertools, math, resource, sys, time
import numpy as np

L, D, O = 3, 4, 1  # block side, dimension, root offset (L-1)/2
PAIRS = [(m, n) for m in range(D) for n in range(D) if m < n]
rng = np.random.default_rng(20261027)
out = []
def say(s): out.append(s); print(s)

def d1(A):  # 1-form (4, n,n,n,n) -> 2-form (6, n,n,n,n)
    return np.stack([np.roll(A[n], -1, m) - A[n] - np.roll(A[m], -1, n) + A[m] for (m, n) in PAIRS])
def d1T(F):
    G = np.zeros((D,) + F.shape[1:])
    for k, (m, n) in enumerate(PAIRS):
        G[n] += np.roll(F[k], 1, m) - F[k]
        G[m] += -np.roll(F[k], 1, n) + F[k]
    return G
def d0(lam):
    return np.stack([np.roll(lam, -1, a) - lam for a in range(D)])
def qstr(A):  # fine side n=T*L -> coarse side T
    n = A.shape[1]; T = n // L; res = []
    for mu in range(D):
        S = sum(np.roll(A[mu], -j, mu) for j in range(L))
        res.append(S.reshape(T, L, T, L, T, L, T, L).sum(axis=(1, 3, 5, 7)) / L**4)
    return np.stack(res)
def qstrT(C):
    res = []
    for mu in range(D):
        up = C[mu]
        for a in range(D): up = np.repeat(up, L, axis=a)
        res.append(sum(np.roll(up, j, mu) for j in range(L)) / L**4)
    return np.stack(res)

def roots(T):
    g = np.indices((T,) * D)
    return L * g + O
def path_int(A, start, delta, sigma):
    n = A.shape[1]; cur = start.copy(); tot = np.zeros(start.shape[1:])
    for a in sigma:
        for _ in range(abs(delta[a])):
            if delta[a] > 0:
                tot += A[a][tuple(cur % n)]; cur[a] += 1
            else:
                cur[a] -= 1; tot -= A[a][tuple(cur % n)]
    return tot
ORDERS = list(itertools.permutations(range(D)))
DELTAS = list(itertools.product(range(-O, O + 1), repeat=D))
def h_slice(A):
    T = A.shape[1] // L; c = roots(T)
    return sum(path_int(A, c, dl, sg) for sg in ORDERS for dl in DELTAS) / (len(ORDERS) * len(DELTAS))
def qroot(A):
    n = A.shape[1]; T = n // L; c = roots(T); res = []
    for mu in range(D):
        e = np.zeros((D,) + (1,) * D, dtype=int); e[mu] = L
        acc = np.zeros((T,) * D)
        for sg in ORDERS:
            for dl in DELTAS:
                y = c + np.array(dl).reshape((D,) + (1,) * D)
                leg = np.zeros((T,) * D); yy = y.copy()
                for _ in range(L):
                    leg += A[mu][tuple(yy % n)]; yy[mu] += 1
                acc += path_int(A, c, dl, sg) + leg - path_int(A, c + e, dl, sg)
        res.append(acc / (len(ORDERS) * len(DELTAS)))
    return np.stack(res)

def gram(fwd, adj, shape_out):
    N = int(np.prod(shape_out)); G = np.zeros((N, N))
    for i in range(N):
        e = np.zeros(N); e[i] = 1.0
        G[:, i] = fwd(adj(e.reshape(shape_out))).ravel()
    return G

ok = {}
t0 = time.time()
# ---- G: validity
T = 2; n = T * L
errs = []
for _ in range(3):
    x = rng.standard_normal((D,) + (n,) * D); y = rng.standard_normal((D,) + (T,) * D)
    errs.append(abs(np.vdot(qstr(x), y) - np.vdot(x, qstrT(y))) / (np.linalg.norm(x) * np.linalg.norm(y)))
    x2 = rng.standard_normal((D,) + (n,) * D); F = rng.standard_normal((6,) + (n,) * D)
    errs.append(abs(np.vdot(d1(x2), F) - np.vdot(x2, d1T(F))) / (np.linalg.norm(x2) * np.linalg.norm(F)))
gerr = []
for _ in range(3):
    lam = rng.standard_normal((n,) * D); c = roots(T)
    lhs = qroot(d0(lam)); rhs = d0(lam[tuple(c)])
    gerr.append(np.max(np.abs(lhs - rhs)) / np.max(np.abs(d0(lam))))
ok['G'] = max(errs) <= 1e-10 and max(gerr) <= 1e-12
say(f"G: dot-test max rel err {max(errs):.2e}; Q_root(d lam) - d(ev lam) max rel {max(gerr):.2e} -> {'PASS' if ok['G'] else 'FAIL'}")

# ---- A: Schur bound
resA = []
for T in (2, 3):
    n = T * L
    G = gram(qstr, qstrT, (D,) + (T,) * D)
    lam = np.linalg.eigvalsh(G).max(); resA.append((T, lam, lam * L**2))
ok['A'] = all(l <= L**-2 * (1 + 1e-12) for _, l, _ in resA)
say("A: " + "; ".join(f"T={T}: lam_max={l:.15f}, ratio to L^-2 = {r:.12f}" for T, l, r in resA) + f" -> {'PASS' if ok['A'] else 'FAIL'}")

# ---- B: identity
T = 2; n = T * L; e1, e2 = 0.0, 0.0
for _ in range(5):
    A = rng.standard_normal((D,) + (n,) * D); M = np.max(np.abs(A))
    qr, qs = qroot(A), qstr(A)
    e1 = max(e1, np.max(np.abs(d1(qr) - d1(qs))) / M)
    e2 = max(e2, np.max(np.abs(qr - (qs - d0(h_slice(A))))) / M)
ok['B'] = e1 <= 1e-12 and e2 <= 1e-12
say(f"B: max|dQ_root A - dQ_str A|/max|A| = {e1:.2e}; max|Q_root - (Q_str - dh)|/max|A| = {e2:.2e} -> {'PASS' if ok['B'] else 'FAIL'}")

# ---- C: noise covariance
def sigma_k(T, k):
    shp = (6,) + (T,) * D; N = int(np.prod(shp)); G = np.zeros((N, N))
    for i in range(N):
        e = np.zeros(N); e[i] = 1.0; v = d1T(e.reshape(shp))
        vs = [v]
        for m in range(1, k): vs.append(qstrT(vs[-1]))
        col = np.zeros(shp)
        for m, w in enumerate(vs):
            u = w
            for _ in range(m): u = qstr(u)
            col += d1(u)
        G[:, i] = col.ravel()
    return np.linalg.eigvalsh((G + G.T) / 2).max()
resC = {}
for (T, k) in [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2)]:
    lam = sigma_k(T, k); bound = 16 * sum(L**(-2 * m) for m in range(k))
    resC[(T, k)] = (lam, bound)
    say(f"C: T={T} k={k}: lam_max(Sigma_k) = {lam:.12f}, bound 16*sum L^-2m = {bound:.12f}, crude 16k = {16*k}, ratio lam/bound = {lam/bound:.6f}")
ok['C'] = all(l <= b * (1 + 1e-10) for l, b in resC.values()) and all(resC[(T, 1)][0] <= 16 * (1 + 1e-12) for T in (2, 3))
for T in (2,):
    inc = [resC[(T, k + 1)][0] - resC[(T, k)][0] for k in (1, 2)]
    say(f"C (informational): T={T} increments k=1->2: {inc[0]:.3e}, k=2->3: {inc[1]:.3e}")
say(f"C -> {'PASS' if ok['C'] else 'FAIL'}")

# ---- D: HS constant
xi = np.arange(-80.0, 80.0 + 1e-4 / 2, 1e-4); ratios = []
for c in (0.0, 0.25, 1.0, 3.0):
    f = np.exp(-xi**2 / 4 + c * np.abs(xi)) / math.sqrt(2 * math.pi)
    I = np.sum((f[1:] + f[:-1]) / 2) * 1e-4
    ratios.append(I / (2 * math.sqrt(2) * math.exp(c * c)))
ok['D'] = all(r <= 1 + 1e-9 for r in ratios)
say("D: ratios " + ", ".join(f"{r:.9f}" for r in ratios) + f" -> {'PASS' if ok['D'] else 'FAIL'}")

# ---- E: ||1 - e^X||_HS <= ||X||_HS
def rand_su(Nn):
    H = rng.standard_normal((Nn, Nn)) + 1j * rng.standard_normal((Nn, Nn)); H = (H + H.conj().T) / 2
    _, V = np.linalg.eigh(H)
    w = rng.standard_normal(Nn); w -= w.mean(); w *= rng.uniform(1e-6, math.pi) / np.max(np.abs(w))
    return w, V
mx = 0.0; good = True
for Nn in (2, 3):
    for _ in range(2000):
        w, V = rand_su(Nn)
        lhs = np.linalg.norm(np.eye(Nn) - V @ np.diag(np.exp(1j * w)) @ V.conj().T)
        rhs = np.linalg.norm(w); mx = max(mx, lhs / rhs); good = good and lhs <= rhs * (1 + 1e-12)
ok['E'] = good
say(f"E: max ||1-e^X||_HS/||X||_HS = {mx:.9f} -> {'PASS' if ok['E'] else 'FAIL'}")

# ---- F: informational
Nn, kap, g2 = 2, 1.0, 0.5; c1 = 1 / (2 * (L**2 + 5.5 * 9)); beta = 11 * Nn / (48 * math.pi**2)
vals = [kap * c1**(2 * m) * (1 / g2 + beta * m * math.log(L)) / (256 * Nn) for m in range(41)]
say("F (informational): exponent of m-th term, m=0,5,10,20,40: " + ", ".join(f"{vals[m]:.3e}" for m in (0, 5, 10, 20, 40)))

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20
say(f"SUMMARY: " + " ".join(f"{k}={'PASS' if v else 'FAIL'}" for k, v in ok.items()) + f"; time {time.time()-t0:.1f}s; peak RSS {rss:.0f} MB")
