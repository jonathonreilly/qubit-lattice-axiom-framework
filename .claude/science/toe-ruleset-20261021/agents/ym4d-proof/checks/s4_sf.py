#!/usr/bin/env python3
"""s4 (lane F, session 4): Lemma HALO, Lemma SH, CE-Q-col / RT-1 constants, SN-1, Lemma TILT, Proposition RES.
Criteria: checks/s4_criteria.md (written before this script)."""
import math, sys, time
import numpy as np
from scipy import ndimage

t0 = time.time()
rng = np.random.default_rng(20261028)
RES = []


def rec(name, ok, info):
    ok = bool(ok)
    RES.append((name, ok))
    print(f"{name}: {'PASS' if ok else 'FAIL'} | {info}")


# ---------------------------------------------------------------- A. Lemma HALO
def chess_dist(S):
    """l-infinity torus distance from every cell to the nearest True cell of S."""
    d = S.ndim
    T = S.shape[0]
    tiled = np.tile(S, (3,) * d)
    dist = ndimage.distance_transform_cdt(~tiled, metric='chessboard')
    sl = tuple(slice(T, 2 * T) for _ in range(d))
    return dist[sl]


def dilate(S, r):
    if r <= 0:
        return S.copy()
    return ndimage.maximum_filter(S.astype(np.uint8), size=2 * r + 1, mode='wrap').astype(bool)


def box_dist(c1, r1, c2, r2, T):
    diff = np.abs(np.array(c1) - np.array(c2))
    diff = np.minimum(diff, T - diff)
    return int(np.max(np.maximum(0, diff - (r1 + r2))))


def connected(S):
    idx = np.argwhere(S)
    if len(idx) == 0:
        return True
    cur = np.zeros_like(S)
    cur[tuple(idx[0])] = True
    while True:
        nxt = dilate(cur, 1) & S
        if nxt.sum() == cur.sum():
            break
        cur = nxt
    return cur.sum() == S.sum()


def halo_trial(d, T, nQ):
    q = rng.integers(0, T, size=(nQ, d))
    ell = rng.integers(1, 5, size=nQ)
    # classes by union-find on halos (boxes radius ell-1), linking at box distance <= 7
    par = list(range(nQ))

    def find(i):
        while par[i] != i:
            par[i] = par[par[i]]
            i = par[i]
        return i
    for i in range(nQ):
        for j in range(i + 1, nQ):
            if box_dist(q[i], ell[i] - 1, q[j], ell[j] - 1, T) <= 7:
                par[find(i)] = find(j)
    cls = np.array([find(i) for i in range(nQ)])
    labels = sorted(set(cls))
    R = np.zeros((T,) * d, bool)
    Rb = {}
    for a in labels:
        Ra = np.zeros((T,) * d, bool)
        for i in np.where(cls == a)[0]:
            one = np.zeros((T,) * d, bool)
            one[tuple(q[i])] = True
            Ra |= dilate(one, ell[i] - 1)
        Rb[a] = Ra
        R |= Ra
    stats = dict(v1=0, v2=0, v3=0, n3=0, v4=0, v5=0, n2l2=0, ctrl=0, n2=0)
    distR = chess_dist(R)
    # A1: small single cubes c (dist(c,R) >= 2); n(y, X) = dist(q, c) - 1 >= ell
    small = distR >= 2
    if small.any():
        dsmall = chess_dist(small)
        for i in range(nQ):
            if dsmall[tuple(q[i])] - 1 < ell[i]:
                stats['v1'] += 1
    count_in_W = np.zeros((T,) * d, np.int32)
    for a in labels:
        Ra = Rb[a]
        da = chess_dist(Ra)
        Wa = dilate(Ra, 2)
        Ua = dilate(Ra, 7)
        Uap = dilate(Ra, 8)
        Qa = np.where(cls == a)[0]
        # A4
        if Wa.sum() > sum((2 * ell[i] + 3) ** d for i in Qa):
            stats['v4'] += 1
        if Ua.sum() > sum((2 * ell[i] + 13) ** d for i in Qa):
            stats['v4'] += 1
        if Uap.sum() > sum((2 * ell[i] + 15) ** d for i in Qa):
            stats['v4'] += 1
        if not connected(Ua):
            stats['v4'] += 1
        # box-in-W count (A5)
        box = Wa.copy()
        for sh in np.ndindex(*(2,) * d):
            box &= np.roll(Wa, shift=tuple(-s for s in sh), axis=tuple(range(d)))
        count_in_W += box
        for i in np.where(cls != a)[0]:
            D = da[tuple(q[i])]
            if D >= 9:  # q(y) not in U_a^+
                n = D - 8
                stats['n2'] += 1
                if ell[i] >= 2:
                    stats['n2l2'] += 1
                if n < max(1, ell[i] - 1) or n < ell[i] / 2:
                    stats['v2'] += 1
                if n < ell[i]:
                    stats['ctrl'] += 1
            else:  # q(y) in U_a^+
                stats['n3'] += 1
                if D - 2 < ell[i] + 5:
                    stats['v3'] += 1
    # A5: boxes X (corner c, cubes c + {0,1}^d) with X^+ meeting R
    near = distR <= 1
    large = near.copy()
    for sh in np.ndindex(*(2,) * d):
        large |= np.roll(near, shift=tuple(-s for s in sh), axis=tuple(range(d)))
    stats['v5'] = int(np.sum(large & (count_in_W != 1)))
    return stats


tot = dict(v1=0, v2=0, v3=0, n3=0, v4=0, v5=0, n2l2=0, ctrl=0, n2=0)
for (d, T, nQ, ntr) in [(2, 64, 26, 40), (3, 36, 16, 30)]:
    for _ in range(ntr):
        s = halo_trial(d, T, nQ)
        for k in tot:
            tot[k] += s[k]
rec("A1 HALO(a) small X: n>=ell", tot['v1'] == 0, f"violations {tot['v1']}")
rec("A2 HALO(b) n>=max(1,ell-1)>=ell/2", tot['v2'] == 0, f"violations {tot['v2']} of {tot['n2']} pairs")
rec("A3 HALO(c) dist to W >= ell+5", tot['v3'] == 0 and tot['n3'] >= 1, f"violations {tot['v3']} of {tot['n3']} pairs")
rec("A4 HALO(d) sizes, U connected", tot['v4'] == 0, f"violations {tot['v4']}")
rec("A5 HALO(e) large X in exactly one W", tot['v5'] == 0, f"violations {tot['v5']}")
rec("A6 non-vacuity (A2 pairs with ell>=2 >= 50)", tot['n2l2'] >= 50, f"{tot['n2l2']}")
rec("A7 NEG CONTROL n>=ell violated", tot['ctrl'] >= 1, f"violations of the stronger claim: {tot['ctrl']}")

# ---------------------------------------------------------------- constants
L2 = math.log(2.0)
kap0 = 16 * math.log(12800.0)
logK0 = kap0 - math.log(6400.0)
logCK = math.log(32.0) + 1.0 + logK0
ap = math.log(2 * 624.0 ** 2)
kt0 = 16 * ap
logKt0 = kt0 - 2 * math.log(624.0)
logBt = math.log(625.0) + logCK + kt0 + logKt0
logC1t = math.log(2 * kt0) + logBt
w8 = sum((2 * n + 1) ** 4 * math.exp(-8 * n) for n in range(1, 200))
L = 3
mu = 4.83e-11


def muM_W3(kc):
    kp = kc + 16 * L2
    x = 1e5
    for _ in range(200):
        x = 2 * (5 * kp + 4 * math.log(x / mu) + 8)
    return x


# ---------------------------------------------------------------- B. Lemma SH
viol1 = viol2 = 0
maxratio = 0.0
nonvac_all = True
growth = False
for kc in [810.0, 1478.5, 2500.0, 10000.0]:
    khat = kc - kap0 - kt0 - 2
    x0 = muM_W3(kc)
    for muM in [x0, 2 * x0, 10 * x0]:
        JM = math.ceil(muM / (4 * L2))
        J = 3 * JM + 10
        j = np.arange(0, J + 1, dtype=np.float64)
        ellj = np.ceil(4 * (j + 1) * L2 / muM)
        for p in [2.0, 2.5, 5.0, 50.0]:
            for h0 in [0.0, 1.0]:
                lg = 2 * khat * (2 * ellj + 13) ** 4 + w8 * (2 * ellj + 15) ** 4 + 2 * h0 * (2 * ellj + 3) ** 4
                Lj = lg - lg[0]
                if not (ellj >= 2).any():
                    nonvac_all = False
                if Lj.max() > 0:
                    growth = True
                jj = j[1:]
                pos = Lj[1:] > 0
                if pos.any():
                    lhs = np.log(Lj[1:][pos])
                    rhs = jj[pos] * math.log(4) + np.log1p(-4.0 ** (-np.minimum(jj[pos], 1000))) + 2 * math.log(p) - math.log(32)
                    viol1 += int(np.sum(lhs > rhs))
                with np.errstate(over='ignore', invalid='ignore'):
                    e = np.exp(np.minimum(jj * math.log(4), 700.0))
                    expo = Lj[1:] - (e - 1) * p * p / 16
                ratio = 1.0 + float(np.sum(np.exp(np.maximum(expo, -745.0)) * (expo > -745.0)))
                maxratio = max(maxratio, ratio)
                if ratio > 2.0:
                    viol2 += 1
rec("B1 SH pointwise", viol1 == 0, f"violations {viol1}")
rec("B2 SH shell sum <= 2 Gamma_0 e^{-p^2/16}", viol2 == 0, f"violations {viol2}; max ratio {maxratio:.6f}")
rec("B3 SH non-vacuity (ell>=2 reached; growth present)", nonvac_all and growth, f"all grid points reach ell>=2: {nonvac_all}; growth: {growth}")

# ---------------------------------------------------------------- C. arithmetic
rec("C1 kt0, log Bt, log C1t", 217.04 <= kt0 <= 217.05 and 574.6 <= logBt <= 574.8 and 580.7 <= logC1t <= 580.8,
    f"kt0={kt0:.4f} logBt={logBt:.3f} logC1t={logC1t:.3f} kap0={kap0:.4f} w8={w8:.5f}")
kstar = (6 * kap0 + 6 * kt0 + 10 + 64 * L2 + 1296 * w8) / 2
rec("C2 CE-col rate threshold", 1149.9 <= kstar <= 1150.0, f"kappa_c^* = {kstar:.3f}")
base = math.log(16 * L ** 4) + logK0 + 32 * L2 + logC1t + 1296 * w8


def f_disp(kc, extra_r=0.0, fac=0.0):
    r = kc - kap0 - 2 * kt0 - 3 - extra_r
    kap = r - 16 * L2
    return base + fac + r - (kap * (L - 1) - kap0 * L - 1)


def f_next(kc, extra_r=0.0, fac=0.0):
    r = kc - kap0 - 2 * kt0 - 3 - extra_r
    kap = r - 16 * L2
    kin = kc + 16 * L2 + 1296 * w8
    return base + fac + r - ((kap - kap0) * L - 1 - kin)


def root(f, **kw):
    a, b = 0.0, 1e5
    for _ in range(200):
        m = (a + b) / 2
        if f(m, **kw) > 0:
            a = m
        else:
            b = m
    return b


th3 = root(f_disp)
rec("C3 CE-col norm threshold (SF displayed form)", 1850 <= th3 <= 1858 and 703 <= f_disp(1149.92) <= 704.2,
    f"threshold {th3:.2f}; log ratio at 1149.92 = {f_disp(1149.92):.2f}")
th4 = root(f_next)
r4 = th4 - kap0 - 2 * kt0 - 3 - 16 * L2
rec("C4 CE-col norm threshold (next-input rate)", math.isfinite(th4) and th4 > th3,
    f"threshold {th4:.2f} (difference to C3: {th4 - th3:.2f}); rate exponent there {(r4 - kap0) * L - 1 - (th4 + 16 * L2 + 1296 * w8):.1f} >= 0")
kQ = (6 * kap0 + 9 * kt0 + 16 + 64 * L2 + 1296 * w8) / 2
thQd = root(f_disp, extra_r=kt0 + 2, fac=L2)
thQn = root(f_next, extra_r=kt0 + 2, fac=L2)
rec("C5 CE-Q-col rate threshold", 1478.4 <= kQ <= 1478.7,
    f"kappa_c^Q* = {kQ:.3f}; norm thresholds: displayed form {thQd:.2f}, next-input form {thQn:.2f}")
la = 4 / (40 * 6.6)
w = (math.exp(1 / 120) - 1) + (math.exp(la) - 1)
v6 = math.exp(la) / (1 - w)
v6r = math.exp(0.0152) / 0.9762
rec("C6 SN-1 exact 1.0398", 1.0398 <= v6 <= 1.0399 and v6r > 1.04, f"exact {v6:.6f}; rounded display {v6r:.6f}; la={la:.7f}, w={w:.7f}")
s7 = sum(math.exp(-(4 ** j - 1) / 8) for j in range(1, 30))
rec("C7 sum_{j>=1} e^{-(4^j-1)/8} <= 1", s7 <= 1, f"{s7:.6f}")
kc = 1478.5
x = muM_W3(kc)
M = x / mu
n = 32
khat = kc - kap0 - kt0 - 2
logG0 = 2 * khat * 15 ** 4 + w8 * 17 ** 4
p0col = math.sqrt(16 * (4 * math.log(M) + (n / 2 + 2) * L2 + 6 * khat + logG0 + math.log(32)))
kh3 = kc - kap0
p03 = math.sqrt(16 * (4 * math.log(M) + 274 * kh3 + math.log(4) + 546 * 15 ** 4 * kh3 + 17 ** 4 * w8 + (n / 2) * L2 + math.log(32)))
kh3c = kc - 2 * kap0 - 2
p03c = math.sqrt(16 * (4 * math.log(M) + 274 * kh3c + math.log(4) + 546 * 15 ** 4 * kh3c + 17 ** 4 * w8 + (n / 2) * L2 + math.log(32)))
rec("C8 p_0(CE-Q-col) < p_0(CE-Q)", p0col < p03,
    f"M={M:.4e} (muM={x:.1f}); p0 CE-Q-col {p0col:.4e}; CE-Q (khat=kc-k0) {p03:.4e}; CE-Q (c1 khat) {p03c:.4e}")

# ---------------------------------------------------------------- D1. Lemma TILT
viol = 0
maxr = 0.0
maxr_exact = 0.0
dim = 6
for t in range(20):
    ev = rng.uniform(0, 1, dim)
    if t % 2 == 0:
        ev[:2] = rng.uniform(0.99, 1.0, 2)
    Qm, _ = np.linalg.qr(rng.normal(size=(dim, dim)))
    K = Qm @ np.diag(ev) @ Qm.T
    trK = ev.sum()
    v = rng.normal(size=(200000, dim))
    qv = np.einsum('ij,jk,ik->i', v, K, v)
    for th in [0.0, 0.3, 0.6, 0.9]:
        # exact-tilt reference: Z * P_tilt(q >= s), tilted covariance (1 - th K)^{-1}
        Ct = Qm @ np.diag(1 / (1 - th * ev)) @ Qm.T
        Lc = np.linalg.cholesky(Ct)
        wv = rng.normal(size=(200000, dim)) @ Lc.T
        qw = np.einsum('ij,jk,ik->i', wv, K, wv)
        Zt = float(np.prod((1 - th * ev) ** -0.5))
        for s in [0.0, 2.0, 8.0]:
            f = np.exp(th * qv / 2) * (qv >= s)
            est = f.mean() + 4 * f.std() / math.sqrt(len(f))
            bound = math.exp((1 + th) * trK / (2 * (1 - th))) * math.exp(-(1 - th) * s / 4)
            if est > bound:
                viol += 1
            maxr = max(maxr, est / bound)
            pe = (qw >= s).mean()
            ex = Zt * (pe + 4 * math.sqrt(max(pe * (1 - pe), 1e-300) / len(qw)))
            maxr_exact = max(maxr_exact, ex / bound)
rec("D1 TILT (plain MC + 4 SE <= bound)", viol == 0,
    f"violations {viol}; max ratio plain {maxr:.4f}; max ratio exact-tilt (+4 SE) {maxr_exact:.4f}")

# ---------------------------------------------------------------- D2/D3. Proposition RES (SU(2), 4x4, blocks 2)
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]
Tb = [1j * s_ / math.sqrt(2) for s_ in sig]


def alg(c):
    return sum(c[k] * Tb[k] for k in range(3))


def coords(A):
    return np.array([(-np.trace(A @ Tb[k])).real for k in range(3)])


def expm2(A):
    c = coords(A)
    a = np.linalg.norm(c) / math.sqrt(2)  # A = i a n.sigma
    if a < 1e-15:
        return np.eye(2, dtype=complex) + A
    return math.cos(a) * np.eye(2) + (math.sin(a) / a) * A


def logm2(U):
    ct = max(-1.0, min(1.0, (np.trace(U).real) / 2))
    a = math.acos(ct)
    if a < 1e-12:
        X = (U - U.conj().T) / 2
    else:
        X = (a / math.sin(a)) * (U - U.conj().T) / 2
    return X - np.trace(X) / 2 * np.eye(2)


def hsn(A):
    return math.sqrt(max(0.0, (-np.trace(A @ A)).real))


def opn(M):
    return float(np.linalg.norm(M, 2))


Ls = 4
sites = [(a, b) for a in range(Ls) for b in range(Ls)]
centres = [(0, 0), (0, 2), (2, 0), (2, 2)]
free = [s_ for s_ in sites if s_ not in centres]


def shift(x, mu_, k=1):
    y = list(x)
    y[mu_] = (y[mu_] + k) % Ls
    return tuple(y)


Ub = {}
for x_ in sites:
    for m_ in range(2):
        Ub[(x_, m_)] = expm2(alg(0.2 * rng.normal(size=3)))


def hmap(A):
    out = []
    for c in centres:
        tot_ = np.zeros((2, 2), complex)
        for (da, db) in [(0, 0), (1, 0), (0, 1), (1, 1)]:
            Tm = np.eye(2, dtype=complex)
            x_ = c
            path = [0] * da + [1] * db
            for m_ in path:
                tot_ += Tm @ A[(x_, m_)] @ Tm.conj().T
                Tm = Tm @ Ub[(x_, m_)]
                x_ = shift(x_, m_)
        out.append(coords(tot_ / 4))
    return np.concatenate(out)


def lam_from(vec):
    lam = {s_: np.zeros((2, 2), complex) for s_ in sites}
    for i, s_ in enumerate(free):
        lam[s_] = alg(vec[3 * i:3 * i + 3])
    return lam


def A_of(vec):
    lam = lam_from(vec)
    A = {}
    for x_ in sites:
        for m_ in range(2):
            y_ = shift(x_, m_)
            W = expm2(lam[x_]) @ Ub[(x_, m_)] @ expm2(-lam[y_]) @ Ub[(x_, m_)].conj().T
            A[(x_, m_)] = logm2(W)
    return A


def F(vec):
    return hmap(A_of(vec))


def plaq_norms(Uf):
    out = []
    for x_ in sites:
        P = Uf[(x_, 0)] @ Uf[(shift(x_, 0), 1)] @ Uf[(shift(x_, 1), 0)].conj().T @ Uf[(x_, 1)].conj().T
        out.append(opn(np.eye(2) - P))
    return np.array(out)


p_bg = plaq_norms(Ub)
good = 0
witness_max = []
info = []
for start in range(5):
    v0 = rng.uniform(-1, 1, 3 * len(free))
    lam0 = lam_from(v0)
    sup = max(hsn(lam0[s_]) for s_ in free)
    vec = v0 * (0.3 / sup)
    for it in range(60):
        Fv = F(vec)
        if np.max(np.abs(Fv)) < 1e-13:
            break
        Jm = np.zeros((len(Fv), len(vec)))
        hstep = 1e-6
        for k in range(len(vec)):
            e_ = np.zeros(len(vec))
            e_[k] = hstep
            Jm[:, k] = (F(vec + e_) - F(vec - e_)) / (2 * hstep)
        vec = vec - np.linalg.pinv(Jm) @ Fv
    resid = float(np.max(np.abs(F(vec))))
    A = A_of(vec)
    amax = max(hsn(A[k]) for k in A)
    aop = max(opn(A[k]) for k in A)
    lam = lam_from(vec)
    rec_err = max(opn(expm2(A[(x_, m_)]) @ Ub[(x_, m_)] - expm2(lam[x_]) @ Ub[(x_, m_)] @ expm2(-lam[shift(x_, m_)]))
                  for x_ in sites for m_ in range(2))
    Uf = {k: expm2(A[k]) @ Ub[k] for k in A}
    pch = float(np.max(np.abs(plaq_norms(Uf) - p_bg)))
    ok = resid <= 1e-10 and amax >= 0.1 and aop < math.pi and rec_err <= 1e-10 and pch <= 1e-10
    good += ok
    if ok:
        witness_max.append(amax)
    info.append(f"[{resid:.1e},{amax:.3f},{rec_err:.1e},{pch:.1e}]")
rec("D2 RES witnesses (>=3 of 5)", good >= 3, f"good {good}/5; [resid, max|A|, recon, plaq change]: " + " ".join(info))

# D3: random A in ker h with the same sup size
keys = [(x_, m_) for x_ in sites for m_ in range(2)]
Hlin = np.zeros((12, 3 * len(keys)))
for k_, key in enumerate(keys):
    for c in range(3):
        A = {kk: np.zeros((2, 2), complex) for kk in keys}
        A[key] = Tb[c]
        Hlin[:, 3 * k_ + c] = hmap(A)
_, sv, Vt = np.linalg.svd(Hlin)
null = Vt[12:]
target = float(np.median(witness_max)) if witness_max else 0.3
mins = []
for t in range(5):
    vv = null.T @ rng.normal(size=null.shape[0])
    A = {key: alg(vv[3 * k_:3 * k_ + 3]) for k_, key in enumerate(keys)}
    sc = target / max(hsn(A[k]) for k in A)
    A = {k: sc * A[k] for k in A}
    hres = float(np.max(np.abs(hmap(A))))
    Uf = {k: expm2(A[k]) @ Ub[k] for k in A}
    mins.append(float(np.max(np.abs(plaq_norms(Uf) - p_bg))))
rec("D3 control: generic slice directions move plaquettes", min(mins) >= 1e-3,
    f"target sup {target:.3f}; max plaquette change per sample: " + ", ".join(f"{m:.3e}" for m in mins) + f"; |h(A)| {hres:.1e}")

npass = sum(ok for _, ok in RES)
print(f"OVERALL: {'PASS' if npass == len(RES) else 'FAIL'} {npass}/{len(RES)}  (runtime {time.time() - t0:.1f} s)")
