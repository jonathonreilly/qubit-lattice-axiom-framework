AUDIT_INPUT_PATHS = ('docs/D4_ZOOM_FIXED_POINT_CHIRALITY_OVERLAP_INDEX_AND_DOMAIN_WALL_SLAB_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""d4-zoom-chirality: does chirality carry over to the D4 zoom fixed-point kernel?

D* = G*^-1, the free fixed point of the factor-2 D4 zoom (weights 1, 1/2, 1/8; d4-zoom-fixed-point-fermion), alpha = 1/2.
(1) Overlap/Luscher on D*: truncated, U(1)-gauged (constant fluxes, straight-line transporters) on a 648-site D4 torus;
GW, index = Q, charge-q indices, P_hat projector and locality. (2) Domain-wall slab with D* along an internal fifth
direction (Borici and Shamir forms): wall content, chirality, the Borici identity, W(F4) covariance, dim-6 of the light
mode vs a Z^4 Wilson control. (3) One-family 16 anomaly sums (exact and with measured indices); mirror structure.
Self-contained (numpy/scipy), seeded, no external files.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import itertools, time, warnings
from fractions import Fraction as Fr
import numpy as np
warnings.filterwarnings("ignore")
AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
rng = np.random.default_rng(20261026)
NP = NF = 0


def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))


# ---------------- lattice data, W(F4) with spinor representatives, gammas
s1 = np.array([[0, 1], [1, 0]]); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1, -1]); I2 = np.eye(2); Z2 = np.zeros((2, 2))
gm = np.array([np.block([[Z2, I2], [I2, Z2]])] + [np.block([[Z2, -1j * s], [1j * s, Z2]]) for s in (s1, s2, s3)])
g5 = gm[0] @ gm[1] @ gm[2] @ gm[3]; g5 = g5 / np.sqrt((g5 @ g5)[0, 0])
gv = lambda v: np.einsum('...m,mab->...ab', v, gm)
E4 = np.eye(4); rt = np.array([1., 1, 0, 0]); ut = rt / np.sqrt(2); Pp = (E4 + g5) / 2; Pm = (E4 - g5) / 2
gens = []; gS = []
for i in range(3):
    n = np.zeros(4); n[i], n[i + 1] = 1 / np.sqrt(2), -1 / np.sqrt(2); gens.append(E4 - 2 * np.outer(n, n)); gS.append(g5 @ gv(n))
n = np.zeros(4); n[0] = 1; gens.append(E4 - 2 * np.outer(n, n)); gS.append(g5 @ gv(n))
n = np.ones(4) / 2; gens.append(E4 - 2 * np.outer(n, n)); gS.append(g5 @ gv(n))
key = lambda A: tuple(np.round(2 * A).astype(int).ravel()); Dd = {key(E4): (E4, np.eye(4, dtype=complex))}; fr = [key(E4)]
while fr:
    nf = []
    for kk in fr:
        A, SA = Dd[kk]
        for g, sg in zip(gens, gS):
            B = g @ A
            if key(B) not in Dd: Dd[key(B)] = (B, sg @ SA); nf.append(key(B))
    fr = nf
GW4 = np.array([v[0] for v in Dd.values()]); SW = np.array([v[1] for v in Dd.values()]); DET = np.round(np.linalg.det(GW4)).astype(int)
def fq(c):  # f(q) from c_a = cos(q_a): (1 + sum_roots/2 cos + sum_S2/8 cos)/16, exact rewrite
    s = c.sum(-1); return (s * s - 0.5 * (c * c).sum(-1) + 2 * c.prod(-1)) / 16



# ---------------- fixed point by image sum
JL = 8


def Pi(q):
    out = np.ones(q.shape[:-1], dtype=q.dtype)
    for j in range(1, JL + 1): out = out * fq(np.cos(q / 2.0 ** j))
    q2 = np.sum(q * q, -1)
    return out * np.exp(-(9 / 32) * q2 / (3 * 4.0 ** JL) - (17 / 2048) * q2 ** 2 / (15 * 16.0 ** JL))


def chi(x, N):
    u = np.clip((x - (N - 2)) / 2.0, 0, 1); g = lambda t: np.where(t > 0, np.exp(-1 / np.maximum(t, 1e-300)), 0.)
    return g(1 - u) / (g(1 - u) + g(u))


IMC = {}


def images(N):
    if N not in IMC:
        a = np.array(list(itertools.product(range(-N - 1, N + 2), repeat=4)), float); L_ = np.vstack([a, a + 0.5]) * 2 * np.pi
        IMC[N] = L_[np.linalg.norm(L_, axis=1) <= 2 * np.pi * (N + 1)]   # |p| <= 2pi after folding
    return IMC[N]


def fold(p):
    x = p / (2 * np.pi); a = np.round(x); b = np.floor(x) + 0.5
    return p - 2 * np.pi * np.where((np.sum((x - a) ** 2, -1) <= np.sum((x - b) ** 2, -1))[:, None], a, b)


def Gstar(p, N=6, m=0.0, al=0.5):   # G* = sigma - i g.rho
    p = fold(np.atleast_2d(p)); IM = images(N); sig = np.zeros(len(p)); rho = np.zeros((len(p), 4)); st = max(1, 200000 // len(IM))
    for i in range(0, len(p), st):
        q = p[i:i + st, None, :] + IM[None]; q2 = np.sum(q * q, -1)
        w = Pi(q) ** 2 / (q2 + m * m) * chi(np.sqrt(q2) / (2 * np.pi), N)
        sig[i:i + st] = m * w.sum(1); rho[i:i + st] = np.einsum('pl,plm->pm', w, q)
    return sig + al, rho


Gm = lambda s, r: s[..., None, None] * E4 - 1j * gv(r)
Bm = np.array([[1, 1, 0, 0], [1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1]], float).T


def nearest_d4(y):
    f = np.round(y); d = y - f; odd = np.where(f.sum(1) % 2 != 0)[0]; j = np.argmax(np.abs(d), 1)
    f[odd, j[odd]] += np.where(d[odd, j[odd]] > 0, 1, -1); return f


def fill_G(L, m, al, N=6):  # direct G* on W(F4) orbit representatives, others by the group action
    m1 = np.arange(L); J = np.stack(np.meshgrid(m1, m1, m1, m1, indexing='ij'), -1).reshape(-1, 4)
    MA = [np.round(Bm.T @ A @ np.linalg.inv(Bm).T).astype(int) for A in GW4]; idx = lambda j: np.ravel_multi_index(tuple((j % L).T), (L,) * 4)
    lab = -np.ones(len(J), int); src = np.zeros(len(J), int); orb = []
    for i in range(len(J)):
        if lab[i] >= 0: continue
        im = idx(np.array([Mm @ J[i] for Mm in MA]))
        for g, t in enumerate(im):
            if lab[t] < 0: lab[t] = len(orb); src[t] = g
        orb.append(i)
    Pg = 2 * np.pi * J @ np.linalg.inv(Bm) / L; s0, r0 = Gstar(Pg[orb], N, m, al)
    return J, Pg, s0[lab], np.einsum('pab,pb->pa', GW4[src], r0[lab]), len(orb)


def kernel_x(L, al):
    J, Pg, sg, rh, no = fill_G(L, 0.0, al)
    den = sg ** 2 + np.sum(rh ** 2, 1); a = sg / den; b = rh / den[:, None]; z0 = np.all(J == 0, 1); a[z0] = 0; b[z0] = 0
    sh = (L,) * 4; ax = np.fft.ifftn(a.reshape(sh)).reshape(-1); bx = np.stack([np.fft.ifftn(b[:, k].reshape(sh)).reshape(-1) for k in range(4)], 1)
    X = J @ Bm.T; X = X - L * nearest_d4(X / L)
    return dict(J=J, a=a, b=b, z0=z0, X=X, ax=ax, bx=bx, n2=np.sum(X * X, 1), no=no)
SPN = max(np.abs(SW[i] @ gm[mu] @ np.linalg.inv(SW[i]) - np.einsum('n,nab->ab', GW4[i][:, mu], gm)).max() for i in range(1152) for mu in range(4))
AL = 0.5; M0 = 1 / (2 * AL); LT = 6; R2MAX = 8
print(f"setup: W(F4) {len(GW4)} elements ({(DET > 0).sum()} proper), spinor reps exact to {SPN:.0e}; alpha = {AL}, m0 = 1/(2 alpha) = {M0}")

# ================= 1 overlap / Luscher on the D4 fixed-point kernel
K = kernel_x(12, AL)


def Dstar(p, N=6):
    sg, rh = Gstar(p, N, 0.0, AL); return np.linalg.inv(Gm(sg, rh))


pr = rng.uniform(-2.5, 2.5, (40, 4)); Dx = Dstar(pr); tr_ = {}
for r2 in (4, 8):
    s_ = np.where(K['n2'] <= r2 + 1e-9)[0]; Kd_ = K['ax'][s_][:, None, None] * E4 + 1j * gv(K['bx'][s_])
    sym = np.einsum('pd,dab->pab', np.exp(-1j * pr @ K['X'][s_].T), Kd_)
    tr_[r2] = ((np.abs(sym - Dx).max(axis=(1, 2)) / np.abs(Dx).max(axis=(1, 2))).max(), np.linalg.svd(sym - M0 * E4, compute_uv=False).min() / M0, len(s_))
sel = np.where(K['n2'] <= R2MAX + 1e-9)[0]; HOP = -K['X'][sel]; KD = K['ax'][sel][:, None, None] * E4 + 1j * gv(K['bx'][sel])
check("1a truncated D4 fixed-point kernel (W(F4)-complete shells |d|^2 <= 8, 169 hops) matches D*(p); A = D_R - m0 is far from 0",
      tr_[8][0] < 5e-2 and tr_[8][1] > 0.3, f"symbol err {tr_[8][0]:.1e}, min sv(A)/m0 {tr_[8][1]:.2f}; [pre-reg shells |d|^2 <= 4 MISS: err {tr_[4][0]:.2f}, sv {tr_[4][1]:.2f}]")
SITES = np.array([x for x in itertools.product(range(LT), repeat=4) if sum(x) % 2 == 0], float)
SID = {tuple(map(int, x)): i for i, x in enumerate(SITES)}; NS = len(SITES); DG = np.arange(4 * NS)
g5L = lambda M: np.einsum('ab,ibj->iaj', g5, M.reshape(NS, 4, -1)).reshape(M.shape)          # (1 x g5) M without dense 1 x g5
g5R = lambda M: np.einsum('ijb,ba->ija', M.reshape(-1, NS, 4), g5).reshape(M.shape)


def H_bg(n12, n34, q=1):   # g5 (D_R[U] - m0), constant U(1) flux, Landau gauge, straight-line transporters, twisted torus
    f12 = q * 2 * np.pi * n12 / LT ** 2; f34 = q * 2 * np.pi * n34 / LT ** 2; Dm = np.zeros((NS, 4, NS, 4), complex)
    for d, Kd in zip(HOP, KD):
        Y = SITES + d; nn = np.floor(Y / LT); XJ = Y - LT * nn; j = np.array([SID[tuple(map(int, y))] for y in XJ])
        ph = f12 * d[1] * (SITES[:, 0] + d[0] / 2) + f34 * d[3] * (SITES[:, 2] + d[2] / 2) - LT * (f12 * nn[:, 0] * XJ[:, 1] + f34 * nn[:, 2] * XJ[:, 3])
        Dm[np.arange(NS), :, j, :] += np.exp(1j * ph)[:, None, None] * Kd[None]
    Dm = Dm.reshape(4 * NS, 4 * NS); Dm[DG, DG] -= M0; return g5L(Dm)


IDX = {}; herm = 0; adm = {}
for bg in ((0, 0, 1), (1, 1, 1), (1, -1, 1), (2, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 1, 6)):
    H = H_bg(*bg); herm = max(herm, np.abs(H - H.conj().T).max()); H += H.conj().T; H *= 0.5; ev = np.linalg.eigvalsh(H)
    IDX[bg] = -0.5 * np.sign(ev).sum(); adm[bg] = np.abs(ev).min() / M0
    if bg == (1, 1, 1): H1 = H
    del H
Qs = {(0, 0, 1): 0, (1, 1, 1): 1, (1, -1, 1): -1, (2, 1, 1): 2}
ok_i = all(abs(IDX[b] + Q) < 1e-9 for b, Q in Qs.items()); ok_q = all(abs(IDX[(1, 1, q)] + q * q) < 1e-9 for q in (2, 3, 4, 6))
check("1b gauged H = g5 (D_R - m0) is Hermitian on the twisted 648-site D4 torus (transition functions consistent)", herm < 1e-12, f"{herm:.0e}")
check("1c overlap index := -(1/2) Tr sign(H) = -Q exactly (one fixed sign convention) for Q = 0, 1, -1, 2; charge-q field in Q = 1: index = -q^2 (q = 2, 3, 4, 6)",
      ok_i and ok_q and min(adm.values()) >= 0.05,
      " ".join(f"{b[0]}{b[1]}q{b[2]}:{IDX[b]:+.0f}" for b in IDX) + "; min|eig H|/m0: " + " ".join(f"{adm[b]:.2f}" for b in IDX))
X = H1 / M0; del H1
for it in range(10):
    X2 = X @ X; X2[DG, DG] -= 1; nse = np.abs(X2).max()
    if nse < 1e-12: break
    X2[DG, DG] -= 2; X = -0.5 * X @ X2                                        # Newton-Schulz: X (3 - X^2)/2
del X2
Dov = M0 * g5L(X); Dov[DG, DG] += M0; del X                                  # D_ov = m0 (1 + g5 sign(H))
T = g5L(Dov); W = Dov @ T; W *= -2 * AL; W += T; W += g5R(Dov); gw = np.abs(W).max(); del W, T
g5h = np.abs(g5L(g5R(Dov)) - Dov.conj().T).max()
gh5 = -2 * AL * Dov; gh5[DG, DG] += 1; del Dov; gh5 = g5L(gh5); trg = np.trace(gh5).real
Ph = -0.5 * gh5; Ph[DG, DG] += 0.5; W = Ph @ Ph; W -= Ph; prj = np.abs(W).max(); del W, Ph
Em = np.abs(gh5.reshape(NS, 4, NS, 4)).max(axis=(1, 3)); del gh5
dx = SITES[None] - SITES[:, None]; dx = dx - LT * np.round(dx / LT); dist = np.sqrt((dx ** 2).sum(-1))
ds = np.unique(np.round(dist, 6)); mx = np.array([Em[np.abs(dist - d) < 1e-6].max() for d in ds]); fs = (ds > 1) & (ds < 4.3)
rate = -np.polyfit(ds[fs], np.log(mx[fs]), 1)[0]
check("1d Q = 1: GW exact, g5-hermitian; Luscher P_hat = (1 - g5_hat)/2 is a projector, Tr g5_hat = 2 index; g5_hat exponentially local",
      gw < 1e-10 and g5h < 1e-10 and prj < 1e-10 and abs(trg + 2) < 1e-8 and rate > 0.5,
      f"sign(H) Newton {it} its ({nse:.0e}); GW {gw:.0e}; g5h {g5h:.0e}; P^2-P {prj:.0e}; Tr {trg:.4f}; |g5_hat(x,y)| max at |x-y| = 1.41, 2.83, 4.0: "
      f"{mx[np.argmin(abs(ds - 1.414))]:.1e}, {mx[np.argmin(abs(ds - 2.828))]:.1e}, {mx[np.argmin(abs(ds - 4))]:.1e}; rate {rate:.2f}/unit")
print(f"  [t = {time.time() - T0:.0f} s]")

# ================= 2 domain-wall slab: D* along an internal fifth direction
def D5(Ak, Ls, mf, b, c):   # Moebius slab: (b A + 1) delta + (c A - 1)(P- delta_{s,s'-1} + P+ delta_{s,s'+1}); walls joined by -mf
    Mx = np.zeros((Ls, 4, Ls, 4), complex); hop = c * Ak - E4
    for s in range(Ls):
        Mx[s, :, s] = b * Ak + E4
        Mx[s, :, (s + 1) % Ls] += (1 if s + 1 < Ls else -mf) * hop @ Pm
        Mx[s, :, (s - 1) % Ls] += (1 if s >= 1 else -mf) * hop @ Pp
    return Mx.reshape(4 * Ls, 4 * Ls)


def Deff(Ak, Ls, mf, b, c):   # 4D operator of the wall fields q = P- psi_1 + P+ psi_Ls (Pauli-Villars mf = 1)
    Pr = np.zeros((Ls, 4, Ls, 4), complex)
    for s in range(Ls): Pr[s, :, s] = Pm; Pr[s, :, (s + 1) % Ls] = Pp
    Pr = Pr.reshape(4 * Ls, 4 * Ls); return (np.linalg.inv(Pr) @ np.linalg.solve(D5(Ak, Ls, 1.0, b, c), D5(Ak, Ls, mf, b, c)) @ Pr)[:4, :4]


FORMS = (("Borici", .5, .5), ("Shamir", 1., 0.)); LS = 8
cnt = {}; wall = {}
for nm, b, c in FORMS:
    U, sv, Vh = np.linalg.svd(D5(-M0 * E4, LS, 0.0, b, c)); vz = Vh[sv < 1e-2].conj(); info = []
    G5L = np.kron(np.eye(LS), g5); cg, cv = np.linalg.eigh(vz.conj() @ G5L @ vz.T); vz = (vz.T @ cv).T   # chirality basis of the null space
    for v, ch in zip(vz, cg):
        w = (np.abs(v.reshape(LS, 4)) ** 2).sum(1); info.append((0 if w[:LS // 2].sum() > 0.5 else 1, max(w[:LS // 2].sum(), w[LS // 2:].sum()), ch))
    cnt[nm] = (len(vz), sorted(set((i[0], round(i[2])) for i in info)), min(i[1] for i in info), min(abs(i[2]) for i in info), sv[sv >= 1e-2].min())
dbl = np.array([v for v in itertools.product([0, 1], repeat=4)] + [np.array(v) + .5 for v in itertools.product([0, 1], repeat=4)], float)[1:] * np.pi
dbl = dbl[np.abs(dbl - np.pi).sum(1) > 1e-9]                  # drop the class of 0 (2pi D4*)
Dd_ = Dstar(dbl); dmin = min(np.linalg.svd(D5(Dk - M0 * E4, LS, 0.0, b, c), compute_uv=False).min() for Dk in Dd_ for nm, b, c in FORMS)
ok = all(cnt[nm][0] == 4 and cnt[nm][1] == [(0, -1), (1, 1)] and cnt[nm][2] > 0.99 and cnt[nm][3] > 0.99 for nm in cnt) and dmin > 0.1
check("2a slab (Ls = 8), p = 0: exactly one 2-component Weyl per wall, g5 = -1 on wall 1 and +1 on wall Ls (mirror on the far wall); no light modes at the 15 classes (30 points) of pi D4* \\ 2pi D4*",
      ok, "; ".join(f"{nm}: {v[0]} null vectors, (wall, g5) {v[1]}, half-slab weight >= {v[2]:.4f}, |g5| >= {v[3]:.3f}, next sv {v[4]:.2f}" for nm, v in cnt.items())
      + f"; corner min sv {dmin:.2f} [pre-reg said '2 singular values': the Weyl pair is 2 + 2 = 4 components]")


def eps_f(H, Ls):
    w, v = np.linalg.eigh((H + H.conj().T) / 2); return v @ np.diag(((1 + w) ** Ls - (1 - w) ** Ls) / ((1 + w) ** Ls + (1 - w) ** Ls)) @ v.conj().T


pb = rng.uniform(-2.5, 2.5, (6, 4)); Db = Dstar(pb); e_mob = e_bor = hsq = 0
for Dk in Db:
    Ak = Dk - M0 * E4
    for nm, b, c in FORMS:
        Hk = g5 @ ((b + c) * Ak) @ np.linalg.inv(2 * E4 + (b - c) * Ak)
        for Ls in (4, 8):
            for mf in (0.0, 0.1): e_mob = max(e_mob, np.abs(Deff(Ak, Ls, mf, b, c) - ((1 + mf) / 2 * E4 + (1 - mf) / 2 * g5 @ eps_f(Hk, Ls))).max())
    hsq = max(hsq, np.abs((g5 @ Ak) @ (g5 @ Ak) - M0 ** 2 * E4).max())
    for Ls in (2, 4, 8, 16):
        hh = M0 / 2; tL = ((1 + hh) ** Ls - (1 - hh) ** Ls) / ((1 + hh) ** Ls + (1 - hh) ** Ls)
        e_bor = max(e_bor, np.abs(Deff(Ak, Ls, 0.0, .5, .5) - ((1 - tL) / 2 * E4 + tL * AL * Dk)).max())
check("2b Borici slab: H_T = g5 A/2 with (g5 A)^2 = m0^2 exactly (GW circle), so D_eff(Ls) = (1 - t)/2 + t alpha D* at every Ls: the light mode is D* plus a momentum-independent residual mass",
      e_mob < 1e-10 and e_bor < 1e-10 and hsq < 1e-12,
      f"(g5 A)^2 - m0^2: {hsq:.0e}; 5D Schur complement vs Moebius formula {e_mob:.0e}; Borici identity {e_bor:.0e} (Ls = 2..16); residual mass (1-t)/t = {2 / (3 ** 8 - 1):.1e} at Ls = 8")
pc = rng.uniform(-2, 2, (2, 4)); Ap = np.einsum('gij,pj->gpi', GW4, pc).reshape(-1, 4); DA = Dstar(Ap).reshape(1152, 2, 4, 4); D0 = Dstar(pc)
J = np.kron(np.eye(LS)[::-1], E4); cpr = cim = 0
for gI in range(1152):
    Sb = np.kron(np.eye(LS), SW[gI]); Si = np.linalg.inv(Sb)
    for k in range(2):
        for nm, b, c in FORMS:
            lhs = D5(DA[gI, k] - M0 * E4, LS, 0.1, b, c); rhs = Sb @ D5(D0[k] - M0 * E4, LS, 0.1, b, c) @ Si
            if DET[gI] > 0: cpr = max(cpr, np.abs(lhs - rhs).max())
            else: cim = max(cim, np.abs(lhs - J @ rhs @ J).max())
check("2c the slab keeps W(F4): all 576 rotations act on spinors only (D5(Ap) = S D5(p) S^-1); the 576 reflections map it to the wall-swapped slab",
      cpr < 1e-10 and cim < 1e-10, f"rotations {cpr:.0e}; reflections x (s -> Ls+1-s) {cim:.0e}; both forms, mf = 0.1")


def hk(ev, k): return np.real(np.sum([np.prod(ev[list(c)]) for c in itertools.combinations_with_replacement(range(4), k)]))


B4 = np.array([np.diag(s) @ np.eye(4)[list(pm)] for pm in itertools.permutations(range(4)) for s in itertools.product([1, -1], repeat=4)])
def counts(G):
    ev = [np.linalg.eigvals(g) for g in G]; tr = np.array([np.trace(g) for g in G])
    return tuple(int(round(np.mean([hk(e, k) * (t if v else 1) for e, t in zip(ev, tr)]))) for k, v in ((4, 0), (3, 1), (6, 0), (5, 1)))


cW = counts(GW4[DET > 0]); cB = counts(B4[np.round(np.linalg.det(B4)) > 0])


def wilson(p): return 1j * gv(np.sin(p)) + np.sum(1 - np.cos(p)) * E4


DIRS = np.array([[1, 0, 0, 0], [1, 1, 0, 0], [2, 1, 1, 0], [1, 1, 1, 1], [.3, .5, .81, -.2]], float); DIRS /= np.linalg.norm(DIRS, axis=1)[:, None]
EPS = np.array([0.2, 0.3, 0.45])


def light(kern, mode):   # anisotropy of the light wall mode's vector part b(eps n)/eps over directions n
    an = []; rem = 0
    for e in EPS:
        g = []
        for n_ in DIRS:
            Dk = kern(e * n_); Ak = Dk - M0 * E4
            if mode == "inf":
                H = g5 @ Ak @ np.linalg.inv(2 * E4 + Ak); w, v = np.linalg.eigh((H + H.conj().T) / 2); Df = (E4 + g5 @ v @ np.diag(np.sign(w)) @ v.conj().T) / 2
            else: Df = Deff(Ak, LS, 0.0, *mode)
            a = np.trace(Df).real / 4; bb = np.array([np.trace(gm[mu] @ Df) / 4j for mu in range(4)]).real; rem = max(rem, np.abs(Df - a * E4 - 1j * gv(bb)).max())
            g.append((bb @ n_ / e, np.linalg.norm(bb - (bb @ n_) * n_) / e))
        g = np.array(g); an.append(max(np.ptp(g[:, 0]), g[:, 1].max()) / abs(g[:, 0].mean()))
    return np.polyfit(np.log(EPS), np.log(an), 1)[0], an, rem


res = {}
for kn, kern in (("D4", lambda p: Dstar(p[None])[0]), ("Z4", wilson)):
    for mn, mode in (("Bor8", (.5, .5)), ("Sha8", (1., 0.)), ("ShaInf", "inf")): res[(kn, mn)] = light(kern, mode)
okd = all(res[("D4", m)][0] >= 3.5 for m in ("Bor8", "Sha8", "ShaInf")) and all(res[("Z4", m)][0] <= 2.5 for m in ("Bor8", "Sha8", "ShaInf"))
c2 = max(res[("D4", m)][1][0] / EPS[0] ** 2 for m in ("Bor8", "Sha8", "ShaInf")); c2z = min(res[("Z4", m)][1][0] / EPS[0] ** 2 for m in ("Bor8", "Sha8", "ShaInf"))
check("2d dim 6 of the light chiral mode: its kernel's direction anisotropy has no eps^2 term on D4 (Borici, Shamir Ls = 8, Shamir Ls -> inf); Z^4 Wilson slab control has it",
      okd and cW == (1, 1, 2, 2) and cB[:2] == (2, 2), " ".join(f"{k[0]}-{k[1]} exp {v[0]:.2f}" for k, v in res.items())
      + f"; anisotropy at eps = 0.2: D4 <= {max(res[('D4', m)][1][0] for m in ('Bor8', 'Sha8', 'ShaInf')):.0e}, Z4 >= {min(res[('Z4', m)][1][0] for m in ('Bor8', 'Sha8', 'ShaInf')):.0e}"
      f"; dim-6 coefficient bound D4 {c2:.0e} vs Z4 {c2z:.2f}; W(F4)+ invariants (quartic, cubic-vector, sextic, quintic-vector) = {cW}, B4+ = {cB}")
print(f"  [t = {time.time() - T0:.0f} s]")

# ================= 3 anomaly content and the mirror
F16 = [("Q", 6, Fr(1, 6), 2, 2), ("u^c", 3, Fr(-2, 3), -1, 0), ("d^c", 3, Fr(1, 3), -1, 0), ("L", 2, Fr(-1, 2), 0, 1), ("e^c", 1, Fr(1), 0, 0), ("nu^c", 1, Fr(0), 0, 0)]
Y3 = sum(m * y ** 3 for _, m, y, _, _ in F16); Y1 = sum(m * y for _, m, y, _, _ in F16)
C2Y = sum((m // 3) * y for nm, m, y, a3, _ in F16 if a3 != 0); W2Y = sum((m // 2) * y for nm, m, y, _, d in F16 if d)
C3 = sum((m // 3) * (1 if a3 > 0 else -1) for nm, m, y, a3, _ in F16 if a3 != 0); ND = sum(m // 2 for nm, m, y, _, d in F16 if d)
ind = lambda q: 0 if q == 0 else IDX[(1, 1, abs(int(q)))]
lat = sum(m * int(6 * y) * ind(6 * y) for _, m, y, _, _ in F16); latL = 2 * (-3) * ind(-3); latQ = 6 * 1 * ind(1)
check("3a one-family 16 (left-handed Weyls): Y^3, Y-gravity, SU(3)^2 Y, SU(2)^2 Y, SU(3)^3 vanish, doublets even; with the MEASURED D4 indices sum (6Y) index(6Y) = 0",
      Y3 == 0 and Y1 == 0 and C2Y == 0 and W2Y == 0 and C3 == 0 and ND % 2 == 0 and lat == 0 and latL != 0,
      f"sums {Y3}, {Y1}, {C2Y}, {W2Y}, {C3}; doublets {ND}; lattice sum {lat} (from indices {[int(ind(q)) for q in (1, 2, 3, 4, 6)]}); lone L gives {latL:.0f}, lone Q {latQ:.0f}")
tw = [i for i in range(1152) if DET[i] > 0 and np.allclose(GW4[i] @ ut, ut) and np.allclose(np.linalg.matrix_power(GW4[i], 3), E4) and not np.allclose(GW4[i], E4)]
sp = []
for i in tw[:4]:
    S_ = SW[i]; bm = np.linalg.eigh(Pm)[1][:, 2:]; bp = np.linalg.eigh(Pp)[1][:, 2:]
    sp.append((np.sort_complex(np.round(np.linalg.eigvals(bm.conj().T @ S_ @ bm), 9)), np.sort_complex(np.round(np.linalg.eigvals(bp.conj().T @ S_ @ bp), 9))))
okm = len(tw) > 0 and all(np.allclose(a, b) for a, b in sp)
check("3b mirror unchanged: the far-wall Weyl carries the light Weyl's charges (the slab acts identically on every gauge label) and the same turn spectrum under every spatial 3-fold turn of the root slice: q_mirror = q_light",
      okm, f"{len(tw)} three-fold turns fixing the root; spectra on P- / P+: {np.round(sp[0][0], 3)} / {np.round(sp[0][1], 3)}; the slab is vector-like, the far wall still needs gapping")
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
