# GUIDE checks for row 903 (free-wall Gaussian test). Small, single-threaded.
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np
from scipy import integrate

def lam(th):
    return 2.0 - 2.0 * np.cos(th)

def omega(M2, th):
    x = (M2 + lam(th)) / 2.0
    return np.log1p(x + np.sqrt(x * (x + 2.0)))

def Fa(a, w):
    return -np.log1p(-np.exp(-a * w))

def grid(kind, n):
    if kind == "N":
        return np.pi * np.arange(n) / n
    if kind == "E":
        return np.pi * np.arange(1, n) / n
    if kind == "D":
        return np.pi * np.arange(1, n + 1) / (n + 1)
    raise ValueError

def path_L(kind, n):
    if kind == "D":
        L = 2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
        return L
    # Neumann vertex Laplacian
    L = np.zeros((n, n))
    for i in range(n - 1):
        L[i, i] += 1; L[i + 1, i + 1] += 1; L[i, i + 1] -= 1; L[i + 1, i] -= 1
    if kind == "N":
        return L
    if kind == "E":  # edge Laplacian d d^T on the n-1 edges
        dmat = np.zeros((n - 1, n))
        for i in range(n - 1):
            dmat[i, i] = -1; dmat[i, i + 1] = 1
        return dmat @ dmat.T
    raise ValueError

def cycle_L(a):
    L = 2 * np.eye(a)
    for i in range(a):
        L[i, (i + 1) % a] -= 1; L[(i + 1) % a, i] -= 1
    return L

def kron_sum(mats):
    n = [M.shape[0] for M in mats]
    out = np.zeros((int(np.prod(n)),) * 2)
    for i, M in enumerate(mats):
        ops = [np.eye(k) for k in n]
        ops[i] = M
        K = ops[0]
        for O in ops[1:]:
            K = np.kron(K, O)
        out += K
    return out

# ---------- A. direct 4D determinants vs mode formula ----------
def check_det(a, b, c, d, m, kind):
    A4 = kron_sum([cycle_L(a), path_L(kind, b), path_L(kind, c), path_L(kind, d)]) + m * m * np.eye(a * b * c * d)
    sign, ld = np.linalg.slogdet(A4)
    logW_direct = -0.5 * ld
    Ls = kron_sum([path_L(kind, b), path_L(kind, c), path_L(kind, d)])
    ev = np.linalg.eigvalsh(Ls) + m * m
    x = ev / 2.0
    wK = np.log1p(x + np.sqrt(x * (x + 2)))
    logW_modes = -np.sum(np.log(2 * np.sinh(a * wK / 2)))
    th1, th2, th3 = (grid(kind, n) for n in (b, c, d))
    M2 = m * m + lam(th2)[:, None] + lam(th3)[None, :]
    wA = omega(M2[None, :, :], th1[:, None, None])
    logW_grid = -np.sum(np.log(2 * np.sinh(a * wA / 2)))
    return sign, logW_direct, logW_modes, logW_grid

print("A. direct 4D log W vs oscillator mode formula (eigvalsh) vs analytic grid")
for kind in ("N", "D"):
    for (a, b, c, d, m) in [(3, 4, 3, 3, 0.3), (4, 6, 3, 4, 0.1), (6, 5, 4, 4, 1.0)]:
        s, x1, x2, x3 = check_det(a, b, c, d, m, kind)
        print(f"  {kind} a={a} b={b} c={c} d={d} m={m}: sign={s:+.0f} direct={x1:.12f} modes={x2:.12f} grid={x3:.12f} maxdiff={max(abs(x1-x2),abs(x1-x3)):.2e}")

# ---------- A2. Proca on the cellular complex vs tower formula ----------
def proca_check(a, b, c, d, m):
    dims = (a, b, c, d)
    idx = {}
    verts = [(t, x, y, z) for t in range(a) for x in range(b) for y in range(c) for z in range(d)]
    for i, v in enumerate(verts):
        idx[v] = i
    def shift(v, mu):
        w = list(v); w[mu] += 1
        if mu == 0:
            w[0] %= a
            return tuple(w)
        return tuple(w) if w[mu] < dims[mu] else None
    edges = {}
    for v in verts:
        for mu in range(4):
            w = shift(v, mu)
            if w is not None:
                edges[(v, mu)] = len(edges)
    rows = []
    for v in verts:
        for mu in range(4):
            for nu in range(mu + 1, 4):
                vm = shift(v, mu); vn = shift(v, nu)
                if vm is None or vn is None:
                    continue
                vmn = shift(vm, nu)
                if vmn is None:
                    continue
                r = np.zeros(len(edges))
                r[edges[(v, mu)]] += 1; r[edges[(vm, nu)]] += 1
                r[edges[(vn, mu)]] -= 1; r[edges[(v, nu)]] -= 1
                rows.append(r)
    d1 = np.array(rows)
    Q = d1.T @ d1 + m * m * np.eye(len(edges))
    s, ld = np.linalg.slogdet(Q)
    logZ_direct = -0.5 * ld
    N0 = len(verts)
    tot = -N0 * np.log(m)
    for i in (1, 2, 3):
        mats = [cycle_L(a)] + [path_L("E" if j == i else "N", dims[j]) for j in (1, 2, 3)]
        Mi = kron_sum(mats) + m * m * np.eye(int(np.prod([M.shape[0] for M in mats])))
        tot += -0.5 * np.linalg.slogdet(Mi)[1]
    return s, logZ_direct, tot

print("A2. Proca (natural cellular walls): direct 1-form determinant vs three scalar towers")
for (a, b, c, d, m) in [(3, 3, 2, 2, 0.5), (3, 4, 3, 2, 0.2), (4, 3, 3, 3, 1.3)]:
    s, x1, x2 = proca_check(a, b, c, d, m)
    print(f"  a={a} b={b} c={c} d={d} m={m}: sign={s:+.0f} direct={x1:.12f} towers={x2:.12f} diff={abs(x1-x2):.2e}")

# ---------- B. delta_e three ways ----------
def hat0(fun, N):
    th = 2 * np.pi * np.arange(N) / N
    return np.mean(fun(th), axis=-1)

def delta_tail(M2, B, Nbig=1 << 15):
    # B sum_{j>=1} |hat omega(2Bj)| = -(B/2)(S(B) - hat omega(0))
    thB = np.pi * np.arange(2 * B) / B
    SB = np.mean(omega(M2[..., None], thB), axis=-1)
    h0 = hat0(lambda th: omega(M2[..., None], th), Nbig)
    return -(B / 2.0) * (SB - h0)

def G0n_int(M2, n):
    # int_{M2}^inf G_s(0,n) ds, G_s(0,n) = (1/2pi) int cos(n th)/(2 sinh w_s) dth
    def G(s):
        f = lambda th: np.cos(n * th) / (2 * np.sinh(omega(s, th)))
        return integrate.quad(f, 0, np.pi, limit=400, epsabs=1e-15, epsrel=1e-12)[0] / np.pi
    val, err = integrate.quad(lambda u: G(M2 + u / (1 - u)) / (1 - u) ** 2, 0, 1, limit=400, epsabs=1e-15, epsrel=1e-10)
    return val

print("B. delta_e for one transverse tower: e(b)-fb+D_inf  vs  image tail  vs  propagator integral (R1)")
for M2 in (0.09, 0.0004):
    w_hat0 = hat0(lambda th: omega(np.array(M2), th), 1 << 16)
    f1 = -0.5 * w_hat0
    Dinf = 0.25 * (omega(M2, 0.0) - omega(M2, np.pi))
    for b in (4, 8, 16):
        e_b = -0.5 * np.sum(omega(M2, grid("N", b)))
        d_direct = e_b - f1 * b + Dinf
        d_tail = delta_tail(np.array(M2), b)
        d_prop = b * sum(G0n_int(M2, 2 * b * j) for j in range(1, 6))
        print(f"  M2={M2} b={b}: direct={d_direct:.10e} tail={float(d_tail):.10e} propagator(j<=5)={d_prop:.10e}")
