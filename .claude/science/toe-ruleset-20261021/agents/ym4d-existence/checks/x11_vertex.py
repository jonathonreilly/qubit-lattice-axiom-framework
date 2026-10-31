"""x11: tree-level (order g^4) Wilson value of the corner observable O = tr(Y12[Y23,Y31]),
path-ordering part + three-gluon-vertex part, in covariant gauges; checks B-E. Criteria: x11_criteria.md."""
import itertools, resource, time
import numpy as np

t0 = time.time()
E4 = np.eye(4, dtype=int)


def plaq_links(mu, nu, x):
    x = np.asarray(x)
    return [(mu, tuple(x), 1), (nu, tuple(x + E4[mu]), 1), (mu, tuple(x + E4[nu]), -1), (nu, tuple(x), -1)]


CORNER = [plaq_links(0, 1, (0, 0, 0, 0)), plaq_links(1, 2, (0, 0, 0, 0)), plaq_links(2, 0, (0, 0, 0, 0))]


def cov_arrays(T, xi):
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
            ph = np.exp(1j * (K[mu] / 2 - K[nu] / 2))
            c = np.fft.ifftn(D * ph)
            assert np.max(np.abs(c.imag)) < 1e-10
            C[mu, nu] = c.real.copy()
    return C


def gam_links(C, T, l1, l2):
    (m1, x1, s1), (m2, x2, s2) = l1, l2
    z = tuple((np.array(x1) - np.array(x2)) % T)
    return s1 * s2 * C[m1, m2][z]


def gam_sets(C, T, A, B):
    return sum(gam_links(C, T, a, b) for a in A for b in B)


def kappa_PO(C, T):
    tot = 0.0
    for (P, Q, R) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        lst = CORNER[P]
        for i, j in itertools.combinations(range(4), 2):
            tot += 0.5 * (gam_sets(C, T, [lst[i]], CORNER[Q]) * gam_sets(C, T, [lst[j]], CORNER[R])
                          - gam_sets(C, T, [lst[i]], CORNER[R]) * gam_sets(C, T, [lst[j]], CORNER[Q]))
    return -0.5 * tot


def kappa_V(C, T):
    # G[r][nu](y) = gamma(L_r, a_nu(y)) = sum_{(mu,x,s) in L_r} s C_{mu nu}(x - y) = s * C_{nu mu}(y - x)
    G = [[None] * 4 for _ in range(3)]
    for r in range(3):
        for nu in range(4):
            acc = np.zeros((T,) * 4)
            for (mu, x, s) in CORNER[r]:
                acc += s * np.roll(C[nu, mu], shift=x, axis=(0, 1, 2, 3))
            G[r][nu] = acc
    tot = 0.0
    for rho, sig in itertools.combinations(range(4), 2):
        links = plaq_links(rho, sig, (0, 0, 0, 0))
        cols = []  # cols[i][r] = gamma(L_r, X_i) as array over plaquette base y
        for (mu, off, s) in links:
            cols.append([s * np.roll(G[r][mu], shift=tuple(-o for o in off), axis=(0, 1, 2, 3)) for r in range(3)])
        LP = [sum(cols[i][r] for i in range(4)) for r in range(3)]
        for i, j in itertools.combinations(range(4), 2):
            a, b, c = LP, cols[i], cols[j]
            det = (a[0] * (b[1] * c[2] - b[2] * c[1]) - b[0] * (a[1] * c[2] - a[2] * c[1])
                   + c[0] * (a[1] * b[2] - a[2] * b[1]))
            tot += det.sum()
    return 0.25 * tot


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
    H = 1j * A
    w, V = np.linalg.eigh(H)
    return (V * np.exp(-1j * w)) @ V.conj().T


def logm_u(U):
    w, V = np.linalg.eig(U)
    L = V @ np.diag(np.log(w)) @ np.linalg.inv(V)
    return 0.5 * (L - L.conj().T)


def trc(A, B, C):
    return np.trace(A @ (B @ C - C @ B)).real


out = []


def pr(s):
    print(s, flush=True)
    out.append(s)


pr("x11: tree-level Wilson value of the corner witness; kappa := coefficient of g^4 N(N^2-1)")
# ---- A, B
res = {}
for T in [12, 16, 20, 24, 32]:
    for xi in [0.0, 1.0, 2.0]:
        C = cov_arrays(T, xi)
        kp = kappa_PO(C, T)
        kv = kappa_V(C, T)
        res[T, xi] = (kp, kv, kp + kv)
        pr(f"T={T:2d} xi={xi:.0f}: kappa_PO={kp:+.9f} kappa_V={kv:+.9f} kappa={kp + kv:+.9f}  (G00={C[0,0][0,0,0,0]:.6f})")
        del C
spr = {T: max(abs(res[T, xi][2] - res[T, 1.0][2]) for xi in [0.0, 2.0]) for T in [12, 16, 20, 24, 32]}
for T in spr:
    pr(f"  T={T}: xi-spread of kappa = {spr[T]:.3e} (relative {spr[T] / abs(res[T, 1.0][2]):.3e})")
k32 = res[32, 1.0][2]; drift = abs(k32 - res[24, 1.0][2])
A1 = spr[32] <= 0.02 * abs(k32) and spr[32] <= spr[16]
A2 = drift <= 0.01 * abs(k32) and abs(k32) >= 10 * spr[32] and abs(k32) >= 10 * drift
pr(f"A1 (gauge independence) {'PASS' if A1 else 'FAIL'}; A2 (convergence, non-vanishing) {'PASS' if A2 else 'FAIL'}: "
   f"kappa(1,32)={k32:+.9f}, drift 24->32 = {drift:.2e}")
B = all(abs(res[T, 1.0][0] - 0.008268) <= 2e-6 for T in [16, 20, 24, 32])
pr(f"B (kappa_PO(xi=1) = 0.008268 +- 2e-6, T>=16) {'PASS' if B else 'FAIL'}")
# ---- C
rng = np.random.default_rng(11)
Cok = True
for N in [2, 3]:
    Tb = np.array(basis(N)); d = len(Tb)
    M = rng.normal(size=(6, 6)); Gm = M @ M.T / 6 + 0.5 * np.eye(6)
    Lc = np.linalg.cholesky(Gm)
    n = 400000; vals = []
    for _ in range(n // 20000):
        x = np.einsum('ij,njd->nid', Lc, rng.normal(size=(20000, 6, d)))
        mats = np.einsum('nid,dab->niab', x, Tb)
        def tcomm(A, Bm, Cm):
            return np.einsum('nab,nba->n', A, Bm @ Cm - Cm @ Bm).real
        vals.append(tcomm(mats[:, 0], mats[:, 1], mats[:, 2]) * tcomm(mats[:, 3], mats[:, 4], mats[:, 5]))
    v = np.concatenate(vals); m, se = v.mean(), v.std() / np.sqrt(len(v))
    pred = 0.25 * N * (N * N - 1) * np.linalg.det(Gm[:3, 3:])
    ok = abs(m - pred) <= 4 * se; Cok &= ok
    pr(f"C N={N}: MC {m:+.5f} +- {se:.5f}, Wick {pred:+.5f}, {abs(m - pred) / se:.2f} SE {'ok' if ok else 'BAD'}")
pr(f"C {'PASS' if Cok else 'FAIL'}")
# ---- D
e = {}
for g in [1e-2, 1e-3]:
    mx = 0.0
    for N in [2, 3]:
        Tb = basis(N)
        for _ in range(100):
            Xs = [sum(rng.normal() * t for t in Tb) for _ in range(4)]
            Xs = [Xs[0], Xs[1], -Xs[2], -Xs[3]]
            U = np.eye(N, dtype=complex)
            for X in Xs:
                U = U @ expm_ah(g * X)
            S = (2 / g ** 2) * np.trace(np.eye(N) - U).real
            L = sum(Xs)
            S2 = 0.5 * (-2 * np.trace(L @ L).real)
            S3 = -sum(np.trace(L @ (Xs[i] @ Xs[j] - Xs[j] @ Xs[i])).real for i, j in itertools.combinations(range(4), 2))
            mx = max(mx, abs((S - S2) / g - S3))
    e[g] = mx
Dok = e[1e-3] <= 0.2 * e[1e-2] and e[1e-3] <= 1e-2
pr(f"D e(1e-2)={e[1e-2]:.3e} e(1e-3)={e[1e-3]:.3e} {'PASS' if Dok else 'FAIL'}")
# ---- E
Eok = True; worst = 0.0
outer = [[(1, (1, 0, 0, 0)), (0, (0, 1, 0, 0))], [(2, (0, 1, 0, 0)), (1, (0, 0, 1, 0))], [(0, (0, 0, 1, 0)), (2, (1, 0, 0, 0))]]
for choice in itertools.product([0, 1], repeat=3):
    tree = [(0, (0, 0, 0, 0)), (1, (0, 0, 0, 0)), (2, (0, 0, 0, 0))] + [outer[p][choice[p]] for p in range(3)]
    nontree = [outer[p][1 - choice[p]] for p in range(3)]
    for N in [2, 3]:
        Tb = basis(N)
        for _ in range(50):
            links = {}
            for P in CORNER:
                for (mu, x, s) in P:
                    if (mu, x) not in links:
                        links[mu, x] = expm_ah(sum(rng.normal() * 1.3 * t for t in Tb))
            h = {(0, 0, 0, 0): np.eye(N, dtype=complex)}
            changed = True
            while changed:
                changed = False
                for (mu, x) in tree:
                    y = tuple(np.array(x) + E4[mu])
                    if x in h and y not in h:
                        h[y] = h[x] @ links[mu, x]; changed = True
            gf = {}
            for (mu, x), U in links.items():
                y = tuple(np.array(x) + E4[mu])
                gf[mu, x] = h[x] @ U @ np.linalg.inv(h[y])

            def plaqs(lk):
                Ps = []
                for P in CORNER:
                    M = np.eye(N, dtype=complex)
                    for (mu, x, s) in P:
                        M = M @ (lk[mu, x] if s > 0 else np.linalg.inv(lk[mu, x]))
                    Ps.append(M)
                return Ps
            Ps = plaqs(gf)
            for (mu, x) in tree:
                worst = max(worst, np.abs(gf[mu, x] - np.eye(N)).max())
            for p in range(3):
                V = gf[nontree[p]]
                worst = max(worst, min(np.abs(Ps[p] - V).max(), np.abs(Ps[p] - np.linalg.inv(V)).max()))
            Y = [logm_u(P) for P in Ps]
            O1 = trc(*Y)
            gf2 = dict(gf)
            for b in nontree:
                gf2[b] = np.linalg.inv(gf[b])
            Y2 = [logm_u(P) for P in plaqs(gf2)]
            worst = max(worst, abs(trc(*Y2) + O1))
Eok = worst <= 1e-10
pr(f"E (8 star corner trees x 2 groups x 50 configs) worst deviation {worst:.2e} {'PASS' if Eok else 'FAIL'}")
pr(f"OVERALL: A1 {'PASS' if A1 else 'FAIL'}, A2 {'PASS' if A2 else 'FAIL'}, B {'PASS' if B else 'FAIL'}, "
   f"C {'PASS' if Cok else 'FAIL'}, D {'PASS' if Dok else 'FAIL'}, E {'PASS' if Eok else 'FAIL'}")
pr(f"wall {time.time() - t0:.1f} s; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20:.0f} MB")
