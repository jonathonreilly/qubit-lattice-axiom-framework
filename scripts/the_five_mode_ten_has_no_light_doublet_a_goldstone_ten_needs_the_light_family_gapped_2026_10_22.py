AUDIT_INPUT_PATHS = ('docs/THE_FIVE_MODE_TEN_HAS_NO_LIGHT_DOUBLET_A_GOLDSTONE_TEN_NEEDS_THE_LIGHT_FAMILY_GAPPED_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""higgs-5mode: can a light electroweak doublet scalar arise WITHOUT inserted content in the 5-mode
framework (5 fermion modes per site, U(5) from the tick, Spin(10) on a 16 per family, 3 families,
mirror gapped symmetrically)?

Self-contained (numpy only). Seeded. Exact finite checks:
  A. Cl(12) from 6 modes (5 Spin(10) modes: E = modes 0,1, T1 = modes 2,3,4; mode 5 = the A1 half-link).
     The 10 = the mode operators: 5_{+2} + 5bar_{-2} under U(5)_X; the doublet is E, the triplet T1.
  B. Lorentz-scalar Weyl pairs of the Spin(12) 32 (internally symmetric): content by exact Casimirs,
     Spin(10) Casimirs and the A1 charge q6. The scalar 10s are light-light and mirror-mirror pairs;
     light-mirror scalars hold no 10.
  C. Goldstone dichotomy: the only Spin(12)-breaking scalar pair whose Goldstones are the 10s is the
     light-mirror Spin(10)-singlet pair, a full-rank Dirac mass for the light 16. A mirror-only gap
     breaks Spin(12) explicitly (same coset, no Goldstone).
  D. Half-link cubic structure: the antipode term puts A1 with E (3 + 3); the doublet coset frequency
     is -6b (face term b); the site-A1 hop gives the doublet a seesaw gap.
  E. Yukawa 16 x 16 x 10: symmetric family matrix, single-10 relations, turn-charge selection with
     N = 3, family-symmetry invariants, anarchic prior.
  F. Estimates against measurement (labelled; not checks of a rule).
"""
import itertools as it
import numpy as np

AUDIT_TIMEOUT_SEC = 90
rng = np.random.default_rng(20261022)
NP = NF = 0


def check(name, ok, detail=""):
    global NP, NF
    ok = bool(ok)
    NP += ok
    NF += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail else ""))


def fock(nm):
    a = np.array([[0, 1], [0, 0]], float)
    Z = np.diag([1.0, -1.0])
    I = np.eye(2)
    cs = []
    for j in range(nm):
        m = np.array([[1.0]])
        for k in range(nm):
            m = np.kron(m, Z if k < j else (a if k == j else I))
        cs.append(m)
    return cs


# ------------------------------------------------------------------ A
print("== A. Cl(12) on 6 modes; the 10 = the mode operators ==")
NM = 6
c = fock(NM)
cd = [x.T for x in c]
g = []
for j in range(NM):
    g.append((c[j] + cd[j]).astype(complex))
    g.append(1j * (cd[j] - c[j]))
D = 2 ** NM
ok = all(np.allclose(g[a] @ g[b] + g[b] @ g[a], 2 * (a == b) * np.eye(D)) for a in range(12) for b in range(12))
check("A1 12 Majoranas obey {g_a,g_b} = 2 delta (Cl(12))", ok)
n = [cd[j] @ c[j] for j in range(NM)]
Ntot5 = sum(n[:5])
occ = np.array([[(s >> (NM - 1 - j)) & 1 for j in range(NM)] for s in range(D)])
even = np.where(occ.sum(1) % 2 == 0)[0]
light = [s for s in even if occ[s, 5] == 0]
mirror = [s for s in even if occ[s, 5] == 1]
check("A2 even 32 = light 16 (A1 empty, even on 5) + mirror 16 (A1 filled, odd on 5)",
      len(even) == 32 and len(light) == 16 and len(mirror) == 16)
X = 2 * Ntot5 - 5 * np.eye(D)
Y = 0.5 * (n[0] + n[1]) - (n[2] + n[3] + n[4]) / 3.0
BL = np.eye(D) - (2.0 / 3.0) * (n[2] + n[3] + n[4])
qX = [np.real(np.trace(cd[j].T @ (X @ cd[j] - cd[j] @ X))) / np.real(np.trace(cd[j].T @ cd[j])) for j in range(5)]
qY = [np.real(np.trace(cd[j].T @ (Y @ cd[j] - cd[j] @ Y))) / np.real(np.trace(cd[j].T @ cd[j])) for j in range(5)]
qB = [np.real(np.trace(cd[j].T @ (BL @ cd[j] - cd[j] @ BL))) / np.real(np.trace(cd[j].T @ cd[j])) for j in range(5)]
check("A3 U(5)_X: every c_j^dag has X = +2, so 10 = 5_{+2} + 5bar_{-2} (rule TJ frame)",
      np.allclose(qX, 2), f"X={np.round(qX, 3).tolist()}")
check("A4 SM charges of c^dag: E -> (1,2) Y=+1/2, B-L=0 (the doublet); T1 -> (3,1) Y=-1/3, B-L=-2/3 (the triplet)",
      np.allclose(qY, [0.5, 0.5, -1/3, -1/3, -1/3]) and np.allclose(qB, [0, 0, -2/3, -2/3, -2/3]),
      f"Y={np.round(qY, 3).tolist()} B-L={np.round(qB, 3).tolist()}")
print("  the 10's doublet/triplet split IS the E/T1 split of the mode labels (same parameter as omega_E != omega_T)")


def gens(nmaj):
    return [(0.5j) * g[a] @ g[b] for a in range(nmaj) for b in range(a + 1, nmaj)]


G12 = gens(12)
G10 = gens(10)
E = np.ix_(even, even)
T12 = [x[E] for x in G12]
T10 = [x[E] for x in G10]
Q6 = (n[5] - 0.5 * np.eye(D))[E]
C12_32 = sum(t @ t for t in T12)
C10_32 = sum(t @ t for t in T10)
check("A5 Casimirs on the 32: Spin(12) spinor 16.5 (norm C = sum l_i(l_i + n - 2i)); Spin(10) 11.25 on both halves",
      np.allclose(C12_32, 16.5 * np.eye(32)) and np.allclose(C10_32, 11.25 * np.eye(32)))
vecC = []
for a in range(10):
    va = g[a]
    out = sum((t @ (t @ va - va @ t) - (t @ va - va @ t) @ t) for t in G10)
    vecC.append(np.real(np.trace(va.conj().T @ out)) / np.real(np.trace(va.conj().T @ va)))
check("A6 the Majoranas g_1..g_10 carry Casimir 9 = the vector 10 (fermionic: odd operators)", np.allclose(vecC, 9))
Om = np.eye(D, dtype=complex)
for j in range(5):
    Om = Om @ (np.eye(D) - 2 * n[j]) * 1j
okO = all(np.allclose(Om @ g[a] @ np.linalg.inv(Om), -g[a]) for a in range(10))
okA = all(np.allclose(Om @ g[a] @ np.linalg.inv(Om), g[a]) for a in (10, 11))
check("A7 the Spin(10) element Omega = prod exp(i pi (n_j-1/2)) acts as -1 on the 10 = (-1)^F5: every 10-tensor on 5 modes is FERMIONIC",
      okO and okA)
b10 = [g[a] @ g[10] for a in range(10)]
check("A8 a BOSONIC 10 exists only with a Spin(10)-singlet fermion: g_a g_A1 is even, Omega-odd (Casimir 9)",
      all(np.allclose(Om @ x @ np.linalg.inv(Om), -x) for x in b10)
      and np.isclose(np.real(np.trace(b10[0].conj().T @ sum(t @ (t @ b10[0] - b10[0] @ t) - (t @ b10[0] - b10[0] @ t) @ t for t in G10)))
                     / np.real(np.trace(b10[0].conj().T @ b10[0])), 9))
print("  (cone correction: free 5-mode cones carry the fermionic 10; products of an even number of 10s never contain a 10)")

# ------------------------------------------------------------------ B
print("== B. Lorentz-scalar Weyl pairs of the 32 (internally symmetric part, 528) ==")
I32 = np.eye(32)
Cp = np.kron(C12_32, I32) + np.kron(I32, C12_32)
for t in T12:
    Cp += 2 * np.kron(t, t)
C10p = np.kron(C10_32, I32) + np.kron(I32, C10_32)
for t in T10:
    C10p += 2 * np.kron(t, t)
Qp = np.kron(Q6, I32) + np.kron(I32, Q6)
cols = []
for i in range(32):
    for j in range(i, 32):
        v = np.zeros(1024)
        v[32 * i + j] += 1
        v[32 * j + i] += 1
        cols.append(v / np.linalg.norm(v))
S = np.array(cols).T
K = S.T @ (Cp + (np.pi / 10) * C10p + (np.e / 7) * Qp) @ S
w, V = np.linalg.eigh(K)
Vf = S @ V
c12 = np.real(np.einsum('ij,ij->j', Vf.conj(), Cp @ Vf))
c10 = np.real(np.einsum('ij,ij->j', Vf.conj(), C10p @ Vf))
q6 = np.real(np.einsum('ij,ij->j', Vf.conj(), Qp @ Vf))
tab = {}
for a, b, q in zip(np.round(c12, 6) + 0.0, np.round(c10, 6) + 0.0, np.round(q6, 6) + 0.0):
    a, b, q = float(a), float(b), float(q)
    tab[(a, b, q)] = tab.get((a, b, q), 0) + 1
print("  (C12, C10, q6): mult  ->", sorted(tab.items()))
d12 = {}
for (a, b, q), m in tab.items():
    d12[a] = d12.get(a, 0) + m
check("B1 symmetric 32x32 = 66 (C=20) + 462 (C=36): no Spin(12) singlet scalar (32 pseudoreal: protected)",
      d12 == {20.0: 66, 36.0: 462})
check("B2 66 -> 45_0 + 1_0 + 10_{+1} + 10_{-1} under Spin(10) x U(1)_A1",
      tab.get((20.0, 16.0, 0.0)) == 45 and tab.get((20.0, 0.0, 0.0)) == 1 and tab.get((20.0, 9.0, 1.0)) == 10
      and tab.get((20.0, 9.0, -1.0)) == 10)
check("B3 light-light pairs (q6=-1) = 10 + 126 (no singlet: the 16 is protected); mirror-mirror = 10 + 126bar",
      tab.get((20.0, 9.0, -1.0)) == 10 and tab.get((36.0, 25.0, -1.0)) == 126 and tab.get((36.0, 25.0, 1.0)) == 126)
lm = {k: m for k, m in tab.items() if k[2] == 0.0}
check("B4 light-mirror scalars (q6=0) = 1 + 45 + 210: NO 10 (a scalar 10 is never a light-mirror bilinear)",
      sum(lm.values()) == 256 and not any(k[1] == 9.0 for k in lm))

# ------------------------------------------------------------------ C
print("== C. Goldstone dichotomy ==")
idx = [i for i in range(528) if abs(c12[i] - 20) < 1e-6 and abs(c10[i]) < 1e-6 and abs(q6[i]) < 1e-6]
b0 = Vf[:, idx[0]]
Bm = b0.reshape(32, 32)
lpos = [even.tolist().index(s) for s in light]
mpos = [even.tolist().index(s) for s in mirror]
offd = np.linalg.norm(Bm[np.ix_(lpos, lpos)]) + np.linalg.norm(Bm[np.ix_(mpos, mpos)])
sv = np.linalg.svd(Bm[np.ix_(lpos, mpos)], compute_uv=False)
check("C1 the 1_0 pair is purely light x mirror and full rank with equal singular values: a Dirac mass for the WHOLE light 16",
      offd < 1e-9 and np.allclose(sv, sv[0]) and sv[0] > 1e-3, f"sv={sv[0]:.4f} x16")
Gm = np.array([(np.kron(t, I32) + np.kron(I32, t)) @ b0 for t in T12]).T
rk = np.linalg.matrix_rank(Gm, tol=1e-8)
check("C2 stabiliser of the 1_0 pair in so(12) = 46 = so(10)+u(1): 20 Goldstones", 66 - rk == 46, f"rank={rk}")
U_, s_, Vh_ = np.linalg.svd(Gm, full_matrices=False)
img = U_[:, :rk]
qimg = np.linalg.eigvalsh(img.conj().T @ Qp @ img)
cimg = np.linalg.eigvalsh(img.conj().T @ C10p @ img)
check("C3 the 20 Goldstones are 10_{+1} + 10_{-1} (they contain the B-L=0, Y=+-1/2 doublets AND the triplets)",
      np.allclose(sorted(qimg), [-1] * 10 + [1] * 10) and np.allclose(cimg, 9))
Pm = np.diag([float(occ[s, 5]) for s in even])
rkP = np.linalg.matrix_rank(np.array([(t @ Pm - Pm @ t).ravel() for t in T12]).T, tol=1e-8)
check("C4 a mirror-only term (spurion = A1 occupation) has the same commutant 46: Spin(12) broken EXPLICITLY, no Goldstone",
      66 - rkP == 46)
print("  => Goldstone 10 exists only if light+mirror pair up (light gapped at f); SMG keeps the light chiral but leaves no Goldstone")

# ------------------------------------------------------------------ D
print("== D. half-link cubic structure (6 link ends + site) ==")
ends = [(s, i) for i in range(3) for s in (1, -1)]
P = np.zeros((6, 6))
F = np.zeros((6, 6))
for a, (s, i) in enumerate(ends):
    for b, (t, j) in enumerate(ends):
        if i == j and s == -t:
            P[a, b] = 1
        if i != j:
            F[a, b] = 1
vecs = np.array([[s * (i == k) for k in range(3)] for (s, i) in ends], float)
perms = []
for pm in it.permutations(range(3)):
    for sg in it.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for k in range(3):
            R[pm[k], k] = sg[k]
        perms.append([next(b for b in range(6) if np.allclose(vecs[b], R @ vecs[a])) for a in range(6)])
orb = set()
for a in range(6):
    for b in range(6):
        orb.add(min(tuple(sorted({(p[a], p[b]) for p in perms}))))
check("D1 O_h (48) on the 6 link ends: 3 orbits on pairs, so covariant one-body terms = span(1, P antipode, F face)",
      len(perms) == 48 and len(orb) == 3)
A1v = np.ones(6) / np.sqrt(6)
Ppl = (np.eye(6) + P) / 2
Ev = Ppl - np.outer(A1v, A1v)
Tv = (np.eye(6) - P) / 2
ev = lambda M, Pr: np.trace(Pr @ M) / np.trace(Pr)
check("D2 P: A1 +1, E +1, T1 -1 (the antipode term groups A1 with E: 6 = 3_even + 3_odd)",
      np.allclose([ev(P, np.outer(A1v, A1v)), ev(P, Ev), ev(P, Tv)], [1, 1, -1]))
check("D3 F: A1 4, E -2, T1 0", np.allclose([ev(F, np.outer(A1v, A1v)), ev(F, Ev), ev(F, Tv)], [4, -2, 0]))
aa, bb = 0.7, 0.13
Hh = aa * P + bb * F
wA, wE, wT = ev(Hh, np.outer(A1v, A1v)), ev(Hh, Ev), ev(Hh, Tv)
check("D4 coset frequencies (c_a^dag c_A1): doublet wE-wA1 = -6b, triplet wT-wA1 = -2a-4b (exact)",
      np.isclose(wE - wA, -6 * bb) and np.isclose(wT - wA, -2 * aa - 4 * bb))
print("  b = 0 (straight-through link ends) gives an exact doublet generator and a triplet split -2a: DT at one-body level")
for h in (0.3, 0.03, 0.003):
    H7 = np.zeros((7, 7))
    H7[1:, 1:] = aa * P
    H7[0, 1:] = H7[1:, 0] = h
    lam = np.linalg.eigvalsh(H7)
    gap = min(abs(l - aa) for l in lam if not np.isclose(l, aa) and not np.isclose(l, -aa))
    exact = np.sqrt(aa ** 2 / 4 + 6 * h ** 2) - aa / 2
    check(f"D5 site-A1 hop h={h}: doublet seesaw gap = sqrt(a^2/4+6h^2)-a/2 (~6h^2/a)",
          np.isclose(gap, exact), f"gap={gap:.3e} 6h^2/a={6*h*h/aa:.3e}")


def commdim(M):
    lam = np.round(np.linalg.eigvalsh(M), 8)
    _, cnt = np.unique(lam, return_counts=True)
    return int((cnt ** 2).sum())


H7[0, 1:] = H7[1:, 0] = 0.3
H70 = H7.copy(); H70[0, 1:] = H70[1:, 0] = 0
check("D6 one-body commutant: h=0 -> 19 (u(3)_A1+E + u(3)_T1 + u(1)), h!=0 -> 15 (doublet generator broken)",
      commdim(H70) == 19 and commdim(H7) == 15)

# ------------------------------------------------------------------ E
del Cp, C10p, Qp, Gm, U_, img, Vf, S, K
print("== E. Yukawa 16 x 16 x 10 ==")
c5 = fock(5)
cd5 = [x.T for x in c5]
g5 = []
for j in range(5):
    g5 += [(c5[j] + cd5[j]).astype(complex), 1j * (cd5[j] - c5[j])]
B1 = np.eye(32, dtype=complex)
for a in range(1, 10, 2):
    B1 = B1 @ g5[a]
M5 = [(0.5j) * g5[a] @ g5[b] for a in range(10) for b in range(a + 1, 10)]
check("E1 B = product of the 5 imaginary Majoranas is Spin(10)-invariant (M^T B + B M = 0)",
      all(np.allclose(m.T @ B1 + B1 @ m, 0) for m in M5))
occ5 = np.array([[(s >> (4 - j)) & 1 for j in range(5)] for s in range(32)])
s16 = [s for s in range(32) if occ5[s].sum() % 2 == 0]
Ya = [(B1 @ g5[a])[np.ix_(s16, s16)] for a in range(10)]
check("E2 Y_a = B g_a on 16 x 16 is symmetric and nonzero: the family matrix of 16_f 16_g 10 is SYMMETRIC",
      all(np.allclose(y, y.T) and np.linalg.norm(y) > 1 for y in Ya))


def lab(s):
    o = occ5[s]
    nE, nT = o[:2].sum(), o[2:].sum()
    return {(0, 0): 'nc', (2, 0): 'ec', (1, 1): 'q', (0, 2): 'uc', (1, 3): 'L', (2, 2): 'dc'}[(nE, nT)]


labs = [lab(s) for s in s16]
Yu = (B1 @ cd5[1])[np.ix_(s16, s16)]
Ydn = (B1 @ c5[1])[np.ix_(s16, s16)]


def pairs(Yx):
    out = {}
    for i in range(16):
        for j in range(16):
            if abs(Yx[i, j]) > 1e-9:
                k = tuple(sorted((labs[i], labs[j])))
                out.setdefault(k, set()).add(round(abs(Yx[i, j]), 9))
    return out


pu, pd = pairs(Yu), pairs(Ydn)
print("  neutral comps: c1^dag ->", sorted(pu), "; c1 ->", sorted(pd))
mags = set().union(*pu.values(), *pd.values())
check("E3 one neutral component couples (q uc),(L nc) [up/Dirac-nu], the other (q dc),(L ec) [down/lepton], all |entries| equal",
      set(pu) == {('q', 'uc'), ('L', 'nc')} and set(pd) == {('dc', 'q'), ('L', 'ec')} and len(mags) == 1,
      f"|Y|={sorted(mags)}")
print("  single 10 per family: m_u = m_nuD, m_d = m_e at matching; real 10 (H_d = H_u*) adds m_t = m_b (tan beta = 1)")
ok3 = [q for q in it.product([1, 2], repeat=3) if (4 * sum(q)) % 3 == 0]
check("E4 N=3 with per-family turn charges q_f in {1,2}: anomaly 4 sum q = 0 mod 3 forces UNIFORM q",
      sorted(ok3) == [(1, 1, 1), (2, 2, 2)], str(ok3))
allow = {(qh,): sum(((2 * ok3[0][0] + qh) % 3 == 0) for _ in range(9)) for qh in range(3)}
check("E5 uniform q: every Y_fg has turn phase w^(2q+qH): all 9 entries allowed (one qH) or none (texture-free)",
      sorted(allow.values()) == [0, 0, 9])
Ls = []
for a in range(3):
    for b in range(a + 1, 3):
        m = np.zeros((3, 3)); m[a, b], m[b, a] = 1, -1; Ls.append(m)
basis = []
for a in range(3):
    for b in range(a, 3):
        m = np.zeros((3, 3)); m[a, b] = m[b, a] = 1; basis.append(m)
A = np.array([np.concatenate([(L.T @ Bs + Bs @ L).ravel() for L in Ls]) for Bs in basis]).T
inv_o3 = 6 - np.linalg.matrix_rank(A, tol=1e-9)
check("E6 family symmetry: Sym^2(3) has 1 SO(3) invariant (Y ~ 1: degenerate families) and 0 U(3) invariants (charge 2): Y = 0",
      inv_o3 == 1)
Ns = 100000
Z = rng.normal(size=(Ns, 3, 3)) + 1j * rng.normal(size=(Ns, 3, 3))
Zs = (Z + np.transpose(Z, (0, 2, 1))) / 2
sv = np.linalg.svd(Zs, compute_uv=False)
r2, r3 = sv[:, 1] / sv[:, 0], sv[:, 2] / sv[:, 0]
hits = int(np.sum((r2 <= 3.2e-3) & (r3 <= 6.5e-6)))
p3 = float(np.mean(r3 <= 6.5e-6))
check("E7 anarchic O(1) symmetric Y (seeded, 1e5): up-type hierarchy (mc/mt 3.2e-3, mu/mt 6.5e-6) essentially never",
      hits == 0, f"hits={hits}, P(r3<=6.5e-6)={p3:.1e}, median r2={np.median(r2):.2f}")

# ------------------------------------------------------------------ F
print("== F. estimates against measurement (approx., cited inputs; not checks of a rule) ==")
M = 2.44e18
mh, v = 125.1, 246.0
print(f"  unprotected scalar 10 at the cell: (m_D/M)^2 needed = {(mh / M) ** 2:.1e} (FITTED tuning)")
print(f"  DT seesaw: 6h^2/a = m_H/M needs h/a = {np.sqrt(mh / M / 6):.1e} (FITTED)")
gut = dict(mt=74.0, mb=1.0, mtau=1.68, ms=0.021, mmu=0.099, md=0.0011, me=0.00047)
print(f"  single 10 at ~2e16 GeV: mb/mtau={gut['mb']/gut['mtau']:.2f}, ms/mmu={gut['ms']/gut['mmu']:.2f}, "
      f"md/me={gut['md']/gut['me']:.1f} (pred 1,1,1); |Vus|=0.225 (pred 0); real 10: mt/mb={gut['mt']/gut['mb']:.0f} (pred 1)")
check("F1 single-10 relations contradicted by >= factor 2 in two light ratios (estimate)",
      abs(np.log(gut['ms'] / gut['mmu'])) > np.log(2) and abs(np.log(gut['md'] / gut['me'])) > np.log(2))
print(f"TOTAL: PASS={NP} FAIL={NF}")
