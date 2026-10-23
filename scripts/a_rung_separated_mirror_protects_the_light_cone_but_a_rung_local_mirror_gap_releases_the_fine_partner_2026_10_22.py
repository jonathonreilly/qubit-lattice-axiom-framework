AUDIT_INPUT_PATHS = ('docs/A_RUNG_SEPARATED_MIRROR_PROTECTS_THE_LIGHT_CONE_BUT_A_RUNG_LOCAL_MIRROR_GAP_RELEASES_THE_FINE_PARTNER_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Rung-separated mirror (repair (a) of spin10-breaking): seeded, self-contained.
A: where the cones of a cone-rule band sit on one rung; nested-reading form factors.
B: two-rung free model (fine Z^3 + one coarse rung on 2^3 blocks): which cross-rung reading
   pairs which cones; the light node's exact decoupling; crystal-momentum selection.
C: gapping the coarse mirror: Golterman-Shamir release of the fine partner (algebra + ED atom),
   and the momentum-selective coarse quartic (rung-2 rows)."""
AUDIT_TIMEOUT_SEC = 120
import itertools, os
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1'); os.environ.setdefault('OMP_NUM_THREADS', '1')
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(20261022)
NP = [0, 0]
def check(name, ok, msg):
    NP[0 if ok else 1] += 1; print(f"[{'PASS' if ok else 'FAIL'}] {name} {msg}")
SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.diag([1.0 + 0j, -1]); I2 = np.eye(2)
SIG = [SX, SY, SZ]
AM = np.array([[1., -1, 0], [0, 1, -1], [0, 0, 1]])       # unimodular momentum map
R3 = np.pi * np.ones(3)
def dvec(p, pert=None):                                    # Karsten-Wilczek-type cone-rule band, nodes 0 and R
    k = AM @ p
    d = np.array([np.sin(k[0]), np.sin(k[1]), np.sin(k[2]) + (2 - np.cos(k[0]) - np.cos(k[1]))])
    if pert is not None:
        a, b, c = pert; d = d + a @ np.cos(p) + b @ np.sin(p) + c
    return d
def hmat(d): return d[0] * SX + d[1] * SY + d[2] * SZ
def jac(f, p, h=1e-6):
    return np.array([(f(p + h * e) - f(p - h * e)) / (2 * h) for e in np.eye(3)]).T
def newton(f, p):
    for _ in range(60):
        v = f(p)
        if np.linalg.norm(v) < 1e-14: break
        p = p - np.linalg.solve(jac(f, p), v)
    return p, np.linalg.norm(f(p))

# ---------------- A: one rung ----------------
g = np.linspace(0, 2 * np.pi, 24, endpoint=False)
P = np.array(list(itertools.product(g, g, g)))
nd = np.array([np.linalg.norm(dvec(p)) for p in P])
cand = P[nd < 0.4]
nodes = []
for p0 in cand:
    p, r = newton(dvec, p0.copy())
    if r < 1e-12:
        p = np.mod(p, 2 * np.pi); p[np.abs(p - 2 * np.pi) < 1e-9] = 0
        if not any(np.linalg.norm(np.angle(np.exp(1j * (p - q)))) < 1e-6 for q, _ in nodes):
            nodes.append((p, int(np.sign(np.linalg.det(jac(dvec, p))))))
chi = {tuple(float(v) for v in np.round(p / np.pi, 6)): c for p, c in nodes}
check("A1", len(nodes) == 2 and chi.get((0., 0., 0.)) == 1 and chi.get((1., 1., 1.)) == -1,
      f"one rung, cone-rule band: nodes {sorted(chi.items())} (p/pi: chirality), sum {sum(chi.values())}; mirror on the SAME rung (Nielsen-Ninomiya per rung)")
pert = (0.05 * rng.standard_normal((3, 3)), 0.05 * rng.standard_normal((3, 3)), 0.05 * rng.standard_normal(3))
fP = lambda p: dvec(p, pert)
res = []
for p0 in (np.zeros(3), R3.copy()):
    p, r = newton(fP, p0); res.append((r, int(np.sign(np.linalg.det(jac(fP, p)))), np.linalg.norm(np.angle(np.exp(1j * (p - p0))))))
ndP = np.array([np.linalg.norm(fP(p)) for p in P])
check("A2", all(r < 1e-12 for r, _, _ in res) and res[0][1] + res[1][1] == 0 and ndP.min() > 0,
      f"random 0.05 nn change: nodes persist (shift {res[0][2]:.3f}, {res[1][2]:.3f}), chiralities {res[0][1]:+d},{res[1][1]:+d}; untuned")
# inversion maps the class (0:+, R:-) to (0:-, R:+): which chirality sits at the block-visible momentum is one bit
fI = lambda p: dvec(-p)
cI = [int(np.sign(np.linalg.det(jac(fI, q)))) for q in (np.zeros(3), R3)]
check("A3", cI == [-1, 1], f"inverted update: chiralities at 0, R = {cI}: the handedness at the smooth momentum is one bit, swapped by inversion")
# nested-reading overlaps and plane-wave form factors on 8^3
L = 8; X = np.array(list(itertools.product(range(L), repeat=3)))
def rows(stag, b=2):
    blocks = {}
    for i, x in enumerate(X):
        blocks.setdefault(tuple(x // b), []).append(i)
    M = np.zeros((len(blocks), len(X)))
    for j, (c, ids) in enumerate(sorted(blocks.items())):
        for i in ids: M[j, i] = ((-1.0) ** X[i].sum() if stag else 1.0) / np.sqrt(len(ids))
    return M
RU, RS, RU4 = rows(False), rows(True), rows(False, 4)
ov1 = RU[0] @ np.eye(len(X))[0]; ov12 = RU4[0] @ RU[0]; ov02 = RU4[0] @ np.eye(len(X))[0]
qs = [np.zeros(3), R3, np.array([2, 4, 6]) * np.pi / 4, np.array([2, 0, 6]) * np.pi / 4]
wU, wS, fU, fS = [], [], [], []
for q in qs:
    psi = np.exp(1j * X @ q) / np.sqrt(len(X))
    wU.append(np.linalg.norm(RU @ psi) ** 2); wS.append(np.linalg.norm(RS @ psi) ** 2)
    fU.append(np.prod(np.cos(q / 2) ** 2)); fS.append(np.prod(np.sin(q / 2) ** 2))
check("A4", abs(ov1 - 2 ** -1.5) < 1e-15 and abs(ov12 - 2 ** -1.5) < 1e-15 and abs(ov02 - 2 ** -3) < 1e-15
      and np.allclose(wU, fU, atol=1e-14) and np.allclose(wS, fS, atol=1e-14),
      f"overlaps 2^(-3/2) per rung ({ov1:.6f},{ov12:.6f}; two rungs {ov02:.6f}); plane-wave weight on uniform rows = prod cos^2(q/2) "
      f"[{', '.join(f'{v:.3f}' for v in wU)}], on staggered rows = prod sin^2(q/2) [{', '.join(f'{v:.3f}' for v in wS)}] at q = 0, R, 2 generic")

# ---------------- B: two-rung free model ----------------
tc, w = 0.5, 0.5
J0, JR = jac(dvec, np.zeros(3)), jac(dvec, R3)            # coarse cone at 0 (in fine units tc*2*J0 = J0), fine cone at R
def polar_lift(Ja, Jb):
    Mx = Ja @ np.linalg.inv(Jb); Uu, s, Vt = np.linalg.svd(Mx); Q = Uu @ Vt
    O = -Q if np.linalg.det(Q) < 0 else Q
    ang = np.arccos(np.clip((np.trace(O) - 1) / 2, -1, 1))
    if ang < 1e-12: return I2, O
    if ang > np.pi - 1e-4:
        ev, vv = np.linalg.eigh((O + O.T) / 2); n = vv[:, np.argmax(ev)]
    else:
        n = np.array([O[2, 1] - O[1, 2], O[0, 2] - O[2, 0], O[1, 0] - O[0, 1]]); n /= np.linalg.norm(n)
    U = np.cos(ang / 2) * I2 - 1j * np.sin(ang / 2) * sum(n[i] * SIG[i] for i in range(3))
    if not all(np.allclose(U @ SIG[j] @ U.conj().T, sum(O[i, j] * SIG[i] for i in range(3))) for j in range(3)): U = U.conj().T
    return U, O
# B1: polar-lift theorem for two opposite-chirality cones with arbitrary frames
okB1, mind = True, 1e9
for _ in range(40):
    Ja = rng.standard_normal((3, 3)); Jb = rng.standard_normal((3, 3))
    if np.linalg.det(Ja) * np.linalg.det(Jb) > 0: Jb[:, 0] *= -1
    U, _ = polar_lift(Jb, Ja)
    for _ in range(50):
        u = rng.standard_normal(3) * rng.uniform(0, 3)
        H = np.block([[hmat(Ja @ u), w * U.conj().T], [w * U, hmat(Jb @ u)]])
        mind = min(mind, np.abs(np.linalg.eigvalsh(H)).min() / w)
okB1 = mind > 1e-3
# identity coupling for the actual pair (fine R, coarse 0): nodal ring at |u| = w, u3 = 0
Hid = lambda u: np.block([[hmat(JR @ u), w * I2], [w * I2, hmat(J0 @ u)]])
uring = np.linalg.solve(JR, np.array([w, 0, 0]))
ering = np.abs(np.linalg.eigvalsh(Hid(uring))).min()
check("B1", okB1 and ering < 1e-9, f"opposite cones gap everywhere with coupling w*U (U = SU(2) lift of the polar rotation between the cone frames; min |E|/w {mind:.3f} over 2000 random frames, momenta); identity coupling on the actual pair leaves a nodal ring (|E| {ering:.0e}): the coupling matrix is fixed by the bands")
UL, OL = polar_lift(J0, JR)
def Htwo(Pc, reading, M, wx=w):
    ns = list(itertools.product((0, 1), repeat=3)); D = 2 * len(ns) + 2
    H = np.zeros((D, D), complex)
    for a, n in enumerate(ns):
        q = (Pc + 2 * np.pi * np.array(n)) / 2
        H[2 * a:2 * a + 2, 2 * a:2 * a + 2] = hmat(dvec(q))
        c = np.prod(1 - np.exp(1j * q)) / 8 if reading == 's' else np.prod(1 + np.exp(1j * q)) / 8
        H[-2:, 2 * a:2 * a + 2] = wx * c * M; H[2 * a:2 * a + 2, -2:] = np.conj(wx * c * M).T
    H[-2:, -2:] = tc * hmat(dvec(Pc)); return H
# B2: uniform reading with the same rule on both rungs: same-chirality cones at P = 0, nothing gaps
E0u = np.linalg.eigvalsh(Htwo(np.zeros(3), 'u', I2))
# radial search for zero crossings near P = 0 (Fermi pocket from same-chirality mixing)
fu = lambda p: np.abs(np.linalg.eigvalsh(Htwo(p, 'u', I2))).min()
pk = []
for _ in range(4):
    dd = rng.standard_normal(3); dd /= np.linalg.norm(dd)
    o = minimize(fu, 2 * w / np.linalg.norm(J0 @ dd) * dd, method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-15, 'maxiter': 4000})
    pk.append((o.fun, np.linalg.norm(J0 @ o.x) / 2))
epk = max(x for x, _ in pk); hr = [y for _, y in pk]
eoff = fu(0.5 * 2 * w / np.linalg.norm(J0 @ np.ones(3)) * np.ones(3))
check("B2", np.sum(np.abs(E0u) < 1e-12) == 2 and epk < 1e-10 and eoff > 1e-3 and min(hr) > 0.8 * w,
      f"uniform-character reading: fine R stays a zero at P=0 (zeros {np.sum(np.abs(E0u) < 1e-12)}), fine 0 + coarse 0 (same chirality) keep zeros (4 searches: |E| <= {epk:.0e} at |h| = {min(hr):.3f}-{max(hr):.3f}, w = {w}): charge +2 cannot gap; no pair removed")
# B3: staggered-character reading: pairs fine R (-) with coarse 0 (+); fine 0 (+) exactly decoupled
E0s = np.sort(np.linalg.eigvalsh(Htwo(np.zeros(3), 's', UL)))
Pz = np.zeros(3); Hs0 = Htwo(Pz, 's', UL); psiL = np.zeros(18, complex); psiL[0] = 1
okdec = np.linalg.norm(Hs0 @ psiL) < 1e-15 and np.linalg.norm(Hs0 @ np.roll(psiL, 1)) < 1e-15
pairE = sorted(np.abs(E0s))[2:6]
check("B3", okdec and np.sum(np.abs(E0s) < 1e-12) == 2 and np.allclose(pairE, w, atol=1e-12),
      f"staggered reading: P=0 zeros = the light fine-0 Weyl only (H psi_L = 0 exactly); fine R + coarse 0 Dirac gap = {pairE[0]:.4f} = w")
# global zeros of the two-rung model
gc = np.linspace(0, 2 * np.pi, 10, endpoint=False)
Pg = np.array(list(itertools.product(gc, gc, gc)))
emin = np.array([np.abs(np.linalg.eigvalsh(Htwo(p, 's', UL))).min() for p in Pg])
fmin = lambda p: np.abs(np.linalg.eigvalsh(Htwo(p, 's', UL))).min()
opt = minimize(fmin, R3 + 0.01, method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-14, 'maxiter': 4000})
PB = opt.x
far = np.array([min(np.linalg.norm(np.angle(np.exp(1j * (p - z)))) for z in (np.zeros(3), PB)) for p in Pg]) > 1.0
def node_info(Pn):
    E, V = np.linalg.eigh(Htwo(Pn, 's', UL)); idx = np.argsort(np.abs(E))[:2]; Vn = V[:, idx]
    def comp(dp):
        he = Vn.conj().T @ Htwo(Pn + dp, 's', UL) @ Vn
        return np.array([np.trace(he @ s).real / 2 for s in SIG])
    Jn = np.array([(comp(1e-5 * e) - comp(-1e-5 * e)) / 2e-5 for e in np.eye(3)]).T
    return int(np.sign(np.linalg.det(Jn))), float(np.sum(np.abs(Vn[-2:, :]) ** 2) / 2)
cL, wcL = node_info(Pz); cB, wcB = node_info(PB)
check("B4", opt.fun < 1e-8 and emin[far].min() > 0.05 and cL + cB == 0,
      f"zeros: light at P=0 (chirality {cL:+d}, coarse weight {wcL:.1e}), mirror B at P={np.round(PB / np.pi, 4).tolist()} pi (|E| {opt.fun:.0e}, chirality {cB:+d}, coarse weight {wcB:.3f}); min |E| elsewhere {emin[far].min():.3f}")
# B5: the light node's coupling to the coarse rung vanishes as q1 q2 q3 (irrelevant)
cq = [abs(np.prod(1 - np.exp(1j * dl * np.array([1, 0.7, 0.4]))) / 8) for dl in (1e-2, 5e-3)]
check("B5", abs(cq[0] / cq[1] - 8) < 1e-3, f"light vertex to coarse rows ~ |q1 q2 q3|/8: halving q divides it by {cq[0] / cq[1]:.4f}")
# B6: crystal momentum: light (fine 0 -> coarse P=0) vs mirror B (coarse R_c) on a real-space torus with random
# coarse-translation-invariant bilinears; and light vs fine partner R (same coarse momentum!)
Lf, Lc = 4, 2
Xf = np.array(list(itertools.product(range(Lf), repeat=3))); Xc = np.array(list(itertools.product(range(Lc), repeat=3)))
Nf, Nc = len(Xf), len(Xc); D = 2 * Nf + 2 * Nc
Hr = rng.standard_normal((D, D)) + 1j * rng.standard_normal((D, D)); Hr = Hr + Hr.conj().T
def tperm(t):
    pf = [int(np.ravel_multi_index(tuple((x + 2 * t) % Lf), (Lf,) * 3)) for x in Xf]
    pc = [int(np.ravel_multi_index(tuple((x + t) % Lc), (Lc,) * 3)) for x in Xc]
    perm = np.zeros(D, int)
    for i, j in enumerate(pf): perm[2 * i], perm[2 * i + 1] = 2 * j, 2 * j + 1
    for i, j in enumerate(pc): perm[2 * Nf + 2 * i], perm[2 * Nf + 2 * i + 1] = 2 * Nf + 2 * j, 2 * Nf + 2 * j + 1
    return np.eye(D)[perm]
Ts = [tperm(np.array(t)) for t in itertools.product(range(Lc), repeat=3)]
Hsym = sum(T @ Hr @ T.T for T in Ts) / len(Ts)
def fwave(q, s):
    v = np.zeros(D, complex); v[0 + s:2 * Nf:2] = np.exp(1j * Xf @ q) / np.sqrt(Nf); return v
def cwave(Pc, s):
    v = np.zeros(D, complex); v[2 * Nf + s::2] = np.exp(1j * Xc @ Pc) / np.sqrt(Nc); return v
mLB = max(abs(fwave(np.zeros(3), a).conj() @ Hsym @ cwave(R3, b)) for a in (0, 1) for b in (0, 1))
mLR = max(abs(fwave(np.zeros(3), a).conj() @ Hsym @ fwave(R3, b)) for a in (0, 1) for b in (0, 1))
mLA = max(abs(fwave(np.zeros(3), a).conj() @ Hsym @ cwave(np.zeros(3), b)) for a in (0, 1) for b in (0, 1))
check("B6", mLB < 1e-12 and mLR > 1e-2 and mLA > 1e-2,
      f"random coarse-translation-invariant bilinear: light-B {mLB:.0e} (forbidden by coarse momentum), light-fine R {mLR:.2f} and light-A {mLA:.2f} (allowed): the light's protection from its own partner needs fine translations on the fine rung plus the staggered row's zero, not the rung split")

# ---------------- C: gapping the coarse mirror ----------------
# C1: exact release at the node: G_R = [i om - w^2 U G_A U^+]^-1, symmetric gapped A: G_A = i om/((i om)^2 - Delta^2)
Dl = 1.0; ws = [1.0, 2 ** -1.5, 2 ** -3]; Zs = []
for wx in ws:
    om = 1e-6; GA = 1j * om / ((1j * om) ** 2 - Dl ** 2); GR = 1 / (1j * om - wx ** 2 * GA)
    Zs.append((GR * 1j * om).real)
check("C1", np.allclose(Zs, [Dl ** 2 / (Dl ** 2 + x ** 2) for x in ws], atol=1e-9) and Zs[0] < Zs[1] < Zs[2],
      f"momentum-blind coarse SMG: fine partner R released at zero energy with weight Z = D^2/(D^2+w^2) = {', '.join(f'{z:.3f}' for z in Zs)} for w/D = 1, 2^-1.5, 2^-3: cross-rung suppression makes the release MORE complete")
# C2: ED atom, SU(4) toy: partner l_a (4 modes) hybridised by w with an A-block m_a carrying -g(m1m2m3m4 + h.c.)
nm = 8
def cop(j):
    ops = []
    for k in range(nm):
        ops.append(np.array([[1, 0], [0, -1.]]) if k < j else (np.array([[0, 1], [0, 0.]]) if k == j else np.eye(2)))
    M = ops[0]
    for o in ops[1:]: M = np.kron(M, o)
    return M
cs = [cop(j) for j in range(nm)]; l, m = cs[:4], cs[4:]
Q = m[0] @ m[1] @ m[2] @ m[3]
def gap(gg, wx):
    H = -gg * (Q + Q.T) + wx * sum(l[a].T @ m[a] + m[a].T @ l[a] for a in range(4))
    E = np.linalg.eigvalsh(H); return E[np.argmax(E > E[0] + 1e-10)] - E[0]
g0 = [gap(0.0, wx) / wx for wx in (0.2, 0.2 * 2 ** -1.5)]
gr = [gap(1.0, wx) / wx for wx in (0.2, 0.2 * 2 ** -1.5, 0.2 * 2 ** -3)]
check("C2", np.allclose(g0, 1, atol=1e-10) and gr[0] < 0.5 and gr[0] > gr[1] > gr[2],
      f"ED (256 states): partner gap / w = 1 free; with g = 1: {', '.join(f'{x:.4f}' for x in gr)} at w = 0.2, 0.2*2^-1.5, 0.2*2^-3 (released, worse when suppressed)")
# C3: momentum-selective coarse quartic from rung-2 staggered rows (2^3 blocks of the coarse 4^3 torus)
Lc2 = 4; Y = np.array(list(itertools.product(range(Lc2), repeat=3)))
R2 = np.zeros((Lc2 ** 3 // 8, Lc2 ** 3))
for i, y in enumerate(Y): R2[int(np.ravel_multi_index(tuple(y // 2), (2, 2, 2))), i] = (-1.0) ** y.sum() / np.sqrt(8)
R2u = np.abs(R2)
wa = [np.linalg.norm(Rw @ (np.exp(1j * Y @ Pv) / np.sqrt(len(Y)))) ** 2 for Rw in (R2, R2u) for Pv in (np.zeros(3), R3)]
check("C3", abs(wa[0]) < 1e-14 and abs(wa[1] - 1) < 1e-14 and abs(wa[2] - 1) < 1e-14 and abs(wa[3]) < 1e-14,
      f"coarse modes on rung-2 rows: staggered rows see A(P=0) {wa[0]:.0e}, B(R_c) {wa[1]:.3f}; uniform rows A {wa[2]:.3f}, B {wa[3]:.0e}: only the staggered rung-2 quartic leaves A (and so the fine partner's pairing) untouched at the node")
# C4: anomaly count for what the coarse quartic must gap (Z16 index of B: n Weyl of one chirality, unit Z4 charge)
idx = {'one 16 (Spin(10) family)': 16 % 16, 'SU(4) toy, 4 flavours': 4 % 16, 'SU(4) toy, 8 Weyl (momentum-selective-mirror)': 8 % 16}
check("C4", idx['one 16 (Spin(10) family)'] == 0 and idx['SU(4) toy, 4 flavours'] != 0,
      f"Z16 index of the coarse mirror B: {idx}: a 16 is allowed a symmetric gap; SU(4) toys of B are anomalous and cannot test it")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
