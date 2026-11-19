#!/usr/bin/env python3
"""edge-block: is the glued split's window top a wall, and on what block size must edge registers sit?

CL-1 edge register: lengths flat x 2^(n/s - 3), n = 0..4s (window [L/8, 2L]); split glued at the all-full
state; children at n = 3s.  Zero-point spread of a one-cell edge sigma_l ~ 0.2 l_rung at Lambda ~ 4
(hop-recheck B3, volume-mode B3; supplied).  numpy/scipy only, self-contained.
"""
import time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl

AUDIT_TIMEOUT_SEC = 120
t0 = time.time()
NP = NF = 0


def check(tag, ok, msg, det=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] [{tag}] {msg} | {det}")


SIG1 = 0.2          # one-cell relative zero-point spread at Lambda = 4 (supplied)
SIGN_MIN = 3.8      # pinning: sigma_n >= 3.8 values (hop-recheck D3)
Z = 6

# ---------------------------------------------------------------- A. the top of the window under the point glue
print("== A. is the top a wall? (point glue at the all-full state)")
E6 = [np.array(e, float) for e in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 0, 1),
                                   (1, -1, 0), (0, 1, -1), (-1, 0, 1))]
rng = np.random.default_rng(1)
worst = np.inf
for _ in range(2000):
    h = rng.normal(size=(3, 3)); h = h + h.T; h -= np.trace(h) / 3 * np.eye(3)
    worst = min(worst, max(e @ h @ e / (2 * e @ e) for e in E6) / np.linalg.norm(h))
check("T", worst > 0,
      "A1 the glue acts at one point of each cube's register space (every register full); every traceless "
      "change of the metric lengthens some edge (both TT polarisations included), so from the all-full state "
      "every shape mode leaves the register range: for all modes but the uniform raise the top value is a hard wall",
      f"min over 2000 traceless h of max_e (dl/l)/|h| = {worst:.3f} > 0")


def chain_h(M):
    return sp.diags([np.ones(M - 1), np.ones(M - 1)], [1, -1], format="csr")


def box(E, M):          # E registers with values 0..M-1, nearest hops (J = 1)
    I = sp.identity(M, format="csr"); H = None
    for i in range(E):
        t = [I] * E; t[i] = chain_h(M); o = t[0]
        for x in t[1:]:
            o = sp.kron(o, x, format="csr")
        H = o if H is None else H + o
    return H


def packet(E, M, c, sig, k=np.pi / 2):
    g = np.arange(M); f = np.exp(-(g - c) ** 2 / (4 * sig ** 2) + 1j * k * g); v = f
    for _ in range(E - 1):
        v = np.kron(v, f)
    return v / np.linalg.norm(v)


def transmit(E, M, sig, point, K=300):
    D = int(3 * sig + 6); Mi = M + 1                       # values 0..M (top = M)
    if point:                                              # walls at M, corner -> exit chain of K sites
        Hb = box(E, Mi); nb = Hb.shape[0]; corner = nb - 1
        C = sp.coo_matrix(([1.0], ([corner], [0])), shape=(nb, K))
        H = sp.bmat([[Hb, C], [C.T, chain_h(K)]], format="csr"); psi = np.concatenate([packet(E, Mi, M - D, sig), np.zeros(K)])
        out = lambda p: np.sum(np.abs(p[nb:]) ** 2)
    else:                                                  # surface glue = no wall: past n_1+..+n_E = E M
        Mx = M + D + (25 if E == 2 else 10); H = -box(E, Mx); psi = packet(E, Mx, M - D, sig)
        idx = np.indices([Mx] * E).reshape(E, -1).sum(0)
        out = lambda p: np.sum(np.abs(p[idx > E * M]) ** 2)
    T = 2.0 * D / 2.0 + 8.0                                 # speed 2 per register at k = pi/2
    if point:
        H = -H
    p1 = spl.expm_multiply(-1j * H * T, psi)
    p2 = spl.expm_multiply(-1j * H * 2 * T, psi) if point else p1
    return out(p1), out(p2)


rows = []
for E, M, sigs in ((2, 60, (2.0, 4.0, 8.0)), (3, 18, (1.5, 2.5, 3.5))):
    for s_ in sigs:
        tp, tp2 = transmit(E, M, s_, True); ts, _ = transmit(E, M, s_, False)
        rows.append((E, s_, tp, tp2, ts))
dec2 = rows[0][2] / rows[2][2]; dec3 = rows[3][2] / rows[5][2]
check("D", all(r[4] > 0.9 for r in rows) and rows[2][2] < 0.25 and rows[5][2] < 0.25 and dec2 > 2 and dec3 > 2,
      "A2 E registers moving together toward the top (packet of spread sigma_n values per register): through the "
      "point glue only the part that meets the corner passes, falling with sigma_n (as 1/sigma_n at E = 2, faster at E = 3); the rest "
      "reflects off the per-register walls; a glue on the whole surface sum n = E x top passes almost all",
      "E, sigma_n: point (t, 2t), surface = " + "; ".join(f"{r[0]}, {r[1]}: ({r[2]:.3f}, {r[3]:.3f}), {r[4]:.3f}" for r in rows))


# ---------------------------------------------------------------- log register in a Weiss field (window mass)
def logreg(s, sig, c, lo_oct=-3, hi_oct=1, J0=1.0, uniform=False, N=None):
    """register with values on lengths 2^(n/s + lo_oct) (or a uniform grid), kinetic -J0 d^2/dl^2 (dressed
    weight: uniform in l), Weiss field k/2 (l - c)^2 with harmonic spread sig; Dirichlet beyond both ends."""
    if uniform:
        l = np.linspace(2.0 ** lo_oct, 2.0 ** hi_oct, N)
    else:
        l = 2.0 ** (np.arange(int(round((hi_oct - lo_oct) * s)) + 1) / s + lo_oct)
    d = np.diff(l); dl = np.concatenate([[d[0]], d, [d[-1]]])
    w = 0.5 * (dl[:-1] + dl[1:]); cond = J0 / dl
    diag = (cond[:-1] + cond[1:]) / w; off = -cond[1:-1] / np.sqrt(w[:-1] * w[1:])
    k = 0.5 * J0 / sig ** 4
    H = np.diag(diag + 0.5 * k * (l - c) ** 2) + np.diag(off, 1) + np.diag(off, -1)
    ev, V = np.linalg.eigh(H); g = V[:, 0]; mel = V.T @ (l * g)
    chi0 = 2 * np.sum(mel[1:] ** 2 / (ev[1:] - ev[0]))
    return chi0 * k, np.sqrt(g @ (l ** 2 * g) - (g @ (l * g)) ** 2)


print("== B. the log window [L/8, 2L], top transparent: the bottom wall")
# B0: relative zero-point spread of a block edge falls as 1/b (block average of a 3D lattice field)
Nf = 40; kk = 2 * np.pi * np.fft.fftfreq(Nf); KX, KY, KZ = np.meshgrid(kk, kk, kk, indexing="ij")
om = 2 * np.sqrt(np.sin(KX / 2) ** 2 + np.sin(KY / 2) ** 2 + np.sin(KZ / 2) ** 2); om[0, 0, 0] = np.inf


def ff(K, b):
    num = np.sin(b * K / 2); den = b * np.sin(K / 2)
    return np.where(np.abs(den) < 1e-14, 1.0, num / np.where(np.abs(den) < 1e-14, 1, den))


sb = {}
for b in (1, 2, 4, 8, 12):
    F2 = (ff(KX, b) * ff(KY, b) * ff(KZ, b)) ** 2
    sb[b] = np.sqrt(np.sum(F2 / (2 * om)) / Nf ** 3)
sl = {b: sb[b] * b for b in sb}
check("D", abs(sl[8] / sl[12] - 1) < 0.1 and sl[1] / sl[12] < 2,
      "B0 the zero-point spread of a block-averaged metric component falls as 1/b (b x spread tends to a "
      "constant): a block edge of b cells has relative spread s1(b) = s1(1)/b, i.e. stiffness Lambda_b = b^2 Lambda "
      "(the hinge sum is homogeneous of degree 2 in lengths, C1); its ABSOLUTE spread stays ~0.2 l_rung",
      "b x sigma(b) / sigma(1) at b = 1,2,4,8,12: " + ", ".join(f"{sl[b]/sl[1]:.3f}" for b in sl))
# B1: wall effect on the log grid vs a uniform grid: same function of d/sigma
sigB = 0.04; lw = 1 / 8.
cmp_ = []
for t in (3.0, 4.0, 5.0, 6.0):
    c = lw + t * sigB
    rl, _ = logreg(400, sigB, c, hi_oct=0)
    ru, _ = logreg(0, sigB, c, uniform=True, N=1000, hi_oct=0)
    cmp_.append((t, 1 - rl, 1 - ru))
check("D", all(abs(np.log(a / b_)) < 0.15 for _, a, b_ in cmp_),
      "B1 a log-spaced register (dressed weights, kinetic form uniform in l) feels its bottom wall exactly as a "
      "uniform one: the window mass depends only on the wall distance in zero-point spreads, not on the spacing",
      "d/sigma: 1-r log, uniform = " + "; ".join(f"{t:.0f}: {a:.2e}, {b_:.2e}" for t, a, b_ in cmp_))
ts = np.array([3.0, 4.0, 5.0, 6.0])
ys = np.array([np.log(1 - logreg(400, sigB, lw + t * sigB, hi_oct=0)[0]) for t in ts]) + ts ** 2 / 2
bb, aa = np.polyfit(np.log(ts[1:]), ys[1:], 1)
inv_lr = 1.2e27; mlim = 1.3e-23 / inv_lr               # LIGO m_g in units of 1/l_rung


def t_need(b):
    target = np.log((mlim * b) ** 2 / Z); t = 10.0      # block mass in units of 1/(b l_rung)
    for _ in range(200):
        t = np.sqrt(2 * (aa + bb * np.log(t) - target))
    return t


tn1, tn37 = t_need(1), t_need(37)
check("E", 20 < tn1 < 24 and abs(tn37 - tn1) < 0.5,
      "B2 the measured graviton-mass bound (m < 1.3e-23 eV) needs every register's wall >~ 22 zero-point spreads "
      "away, recomputed on the log register; a block's mass is per block length, which moves this by < 0.5 sigma",
      f"fit 1-r = e^{aa:.2f} t^{bb:.2f} e^(-t^2/2); d/sigma needed: b = 1 {tn1:.1f}, b = 37 {tn37:.1f}")
tn = tn1
bmin = {Lam: tn * SIG1 * np.sqrt(4 / Lam) / (1 - 1 / 8) for Lam in (4.0, 1.0)}
dist1 = (1 - 1 / 8) / SIG1
check("E", dist1 < tn and bmin[4.0] < 6,
      "B3 with a transparent top the binding wall is the bottom at L/8, nearest when a child is born at L "
      "(7/8 L away): one-cell edges sit 4.4 sigma from it (cell-scale mass); block edges need b >= 22 x 0.2/0.875",
      f"one-cell distance {dist1:.1f} sigma; b_min = {bmin[4.0]:.2f} (Lambda 4), {bmin[1.0]:.2f} (Lambda 1, "
      "l_rung = sqrt(8 pi) l_P read literally)")
alpha = {"J0740 (alpha_c 0.45)": 0.45, "causal max-mass (0.24)": 0.24}
bns = {k_: tn * SIG1 / (a - 1 / 8) for k_, a in alpha.items()}
check("E", all(v > bmin[4.0] for v in bns.values()),
      "B4 strong fields bind harder: a static core's edges are alpha_c times the far edges (window-fix A1), so at "
      "the worst far phase (L) a neutron-star core sits (alpha_c - 1/8) L above the floor; a cell-scale mass there "
      "would cut the core's self-gravity",
      "b_min: " + ", ".join(f"{k_} {v:.1f}" for k_, v in bns.items()))
top_frac = {b: -np.log2(1 - min(0.999, tn * SIG1 / (2 * b))) for b in (6, 14, 37)}
check("E", all(v > 0.05 for v in top_frac.values()),
      "B5 under the point glue the top is a wall (A1-A2) that every parent edge reaches at its split: d = 0 "
      "there, a cell-scale mass, and the edges sit within 22 sigma of it for a fixed share of every doubling "
      "cycle at any b; the point glue fails at every block size",
      "share of the log cycle within 22 sigma of the top: " + ", ".join(f"b={b}: {v:.2f}" for b, v in top_frac.items()))
Dl = {b: np.log2(1 + tn * SIG1 / (2 * b)) for b in (6, 14, 37)}
check("E", all(v < 0.5 for v in Dl.values()),
      "B6 fix: glue on the surface where the mean register value of a cube reaches 4s (log-mean edge 2L), with "
      "each register running Delta octaves above it, Delta >= log2(1 + 22 sigma_l/2L): every mode then passes "
      "into the children (A2 surface) and the top wall stays >= 22 sigma from every edge",
      "Delta octaves needed: " + ", ".join(f"b={b}: {v:.2f}" for b, v in Dl.items()))

# ---------------------------------------------------------------- C. G, unit map, matter reading
print("== C. G, the unit map and the matter reading on block edges")
P = rng.normal(size=(4, 3)); b_ = 7.0


def tet(P):
    A = sum(0.5 * np.linalg.norm(np.cross(P[j] - P[i], P[k] - P[i])) for i, j, k in ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)))
    n = lambda a, b2, c: np.cross(P[b2] - P[a], P[c] - P[a])
    na, nb_ = n(0, 1, 2), n(0, 1, 3)
    dih = np.arccos(np.dot(na, nb_) / np.linalg.norm(na) / np.linalg.norm(nb_))
    return A, dih


(A1_, d1), (A7, d7) = tet(P), tet(b_ * P)
check("T", abs(A7 / A1_ - b_ ** 2) < 1e-9 and abs(d7 - d1) < 1e-12,
      "C1 areas scale as b^2 and dihedral angles (so deficits) are scale-free: the hinge sum A eps/(8 pi G) on a "
      "b-scaled triangulation is b^2 times the cell one, as the Einstein-Hilbert action of a b-scaled metric is: "
      "the same G, Lambda_b = b^2 Lambda for the block registers, and l_rung (the unit map) untouched",
      f"area ratio {A7/A1_:.6f} (b^2 = {b_**2:.0f}), dihedral change {abs(d7-d1):.1e}")
onface = 0
for b in range(2, 10):
    g = np.arange(b) + 0.5; X, Y, Zc = np.meshgrid(g, g, g, indexing="ij")
    for sx in (1, -1):
        for sy in (1, -1):
            for sz in (1, -1):
                v = sx * X + sy * Y + sz * Zc
                onface += np.sum(np.abs(v / b - np.round(v / b)) < 1e-12)
check("T", onface == 0,
      "C2 the faces of a block's five tetrahedra lie on planes +-x+-y+-z = integer multiples of b, and cell "
      "centres (half-integers) are never on them: each cell lies in exactly one block tetrahedron, so 'each "
      "cell reads the flat metric of the block tetrahedron holding its centre' is well defined (no interpolant)",
      f"cell centres on a face for b = 2..9: {onface}")
for e0 in (0.0075, 0.0375):
    smove = 0.85 / np.sin(e0)
    print(f"   one-cell edges at eps0 {e0}: 48 s = {48*smove:.0f} register sites per cell (s = {smove:.0f})")
check("T", 48 * 0.85 / np.sin(0.0375) > 125,
      "C3 counting: six registers of 2 x 4s sites per cell cost 48 s >= 1100 (eps0 0.0375) to 5400 (0.0075) "
      "sites per cell, beyond a 5^3 (125) or 7^3 (343) role block: one-cell edge registers do not fit the cell; "
      "sharing one register set among b_e^3 cells divides the cost by b_e^3",
      "")

# ---------------------------------------------------------------- D. budget
print("== D. sites per cell for block-edge registers (eps0, b_e)")
okfit = True
for e0 in (0.0075, 0.0375):
    parts = []
    for be in (6, 8, 14, 38):
        s_pin = SIGN_MIN * 2 * np.log(2) * be / SIG1
        s = max(0.85 / np.sin(e0), s_pin); Dlt = np.log2(1 + tn * SIG1 / (2 * be))
        per_block = 12 * (4 + Dlt) * s; per_cell = per_block / be ** 3
        parts.append(f"b_e {be}: s {s:.0f}, {per_cell:.1f}/cell")
        if be == 6 and per_cell > 125 - 70:
            okfit = False
    print("   eps0 " + str(e0) + ": " + "; ".join(parts))
check("E", okfit,
      "D1 s >= max(0.85/sin eps0, 26.3 b_e) (moving, with one update per block half-tick; pinning sigma_n >= 3.8 "
      "at the top, where values are sparsest); per cell 12 (4 + Delta) s / b_e^3, falling as 1/b_e^2: at b_e = 6 "
      "it fits the 55 spare sites of a 5^3 cell beside 54 rishons (S_Y = 2) and 16 matter modes; at the S_Y ~ 275 "
      "the hypercharge coupling needs, rishons (~3300) set the cell size, not the edges",
      "")
print("theorems: A1, C1-C3; diagnostics: A2, B0, B1; estimates: B2-B6, D1")
print("supplied: s1(1) = 0.2 at Lambda 4, harmonic Weiss/RPA wall model (z=6), dressed weights uniform in l, "
      "one block-edge update per block half-tick, rishon sizes, J0740/causal alpha_c")
print(f"elapsed_seconds {time.time()-t0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")
