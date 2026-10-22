AUDIT_INPUT_PATHS = ('docs/THE_CUBE_TASTES_ARE_TWO_DOUBLETS_AND_NO_SYMMETRY_PROTECTS_A_FAMILY_TRIPLET_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""families-from-tastes: does the family number 3 follow from the cube / staggered taste structure?

Self-contained (numpy + scipy). Seeded. Exact finite checks on:
  A. CL-1's cell: one fermion mode per site, face phase -1 (anticommuting W_i), Margolus tick on
     2x2x2 cubes of both tilings, Bloch over 2Z^3 (8-dim cell), cube-centred rotations with site gauge.
  B. The merged ruleset's cell x qubit (16-dim): which locked hops exist, and the rotation-invariant
     Dirac masses for the qubit locked / unlocked.
  C. The one locked hop that gives a 1 + 3 (zero flux, qubit = spin, two modes per site): mass
     operators, protecting symmetries, link-field breaking of the only protecting charge.
  D. Measured mixing and the Z width against the family structures found.
"""
import itertools as it
import numpy as np
from scipy.linalg import expm, null_space

AUDIT_TIMEOUT_SEC = 60
rng = np.random.default_rng(20261022)
NPASS = NFAIL = 0


def check(name, ok, detail=""):
    global NPASS, NFAIL
    ok = bool(ok)
    NPASS += ok
    NFAIL += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail else ""))


def nullsp(rows):
    return null_space(np.vstack(rows), rcond=1e-9)


def inv(g):  # vec(g M g^dag) = M
    return np.kron(g, g.conj()) - np.eye(g.shape[0] ** 2)


def acomm(a):  # {a, M} = 0
    n = a.shape[0]
    return np.kron(a, np.eye(n)) + np.kron(np.eye(n), a.T)


sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]])
sz = np.diag([1.0, -1.0]).astype(complex)
SG, I2 = [sx, sy, sz], np.eye(2)


def axang(R):
    w, v = np.linalg.eig(R)
    n = np.real(v[:, np.argmin(abs(w - 1))])
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
C2x, C2y = np.diag([1, -1, -1.0]), np.diag([-1, 1, -1.0])


def cls(R):
    t = round(np.trace(R))
    return {3: "E", 0: "C3", 1: "C4"}.get(t, "C2" if np.allclose(R, np.diag(np.diag(R))) else "C2'")


# ------------------------------------------------------------------ A. CL-1 cell
print("== A. CL-1 cell: one mode per site, face phase -1, Margolus cube tick ==")
CELL = list(it.product([0, 1], repeat=3))
IDX = {a: 4 * a[0] + 2 * a[1] + a[2] for a in CELL}


def eta(i, a):
    return [1, (-1) ** a[0], (-1) ** (a[0] + a[1])][i]


def W_even(i):
    M = np.zeros((8, 8), complex)
    for a in CELL:
        if a[i] == 0:
            b = list(a); b[i] = 1; b = tuple(b)
            M[IDX[b], IDX[a]] = M[IDX[a], IDX[b]] = eta(i, a)
    return M


def W_odd(i, k):
    M = np.zeros((8, 8), complex)
    for a in CELL:
        if a[i] == 1:
            b = list(a); b[i] = 0; b = tuple(b)
            ph = np.exp(2j * k[i])
            M[IDX[b], IDX[a]] = eta(i, a) * ph
            M[IDX[a], IDX[b]] = eta(i, a) * np.conj(ph)
    return M


W = [W_even(i) for i in range(3)]
Re = sum(W) / np.sqrt(3)
s_copy = 1j * W[0] @ W[1] @ W[2] @ Re


def U(k, eps=0.3, mu=0.0, M=0.0):
    Ro = sum(W_odd(i, k) for i in range(3)) / np.sqrt(3)
    Ue = expm(-1j * (eps - mu / 2) * Re)
    if M:
        Cm = expm(1j * (M / 4) * (np.eye(8) - s_copy) @ Re)
        Ue = Cm @ Ue @ Cm
    return expm(1j * (eps + mu / 2) * Ro) @ Ue


ac = all(np.allclose(W[i] @ W[j] + W[j] @ W[i], 2 * (i == j) * np.eye(8)) for i in range(3) for j in range(3))
check("A1 face phase -1 <=> W_i anticommute; massless tick U(0) = 1 (all 8 cell states at the K=0 node)",
      ac and np.allclose(U(np.zeros(3)), np.eye(8)))
h = 1e-6
Av = []
for i in range(3):
    d = np.zeros(3); d[i] = h
    Av.append(1j * (U(d) - U(-d)) / (2 * h))
v2 = np.trace(Av[0] @ Av[0]).real / 8
Ah = [a / np.sqrt(v2) for a in Av]
cl = all(np.allclose(Ah[i] @ Ah[j] + Ah[j] @ Ah[i], 2 * (i == j) * np.eye(8), atol=1e-5) for i in range(3) for j in range(3))
S = [-0.25j * (Ah[(i + 1) % 3] @ Ah[(i + 2) % 3] - Ah[(i + 2) % 3] @ Ah[(i + 1) % 3]) for i in range(3)]
chi = 1j * Ah[0] @ Ah[1] @ Ah[2]
check("A2 velocity matrices A_i = i dU/dk_i form Cl(3): isotropic cone, spin su(2) S = -(i/4)eps[A,A]",
      cl and all(np.allclose(S[i] @ S[(i + 1) % 3] - S[(i + 1) % 3] @ S[i], 1j * S[(i + 2) % 3], atol=1e-5) for i in range(3)),
      f"v = {np.sqrt(v2):.4f} per tick at eps = 0.3")
# cube-centred rotations with a +-1 site gauge
cen = np.array([0.5, 0.5, 0.5])
SIGNS = list(it.product([1, -1], repeat=8))
kt = [rng.uniform(-1, 1, 3) for _ in range(2)]
V = []
for R in ROTS:
    P = np.zeros((8, 8))
    for a in CELL:
        b = tuple(np.rint(R @ (np.array(a) - cen) + cen).astype(int)); P[IDX[b], IDX[a]] = 1
    found = None
    for sgn in SIGNS:
        Vg = np.diag(sgn) @ P
        if all(np.allclose(Vg @ U(k) @ Vg.T, U(R @ k)) for k in kt):
            found = Vg; break
    V.append(found)
check("A3 all 24 cube-centred rotations are tick symmetries up to a +-1 site gauge (U(Rk) = V U(k) V^T)",
      all(v is not None for v in V))
iC4, iC3, iX, iY = [next(n for n, R in enumerate(ROTS) if np.allclose(R, Q)) for Q in (C4z, C3d, C2x, C2y)]
cm = V[iX] @ V[iY] @ V[iX].T @ V[iY].T
check("A4 the cell rep is spinorial (double cover): the compensated half-turns anticommute (phase-free test)",
      np.allclose(cm, -np.eye(8)))
tau = []
for n, R in enumerate(ROTS):
    rho = spinor(R, S)
    tau.append(rho.conj().T @ V[n])
okv = all(np.allclose(V[n] @ S[i] @ V[n].T, sum(ROTS[n][j, i] * S[j] for j in range(3)), atol=1e-5) for n in range(24) for i in range(3))
okt = all(np.allclose(t @ s, s @ t, atol=1e-5) for t in tau for s in S)
tc = tau[iX] @ tau[iY] @ np.linalg.inv(tau[iX]) @ np.linalg.inv(tau[iY])
check("A5 V = rho(spin) x tau(taste); the TASTE factor is projectively LINEAR: its half-turn lifts commute",
      okv and okt and np.allclose(tc, np.eye(8), atol=1e-6), "taste half-turn commutator = +1")
check("A6 chirality chi = iA1A2A3 commutes with every rotation and is traceless (2 tastes per sign)",
      all(np.allclose(V[n] @ chi, chi @ V[n], atol=1e-5) for n in range(24)) and abs(np.trace(chi)) < 1e-6)
# characters of taste per chirality, after fixing the linear sign (tau_C3^3 = +1)
if not np.allclose(np.linalg.matrix_power(tau[iC3], 3), np.eye(8), atol=1e-6):
    tau[iC3] = -tau[iC3]
def close(gens):
    G = [(np.eye(3), np.eye(8, dtype=complex))]
    front = list(G)
    while front and len(G) <= 48:
        new = []
        for R0, t0 in front:
            for Rg, tg in gens:
                R2, t2 = Rg @ R0, tg @ t0
                if not any(np.allclose(R2, a) and np.allclose(t2, b, atol=1e-6) for a, b in G):
                    G.append((R2, t2)); new.append((R2, t2))
        front = new
    return G


# remove the phase freedom: tau' = tau * i^(odd axis permutation) is a genuine linear rep
G = min((close([(ROTS[iC4], sg * 1j * tau[iC4]), (ROTS[iC3], tau[iC3])]) for sg in (1, -1)), key=len)
PL = (np.eye(8) + chi) / 2
ch = {}
for R0, t0 in G:
    ch.setdefault(cls(R0), set()).add(round(np.trace(PL @ t0).real / 2, 6))
E_irrep = {"E": 2, "C2": 2, "C3": -1, "C4": 0, "C2'": 0}
check("A7 taste per chirality (after the i^odd phase) = E of O (chars E,C2,C3,C4,C2' = 2,2,-1,0,0): 4 tastes = E + E, NOT 1 + 3",
      len(G) == 24 and all(ch[c] == {float(E_irrep[c])} for c in E_irrep), f"group order {len(G)}, chars {dict((k, sorted(v)) for k, v in ch.items())}")
check("A8 theorem: 1+3 is impossible: chi is a rotation-invariant traceless taste operator, so by Schur it "
      "would be a scalar on a 1 and on a 3, with trace +-1 +-3 != 0",
      all(abs(a + b) > 0 for a in (1, -1) for b in (3, -3)))
check("A9 the three axis half-turns act trivially on taste: taste rotations factor through S3 (axis "
      "permutations); E = (3 axes) - (singlet), i.e. d - 1 = 2 tastes per chirality",
      all(np.allclose(tau[n], np.eye(8), atol=1e-6) or np.allclose(tau[n], -np.eye(8), atol=1e-6)
          for n in (iX, iY)))
nsr = nullsp([acomm(a) for a in Ah] + [inv(V[iC4]), inv(V[iC3])])
mus = []
for j in range(nsr.shape[1]):
    Mm = nsr[:, j].reshape(8, 8)
    for Hm in ((Mm + Mm.conj().T) / 2, 1j * (Mm - Mm.conj().T) / 2):
        if np.linalg.norm(Hm) > 1e-8:
            mus.append(np.unique(np.round(abs(np.linalg.eigvalsh(Hm / np.linalg.norm(Hm) * np.sqrt(8))), 6)))
check("A10 every rotation-invariant cell mass gaps all 4 tastes equally (Schur on E+E with chi)",
      len(mus) > 0 and all(len(m) == 1 for m in mus), f"invariant mass space dim {nsr.shape[1]}")


def commutant(ops):
    n = ops[0].shape[0]
    return nullsp([np.kron(o, np.eye(n)) - np.kron(np.eye(n), o.T) for o in ops]).shape[1]


ks = [rng.uniform(-1.5, 1.5, 3) for _ in range(3)]
d0 = commutant([U(k) for k in ks]); dr = commutant([U(k) for k in ks] + V)
dm = commutant([U(k, mu=0.2, M=0.7) for k in ks])
check("A11 exact internal symmetries: commutant of the tick over all k has dim 8 (dim 1 with rotations); "
      "with CL-1's copy mass it is dim 1: no exact taste symmetry is left to protect any multiplet",
      d0 == 8 and dr == 1 and dm == 1, f"dims {d0}, {dr}, {dm}")
ev = np.sort(np.round(np.angle(np.linalg.eigvals(U(np.zeros(3), mu=0.2, M=0.7))), 6))
ok_cs = np.allclose(s_copy @ chi, chi @ s_copy, atol=1e-6) and all(np.allclose(s_copy @ a, a @ s_copy, atol=1e-6) for a in Ah)
check("A12 CL-1 copy sign commutes with A and chi; copy mass leaves 4 light states (+-mu) = 2 spin x 1 taste "
      "per chirality = ONE light Dirac family, and 4 heavy (+-(mu+M))",
      ok_cs and np.allclose(ev, [-0.9, -0.9, -0.2, -0.2, 0.2, 0.2, 0.9, 0.9]), f"k=0 phases {ev.tolist()}")

# ------------------------------------------------------------------ B. cell x qubit
print("== B. merged ruleset: cell x qubit (16 dims, one extra 2-level label per site) ==")


def Wcell(flux):
    X = np.array([[0, 1], [1, 0.0]]); Z = np.diag([1, -1.0]); I = np.eye(2)
    if flux:
        return [np.kron(np.kron(X, I), I), np.kron(np.kron(Z, X), I), np.kron(np.kron(Z, Z), X)]
    return [np.kron(np.kron(X, I), I), np.kron(np.kron(I, X), I), np.kron(np.kron(I, I), X)]


res = {}
for flux in (1, 0):
    Wc = Wcell(flux)
    for th in np.linspace(0, np.pi / 2, 13):
        a, b = np.cos(th), np.sin(th)
        Gq = [np.kron(Wc[i], a * I2 + b * SG[i]) for i in range(3)]
        Rq = sum(Gq) / np.sqrt(3)
        res[(flux, round(th, 4))] = np.allclose(Rq @ Rq, np.eye(16))
good = sorted(k for k, v in res.items() if v)
check("B1 hops W_i x (a + b sigma_i), face phase +-1: R^2 = 1 (CL-1's reflection) only for (pi flux, b = 0: "
      "qubit-blind) or (zero flux, a = 0: qubit = spin, no cell Clifford)",
      good == [(0, round(np.pi / 2, 4)), (1, 0.0)], f"solutions {good}")
I8, I16 = np.eye(8), np.eye(16)
A16 = [np.kron(a, I2) for a in Ah]


def u_q(R):
    return spinor(R, [g / 2 for g in SG])


lockg = [np.kron(V[n], u_q(ROTS[n])) for n in (iC4, iC3)]
fx, fy = [np.kron(tau[n], u_q(ROTS[n])) for n in (iX, iY)]
check("B2 qubit locked to the axes: flavour tau x u is SPINORIAL (its half-turn lifts anticommute, a phase-"
      "free test), so it holds no 1 and no 3; per chirality it is E x E_1/2 = G_3/2 (4-dim irreducible)",
      np.allclose(fx @ fy @ np.linalg.inv(fx) @ np.linalg.inv(fy), -I16, atol=1e-6))


def mass_spectra(gens):
    ns = nullsp([acomm(a) for a in A16] + [inv(g) for g in gens])
    out = []
    for j in range(ns.shape[1]):
        Mm = ns[:, j].reshape(16, 16)
        for Hm in ((Mm + Mm.conj().T) / 2, 1j * (Mm - Mm.conj().T) / 2):
            if np.linalg.norm(Hm) > 1e-8:
                e = np.round(abs(np.linalg.eigvalsh(Hm / np.linalg.norm(Hm) * 4)), 5)
                out.append(tuple(np.unique(e, return_counts=True)[1]))
    return ns.shape[1], out


dl, sl = mass_spectra(lockg)
du, su = mass_spectra([np.kron(V[n], I2) for n in (iC4, iC3)])
dq, sq = mass_spectra([np.kron(V[n], I2) for n in (iC4, iC3)] + [np.kron(I8, q) for q in SG])
check("B3 locked: every invariant Dirac mass gaps all 16 states equally (no 12 + 4 split exists)",
      all(m == (16,) for m in sl), f"dim {dl}")
check("B4 unlocked: invariant masses split 16 only as 8 + 8 (two E-doublets x spin x chirality), never 12 + 4",
      all(m in [(16,), (8, 8)] for m in su) and (8, 8) in su, f"dim {du}")
check("B5 qubit-blind hop keeps SU(2)_qubit exact; then every invariant mass is flavour-universal",
      all(m == (16,) for m in sq), f"dim {dq}")

# ------------------------------------------------------------------ C. qubit = spin (zero flux)
print("== C. zero-flux hop W_i x sigma_i (qubit = spin; 2 modes per site): the 1 + 3 corners ==")
CRN = list(it.product([0, 1], repeat=3))
hw = [sum(c) for c in CRN]
Ac = [np.kron(np.diag([np.cos(np.pi * c[i]) for c in CRN]), SG[i]) for i in range(3)]
chic = np.kron(np.diag([(-1.0) ** w for w in hw]), I2)


def Tn(n):
    return np.kron(np.diag([np.exp(1j * np.pi * np.dot(n, c)) for c in CRN]), I2)


def rotc(R):
    P = np.zeros((8, 8))
    for c in CRN:
        d = tuple((np.rint(R @ np.array(c)) % 2).astype(int)); P[CRN.index(d), CRN.index(c)] = 1
    return np.kron(P, u_q(R))


Vc = [rotc(C4z), rotc(C3d)]
okc = all(np.allclose(Vv @ Ac[i] @ Vv.conj().T, sum(R[j, i] * Ac[j] for j in range(3))) for Vv, R in zip(Vc, [C4z, C3d]) for i in range(3))
check("C1 8 Weyl corners, chirality (-1)^hw, rotation forces the qubit locked; L = hw0 + hw2 = 1 + 3, "
      "R = hw1 + hw3 = 3 + 1 (the triplet is the axis vector: 3 = d)",
      okc and (np.allclose(1j * Ac[0] @ Ac[1] @ Ac[2], chic) or np.allclose(1j * Ac[0] @ Ac[1] @ Ac[2], -chic))
      and sorted(hw).count(1) == 3 and sorted(hw).count(2) == 3)
Ps = np.kron(np.diag([1.0 if w in (0, 3) else 0.0 for w in hw]), I2)
base = [acomm(a) for a in Ac] + [inv(g) for g in Vc]


def masses(extra):
    ns = nullsp(base + extra)
    vec = []
    for j in range(ns.shape[1]):
        Mm = ns[:, j].reshape(16, 16)
        for Hm in ((Mm + Mm.conj().T) / 2, 1j * (Mm - Mm.conj().T) / 2):
            if np.linalg.norm(Hm) > 1e-8:
                vec.append((np.linalg.norm(Ps @ Hm @ Ps), np.linalg.norm((I16 - Ps) @ Hm @ (I16 - Ps))))
    return ns.shape[1], (np.linalg.matrix_rank(np.array(vec), 1e-8) if vec else 0)


d_all, _ = masses([inv(Tn(np.eye(3)[i])) for i in range(3)])
check("C2 exact one-site translations forbid every mass (paired corners carry different characters)", d_all == 0)
fcc = [inv(Tn(n)) for n in ([1, 1, 0], [1, 0, 1], [0, 1, 1])]
d_f, r_f = masses(fcc)
check("C3 with face-diagonal (fcc) translations + rotations: 4 real masses, singlet and triplet INDEPENDENT "
      "(rank 2): a light triplet needs m_t = 0, a codimension-2 tuning", d_f == 4 and r_f == 2)
sep = []
for n in it.product([0, 1], repeat=3):
    d, r = masses(fcc + [inv(Tn(n))])
    sep.append((n, d, r))
check("C4 no translation class separates them: each of the 8 classes allows both or forbids both",
      all((d, r) in [(4, 2), (0, 0)] for _, d, r in sep), str([(n, d) for n, d, _ in sep]))
Q = np.array([1, 1, 1])
Me = np.zeros((16, 16), complex)
for a, c in enumerate(CRN):
    b = CRN.index(tuple((np.array(c) + Q) % 2)); Me[2 * b:2 * b + 2, 2 * a:2 * a + 2] = I2
ms = np.linalg.norm(Ps @ Me @ Ps) / 2; mt = np.linalg.norm((I16 - Ps) @ Me @ (I16 - Ps)) / np.sqrt(12)
check("C5 the shortest mass, on-site staggered (-1)^(x+y+z), gaps singlet and triplet EQUALLY (P0 picks no 3)",
      abs(ms - mt) < 1e-12 and ms > 0)
Z4 = 1j * I16
check("C6 the Z4 (i on every mode) is taste-blind: it leaves every Dirac mass allowed, so it cannot separate",
      np.allclose(inv(Z4), 0))


def fval(c):
    cc = np.cos(np.pi * np.array(c)); return cc.sum() - 3 * np.prod(cc)


fq = {c: fval(c) for c in CRN}
okf = np.isclose(fq[(0, 0, 0)], fq[(1, 1, 1)]) and all(not np.isclose(fq[tuple(np.eye(3, dtype=int)[i])], fq[tuple(1 - np.eye(3, dtype=int)[i])]) for i in range(3))
check("C7 a swap-type protecting charge exists only as a FREE-hop charge: Q_f = sum_k f(k) n_k with "
      "f = sum cos k_i - 3 prod cos k_i (range 3) allows the singlet mass and forbids the triplet's; the only "
      "finite-range unitary scalars are translations, which do not (C4)", okf,
      f"f: singlet {fq[(0,0,0)]:.0f},{fq[(1,1,1)]:.0f}; triplet {fq[(1,0,0)]:.0f} vs {fq[(0,1,1)]:.0f}")
L = 4
N = L ** 3
site = lambda x: (x[0] % L) * L * L + (x[1] % L) * L + (x[2] % L)


def build(theta):
    T = []
    for i in range(3):
        M = np.zeros((N, N), complex)
        for x in it.product(range(L), repeat=3):
            y = list(x); y[i] += 1
            M[site(y), site(x)] = np.exp(1j * theta[i][x])
        T.append(M)
    H = sum(np.kron((T[i] - T[i].conj().T) / 2j, SG[i]) for i in range(3))
    Cc = [np.kron((T[i] + T[i].conj().T) / 2, I2) for i in range(3)]
    prod = sum(Cc[p[0]] @ Cc[p[1]] @ Cc[p[2]] for p in it.permutations(range(3))) / 6
    return H, sum(Cc) - 3 * prod


th0 = [np.zeros((L, L, L)) for _ in range(3)]
H0, Q0 = build(th0)
thA = [0.3 * rng.standard_normal((L, L, L)) for _ in range(3)]
HA, QA = build(thA)
r0 = np.linalg.norm(H0 @ Q0 - Q0 @ H0); rA = np.linalg.norm(HA @ QA - QA @ HA) / np.linalg.norm(QA)
check("C8 that charge is broken by any link field: [Q_f, H] = 0 on free links, O(1) with random link phases "
      "(covariantised, 4^3 torus): gauge couplings regenerate triplet masses (not protected)",
      r0 < 1e-10 and rA > 1e-2, f"free {r0:.1e}, linked {rA:.3f}")

# ------------------------------------------------------------------ D. measurement
print("== D. families as a rotation triplet vs measured masses, mixing and the Z width ==")


def comm_dim3(gens):
    return nullsp([np.kron(g, np.eye(3)) - np.kron(np.eye(3), g.T) for g in gens]).shape[1]


sub = {"O": ROTS, "D4": [C4z, C2x], "D3": [C3d, np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1.0]])],
       "D2": [C2x, C2y], "C4": [C4z], "C3": [C3d]}
dims = {k: comm_dim3(g) for k, g in sub.items()}
check("D1 a T1 family triplet: O keeps 3 degenerate; D4, D3 keep a degenerate pair (1+2); three distinct "
      "masses need the residual group to be D2, C4, C3 or smaller", dims == {"O": 1, "D4": 2, "D3": 2, "D2": 3, "C4": 3, "C3": 3},
      str(dims))
F = np.array([[np.exp(2j * np.pi * a * b / 3) for b in range(3)] for a in range(3)]) / np.sqrt(3)
Vus_meas, Vud_meas = 0.22500, 0.97435
check("D2 mixing: a shared residual gives V = permutation (|V_us| = 0 vs 0.2250); C3 vs D2 residuals give "
      "|V_ij| = 1/sqrt3 (|V_ud| 0.577 vs 0.97435): both excluded, so masses+mixing need generic breaking "
      "(no prediction)", abs(abs(F[0, 0]) - 1 / np.sqrt(3)) < 1e-12 and abs(1 / np.sqrt(3) - Vud_meas) > 0.3 and Vus_meas > 0.2)
chars = []
for i in range(3):
    c1 = np.eye(3, dtype=int)[i]; c2 = 1 - c1
    chars.append(tuple(np.round([np.exp(1j * np.pi * np.dot(n, c1)).real for n in ([1, 1, 0], [1, 0, 1], [0, 1, 1])], 6)))
check("D3 in C the three triplet pairs carry distinct fcc characters, so every fcc-invariant mass matrix is "
      "family-diagonal: no mixing until fcc is broken in the family sector (a further supplied breaking)",
      len(set(chars)) == 3, str(chars))
Nnu, sNnu = 2.9840, 0.0082
check("D4 Z width: N_nu = 2.9840 +- 0.0082 (LEP) excludes 4 degenerate light (B5/A10) and 1 "
      "(CL-1 copy mass, A12); 3 is reached only by the tuned m_t = 0 of C3",
      (4 - Nnu) / sNnu > 100 and (Nnu - 1) / sNnu > 200, f"{(4-Nnu)/sNnu:.0f} and {(Nnu-1)/sNnu:.0f} sigma")
print(f"TOTAL: PASS={NPASS} FAIL={NFAIL}")
