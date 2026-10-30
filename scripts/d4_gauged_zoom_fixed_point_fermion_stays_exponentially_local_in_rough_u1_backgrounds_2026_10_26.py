AUDIT_INPUT_PATHS = ('docs/D4_GAUGED_ZOOM_FIXED_POINT_FERMION_STAYS_EXPONENTIALLY_LOCAL_IN_ROUGH_U1_BACKGROUNDS_GW_AND_INDEX_ONLY_IN_THE_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""d4-gauged-fixed-point-locality: does the D4 zoom fixed-point fermion stay exponentially local in U(1) backgrounds?

Gauged zoom (gauge-covariant blocking, classically-perfect-action style: Hasenfratz-Niedermayer / Bietenholz-Wiese,
supplied): G_{l+1} - alpha = 8 B_l (G_l - alpha) B_l^dag, B_l(X,x) = (1/16) w(x-2X) T(2X->x), w = 1, 1/2, 1/8 (the forced
W(F4) kernel of the free D4 fixed point), T = straight-line transporter of a continuum U(1) background A (constant flux Q
with twisted transition functions + periodic Fourier modes). Seed: the NN D4 Wilson start, gauged by the same A, on a
2^n-finer D4 torus. D_n = G_n^-1 by Woodbury (fine GMRES solves; no dense fine matrix). alpha = 1/2.
Checks: free limit = momentum-space R^n exactly; gauge covariance; g5-hermiticity; locality rate vs roughness
(max coarse triangle-plaquette deviation eps, from 1/30 = the HJL admissibility bound up to 1.9); GW residual and
convergence in n = 1, 2, 3; overlap index of D_n = -Q. Self-contained (numpy/scipy), seeded, no external files.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import itertools, time, warnings
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl
import scipy.linalg as sla
warnings.filterwarnings("ignore")
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0
rng = np.random.default_rng(20261026)


def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))


s1 = np.array([[0, 1], [1, 0]]); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1, -1]); I2 = np.eye(2); Z2 = np.zeros((2, 2))
gm = np.array([np.block([[Z2, I2], [I2, Z2]])] + [np.block([[Z2, -1j * s], [1j * s, Z2]]) for s in (s1, s2, s3)])
g5 = gm[0] @ gm[1] @ gm[2] @ gm[3]; g5 = g5 / np.sqrt((g5 @ g5)[0, 0])
gv = lambda v: np.einsum('...m,mab->...ab', v, gm)
E4 = np.eye(4)
ROOTS = np.array([v for v in itertools.product([-1, 0, 1], repeat=4) if sum(abs(x) for x in v) == 2], float)
N4 = np.array([v for v in itertools.product([-2, -1, 0, 1, 2], repeat=4) if sum(x * x for x in v) == 4 and sum(v) % 2 == 0], float)
WE = [(np.zeros(4), 1.0)] + [(r, 0.5) for r in ROOTS] + [(v, 0.125) for v in N4]
AL = 0.5


def fq(c):
    s = c.sum(-1); return (s * s - 0.5 * (c * c).sum(-1) + 2 * c.prod(-1)) / 16


class Field:
    """continuum U(1) background on the coarse torus box Lc (coarse units): constant flux (n12, n34) + periodic modes + gauge"""
    def __init__(self, Lc, n12=0, n34=0, modes=None, scale=0.0, lam=None):
        self.Lc = Lc; self.f12 = 2 * np.pi * n12 / Lc ** 2; self.f34 = 2 * np.pi * n34 / Lc ** 2
        self.modes = modes; self.scale = scale; self.lam = lam

    def phase(self, a, d):   # straight-line integral from a (in box) to a + d, endpoint transition; coarse units
        L = self.Lc; Y = a + d; nn = np.floor(Y / L + 1e-9); Yw = Y - L * nn
        ph = self.f12 * d[1] * (a[:, 0] + d[0] / 2) + self.f34 * d[3] * (a[:, 2] + d[2] / 2) - L * (self.f12 * nn[:, 0] * Yw[:, 1] + self.f34 * nn[:, 2] * Yw[:, 3])
        if self.modes is not None and self.scale != 0:
            K, C, P = self.modes; kd = K @ d; cd = C @ d; ka = a @ K.T + P; sm = np.abs(kd) > 1e-12
            I = np.where(sm, (np.sin(ka + kd) - np.sin(ka)) / np.where(sm, kd, 1), np.cos(ka))
            ph = ph + self.scale * (I @ cd)
        if self.lam is not None:
            l0, kg, pg = self.lam; ph = ph + l0 * (np.cos(Y @ kg + pg) - np.cos(a @ kg + pg))
        return ph


class Level:
    def __init__(self, Lb):
        self.Lb = Lb; S = np.array([x for x in itertools.product(range(Lb), repeat=4) if sum(x) % 2 == 0], float)
        self.S = S; self.N = len(S); self.idx = -np.ones((Lb,) * 4, int)
        self.idx[tuple(S.astype(int).T)] = np.arange(self.N)

    def look(self, Y):
        return self.idx[tuple((np.round(Y).astype(int) % self.Lb).T)]


def triangles():
    T = []
    for r1 in ROOTS:
        for r2 in ROOTS:
            s = r1 + r2
            if np.sum(s * s) == 2: T.append((r1, r2))
    return T
TRI = triangles()


HOPS = [(r, -E4 / 12 + gv(r) / 12) for r in ROOTS]


def D_nn(F, lev, unit):   # NN D4 Wilson start, straight-line U(1) links: 2 + sum_r U_r (x) (-1/12 + g.r/12)
    P = lev.S * unit; N = lev.N; base = 4 * np.arange(N, dtype=np.int32)
    ent = [(a, b) for r, H in HOPS for a in range(4) for b in range(4) if H[a, b] != 0]; nnz = 4 * N + len(ent) * N
    R_ = np.empty(nnz, np.int32); C_ = np.empty(nnz, np.int32); V_ = np.empty(nnz, complex); k = 0
    for a in range(4): R_[k:k + N] = base + a; C_[k:k + N] = base + a; V_[k:k + N] = 2.0; k += N
    for r, H in HOPS:
        j = 4 * lev.look(lev.S + r).astype(np.int32); e = np.exp(1j * F.phase(P, r * unit))
        for a in range(4):
            for b in range(4):
                if H[a, b] != 0: R_[k:k + N] = base + a; C_[k:k + N] = j + b; V_[k:k + N] = e * H[a, b]; k += N
    D = sp.csr_matrix((V_, (R_, C_)), shape=(4 * N, 4 * N)); del R_, C_, V_; return D


def Bmat(F, fine, coarse, ufine):   # coarse site X (level coords) at fine-level coords 2X; unit = coarse-units per fine-level step
    rows = []; cols = []; vals = []; P = coarse.S * 2 * ufine; base = 4 * np.arange(coarse.N)
    for e, w in WE:
        j = fine.look(2 * coarse.S + e); ph = np.exp(1j * F.phase(P, e * ufine)) * w / 16
        for a in range(4): rows.append(base + a); cols.append(4 * j + a); vals.append(ph)
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(4 * coarse.N, 4 * fine.N))


class Blocked:
    def __init__(self, F, n):
        Lc = F.Lc; self.n = n; self.levs = [Level(Lc * 2 ** (n - l)) for l in range(n + 1)]
        self.units = [2.0 ** (l - n) for l in range(n + 1)]
        self.D0 = D_nn(F, self.levs[0], self.units[0])
        Bt = None
        for l in range(n):
            B = Bmat(F, self.levs[l], self.levs[l + 1], self.units[l]); Bt = B if Bt is None else B @ Bt
        self.BB = Bt.tocsr(); self.c = 8.0 ** n
        Nc = self.BB.shape[0]; K = (self.BB @ self.BB.conj().T).toarray(); K *= -self.c * AL; K[np.diag_indices(Nc)] += AL
        self.cf = sla.cho_factor(K, overwrite_a=True, check_finite=False); self.Nc = Nc; del K

    def full(self):   # small fine lattices: direct
        return self.apply(np.eye(self.Nc, dtype=complex))[0]

    def apply(self, E, tol=1e-10):   # D_n E for coarse vectors E (Nc x k), iterative fine solves
        Ki = lambda x: sla.cho_solve(self.cf, x, check_finite=False)
        Bh = self.BB.conj().T.tocsr(); KE = Ki(E); BK = self.BB; c = self.c; D0 = self.D0
        Mop = spl.LinearOperator(D0.shape, matvec=lambda x: D0 @ x + c * (Bh @ Ki(BK @ x)), dtype=complex)
        out = np.zeros_like(KE); its = []
        for k in range(E.shape[1]):
            rhs = Bh @ KE[:, k]; cnt = [0]
            x, info = spl.gmres(Mop, rhs, rtol=tol, atol=0, restart=60, maxiter=40, callback=lambda r: cnt.__setitem__(0, cnt[0] + 1), callback_type='pr_norm')
            its.append(cnt[0]); out[:, k] = KE[:, k] - c * Ki(BK @ x)
        return out, its


def tri_phases(F, lev, unit):   # per-triangle holonomy phases, concatenated
    out = []; P = lev.S * unit; L = F.Lc
    for r1, r2 in TRI:
        ph = F.phase(P, r1 * unit); A2 = (P + r1 * unit) - L * np.floor((P + r1 * unit) / L + 1e-9)
        ph = ph + F.phase(A2, r2 * unit); A3 = (A2 + r2 * unit) - L * np.floor((A2 + r2 * unit) / L + 1e-9)
        out.append(ph + F.phase(A3, -(r1 + r2) * unit))
    return np.concatenate(out)


def tune(Lc, n12, n34, modes, eps):   # scale s with max |1 - U_p| = eps on the coarse triangles (phases linear in s)
    lev = Level(Lc); p0 = tri_phases(Field(Lc, n12, n34), lev, 1.0); p1 = tri_phases(Field(Lc, 0, 0, modes, 1.0), lev, 1.0)
    dev = lambda s: np.abs(1 - np.exp(1j * (p0 + s * p1))).max()
    if dev(0) >= eps: return 0.0
    lo, hi = 0.0, 1e-3
    while dev(hi) < eps: lo, hi = hi, hi * 1.5
    for _ in range(50):
        mid = (lo + hi) / 2
        if dev(mid) < eps: lo = mid
        else: hi = mid
    return lo


def modes_band(rng, Lc, mmax, nm):
    K = []
    while len(K) < nm:
        m = rng.integers(-mmax, mmax + 1, 4)
        if np.any(m != 0): K.append(2 * np.pi * m / Lc)
    return np.array(K), rng.normal(size=(nm, 4)), rng.uniform(0, 2 * np.pi, nm)


def locality(col, S, Lc, src=0, rmax=None):
    dX = S - S[src]; dX -= Lc * np.round(dX / Lc); dist = np.sqrt((dX ** 2).sum(1)); nr = np.sqrt((np.abs(col) ** 2).sum((1, 2)))
    ds = np.unique(np.round(dist, 6)); env = np.array([nr[dist >= d - 1e-6].max() for d in ds])
    rmax = rmax or Lc * 0.75 + 0.1; sel = (ds > 1.3) & (ds < rmax); rate = -np.polyfit(ds[sel], np.log(env[sel]), 1)[0]
    return rate, ds, env


# ---------------- momentum-space reference: the free #10098 map R^n(G_NN) on the torus momenta
a2 = np.array(list(itertools.product(range(2), repeat=4)), float); REPS = []
for c in np.vstack([a2, a2 + .5]):
    if not any((lambda d: np.allclose(d, np.round(d)) or np.allclose(d - np.floor(d), .5))((c - r) / 2) for r in REPS): REPS.append(c)
REPS = np.array(REPS) * 2 * np.pi


def G_rung(q, n):
    if n == 0:
        A = 2 - np.cos(q @ ROOTS.T).sum(-1) / 12; B = np.sin(q @ ROOTS.T) @ ROOTS / 12; d = A * A + np.sum(B * B, -1)
        with np.errstate(all='ignore'): return A / d, B / d[..., None]
    s = 0; r = 0; sf = 0
    for lk in REPS:
        Q = (q + lk) / 2; f2 = fq(np.cos(Q)) ** 2; sq, rq = G_rung(Q, n - 1); s = s + 0.5 * f2 * sq; r = r + 0.5 * f2[..., None] * rq; sf = sf + 0.5 * f2
    return s + AL * (1 - sf), r


def col0(Bk):
    E = np.zeros((Bk.Nc, 4), complex); E[:4, :4] = np.eye(4); return Bk.apply(E)


g5c = lambda v, N: np.einsum('ab,xbk->xak', g5, v.reshape(N, 4, -1)).reshape(v.shape)
print(f"setup: D4 roots {len(ROOTS)}, norm-4 {len(N4)}, kernel weights 1, 1/2, 1/8; triangles per site {len(TRI)}; alpha = {AL}; HJL bound eps = 1/30")

# ================= 0 code checks
err = 0
for Lc, n in ((4, 1), (2, 2), (2, 3)):
    Bk = Blocked(Field(Lc), n); v, _ = col0(Bk); lev = Bk.levs[-1]
    P = 2 * np.pi * np.array(list(itertools.product(range(Lc), repeat=4)), float) / Lc; s, r = G_rung(P, n)
    bad = ~np.isfinite(s); s[bad] = 1; r[bad] = 0; Dp = np.linalg.inv(s[:, None, None] * E4 - 1j * gv(r)); Dp[bad] = 0
    Dx = np.einsum('xp,pab->xab', np.exp(1j * lev.S @ P.T) / Lc ** 4, Dp); err = max(err, np.abs(v.reshape(lev.N, 4, 4) - Dx).max())
check("0a [T+F] free limit: position-space gauged code at A = 0 equals the momentum-space #10098 map R^n(G_NN) (L_c = 4 n = 1; L_c = 2 n = 2, 3)", err < 1e-10, f"max err {err:.0e}")
IR2 = modes_band(rng, 2, 1, 16); sc = tune(2, 1, 1, IR2, 1.2); lam = (0.7, np.array([np.pi, 0, np.pi, 0]), 0.3)
Da = Blocked(Field(2, 1, 1, IR2, sc), 2).full(); Db = Blocked(Field(2, 1, 1, IR2, sc, lam), 2).full()
lv = Level(2); lc = np.repeat(np.exp(1j * lam[0] * np.cos(lv.S @ lam[1] + lam[2])), 4)
cov = np.abs(Db - np.conj(lc)[:, None] * Da * lc[None]).max(); g5N = np.kron(np.eye(lv.N), g5); herm = np.abs(g5N @ Da @ g5N - Da.conj().T).max()
check("0b [F] gauge covariance D_n[A + d lambda] = L^-1 D_n[A] L and g5-hermiticity (Q = 1 + rough modes, eps = 1.2, L_c = 2, n = 2)", cov < 1e-10 and herm < 1e-10, f"cov {cov:.0e}, g5-herm {herm:.0e}")
print(f"  [t = {time.time() - T0:.0f} s]")

# ================= 1 locality vs roughness
def scan(Lc, n, bgs):
    lev = Level(Lc); out = {}
    for nm, n12, n34, md, eps in bgs:
        sc = tune(Lc, n12, n34, md, eps) if md is not None else 0.0; F = Field(Lc, n12, n34, md, sc)
        pdc = np.abs(1 - np.exp(1j * tri_phases(F, lev, 1.0))).max(); Bk = Blocked(F, n); v, its = col0(Bk)
        rate, ds, env = locality(v.reshape(lev.N, 4, 4), lev.S, Lc); out[(nm, eps)] = (rate, pdc, its[0], env); del Bk
    return out


IR6 = modes_band(rng, 6, 3, 16); UV6 = modes_band(rng, 6, 6, 40)
S6 = scan(6, 1, (("free", 0, 0, None, 0), ("IR", 0, 0, IR6, 1 / 30), ("Q1", 1, 1, None, 0), ("IR", 0, 0, IR6, 0.3), ("IR", 0, 0, IR6, 1.0),
                  ("Q1+IR", 1, 1, IR6, 1.0), ("UV", 0, 0, UV6, 1.0), ("UV", 0, 0, UV6, 1.9)))
fr = S6[("free", 0)][0]; adm = [S6[k][0] for k in S6 if k[1] <= 1 / 30 + 1e-12]; allr = [v[0] for v in S6.values()]
check("1a [F] L_c = 6, n = 1: envelope decay of ||D(x,y)|| stays exponential with rate >= 0.8 x free at the HJL bound and >= 1.0/unit up to eps = 1.9",
      min(adm) >= 0.8 * fr and min(allr) >= 1.0, f"free {fr:.2f}/unit; " + "; ".join(f"{k[0]} eps={k[1]:.3g} (dev {v[1]:.2f}): {v[0]:.2f}" for k, v in S6.items() if k[0] != "free"))
IR4 = modes_band(rng, 4, 2, 16); UV4 = modes_band(rng, 4, 8, 40)
S4 = scan(4, 2, (("free", 0, 0, None, 0), ("Q1+IR", 1, 1, IR4, 1.0), ("UV", 0, 0, UV4, 1.9)))
fr4 = S4[("free", 0)][0]
check("1b [F] L_c = 4, n = 2 (fine 16^4 D4 torus, 131k complex unknowns per solve): rate >= 0.8 x free in a rough flux background and a maximally rough UV field",
      min(v[0] for v in S4.values()) >= 0.8 * fr4, "; ".join(f"{k[0]} eps={k[1]:.3g}: rate {v[0]:.2f}, GMRES its {v[2]}" for k, v in S4.items()))
print(f"  [t = {time.time() - T0:.0f} s]")

# ================= 2 GW and convergence in n (L_c = 2)
UV2 = modes_band(rng, 2, 8, 40); TAB = {}
for nm, n12, n34, md, eps in (("free", 0, 0, None, 0), ("Q1", 1, 1, None, 0), ("UV", 0, 0, UV2, 1.0)):
    sc = tune(2, n12, n34, md, eps) if md is not None else 0.0; F = Field(2, n12, n34, md, sc); prev = None; row = []
    for n in (1, 2, 3):
        Bk = Blocked(F, n); v, _ = col0(Bk); w, _ = Bk.apply(g5c(v, 8))
        gw = np.linalg.norm(g5c(v, 8) + v @ g5 - 2 * AL * w) / np.linalg.norm(v)
        row.append((gw, np.linalg.norm(v - prev) / np.linalg.norm(v) if prev is not None else np.nan)); prev = v; del Bk
    TAB[nm] = row
mono = all(r[0][0] > r[1][0] > r[2][0] for r in TAB.values()); fac = {k: (r[0][0] / r[1][0], r[1][0] / r[2][0]) for k, r in TAB.items()}
check("2a [F] GW residual ||g5 D + D g5 - 2 alpha D g5 D|| / ||D|| falls monotonically with n = 1, 2, 3 in every background (only the limit is exact)",
      mono, "; ".join(f"{k}: " + ", ".join(f"{x[0]:.1e}" for x in r) + f" (x{fac[k][0]:.1f}, x{fac[k][1]:.1f})" for k, r in TAB.items())
      + " [pre-reg bar x1.5 per step: MISS where < 1.5]")
cr = {k: r[2][1] / r[1][1] for k, r in TAB.items()}
check("2b [F] the gauged zoom converges: ||D_3 - D_2|| / ||D_2 - D_1|| <= 0.7 in every background", max(cr.values()) <= 0.7,
      "; ".join(f"{k}: dD2 {r[1][1]:.1e}, dD3 {r[2][1]:.1e}, ratio {cr[k]:.2f}" for k, r in TAB.items()))
print(f"  [t = {time.time() - T0:.0f} s]")

# ================= 3 index of D_n in Q backgrounds (overlap of D_n; L_c = 2 coarse, n = 1, 2)
IDX = {}
for nm, n12, n34, md, eps in (("Q0", 0, 0, None, 0), ("Q1", 1, 1, None, 0), ("Q-1", 1, -1, None, 0), ("Q1+IR", 1, 1, IR2, 1.2), ("Q0+IR", 0, 0, IR2, 1.0)):
    sc = tune(2, n12, n34, md, eps) if md is not None else 0.0; F = Field(2, n12, n34, md, sc)
    for n in (1, 2):
        D = Blocked(F, n).full(); H = g5N @ (2 * AL * D - np.eye(32)); H = (H + H.conj().T) / 2; ev = np.linalg.eigvalsh(H)
        lm, V = np.linalg.eig(D); i = np.argmin(np.abs(lm)); ch = np.real(V[:, i].conj() @ g5N @ V[:, i]) / np.linalg.norm(V[:, i]) ** 2
        IDX[(nm, n)] = (-0.5 * np.sign(ev).sum(), np.abs(ev).min(), lm[i], ch)
want = {"Q0": 0, "Q1": -1, "Q-1": 1, "Q1+IR": -1, "Q0+IR": 0}
check("3a [F] overlap index -(1/2) Tr sign(g5(2 alpha D_n - 1)) = -Q for Q = 0, 1, -1 (smooth and eps = 1.2 rough), n = 1, 2; spectral gap > 0.05",
      all(abs(v[0] - want[k[0]]) < 1e-9 and v[1] > 0.05 for k, v in IDX.items()),
      "; ".join(f"{k[0]} n{k[1]}: {v[0]:+.0f} gap {v[1]:.2f}" for k, v in IDX.items()))
z = [IDX[("Q1", n)] for n in (1, 2)]
check("3b [F] Q = 1: the lowest mode of D_n is real and chiral (g5 = -1) and moves toward 0 with n (the GW zero mode appears only in the limit)",
      all(abs(x[2].imag) < 1e-8 and abs(x[3] + 1) < 1e-6 for x in z) and z[1][2].real < z[0][2].real,
      f"lambda_0 = {z[0][2].real:.3f} (n=1), {z[1][2].real:.3f} (n=2); chirality {z[0][3]:.3f}, {z[1][3]:.3f}; ratio {z[0][2].real / z[1][2].real:.2f}")
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
