AUDIT_INPUT_PATHS = ('docs/THE_COMPOSITE_TWIST_WALK_IS_A_FIVE_LAYER_CUBE_LOCAL_CIRCUIT_AND_FREEZING_ONE_COPY_LEAVES_ONE_L_AND_ONE_R_PER_NODE_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""twist-local-single: composite TWIST (CTWIST) on one-qubit sites -- cube-local layers, the eta doubling,
and the light content per node.

Self-contained (numpy + scipy), seeded. Rebuilds CL-1's 2^3 cell (one fermion mode per site, face phase -1,
Bloch over 2Z^3, 8 cell states), the 12 tetrahedral rotations T with CL-1's site gauges V, the cell spin sigma,
the cell taste doublet tau, CL-1's chirality chi, and CTWIST U(K) = f + i(h1 tau1 + h2 tau2 + tau3 g.sigma).
  A. Layers: exact no-go for any even.odd.even product of cube-local layers (this includes CL-1's own
     two-layer shape); exact factorisation into five cube-local layers (even.odd.even.odd.even) on the two
     tilings; finite search for a factorisation whose layers each commute with the site rotations.
  B. The eta doubling: Schur/Kramers structure at the T-fixed nodes; the chirality-agreement sector
     (1 + chi tau3)/2; rule FREEZE (the disagreeing sector does not hop); its content and its layers.
  C. The label mirror term (1 - tau3)/2: what a free term does to the remaining R Weyl.
"""
import itertools as it
import numpy as np
from scipy.linalg import expm, null_space
from scipy.optimize import minimize_scalar

AUDIT_TIMEOUT_SEC = 120
rng = np.random.default_rng(20261023)
NPASS = NFAIL = 0
w = np.exp(2j * np.pi / 3)


def check(name, ok, detail=""):
    global NPASS, NFAIL
    ok = bool(ok); NPASS += ok; NFAIL += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail else ""))


def nullsp(rows):
    return null_space(np.vstack(rows), rcond=1e-9)


def cm(o):
    return np.kron(o, np.eye(8)) - np.kron(np.eye(8), o.T)


def axang(R):
    ev, vv = np.linalg.eig(R)
    n = np.real(vv[:, np.argmin(abs(ev - 1))])
    th = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    return (n if np.allclose(expm(th * K), R) else -n), th


ROTS = []
for p in it.permutations(range(3)):
    for sg in it.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[p[i], i] = sg[i]
        if np.linalg.det(R) > 0:
            ROTS.append(R)
C3d = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0.0]])
TI = [n for n, R in enumerate(ROTS) if abs(np.trace(R)) < 1e-9 or np.allclose(R, np.diag(np.diag(R)))]
iC3 = next(n for n, R in enumerate(ROTS) if np.allclose(R, C3d))
CELL = list(it.product([0, 1], repeat=3)); A = np.array(CELL)
IDX = {a: 4 * a[0] + 2 * a[1] + a[2] for a in CELL}


def eta_s(i, a):
    return [1, (-1) ** a[0], (-1) ** (a[0] + a[1])][i]


def Wl(i, k, odd):
    M = np.zeros((8, 8), complex)
    for a in CELL:
        if a[i] == (1 if odd else 0):
            b = list(a); b[i] = 1 - a[i]; b = tuple(b)
            ph = np.exp(2j * k[i]) if odd else 1
            M[IDX[b], IDX[a]] = eta_s(i, a) * ph; M[IDX[a], IDX[b]] = eta_s(i, a) * np.conj(ph)
    return M


Re = sum(Wl(i, np.zeros(3), 0) for i in range(3)) / np.sqrt(3)


def U1(k, eps=0.3):
    return expm(1j * eps * sum(Wl(i, k, 1) for i in range(3)) / np.sqrt(3)) @ expm(-1j * eps * Re)


hh = 1e-6
Av = []
for i in range(3):
    d = np.zeros(3); d[i] = hh; Av.append(1j * (U1(d) - U1(-d)) / (2 * hh))
Ah = [a / np.sqrt(np.trace(a @ a).real / 8) for a in Av]
S = [-0.25j * (Ah[(i + 1) % 3] @ Ah[(i + 2) % 3] - Ah[(i + 2) % 3] @ Ah[(i + 1) % 3]) for i in range(3)]
chi = 1j * Ah[0] @ Ah[1] @ Ah[2]
kt = [rng.uniform(-1, 1, 3) for _ in range(2)]
V = {}
for n in TI:
    P = np.zeros((8, 8))
    for a in CELL:
        b = tuple(np.rint(ROTS[n] @ (np.array(a) - .5) + .5).astype(int)); P[IDX[b], IDX[a]] = 1
    for sgn in it.product([1, -1], repeat=8):
        Vg = np.diag(sgn) @ P
        if all(np.allclose(Vg @ U1(k) @ Vg.T, U1(ROTS[n] @ k)) for k in kt):
            V[n] = Vg; break
VT = list(V.values())
nl, th = axang(ROTS[iC3])
t = expm(-1j * th * sum(nl[i] * S[i] for i in range(3))).conj().T @ V[iC3]
if not np.allclose(np.linalg.matrix_power(t, 3), np.eye(8), atol=1e-6):
    t = -t
PL = (np.eye(8) + chi) / 2; PR = np.eye(8) - PL
sig = [2 * s for s in S]
tau3 = (t - t.conj().T) / (1j * np.sqrt(3)); tau3 = (tau3 + tau3.conj().T) / 2
Pw = (np.eye(8) + tau3) / 2; Pb = np.eye(8) - Pw
Cb = nullsp([cm(o) for o in sig + [chi]])
Yr = (Cb @ rng.normal(size=Cb.shape[1])).reshape(8, 8)
tp = np.zeros((8, 8), complex)
for P in (PL, PR):
    Zb = P @ Pw @ Yr @ Pb @ P; tp += Zb / np.sqrt(np.trace(Zb @ Zb.conj().T).real / 2)
tau1 = tp + tp.conj().T; tau2 = -1j * (tp - tp.conj().T)
gam = [tau1, tau2] + [tau3 @ s for s in sig]


def Uc(K):
    c, s = np.cos(K), np.sin(K)
    H = (np.sqrt(2) / 3) * (c[0] + np.conj(w) * c[1] + w * c[2])
    return c.sum() / 3 * np.eye(8) + 1j * (H * tp + np.conj(H) * tp.conj().T + (s @ np.array(gam[2:]).reshape(3, 64)).reshape(8, 8) / np.sqrt(3))


Kr = [rng.uniform(-np.pi, np.pi, 3) for _ in range(5)]
cov = max(np.linalg.norm(V[n] @ Uc(K) @ V[n].T - Uc(ROTS[n] @ K)) for n in TI for K in Kr)
uni = max(np.linalg.norm(Uc(K) @ Uc(K).conj().T - np.eye(8)) for K in Kr)
check("A0 rebuild: CTWIST on CL-1's cell is unitary and T-covariant with CL-1's site gauges V",
      uni < 1e-12 and cov < 1e-12 and len(VT) == 12, f"unitarity {uni:.1e}, T residual {cov:.1e}")

print("== A. cube-local layers on the two tilings ==")


def coef(i, s, U):
    acc = np.zeros((8, 8), complex)
    for m in range(8):
        K = np.zeros(3); K[i] = 2 * np.pi * m / 8; acc += U(K) * np.exp(-1j * s * K[i])
    return acc / 8


def rproj(M):
    u, s, vh = np.linalg.svd(M); r = int((s > 1e-9).sum()); return u[:, :r] @ u[:, :r].conj().T, r


Pr = [rproj(coef(i, 1, Uc)) for i in range(3)]
jd = []
for a in CELL:
    X = np.eye(8)
    for i in range(3):
        X = X @ (Pr[i][0] if a[i] == 0 else np.eye(8) - Pr[i][0])
    jd.append(int(np.linalg.matrix_rank(X, tol=1e-9)))
comm = max(np.linalg.norm(Pr[i][0] @ Pr[j][0] - Pr[j][0] @ Pr[i][0]) for i in range(3) for j in range(i))
check("A1 exact no-go for even.odd.even (C1 D C2 D^+ C3, which contains CL-1's odd.even shape): it needs the "
      "z_i ranges to cut the cell into 8 one-dim vertex spaces; CTWIST's ranges commute but their joint spaces "
      "have dims (2,2,2,2,0,0,0,0) -- two states on each vertex of one tetrahedron",
      [p[1] for p in Pr] == [4, 4, 4] and comm < 1e-12 and sorted(jd) == [0, 0, 0, 0, 2, 2, 2, 2],
      f"ranks {[p[1] for p in Pr]}, joint dims {jd}")
ng = 5
Ks = np.array(list(it.product(2 * np.pi * np.arange(ng) / ng, repeat=3)))
Dk = np.exp(-1j * Ks @ A.T)


def polar(Y):
    u, s, vh = np.linalg.svd(Y); return vh.conj().T @ u.conj().T


def lay(C, odd):
    return Dk[:, :, None] * C[None] * Dk.conj()[:, None, :] if odd else np.broadcast_to(C, (len(Ks), 8, 8))


def search(Ut, pat, iters, seed, covar):
    r = np.random.default_rng(seed)
    avg = (lambda Y: sum(v @ Y @ v.T for v in VT) / 12) if covar else (lambda Y: Y)
    Cs = [polar(avg(r.normal(size=(8, 8)) + 1j * r.normal(size=(8, 8)))) for _ in pat]
    I = np.broadcast_to(np.eye(8), (len(Ks), 8, 8))
    for _ in range(iters):
        for j in range(len(pat)):
            L = I.copy(); R = I.copy()
            for m in range(j): L = L @ lay(Cs[m], pat[m])
            for m in range(j + 1, len(pat)): R = R @ lay(Cs[m], pat[m])
            Y = R @ Ut.conj().transpose(0, 2, 1) @ L
            if pat[j]: Y = Dk.conj()[:, :, None] * Y * Dk[:, None, :]
            Cs[j] = polar(avg(Y.sum(0)))
    Pp = I.copy()
    for m in range(len(pat)): Pp = Pp @ lay(Cs[m], pat[m])
    return np.sqrt(np.mean(np.sum(abs(Pp - Ut) ** 2, axis=(1, 2)))), Cs


def prod(Cs, pat, K):
    D = np.diag(np.exp(-1j * A @ K)); P = np.eye(8)
    for C, o in zip(Cs, pat): P = P @ (D @ C @ D.conj().T if o else C)
    return P


P5 = (0, 1, 0, 1, 0)


def factor(U, label):
    Ut = np.array([U(K) for K in Ks])
    for s in range(1, 9):
        r, Cs = search(Ut, P5, 1500, s, False)
        if r < 1e-10: break
    off = max(np.linalg.norm(prod(Cs, P5, K) - U(K)) for K in [rng.uniform(-3, 3, 3) for _ in range(4)])
    nz = [int((abs(C) > 1e-9).sum()) for C in Cs]
    ninv = min(max(np.linalg.norm(v @ C @ v.T - C) for v in VT) for C in Cs)
    return r, off, nz, ninv, Ut


r5, off5, nz5, ninv5, UtC = factor(Uc, "CTWIST")
check("A2 CTWIST factorises EXACTLY into five cube-local layers even.odd.even.odd.even on CL-1's two tilings "
      "(degree <= 2 per direction, so the 5^3 grid identifies the product; off-grid check too)",
      r5 < 1e-10 and off5 < 1e-10, f"grid rms {r5:.1e}, off-grid {off5:.1e}, nonzero gate entries {nz5}")
fl = {}
for pat in [(0, 1, 0, 1, 0), (0, 1, 0, 1, 0, 1, 0), (0, 1, 0, 1, 0, 1, 0, 1, 0)]:
    fl[len(pat)] = min(search(UtC, pat, 250, 100 + s, True)[0] for s in range(5))
check("A3 finite diagnostic: with every layer commuting with the 12 site rotations (frames = V), no "
      "factorisation found at depth 5, 7, 9 (rms floor stays O(1)); the found layers are not T-invariant",
      min(fl.values()) > 0.5 and ninv5 > 0.5, f"floors {dict((k, round(v, 3)) for k, v in fl.items())}; "
      f"min layer T-noninvariance {ninv5:.2f}")

print("== B. the eta doubling ==")
Tinv = nullsp([cm(v) for v in VT])
tq = max(np.linalg.norm(Tinv[:, j].reshape(8, 8) @ s - s @ Tinv[:, j].reshape(8, 8)) for j in range(Tinv.shape[1]) for s in sig)
td = max(np.linalg.norm(Pw @ Tinv[:, j].reshape(8, 8) @ Pb) for j in range(Tinv.shape[1]))
check("B1 Schur/Kramers at the T-fixed nodes K = 0, R: every T-invariant on-cell operator commutes with sigma and "
      "tau3 (dim 8 = M2 + M2 on the eta copies), so for ANY T-covariant cell walk every level at a node is a "
      "2-fold spinor irrep; free terms move node quasienergies but can never gap a node Weyl", tq < 1e-9 and td < 1e-9
      and Tinv.shape[1] == 8, f"dim {Tinv.shape[1]}, max [Q,sigma] {tq:.0e}")
Cm = nullsp([cm(o) for o in sig + [tau1, tau2, tau3]])
Ex = None
for j in range(Cm.shape[1]):
    e = Cm[:, j].reshape(8, 8); a = (e - chi @ e @ chi) / 2
    if np.linalg.norm(a) > 1e-6: Ex = a + a.conj().T; break
Ex = Ex / np.sqrt(np.trace(Ex @ Ex).real / 8)
tE = max(np.linalg.norm(v @ Ex @ v.T - Ex) for v in VT)
check("B2 the eta copy algebra (commutant of sigma, tau) is M2 = <chi, eta_x>, and T acts on it TRIVIALLY: no "
      "rotation tells the two eta copies apart; only cell operators (chi) can", Cm.shape[1] == 4 and tE < 1e-9
      and np.allclose(Ex @ chi + chi @ Ex, 0), f"commutant dim {Cm.shape[1]}, T action on eta_x {tE:.0e}")
Y = Pw + Pb @ Ex
UA = lambda K: Y @ Uc(K) @ Y.conj().T
Pp = (np.eye(8) + chi @ tau3) / 2; Pm = np.eye(8) - Pp
ca = max(np.linalg.norm(UA(K) @ Pp - Pp @ UA(K)) for K in Kr)
sw = max(np.linalg.norm(UA(K) @ Ex - Ex @ UA(K)) for K in Kr) + np.linalg.norm(Ex @ Pp @ Ex - Pm)
check("B3 chirality agreement: the T-invariant cell relabelling Y = P_w + P_wbar eta_x gives U_A = Y U Y^+ "
      "(taste flips tau_1,2 eta_x) conserving the sector chi tau3 = +1 where CL-1's chirality agrees with the "
      "walk's; eta_x is a symmetry swapping the two sectors, so the choice of sector is not lopsided",
      ca < 1e-12 and sw < 1e-12 and max(np.linalg.norm(v @ Y @ v.T - Y) for v in VT) < 1e-9, f"{ca:.0e}, {sw:.0e}")
UF = lambda K: Pp @ UA(K) + Pm @ (1j * tau3)
uF = max(np.linalg.norm(UF(K) @ UF(K).conj().T - np.eye(8)) for K in Kr)
cF = max(np.linalg.norm(V[n] @ UF(K) @ V[n].T - UF(ROTS[n] @ K)) for n in TI for K in Kr)
g12 = np.linspace(-np.pi, np.pi, 12, endpoint=False)
gap0 = gapP = 9.0
for K in map(np.array, it.product(g12, repeat=3)):
    th = np.angle(np.linalg.eigvals(UF(K)))
    if not np.allclose(K, 0): gap0 = min(gap0, abs(th).min())
    if not np.allclose(np.cos(K), -1): gapP = min(gapP, (np.pi - abs(th)).min())
check("B4 rule FREEZE (the disagreeing sector does not hop; it ticks i tau3, quasienergies +-pi/2): unitary, "
      "T-covariant; quasienergy 0 only at K = 0 and pi only at R on a 12^3 grid; the frozen copy sits pi/2 "
      "from both", uF < 1e-12 and cF < 1e-12 and gap0 > 0.1 and gapP > 0.1,
      f"unitarity {uF:.0e}, T {cF:.0e}, min |theta| off K=0 {gap0:.3f}, min |pi-theta| off R {gapP:.3f}")


def weyl(U, K0):
    out = []
    for a in (1, -1):
        Pq = Pp @ (np.eye(8) + a * tau3) / 2; vv, Bv = np.linalg.eigh(Pq); B = Bv[:, vv > 0.5]
        Ad = []
        for i in range(3):
            d = np.zeros(3); d[i] = hh
            Ad.append(B.conj().T @ (1j * (U(K0 + d) - U(K0 - d)) / (2 * hh) @ U(K0).conj().T) @ B)
        M = np.array([[np.trace(Ad[i] @ B.conj().T @ sig[j] @ B).real / 2 for j in range(3)] for i in range(3)])
        dq = np.linalg.det(B.conj().T @ V[iC3] @ B)
        out.append(("L" if np.linalg.det(M) > 0 else "R", B.shape[1], [x for x in range(3) if np.isclose(dq, w ** (2 * x))]))
    return sorted(out)


wz, wr = weyl(UF, np.zeros(3)), weyl(UF, np.pi * np.ones(3))
check("B5 light content under FREEZE: exactly one L Weyl (q = 2) and one R Weyl (q = 1) at each node, 2 L + 2 R in "
      "all (half of CTWIST's 4 + 4); by B1 Schur no T-invariant L-R mass (characters differ)",
      wz == wr == [("L", 2, [2]), ("R", 2, [1])], f"K=0 {wz}; R {wr}")
r5F, off5F, nzF, _, _ = factor(UF, "FREEZE")
check("B6 the FREEZE walk also factorises exactly into five cube-local layers (no nearest-neighbour bend)",
      r5F < 1e-10 and off5F < 1e-10, f"grid rms {r5F:.1e}, off-grid {off5F:.1e}")

print("== C. the label mirror term (1 - tau3)/2 ==")
PRl = Pp @ (np.eye(8) - tau3) / 2
UM = lambda K, ph: expm(1j * ph * PRl) @ UF(K)
e_line = np.array([1, 0.37, 0.21])
F = lambda k: np.linalg.svd(UM(k * e_line, np.pi / 2) - np.eye(8), compute_uv=False)[-1]
ks = np.linspace(0.05, np.pi, 300); j = int(np.argmin([F(k) for k in ks]))
fs = minimize_scalar(F, bounds=(ks[max(j - 1, 0)], ks[min(j + 1, 299)]), method="bounded", options={"xatol": 1e-12})
eR = np.angle(np.linalg.eigvals(Pp @ UM(np.pi * np.ones(3), np.pi) @ Pp + 0.5j * Pm))
nR0 = int(sum(abs(x) < 1e-9 for x in eR))
check("C1 a free label term exp(i phi (1 - tau3)/2) cannot gap the mirror: phi = pi/2 moves the R Weyl at K = 0 "
      "to pi/2 (still a 2-fold irrep) and opens a quasienergy-0 Fermi surface; phi = pi puts the R-labelled "
      "states at the R node at quasienergy 0", fs.fun < 1e-6 and nR0 == 2,
      f"sigma_min(U-1) {fs.fun:.1e} at k = {fs.x:.3f} on a generic line; R-node states at 0 for phi=pi: {nR0}")
lk = [np.linalg.norm(Pp @ (np.eye(8) + tau3) / 2 @ UF(np.array([1, .3, -.2]) * x) @ PRl) for x in (0.02, 0.01)]
check("C2 the label (1 - tau3)/2 is exact at the nodes and leaks O(K^2) under FREEZE (ratio 4 for K -> K/2)",
      abs(lk[0] / lk[1] - 4) < 0.05, f"ratio {lk[0] / lk[1]:.3f}")
print("verdict: CTWIST and FREEZE are five-layer cube-local circuits (no bend), layers not individually T-symmetric;")
print("FREEZE leaves one L(q=2)+one R(q=1) per node; separating the mirror needs an interacting (multi-family) term.")
print(f"TOTAL: PASS={NPASS} FAIL={NFAIL}")
