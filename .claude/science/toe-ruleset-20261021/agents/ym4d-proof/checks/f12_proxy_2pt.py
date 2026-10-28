"""f12 (lane C, session 9): the scalar proxy in two-point form at U = 1 (FLOW.md §64 (S1)), n = 1..4.

Criteria: checks/f12_criteria.md (written before this script).
h_n(p) = [eps^2] G_S,n at U_{x,1} = exp(i eps cos(p x_2 + theta)) is computed as
  h_n(p) = (1/4) avg_K l^{-4} [T(K, p) - I(K, p)]
(traces over the alias fibre of the extended matrix [[Delta, M^dag], [M, -C]] at U = 1; 𝔐_0^{-1} = (Lambda^{-1} + 0) - alpha xi xi^dag).
Fibre sums over the l^4 aliases use 1/(lam^a lam'^b) = int dT e^{-T lam_perp} g_ab(T; lam_2, lam'_2) (directions 1, 3, 4
factorise; direction 2 carries the momentum transfer p and is done per alias in closed form).
c^S_n = lim_{p->0} h_n(p) / (2 sin^2(p/2)).
Run:  OMP_NUM_THREADS=1 ... nice -n 10 python3 f12_proxy_2pt.py > f12_out.txt
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")
import itertools
import time
import numpy as np

L = 3
S = 4.0
CG = 1.0 / (96 * np.pi ** 2)
SMOKE = os.environ.get("F12_SMOKE") == "1"
T0 = time.time()
VERD = []


def say(*a):
    print(*a, flush=True)


def verdict(name, ok, detail):
    VERD.append((name, ok))
    say(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")


def lam1(q):
    return 2.0 - 2.0 * np.cos(q)


# ------------------------------------------------------------------ block-digit form factors (1D, fine momentum q)
def dl(q, r):
    return (1.0 + 2.0 * np.cos(q * L ** r)) / 3.0


def prod_d(q, n, skip=(), qshift=None, shift_set=()):
    """prod_{r<n, r not in skip} dl(q_r, r), with q replaced by qshift for r in shift_set."""
    out = np.ones_like(q)
    for r in range(n):
        if r in skip:
            continue
        out = out * dl(qshift if (qshift is not None and r in shift_set) else q, r)
    return out


def D1(q, n):
    return prod_d(q, n)


def G1(q, n, k):          # i * F1_k: i * L^k (2i/3) sin(q L^k) prod_{r != k} dl = -(2/3) L^k sin(q L^k) prod
    return -(2.0 / 3.0) * L ** k * np.sin(q * L ** k) * prod_d(q, n, skip=(k,))


def F1sq(q, n, k):
    return L ** (2 * k) * (2.0 / 3.0) * np.cos(q * L ** k) * prod_d(q, n, skip=(k,))


def F1pair(q, n, k, k2):
    return -(4.0 / 9.0) * L ** (k + k2) * np.sin(q * L ** k) * np.sin(q * L ** k2) * prod_d(q, n, skip=(k, k2))


def F2(q, p, n, i):       # prod_{r<i} dl(q) prod_{r>=i} dl(q + p)
    return prod_d(q, n, qshift=q + p, shift_set=tuple(range(i, n)))


def H2(q, p, n, k):
    return 0.5 * (F2(q, p, n, k + 1) + F2(q, p, n, k))


def F2cos(q, p, n, i, i2):
    a, b = min(i, i2), max(i, i2)
    st = tuple(range(a, b))
    return 0.5 * (prod_d(q, n, qshift=q + p, shift_set=st) + prod_d(q, n, qshift=q - p, shift_set=st))


def c_level(n):
    return sum(L ** (-4 * (n - j)) / (S * L ** (2 * j)) for j in range(1, n + 1))


def c2_vertex(n, p):
    return -sum(L ** (-4 * (n - j)) / (S * L ** (2 * j)) * sum((4.0 / 9.0) * L ** (2 * k) * (1 - np.cos(p * L ** k))
                                                               for k in range(j, n)) for j in range(1, n + 1))


# ------------------------------------------------------------------ proper-time kernels for direction 2
def E0(z):
    z = np.asarray(z, float)
    out = np.empty_like(z)
    sm = z < 1e-4
    zs = z[sm]
    out[sm] = 1 - zs / 2 + zs ** 2 / 6 - zs ** 3 / 24
    zb = z[~sm]
    out[~sm] = -np.expm1(-zb) / zb
    return out


def E1(z):
    z = np.asarray(z, float)
    out = np.empty_like(z)
    sm = z < 0.05
    zs = z[sm]
    acc = np.zeros_like(zs); fact = 1.0
    for k in range(12):
        if k > 0:
            fact *= k
        acc += (-zs) ** k / (fact * (k + 2))
    out[sm] = acc
    zb = z[~sm]
    out[~sm] = (1 - np.exp(-zb) * (1 + zb)) / zb ** 2
    return out


def gkind(kind, T, A, B):
    """g_ab(T; A, B) with int_0^inf dT e^{-T x} g_ab = 1/((A + x)^a (B + x)^b)."""
    if kind == "10":
        return np.exp(-T * A)
    if kind == "20":
        return T * np.exp(-T * A)
    if kind == "01":
        return np.exp(-T * B)
    mn = np.minimum(A, B)
    z = T * np.abs(A - B)
    if kind == "11":
        return T * np.exp(-T * mn) * E0(z)
    e0, e1 = E0(z), E1(z)
    if kind == "21":   # weight t on A
        return T ** 2 * np.where(A >= B, np.exp(-T * B) * e1, np.exp(-T * A) * (e0 - e1))
    if kind == "12":   # weight on B
        return T ** 2 * np.where(B >= A, np.exp(-T * A) * e1, np.exp(-T * B) * (e0 - e1))
    raise ValueError(kind)


# ------------------------------------------------------------------ the fibre machinery
class Fibre:
    def __init__(self, n, Ks, p, h_u=0.3, u_min=-36.0):
        """Ks: list of four 1D arrays of level momenta (per direction)."""
        self.n = n; self.l = L ** n; self.p = p
        l = self.l
        m = np.arange(l)
        self.q = [((K[:, None] + 2 * np.pi * m[None, :]) / l) for K in Ks]
        lams = [lam1(q) for q in self.q]
        lam2p = lam1(self.q[1] + p)
        lmin = sum(x.min() for x in lams)
        lmin = min(lmin, lmin - lams[1].min() + lam2p.min())
        u_max = np.log(80.0 / max(lmin, 1e-300))
        u = np.arange(u_min, u_max + h_u, h_u)
        self.T = np.exp(u); self.w = h_u * self.T
        T = self.T[None, :, None]
        self.E = [np.exp(-T * lams[mu][:, None, :]) if mu != 1 else None for mu in range(4)]
        A = lams[1][:, None, :]; B = lam2p[:, None, :]
        self.G2 = {k: gkind(k, T, A, B) for k in ("10", "20", "01", "11", "21", "12")}
        self.cache = {}

    def fsum(self, terms, kind):
        """sum over fibre of sum_terms coef * prod_mu g_mu, times 1/(lam^a lam'^b) (kind 'ab')."""
        tot = 0.0
        for coef, g in terms:
            Y = []
            for mu in range(4):
                tab = self.G2[kind] if mu == 1 else self.E[mu]
                Y.append(np.einsum("km,ktm->kt", g[mu], tab))
            X12 = (Y[0][:, None, :] * Y[1][None, :, :] * self.w).reshape(-1, len(self.T))
            X34 = (Y[2][:, None, :] * Y[3][None, :, :]).reshape(-1, len(self.T))
            R = (X12 @ X34.T).reshape(Y[0].shape[0], Y[1].shape[0], Y[2].shape[0], Y[3].shape[0])
            tot = tot + coef * R
        return tot


def times(a, b):
    return [(ca * cb, [ga[mu] * gb[mu] for mu in range(4)]) for ca, ga in a for cb, gb in b]


def integrand(n, Ks, p, h_u=0.3):
    """(T - I)(K, p) * l^{-4} on the K grid (array) for the proxy at level n."""
    F = Fibre(n, Ks, p, h_u=h_u)
    l = F.l; q1, q2, q3, q4 = F.q
    one = [np.ones_like(x) for x in F.q]
    d1, d2, d3, d4 = D1(q1, n), D1(q2, n), D1(q3, n), D1(q4, n)
    d2p = D1(q2 + p, n)
    l4 = float(l) ** -4
    Dv = [(1.0, [d1, d2, d3, d4])]                      # D(k)
    Dpv = [(1.0, [d1, d2p, d3, d4])]                    # D(k + p e_2)
    sig = [(1.0, [2 * np.sin(q1), one[1], one[2], one[3]])]
    Wv = [(1.0, [2 * np.cos(q1), one[1], one[2], one[3]])]
    u = [(1.0, [G1(q1, n, k), H2(q2, p, n, k), d3, d4]) for k in range(n)]
    um = [(1.0, [G1(q1, n, k), H2(q2 + p, -p, n, k), d3, d4]) for k in range(n)]
    m2 = [(-1.0, [F1sq(q1, n, k), d2, d3, d4]) for k in range(n)]
    for k in range(n):
        for k2 in range(k + 1, n):
            f2 = sum(F2cos(q2, p, n, i, i2) for i in (k, k + 1) for i2 in (k2, k2 + 1))
            m2.append((-0.5, [F1pair(q1, n, k, k2), f2, d3, d4]))
    sc = lambda t, c: [(c * a, g) for a, g in t]
    Cn = c_level(n); c2 = c2_vertex(n, p)
    G = F.fsum(sc(times(Dv, Dv), l4), "10")
    Gp = F.fsum(sc(times(Dpv, Dpv), l4), "01")
    sW = F.fsum(Wv, "10")
    svW = F.fsum(sc(times(times(Dv, Dv), Wv), l4), "20")
    svo = F.fsum(sc(times(Dv, m2), l4), "10")
    smu = F.fsum(sc(times(u, u), l4), "10")
    smuv = F.fsum(sc(times(u, Dv), l4), "10")
    smum = F.fsum(sc(times(um, um), l4), "01")
    svpm = F.fsum(sc(times(Dpv, um), l4), "01")
    Sff = F.fsum(times(sig, sig), "11")
    s12 = F.fsum(sc(times(times(sig, sig), times(Dpv, Dpv)), l4), "12")
    s21 = F.fsum(sc(times(times(sig, sig), times(Dv, Dv)), l4), "21")
    sspm = F.fsum(sc(times(times(sig, Dpv), u), l4), "11")
    ssvm = F.fsum(sc(times(times(sig, Dv), um), l4), "11")
    sxi = F.fsum(sc(times(times(Dpv, sig), Dv), l4), "11")
    al = 1.0 / (Cn + G); alp = 1.0 / (Cn + Gp)
    Tad = sW - al * (svW - 2 * svo - c2)
    wLw = s12 - 2 * sspm + smu
    zLz = s21 - 2 * ssvm + smum
    Xi = sxi - svpm - smuv
    I = Sff - alp * wLw - al * zLz + al * alp * Xi ** 2
    return l4 * (Tad - I)


def shifted(N):
    return 2 * np.pi * (np.arange(N) + 0.5) / N


_ZERO = {}


def h_of_p(n, NK, p, h_u=0.3, sub=True):
    Ks = [shifted(NK)] * 4
    J = integrand(n, Ks, p, h_u)
    if sub:
        key = (n, NK, h_u)
        if key not in _ZERO:
            _ZERO[key] = integrand(n, Ks, 0.0, h_u)
        J = J - _ZERO[key]
    return 0.25 * J.mean()


# ------------------------------------------------------------------ Part I: implementation checks
def brute_torus(Tdims, p, theta, eps):
    """n = 1 direct 4D torus N = 3*Tdims, antiperiodic BC, plane wave U_{x,1} = exp(i eps cos(p x_2 + theta)), 24 orders."""
    n = 1; l = 3; h = 1
    dims = [l * t for t in Tdims]
    V = int(np.prod(dims))
    sites = list(itertools.product(*[range(d) for d in dims]))
    idx = {x: i for i, x in enumerate(sites)}
    def link(x, mu):
        ph = np.exp(1j * eps * np.cos(p * x[1] + theta)) if mu == 0 else 1.0 + 0j
        if x[mu] == dims[mu] - 1:
            ph = -ph
        return ph
    H = np.zeros((V, V), complex)
    for x in sites:
        i = idx[x]
        H[i, i] += 8.0
        for mu in range(4):
            xp = list(x); xp[mu] = (xp[mu] + 1) % dims[mu]
            j = idx[tuple(xp)]
            H[i, j] += -link(x, mu); H[j, i] += -np.conj(link(x, mu))
    cd = Tdims
    levs = list(itertools.product(*[range(t) for t in cd]))
    M = np.zeros((len(levs), V), complex)
    orders = list(itertools.permutations(range(4)))
    for a, X in enumerate(levs):
        c = [l * X[mu] + h for mu in range(4)]
        for jv in itertools.product(range(l), repeat=4):
            y = [l * X[mu] + jv[mu] for mu in range(4)]
            tot = 0.0
            for o in orders:
                z = list(c); ph = 1.0 + 0j
                for mu in o:
                    while z[mu] != y[mu]:
                        if y[mu] > z[mu]:
                            ph *= link(tuple(z), mu); z[mu] += 1
                        else:
                            z[mu] -= 1; ph *= np.conj(link(tuple(z), mu))
                tot += ph
            M[a, idx[tuple(y)]] = l ** -4 * tot / 24
    kap = S * L ** 2
    K = H + kap * (M.conj().T @ M)
    sg, ld = np.linalg.slogdet(K)
    return (ld + len(levs) * np.log(1.0 / kap)) / V


def part_i():
    say("Part I (implementation)")
    Td = (2, 4, 2, 1)
    p = 2 * np.pi / (3 * Td[1]); th = 0.37
    epss = [0.02, 0.04, 0.06, 0.08]
    g0 = brute_torus(Td, p, th, 0.0)
    y = np.array([brute_torus(Td, p, th, e) - g0 for e in epss]); e = np.array(epss)
    A = np.vstack([e ** 2, e ** 4, e ** 6]).T
    hb = np.linalg.lstsq(A, y, rcond=None)[0][0]
    Ks = [shifted(t) for t in Td]
    hm = 0.25 * integrand(1, Ks, p).mean()
    verdict("I1 brute force (n = 1 torus (6,12,6,3), 24 orders, eps-fit)", abs(hm - hb) <= 1e-7 * abs(hb),
            f"h direct = {hb:.12e}, momentum formula = {hm:.12e}, rel diff = {abs(hm - hb) / abs(hb):.1e}")
    # reported: vertex form factors at n = 2 against the real-space block kernel (24 orders), random momenta
    rng = np.random.default_rng(12)
    n = 2; l = 9; h = 4; p = 0.21
    offs = list(itertools.product(range(-h, h + 1), repeat=4))
    orders = list(itertools.permutations(range(4)))
    digits = lambda j: [((j + 4) // 3 ** 0) % 3 - 1, ((j + 4) // 3) % 3 - 1]  # balanced base-3 digits of j in [-4, 4]
    def centres(jj):
        out = []
        for lev in range(n + 1):
            out.append([sum(digits(jj[mu])[r] * L ** r for r in range(lev, n)) for mu in range(4)])
        return out
    # geometry (24 orders, no reduction assumed): per offset t, level k, order o: leg-1 length and the x_2 of the leg
    Dlt = np.zeros((len(offs), n)); pos = np.zeros((len(offs), n, len(orders)))
    for t, jj in enumerate(offs):
        cs = centres(jj)
        for k in range(n):
            cfr, cto = cs[k + 1], cs[k]
            Dlt[t, k] = cto[0] - cfr[0]
            for io, o in enumerate(orders):
                pos2 = cfr[1]
                for mu in o:
                    if mu == 1:
                        pos2 = cto[1]
                    if mu == 0:
                        pos[t, k, io] = pos2
                        break
    def kernel(eps, th):
        a = eps * np.cos(p * pos + th)
        w = np.mean(np.exp(1j * Dlt[:, :, None] * a), 2)
        return np.prod(w, 1)
    de = 1e-3; ths = 2 * np.pi * np.arange(8) / 8
    k1p = np.array([(kernel(de, t) - kernel(-de, t)) / (2 * de) for t in ths])
    k1p2 = np.array([(kernel(2 * de, t) - kernel(-2 * de, t)) / (4 * de) for t in ths])
    k1 = (4 * k1p - k1p2) / 3
    up_ker = 2 * np.mean(np.exp(-1j * ths)[:, None] * k1, 0)     # coefficient of (eps/2) e^{i theta}
    k0 = kernel(0.0, 0.0)
    k2a = np.array([(kernel(de, t) + kernel(-de, t) - 2 * k0) / (2 * de ** 2) for t in ths])
    k2b = np.array([(kernel(2 * de, t) + kernel(-2 * de, t) - 2 * k0) / (8 * de ** 2) for t in ths])
    m2_ker = 4 * np.mean((4 * k2a - k2b) / 3, 0)                 # coefficient of eps^2/4, zero theta-mode
    J = np.array(offs, float)
    worst_u = worst_m = 0.0
    for _ in range(4):
        kv = rng.uniform(-np.pi, np.pi, 4)
        ph = np.exp(1j * J @ kv) / l ** 4
        u_rs = np.sum(ph * up_ker); m_rs = np.sum(ph * m2_ker)
        q1, q2, q3, q4 = [np.array([x]) for x in kv]
        u_cf = sum(G1(q1, n, k) * H2(q2, p, n, k) for k in range(n)) * D1(q3, n) * D1(q4, n)
        m_cf = -sum(F1sq(q1, n, k) for k in range(n)) * D1(q2, n) * D1(q3, n) * D1(q4, n)
        for k in range(n):
            for k2 in range(k + 1, n):
                f2 = sum(F2cos(q2, p, n, i, i2) for i in (k, k + 1) for i2 in (k2, k2 + 1))
                m_cf = m_cf - 0.5 * F1pair(q1, n, k, k2) * f2 * D1(q3, n) * D1(q4, n)
        worst_u = max(worst_u, abs(u_rs - u_cf[0]) / max(abs(u_cf[0]), 1e-12))
        worst_m = max(worst_m, abs(m_rs - m_cf[0]) / max(abs(m_cf[0]), 1e-12))
    say(f"    [reported] n = 2 vertex form factors vs real-space block kernel (24 orders, 4 random k): "
        f"max rel |u| diff = {worst_u:.1e}, |m2| diff = {worst_m:.1e} (finite-difference eps = 1e-3, Richardson)")


# ------------------------------------------------------------------ Part P: c^S_n
def cS(n, NK, Ps, h_u=0.3, verbose=True):
    l = L ** n
    vals = []
    for P in Ps:
        p = P / l
        hv = h_of_p(n, NK, p, h_u)
        vals.append(hv / (2 * np.sin(p / 2) ** 2))
    vals = np.array(vals); x = np.array(Ps) ** 2
    A = np.vstack([np.ones_like(x), x, x ** 2, x ** 3]).T
    c_all = np.linalg.lstsq(A, vals, rcond=None)[0][0]
    c_drop = np.linalg.solve(A[:-1], vals[:-1])[0]
    if verbose:
        say(f"    n = {n}, N_K = {NK}, h_u = {h_u}: c(P) = " + ", ".join(f"{v:.10e}" for v in vals))
    return c_all, c_drop


def part_p():
    say("Part P (scalar proxy at U = 1, two-point form; L = 3, s = 4)")
    Ps = [0.1, 0.2, 0.3, 0.4, 0.5]
    NKs = (8, 12) if SMOKE else (16, 20)
    ns = (1, 2) if SMOKE else (1, 2, 3, 4)
    res = {}
    for n in ns:
        t1 = time.time()
        l = L ** n
        # Ward (I2): unsubtracted p = 0 value
        b0 = 0.25 * integrand(n, [shifted(NKs[1])] * 4, 0.0).mean()
        ca, cd = cS(n, NKs[0], Ps)
        cb, cd2 = cS(n, NKs[1], Ps)
        ch, _ = cS(n, NKs[1], Ps, h_u=0.15, verbose=False)
        conv = abs(ca - cb) <= 1e-9 and abs(cb - ch) <= 1e-10
        verdict(f"I3 convergence (n = {n})", conv, f"|c(N_K={NKs[0]}) - c(N_K={NKs[1]})| = {abs(ca - cb):.1e}, |c(h_u) - c(h_u/2)| = {abs(cb - ch):.1e}")
        verdict(f"I4 p-fit stability (n = {n})", abs(cb - cd2) <= 1e-9, f"|c(all P) - c(without P = {Ps[-1]})| = {abs(cb - cd2):.1e}")
        pmin = Ps[0] / l
        if n <= 2:
            verdict(f"I2 Ward (n = {n})", abs(b0) <= 1e-3 * abs(cb) * pmin ** 2 / 2,
                    f"unsubtracted p = 0 value b0 = {b0:.2e} vs 1e-3 |c| p_min^2/2 = {1e-3 * abs(cb) * pmin ** 2 / 2:.2e}")
        else:
            say(f"    [reported] Ward (n = {n}): b0 = {b0:.2e} (1e-3 |c| p_min^2/2 = {1e-3 * abs(cb) * pmin ** 2 / 2:.2e})")
        rho = cb - 2 * CG * np.log(l)
        res[n] = (cb, rho, conv)
        say(f"    n = {n}: c^S_n = {cb:.10e}, rho_n = {rho:.10e}  ({time.time() - t1:.0f} s)")
    if 1 in res:
        verdict("P-a n = 1 (f11 7.123425e-4)", abs(res[1][0] - 7.123425e-4) <= 1e-8, f"|diff| = {abs(res[1][0] - 7.123425e-4):.1e}")
    if 2 in res:
        verdict("P-a n = 2 (f11 2.885494e-3)", abs(res[2][0] - 2.885494e-3) <= 1e-8, f"|diff| = {abs(res[2][0] - 2.885494e-3):.1e}")
    if 3 in res:
        d32 = abs(res[3][1] - res[2][1])
        verdict("P-b |rho_3 - rho_2| <= 4.9e-5", d32 <= 4.9e-5, f"rho_3 - rho_2 = {res[3][1] - res[2][1]:+.4e}")
    ks = sorted(res)
    cprev = 0.0
    for k in ks:
        phi = res[k][0] - cprev
        say(f"    phi_{k - 1} = c^S_{k} - c^S_{k - 1} = {phi:.10e}; phi - 2 c_g log 3 = {phi - 2 * CG * np.log(L):+.6e}")
        cprev = res[k][0]
    for a, b in zip(ks[:-1], ks[1:]):
        say(f"    rho_{b} - rho_{a} = {res[b][1] - res[a][1]:+.6e}")
    incs = [res[b][1] - res[a][1] for a, b in zip(ks[:-1], ks[1:])]
    for i in range(len(incs) - 1):
        say(f"    increment ratio {i + 2}->{i + 3} / {i + 1}->{i + 2} = {incs[i + 1] / incs[i]:.4f}")
    say("    vector rho^V_n: not attempted in f12")


if __name__ == "__main__":
    say(f"f12 (lane C, session 9) start {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} UTC; SMOKE = {SMOKE}")
    part_i()
    part_p()
    npass = sum(ok for _, ok in VERD)
    say(f"Summary: {npass}/{len(VERD)} verdict lines PASS; total {time.time() - T0:.0f} s")
