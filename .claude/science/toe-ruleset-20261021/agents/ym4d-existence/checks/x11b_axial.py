"""x11b: the corner witness's tree-level Wilson coefficient in a complete axial (comb) gauge (path-ordering part = 0)
against the covariant value; same-sample re-test of x11 D. Criteria: x11b_criteria.md (written after x11 was read)."""
import itertools, resource, time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl

t0 = time.time()
E4 = np.eye(4, dtype=int)
out = []


def pr(s):
    print(s, flush=True)
    out.append(s)


def plaq_links(mu, nu, x):
    x = np.asarray(x)
    return [(mu, tuple(x + 0), 1), (nu, tuple(x + E4[mu]), 1), (mu, tuple(x + E4[nu]), -1), (nu, tuple(x), -1)]


CORNER = [plaq_links(0, 1, (0, 0, 0, 0)), plaq_links(1, 2, (0, 0, 0, 0)), plaq_links(2, 0, (0, 0, 0, 0))]


def lidx(T, mu, x):
    x = np.asarray(x) % T
    return 4 * (((x[..., 3] * T + x[..., 2]) * T + x[..., 1]) * T + x[..., 0]) + mu


def comb_tree(T):
    g = np.indices((T,) * 4).reshape(4, -1).T  # site coords (x0..x3)
    intree = np.zeros(4 * T ** 4, bool)
    for mu in range(4):
        if mu == 3:
            ok = g[:, 3] != T - 1
        elif mu == 2:
            ok = (g[:, 3] == 0) & (g[:, 2] != T - 1)
        elif mu == 1:
            ok = (g[:, 3] == 0) & (g[:, 2] == 0) & (g[:, 1] != T - 1)
        else:
            ok = (g[:, 3] == 0) & (g[:, 2] == 0) & (g[:, 1] == 0) & (g[:, 0] != T - 1)
        intree[lidx(T, mu, g[ok])] = True
    return intree


def kappa_tree(T):
    nl = 4 * T ** 4
    intree = comb_tree(T)
    assert intree.sum() == T ** 4 - 1
    g = np.indices((T,) * 4).reshape(4, -1).T
    rows, cols, vals = [], [], []
    pl = []  # list of (plane, link index array (4,V), signs)
    p = 0
    for rho, sig in itertools.combinations(range(4), 2):
        li = np.stack([lidx(T, rho, g), lidx(T, sig, g + E4[rho]), lidx(T, rho, g + E4[sig]), lidx(T, sig, g)])
        sg = np.array([1, 1, -1, -1])
        pl.append((li, sg))
        for i in range(4):
            rows.append(p + np.arange(T ** 4)); cols.append(li[i]); vals.append(np.full(T ** 4, sg[i], float))
        p += T ** 4
    Inc = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(p, nl))
    nt = np.where(~intree)[0]
    In = Inc[:, nt]
    M = (In.T @ In).tocsr()
    for (mu, x, s) in [l for P in CORNER for l in P]:
        pass
    # corner incidence vectors on all links, then restricted
    gvec = []
    for P in CORNER:
        v = np.zeros(nl)
        for (mu, x, s) in P:
            v[lidx(T, mu, x)] += s
        vr = v[nt]
        x, info = spl.cg(M, vr, rtol=1e-13, atol=0.0, maxiter=20000)
        assert info == 0, info
        res = np.linalg.norm(M @ x - vr) / np.linalg.norm(vr)
        full = np.zeros(nl); full[nt] = x
        gvec.append(full)
        # full[b] = gamma(L_P, a_b) in the tree gauge (tree links have zero covariance)
    pr(f"  T={T}: non-tree links {len(nt)}, CG residual (last) {res:.1e}")
    # path-ordering part
    kpo = 0.0
    for (P, Q, R) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        lst = CORNER[P]
        for i, j in itertools.combinations(range(4), 2):
            (mi, xi_, si), (mj, xj, sj) = lst[i], lst[j]
            bi, bj = lidx(T, mi, xi_), lidx(T, mj, xj)
            # gamma(l_i, L_Q) with l_i signed; covariance between two links in tree gauge is needed:
            # gamma(a_b, L_Q) = gvec[Q][b]
            kpo += 0.5 * si * sj * (gvec[Q][bi] * gvec[R][bj] - gvec[R][bi] * gvec[Q][bj])
    kpo *= -0.5
    kv = 0.0
    for (li, sg) in pl:
        colsr = [[sg[i] * gvec[r][li[i]] for r in range(3)] for i in range(4)]
        LP = [sum(colsr[i][r] for i in range(4)) for r in range(3)]
        for i, j in itertools.combinations(range(4), 2):
            a, b, c = LP, colsr[i], colsr[j]
            det = (a[0] * (b[1] * c[2] - b[2] * c[1]) - b[0] * (a[1] * c[2] - a[2] * c[1])
                   + c[0] * (a[1] * b[2] - a[2] * b[1]))
            kv += det.sum()
    return kpo, 0.25 * kv


def cov_arrays(T, xi=1.0):
    k = 2 * np.pi * np.fft.fftfreq(T, d=1.0 / T) / T
    K = np.meshgrid(k, k, k, k, indexing="ij")
    kh = [2 * np.sin(Ki / 2) for Ki in K]
    k2 = sum(h * h for h in kh)
    zero = k2 == 0
    k2s = np.where(zero, 1.0, k2)
    C = {}
    for mu in range(4):
        for nu in range(4):
            D = (1.0 if mu == nu else 0.0) / k2s - (1 - xi) * kh[mu] * kh[nu] / k2s ** 2
            D = np.where(zero, 0.0, D)
            C[mu, nu] = np.fft.ifftn(D * np.exp(1j * (K[mu] / 2 - K[nu] / 2))).real.copy()
    return C


def kappa_cov(T):
    # x11's covariant formulas, re-implemented on the full link covariance via the same gvec construction
    C = cov_arrays(T)
    nl = 4 * T ** 4
    g = np.indices((T,) * 4).reshape(4, -1).T
    gvec = []
    for P in CORNER:
        full = np.zeros(nl)
        for nu in range(4):
            acc = np.zeros(T ** 4)
            for (mu, x, s) in P:
                z = (np.asarray(x) - g) % T  # gamma(a_mu(x), a_nu(y)) = C_{mu nu}(x - y)
                acc += s * C[mu, nu][z[:, 0], z[:, 1], z[:, 2], z[:, 3]]
            full[lidx(T, nu, g)] = acc
        gvec.append(full)
    pl = []
    for rho, sig in itertools.combinations(range(4), 2):
        li = np.stack([lidx(T, rho, g), lidx(T, sig, g + E4[rho]), lidx(T, rho, g + E4[sig]), lidx(T, sig, g)])
        pl.append((li, np.array([1, 1, -1, -1])))
    kpo = 0.0
    for (P, Q, R) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        lst = CORNER[P]
        for i, j in itertools.combinations(range(4), 2):
            (mi, xi_, si), (mj, xj, sj) = lst[i], lst[j]
            bi, bj = lidx(T, mi, xi_), lidx(T, mj, xj)
            kpo += 0.5 * si * sj * (gvec[Q][bi] * gvec[R][bj] - gvec[R][bi] * gvec[Q][bj])
    kpo *= -0.5
    kv = 0.0
    for (li, sg) in pl:
        colsr = [[sg[i] * gvec[r][li[i]] for r in range(3)] for i in range(4)]
        LP = [sum(colsr[i][r] for i in range(4)) for r in range(3)]
        for i, j in itertools.combinations(range(4), 2):
            a, b, c = LP, colsr[i], colsr[j]
            kv += (a[0] * (b[1] * c[2] - b[2] * c[1]) - b[0] * (a[1] * c[2] - a[2] * c[1])
                   + c[0] * (a[1] * b[2] - a[2] * b[1])).sum()
    return kpo, 0.25 * kv


pr("x11b: complete axial (comb) gauge vs covariant (xi = 1); kappa := coefficient of g^4 N(N^2-1)")
F1 = True; F2 = True
for T in [6, 8, 12]:
    kpo_t, kv_t = kappa_tree(T)
    kpo_c, kv_c = kappa_cov(T)
    kt, kc = kpo_t + kv_t, kpo_c + kv_c
    rel = abs(kt - kc) / abs(kc)
    F1 &= abs(kpo_t) <= 1e-12
    F2 &= rel <= 0.05
    pr(f"T={T:2d}: tree gauge kappa_PO={kpo_t:+.3e} kappa_V={kv_t:+.9f} | covariant kappa_PO={kpo_c:+.9f} "
       f"kappa_V={kv_c:+.9f} total={kc:+.9f} | rel diff {rel:.2e}")
pr(f"F1 (kappa_PO^tree = 0) {'PASS' if F1 else 'FAIL'}; F2 (tree total = covariant total within 5%) {'PASS' if F2 else 'FAIL'}")


def basis(N):
    if N == 2:
        s = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
        return [-0.5j * m for m in s]
    l = np.zeros((8, 3, 3), complex)
    l[0][0, 1] = l[0][1, 0] = 1
    l[1][0, 1] = -1j; l[1][1, 0] = 1j
    l[2][0, 0] = 1; l[2][1, 1] = -1
    l[3][0, 2] = l[3][2, 0] = 1
    l[4][0, 2] = -1j; l[4][2, 0] = 1j
    l[5][1, 2] = l[5][2, 1] = 1
    l[6][1, 2] = -1j; l[6][2, 1] = 1j
    l[7] = np.diag([1, 1, -2]) / np.sqrt(3)
    return [-0.5j * m for m in l]


def expm_ah(A):
    w, V = np.linalg.eigh(1j * A)
    return (V * np.exp(-1j * w)) @ V.conj().T


rng = np.random.default_rng(111)
samples = []
for N in [2, 3]:
    Tb = basis(N)
    for _ in range(100):
        Xs = [sum(rng.normal() * t for t in Tb) for _ in range(4)]
        samples.append((N, [Xs[0], Xs[1], -Xs[2], -Xs[3]]))
e = {}
for gg in [1e-2, 1e-3, 1e-4]:
    mx = 0.0
    for N, Xs in samples:
        U = np.eye(N, dtype=complex)
        for X in Xs:
            U = U @ expm_ah(gg * X)
        th = np.angle(np.linalg.eigvals(U))
        S = (2 / gg ** 2) * np.sum(2 * np.sin(th / 2) ** 2)
        L = sum(Xs)
        S2 = -np.trace(L @ L).real
        S3 = -sum(np.trace(L @ (Xs[i] @ Xs[j] - Xs[j] @ Xs[i])).real for i, j in itertools.combinations(range(4), 2))
        mx = max(mx, abs((S - S2) / gg - S3))
    e[gg] = mx
r1, r2 = e[1e-3] / e[1e-2], e[1e-4] / e[1e-3]
Dp = 0.08 <= r1 <= 0.12 and 0.08 <= r2 <= 0.12
pr(f"D' e(1e-2)={e[1e-2]:.3e} e(1e-3)={e[1e-3]:.3e} e(1e-4)={e[1e-4]:.3e} ratios {r1:.3f}, {r2:.3f} {'PASS' if Dp else 'FAIL'}")
pr(f"OVERALL: F1 {'PASS' if F1 else 'FAIL'}, F2 {'PASS' if F2 else 'FAIL'}, D' {'PASS' if Dp else 'FAIL'}")
pr(f"wall {time.time() - t0:.1f} s; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20:.0f} MB")
