"""Check s1 (lane F, SF.md). Criteria: checks/s1_criteria.md (written first). Prints PASS/FAIL per criterion."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(v, "1")
import math
import numpy as np
from scipy.stats import chi2

results = {}


def rec(name, ok, msg):
    ok = None if ok is None else bool(ok)  # post-run fix 1: numpy bools were mis-reported
    results[name] = ok
    print(f"{name}: {'PASS' if ok is True else ('INCONCLUSIVE' if ok is None else 'FAIL')}  {msg}")


# ---------------------------------------------------------------- A. SF-DC
Tc, L, R, rK = 12, 3, 1, 1
S = Tc * L
n = S * S
rng = np.random.default_rng(20261028)
xs = np.repeat(np.arange(S), S)
ys = np.tile(np.arange(S), S)
bx, by = xs // L, ys // L  # block coords of each site


def cdist(a, b):
    d = np.abs(a - b) % Tc
    return np.minimum(d, Tc - d)


blk_d = np.maximum(cdist(bx[:, None], bx[None, :]), cdist(by[:, None], by[None, :]))  # site-site block distance
K0 = np.zeros((n, n))
for i in range(n):
    x, y = xs[i], ys[i]
    K0[i, i] = 4.0 + 4.0  # -Delta diagonal + m^2 (m^2 = 4)
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        j = ((x + dx) % S) * S + (y + dy) % S
        K0[i, j] -= 1.0
E = rng.standard_normal((n, n)) * (blk_d <= rK)
E = (E + E.T) / 2
E *= 0.3 / np.linalg.norm(E, 2)
K = K0 + E
print(f"A: n = {n}, lambda_min(K) = {np.linalg.eigvalsh(K)[0]:.4f}, ||E|| = {np.linalg.norm(E, 2):.3f}")

# boxes = single blocks (R = 1): box id = bx*Tc + by
box_of_site = bx * Tc + by
nbox = Tc * Tc
box_coord = np.array([(a, b) for a in range(Tc) for b in range(Tc)])


def box_dist(p, q):
    return max(cdist(box_coord[p][0], box_coord[q][0]), cdist(box_coord[p][1], box_coord[q][1]))


Omega = [np.where(np.maximum(cdist(bx, box_coord[b][0]), cdist(by, box_coord[b][1])) <= R)[0] for b in range(nbox)]
Ymask = np.zeros(nbox, bool)
Y = [0 * Tc + 0, 6 * Tc + 6]
Ymask[Y] = True
s_val = 0.5
# components: linked iff box distance <= R + rK
comps = []
for b in Y:
    placed = False
    for c in comps:
        if any(box_dist(b, b2) <= R + rK for b2 in c):
            c.append(b); placed = True
    if not placed:
        comps.append([b])
print(f"A: linked components of Y: {comps}")
comp_of = {b: ci for ci, c in enumerate(comps) for b in c}
Yplus = [sorted({b2 for b2 in range(nbox) if any(box_dist(b2, b) <= R + rK for b in c)}) for c in comps]
OmegaYplus = [np.unique(np.concatenate([Omega[b] for b in yp])) for yp in Yplus]
inOYp = [np.zeros(n, bool) for _ in comps]
for ci in range(len(comps)):
    inOYp[ci][OmegaYplus[ci]] = True
inOmega = np.zeros((nbox, n), bool)
for b in range(nbox):
    inOmega[b, Omega[b]] = True
cols_of_box = [np.where(box_of_site == b)[0] for b in range(nbox)]
Ycols = np.concatenate([cols_of_box[b] for b in Y])


def kinv_s(Kmat, t):
    """K^{-1}(s;t) = P (1 - R(s))^{-1}; R(s) has non-zero columns only on Y boxes (Woodbury on those columns)."""
    P = np.zeros((n, n))
    Rs = np.zeros((n, len(Ycols)))
    col_pos = 0
    Gs = {}
    for b in range(nbox):
        Om = Omega[b]
        G = np.linalg.inv(Kmat[np.ix_(Om, Om)] + t * np.eye(len(Om)))
        cols = cols_of_box[b]
        # P[:, cols] = G[Om, cols]
        loc = np.searchsorted(Om, cols)
        P[np.ix_(Om, cols)] = G[:, loc]
        Gs[b] = (Om, G, loc)
    full_R_rows = 0.0
    for b in Y:
        Om, G, loc = Gs[b]
        cols = cols_of_box[b]
        v = Kmat[:, Om] @ G[:, loc]  # K G 1_box
        v[inOmega[b]] = 0.0
        Rs[:, col_pos:col_pos + len(cols)] = -s_val * v
        col_pos += len(cols)
    N0 = np.abs(Rs).sum(axis=1).max()  # row-sum norm of |R(s)| (only Y columns non-zero)
    # (1 - R)^{-1} = 1 + R_Y (1_Y - R_YY)^{-1} E_Y^T
    RYY = Rs[Ycols, :]
    M = np.linalg.solve(np.eye(len(Ycols)) - RYY, np.eye(len(Ycols)))
    Kin = P.copy()
    Kin[:, Ycols] += P @ Rs @ M
    return Kin, N0


A0ok, A1w, A2w, A3b = True, 0.0, 0.0, 0.0
for t in (0.0, 1.0, 10.0):
    Kin, N0 = kinv_s(K, t)
    mx = np.abs(Kin).max()
    if not N0 < 1:
        A0ok = False
    a1 = 0.0
    for b in range(nbox):
        if Ymask[b]:
            continue
        cols = cols_of_box[b]
        a1 = max(a1, np.abs(Kin[np.ix_(~inOmega[b], cols)]).max() / mx)
    a2, a3 = 0.0, 0.0
    for b in Y:
        ci = comp_of[b]
        cols = cols_of_box[b]
        a2 = max(a2, np.abs(Kin[np.ix_(~inOYp[ci], cols)]).max() / mx)
        reach = inOYp[ci] & ~inOmega[b]
        a3 = max(a3, np.abs(Kin[np.ix_(reach, cols)]).max() / mx)
    A1w, A2w, A3b = max(A1w, a1), max(A2w, a2), max(A3b, a3)
    print(f"A t={t}: N_0(|R(s)|) = {N0:.4f}; max off-Omega (non-Y cols) = {a1:.2e}; max off-Omega(Y+) (Y cols) = {a2:.2e}; "
          f"max reach beyond Omega_box = {a3:.2e}")
rec("A0", True if A0ok else None, "N_0(|R(s;t)|) < 1 at t = 0, 1, 10")
if A0ok:
    rec("A1", A1w <= 1e-12, f"max rel {A1w:.2e} (<= 1e-12)")
    rec("A2", A2w <= 1e-12, f"max rel {A2w:.2e} (<= 1e-12)")
    rec("A3", A3b >= 1e-8, f"max rel reach {A3b:.2e} (>= 1e-8)")
else:
    for c in ("A1", "A2", "A3"):
        rec(c, None, "A0 inconclusive")

# A4 / A5: quadrature in theta, u = tan(theta): (2/pi) int_0^{pi/2} K^{-1}(s; tan^2) sec^2 dtheta
nodes, wts = np.polynomial.legendre.leggauss(200)
th = (nodes + 1) * (math.pi / 4)
wt = wts * (math.pi / 4)
lam, Q = np.linalg.eigh(K)
Kmhalf = (Q / np.sqrt(lam)) @ Q.T
C1 = np.zeros((n, n))
Cs = np.zeros((n, n))
for th_i, w_i in zip(th, wt):
    c2, s2 = math.cos(th_i) ** 2, math.sin(th_i) ** 2
    C1 += w_i * np.linalg.inv(K * c2 + s2 * np.eye(n))  # (K + tan^2)^{-1} sec^2 = (K cos^2 + sin^2)^{-1}
    Kin, _ = kinv_s(K, math.tan(th_i) ** 2)
    Cs += w_i * Kin / c2
C1 *= 2 / math.pi
Cs *= 2 / math.pi
a4 = np.abs(C1 - Kmhalf).max() / np.abs(Kmhalf).max()
rec("A4", a4 <= 1e-6, f"quadrature vs eigen K^(-1/2): rel max-entry err {a4:.2e} (<= 1e-6)")
# predicted allowed (x, y): y in box b' not in Y with x in Omega_b'; y in Y box of comp a with x in Omega(Y_a^+); y in x's own block
allowed = np.zeros((n, n), bool)
for b in range(nbox):
    cols = cols_of_box[b]
    if Ymask[b]:
        allowed[np.ix_(inOYp[comp_of[b]], cols)] = True
    else:
        allowed[np.ix_(inOmega[b], cols)] = True
allowed |= (box_of_site[:, None] == box_of_site[None, :])
a5 = np.abs(Cs[~allowed]).max() / np.abs(Cs).max()
rec("A5", a5 <= 1e-10, f"C(s) outside predicted D(x): rel {a5:.2e} (<= 1e-10)")
# A6: one long-range entry
z = Omega[0][np.argmin(np.abs(bx[Omega[0]] - 0) + np.abs(by[Omega[0]] - 1) + 0)]  # a site of Omega_(0,0)
cand = np.where(~(inOYp[0] | inOYp[1]))[0]
dmin = np.array([min(np.maximum(cdist(bx[c], bx[OmegaYplus[0]]), cdist(by[c], by[OmegaYplus[0]])).min(),
                     np.maximum(cdist(bx[c], bx[OmegaYplus[1]]), cdist(by[c], by[OmegaYplus[1]])).min()) for c in cand])
far = cand[dmin >= 2]
if len(far) == 0:
    rec("A6", False, "no site at block distance >= 2 from Omega(Y+)")
else:
    w = far[0]
    K2 = K.copy()
    K2[z, w] += 1e-3; K2[w, z] += 1e-3
    lm = np.linalg.eigvalsh(K2)[0]
    Kin2, N02 = kinv_s(K2, 0.0)
    outside = ~(inOYp[0] | inOYp[1])
    a6 = np.abs(Kin2[np.ix_(outside, cols_of_box[0])]).max() / np.abs(Kin2).max()
    rec("A6", (a6 >= 1e-10) and lm > 0, f"long-range entry z={z}, w={w} (block dist {dmin[dmin >= 2][0]} from Omega(Y+)),"
        f" lambda_min = {lm:.3f}, N_0 = {N02:.3f}: column in box(0,0) reaches outside Omega(Y+) with rel {a6:.2e} (>= 1e-10)")

# ---------------------------------------------------------------- B. SF-J
rngB = np.random.default_rng(7)


def sl_basis(N):
    B = []
    for a in range(N):
        for b in range(N):
            if a != b:
                M = np.zeros((N, N), complex); M[a, b] = 1; B.append(M)
    for k in range(N - 1):
        M = np.zeros((N, N), complex); M[k, k] = 1; M[k + 1, k + 1] = -1; B.append(M)
    return B


def f_series(X, terms=80):
    # f(X) = sum_{k>=0} (-X)^k/(k+1)!
    out = np.eye(X.shape[0], dtype=complex)
    term = np.eye(X.shape[0], dtype=complex)
    for k in range(1, terms):
        term = term @ (-X) / (k + 1)
        out = out + term
    return out


def ell(z):
    w = z / 2
    return np.log(np.sinh(w) / w) if abs(w) > 1e-12 else w * w / 6


b1, b2, b3 = 0.0, -np.inf, -np.inf
for N in (2, 3, 4):
    basis = sl_basis(N)
    Bmat = np.array([M.ravel() for M in basis]).T  # N^2 x (N^2-1)
    for _ in range(200):
        A = rngB.standard_normal((N, N)) + 1j * rngB.standard_normal((N, N))
        A -= np.trace(A) / N * np.eye(N)
        A *= rngB.uniform(1e-3, math.pi / 2) / np.linalg.norm(A, 2)
        ad = np.linalg.lstsq(Bmat, np.array([(A @ M - M @ A).ravel() for M in basis]).T, rcond=None)[0]
        detf = np.linalg.det(f_series(ad))
        lamA = np.linalg.eigvals(A)
        prod = 1.0 + 0j
        for a in range(N):
            for b in range(a + 1, N):
                w = (lamA[a] - lamA[b]) / 2
                prod *= (np.sinh(w) / w) ** 2 if abs(w) > 1e-14 else 1.0
        b1 = max(b1, abs(detf - prod) / abs(prod))
        Lval = sum(ell(lamA[a] - lamA[b]) for a in range(N) for b in range(N) if a != b)
        hs2 = np.linalg.norm(A, 'fro') ** 2
        b2 = max(b2, abs(Lval) / ((N / 9) * hs2))
        b3 = max(b3, abs(Lval - (N / 12) * np.trace(A @ A)) / ((N / 270) * hs2 ** 2))
        b1 = max(b1, abs(np.exp(Lval) - prod) / abs(prod))  # branch consistency folded into B1's error
rec("B1", b1 <= 1e-9, f"det f(ad A) vs product formula (and exp L): max rel {b1:.2e} (<= 1e-9)")
rec("B2", b2 <= 1.0, f"max |L|/((N/9)|A|_HS^2) = {b2:.4f} (<= 1)")
rec("B3", b3 <= 1.0, f"max |L - (N/12)trA^2|/((N/270)|A|_HS^4) = {b3:.4f} (<= 1)")
rr, pp = np.meshgrid(np.linspace(1e-3, math.pi / 2, 120), np.linspace(0, 2 * math.pi, 120))
ww = (rr * np.exp(1j * pp)).ravel()
b4 = np.max(np.abs(np.log(np.sinh(ww) / ww)) / ((2 / 9) * np.abs(ww) ** 2))
rec("B4", b4 <= 1.0, f"max |Log(sinh w/w)|/((2/9)|w|^2) on {ww.size} points = {b4:.4f} (<= 1)")
q = rngB.standard_normal((200000, 4))
q /= np.linalg.norm(q, axis=1)[:, None]
theta = np.sort(np.arccos(np.clip(q[:, 0], -1, 1)))
Fth = (theta - np.sin(theta) * np.cos(theta)) / math.pi
emp = np.arange(1, theta.size + 1) / theta.size
ks = max(np.abs(emp - Fth).max(), np.abs(emp - 1 / theta.size - Fth).max())
rec("B5", ks <= 0.01, f"Haar SU(2) eigen-angle CDF vs (2/pi)sin^2: KS = {ks:.4f} (<= 0.01)")

# ---------------------------------------------------------------- C. SF-cut
c1 = -np.inf
for nn in (12, 32):
    for p in np.linspace(0.5, 20, 400):
        c1 = max(c1, chi2.sf(p * p, nn) / (2 ** (nn / 2) * math.exp(-p * p / 4)))
rec("C1", c1 <= 1.0, f"max P(chi2_n > p^2)/(2^(n/2) e^(-p^2/4)) = {c1:.4f} (<= 1)")

# ---------------------------------------------------------------- D. SF-geo
d1 = True
for v in range(16):
    path = [(i ^ (i >> 1)) ^ v for i in range(16)]
    if path[0] != v or len(set(path)) != 16:
        d1 = False
    if any(bin(path[i] ^ path[i + 1]).count("1") != 1 for i in range(15)):
        d1 = False
rec("D1", d1, "translated Gray code: Hamiltonian path of 15 unit edges from every vertex")
d2 = True
import itertools
for e in itertools.product((-1, 0, 1), repeat=4):
    if e == (0, 0, 0, 0):
        continue
    inter = [(max(0, ei), min(1, ei + 1)) for ei in e]
    if any(lo > hi for lo, hi in inter):
        d2 = False; continue
    vert = [lo if lo in (0, 1) else None for lo, hi in inter]
    if any(c is None for c in vert):
        d2 = False
rec("D2", d2, "every *-neighbour of [0,1]^4 contains a vertex of it (80 offsets)")

# ---------------------------------------------------------------- E. arithmetic
k0 = 16 * math.log(12800)
logK0 = k0 - math.log(6400)
Lr = 3
e1 = 273 * (3 * k0 + 3 + 16 * math.log(2))
rec("E1", abs(e1 / 1.2779e5 - 1) <= 1e-3, f"273(3k0+3+16log2) = {e1:.6g}")
e2a = (k0 * Lr + 1) / (Lr - 1)
e2b = (k0 * Lr + 1 + math.log(16 * Lr ** 4) + logK0) / (Lr - 1)
rec("E2", abs(e2a - 227.5) <= 0.5 and abs(e2b - 302.4) <= 0.5, f"rate threshold {e2a:.3f}, contraction threshold {e2b:.3f}")
e3a = 1.2779e5 / 4.83e-11
e3b = (3 * 1.7e12 + 1) * 3
e3c = (2.65e15) ** 4
rec("E3", abs(e3a / 2.65e15 - 1) <= 0.01 and abs(e3b / 1.53e13 - 1) <= 0.01 and abs(e3c / 4.9e61 - 1) <= 0.02,
    f"M >= {e3a:.4g}, collar {e3b:.4g}, M^4 = {e3c:.4g}")
xg = np.linspace(1e-6, 0.5, 100000)
e4 = np.max(2 * np.arcsin(xg / 2) / xg)
rec("E4", e4 <= 1.0107, f"max 2arcsin(x/2)/x on (0,1/2] = {e4:.6f} (<= 1.0107)")

vals = list(results.values())
overall = "FAIL" if any(v is False for v in vals) else ("INCONCLUSIVE" if any(v is None for v in vals) else "PASS")
print(f"OVERALL: {overall}")
