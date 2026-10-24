AUDIT_INPUT_PATHS = ('docs/THE_SPIN10_PAIR_SQUARE_ON_TWO_SIXTEENS_IS_A_SPIN12_CASIMIR_WITH_A_UNIQUE_SINGLET_GROUND_STATE_AND_GAP_FOUR_G_BUT_A_FROZEN_FAR_REGION_STILL_MOVES_THE_MIRROR_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""spin10-two-flavour: the 10-channel pair square on TWO 16s of Spin(10) (32 modes, Fock 2^32) through Casimirs.
 A  one-body algebra (exact): the 16, C Gamma^a, Pauli/flavour structure, closure of {T_ab, B_a, B_a^+, J} into so(12).
 B  Fock identity (exact, complete for number-conserving degree-4 operators): sum_a {B_a, B_a^+} = 2[144 - 2 S(S+1) - C2_10 - J^2].
 C  spectrum by representation theory: Weyl-formula Casimirs, spherical irreps, Spin(10) singlet counts, ground state, gaps,
    ordering, contrasts 16 + 16bar and 15 + 15.
 D  reduced analogues by full diagonalisation: Spin(6) 4 x 2 flavours (2^8) and its 3 + 3 truncation (2^6).
 E  slab: does a two-layer far region capture the wall mode, and does freezing it avoid relocation.
Labels: [T] exact, [F] finite diagnostic. Supplied: the 16 with one orbital per weight and a two-valued flavour (spin) index,
the 10-channel pair form, the particle-hole symmetric ordering, the free slab model with the m sz stand-in for a frozen layer.
Cited, not rederived: You-He-Xu-Vishwanath 2018, Razamat-Tong 2021, Tong 2021, Wang-Wen 2018/2020,
Butt-Catterall-Hasenfratz (SO(4) lattice SMG), Cartan-Helgason theorem (used only as a cross-check of C3)."""
AUDIT_TIMEOUT_SEC = 120
import os, time, itertools, resource
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
from collections import Counter
from fractions import Fraction as Fr
import numpy as np, scipy.sparse as sp

rng = np.random.default_rng(20261023)
T0 = time.time(); NP = NF = 0
def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))

def ann(n):
    """dense Jordan-Wigner annihilators on n modes"""
    dim = 1 << n; st = np.arange(dim); out = []
    for j in range(n):
        A = np.zeros((dim, dim)); src = st[(st >> j) & 1 == 1]
        A[src ^ (1 << j), src] = 1 - 2 * (np.bitwise_count(src & ((1 << j) - 1)).astype(np.int64) & 1)
        out.append(A)
    return out

def spinor(n):
    """chiral spinor of Spin(2n) on the even states of n oscillators: generators t_ab and the pair matrices M_a = (C g_a)|_+"""
    b = ann(n); G = []
    for k in range(n): G += [b[k] + b[k].T, 1j * (b[k] - b[k].T)]
    ev = [s for s in range(1 << n) if bin(s).count('1') % 2 == 0]
    t = [(-0.25j * (G[a] @ G[c] - G[c] @ G[a]))[np.ix_(ev, ev)] for a, c in itertools.combinations(range(2 * n), 2)]
    best = None
    for C in (np.linalg.multi_dot(G[0::2]) if n > 1 else G[0], np.linalg.multi_dot(G[1::2]) if n > 1 else G[1]):
        M = [(C @ g)[np.ix_(ev, ev)] for g in G]
        if all(np.abs(m).max() > 0.5 for m in M): best = M; break
    return t, best, len(ev)

def vec_rep(t, M):
    """induced action X -> -(t^T X + X t) on span{M_a}; returns the rep matrices (in the M_a basis) and the span residual"""
    B = np.array([m.ravel() for m in M]).T; res = 0; R = []
    for tt in t:
        Y = np.array([(-(tt.T @ m + m @ tt)).ravel() for m in M]).T
        x, *_ = np.linalg.lstsq(B, Y, rcond=None); res = max(res, np.abs(B @ x - Y).max()); R.append(x)
    return R, res

# ------------------------------------------------------------------ A
print("== A. one-body algebra: 16 of Spin(10), pair B_a = c_1^T M_a c_2, flavour = two spin components")
t16, M16, d16 = spinor(5)
cas16 = sum(x @ x for x in t16)
symm = max(np.abs(m - m.T).max() for m in M16); unit = max(np.abs(m @ m.conj().T - np.eye(16)).max() for m in M16)
R10, res10 = vec_rep(t16, M16); cas10 = sum(r @ r for r in R10)
check("A1 [T] 45 Hermitian t_ab, Casimir 45/4 on the 16; M_a = (C gamma_a)|_+ symmetric and unitary; span{M_a} invariant, "
      "induced 10-dim rep has Casimir 9 (the vector)", len(t16) == 45 and np.abs(cas16 - 45 / 4 * np.eye(16)).max() < 1e-12
      and symm < 1e-12 and unit < 1e-12 and res10 < 1e-12 and np.abs(cas10 - 9 * np.eye(10)).max() < 1e-9,
      f"|M-M^T| {symm:.0e}, Casimir(10) {np.real(np.trace(cas10))/10:.3f}")
NM = 32
def nambu(h11=None, A=None, Ad=None):
    Z = np.zeros((NM, NM), complex); h11 = Z if h11 is None else h11; A = Z if A is None else A; Ad = Z if Ad is None else Ad
    return np.block([[h11, 2 * Ad], [2 * A, -h11.T]])
def pairA(M):
    A = np.zeros((NM, NM), complex); A[:16, 16:] = M / 2; A[16:, :16] = -M.T / 2; return A
I2 = np.eye(2)
NT = [nambu(h11=np.kron(I2, x)) for x in t16]
NB = [nambu(A=pairA(m)) for m in M16]; NBd = [nambu(Ad=-pairA(m).conj()) for m in M16]
NX = [(b + bd) / 2 for b, bd in zip(NB, NBd)]; NY = [1j * (b - bd) / 2 for b, bd in zip(NB, NBd)]
NJ = nambu(h11=np.eye(NM) / 2)
sp_ = np.zeros((NM, NM)); sp_[:16, 16:] = np.eye(16)
NS = [nambu(h11=(sp_ + sp_.T) / 2), nambu(h11=-1j * (sp_ - sp_.T) / 2), nambu(h11=np.diag([0.5] * 16 + [-0.5] * 16))]
pauli = max(np.abs(m - m.T).max() for m in M16)   # c^T M c = 0 for symmetric M (fermions)
comm = lambda a, b: a @ b - b @ a
fcomm = max(np.abs(comm(s, x)).max() for s in NS for x in NT + NB + NBd + [NJ])
check("A2 [T] Pauli: M_a symmetric, so c_1^T M_a c_1 = 0 and B_a is the flavour-antisymmetric (epsilon) pair - for the two spin "
      "components of one Weyl 16 it is the Lorentz-scalar 10 bilinear; the 3 flavour generators commute with all T, B, B^+, J",
      pauli < 1e-12 and fcomm < 1e-12, f"max |[S, .]| {fcomm:.0e}")
GEN = NT + NX + NY + [NJ]; Bm = np.array([g.ravel() for g in GEN]).T
rank = np.linalg.matrix_rank(Bm, tol=1e-9); resid = 0
for i in range(66):
    for j in range(i + 1, 66):
        y = comm(GEN[i], GEN[j]).ravel(); x, *_ = np.linalg.lstsq(Bm, y, rcond=None); resid = max(resid, np.abs(Bm @ x - y).max())
# explicit so(12) relations: G_ab = s_T T_ab, G_{a,10} = X_a, G_{a,11} = Y_a, G_{10,11} = s_J J
pairs10 = list(itertools.combinations(range(10), 2))
def so12(sT, sJ):
    G = {}
    for k, (a, c) in enumerate(pairs10): G[(a, c)] = sT * NT[k]
    for a in range(10): G[(a, 10)] = NX[a]; G[(a, 11)] = NY[a]
    G[(10, 11)] = sJ * NJ
    g = lambda A, B: G[(A, B)] if A < B else (-G[(B, A)] if A > B else 0 * NJ)
    d = lambda x, y: 1.0 if x == y else 0.0; err = 0
    keys = list(G)
    for (A, B) in keys:
        for (C, D) in keys:
            rhs = 1j * (d(B, C) * g(A, D) - d(A, C) * g(B, D) - d(B, D) * g(A, C) + d(A, D) * g(B, C))
            err = max(err, np.abs(comm(G[(A, B)], G[(C, D)]) - rhs).max())
    return err
errs = {(sT, sJ): so12(sT, sJ) for sT in (1, -1) for sJ in (1, -1)}; sgn = min(errs, key=errs.get)
check("A3 [T] closure: the 66 Nambu matrices {T_ab, (B+B^+)/2, i(B-B^+)/2, J} are independent and closed under commutators; "
      "with signs (s_T, s_J) they obey the so(12) relations exactly (so(10)+u(1), the 10 at J-charge +-1)",
      rank == 66 and resid < 1e-10 and errs[sgn] < 1e-12, f"rank {rank}, closure resid {resid:.0e}, signs {sgn}, rel err {errs[sgn]:.0e}")

# ------------------------------------------------------------------ B
print("== B. Fock identity on 32 modes (mode x = 16 i + alpha)")
SECT = {N: np.array(sorted(sum(1 << x for x in cmb) for cmb in itertools.combinations(range(32), N)), dtype=np.int64) for N in range(6)}
def look(N, s): return np.searchsorted(SECT[N], s)
def sgn(s, x): return 1 - 2 * (np.bitwise_count(s & ((1 << x) - 1)).astype(np.int64) & 1)
def create2(N, p, q):
    """c^+_p c^+_q on sector N -> N+2: (rows, cols, signs)"""
    S = SECT[N]; ok = ((S >> q) & 1 == 0) & ((S >> p) & 1 == 0) & (p != q); s = S[ok]; col = np.nonzero(ok)[0]
    sg = sgn(s, q); s1 = s | (1 << q); sg = sg * sgn(s1, p); s2 = s1 | (1 << p); return look(N + 2, s2), col, sg
def hop1(N, p, q):
    """c^+_p c_q on sector N"""
    S = SECT[N]; ok = ((S >> q) & 1 == 1); s = S[ok]; col = np.nonzero(ok)[0]; sg = sgn(s, q); s1 = s ^ (1 << q)
    ok2 = ((s1 >> p) & 1 == 0); s1, col, sg = s1[ok2], col[ok2], sg[ok2]; sg = sg * sgn(s1, p); return look(N, s1 | (1 << p)), col, sg
def Bdag(N, M):
    r, c, v = [], [], []
    for al, be in zip(*np.nonzero(np.abs(M) > 1e-14)):
        rr, cc, sg = create2(N, 16 + be, al); r.append(rr); c.append(cc); v.append(np.conj(M[al, be]) * sg)
    return sp.csr_matrix((np.concatenate(v), (np.concatenate(r), np.concatenate(c))), shape=(len(SECT[N + 2]), len(SECT[N])))
def onebody(N, h):
    r, c, v = [], [], []
    for p, q in zip(*np.nonzero(np.abs(h) > 1e-14)):
        rr, cc, sg = hop1(N, p, q); r.append(rr); c.append(cc); v.append(h[p, q] * sg)
    n = len(SECT[N]); return sp.csr_matrix((np.concatenate(v), (np.concatenate(r), np.concatenate(c))), shape=(n, n))
BD = {N: [Bdag(N, m) for m in M16] for N in range(4)}
def lhs(N, v):
    out = sum(b.conj().T @ (b @ v) for b in BD[N])
    if N >= 2: out = out + sum(b @ (b.conj().T @ v) for b in BD[N - 2])
    return out
def comm_BB(N, v):
    out = sum(b.conj().T @ (b @ v) for b in BD[N])
    if N >= 2: out = out - sum(b @ (b.conj().T @ v) for b in BD[N - 2])
    return out
def rhs_ops(N):
    T = [onebody(N, np.kron(I2, x)) for x in t16]; C10 = sum(x @ x for x in T)
    Sp = onebody(N, sp_.astype(complex)); Sm = Sp.conj().T
    S = SECT[N]; n1 = np.bitwise_count(S & 0xFFFF).astype(float); Sz = sp.diags((2 * n1 - N) / 2)
    Cf = Sz @ Sz + 0.5 * (Sp @ Sm + Sm @ Sp); J = (N - 16) / 2
    return C10, Cf, J
eB1 = eB2 = 0
for N in range(3):
    C10, Cf, J = rhs_ops(N); n = len(SECT[N]); I = sp.identity(n, format='csr', dtype=complex)
    L = lhs(N, I); R = 2 * (144 * I - 2 * Cf - C10 - J**2 * I); eB1 = max(eB1, np.abs((L - R).toarray()).max())
    eB2 = max(eB2, np.abs((comm_BB(N, I) - (-20 * J) * I).toarray()).max())
check("B1 [T] on the N <= 2 sectors (529 states; complete for number-conserving degree-4 operators): sum_a {B_a, B_a^+} = "
      "2 [144 - 2 S(S+1) - C2_10 - J^2], J = (N-16)/2; i.e. C2(so12) = 144 - 2 S(S+1) on the whole Fock space", eB1 < 1e-10, f"err {eB1:.0e}")
check("B2 [T] sum_a [B_a, B_a^+] = -20 J, so -g sum_a B_a B_a^+ = -g (F - 10 J), F = 144 - 2S(S+1) - C2_10 - J^2", eB2 < 1e-10, f"err {eB2:.0e}")
C10, Cf, J = rhs_ops(3); eB3 = 0
for _ in range(3):
    v = rng.standard_normal(len(SECT[3])) + 1j * rng.standard_normal(len(SECT[3]))
    eB3 = max(eB3, np.abs(lhs(3, v) - 2 * (144 * v - 2 * (Cf @ v) - C10 @ v - J**2 * v)).max() / np.abs(v).max())
check("B3 [F] redundancy: the identity on 3 seeded random vectors of the N = 3 sector (4960 states, via N = 5)", eB3 < 1e-9, f"err {eB3:.0e}")

# ------------------------------------------------------------------ C
print("== C. spectrum by representation theory (H_sym = -(g/2) sum {B, B^+} = -g F)")
rho6 = [Fr(x) for x in (5, 4, 3, 2, 1, 0)]
cas12 = lambda lam: sum((Fr(l) + r)**2 - r**2 for l, r in zip(lam, rho6))
h = Fr(1, 2); f2 = lambda j: 144 - 2 * j * (j + 1)
c1 = [cas12((8, 0, 0, 0, 0, 0)) == f2(0), cas12((h,) * 6) == f2(Fr(15, 2)), cas12((1, 1, 1, 1, 0, 0)) == f2(Fr(7)),
      cas12((Fr(15, 2),) + (h,) * 5) == f2(h)]
check("C1 [T] standard Casimirs <lam, lam+2rho> match 144 - 2j(j+1): (8,0^5) = 144 (j=0, holds |0>, |F>); Lambda^1(32) = 33/2 "
      "(j=15/2); Lambda^2_0 = (1^4,0,0) = 32 (j=7); (15/2,(1/2)^5) = 285/2 (j=1/2, holds c^+|0>)", all(c1))
sph = [(a, b) for a in range(0, 13) for b in range(0, a + 1) if (a - b) % 2 == 0 and cas12((a, b, 0, 0, 0, 0)) == 144]
w32 = [np.array(v) / 2 for v in itertools.product((1, -1), repeat=6) if np.prod(v) == 1]
m1 = sum(max(0, w[0]) for w in w32); m12 = sum(max(0, w[0] + w[1]) for w in w32); top = [w for w in w32 if w[0] > 0]
check("C2 [T] spherical irreps (a,b,0^4) with C2 = 144 are exactly (8,0) and (6,4); Fock weights obey mu_1 <= 8 and "
      "mu_1 + mu_2 <= 8, so (6,4) is absent; weight (8,0^5) arises from one subset only (all 16 w with w_1 = +1/2, S_z = 0): "
      "(8,0) occurs once, flavour singlet => one state with F = 144", sph == [(6, 4), (8, 0)] and m1 == 8 and m12 == 8
      and len(top) == 16 and np.allclose(sum(top), [8, 0, 0, 0, 0, 0]), f"spherical {sph}")
# Spin(10) decompositions of Lambda^k(16) (doubled weights)
def psign(p):
    s = 1; p = list(p)
    for i in range(len(p)):
        while p[i] != i: j = p[i]; p[i], p[j] = p[j], p[i]; s = -s
    return s
W5 = [(np.array(p), np.array(f), psign(p)) for p in itertools.permutations(range(5)) for f in itertools.product((1, -1), repeat=5) if np.prod(f) == 1]
rho5 = np.array([8, 6, 4, 2, 0])
w16 = [np.array(v) for v in itertools.product((1, -1), repeat=5) if np.prod(v) == 1]
def mult(cnt, lam): return sum(sg * cnt.get(tuple((lam + rho5)[p] * f - rho5), 0) for p, f, sg in W5)
dominant = lambda l: l[0] >= l[1] >= l[2] >= l[3] >= abs(l[4])
st16 = np.arange(1 << 16); bits16 = ((st16[:, None] >> np.arange(16)) & 1); N16 = bits16.sum(1); WT = bits16 @ np.array(w16)
DEC = []
for k in range(17):
    cnt = Counter(map(tuple, WT[N16 == k])); dec = {}
    for lam in cnt:
        if dominant(lam):
            m = mult(cnt, np.array(lam))
            if m: dec[lam] = m
    DEC.append(dec)
def sing(n1, n2):
    if not (0 <= n1 <= 16 and 0 <= n2 <= 16): return 0
    return sum(m * DEC[16 - n2].get(l, 0) for l, m in DEC[n1].items())
def nflav(N, j):                       # Spin(10)-singlet states of flavour spin j at total N (one per multiplet)
    if (N - 2 * j) % 2: return 0
    return sing((N + 2 * j) // 2, (N - 2 * j) // 2) - sing((N + 2 * j) // 2 + 1, (N - 2 * j) // 2 - 1)
tot = [sum(sing(n1, N - n1) for n1 in range(max(0, N - 16), min(16, N) + 1)) for N in range(33)]
n016, n116, n012, n020 = nflav(16, 0), nflav(16, 1), nflav(12, 0), nflav(20, 0)
check("C3 [T] Spin(10) singlets (Weyl formula, |W(D5)| = 1920) occur only at N = 0 mod 4 (centre Z4); at N = 16 exactly one "
      "flavour singlet => the F = 144 state is unique; flavour-singlet singlets exist at N = 12, 20 (F = 140)",
      all(tot[N] == 0 for N in range(33) if N % 4) and n016 == 1 and n012 >= 1 and n020 == n012,
      f"n_j=0(16) {n016}, n_j=1(16) {n116}, n_j=0(12) {n012}, singlets at N=0,4,..,32: {[tot[N] for N in range(0, 33, 4)]}")
# class minima of the Spin(10) Casimir (doubled dominant weights, Casimir = sum((l+rho)^2 - rho^2)/4)
cls = {}
for lam in itertools.product(range(-8, 9), repeat=5):
    if dominant(lam) and len({x % 2 for x in lam}) == 1 and any(lam):
        c = sum((l + r)**2 - r**2 for l, r in zip(lam, rho5)) / 4; k = sum(lam) % 4; cls[k] = min(cls.get(k, 99), c)
dF = []
for N in range(33):
    J = Fr(N - 16, 2); js = [Fr(x, 2) for x in range(N % 2, 17, 2)]
    c = 0 if N % 4 == 0 else cls[N % 4]
    for j in js:
        for cc in ([0, cls[0]] if N % 4 == 0 else [c]):
            v = 2 * j * (j + 1) + cc + J**2
            if v > 0: dF.append(v)
gapmin = min(dF)
check("C4 [T] H_sym = -g F: E0 = -144 g unique (Spin(10), flavour and particle-hole singlet at N = 16); every other state has "
      "Delta F >= 4 (centre class minima C2 = 16, 9, 45/4; j half-integer for odd N), attained by the N = 16 +- 4 singlets: gap 4 g; "
      "B^+|GS> is exact at -134 g (10 g), c^+|GS> at -131 g (fermion gap 13 g)",
      cls == {0: 16.0, 2: 9.0, 1: 11.25, 3: 11.25} and gapmin == 4 and n012 >= 1 and
      144 - 9 - 1 == 134 and 144 - 2 * h * (h + 1) - Fr(45, 4) - h * h == 131, f"class minima {cls}")
cand = {}
for N in range(0, 33, 4):
    J = (N - 16) // 2
    if nflav(N, 0) >= 1: cand[N] = 144 - J * J - 10 * J
for N in range(2, 33, 4):
    J = (N - 16) // 2; cand[N] = 144 - 9 - J * J - 10 * J            # upper bound on F - 10 J in class 2
for N in range(0, 33, 4):
    J = (N - 16) // 2; cand[N] = max(cand.get(N, -999), 144 - 16 - J * J - 10 * J)   # class-0 non-singlets (bound)
for N in range(1, 33, 2):
    J = Fr(N - 16, 2); cand[N] = 144 - Fr(3, 2) - Fr(45, 4) - J * J - 10 * J       # odd N (bound)
best = max(cand.values()); arg = sorted(N for N in cand if cand[N] == best and N % 4 == 0)
check("C5 [T] naive ordering H = -g sum B B^+: ground energy -168 g, two-fold (N = 4 and 8: charged); the particle-hole "
      "symmetric completion H_sym = H - 5 g (N - 16) is needed to put a unique state at N = 16", best == 168 and arg == [4, 8],
      f"max F-10J = {best} at N = {arg}")
p16b = Counter(tuple(a - b) for a in w16 for b in w16)
mz = mult(p16b, np.array([2, 0, 0, 0, 0])); m1_ = mult(p16b, np.zeros(5, int))
realM = np.abs(np.imag(sum(np.kron(m, m.conj()) for m in M16))).max()
check("C6 [T] contrasts: 16 x 16bar has no 10 and one singlet (the 10 channel vanishes; a quadratic Dirac pairing is allowed: "
      "vector-like, no SMG content). 15 + 15: H conserves N and N1 - N2 and is particle-hole symmetric (sum M x M* real); a "
      "unique C-symmetric state needs N = 15 and N1 = N2: impossible, every level >= 2-fold",
      mz == 0 and m1_ == 1 and realM < 1e-12 and all((15 - 2 * n1) != 0 for n1 in range(16)))

# ------------------------------------------------------------------ D
print("== D. reduced analogues, full diagonalisation")
t4, M4, d4 = spinor(3)
asym = max(np.abs(m + m.T).max() for m in M4)
def site(M, t, nf):
    """two flavours of nf modes; returns H_sym, F-formula parts"""
    n = 2 * nf; c = ann(n); cd = [x.T for x in c]; dim = 1 << n
    Bs = [sum(m[a_, b_] * (c[a_] @ c[nf + b_]) for a_ in range(nf) for b_ in range(nf) if abs(m[a_, b_]) > 1e-14) for m in M]
    Hs = -0.5 * sum(b @ b.conj().T + b.conj().T @ b for b in Bs)
    N = sum(x @ y for x, y in zip(cd, c)); N1 = sum(cd[i] @ c[i] for i in range(nf))
    T = [sum(tt[p, q] * (cd[i * nf + p] @ c[i * nf + q]) for i in range(2) for p in range(nf) for q in range(nf) if abs(tt[p, q]) > 1e-14) for tt in t]
    C2 = sum(x @ x for x in T) if t is not None else None
    return Hs, N, N1, C2, dim
Hs, N, N1, C2, dim = site(M4, t4, 4)
Sz = N1 - N / 2; J = (N - 4 * np.eye(dim)) / 2
Fm = 16 * np.eye(dim) - 4 * Sz @ Sz - C2 - J @ J
e = np.sort(np.linalg.eigvalsh(Hs)); idf = np.abs(Hs + Fm).max()
Nd = np.diag(N).round().astype(int); ef = {}
for Nv in (3, 5):
    P = np.nonzero(Nd == Nv)[0]; ef[Nv] = np.linalg.eigvalsh(Hs[np.ix_(P, P)]).min()
check("D1 [F] n = 3: Spin(6) 4 x 2 flavours (2^8): M antisymmetric (so O_11 != 0 and only U(1) flavour survives); "
      "sum {B,B^+} = 2[16 - 4 S_z^2 - C2_6 - J^2] on the whole Fock space; unique GS at -16 g, gap 4 g, fermion gap 5 g",
      asym < 1e-12 and idf < 1e-10 and abs(e[0] + 16) < 1e-9 and abs(e[1] - e[0] - 4) < 1e-9 and
      abs(min(ef.values()) - e[0] - 5) < 1e-9, f"identity err {idf:.0e}, levels {e[0]:.3f}, {e[1]:.3f}, fermion {min(ef.values()) - e[0]:.3f}")
Hs3, N3, N13, _, _ = site([m[:3, :3] for m in M4], [], 3)
e3 = np.sort(np.linalg.eigvalsh(Hs3))
check("D2 [F] 3 + 3 truncation (one weight dropped per flavour, 2^6): the ground state is degenerate (odd modes per flavour)",
      e3[1] - e3[0] < 1e-9, f"E0 {e3[0]:.3f} x{int(np.sum(abs(e3 - e3[0]) < 1e-9))}")

# ------------------------------------------------------------------ E
print("== E. slab: far two layers vs relocation (free model of smg-strong-coupling A7)")
SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.diag([1., -1]).astype(complex)
def slab(k, Ls, m, r):
    H = np.zeros((2 * Ls, 2 * Ls), complex); T = -(SZ + 1j * SY) / 2
    for s in range(Ls):
        H[2*s:2*s+2, 2*s:2*s+2] = np.sin(k) * SX + (1 - np.cos(k)) * SZ + (m * SZ if s >= Ls - r else 0)
        if s + 1 < Ls: H[2*s+2:2*s+4, 2*s:2*s+2] = T; H[2*s:2*s+2, 2*s+2:2*s+4] = T.conj().T
    return H
def branch(k, r, Ls=12, m=20.0):
    ee, vv = np.linalg.eigh(slab(k, Ls, m, r)); i = np.argmin(abs(ee - np.sin(k))); w = np.abs(vv[:, i])**2
    lay = w.reshape(Ls, 2).sum(1)[::-1]; return abs(ee[i] - np.sin(k)), lay      # lay[0] = far layer
k8 = np.pi / 8; d0, l0 = branch(k8, 0); prof = [branch(k, 0)[1][:2].sum() for k in (np.pi / 16, np.pi / 8, np.pi / 4, np.pi / 2)]
check("E1 [F] free slab (Ls = 12): the far-wall branch E = sin k has weight > 0.9 on the far two layers at k = pi/8 "
      "(a two-layer region captures the wall mode)", d0 < 1e-9 and l0[:2].sum() > 0.9,
      f"w(far 2) at k = pi/16..pi/2: {', '.join(f'{x:.3f}' for x in prof)}")
rel = [branch(k8, r) for r in (1, 2, 3, 4)]
okr = all(d < 1e-6 and lay[:r].sum() < 0.01 and lay[r] > 0.9 for r, (d, lay) in zip((1, 2, 3, 4), rel))
check("E2 [F] the far TWO layers frozen (m sz, m = 20): the branch keeps E = sin k, weight < 0.01 on the frozen layers and "
      "> 0.9 on the third layer from the far end; the same for r = 1..4 frozen layers: relocation by r layers",
      okr, f"r=2: |dE| {rel[1][0]:.0e}, w_frozen {rel[1][1][:2].sum():.4f}, w_next {rel[1][1][2]:.3f}")
print(f"Supplied: 16 with one orbital per weight, two-valued flavour (spin), 10-channel pair, PH ordering, free slab + m sz. "
      f"elapsed {time.time() - T0:.1f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20:.0f} MB")
print(f"TOTAL: PASS={NP} FAIL={NF}")
