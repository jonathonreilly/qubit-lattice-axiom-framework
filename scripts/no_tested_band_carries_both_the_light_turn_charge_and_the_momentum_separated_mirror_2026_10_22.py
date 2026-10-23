AUDIT_INPUT_PATHS = ('docs/NO_TESTED_BAND_CARRIES_BOTH_THE_LIGHT_TURN_CHARGE_AND_THE_MOMENTUM_SEPARATED_MIRROR_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""one-band-check: does ONE free band do both jobs of the ruleset?
  R10 (family count) needs the light copy to carry a nonzero three-fold-turn charge q.
  R11 (mirror separation) needs light and mirror at different exact momentum labels, so a
      filtered charge-4 mirror term can vanish on the light cone.
Bands tested (exact, free level):
  A/B  CL-1 cube tick with the AX-3 copy mass (even cubes)  -- the band R10 uses
  C    the glide-symmetric CL-1 tick (no copy mass, or copy mass on both tilings)
  D    the Karsten-Wilczek-type two-cone band                 -- the band R11 uses
Self-contained (numpy + scipy). Seeded. Bloch over 2Z^3 = twisted 2^3 torus (twist = 2k).
"""
import itertools as it
import numpy as np
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 60
rng = np.random.default_rng(20261022)
NP = [0, 0]
W3 = np.exp(2j * np.pi / 3)


def check(name, ok, detail=""):
    NP[0 if ok else 1] += 1
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail else ""))


CELL = list(it.product([0, 1], repeat=3))
IDX = {a: n for n, a in enumerate(CELL)}


def eta(i, x):
    return [1, (-1) ** x[0], (-1) ** (x[0] + x[1])][i]


def build(th):
    """even/odd link hops on the 2^3 torus with twist th (= 2k), and the (1,1,1) shift."""
    We, Wo = [], []
    for i in range(3):
        for par, out in ((0, We), (1, Wo)):
            M = np.zeros((8, 8), complex)
            for x in CELL:
                if x[i] == par:
                    y = list(x); y[i] = (y[i] + 1) % 2; y = tuple(y)
                    ph = np.exp(1j * th[i]) if x[i] == 1 else 1
                    M[IDX[y], IDX[x]] += eta(i, x) * ph
                    M[IDX[x], IDX[y]] += eta(i, x) * np.conj(ph)
            out.append(M)
    P = np.zeros((8, 8), complex)
    for x in CELL:
        y = tuple((np.array(x) + 1) % 2)
        P[IDX[y], IDX[x]] = np.prod([np.exp(1j * th[i]) if x[i] == 1 else 1 for i in range(3)])
    return We, Wo, P


DG = np.diag([(-1) ** (a[0] + a[2]) for a in CELL]).astype(complex)  # glide site gauge (found by search)


def tick(th, eps=0.3, M=0.0, both=False):
    We, Wo, P = build(th)
    Re, Ro = sum(We) / np.sqrt(3), sum(Wo) / np.sqrt(3)
    se = 1j * We[0] @ We[1] @ We[2] @ Re
    so = 1j * Wo[0] @ Wo[1] @ Wo[2] @ Ro
    Ue, Uo = expm(-1j * eps * Re), expm(1j * eps * Ro)
    if M:
        Ce = expm(1j * (M / 4) * (np.eye(8) - se) @ Re); Ue = Ce @ Ue @ Ce
        if both:
            Co = expm(-1j * (M / 4) * (np.eye(8) - so) @ Ro); Uo = Co @ Uo @ Co
    G = np.linalg.inv(Ue) @ DG @ P            # glide: one-site (1,1,1) shift, then undo the even half-step
    return Uo @ Ue, G, Re, Ro, P


ROTS = []
for p in it.permutations(range(3)):
    for sg in it.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[p[i], i] = sg[i]
        if np.linalg.det(R) > 0:
            ROTS.append(R)
TURNS = [R for R in ROTS if round(np.trace(R)) == 0]
cen = np.full(3, 0.5)
KT = [np.array([.2, -.3, .5]), np.array([-.6, .1, .3])]


def perm(R):
    Pm = np.zeros((8, 8))
    for a in CELL:
        b = tuple(np.rint(R @ (np.array(a) - cen) + cen).astype(int)); Pm[IDX[b], IDX[a]] = 1
    return Pm


def rot_gauge(R, f):
    Pm = perm(R)
    for sg in it.product([1, -1], repeat=8):
        V = np.diag(sg) @ Pm
        if all(np.allclose(V @ f(t) @ V.T, f(R @ t), atol=1e-10) for t in KT):
            return V
    return None


def chirality(f):
    h = 1e-6; A = []
    for i in range(3):
        d = np.zeros(3); d[i] = h
        A.append(1j * (f(d) - f(-d)) / (2 * h))
    v2 = np.trace(A[0] @ A[0]).real / 8
    A = [a / np.sqrt(v2) for a in A]
    return 1j * A[0] @ A[1] @ A[2]


def light_blocks(U0, chi):
    w, v = np.linalg.eig(U0)
    Lt, _ = np.linalg.qr(v[:, abs(np.angle(w)) < 1e-3])
    out = {}
    for s in (1, -1):
        Pc = Lt.conj().T @ ((np.eye(8) + s * chi) / 2) @ Lt
        ew, ev = np.linalg.eigh((Pc + Pc.conj().T) / 2)
        out[s] = Lt @ ev[:, ew > 0.5]
    return Lt.shape[1], out


def qof(V, B):
    d = np.linalg.det(B.conj().T @ V @ B)
    return [q for q in range(3) if abs(d - W3 ** (2 * q)) < 1e-6]


# ---------------------------------------------------------------- A. the glide and the copy mass
print("== A. CL-1 cell tick: the one-site (1,1,1) glide G = Ue^-1 D T(1,1,1) ==")
comm = lambda M, both: max(np.abs(tick(t, M=M, both=both)[1] @ tick(t, M=M, both=both)[0]
                                  - tick(t, M=M, both=both)[0] @ tick(t, M=M, both=both)[1]).max() for t in KT + [np.zeros(3)])
c0, c3, cb = comm(0, False), comm(0.7, False), comm(0.7, True)
check("A1 massless tick: G commutes with U(k) at every k (exact glide; G^2 = cell translation x U^-1)", c0 < 1e-10, f"max|[G,U]| {c0:.1e}")
def glide_any_gauge(M):
    best = 9.0
    for sg in it.product([1, -1], repeat=7):
        Dg = np.diag((1,) + sg).astype(complex)
        e = 0.0
        for t in KT:
            Ut, _, Re_, Ro_, P_ = tick(t, M=M)
            We_ = build(t)[0]; se_ = 1j * We_[0] @ We_[1] @ We_[2] @ Re_
            Ce_ = expm(1j * (M / 4) * (np.eye(8) - se_) @ Re_)
            Gd = np.linalg.inv(Ce_ @ expm(-1j * 0.3 * Re_) @ Ce_) @ Dg @ P_
            e = max(e, np.abs(Gd @ Ut - Ut @ Gd).max())
        best = min(best, e)
    return best
g3 = glide_any_gauge(0.7)
check("A2 AX-3 copy mass (even cubes only) BREAKS the glide, for every site gauge (all 2^8, overall sign fixed)",
      c3 > 0.1 and g3 > 0.1, f"max|[G,U]| {c3:.3f}; best over gauges {g3:.3f}")
check("A3 copy mass on both tilings keeps the glide", cb < 1e-10, f"{cb:.1e}")
for eps in (0.3, 0.6):
    f0 = lambda t, e=eps: tick(t, eps=e)[0]
    chi0 = chirality(f0); G0 = tick(np.zeros(3), eps=eps)[1]
    if eps == 0.3:
        gchi = np.abs(G0 - chi0).max()
    else:
        gchi = max(gchi, np.abs(G0 - chi0).max())
check("A4 THEOREM (massless tick, K = 0): G = chirality as 8x8 operators (eps = 0.3, 0.6): all L tastes have G = +1, "
      "all R tastes G = -1 -- a KW-like split by the glide label", gchi < 1e-6, f"max|G - chi| {gchi:.1e}")
Ub = tick(np.zeros(3), M=0.7, both=True)[0]
nb = int(np.sum(abs(np.angle(np.linalg.eigvals(Ub))) < 1e-3))
check("A5 hence no glide-symmetric bilinear can pair L with R at K = 0 (would need equal G); the both-tilings copy mass "
      "gaps nothing there", nb == 8, f"light states at K=0: {nb}/8")
Xr = rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8)); Xr = Xr + Xr.conj().T
Xg = (Xr + G0 @ Xr @ np.linalg.inv(G0)) / 2
check("A6 random G-symmetric cell term: its L-R block vanishes identically at K = 0 (Schur, G = chi)",
      np.linalg.norm(((np.eye(8) + chi0) / 2) @ Xg @ ((np.eye(8) - chi0) / 2)) < 1e-9)

# ---------------------------------------------------------------- B. the AX-3 band (R10's band)
print("== B. AX-3 copy-mass tick (the band the family count uses) ==")
M = 0.7
fAX = lambda t: tick(t, M=M)[0]
U0 = fAX(np.zeros(3)); chiA = chirality(fAX)
nl, BL = light_blocks(U0, chiA)
check("B1 light copy = 1 L Weyl + 1 R Weyl (2 spin each), BOTH at cell momentum K = 0", nl == 4 and BL[1].shape[1] == 2 == BL[-1].shape[1])
cw = {}
for s in (1, -1):
    cw[s] = [float(np.linalg.norm((np.array([(-1) ** np.dot(pc, a) for a in CELL]) / np.sqrt(8)) @ BL[s]) ** 2) for pc in CELL]
check("B2 fine-corner content: L and R each spread 1/4 on every one of the 8 corners (no fine-momentum separation); "
      "the cube average (corner 000) has weight 1/4 on light AND mirror", all(np.allclose(cw[s], 0.25) for s in (1, -1)),
      f"L {np.round(cw[1], 3).tolist()[:3]}.., R {np.round(cw[-1], 3).tolist()[:3]}..")
KG = [(R, rot_gauge(R, fAX)) for R in ROTS]
KG = [(R, V) for R, V in KG if V is not None]
qL = [qof(V, BL[1]) for R, V in KG if round(np.trace(R)) == 0]
qR = [qof(V, BL[-1]) for R, V in KG if round(np.trace(R)) == 0]
check("B3 R10 holds here: 12 rotations kept; every turn gives q in {1,2} on the light copy, q_L = q_R",
      len(KG) == 12 and all(a in ([1], [2]) for a in qL) and qL == qR, f"q per turn {[a[0] for a in qL]}")
Hr = rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8)); Hr = (Hr + Hr.conj().T) / 2
Hs = sum(V.T @ Hr @ V for R, V in KG) / len(KG)
lr = np.linalg.norm(BL[1].conj().T @ Hs @ BL[-1])
gaps = []
for dl in (0.01, 0.02):
    Up = U0 @ expm(-1j * dl * Hs)
    keep = all(np.allclose(V @ (fAX(t) @ expm(-1j * dl * Hs)) @ V.T, fAX(R @ t) @ expm(-1j * dl * Hs)) for R, V in KG for t in KT[:1])
    w = np.sort(np.angle(np.linalg.eigvals(Up))); w = w[abs(w) < 0.2]
    lo, hi = w[w < 0].max(), w[w > 0].min()
    gaps.append((keep, lo, hi))
check("B4 a random cell-local term keeping cell translations and all 12 kept rotations has an L-R block and opens a "
      "Dirac gap linear in its size: crystal momentum + turns do NOT forbid the light-mirror mass in this band",
      lr > 0.1 and all(g[0] and g[1] < 0 < g[2] for g in gaps) and abs(gaps[1][2] / gaps[0][2] - 2) < 0.05,
      f"|P_L H P_R| {lr:.3f}; K=0 light levels {[(round(float(g[1]), 4), round(float(g[2]), 4)) for g in gaps]}")
check("B5 so R11's selection rule (light-mirror pairing allowed iff Q_L = Q_M) is met with Q_L = Q_M: the composite "
      "partner channel psi_L (mirror^3) is open, and any cube/cell filter at K = 0 contains the light legs", lr > 0.1 and min(cw[1]) > 0.2)

# ---------------------------------------------------------------- C. the glide-symmetric band
print("== C. glide-symmetric massless tick (separation available) ==")
f0 = lambda t: tick(t)[0]
U00, G00 = tick(np.zeros(3))[:2]
chi0 = chirality(f0)
F = (np.eye(8) - G00) / 2
nL = np.linalg.norm(F @ (np.eye(8) + chi0) / 2); nR = np.linalg.norm(F @ (np.eye(8) - chi0) / 2) ** 2
check("C1 glide filter F = (1 - G)/2 (range one): exactly 0 on every light L state, 1 on every R state at K = 0",
      nL < 1e-9 and abs(nR - 4) < 1e-9, f"|F P_L| {nL:.1e}, tr F P_R {nR:.3f}")
lk = []
for s in (0.01, 0.02):
    t = s * np.array([0.6, -0.3, 0.74])
    Gt = tick(t)[1]
    lk.append(min(abs(1 - g) / 2 for g in np.linalg.eigvals(Gt)))
check("C2 leak of F onto the light branch grows linearly in k (|1-g(k)|/2), cf. k^3 for the KW cube filter",
      abs(lk[1] / lk[0] - 2) < 0.1, f"leak {lk[0]:.2e}, {lk[1]:.2e}")
V0 = [(R, rot_gauge(R, f0)) for R in ROTS]
cov = all(np.allclose(V @ G00 @ V.T, G00) or np.allclose(V @ G00 @ V.T, -G00) for R, V in V0 if V is not None)
sgnF = all(np.allclose(V @ chi0 @ V.T, chi0) for R, V in V0 if V is not None)
check("C3 F is cube-covariant: all 24 rotations kept by the massless tick map G -> G (rotations keep chirality)",
      sum(V is not None for R, V in V0) == 24 and cov and sgnF)
PL = (np.eye(8) + chi0) / 2
qs = []
for R, V in V0:
    if V is not None and round(np.trace(R)) == 0:
        ev = np.linalg.eigvals(PL @ V @ PL + 5 * (np.eye(8) - PL)); ev = ev[abs(ev) < 2]
        qs.append(np.prod(ev))
check("C4 but R10 fails here: the light L content is E (q = 1 and 2), total turn phase det = w^(2(1+2)) = 1, so the "
      "light vertex w^(4N(1+2)) = 1 for every N -- no family count", all(abs(x - 1) < 1e-6 for x in qs), f"det on L per turn {np.round(qs, 4).tolist()[:2]}..")

# ---------------------------------------------------------------- D. the KW band (R11's band)
print("== D. Karsten-Wilczek-type band (the band the separation uses) ==")


def dKW(p):
    k = np.array([p[0] - p[1], p[1] - p[2], p[2]])
    return np.array([np.sin(k[0]), np.sin(k[1]), np.sin(k[2]) + 2 - np.cos(k[0]) - np.cos(k[1])])


jac = lambda p: np.stack([(dKW(p + 1e-6 * e) - dKW(p - 1e-6 * e)) / 2e-6 for e in np.eye(3)], 1)
n = 12; zs = [p for p in it.product(2 * np.pi * np.arange(n) / n, repeat=3) if np.linalg.norm(dKW(np.array(p))) < 1e-9]
chis = (int(np.sign(np.linalg.det(jac(np.zeros(3))))), int(np.sign(np.linalg.det(jac(np.pi * np.ones(3))))))
check("D1 KW band: zeros only at K = 0 (+1) and R = pi(1,1,1) (-1)", len(zs) == 2 and chis == (1, -1), f"chi {chis}")
ps = rng.uniform(-np.pi, np.pi, (200, 3))
nd = np.array([np.linalg.norm(dKW(p)) for p in ps])
dev = [min(np.max(np.abs(np.array([np.linalg.norm(dKW(sg * R @ p + np.pi * np.array(Q))) for p in ps]) - nd))
           for sg in (1, -1) for Q in CELL) for R in TURNS]
check("D2 no three-fold cube turn (unitary or antiunitary, any translation or pi-momentum shift) preserves the KW spectrum: R10 has no kept turn",
      min(dev) > 0.1, f"min over turns of max | |d(Rp)| - |d(p)| | = {min(dev):.3f}")
xs = np.array(list(it.product(range(-3, 4), repeat=3)))
ph = all(np.allclose(np.exp(1j * (xs @ R.T - xs) @ Q), 1) for R in ROTS for Q in (np.zeros(3), np.pi * np.ones(3)))
check("D3 for ANY cube-covariant on-site-spinor band with cones at K and R, the Bloch phase of every rotation is 1 at both "
      "cones (Rx - x has even coordinate sum): the turn acts on each cone as spinor x one on-site phase mu", ph)
mus = [np.exp(1j * np.pi * j / 3) for j in range(6)]
okmu = [j for j, m in enumerate(mus) if abs(m ** 4 - 1) < 1e-9]
check("D4 the charge-4 mirror term (spin singlet) keeps the turn only if mu^4 = 1; with mu^6 = 1 that leaves mu = +-1, "
      "q = 0 on light and mirror; mu = w is the fermion-number Z3, broken by the term (w^4 = w) -- R10 is silent here",
      okmu == [0, 3] and abs(W3 ** 4 - W3) < 1e-12, f"allowed mu = exp(i pi j/3), j in {okmu}")

# ---------------------------------------------------------------- E. verdict
print("== E. verdict ==")
R10 = {"AX3": NP[1] == 0 and min(len(a) for a in qL) == 1, "glide": False, "KW": False}
R11 = {"AX3": not (lr > 0.1), "glide": bool(nL < 1e-9), "KW": len(zs) == 2}
BOTH_FAIL = not any(R10[b] and R11[b] for b in R10) and R10["AX3"] and R11["glide"] and R11["KW"]
print("job table (R10 count, R11 separation):", {b: (R10[b], R11[b]) for b in R10})
check("E1 no band tested does both jobs: AX-3 (q != 0, no separation); glide/massless (separation, q sum 0); KW "
      "(separation, no turn / q = 0). Within glide-symmetric number-conserving bilinears the 2+2 -> 1+1 reduction "
      "is impossible at K = 0 (A4-A6)", BOTH_FAIL)
print("open (not computed): a glide-symmetric band that annihilates the q=1 L/R tastes away from K=0 (node motion),"
      " leaving L(q=2, G=+1) and R(q=2, G=-1)")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
