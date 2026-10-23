AUDIT_INPUT_PATHS = ('docs/THE_CELL_TASTE_DOUBLET_IS_A_GEOMETRIC_TETRAHEDRAL_TWIST_GIVING_A_ONE_QUBIT_CHIRAL_TURN_CHARGE_WALK_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""composite-twist: the TWIST walk with the flavour qubit replaced by the 2^3 cell's taste doublet.

Self-contained (numpy + scipy), seeded, exact free-band checks on CL-1's cell (one fermion mode per site,
face phase -1, Margolus cube tick on both tilings, Bloch over 2Z^3, 8 cell states):
  A. CL-1's own tick under the 12 tetrahedral rotations T (kept by the copy mass): taste characters,
     turn charges, allowed masses, exact internal symmetries, and whether a twisted turn is a symmetry.
  B. Composite TWIST: U(K) = f + i(h1 tau1 + h2 tau2 + tau3 g.sigma) on the same 8 cell states, with sigma the
     cell spin, tau the taste doublet whose turn character is the cell's own geometric one, and the CL-1
     chirality eta a spectator. Covariance, nodes, chiralities, turn charges, mass selection rules, leak.
"""
import itertools as it
import numpy as np
from scipy.linalg import expm, null_space

AUDIT_TIMEOUT_SEC = 60
rng = np.random.default_rng(20261023)
NPASS = NFAIL = 0
w = np.exp(2j * np.pi / 3)


def check(name, ok, detail=""):
    global NPASS, NFAIL
    ok = bool(ok); NPASS += ok; NFAIL += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail else ""))


def nullsp(rows):
    return null_space(np.vstack(rows), rcond=1e-9)


def cm(o, n=8):  # vec([o, M]) rows
    return np.kron(o, np.eye(n)) - np.kron(np.eye(n), o.T)


def axang(R):
    ev, vv = np.linalg.eig(R)
    n = np.real(vv[:, np.argmin(abs(ev - 1))])
    th = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    if not np.allclose(expm(th * K), R):
        n = -n
    return n, th


def spinor(R, gens):
    n, th = axang(R)
    return expm(-1j * th * sum(n[i] * gens[i] for i in range(3)))


ROTS = []
for p in it.permutations(range(3)):
    for sg in it.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[p[i], i] = sg[i]
        if np.linalg.det(R) > 0:
            ROTS.append(R)
C4z = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1.0]])
C3d = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0.0]])
TI = [n for n, R in enumerate(ROTS) if abs(np.trace(R)) < 1e-9 or np.allclose(R, np.diag(np.diag(R)))]

# ------------------------------------------------------------------ CL-1 cell
CELL = list(it.product([0, 1], repeat=3))
IDX = {a: 4 * a[0] + 2 * a[1] + a[2] for a in CELL}


def eta_s(i, a):
    return [1, (-1) ** a[0], (-1) ** (a[0] + a[1])][i]


def W_even(i):
    M = np.zeros((8, 8), complex)
    for a in CELL:
        if a[i] == 0:
            b = list(a); b[i] = 1; b = tuple(b)
            M[IDX[b], IDX[a]] = M[IDX[a], IDX[b]] = eta_s(i, a)
    return M


def W_odd(i, k):
    M = np.zeros((8, 8), complex)
    for a in CELL:
        if a[i] == 1:
            b = list(a); b[i] = 0; b = tuple(b)
            ph = np.exp(2j * k[i])
            M[IDX[b], IDX[a]] = eta_s(i, a) * ph
            M[IDX[a], IDX[b]] = eta_s(i, a) * np.conj(ph)
    return M


W = [W_even(i) for i in range(3)]
Re = sum(W) / np.sqrt(3)
s_copy = 1j * W[0] @ W[1] @ W[2] @ Re


def U1(k, eps=0.3, mu=0.0, M=0.0):
    Ro = sum(W_odd(i, k) for i in range(3)) / np.sqrt(3)
    Ue = expm(-1j * (eps - mu / 2) * Re)
    if M:
        Cm = expm(1j * (M / 4) * (np.eye(8) - s_copy) @ Re)
        Ue = Cm @ Ue @ Cm
    return expm(1j * (eps + mu / 2) * Ro) @ Ue


print("== A. CL-1's own cell tick under the tetrahedral rotations ==")
hh = 1e-6
Av = []
for i in range(3):
    d = np.zeros(3); d[i] = hh
    Av.append(1j * (U1(d) - U1(-d)) / (2 * hh))
Ah = [a / np.sqrt(np.trace(a @ a).real / 8) for a in Av]
S = [-0.25j * (Ah[(i + 1) % 3] @ Ah[(i + 2) % 3] - Ah[(i + 2) % 3] @ Ah[(i + 1) % 3]) for i in range(3)]
chi = 1j * Ah[0] @ Ah[1] @ Ah[2]
cen = np.array([0.5, 0.5, 0.5])
kt = [rng.uniform(-1, 1, 3) for _ in range(2)]
V = []
for R in ROTS:
    P = np.zeros((8, 8))
    for a in CELL:
        b = tuple(np.rint(R @ (np.array(a) - cen) + cen).astype(int)); P[IDX[b], IDX[a]] = 1
    for sgn in it.product([1, -1], repeat=8):
        Vg = np.diag(sgn) @ P
        if all(np.allclose(Vg @ U1(k) @ Vg.T, U1(R @ k)) for k in kt):
            V.append(Vg); break
iC4, iC3 = [next(n for n, R in enumerate(ROTS) if np.allclose(R, Q)) for Q in (C4z, C3d)]
check("A1 CL-1 cell rebuilt: all 24 cube-centred rotations are tick symmetries up to a +-1 site gauge; "
      "T = 12 of them", len(V) == 24 and len(TI) == 12)
ks = [rng.uniform(-1.5, 1.5, 3) for _ in range(8)]
dims = [nullsp([cm(U1(k)) for k in ks[:n]]).shape[1] for n in (3, 8)]
chic = min(np.linalg.norm(chi @ U1(k) - U1(k) @ chi) for k in ks)
check("A2 exact internal symmetries of the MASSLESS tick: commutant over 8 momenta has dim 1 (3 momenta "
      "give a spurious 8); the chirality chi and the taste doublet are not conserved away from K = 0",
      dims == [8, 1] and chic > 0.5, f"dims (3 k, 8 k) = {dims}; min ||[chi,U(k)]|| = {chic:.3f}")
t = spinor(ROTS[iC3], S).conj().T @ V[iC3]
if not np.allclose(np.linalg.matrix_power(t, 3), np.eye(8), atol=1e-6):
    t = -t
PL = (np.eye(8) + chi) / 2
PR = np.eye(8) - PL


def chars(P):  # taste characters of the turn on one chirality (per spin pair)
    e = np.linalg.eigvals(P @ t @ P)
    e = e[abs(e) > 0.5]
    return sorted(int(round(np.angle(x) / (2 * np.pi / 3))) % 3 for x in e)


cL, cR = chars(PL), chars(PR)
check("A3 under T each chirality's taste E splits into w + wbar: L carries both turn characters and so does R, "
      "so the turn charges are vector-like (q in {1,2} for L and for R)",
      cL == cR == [1, 1, 2, 2], f"L chars w^{cL}, R chars w^{cR}")
dT = nullsp([(np.kron(a, np.eye(8)) + np.kron(np.eye(8), a.T)) for a in Ah] + [cm(V[n]) for n in TI]).shape[1]
dO = nullsp([(np.kron(a, np.eye(8)) + np.kron(np.eye(8), a.T)) for a in Ah] + [cm(V[n]) for n in range(24)]).shape[1]
check("A4 K = 0 Dirac masses (anticommuting with the velocities): T allows more than O, one per character "
      "pair, so T never forbids an L-R mass on CL-1's cell", dT == 2 * dO and dO >= 1, f"dim O {dO}, dim T {dT}")
sc_T = all(np.allclose(V[n] @ s_copy @ V[n].T, s_copy, atol=1e-9) for n in TI)
sc_O = np.allclose(V[iC4] @ s_copy @ V[iC4].T, s_copy, atol=1e-9)
Pl = (np.eye(8) + s_copy) / 2 if np.allclose(s_copy @ s_copy, np.eye(8)) else None
ev = np.sort(np.round(np.angle(np.linalg.eigvals(U1(np.zeros(3), mu=0.2, M=0.7))), 6))
lightL = chars(PL @ (np.eye(8) + s_copy) / 2) if Pl is not None else None
lightR = chars(PR @ (np.eye(8) + s_copy) / 2) if Pl is not None else None
check("A5 the copy sign keeps T, breaks the 4-fold; its light family has L and R of the SAME turn character, "
      "and the T-invariant mass mu gaps it (light phases +-mu)",
      sc_T and not sc_O and lightL == lightR and len(lightL) == 2 and np.allclose(abs(ev[2:6]), 0.2),
      f"light L chars {lightL}, R chars {lightR}; K=0 phases {ev.tolist()}")
X = PR + PL @ (w * np.linalg.inv(t)) @ PL  # turn twist making both L tastes the same character
ok_tw = np.allclose(X @ X.conj().T, np.eye(8), atol=1e-6) and np.allclose(X @ t, t @ X, atol=1e-6)
res = min(np.linalg.norm(V[iC3] @ X @ U1(k) @ (V[iC3] @ X).conj().T - U1(C3d @ k)) for k in ks)
check("A6 a twisted turn (geometric turn times the taste phase that gives every L the same character) is NOT "
      "a symmetry of CL-1's tick: TWIST cannot be read off CL-1 by relabelling",
      ok_tw and res > 0.1, f"min residual over 8 momenta {res:.3f}")

# ------------------------------------------------------------------ B. composite TWIST
print("== B. composite TWIST on the same 8 cell states (sigma = cell spin, tau = taste, eta = chi) ==")
sig = [2 * s for s in S]
tau3 = (t - t.conj().T) / (1j * np.sqrt(3)); tau3 = (tau3 + tau3.conj().T) / 2
Pw = (np.eye(8) + tau3) / 2; Pb = np.eye(8) - Pw
Cb = nullsp([cm(o) for o in sig + [chi]])
Y = (Cb @ rng.normal(size=Cb.shape[1])).reshape(8, 8)
tp = np.zeros((8, 8), complex)
for P in (PL, PR):
    Zb = P @ Pw @ Y @ Pb @ P
    tp += Zb / np.sqrt(np.trace(Zb @ Zb.conj().T).real / 2)
tau1 = tp + tp.conj().T; tau2 = -1j * (tp - tp.conj().T)
anti = lambda a, b: np.allclose(a @ b + b @ a, 0, atol=1e-8)
gam = [tau1, tau2] + [tau3 @ s for s in sig]
alg = all(anti(gam[a], gam[b]) for a in range(5) for b in range(a)) and all(np.allclose(g @ g, np.eye(8), atol=1e-8) for g in gam) \
    and all(np.allclose(chi @ g, g @ chi, atol=1e-8) for g in gam)
chp = {n: np.trace(tp.conj().T @ V[n] @ tp @ V[n].T) / 4 for n in TI}
geo = all(np.isclose(chp[n], 1) for n in TI if np.allclose(ROTS[n], np.diag(np.diag(ROTS[n])))) and np.isclose(chp[iC3], np.conj(w))
check("B1 cell operators: sigma (spin from the velocities), tau (taste doublet), eta = chi; tau1, tau2, "
      "tau3 sigma_i are 5 anticommuting involutions commuting with eta; tau+ has character wbar under the "
      "turn and 1 under the half-turns: the twist is the cell's OWN geometric taste action", alg and geo,
      f"tau+ char under turn {np.round(chp[iC3], 4)}")


def Uc(K, sgn=1):
    c, s = np.cos(K), np.sin(K)
    f = c.sum() / 3
    H = (np.sqrt(2) / 3) * (c[0] + (np.conj(w) if sgn > 0 else w) * c[1] + (w if sgn > 0 else np.conj(w)) * c[2])
    return f * np.eye(8) + 1j * (H * tp + np.conj(H) * tp.conj().T + (s[0] * gam[2] + s[1] * gam[3] + s[2] * gam[4]) / np.sqrt(3))


Kr = [rng.uniform(-np.pi, np.pi, 3) for _ in range(6)]
uni = max(np.linalg.norm(Uc(K) @ Uc(K).conj().T - np.eye(8)) for K in Kr)
cov = max(np.linalg.norm(V[n] @ Uc(K) @ V[n].T - Uc(ROTS[n] @ K)) for n in TI for K in Kr)
covw = max(np.linalg.norm(V[n] @ Uc(K, -1) @ V[n].T - Uc(ROTS[n] @ K, -1)) for n in TI for K in Kr)
c4 = min(np.linalg.norm(V[iC4] @ Uc(K) @ V[iC4].T - Uc(C4z @ K)) for K in Kr)
flip = np.allclose(V[iC4] @ tau3 @ V[iC4].T, -tau3, atol=1e-8)
check("B2 the cell-nearest-neighbour walk is unitary and exactly covariant under all 12 T rotations with the "
      "plain site permutations (no supplied internal factor); the opposite twist is not; the 4-fold maps tau3 "
      "to -tau3 and is not a symmetry", uni < 1e-12 and cov < 1e-12 and covw > 0.1 and c4 > 0.1 and flip,
      f"unitarity {uni:.1e}, T residual {cov:.1e}, wrong twist {covw:.2f}, 4-fold {c4:.2f}")
N = 16
g1 = np.linspace(-np.pi, np.pi, N, endpoint=False)
nodes = []
for K in it.product(g1, repeat=3):
    K = np.array(K)
    if min(abs(np.angle(np.linalg.eigvals(Uc(K))) - a).min() for a in (0.0,)) < 1e-9 or np.allclose(Uc(K), -np.eye(8)):
        nodes.append(np.round(K / np.pi, 3).tolist())
fmin = min(np.sqrt(1 - (np.cos(K).sum() / 3) ** 2) for K in map(np.array, it.product(g1, repeat=3)) if not (np.allclose(np.cos(K), 1) or np.allclose(np.cos(K), -1)))
check("B3 nodes: exactly K = 0 (U = +1) and K = R = pi(1,1,1) of the cell zone (U = -1, quasienergy pi), "
      "each 8-fold; the R node is site momentum (pi/2)(1,1,1)",
      sorted(nodes) == [[-1.0, -1.0, -1.0], [0.0, 0.0, 0.0]] and np.allclose(Uc(np.zeros(3)), np.eye(8)),
      f"nodes {nodes}; smallest gap elsewhere on 16^3 {fmin:.3f}")


def chir(K0):
    res = []
    for a in (1, -1):
        for e in (1, -1):
            P = ((np.eye(8) + a * tau3) / 2) @ ((np.eye(8) + e * chi) / 2)
            vv, Bv = np.linalg.eigh(P); B = Bv[:, vv > 0.5]
            Ad = []
            for i in range(3):
                d = np.zeros(3); d[i] = hh
                Hd = 1j * (Uc(K0 + d) - Uc(K0 - d)) / (2 * hh) @ Uc(K0).conj().T
                Ad.append(B.conj().T @ Hd @ B)
            Sb = [B.conj().T @ s @ B for s in sig]
            M = np.array([[np.trace(Ad[i] @ Sb[j]).real / 2 for j in range(3)] for i in range(3)])
            tb = B.conj().T @ V[iC3] @ B
            dq = np.linalg.det(tb)
            qq = [qv for qv in (0, 1, 2) if np.isclose(dq, w ** (2 * qv))]
            res.append((a, e, int(np.sign(np.linalg.det(M))), qq[0] if qq else None,
                        np.allclose(sum(Ad[i] @ Ad[i] for i in range(3)) / 3, Ad[0] @ Ad[0], atol=1e-6)))
    return res


c0, cRn = chir(np.zeros(3)), chir(np.pi * np.ones(3))
L0 = [r for r in c0 if r[2] > 0]; R0 = [r for r in c0 if r[2] < 0]
same = all(a[:3] == b[:3] for a, b in zip(c0, cRn))
check("B4 each node holds 4 Weyl blocks (tau3 x eta); Weyl chirality = tau3 at BOTH nodes, eta a spectator: "
      "light content 4 L + 4 R (twice TWIST's, from the spectator eta)",
      len(L0) == 2 and len(R0) == 2 and all(r[0] == L0[0][0] for r in L0) and same,
      f"(tau3, eta, chirality, q) at 0: {[r[:4] for r in c0]}; at R: {[r[:4] for r in cRn]}")
qL = {r[3] for r in c0 + cRn if r[2] > 0}; qR = {r[3] for r in c0 + cRn if r[2] < 0}
check("B5 turn charges (det of the turn on a Weyl block = w^(2q)): every L has the same q and every R the other "
      "(the atomic TWIST pattern, with L = positive velocity determinant); the turn is a chiral Z3 forced by geometry",
      len(qL) == 1 and len(qR) == 1 and qL != qR and None not in qL | qR, f"q_L = {qL}, q_R = {qR}")
Tinv = nullsp([cm(V[n]) for n in TI])
offd = max(np.linalg.norm(Pw @ Tinv[:, j].reshape(8, 8) @ Pb) + np.linalg.norm(Pb @ Tinv[:, j].reshape(8, 8) @ Pw) for j in range(Tinv.shape[1]))
check("B6 every T-invariant on-cell operator is tau3-diagonal (Schur on 2(E1/2 x w) + 2(E1/2 x wbar)): no "
      "L-R mass exists at either node, for any T-keeping on-cell term", offd < 1e-9,
      f"T-invariant on-cell dim {Tinv.shape[1]}, max L-R block {offd:.1e}")
Q = (Tinv @ rng.normal(size=Tinv.shape[1])).reshape(8, 8); Q = Q + Q.conj().T
Qs = 1j * W[0] @ W[1] @ W[2] @ Re
pert = [expm(0.4j * Q) @ Uc(K0) @ expm(0.3j * Qs) for K0 in (np.zeros(3), np.pi * np.ones(3))]
ok7 = np.allclose(Qs, Qs.conj().T) and all(np.linalg.norm(Pw @ u @ Pb) < 1e-9 for u in pert)
eta_mix = nullsp([cm(V[n]) for n in TI] + [cm(tau3)]).shape[1]
check("B7 adding CL-1's copy sign and a random T-invariant on-cell term keeps L and R unmixed at both "
      "T-fixed nodes (they only shift node energies or mix the two eta copies within a chirality)",
      ok7 and eta_mix == Tinv.shape[1], f"T-invariant terms inside chiralities {eta_mix}")
lk = [np.linalg.norm(Pw @ Uc(np.array([1, 0.3, -0.2]) * x) @ Pb) for x in (0.02, 0.01)]
check("B8 on-cell filter (1 + tau3)/2: leak from L to R is O(K^2) (h vanishes to second order)",
      abs(lk[0] / lk[1] - 4) < 0.05, f"leak ratio for K -> K/2 = {lk[0] / lk[1]:.3f}")
Ng = 4
gK = 2 * np.pi * np.arange(Ng) / Ng
Ug = np.array([[[Uc(np.array([a, b, c])) for c in gK] for b in gK] for a in gK])
F = np.fft.ifftn(Ug, axes=(0, 1, 2))
supp = sorted(tuple(int(((x + Ng // 2) % Ng) - Ng // 2) for x in n) for n in it.product(range(Ng), repeat=3) if np.abs(F[n]).max() > 1e-12)
want = sorted([tuple(int(sg * (i == j)) for j in range(3)) for i in range(3) for sg in (1, -1)])
span = max(abs(a[0] - (b[0] + 2)) for a in CELL for b in CELL)
check("B9 range: U(K) is a pure nearest-cell hop: Fourier support on the 6 neighbouring cells only (no on-cell term); in site units a hop "
      "spans up to 3 lattice steps along an axis (CL-1's tick is two cube-local layers)", supp == want and span == 3,
      f"support {len(supp)} cells")
print("== verdict lines ==")
print("R10 premise (every light L with the same q != 0): MET, forced by the cell's own taste geometry.")
print("R11 premise (light and mirror at different momenta): NOT MET; separation is by tau3 label, O(K^2) leak.")
print("Cost: no second qubit per site; CL-1's tick is replaced by a cell-range walk; O -> T; eta doubling.")
print(f"TOTAL: PASS={NPASS} FAIL={NFAIL}")
