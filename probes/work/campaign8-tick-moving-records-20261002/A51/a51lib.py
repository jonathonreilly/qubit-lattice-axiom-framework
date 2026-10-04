"""A51 library (supplied toys; nothing adopted).  Long-range inverse search in the Klein-dual frame.
Extends A49 (a49lib: four-spin star/plaquette terms, mf_state, product_state, releig) with dual-frame Heisenberg class
sums O_c = sum_{unordered torus pairs {i,j} in class c} s_i.s_j for EVERY displacement class with folded components
<= L/2.  Estimator per pair: X0_ij = z_i z_j + (1 - z_i z_j) (R1_i R1_j - G_ij G_ji), G = Pa Q (full N x N)."""
import sys, time, itertools, numpy as np
D51 = __file__.rsplit('/', 1)[0]
sys.path.insert(0, D51.rsplit('/', 1)[0] + "/A49")
from a49lib import *          # noqa (cube, SIG, Vx, FD, mf_state, product_state, four_basis, Tables, estimators, releig, kR, hs)


def fold(v, L):
    v = np.mod(v, L)
    return np.minimum(v, L - v)


def class_list(L):
    """All classes (a<=b<=c, components 0..L/2, not all 0), ordered by |d|^2 then lexicographically."""
    h = L // 2
    ks = [k for k in itertools.combinations_with_replacement(range(h + 1), 3) if k != (0, 0, 0)]
    return sorted(ks, key=lambda k: (sum(c * c for c in k), k))


def class_matrix(cl, L):
    """K[i,j] = class index of x_j - x_i (folded, sorted); diagonal = ncls (discarded). Also m_c per site."""
    X = np.array(cl.sites); N = len(X); ks = class_list(L); lab = {k: n for n, k in enumerate(ks)}
    D = fold(X[None, :, :] - X[:, None, :], L); D.sort(axis=2)
    code = (D[:, :, 0] * (L + 1) + D[:, :, 1]) * (L + 1) + D[:, :, 2]
    lut = np.full((L + 1) ** 3, len(ks), int)
    for k, n in lab.items():
        lut[(k[0] * (L + 1) + k[1]) * (L + 1) + k[2]] = n
    K = lut[code]; np.fill_diagonal(K, len(ks))
    m = np.bincount(K[0], minlength=len(ks) + 1)[:len(ks)]
    return ks, K, m


def class_estimators(Phi, Q, s, Kflat, ncls, rows0):
    """E_c(s) = (O_c psi)(s)/psi(s) for all classes (complex)."""
    Pa = Phi[rows0 + 1 - s]
    Gm = Pa @ Q
    R1 = np.diag(Gm).copy(); z = 1. - 2. * s
    zz = np.outer(z, z)
    X0 = zz + (1. - zz) * (np.outer(R1, R1) - Gm * Gm.T)
    X0 = X0.ravel()
    re = np.bincount(Kflat, weights=X0.real, minlength=ncls + 1)[:ncls]
    im = np.bincount(Kflat, weights=X0.imag, minlength=ncls + 1)[:ncls]
    return 0.5 * (re + 1j * im)


def class_gram(m):
    """Per-site HS norm^2 of O_c: 3 m_c / 2 (classes mutually orthogonal)."""
    return np.diag(1.5 * np.asarray(m, float))


def four_ops():
    F4 = four_basis()
    sold = [o[3] for o in F4]
    G4 = np.array([[hs(a, b) for b in sold] for a in sold])
    return F4, G4


def soldered_class_op(k):
    """Soldered-frame image of sum over the class-k displacements of s_0.s_d (canonical dict), for covariance checks."""
    op = {}
    seen = set()
    for perm in itertools.permutations(k):
        for sg in itertools.product((1, -1), repeat=3):
            d = tuple(int(sg[i] * perm[i]) for i in range(3))
            if d == (0, 0, 0): continue
            key = max(d, tuple(-c for c in d))
            if key in seen: continue
            seen.add(key)
            for b in range(3):
                eps = (-1) ** ((d[(b + 1) % 3] + d[(b + 2) % 3]) % 2)
                add(op, canon([((0, 0, 0), b), (d, b)]), float(eps))
    return clean(op)


def state(cl, spec):
    """Dual-frame orbitals Phi (2N x N) and (mode, conserve).
    lp:<lam2>           projected parton (A44/A49), exact singlet at lam2 = 0
    neez:<m> / colz:<m> projected weakly ordered Neel / collinear (pi,pi,0), field along dual z (S^z = 0)
    sdw:<m>:<n1>,<n2>,<n3>  pi-flux + collinear field m cos(Q.x) s^z, Q = 2 pi n / L
    fs0                 dual-frame 0-flux projected Fermi sea (singlet control; twist slightly off APBC)
    pol / cs            product-state controls (full sampling)"""
    N = cl.N; X = np.array(cl.sites); kind = spec.split(":")[0]
    if kind == "lp":
        Phi, gap = mf_state(cl, lam2=float(spec.split(":")[1])); return Phi, gap, "singlet", True
    if kind in ("neez", "colz"):
        Phi, gap = mf_state(cl, m=float(spec.split(":")[1]), pattern=("neel" if kind == "neez" else "collinear"))
        return Phi, gap, "singlet", True
    if kind == "sdw":
        _, m, n = spec.split(":"); m = float(m); L = round(N ** (1 / 3)); qv = 2 * np.pi * np.array([float(c) for c in n.split(",")]) / L
        h = _parton_h(cl)
        f = np.cos(X @ qv)
        for i in range(N):
            h[2 * i:2 * i + 2, 2 * i:2 * i + 2] += m * f[i] * SIG[2]
        ev, W = np.linalg.eigh(h); W = W[:, :N].copy()
        nup = float((np.abs(W[0::2]) ** 2).sum()); assert abs(nup - N / 2) < 1e-6, f"filled up-weight {nup} != N/2"
        return W, ev[N] - ev[N - 1], "singlet", True
    if kind == "fs0":
        tw = np.array([np.pi + 0.13, np.pi + 0.29, np.pi + 0.41]); h = np.zeros((N, N), complex)
        for (i, j, a, n) in cl.bonds:
            ph = np.exp(1j * (tw @ n)); h[i, j] += -ph; h[j, i] += -np.conj(ph)
        ev, W = np.linalg.eigh(h); W = W[:, :N // 2]
        Phi = np.zeros((2 * N, N), complex); Phi[0::2, :N // 2] = W; Phi[1::2, N // 2:] = W
        return Phi, ev[N // 2] - ev[N // 2 - 1], "singlet", True
    if kind == "vbs":                                # columnar dimer singlets on (x, x+e1), x1 even (singlet competitor)
        X = np.array(cl.sites); Phi = np.zeros((2 * N, N), complex); o = 0
        for i, x in enumerate(cl.sites):
            if x[0] % 2: continue
            j = cl.idx[tuple(cl.canon(np.array(x) + np.array([1, 0, 0]))[0])]
            Phi[2 * i, o] = Phi[2 * j, o] = 2 ** -0.5; Phi[2 * i + 1, o + 1] = Phi[2 * j + 1, o + 1] = 2 ** -0.5; o += 2
        return Phi, np.nan, "singlet", True
    if kind == "cs":
        return product_state([(-1) ** int(sum(x)) * np.ones(3) / np.sqrt(3) for x in cl.sites]), np.nan, "full", False
    if kind == "pol":
        nh = np.array([1., 2., 3.]) / np.sqrt(14.)
        return product_state([np.array([kR(x, b) * nh[b] for b in range(3)]) for x in cl.sites]), np.nan, "full", False
    raise ValueError(spec)


def _parton_h(cl):
    """Dual-frame pi-flux mean-field matrix (soldered NN hop i s^a, APBC, rotated by V), as in a49 mf_state (m = 0)."""
    N = cl.N; tw = np.array((np.pi,) * 3); h = np.zeros((2 * N, 2 * N), complex)
    for (i, j, a, n) in cl.bonds:
        u = 1j * SIG[a] * np.exp(1j * (tw @ n))
        h[2 * i:2 * i + 2, 2 * j:2 * j + 2] += u; h[2 * j:2 * j + 2, 2 * i:2 * i + 2] += u.conj().T
    V = np.zeros((2 * N, 2 * N), complex)
    for i, s in enumerate(cl.sites):
        V[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Vx(s)
    return V.conj().T @ h @ V


def vmc51(cl, Phi, Kflat, ncls, T4, nsweep, ntherm, seed, tlimit, mode, conserve, every=1, s0=None):
    """A44/A46/A49 move set.  Returns samples (n, ncls + n4) complex: class estimators then four-spin estimators."""
    N = cl.N; rng = np.random.default_rng(seed); rows0 = 2 * np.arange(N)
    for _ in range(2000):
        s = rng.permutation(np.r_[np.zeros(N // 2, int), np.ones(N - N // 2, int)])
        M = Phi[rows0 + s]
        if np.linalg.cond(M) < 1e10: break
    else:
        if s0 is None: raise RuntimeError("no non-singular start")
        s = np.array(s0, int); M = Phi[rows0 + s]
    Q = np.linalg.inv(M); bi, bj = cl.bi, cl.bj
    acc = [0, 0, 0, 0]; out = []; drift = 0.; t0 = time.time()
    for sw in range(ntherm + nsweep):
        for _ in range(N):
            if (not conserve) and rng.random() < 0.5:
                i = rng.integers(N); v = Phi[2 * i + 1 - s[i]]; R = v @ Q[:, i]; acc[1] += 1
                if rng.random() < abs(R) ** 2:
                    u = v @ Q; u[i] -= 1.; Q -= np.outer(Q[:, i], u) / R; s[i] = 1 - s[i]; acc[0] += 1
            else:
                b = rng.integers(len(bi)); i, j = bi[b], bj[b]
                if conserve and s[i] == s[j]:
                    acc[3] += 1; continue
                vi, vj = Phi[2 * i + 1 - s[i]], Phi[2 * j + 1 - s[j]]; Qc = Q[:, [i, j]]
                Rm = np.array([[vi @ Qc[:, 0], vi @ Qc[:, 1]], [vj @ Qc[:, 0], vj @ Qc[:, 1]]])
                R = Rm[0, 0] * Rm[1, 1] - Rm[0, 1] * Rm[1, 0]; acc[3] += 1
                if rng.random() < abs(R) ** 2:
                    U = np.vstack([vi @ Q, vj @ Q]); U[0, i] -= 1.; U[1, j] -= 1.
                    Q -= Qc @ np.linalg.solve(Rm, U); s[i], s[j] = 1 - s[i], 1 - s[j]; acc[2] += 1
        if sw % 10 == 0 or sw == ntherm + nsweep - 1:
            Qf = np.linalg.inv(Phi[rows0 + s]); drift = max(drift, np.abs(Q - Qf).max() / np.abs(Qf).max()); Q = Qf
        if time.time() - t0 > tlimit:                    # time cap also during thermalization (A51 fix)
            break
        if sw < ntherm or (sw - ntherm) % every:
            continue
        Ec = class_estimators(Phi, Q, s, Kflat, ncls, rows0)
        if T4 is not None:
            e4 = estimators(T4, Phi, Q, s, mode)
            e4 = e4[0] if mode == "singlet" else e4
            Ec = np.concatenate([Ec, e4])
        out.append(Ec)
        if time.time() - t0 > tlimit:
            break
    return np.array(out), dict(acc=acc, drift=drift, secs=time.time() - t0)
