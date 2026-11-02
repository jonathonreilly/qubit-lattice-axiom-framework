"""f15 (lane C, session 12): FLOW.md §94 check f15.

Criteria: checks/f15_criteria.md (written before this script).
Part A: Lemma CL-V (W2): the explicit root-sector Wilson Hessian at Cartan backgrounds against the exact second derivative,
        the root-sector covariant gradient, and the classical continuum limit of the plane-wave vertices (spin coefficient 2).
Part B: (W4)-(W6) at U = 1: the S4' composite symbol, the level-transverse (T-split) symbol convergence, the longitudinal
        growth from d∘h, the straight-path control, and the LONG-n lower bound.
Run:  OMP_NUM_THREADS=1 ... nice -n 10 python3 f15_cl_vct.py > f15_out.txt
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys
import time
import itertools
from math import comb
import numpy as np
from scipy.linalg import expm, logm

sys.dont_write_bytecode = True
L = 3
SMOKE = os.environ.get("F15_SMOKE") == "1"
T0 = time.time()
VERD = []


def say(*a):
    print(*a, flush=True)


def verdict(name, ok, detail):
    VERD.append((name, bool(ok)))
    say(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")


# =============================================================== Part A: Lemma CL-V
S_SIGN = (1, 1, -1, -1)


def shift(arr, mu, twist=None):
    """arr[x + e_mu] on a (twisted) periodic lattice; arr has the 4 lattice axes first."""
    out = np.roll(arr, -1, axis=mu)
    if twist is not None and twist[mu] != 0.0:
        n = arr.shape[mu]
        idx = [slice(None)] * arr.ndim
        idx[mu] = slice(n - 1, n)
        out = out.astype(complex)
        out[tuple(idx)] *= np.exp(1j * twist[mu])
    return out


def unshift(arr, mu, twist=None):
    """arr[x - e_mu]."""
    out = np.roll(arr, 1, axis=mu)
    if twist is not None and twist[mu] != 0.0:
        idx = [slice(None)] * arr.ndim
        idx[mu] = slice(0, 1)
        out = out.astype(complex)
        out[tuple(idx)] *= np.exp(-1j * twist[mu])
    return out


def q_formula(phi, a, q, hb, twist=None, spin=True):
    """(W2) (b): sum_P cos(hb F)[cos(qF/2)|w|^2 - 2 sin(qF/2) sum_{a<b} s_a s_b Im(y_a conj y_b)].
    phi[x..., mu] complex (field twisted by `twist`), a[x..., mu] real (periodic, untwisted)."""
    tot = 0.0
    for mu in range(4):
        for nu in range(mu + 1, 4):
            a1 = a[..., mu]; a2 = shift(a[..., nu], mu); a3 = shift(a[..., mu], nu); a4 = a[..., nu]
            p1 = phi[..., mu]; p2 = shift(phi[..., nu], mu, twist); p3 = shift(phi[..., mu], nu, twist); p4 = phi[..., nu]
            F = a1 + a2 - a3 - a4
            y = [np.exp(-1j * q * a2) * p1, p2, p3, np.exp(-1j * q * a3) * p4]
            w = y[0] + y[1] - y[2] - y[3]
            J = 0.0
            for i in range(4):
                for j in range(i + 1, 4):
                    J = J + S_SIGN[i] * S_SIGN[j] * np.imag(y[i] * np.conj(y[j]))
            term = np.cos(q * F / 2) * np.abs(w) ** 2
            if spin:
                term = term - 2 * np.sin(q * F / 2) * J
            tot = tot + np.sum(np.cos(hb * F) * term)
    return float(np.real(tot))


def dstar(phi, a, q, twist=None):
    """(D_U^* phi)(x) = sum_mu [e^{i q a_{x,mu}} phi_{x,mu} - phi_{x-mu,mu}]."""
    out = 0.0
    for mu in range(4):
        out = out + np.exp(1j * q * a[..., mu]) * phi[..., mu] - unshift(phi[..., mu], mu, twist)
    return out


def q_total(phi, a, q, hb, twist=None, spin=True):
    return q_formula(phi, a, q, hb, twist, spin) + float(np.sum(np.abs(dstar(phi, a, q, twist)) ** 2))


def hess_exact(Bd, X):
    """d^2/dt^2 S_W(U e^{tX}) at t = 0, S_W = sum_P Re tr(1 - U_P) (beta = N). Bd[x..., mu, N] diagonal phases of B,
    X[x..., mu, N, N]. Product rule on the matrices."""
    N = Bd.shape[-1]
    tot = 0.0
    for mu in range(4):
        for nu in range(mu + 1, 4):
            def mat(d):
                return d[..., :, None] * np.eye(N)
            B1 = mat(Bd[..., mu, :]); B2 = mat(shift(Bd[..., nu, :], mu)); B3 = mat(shift(Bd[..., mu, :], nu)); B4 = mat(Bd[..., nu, :])
            X1 = X[..., mu, :, :]; X2 = shift(X[..., nu, :, :], mu); X3 = shift(X[..., mu, :, :], nu); X4 = X[..., nu, :, :]
            B3i = np.conj(B3); B4i = np.conj(B4)
            f0 = [B1, B2, B3i, B4i]
            f1 = [B1 @ X1, B2 @ X2, -X3 @ B3i, -X4 @ B4i]
            f2 = [B1 @ X1 @ X1, B2 @ X2 @ X2, X3 @ X3 @ B3i, X4 @ X4 @ B4i]
            acc = 0.0
            for a_ in range(4):
                fs = list(f0); fs[a_] = f2[a_]
                acc = acc + fs[0] @ fs[1] @ fs[2] @ fs[3]
            for a_ in range(4):
                for b_ in range(a_ + 1, 4):
                    fs = list(f0); fs[a_] = f1[a_]; fs[b_] = f1[b_]
                    acc = acc + 2 * (fs[0] @ fs[1] @ fs[2] @ fs[3])
            tot = tot - np.sum(np.real(np.trace(acc, axis1=-2, axis2=-1)))
    return float(tot)


def background(dims, eps, p, theta):
    x2 = np.arange(dims[1])
    a = np.zeros(tuple(dims) + (4,))
    a[..., 0] = (eps * np.cos(p * x2 + theta))[None, :, None, None]
    return a


def root_X(phi, N, i, j):
    X = np.zeros(phi.shape + (N, N), complex)
    X[..., i, j] = phi
    X[..., j, i] = -np.conj(phi)
    return X


def part_a():
    say("Part A (Lemma CL-V)")
    rng = np.random.default_rng(1512)
    dims = (3, 6, 2, 2)
    eps, p, theta = 0.7, 2 * np.pi / 6, 0.3
    a = background(dims, eps, p, theta)
    groups = {"SU(2)": (np.array([0.5, -0.5]), [(0, 1)]),
              "SU(3)": (np.array([0.7, -0.2, -0.5]), [(0, 1), (0, 2), (1, 2)])}
    ctrl = 0.0
    for gname, (h, roots) in groups.items():
        N = len(h)
        Bd = np.exp(1j * a[..., None] * h)                    # B_b = exp(a_b H_1), H_1 = i diag(h)
        worst = 0.0
        for (i, j) in roots:
            q = h[i] - h[j]; hb = (h[i] + h[j]) / 2
            for s in range(4):
                phi = rng.normal(size=dims + (4,)) + 1j * rng.normal(size=dims + (4,))
                He = hess_exact(Bd, root_X(phi, N, i, j))
                Qf = q_formula(phi, a, q, hb)
                Q0 = q_formula(phi, a, q, hb, spin=False)
                worst = max(worst, abs(He - 2 * Qf) / abs(He))
                ctrl = max(ctrl, abs(He - 2 * Q0) / abs(He))
            say(f"    {gname} root ({i + 1},{j + 1}): q = {q:.3f}, hbar = {hb:.3f}; last sample Hess = {He:.10e}, 2Q = {2 * Qf:.10e}")
        verdict(f"A1 explicit root Hessian = exact second derivative ({gname})", worst <= 1e-11, f"max rel = {worst:.2e} (<= 1e-11)")
        if gname == "SU(3)":
            cx = 0.0
            pairs = [((0, 1), (0, 2)), ((0, 1), (1, 2)), ((0, 2), (1, 2))]
            for (r1, r2) in pairs:
                p1 = rng.normal(size=dims + (4,)) + 1j * rng.normal(size=dims + (4,))
                p2 = rng.normal(size=dims + (4,)) + 1j * rng.normal(size=dims + (4,))
                Xa = root_X(p1, N, *r1); Xb = root_X(p2, N, *r2)
                ha, hb_, hab = hess_exact(Bd, Xa), hess_exact(Bd, Xb), hess_exact(Bd, Xa + Xb)
                cx = max(cx, abs(hab - ha - hb_) / (abs(ha) + abs(hb_)))
            for r1 in roots:
                p1 = rng.normal(size=dims + (4,)) + 1j * rng.normal(size=dims + (4,))
                Xa = root_X(p1, N, *r1)
                c = rng.normal(size=dims + (4, N)); c = c - c.mean(axis=-1, keepdims=True)
                Xc = np.zeros(dims + (4, N, N), complex)
                for kk in range(N):
                    Xc[..., kk, kk] = 1j * c[..., kk]
                ha, hc, hac = hess_exact(Bd, Xa), hess_exact(Bd, Xc), hess_exact(Bd, Xa + Xc)
                cx = max(cx, abs(hac - ha - hc) / (abs(ha) + abs(hc)))
            verdict("A1x no root/root' and root/Cartan cross terms (SU(3))", cx <= 1e-12, f"max rel = {cx:.2e} (<= 1e-12)")
            # A2: covariant gradient
            worst2 = 0.0
            for (i, j) in roots:
                q = h[i] - h[j]
                om = rng.normal(size=dims) + 1j * rng.normal(size=dims)
                for x in itertools.product(*[range(d) for d in dims]):
                    for mu in range(4):
                        xp = list(x); xp[mu] = (xp[mu] + 1) % dims[mu]; xp = tuple(xp)
                        U = np.diag(Bd[x + (mu,)])
                        w0 = np.zeros((N, N), complex); w0[i, j] = om[x]; w0[j, i] = -np.conj(om[x])
                        w1 = np.zeros((N, N), complex); w1[i, j] = om[xp]; w1[j, i] = -np.conj(om[xp])
                        def Xt(t):
                            return logm(np.conj(U).T @ expm(t * w0) @ U @ expm(-t * w1))
                        def Dh(hh):
                            return (Xt(hh) - Xt(-hh)) / (2 * hh)
                        R = (4 * Dh(5e-5) - Dh(1e-4)) / 3
                        pred = np.exp(-1j * q * a[x + (mu,)]) * om[x] - om[xp]
                        worst2 = max(worst2, abs(R[i, j] - pred) / abs(pred))
            verdict("A2 root covariant gradient D_U = derivative of the gauge orbit (SU(3))", worst2 <= 1e-8, f"max rel = {worst2:.2e} (<= 1e-8)")
    verdict("A1c control (spin term dropped) fails the A1 comparison", ctrl >= 1e-3, f"max rel = {ctrl:.3e} (>= 1e-3)")
    # A3: continuum limit on the Bloch chain
    dirs = [rng.normal(size=4) for _ in range(3)]
    dirs = [d / np.linalg.norm(d) for d in dirs]
    roots3 = [("SU(2)", 1.0, 0.0), ("SU(3)(1,2)", 0.9, 0.25)]
    Ns = (157, 314) if SMOKE else (157, 314, 628)
    e1max, e2max, e0max, e1cmin, decr = 0.0, 0.0, 0.0, np.inf, True
    for (rname, q, hb) in roots3:
        for di, kh in enumerate(dirs):
            E1 = {}
            for N2 in Ns:
                s = 2 * np.pi / N2
                k = s * kh
                tw = (k[0], (k[1] * N2) % (2 * np.pi), k[2], k[3])
                x2 = np.arange(N2)
                dims = (1, N2, 1, 1)
                def field(vec, kk2):
                    ph = np.zeros(dims + (4,), complex)
                    ph[0, :, 0, 0, :] = np.exp(1j * kk2 * x2)[:, None] * vec[None, :]
                    return ph
                def B(e, f1, f2):
                    aa = background(dims, e, s, 0.0)
                    return 0.25 * sum((1j) ** (-r) * q_total(f1 + (1j) ** r * f2, aa, q, hb, tw) for r in range(4))
                I4 = np.eye(4)
                Vp = np.zeros((4, 4), complex); O2 = np.zeros((4, 4), complex); O0 = np.zeros((4, 4), complex)
                de1, de2 = 1e-5, 1e-3
                for mu in range(4):
                    for nu in range(4):
                        fo = field(I4[mu], k[1] + s); fi = field(I4[nu], k[1])
                        Vp[mu, nu] = 2 * (B(de1, fo, fi) - B(-de1, fo, fi)) / (2 * de1) / N2
                        fo2 = field(I4[mu], k[1])
                        b0 = B(0.0, fo2, fi)
                        O0[mu, nu] = b0 / N2
                        O2[mu, nu] = (B(de2, fo2, fi) + B(-de2, fo2, fi) - 2 * b0) / (2 * de2 ** 2) / N2
                lam = np.sum(4 * np.sin(k / 2) ** 2)
                e0max = max(e0max, np.max(np.abs(O0 - lam * I4)))
                Vc = 2 * q * kh[0] * I4; Vc[0, 1] -= 2 * q; Vc[1, 0] += 2 * q
                Vcc = 2 * q * kh[0] * I4; Vcc[0, 1] -= 1 * q; Vcc[1, 0] += 1 * q
                e1 = np.linalg.norm(Vp / s - Vc) / np.linalg.norm(Vc)
                e1c = np.linalg.norm(Vp / s - Vcc) / np.linalg.norm(Vcc)
                e2 = np.linalg.norm(O2 - (q * q / 2) * I4) / np.linalg.norm((q * q / 2) * I4)
                E1[N2] = e1
                say(f"    {rname} khat#{di} N_2 = {N2} (s = {s:.5f}): E1 = {e1:.4e}, E1(spin 1) = {e1c:.4e}, E2 = {e2:.4e}")
            nmax = Ns[-1]
            e1max = max(e1max, E1[nmax])
            decr = decr and (E1[nmax] <= 0.7 * E1[Ns[-2]])
            e2max = max(e2max, e2)
            e1cmin = min(e1cmin, e1c)
    verdict("A3 O_1 leading part = O^c (spin coefficient 2): E1 at the finest s, decreasing", e1max <= 0.03 and decr,
            f"max E1 = {e1max:.3e} (<= 0.03), E1(finest) <= 0.7 E1(previous) for all: {decr}")
    verdict("A3 O_2 degree-0 part = q^2/2 (diamagnetic)", e2max <= 0.03, f"max E2 = {e2max:.3e} (<= 0.03)")
    verdict("A3 O_0 = lambda(k) 1 (sanity)", e0max <= 1e-12, f"max abs = {e0max:.2e} (<= 1e-12)")
    verdict("A3c control (spin coefficient 1) fails", e1cmin >= 0.2, f"min E1 = {e1cmin:.3e} (>= 0.2)")


# =============================================================== Part B: S4' symbols at U = 1
def Dr(r, th):
    th = np.asarray(th, complex)
    if r == 1:
        return np.ones_like(th)
    s = np.sin(th / 2)
    return np.sin(r * th / 2) / (r * s)


def Sr(r, th):
    th = np.asarray(th, complex)
    if r == 1:
        return np.ones_like(th)
    return (np.exp(1j * r * th) - 1) / (np.exp(1j * th) - 1)


def h1(th):
    return (Dr(L, th) - 1) / (np.exp(1j * th) - 1)


def onestep_closed(k):
    """(W5) (a) one-step symbol M_L(k) (4x4), centring phase dropped (c_X = 0)."""
    k = np.asarray(k, float)
    D = [Dr(L, x) for x in k]
    PD = np.prod(D)
    M = np.zeros((4, 4), complex)
    for nu in range(4):
        oth = [D[b] for b in range(4) if b != nu]
        a_nu = 0.25 * (1 + sum(oth) / 3 + (oth[0] * oth[1] + oth[0] * oth[2] + oth[1] * oth[2]) / 3 + oth[0] * oth[1] * oth[2])
        hnu = h1(k[nu]) * a_nu
        for mu in range(4):
            M[mu, nu] = (Sr(L, k[mu]) * PD if mu == nu else 0.0) - (np.exp(1j * L * k[mu]) - 1) * hnu
    return M


def onestep_contours(k):
    """Q_root by direct S4' contour sums (abelian, plane-wave input e^{ik.x} in component nu0)."""
    k = np.asarray(k, float)
    r = (L - 1) // 2
    ys = list(itertools.product(range(-r, r + 1), repeat=4))
    perms = list(itertools.permutations(range(4)))
    M = np.zeros((4, 4), complex)

    def path(start, end, sig, nu0):
        pos = list(start); tot = 0.0
        for al in sig:
            cur, tgt = pos[al], end[al]
            if tgt > cur:
                rng_ = range(cur, tgt); sgn = 1.0
            else:
                rng_ = range(tgt, cur); sgn = -1.0
            if al == nu0:
                for t in rng_:
                    pp = list(pos); pp[al] = t
                    tot += sgn * np.exp(1j * np.dot(k, pp))
            pos[al] = tgt
        return tot

    for mu in range(4):
        cX = [0, 0, 0, 0]; cY = [0, 0, 0, 0]; cY[mu] = L
        for nu0 in range(4):
            acc = 0.0
            for sig in perms:
                for y in ys:
                    yY = list(y); yY[mu] += L
                    leg = 0.0
                    if nu0 == mu:
                        for j in range(L):
                            pp = list(y); pp[mu] += j
                            leg += np.exp(1j * np.dot(k, pp))
                    acc += path(cX, y, sig, nu0) + leg - path(cY, yY, sig, nu0)
            M[mu, nu0] = acc / (len(perms) * len(ys))
    return M


def h_terms(n, nu):
    """h^(n)_nu as a list of (coef, [f_alpha(theta) callables]) product terms (functions of the fine momentum per direction)."""
    terms = []
    others = [b for b in range(4) if b != nu]
    for j in range(n):
        r = L ** j
        for s_ in range(4):
            for T in itertools.combinations(others, s_):
                coef = 0.25 / comb(3, s_)
                fs = []
                for al in range(4):
                    if al == nu:
                        fs.append(lambda th, r=r: h1(r * th) * Sr(r, th) * Dr(r, th))
                    elif al in T:
                        fs.append(lambda th, r=r: Dr(L * r, th))
                    else:
                        fs.append(lambda th, r=r: Dr(r, th))
                terms.append((coef, fs))
    return terms


def qstr_term(n, mu):
    l = L ** n
    return [(1.0, [(lambda th, l=l: Sr(l, th) * Dr(l, th)) if al == mu else (lambda th, l=l: Dr(l, th)) for al in range(4)])]


def eval_terms(terms, k):
    return sum(c * np.prod([f(k[al]) for al, f in enumerate(fs)]) for c, fs in terms)


def composite_closed(n, k):
    l = L ** n
    k = np.asarray(k, float)
    M = np.zeros((4, 4), complex)
    for nu in range(4):
        hn = eval_terms(h_terms(n, nu), k)
        for mu in range(4):
            M[mu, nu] = (eval_terms(qstr_term(n, mu), k) if mu == nu else 0.0) - (np.exp(1j * l * k[mu]) - 1) * hn
    return M


class Fibre:
    """1D alias arrays and proper-time weights for the level fibre of K at level n."""

    def __init__(self, n, K, h_u=0.3, u_min=-36.0):
        self.l = L ** n
        m = np.arange(self.l)
        self.k = [(K[al] + 2 * np.pi * m) / self.l for al in range(4)]
        self.lam = [4 * np.sin(x / 2) ** 2 for x in self.k]
        lmin = sum(x.min() for x in self.lam)
        u = np.arange(u_min, np.log(80.0 / lmin) + h_u, h_u)
        self.T = np.exp(u); self.h_u = h_u
        self.E = [np.exp(-self.T[None, :] * x[:, None]) for x in self.lam]       # (m, T)

    def pair_sum(self, terms, power):
        """l^-4 sum_m |sum_t c_t prod_al f_t,al(k_al)|^2 / lambda^power (power 1 or 2)."""
        cs = np.array([c for c, _ in terms], complex)
        prodG = None
        for al in range(4):
            F = np.array([fs[al](self.k[al]) for _, fs in terms])                # (t, m)
            G = np.einsum("tm,sm,mT->tsT", F, np.conj(F), self.E[al], optimize=True)
            prodG = G if prodG is None else prodG * G
        wT = self.h_u * self.T ** power
        val = np.einsum("t,s,tsT,T->", cs, np.conj(cs), prodG, wT)
        return float(np.real(val)) / float(self.l) ** 4


def Vvec(K):
    Dl = np.exp(1j * np.asarray(K)) - 1
    return Dl / np.linalg.norm(Dl), np.linalg.norm(Dl)


def xblk(n, K, h_u=0.3, sp=False):
    F = Fibre(n, K, h_u)
    out = []
    for mu in range(4):
        terms = qstr_term(n, mu)
        if sp:
            l = L ** n
            terms = [(1.0, [(lambda th, l=l: Sr(l, th)) if al == mu else (lambda th: np.ones_like(th, complex)) for al in range(4)])]
        out.append(F.pair_sum(terms, 1))
    return np.array(out)


def Tsplit(x, K):
    V, _ = Vvec(K)
    P = np.eye(4) - np.outer(V, np.conj(V))
    return P @ np.diag(x) @ P


def long_L(n, K):
    """<V, N_n[M] V> for the actual composite S4' symbol."""
    V, nD = Vvec(K)
    F = Fibre(n, K)
    tot = 0.0
    for nu in range(4):
        terms = [(np.conj(V[nu]) * c, fs) for c, fs in qstr_term(n, nu)] + [(-nD * c, fs) for c, fs in h_terms(n, nu)]
        tot += F.pair_sum(terms, 1)
    one = [(1.0, [lambda th: np.ones_like(th, complex)] * 4)]
    g2 = F.pair_sum(one, 2)
    return tot - nD ** 2 * g2


def s_i(i, K):
    r = L ** i
    m = np.arange(r)
    kap = [(K[al] + 2 * np.pi * m) / r for al in range(4)]
    out = []
    for mu in range(4):
        val = 1.0
        for al in range(4):
            f = Dr(r, kap[al]) * (Sr(r, kap[al]) if al == mu else 1.0)
            val *= np.sum(np.abs(f) ** 2)
        out.append(val / float(r) ** 4)
    return np.array(out)


def c_long(n, K):
    """sum_{i<n} L^-4i sum_m |V^dag M^(i)(kappa_m)|^2 (Pi = 1)."""
    V, nD = Vvec(K)
    tot = 1.0
    for i in range(1, n):
        r = L ** i
        m = np.arange(r)
        kap = [(K[al] + 2 * np.pi * m) / r for al in range(4)]
        for nu in range(4):
            terms = [(np.conj(V[nu]) * c, fs) for c, fs in qstr_term(i, nu)] + [(-nD * c, fs) for c, fs in h_terms(i, nu)]
            cs = np.array([c for c, _ in terms], complex)
            prodG = None
            for al in range(4):
                Fm = np.array([fs[al](kap[al]) for _, fs in terms])
                G = Fm @ np.conj(Fm).T
                prodG = G if prodG is None else prodG * G
            tot += float(np.real(cs @ prodG @ np.conj(cs))) / float(r) ** 4
    return tot


def part_b():
    say("Part B (S4' symbols at U = 1; T-split)")
    rng = np.random.default_rng(1215)
    # B0
    e1 = 0.0
    for _ in range(3):
        k = rng.uniform(-np.pi, np.pi, 4)
        e1 = max(e1, np.max(np.abs(onestep_closed(k) - onestep_contours(k))))
    verdict("B0(i) one-step closed form = S4' contour sums", e1 <= 1e-12, f"max abs = {e1:.2e} (<= 1e-12)")
    e2 = 0.0; e3 = 0.0
    for n in range(1, 5):
        for _ in range(3):
            k = rng.uniform(-np.pi, np.pi, 4)
            Mc = composite_closed(n, k)
            if n >= 2:
                Mp = np.eye(4, dtype=complex)
                for j in range(n):
                    Mp = onestep_closed(L ** j * k) @ Mp
                e2 = max(e2, np.max(np.abs(Mc - Mp)) / np.max(np.abs(Mp)))
            sk = np.exp(1j * k) - 1
            e3 = max(e3, np.max(np.abs(Mc @ sk - (np.exp(1j * L ** n * k) - 1))))
    verdict("B0(ii) composite closed form = product of one-step symbols (n = 2..4)", e2 <= 1e-11, f"max rel = {e2:.2e} (<= 1e-11)")
    verdict("B0(iii) covariance M^(n) s = Dhat_l (n = 1..4)", e3 <= 1e-11, f"max abs = {e3:.2e} (<= 1e-11)")
    Ks = {"K_a": (0.7, 0.4, 0.3, 0.2), "K_b": (2.1, -1.3, 0.9, 2.8), "K_c": (0.06, 0.04, 0.03, 0.02)}
    nmax = 4 if SMOKE else 6
    stepchg = 0.0
    sratio_ok = True
    for name, K in Ks.items():
        K = np.array(K)
        T = {}; Tsp = {}
        for n in range(1, nmax + 1):
            x = xblk(n, K)
            x2 = xblk(n, K, h_u=0.15)
            stepchg = max(stepchg, np.max(np.abs(x - x2) / np.abs(x2)))
            T[n] = Tsplit(x, K)
            if name != "K_c":
                Tsp[n] = Tsplit(xblk(n, K, sp=True), K)
            say(f"    {name} n = {n}: x^blk = " + ", ".join(f"{v:.12e}" for v in x))
        D = {n: np.linalg.norm(T[n] - T[n - 1]) for n in range(2, nmax + 1)}
        say(f"    {name}: Delta_n = " + ", ".join(f"{D[n]:.4e}" for n in range(2, nmax + 1))
            + "; ratios " + ", ".join(f"{D[n] / D[n - 1]:.4f}" for n in range(3, nmax + 1)))
        for n in (nmax - 1, nmax):
            rr = D[n] / D[n - 1]
            verdict(f"B1 T-split geometric convergence n = {n} ({name})", 0.07 <= rr <= 0.16, f"Delta_n/Delta_(n-1) = {rr:.4f} (in [0.07, 0.16])")
        sv = [np.linalg.norm(s_i(i, K)) for i in range(0, 6)]
        say(f"    {name}: ||s_i|| (i = 0..5) = " + ", ".join(f"{v:.4e}" for v in sv))
        for i in (4, 5):
            sratio_ok = sratio_ok and (0.07 <= sv[i] / sv[i - 1] <= 0.16)
        if name != "K_c":
            Dsp = {n: np.linalg.norm(Tsp[n] - Tsp[n - 1]) for n in range(2, nmax + 1)}
            rs = [Dsp[n] / Dsp[n - 1] for n in (nmax - 1, nmax)]
            say(f"    {name}: straight path Delta^sp_n = " + ", ".join(f"{Dsp[n]:.4e}" for n in range(2, nmax + 1)))
            verdict(f"B3 control: straight-path T-split symbol diverges ({name})", min(rs) >= 2, f"ratios {rs[0]:.3f}, {rs[1]:.3f} (>= 2)")
            Lv = {n: long_L(n, K) for n in range(1, nmax + 1)}
            dl = {n: Lv[n] - Lv[n - 1] for n in range(2, nmax + 1)}
            _, nD = Vvec(K)
            say(f"    {name}: <V, N_n V> = " + ", ".join(f"{Lv[n]:.10e}" for n in range(1, nmax + 1)))
            say(f"    {name}: increments delta_n/|Dhat|^2 = " + ", ".join(f"{dl[n] / nD ** 2:.6e}" for n in range(2, nmax + 1)))
            a5, a6 = dl[nmax - 1], dl[nmax]
            verdict(f"B2 (W6) longitudinal growth from d.h: constant positive increments ({name})",
                    a5 > 0 and a6 > 0 and abs(a6 / a5 - 1) <= 0.10, f"delta = {a5:.4e}, {a6:.4e}, ratio {a6 / a5:.4f}")
    verdict("B1 C-part s_i geometric (i = 4, 5; all K)", sratio_ok, "ratios in [0.07, 0.16]")
    verdict("B1 step control h_u 0.3 vs 0.15", stepchg <= 1e-9, f"max rel = {stepchg:.1e} (<= 1e-9)")
    okb4 = True
    for name, K in Ks.items():
        K = np.array(K)
        _, nD = Vvec(K)
        cs = [c_long(n, K) for n in range(1, nmax + 1)]
        bd = [1 + (n - 1) * nD ** 2 / 8 for n in range(1, nmax + 1)]
        okb4 = okb4 and all(c >= b - 1e-12 for c, b in zip(cs, bd))
        say(f"    {name}: kappa<V, C_n V> = " + ", ".join(f"{c:.8f}" for c in cs) + "; bound " + ", ".join(f"{b:.8f}" for b in bd))
        say(f"    {name}: increments = " + ", ".join(f"{cs[n] - cs[n - 1]:.6e}" for n in range(1, nmax)))
    verdict("B4 LONG-n lower bound kappa<V, C_n V> >= 1 + (n-1)|Dhat|^2/8", okb4, "all n, all K")


if __name__ == "__main__":
    say(f"f15 start; SMOKE = {SMOKE}")
    part_a()
    say(f"  (Part A time {time.time() - T0:.1f} s)")
    part_b()
    npass = sum(1 for _, ok in VERD if ok)
    say(f"SUMMARY: {npass}/{len(VERD)} verdict lines PASS; FAIL: " + (", ".join(n for n, ok in VERD if not ok) or "none"))
    say(f"total time {time.time() - T0:.1f} s")
