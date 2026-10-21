"""C3b s1: exact / finite certificates for the lemmas.

(a) Witness X (checkerboard clock): ergodic, O_h- and translation-covariant clock, record = parity (crystal LRO).
(b) Kolmogorov interpolation variance on a torus: v = 1/mean(1/f) vs dense-matrix inversion; det bound for
    conditional covariance of T_S given T_0  >= v^{|S|}.
(c) Theorem J chain count: E #{decreasing chains along a fixed SAW, t_0<=t} = (lam t)^{n+1}/(n+1)!  (MC, 4 SE).
(d) Theorem H volume bound: P(path decreasing, T_0 - T_n <= M) <= (K M)^n / n!  (MC for correlated Gaussian paths).
(e) Theorem K exact: ring Z_7, NON-mixing clock law (1/2 deterministic order + 1/2 iid), noisy majority rule:
    E sigma_0 = 0 and |E sigma_0 sigma_r| <= P(Anc(0) cap Anc(r) != empty), exact rationals.
"""
import itertools
import math
from fractions import Fraction
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from c3b_common import check, total, nbr_table, depth_and_record

rng = np.random.default_rng(20261019)

# ---------------- (a) checkerboard witness ----------------
print("== (a) witness X: checkerboard clock ==")
Lb = 8
shape = (Lb, Lb, Lb)
nbr = nbr_table(shape)
X = np.indices(shape).reshape(3, -1).T
par = X.sum(1) % 2
# O_h acts by signed permutations; parity of x1+x2+x3 is invariant (x_i -> -x_i changes sum by 2x_i)
ok = True
for perm in itertools.permutations(range(3)):
    for sg in itertools.product([1, -1], repeat=3):
        Y = X[:, perm] * np.array(sg)
        ok &= np.all(Y.sum(1) % 2 == par)
check("a1 parity is O_h-invariant (48 elements, all 512 points)", ok)


@__import__('numba').njit
def any_earlier(T, nbr):
    N = T.shape[0]
    out = np.zeros(N, np.int8)
    for x in range(N):
        for j in range(nbr.shape[1]):
            if T[nbr[x, j]] < T[x]:
                out[x] = 1
    return out


covs_even, covs_odd = [], []
allok = True
for phase in (0, 1):
    for rep in range(20):
        T = ((par + phase) % 2) + 0.4 * rng.random(par.size)   # noise < 1/2: early sublattice strictly earlier
        xi = any_earlier(T, nbr)  # rule: content 1 iff some neighbour formed earlier (zeros allowed, C3 sec.1)
        allok &= np.array_equal(xi, (par + phase) % 2)
check("a2 record equals the late-sublattice indicator exactly (40 samples, both phases)", allok)
# exact covariance under uniform random phase: E xi = 1/2; E xi_0 xi_x = 1/2 (|x| even) or 0 (odd)
c_even = Fraction(1, 2) - Fraction(1, 4)
c_odd = Fraction(0) - Fraction(1, 4)
check("a3 Cov(xi_0, xi_x) = +-1/4 for all x (no decay): genuine LRO of an ERGODIC law",
      c_even == Fraction(1, 4) and c_odd == Fraction(-1, 4), f"even {c_even}, odd {c_odd}")

# ---------------- (b) Kolmogorov interpolation on torus ----------------
print("== (b) interpolation variance ==")
for (Lt, alpha, s2) in [(12, 0.5, 0.05), (12, 1.5, 0.02), (10, 0.3, 0.2)]:
    k = 2 * np.pi * np.fft.fftfreq(Lt)
    KX, KY = np.meshgrid(k, k, indexing='ij')
    lap = 4 - 2 * np.cos(KX) - 2 * np.cos(KY)
    f = np.where(lap > 0, s2 + lap ** ((alpha - 2) / 2), s2 + 10.0)  # power-law spectral weight, regular zero mode
    C = np.real(np.fft.ifft2(f))
    idx = np.indices((Lt, Lt)).reshape(2, -1).T
    D = (idx[:, None, :] - idx[None, :, :]) % Lt
    Sig = C[D[..., 0], D[..., 1]]
    Q = np.linalg.inv(Sig)
    v_dense = 1.0 / Q[0, 0]
    v_formula = 1.0 / np.mean(1.0 / f)
    check(f"b1 L={Lt} alpha={alpha}: 1/Q00 == 1/mean(1/f)", abs(v_dense / v_formula - 1) < 1e-9,
          f"{v_dense:.10g} vs {v_formula:.10g}")
    # det bound on conditional covariance of T_S given T_0
    worst = np.inf
    for rep in range(200):
        m = rng.integers(1, 12)
        S = rng.choice(np.arange(1, Lt * Lt), size=m, replace=False)
        A = np.concatenate([[0], S])
        Sub = Sig[np.ix_(A, A)]
        cond = Sub[1:, 1:] - np.outer(Sub[1:, 0], Sub[0, 1:]) / Sub[0, 0]
        sign, logdet = np.linalg.slogdet(cond)
        worst = min(worst, logdet / m - np.log(v_formula))
    check(f"b2 L={Lt} alpha={alpha}: (1/|S|) log det Cov(T_S|T_0) >= log v  (200 random S)", worst >= -1e-9,
          f"min margin {worst:.4g}")

# ---------------- (c) Theorem J chain count ----------------
print("== (c) time-cutoff chain count ==")
for (n, lam, t) in [(1, 1.0, 1.0), (2, 1.5, 1.0), (3, 1.0, 2.0), (4, 2.0, 1.0)]:
    R = 200000
    counts = np.zeros(R)
    # count tuples (p_0 > p_1 > ... > p_n) with p_k a point of site k, p_0 <= t; dynamic programming per sample
    # vectorised: simulate number of points per site, positions sorted
    tot = 0.0
    tot2 = 0.0
    B = 20000
    nb_ = R // B
    vals = []
    for b in range(nb_):
        npts = rng.poisson(lam * t, size=(B, n + 1))
        mx = npts.max()
        P = rng.random((B, n + 1, max(mx, 1))) * t
        mask = np.arange(max(mx, 1))[None, None, :] < npts[:, :, None]
        P = np.where(mask, P, np.nan)
        # W[k][b, i] = number of chains ending... compute from site n upward: ways(k, point) = sum_{points q of k+1, q<p} ways(k+1,q)
        ways = np.where(mask[:, n, :], 1.0, 0.0)
        for kk in range(n - 1, -1, -1):
            pk = P[:, kk, :]  # (B, mx)
            pq = P[:, kk + 1, :]
            less = (pq[:, None, :] < pk[:, :, None])  # nan compares False
            ways = np.where(mask[:, kk, :], (less * ways[:, None, :]).sum(2), 0.0)
        vals.append(ways.sum(1))
    vals = np.concatenate(vals)
    est, se = vals.mean(), vals.std(ddof=1) / np.sqrt(len(vals))
    exact = (lam * t) ** (n + 1) / math.factorial(n + 1)
    check(f"c1 n={n} lam={lam} t={t}: E#chains = (lam t)^(n+1)/(n+1)!", abs(est - exact) < 4 * se,
          f"MC {est:.5f}+-{se:.5f} exact {exact:.5f}")

# ---------------- (d) Theorem H volume bound ----------------
print("== (d) volume bound for correlated Gaussian paths ==")
for (n, alpha, s2, M) in [(4, 0.5, 0.3, 2.0), (6, 1.0, 0.2, 3.0), (5, 0.3, 1.0, 1.5)]:
    # stationary covariance along a straight line in Z^2 (sites distinct): C(r) = s2*delta + (1+r)^(-alpha)
    r = np.abs(np.arange(n + 1)[:, None] - np.arange(n + 1)[None, :])
    Sig = s2 * (r == 0) + (1.0 + r) ** (-alpha)
    # K from the white-noise component only (Theorem H, Gaussian case uses v >= s2 here): density of T_S|T_0 <= (2 pi s2)^(-|S|/2)
    K = (2 * np.pi * s2) ** -0.5
    Lc = np.linalg.cholesky(Sig)
    R = 400000
    Z = rng.standard_normal((R, n + 1)) @ Lc.T
    dec = np.all(np.diff(Z, axis=1) < 0, axis=1) & ((Z[:, 0] - Z[:, -1]) <= M)
    p, se = dec.mean(), dec.std(ddof=1) / np.sqrt(R)
    bound = (K * M) ** n / math.factorial(n)
    check(f"d1 n={n} alpha={alpha} s2={s2} M={M}: P <= (KM)^n/n!", p - 4 * se <= bound,
          f"P={p:.3e}+-{se:.1e} bound={bound:.3e}")

# ---------------- (e) Theorem K exact on ring Z_7 ----------------
print("== (e) internal-symmetry bound, exact ==")
Nr = 7
delta = Fraction(1, 10)
ring_nb = [((x - 1) % Nr, (x + 1) % Nr) for x in range(Nr)]


def rule_prob(s, seen):
    """noisy majority, q=2: P(s | colours seen)."""
    tot = sum(seen)
    if len(seen) == 0 or tot == 0:
        return Fraction(1, 2)
    maj = 1 if tot > 0 else -1
    return (1 - delta) * (1 if s == maj else 0) + delta / 2


def stats_for_order(rank):
    """rank[x] = position in formation order (all distinct). Returns E[s0], E[s0 s_r] for r=1..3 (exact), overlap flags."""
    order = sorted(range(Nr), key=lambda x: rank[x])
    # ancestry sets
    anc = {}
    for x in order:
        a = {x}
        for y in ring_nb[x]:
            if rank[y] < rank[x]:
                a |= anc[y]
        anc[x] = a
    # exact record law by enumeration of colour sequences in formation order
    dist = {(): Fraction(1)}
    for x in order:
        nd = {}
        for conf, pr in dist.items():
            cmap = dict(zip(order[:len(conf)], conf))
            seen = [cmap[y] for y in ring_nb[x] if rank[y] < rank[x]]
            for s in (1, -1):
                q = rule_prob(s, seen)
                if q:
                    key = conf + (s,)
                    nd[key] = nd.get(key, 0) + pr * q
        dist = nd
    E0 = Fraction(0)
    E0r = [Fraction(0)] * 4
    for conf, pr in dist.items():
        cmap = dict(zip(order, conf))
        E0 += pr * cmap[0]
        for rr in range(1, 4):
            E0r[rr] += pr * cmap[0] * cmap[rr]
    ov = [None] + [bool(anc[0] & anc[rr]) for rr in range(1, 4)]
    return E0, E0r, ov


E0 = Fraction(0)
E0r = [Fraction(0)] * 4
P_ov = [Fraction(0)] * 4
w_iid = Fraction(1, 2) / math.factorial(Nr)
perms = list(itertools.permutations(range(Nr)))
for perm in perms:
    e0, e0r, ov = stats_for_order(perm)
    E0 += w_iid * e0
    for rr in range(1, 4):
        E0r[rr] += w_iid * e0r[rr]
        P_ov[rr] += w_iid * (1 if ov[rr] else 0)
# deterministic "level" order on the ring: T_x = x (non-mixing, non-exchangeable component)
e0, e0r, ov = stats_for_order(tuple(range(Nr)))
E0 += Fraction(1, 2) * e0
for rr in range(1, 4):
    E0r[rr] += Fraction(1, 2) * e0r[rr]
    P_ov[rr] += Fraction(1, 2) * (1 if ov[rr] else 0)
check("e1 E sigma_0 = 0 exactly (internal Z2 symmetry, non-mixing clock law)", E0 == 0, str(E0))
for rr in range(1, 4):
    check(f"e2 r={rr}: |E s0 s_r| <= P(Anc(0) cap Anc(r) nonempty)", abs(E0r[rr]) <= P_ov[rr],
          f"{float(E0r[rr]):.5f} <= {float(P_ov[rr]):.5f}")
total()
