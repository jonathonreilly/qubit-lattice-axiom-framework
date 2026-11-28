# GUIDE run for row 862 (discharges nothing). Checks conventions and the linear algebra of Lemmas H1, H2, H4.
import os
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("OPENBLAS_NUM_THREADS", "1"); os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")
import numpy as np
rng = np.random.default_rng(862)

def sgn(c, mu, x, n):
    # tau of the fibre link (x, mu), colour c in {0,1,2} (CH:35)
    if mu == 0 and x[0] == n - 1 and c in (1, 2): return -1.0
    if mu == 1 and x[1] == n - 1 and c in (0, 2): return -1.0
    return 1.0

def fibre_ops(n):
    sites = [(a, b) for a in range(n) for b in range(n)]
    sidx = {(x, c): 3 * i + c for i, x in enumerate(sites) for c in range(3)}
    lidx = {(x, mu, c): 3 * (2 * i + mu) + c for i, x in enumerate(sites) for mu in range(2) for c in range(3)}
    def sh(x, mu): return ((x[0] + (mu == 0)) % n, (x[1] + (mu == 1)) % n)
    D0 = np.zeros((6 * n * n, 3 * n * n))
    for x in sites:
        for mu in range(2):
            for c in range(3):
                D0[lidx[(x, mu, c)], sidx[(sh(x, mu), c)]] += 1.0
                D0[lidx[(x, mu, c)], sidx[(x, c)]] -= sgn(c, mu, x, n)
    D1 = np.zeros((3 * n * n, 6 * n * n))
    for i, x in enumerate(sites):
        for c in range(3):
            r = 3 * i + c
            D1[r, lidx[(x, 0, c)]] += sgn(c, 1, sh(x, 0), n)      # tau_nu X_mu(y), nu-link at y+mu
            D1[r, lidx[(sh(x, 0), 1, c)]] += 1.0                  # X_nu(y+mu)
            D1[r, lidx[(sh(x, 1), 0, c)]] -= 1.0                  # X_mu(y+nu)
            D1[r, lidx[(x, 1, c)]] -= sgn(c, 0, sh(x, 1), n)      # tau_mu X_nu(y), mu-link at y+nu
    return sites, sidx, lidx, sh, D0, D1

def stack_form(n, M, T, a=0.0):
    sites, sidx, lidx, sh, D0, D1F = fibre_ops(n)
    nf, ns = 6 * n * n, 3 * n * n
    bpts = [(t, j) for t in range(T) for j in range(M)]
    tedges = [(t, j) for t in range(T - 1) for j in range(M)]     # (t,j)->(t+1,j)
    redges = [(t, j) for t in range(T) for j in range(M)]         # (t,j)->(t,j+1)
    off = {}; pos = 0
    for b in bpts: off[("f", b)] = pos; pos += nf
    for e in tedges: off[("t", e)] = pos; pos += ns
    for e in redges: off[("r", e)] = pos; pos += ns
    dim = pos
    rows = []; wts = []
    def newrow(w):
        rows.append(np.zeros(dim)); wts.append(w); return rows[-1]
    for b in bpts:                                               # fibre plaquettes
        w = 0.5 if b[0] in (0, T - 1) else 1.0
        for k in range(D1F.shape[0]):
            r = newrow(w); r[off[("f", b)]:off[("f", b)] + nf] = D1F[k]
    def mixed(b, bp, ekey, w):
        for x in sites:
            for mu in range(2):
                for c in range(3):
                    r = newrow(w)
                    r[off[("f", b)] + lidx[(x, mu, c)]] += 1.0
                    r[off[ekey] + sidx[(sh(x, mu), c)]] += 1.0
                    r[off[("f", bp)] + lidx[(x, mu, c)]] -= 1.0
                    r[off[ekey] + sidx[(x, c)]] -= sgn(c, mu, x, n)
    for (t, j) in tedges: mixed((t, j), (t + 1, j), ("t", (t, j)), 1.0)
    for (t, j) in redges: mixed((t, j), (t, (j + 1) % M), ("r", (t, j)), 0.5 if t in (0, T - 1) else 1.0)
    for (t, j) in tedges:                                        # base plaquettes (3,4) at each x, colour
        for x in sites:
            for c in range(3):
                r = newrow(1.0)
                r[off[("t", (t, j))] + sidx[(x, c)]] += 1.0
                r[off[("r", (t + 1, j))] + sidx[(x, c)]] += 1.0
                r[off[("t", (t, (j + 1) % M))] + sidx[(x, c)]] -= 1.0
                r[off[("r", (t, j))] + sidx[(x, c)]] -= 1.0
    D1 = np.array(rows); W = np.array(wts)
    # basis of the constrained space: fibre-transverse on each fibre, free on edges
    u, s, vt = np.linalg.svd(D0.T)                               # ker D0^T
    Nb = vt[np.sum(s > 1e-10):].T                                # nf x (nf - rank)
    cols = []; psi = []
    for b in bpts:
        for k in range(Nb.shape[1]):
            v = np.zeros(dim); v[off[("f", b)]:off[("f", b)] + nf] = Nb[:, k]; cols.append(v); psi.append(-a * b[0])
    for e in tedges:
        for k in range(ns):
            v = np.zeros(dim); v[off[("t", e)] + k] = 1.0; cols.append(v); psi.append(-a * (e[0] + 0.5))
    for e in redges:
        for k in range(ns):
            v = np.zeros(dim); v[off[("r", e)] + k] = 1.0; cols.append(v); psi.append(-a * e[0])
    B = np.array(cols).T
    Q = B.T @ (D1.T * W) @ D1 @ B
    return Q, np.array(psi), D0, D1F, Nb

def G(a):
    sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]
    def ex(v, sign=1.0):
        th = np.linalg.norm(v)
        if th < 1e-300: return np.eye(2, dtype=complex)
        return np.cos(th / 2) * np.eye(2) + 1j * sign * np.sin(th / 2) * sum(v[k] / th * sig[k] for k in range(3))
    E = ex(a[0:3]) @ ex(a[3:6]) @ ex(a[6:9], -1.0) @ ex(a[9:12], -1.0)
    return 1.0 - 0.5 * np.trace(E).real

print("GUIDE run, row 862. Criteria written before the run:")
print(" (1) D1F D0F = 0; (2) least eig of D0F^T D0F = mu_n; least eig of D1F^T D1F on ker D0F^T >= mu_n;")
print(" (3) H2: least eig of sum_p w_p |D_1 Z|^2 on the constrained space >= mu_n/2;")
print(" (4) H4: sym part of e^psi (Q/4) e^-psi at a = a_n has least eig >= mu_n/8 - 4.68 (cosh a_n - 1) > 0;")
print(" (5) H1: Hessian of G at 0 equals L^T L/4; |third directional derivative of G| <= |b|^3 at random points.")
for (n, M, T) in [(2, 4, 3), (2, 6, 4), (3, 4, 3)]:
    mu = (2 * np.sin(np.pi / (2 * n))) ** 2
    an = np.arccosh(1 + mu / 300)
    Q, psi, D0, D1F, Nb = stack_form(n, M, T, a=an)
    c1 = np.abs(D1F @ D0).max()
    e0 = np.linalg.eigvalsh(D0.T @ D0).min()
    e1 = np.linalg.eigvalsh(Nb.T @ D1F.T @ D1F @ Nb).min()
    q = np.linalg.eigvalsh(Q).min()
    Eps = np.exp(psi); S = (Eps[:, None] * (Q / 4) / Eps[None, :]); S = (S + S.T) / 2
    s_min = np.linalg.eigvalsh(S).min()
    # largest a for which the weighted form stays positive (bisection), compare with arccosh(1 + mu/2)
    lo, hi = 0.0, 3.0
    for _ in range(40):
        mid = (lo + hi) / 2
        ps = psi / an * mid; Ee = np.exp(ps); Sm = Ee[:, None] * (Q / 4) / Ee[None, :]; Sm = (Sm + Sm.T) / 2
        if np.linalg.eigvalsh(Sm).min() > 0: lo = mid
        else: hi = mid
    print(f"n={n} M={M} T={T}: dim={Q.shape[0]} mu_n={mu:.6f} | (1) max|D1F D0F|={c1:.1e} | (2) eig D0^TD0={e0:.6f}, eig D1^TD1|transverse={e1:.6f}"
          f" | (3) least eig={q:.6f} vs mu_n/2={mu/2:.6f} | (4) a_n={an:.5f}: least eig sym={s_min:.6f} vs bound {mu/8 - 4.68*(np.cosh(an)-1):.6f};"
          f" a_crit={lo:.4f}, arccosh(1+mu_n/2)={np.arccosh(1+mu/2):.4f}")
# (5)
L = np.hstack([np.eye(3), np.eye(3), -np.eye(3), -np.eye(3)])
h = 1e-3; Hn = np.zeros((12, 12)); I12 = np.eye(12)
for i in range(12):
    for j in range(12):
        Hn[i, j] = (G(h * (I12[i] + I12[j])) - G(h * (I12[i] - I12[j])) - G(h * (-I12[i] + I12[j])) + G(-h * (I12[i] + I12[j]))) / (4 * h * h)
print(f"(5) max |Hess G(0) - L^T L/4| = {np.abs(Hn - L.T @ L / 4).max():.2e}")
worst = 0.0
for _ in range(4000):
    x = rng.normal(size=12) * rng.uniform(0, 3); b = rng.normal(size=12); b /= np.linalg.norm(b)
    t = 2e-2
    d3 = (G(x + 2 * t * b) - 2 * G(x + t * b) + 2 * G(x - t * b) - G(x - 2 * t * b)) / (2 * t ** 3)
    worst = max(worst, abs(d3))
print(f"(5) max over 4000 random points of |d^3/dt^3 G(x + t b)|, |b| = 1: {worst:.4f} (bound 1)")
