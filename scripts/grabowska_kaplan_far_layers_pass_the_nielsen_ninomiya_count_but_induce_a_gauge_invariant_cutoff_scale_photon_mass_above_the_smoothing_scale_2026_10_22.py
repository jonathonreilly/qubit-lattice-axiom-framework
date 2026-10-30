AUDIT_INPUT_PATHS = ('docs/GRABOWSKA_KAPLAN_FAR_LAYERS_PASS_THE_NIELSEN_NINOMIYA_COUNT_BUT_INDUCE_A_GAUGE_INVARIANT_CUTOFF_SCALE_PHOTON_MASS_ABOVE_THE_SMOOTHING_SCALE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Hostile check of the leading chirality route ('layer s reads rung s',
Grabowska-Kaplan far layers that read a smoothed field). Free domain-wall
slabs (Shamir, Wilson kernel) in 2D and 4D momentum space, the overlap
(infinite-Ls) form, 2D SU(2) block-flux spreading with anchor transports,
and a 1+1D Hamiltonian slab (Chern strip) quench. Self-contained, seeded."""
import time
import itertools
import numpy as np

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = [0, 0]


def check(tag, kind, ok, msg, detail):
    NP[0 if ok else 1] += 1
    print("[%s] %s %s %s | %s" % ("PASS" if ok else "FAIL", tag, kind, msg, detail))


def note(tag, kind, msg):
    print("   %s %s %s" % (tag, kind, msg))


S1 = np.array([[0, 1], [1, 0]], complex)
S2 = np.array([[0, -1j], [1j, 0]])
S3 = np.diag([1.0, -1.0]).astype(complex)
I2 = np.eye(2, dtype=complex)


def gammas(d):
    if d == 2:
        return [S1, S2], S3
    return [np.kron(S1, s) for s in (S1, S2, S3)] + [np.kron(S2, I2)], np.kron(S3, I2)


def dw(p, G, M):
    """Wilson-Dirac kernel D_W(p) = sum(1 - cos p) - M + i gamma.sin p; p (B, d)."""
    ns = G[0].shape[0]
    D = ((np.sum(1 - np.cos(p), 1) - M)[:, None, None]) * np.eye(ns)
    for m in range(len(G)):
        D = D + 1j * np.sin(p[:, m])[:, None, None] * G[m]
    return D


def slab(p, G, g5, Ls, M, mf):
    """Shamir slab: (D_W + 1) on each layer, -P_- to s+1, -P_+ to s-1, mf wraps."""
    ns = G[0].shape[0]
    PP, PM = (np.eye(ns) + g5) / 2, (np.eye(ns) - g5) / 2
    B, n = len(p), ns * Ls
    D = np.zeros((B, n, n), complex)
    Dw = dw(p, G, M) + np.eye(ns)
    for s in range(Ls):
        a = slice(s * ns, (s + 1) * ns)
        D[:, a, a] = Dw
        if s + 1 < Ls:
            D[:, a, (s + 1) * ns:(s + 2) * ns] = -PM
        else:
            D[:, a, 0:ns] = mf * PM
        if s > 0:
            D[:, a, (s - 1) * ns:s * ns] = -PP
        else:
            D[:, a, (Ls - 1) * ns:] = mf * PP
    return D


def bz(d, N):
    k = 2 * np.pi * (np.arange(N) + 0.5) / N
    return np.array(list(itertools.product(k, repeat=d)))


def layer_pi(d, Ls, N, M=1.0, chunk=512):
    """Pi^{st} = d^2 Gamma / dA_s dA_t for a constant field A_0 on layer s
    (Gamma = -log det, DW mf=0 minus PV mf=1), per site. A constant field on
    every layer alike is pure gauge, so the rows of Pi sum to zero."""
    G, g5 = gammas(d)
    ns = G[0].shape[0]
    pts = bz(d, N)
    out = np.zeros((Ls, Ls))
    for mf, sg in ((0.0, 1), (1.0, -1)):
        for c in range(0, len(pts), chunk):
            p = pts[c:c + chunk]
            B = len(p)
            Gb = np.linalg.inv(slab(p, G, g5, Ls, M, mf)).reshape(B, Ls, ns, Ls, ns)
            d1 = np.sin(p[:, 0])[:, None, None] * np.eye(ns) + 1j * np.cos(p[:, 0])[:, None, None] * G[0]
            d2 = np.cos(p[:, 0])[:, None, None] * np.eye(ns) - 1j * np.sin(p[:, 0])[:, None, None] * G[0]
            tad = np.einsum('bsisj,bji->s', Gb, d2)
            Y = np.einsum('bsitj,bjk->bsitk', Gb, d1)
            bub = np.einsum('bsitk,btksi->st', Y, Y)
            out += sg * np.real(-np.diag(tad) + bub) / len(pts)
    return out


def sign_hw(p, G, g5, M=1.0):
    w, V = np.linalg.eigh(g5 @ dw(p, G, M))
    return np.einsum('bij,bj,bkj->bik', V, np.sign(w), V.conj())


# ===================== A. Nielsen-Ninomiya / Golterman-Shamir count ========
print("== A. spectrum count, free 2D slab (Ls = 8, M = 1): the theorem's setting is gauge-off")
G2, g52 = gammas(2)
PP2, PM2 = (I2 + S3) / 2, (I2 - S3) / 2


def bnd(p, Ls=8):
    """boundary field q = P_- psi_0 + P_+ psi_{Ls-1}: its 2x2 propagator."""
    Gi = np.linalg.inv(slab(p[None, :], G2, g52, Ls, 1.0, 0.0)[0])
    e = 2 * (Ls - 1)
    return (PM2 @ Gi[0:2, 0:2] @ PP2 + PM2 @ Gi[0:2, e:e + 2] @ PM2 + PP2 @ Gi[e:e + 2, 0:2] @ PP2
            + PP2 @ Gi[e:e + 2, e:e + 2] @ PM2)


def wind(f, c, rad=0.25, n=240):
    th = np.linspace(0, 2 * np.pi, n + 1)
    v = np.array([f(np.array(c) + rad * np.array([np.cos(t), np.sin(t)])) for t in th])
    return int(round(np.sum(np.angle(v[1:] / v[:-1])) / (2 * np.pi)))


corners = [(0, 0), (np.pi, 0), (0, np.pi), (np.pi, np.pi)]
fl = lambda p: bnd(p)[1, 0]     # light Weyl element (layer 0, P_-)
fm = lambda p: bnd(p)[0, 1]     # mirror element (layer Ls-1, P_+)
wl, wm = [wind(fl, c) for c in corners], [wind(fm, c) for c in corners]
al = [abs(fl(np.array(c) + 1e-3)) for c in corners]
check("A1", "THEOREM", sum(wl) == 0 and sum(wm) == 0 and wl[0] == -wm[0] and max(al[1:]) < 1e-3 < al[0],
      "argument principle on the zone torus: windings of a chiral propagator element sum to 0; the light end alone has its pole at p = 0 and zeros of opposite net chirality at the three doubler corners (kinematical zeros); the mirror element is the mirror image: the boundary field is one vector-like pair, as the generalized Nielsen-Ninomiya theorem demands",
      "windings (0,0),(pi,0),(0,pi),(pi,pi): light %s, mirror %s; |light| near corners %s" % (wl, wm, ["%.0e" % a for a in al]))
note("A2", "THEOREM", "which assumption fails: none of GS 2505.20436's (finite-range fermion-only H, unbroken G, free massless continuum, zero-free interpolating set); the gauge-off slab meets them and is vector-like (A1). GK evades only the corollary 'vector-like spectrum => vector-like gauge theory', which needs both ends to couple through the local current; the mirror reads a range-r functional A_* with f(0) = 1, so it is chiral only for 1/r << k << 1/a")

# ===================== B. the induced gauge-invariant mass term ============
print("== B. far layers that read A_* != A: Gamma gains c (A - A_*)^2, gauge invariant, unprotected")
P8 = layer_pi(4, 8, 16)
cuts8 = [w @ P8 @ w for w in [(np.arange(8) < j).astype(float) for j in range(1, 8)]]
ramps = [np.clip((4 + nr / 2 - np.arange(8) - 0.5) / nr, 0, 1) for nr in (1, 2, 4)]
rv = [w @ P8 @ w for w in ramps]
P16 = layer_pi(4, 16, 12)
c16 = (np.arange(16) < 8).astype(float) @ P16 @ (np.arange(16) < 8).astype(float)
P8b = layer_pi(4, 8, 12)
c8b = (np.arange(8) < 4).astype(float) @ P8b @ (np.arange(8) < 4).astype(float)
ward = max(np.abs(P8.sum(1)).max(), np.abs(P16.sum(1)).max())
cDW = cuts8[3]
check("B1", "DIAGNOSTIC", ward < 1e-3 and abs(cDW) > 0.01 and abs(c16 - c8b) < 1e-3 and np.ptp(cuts8[1:-1]) < 1e-3 and np.ptp(rv) < 2e-3 * 1 + 0.002,
      "4D Shamir slab (DW - PV), constant layer fields: Ward rows -> 0; near layers read A, far A_* = 0 (window k >> 1/r): a mass term c A^2 per q^2, the same for every cut position, ramp width and Ls: an end term, not a bulk F_s mu^2",
      "Ward max %.0e (N=16); c at cut j=1..7: %s; ramps n=1,2,4: %s; Ls=16 %.4f vs Ls=8 %.4f (N=12)"
      % (ward, np.round(cuts8, 4), np.round(rv, 4), c16, c8b))
G4, g54 = gammas(4)
pts = bz(4, 16)
e0 = sign_hw(pts, G4, g54)
h = 2e-3
gam = []
for a in (-h, 0.0, h):
    q = pts.copy()
    q[:, 0] += a
    gam.append(-np.mean(np.log(np.abs(np.linalg.det((np.eye(4) + sign_hw(q, G4, g54) @ e0) / 2)))))
cOV = (gam[0] - 2 * gam[1] + gam[2]) / h ** 2
q1, q2 = pts.copy(), pts.copy()
q1[:, 0] += 1e-4
q2[:, 0] -= 1e-4
dP = (sign_hw(q2, G4, g54) - sign_hw(q1, G4, g54)) / 4e-4     # d(P_-) with P_- = (1 - eps)/2
gq = 0.5 * np.real(np.einsum('bij,bji->b', dP, dP))
check("B2", "THEOREM", abs(cOV - 2 * gq.mean()) < 1e-4 and gq.mean() > 0.01,
      "overlap form (Ls -> inf): |det| = |<v(A)|v(A_*)>|^2 per momentum, so for A_* = 0 the mass coefficient is c = 2 <g_00>, the zone mean of the quantum metric of H_W's filled bands: positive, zero only if the filled projector is momentum independent (trivial bands, no light chiral mode): the topology that makes the light end chiral forces the mass",
      "c_overlap %.5f, 2<g> %.5f, min g %.0e" % (cOV, 2 * gq.mean(), gq.min()))
del e0, dP, pts
al_em = 1 / 137.036
e2 = 4 * np.pi * al_em
sq = 16.0   # sum Q^2 over three families of Weyl fields
mDW, mOV = np.sqrt(e2 * sq * abs(cDW)), np.sqrt(e2 * sq * cOV)
inv_a = 2.44e18   # GeV, hbar c / a with a = sqrt(8 pi) l_P
check("B3", "ESTIMATE", mOV * inv_a > 1e16,
      "window photon: Pi(k) = e^2 c sum Q^2 (1 - f(kr))^2 / a^2, a Planck-scale mass (tachyonic for Shamir) for all k > 1/r, so no electromagnetism below r (and r >> 1/m_e is needed); no local A^2 counterterm is gauge invariant; only a tuned -c(A - A_*)^2, to ~1e-90",
      "sum Q^2 = %.0f, alpha = 1/137: m_gamma a = %.2f (Shamir, m^2 < 0), %.2f (overlap) -> |m| = %.1e, %.1e GeV" % (sq, mDW, mOV, mDW * inv_a, mOV * inv_a))
c2 = None
p2 = bz(2, 512)
ea = sign_hw(p2, G2, g52)
gm2 = []
for a in (-h, 0.0, h):
    q = p2.copy()
    q[:, 0] += a
    gm2.append(-np.mean(np.log(np.abs(np.linalg.det((I2 + sign_hw(q, G2, g52) @ ea) / 2)))))
c2 = (gm2[0] - 2 * gm2[1] + gm2[2]) / h ** 2
note("B4", "DIAGNOSTIC", "2D: the same term is c2 = %.4f per q^2 (overlap), dimensionless: e^2 c2 sum q^2 is a fraction %.2f of the Weyl Schwinger-type term e^2 sum q^2/(2 pi): marginal, which is why the 2D toy (gk-smoothed-layers C2: smoothed/unsmoothed 0.26-0.33, not 1/2) passed; in 4D it is relevant (dimension 2, coefficient 1/a^2)" % (c2, 2 * np.pi * c2))

# ===================== C. scaling with the smoothing radius ================
print("== C. what scales with r (abelian; slab gauge invariance is exact at every r)")
Lx = 4096
xs = np.arange(Lx)
k = 2 * np.pi * 37 / Lx
F = np.cos(k * xs)
bs = [16, 64, 256, 1024]
leak = []
for b in bs:
    Fb = np.repeat(F.reshape(-1, b).mean(1), b)
    leak.append(np.linalg.norm(Fb) / np.linalg.norm(F))
env = np.array(leak) * np.array(bs) * k
fl_t = [(1 - 4 * 0.125 * np.sin(k / 2) ** 2) ** n for n in (400, 1600, 6400, 25600)]
check("C1", "THEOREM", np.all(env[2:] < 2.01) and leak[-1] < 0.05 and fl_t[-1] < 1e-3,
      "mirror's residual field-strength coupling at fixed k: block (box) reading |sin(kb/2)/(b sin(k/2))| <= 2/(kb), a power 1/r in amplitude (1/r^2 in the action); flow (1 - eps khat^2)^n, gaussian in r = sqrt(n); the induced mass c(1 - f)^2 grows to its full value instead: gauge non-invariance does not appear at any r, but the mass does not fall with r",
      "k = 2pi*37/4096, b=%s: leak %s, kb*leak %s; flow n=400..25600: %s" % (bs, np.round(leak, 3), np.round(env, 2), ["%.0e" % v for v in fl_t]))

# ===================== D. non-abelian block-flux spreading =================
print("== D. SU(2) on 8 x 8: rung-b spreading with anchor (comb-tree) transports")


def ex(v):
    a = np.linalg.norm(v)
    if a < 1e-300:
        return I2.copy()
    n = v / a
    return np.cos(a) * I2 + 1j * np.sin(a) * (n[0] * S1 + n[1] * S2 + n[2] * S3)


def lg(W):
    th = np.arccos(np.clip(np.real(np.trace(W)) / 2, -1, 1))
    v = np.array([np.imag(np.trace(W @ s)) / 2 for s in (S1, S2, S3)])
    sn = np.linalg.norm(v)
    return th * v / sn if sn > 1e-300 else np.zeros(3)


dg = lambda A: A.conj().T
L = 8
nxt = lambda x, y, mu: ((x + 1) % L, y) if mu == 0 else (x, (y + 1) % L)
plq = lambda U, x, y: U[0][x][y] @ U[1][(x + 1) % L][y] @ dg(U[0][x][(y + 1) % L]) @ dg(U[1][x][y])
ang = lambda M: np.arccos(np.clip(np.real(np.trace(M)) / 2, -1, 1))


def gauge_su2(U, g):
    return [[[g[x][y] @ U[mu][x][y] @ dg(g[nxt(x, y, mu)[0]][nxt(x, y, mu)[1]]) for y in range(L)]
             for x in range(L)] for mu in range(2)]


def spread(U, b):
    """each b x b block: tree frame from the anchor (down the column, then along
    the bottom row), block loop W from the top links, every plaquette's lasso set
    to X = W^(1/b^2) (principal root, conjugation covariant), boundary links
    untouched, interior links transported back."""
    V = [[[U[mu][x][y].copy() for y in range(L)] for x in range(L)] for mu in range(2)]
    clo = 0.0
    for X in range(0, L, b):
        for Y in range(0, L, b):
            phi = {}
            for i in range(b + 1):
                for j in range(b + 1):
                    m = I2.copy()
                    for jj in range(j, 0, -1):
                        m = m @ dg(U[1][(X + i) % L][(Y + jj - 1) % L])
                    for ii in range(i, 0, -1):
                        m = m @ dg(U[0][(X + ii - 1) % L][Y % L])
                    phi[(i, j)] = m
            T = [dg(phi[(i, b)]) @ U[0][(X + i) % L][(Y + b) % L] @ phi[(i + 1, b)] for i in range(b)]
            P = I2.copy()
            for t in T:
                P = P @ t
            Xr = ex(lg(dg(P)) / b ** 2)
            Vc = [I2.copy()]
            for i in range(b):
                Vc.append(np.linalg.matrix_power(Xr, b) @ Vc[-1] @ T[i])
            clo = max(clo, np.abs(Vc[b] - I2).max())
            for i in range(b):
                for kk in range(1, b):
                    V[0][(X + i) % L][(Y + kk) % L] = phi[(i, kk)] @ np.linalg.matrix_power(dg(Xr), kk) @ dg(phi[(i + 1, kk)])
            for i in range(1, b):
                for j in range(b):
                    V[1][(X + i) % L][(Y + j) % L] = phi[(i, j)] @ (Vc[i] if j == b - 1 else I2) @ dg(phi[(i, j + 1)])
    return V, clo


def proj(A):
    u, _, vh = np.linalg.svd(A)
    W = u @ vh
    return W / np.sqrt(np.linalg.det(W))


naive = lambda U: [[[proj(U[mu][x][y] + U[mu][x][(y + 1) % L] if mu == 0 else U[mu][x][y] + U[mu][(x + 1) % L][y])
                     for y in range(L)] for x in range(L)] for mu in range(2)]
U = [[[ex(0.5 * RNG.standard_normal(3)) for y in range(L)] for x in range(L)] for mu in range(2)]
g = [[ex(3.0 * RNG.standard_normal(3)) for y in range(L)] for x in range(L)]
dif = lambda A, B: max(np.abs(A[mu][x][y] - B[mu][x][y]).max() for mu in range(2) for x in range(L) for y in range(L))
cov, clos, unif, mx = {}, 0.0, 0.0, {}
for b in (2, 4):
    S, c0 = spread(U, b)
    cov[b] = dif(spread(gauge_su2(U, g), b)[0], gauge_su2(S, g))
    clos = max(clos, c0)
    for X in range(0, L, b):
        for Y in range(0, L, b):
            a = [ang(plq(S, x, y)) for x in range(X, X + b) for y in range(Y, Y + b)]
            unif = max(unif, max(a) - min(a))
    mx[b] = max(ang(plq(S, x, y)) for x in range(L) for y in range(L))
cnv = dif(naive(gauge_su2(U, g)), gauge_su2(naive(U), g))
mx0 = max(ang(plq(U, x, y)) for x in range(L) for y in range(L))
check("D1", "THEOREM", max(cov.values()) < 1e-12 and clos < 1e-12 and unif < 1e-12 and cnv > 0.1,
      "per-site covariance: the tree-frame links turn by the anchor's g(c) only, W^(1/b^2) is conjugation covariant, so spread[g.U] = g.spread[U]; the closure V_(X+b) = 1 holds exactly (X^(b^2) = W), every block plaquette becomes a conjugate of one X; link averaging without transports is not covariant",
      "rough field: residual b=2 %.0e, b=4 %.0e; closure %.0e; within-block angle spread %.0e; max plaquette angle %.2f -> %.2f (b=2), %.2f (b=4); naive %.2f"
      % (cov[2], cov[4], clos, unif, mx0, mx[2], mx[4], cnv))


def holo(U):
    Px, Py = I2.copy(), I2.copy()
    for x in range(L):
        Px = Px @ U[0][x][0]
    for y in range(L):
        Py = Py @ U[1][0][y]
    return Px, Py


tw = {}
for name in ("twisted", "vortex"):
    V0 = [[[ex(0.03 * RNG.standard_normal(3)) for y in range(L)] for x in range(L)] for mu in range(2)]
    if name == "twisted":   # twist eaters: P_x ~ i s1, P_y ~ i s2, commutator -1
        for y in range(L):
            V0[0][L - 1][y] = 1j * S1 @ V0[0][L - 1][y]
        for x in range(L):
            V0[1][x][L - 1] = 1j * S2 @ V0[1][x][L - 1]
    else:                   # commuting holonomies, a vortex pair joined by a sign string
        for y in range(2, 6):
            V0[0][2][y] = -V0[0][2][y]
    Sv, _ = spread(V0, 4)
    hb, ha = holo(V0), holo(Sv)
    com = lambda h: np.real(np.trace(h[0] @ h[1] @ dg(h[0]) @ dg(h[1]))) / 2
    tw[name] = (com(hb), com(ha), np.abs(hb[0] - ha[0]).max() + np.abs(hb[1] - ha[1]).max(),
                max(ang(plq(V0, x, y)) for x in range(L) for y in range(L)),
                max(ang(plq(Sv, x, y)) for x in range(L) for y in range(L)))
t, v = tw["twisted"], tw["vortex"]
check("D2", "THEOREM", t[2] < 1e-12 and v[2] < 1e-12 and t[0] < -0.9 and v[0] > 0.9 and t[4] < 0.4 and v[4] < 0.4,
      "topology in 2D SU(2): block loops and the torus holonomies along block-boundary lines are untouched, so the 't Hooft twist (commutator [P_x, P_y] = -1) is kept exactly while its thin plaquette is spread smooth; a thin vortex pair with commuting holonomies (twist +1) is spread likewise; the twist is never lost, unlike the abelian anchor reading's Q (gk-smoothed-layers A2)",
      "(1/2 tr[Px,Py] before, after, |dP|, max angle before, after): twisted (%.3f, %.3f, %.0e, %.2f, %.2f); vortex (%.3f, %.3f, %.0e, %.2f, %.2f)" % (t + v))

# ===================== E. does any rule fill the far layers? ===============
print("== E. 'mirror starts empty': 1+1D Hamiltonian slab (Chern strip, u = -1, N = 32, Ls = 8)")
N, Ls = 32, 8
n = N * Ls * 2
H = np.zeros((n, n), complex)
Tx, Ts = (S3 - 1j * S1) / 2, (S3 - 1j * S2) / 2
ix = lambda x, s: 2 * (x * Ls + s)
for x in range(N):
    for s in range(Ls):
        i = ix(x, s)
        H[i:i + 2, i:i + 2] += -1.0 * S3
        j = ix((x + 1) % N, s)
        bc = -1.0 if x == N - 1 else 1.0
        H[j:j + 2, i:i + 2] += bc * Tx
        H[i:i + 2, j:j + 2] += bc * dg(Tx)
        if s + 1 < Ls:
            j = ix(x, s + 1)
            H[j:j + 2, i:i + 2] += Ts
            H[i:i + 2, j:j + 2] += dg(Ts)
ev, V = np.linalg.eigh(H)
lay = np.sum(np.abs(V.reshape(N, Ls, 2, -1)) ** 2, axis=(0, 2))
near, far = lay[:Ls // 2].sum(0), lay[Ls // 2:].sum(0)
edge = np.abs(ev) < 0.9
qx = {}
for name, lys in (("layer-blind", range(Ls)), ("layer 0 only", [0])):
    dv = np.zeros(n)
    for x in range(N):
        for s in lys:
            dv[ix(x, s):ix(x, s) + 2] = 0.6 * (-1) ** x
    ei, Vi = np.linalg.eigh(H + np.diag(dv))
    Po = Vi[:, ei < 0]
    occ = np.sum(np.abs(V.conj().T @ Po) ** 2, axis=1)
    exq = np.where(ev > 0, occ, 1 - occ)
    qx[name] = ((exq * near * edge).sum(), (exq * far * edge).sum())
a, b_ = qx["layer-blind"], qx["layer 0 only"]
check("E1", "THEOREM", abs(a[0] - a[1]) < 1e-10 and a[1] > 0.1 and b_[1] < 1e-2 * b_[0],
      "inversion (x, s) -> (-x, Ls-1-s) with sigma_z is a symmetry of the slab exchanging the ends; a fold (period-2 order on every site) that ends suddenly respects it, so it fills light and mirror edge modes equally; only a rule that singles out the near layers fills the light end alone",
      "edge quanta (near, far): layer-blind (%.4f, %.4f); layer 0 only (%.4f, %.1e)" % (a + b_))
neff = 48 * (10.75 / 106.75) ** (4 / 3)
note("E2", "ESTIMATE", "the CL rules that make excitations are layer-blind (the fold, its misfolds on every layer of the role block, the split's flips), so reheating gives the mirror the SM temperature: Delta N_eff = %.2f vs Planck 2.99 +- 0.17 (%.0f sigma); allowed needs rho_mirror/rho_SM <~ 0.1, a lopsided reheating no rule supplies" % (neff, (neff + 3.044 - 2.99) / 0.17))
note("E3", "ESTIMATE", "after reheating: gravity Gamma/H ~ (T/M_P)^3 <= 1e-30; sphalerons give only the r-cell net winding (rho ratio ~1e-45 at 130 GeV, r = R_Earth); smoothed fields with E^2 > B^2 or E.B != 0 pair-make the massless mirror, so r must exceed every coherent field (r ~ c/H0 is safe)")
print("verdict: 2D toy survives; 3+1D route FAILS as stated (B: Planck-scale photon mass above 1/r) unless a tuned (A - A_*)^2 clause is added; it also needs lopsided reheating (E); D passes")
print("supplied: Shamir and overlap kernels, M = 1, Ls, grids, PV, profiles, SU(2) fields, Chern strip, measured inputs | %.1f s" % (time.time() - T0))
print("cited: gk-smoothed-layers, rung-dimension-chirality, fold-inflaton; Golterman-Shamir 2505.20436; Grabowska-Kaplan 1511.03649; Ago-Kikukawa 1911.10925")
print("TOTAL: PASS=%d FAIL=%d" % tuple(NP))
