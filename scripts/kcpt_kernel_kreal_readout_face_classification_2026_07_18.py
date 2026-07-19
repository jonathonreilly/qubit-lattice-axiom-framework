#!/usr/bin/env python3
"""KCPT kernel K-real readout face classification (bounded theorem).

Integer / rational-exact verification runner. The lattice/kernel/group
construction is copied verbatim from the companion kernel induced-representation
runner (scripts/kcpt_kernel_induced_representation_central_complex_structure_2026_07_18.py);
every gated quantity is recomputed from that construction and expected values
appear only on the comparison side of each gate. The raw complex-structure
representative J64 is FOUND by the selection rule (central raw element squaring
to -64 I, canonical orientation), normalized as j = J64/64, and only THEN gated
against its closed-form Pauli word -- it is never hard-coded.

Group elements are 64 times an orthogonal matrix; commutant, orbit and
certificate gates run on the RAW integer matrices (those tests are
scale-invariant). The product A@B of two group elements is divisible by 64, so
mul(A,B) = (A@B)//64 stays exact.

Paired note: docs/KCPT_KERNEL_KREAL_READOUT_FACE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-18.md
Cache: logs/runner-cache/kcpt_kernel_kreal_readout_face_classification_2026_07_18.txt
"""

import os
import re
import sys
import itertools
import numpy as np
from sympy import Matrix, eye, symbols, expand, I as sy_I, im as sy_im, re as sy_re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PASS = 0
FAIL = 0


def gate(tag, cond, desc):
    global PASS, FAIL
    ok = bool(cond)
    print(f"[{tag}] {'PASS' if ok else 'FAIL'} {desc}")
    if ok:
        PASS += 1
    else:
        FAIL += 1
    return ok


# ------------------------------------------------------------------ construction
L = 4
N = 64


def idx(x1, x2, x3):
    return (x1 * L + x2) * L + x3


coords = np.zeros((N, 3), dtype=np.int64)
for a in range(L):
    for b in range(L):
        for c in range(L):
            coords[idx(a, b, c)] = (a, b, c)


def eta_mu(mu, x):
    if mu == 0:
        return 1
    if mu == 1:
        return (-1) ** int(x[0])
    return (-1) ** int(x[0] + x[1])


e = [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])]
D2 = np.zeros((N, N), dtype=np.int64)
for i in range(N):
    x = coords[i]
    for mu in range(3):
        D2[i, idx(*((x + e[mu]) % L))] += eta_mu(mu, x)
        D2[i, idx(*((x - e[mu]) % L))] -= eta_mu(mu, x)

SUBSETS = [(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]
HW = [0, 1, 1, 1, 2, 2, 2, 3]
sub_index = {s: k for k, s in enumerate(SUBSETS)}


def sub_xor(sa, sb):
    return tuple(sorted(set(sa).symmetric_difference(set(sb))))


V8 = np.zeros((N, 8), dtype=np.int64)
for i in range(N):
    x = coords[i]
    for k, S in enumerate(SUBSETS):
        V8[i, k] = (-1) ** int(sum(x[j] for j in S))


def perm(fmap):
    P = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        y = np.array(fmap(coords[i])) % L
        P[i, idx(int(y[0]), int(y[1]), int(y[2]))] = 1
    return P


UR = perm(lambda x: (x[1], x[2], x[0]))
U2 = perm(lambda x: (-x[1], -x[0], -x[2]))
STAB = np.eye(N, dtype=np.int64)
TR = {t: perm(lambda x, t=t: (x[0] - t[0], x[1] - t[1], x[2] - t[2]))
      for t in itertools.product(range(L), repeat=3)}


def signfield(bits):
    a1, a2, a3, b12, b13, b23 = bits
    d = np.zeros(N, dtype=np.int64)
    for i in range(N):
        x1, x2, x3 = coords[i]
        expo = a1 * x1 + a2 * x2 + a3 * x3 + b12 * x1 * x2 + b13 * x1 * x3 + b23 * x2 * x3
        d[i] = (-1) ** int(expo)
    return d


ALLBITS = list(itertools.product([0, 1], repeat=6))
SF = {bits: signfield(bits) for bits in ALLBITS}
BASES = {"stab": STAB, "U2": U2, "UR": UR}
I8 = 64 * np.eye(8, dtype=np.int64)


def induced(U):
    return V8.T @ U @ V8


def mul(A, B):
    P = A @ B
    assert np.all(P % 64 == 0), "mul divisibility failure"
    return P // 64


def eqm(a, b):
    return np.array_equal(a, b)


# ------------------------------------------------------- scan the dressed classes
scan = {}
for name, base in BASES.items():
    commuting = []
    for bits in ALLBITS:
        diagd = np.diag(SF[bits])
        for t in itertools.product(range(L), repeat=3):
            U = diagd @ base @ TR[t]
            if np.array_equal(U @ D2, D2 @ U):
                commuting.append((bits, t, induced(U)))
    scan[name] = dict(commuting=commuting)


def closure(gs):
    gs = [g.copy() for g in gs]
    elts = {g.tobytes(): g for g in gs}
    frontier = list(elts.values())
    while frontier:
        nf = []
        for x in frontier:
            for g in gs:
                p = mul(x, g)
                k = p.tobytes()
                if k not in elts:
                    elts[k] = p
                    nf.append(p)
        frontier = nf
    return list(elts.values())


def block_diag(K):
    for i in range(8):
        for j in range(8):
            if HW[i] != HW[j] and K[i, j] != 0:
                return False
    return True


def triplet_pres(K):
    for c in (1, 2, 3):
        for r in range(8):
            if r not in (1, 2, 3) and K[r, c] != 0:
                return False
    return True


def axis_word(axis, inter, present_axis):
    Jp = np.zeros((8, 8), dtype=np.int64)
    for c, S in enumerate(SUBSETS):
        r = sub_index[sub_xor(S, (axis,))]
        Jp[r, c] = 64 * ((-1) ** len(set(S) & inter)) * (1 if present_axis in S else -1)
    return Jp


# ------------------------------------------------------------- the induced group
gens_by_class = {name: [K for _, _, K in scan[name]["commuting"]] for name in BASES}
gens_all = {}
for name in BASES:
    for K in gens_by_class[name]:
        gens_all[K.tobytes()] = K
GEN = list(gens_all.values())
G = closure(GEN)
center = [g for g in G if all(eqm(mul(g, h), mul(h, g)) for h in G)]
central_sq = [g for g in center if eqm(mul(g, g), -I8)]

# find raw J64 by the selection rule, then normalize
i_vac = sub_index[()]
i_x2 = sub_index[(1,)]
cand_J64 = [g for g in central_sq if g[i_vac, i_x2] > 0]
J64 = cand_J64[0] if cand_J64 else np.zeros((8, 8), dtype=np.int64)
otherJ64 = [g for g in central_sq if not eqm(g, J64)]
otherJ64 = otherJ64[0] if otherJ64 else np.zeros((8, 8), dtype=np.int64)
jm_int = J64 // 64
jm = Matrix(jm_int.tolist())

# genpair: first scan-order pair of induced generators whose closure is all 96
genpair = None
for a in range(len(GEN)):
    for b in range(a + 1, len(GEN)):
        if len(closure([GEN[a], GEN[b]])) == 96:
            genpair = [GEN[a], GEN[b]]
            break
    if genpair:
        break


# ------------------------------------------------------------------ note reading
def read_text(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return None


def normalize(text):
    lines = [re.sub(r'^\s*>\s?', '', ln) for ln in text.split('\n')]
    return re.sub(r'\s+', ' ', ' '.join(lines)).strip()


NOTE_PATH = os.path.join(
    ROOT, "docs",
    "KCPT_KERNEL_KREAL_READOUT_FACE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-18.md")
note_raw = read_text(NOTE_PATH)
note_norm = normalize(note_raw) if note_raw is not None else ""


# --------------------------------------------------------------- symbolic helpers
eye8 = eye(8)


def zmat(M):
    return all(expand(x) == 0 for x in M)


def E(M, v):
    return expand((v.conjugate().T * M * v)[0, 0])


def Bform(M, v, vp):
    return expand((v.T * M * vp)[0, 0])


def real_entries(M):
    return all(expand(sy_im(x)) == 0 for x in M)


def obj_eye(n):
    Emat = np.zeros((n, n), dtype=object)
    for i in range(n):
        Emat[i, i] = 1
    return Emat


e0col = Matrix([1, 0, 0, 0, 0, 0, 0, 0])

# ============================================================================ B1
print("== B1 construction and ambient-K compatibility ==")
gate("B1.1", eqm(D2, -D2.T) and set(np.unique(D2).tolist()).issubset({-1, 0, 1}),
     "D2 integer antisymmetric (D2==-D2.T), entries in {-1,0,1}")
rankD2 = Matrix(D2.tolist()).rank()
gate("B1.2", rankD2 == 56, f"exact rank(D2)==56 so dim ker==8 (got {rankD2})")
gate("B1.3", eqm(D2 @ V8, np.zeros((N, 8), dtype=np.int64)),
     "D2 @ V8 == 0 exactly (corner waves span the kernel)")
gate("B1.4", eqm(V8.T @ V8, I8),
     "V8.T @ V8 == 64 I8 exactly (orthogonal corner-wave frame)")
gate("B1.5", HW == [0, 1, 1, 1, 2, 2, 2, 3]
     and [HW.count(h) for h in (0, 1, 2, 3)] == [1, 3, 3, 1],
     "Hamming grading of SUBSETS == [0,1,1,1,2,2,2,3] (counts 1+3+3+1)")
csym = Matrix(symbols('c0:8'))
V8s = Matrix(V8.tolist())
gate("B1.6", zmat((V8s * csym).conjugate() - V8s * csym.conjugate()),
     "conj(V8 c) == V8 conj(c) entrywise (V8 real: kernel K is ambient K restricted)")

# ============================================================================ B2
print("== B2 group, central complex structure, commutant (found, not hardcoded) ==")
gate("B2.1", len(GEN) == 24, f"generator scan yields exactly 24 distinct induced images (got {len(GEN)})")
gate("B2.2a", len(G) == 96, f"closure under mul has order exactly 96 (got {len(G)})")
gate("B2.2b", any(eqm(g, -I8) for g in G), "the closure contains -64 I8")
gate("B2.3", len(center) == 4, f"center (commuting with all 96) has order exactly 4 (got {len(center)})")
gate("B2.4", len(central_sq) == 2,
     f"exactly 2 central elements satisfy mul(g,g)==-64 I8 (got {len(central_sq)})")
gate("B2.5", len(cand_J64) == 1,
     "selection rule: exactly ONE central square-root has entry [i_vac,i_x2] > 0 (that is J64)")

formula_ok = True
for S in SUBSETS:
    r = sub_index[sub_xor(S, (1,))]
    c = sub_index[S]
    val = 64 * ((-1) ** len(set(S) & {0, 2})) * (1 if 1 in S else -1)
    if int(J64[r, c]) != val:
        formula_ok = False
gate("B2.6a", formula_ok,
     "closed-form gate: J64[idx(S^{1}),idx(S)] == 64*(-1)^{|S&{0,2}|}*(+1 iff 1 in S)")
gate("B2.6b", int(np.count_nonzero(J64)) == 8, "J64 has exactly 8 nonzero entries")
gate("B2.7a", eqm(J64.T, -J64), "J64.T == -J64")
gate("B2.7b", eqm(mul(J64, J64), -I8), "mul(J64,J64) == -64 I8 (so j^2 == -I)")
gate("B2.7c", int(np.trace(J64)) == 0, "trace(J64) == 0")

Zg = np.array([[1, 0], [0, -1]], dtype=np.int64)
iYg = np.array([[0, 1], [-1, 0]], dtype=np.int64)
pauli = np.kron(Zg, np.kron(iYg, Zg))


def binval(S):
    return 4 * (0 in S) + 2 * (1 in S) + 1 * (2 in S)


Pb = np.zeros((8, 8), dtype=np.int64)
for S in SUBSETS:
    Pb[binval(S), sub_index[S]] = 1
gate("B2.8", eqm(Pb @ jm_int @ Pb.T, pauli),
     "j == Z (x) iY (x) Z on the parity qubits (Z=diag(1,-1), iY=[[0,1],[-1,0]])")

gate("B2.9", genpair is not None and len(closure(genpair)) == 96,
     "genpair: the first scan-order induced pair whose closure has order 96 exists")

K1n = Matrix(genpair[0].tolist()) / 64
K2n = Matrix(genpair[1].tolist()) / 64
blocks = []
for Kn in (K1n, K2n):
    Kobj = np.array(Kn.tolist(), dtype=object)
    Ie = obj_eye(8)
    M = np.kron(Kobj, Ie) - np.kron(Ie, Kobj.T)
    blocks.append(Matrix(M.tolist()))
commutant_dim = len(Matrix.vstack(*blocks).nullspace())
gate("B2.10a", commutant_dim == 2,
     f"rational commutant (stacked kron equations) has nullspace length exactly 2 (got {commutant_dim})")
comm_ok = all((Kn * jm - jm * Kn).is_zero_matrix for Kn in (K1n, K2n))
vecI = Matrix([eye8[i, j] for i in range(8) for j in range(8)])
vecj = Matrix([jm[i, j] for i in range(8) for j in range(8)])
indep = Matrix.hstack(vecI, vecj).rank() == 2
gate("B2.10b", comm_ok and indep,
     "both I8 and j commute with the two normalized generators and are linearly independent")

# ============================================================================ B3
print("== B3 T1 Hermitian bridge (symbolic) ==")
A = Matrix(8, 8, symbols('a0:64', real=True))
H1 = (A + A.T) / 2
H2 = -sy_I * (A - A.T) / 2
gate("B3.1", zmat(H1 - H1.conjugate().T) and zmat(H1.conjugate() - H1),
     "H1=(A+A^T)/2 is Hermitian and K-even (conjugate(H1)==H1)")
gate("B3.2", zmat(H2 - H2.conjugate().T) and zmat(H2.conjugate() + H2),
     "H2=-i(A-A^T)/2 is Hermitian and K-odd (conjugate(H2)==-H2)")
symp = (A + A.T) / 2
asymp = (A - A.T) / 2
n_sym = sum(1 for i in range(8) for j in range(8) if i <= j and expand(symp[i, j]) != 0)
n_asym = sum(1 for i in range(8) for j in range(8) if i < j and expand(asymp[i, j]) != 0)
diag_asym_zero = all(expand(asymp[i, i]) == 0 for i in range(8))
gate("B3.3", zmat(A - (H1 + sy_I * H2)) and n_sym == 36 and n_asym == 28
     and (36 + 28) == 64 and diag_asym_zero,
     "A == H1 + i H2; rigid split dims 36 + 28 == 64 (symmetric/antisymmetric counts)")

wr = Matrix(symbols('wr0:8', real=True))
wi = Matrix(symbols('wi0:8', real=True))
w = wr + sy_I * wi
EA = E(A, w)
EAc = expand(EA.conjugate())
gate("B3.4a", expand(E(H1, w) - (EA + EAc) / 2) == 0,
     "E(H1,w) == (E(A,w)+conjugate(E(A,w)))/2 (real part)")
gate("B3.4b", expand(E(H2, w) - (EA - EAc) / (2 * sy_I)) == 0,
     "E(H2,w) == (E(A,w)-conjugate(E(A,w)))/(2 i) (imaginary part)")
wbar = wr - sy_I * wi
gate("B3.5", expand(E(A, wbar) - EAc) == 0,
     "conjugate-values lemma: E(A,conjugate(w)) == conjugate(E(A,w)) (A real)")
Ejw = E(jm, w)
gate("B3.6", expand(E(jm, wbar) - expand(Ejw.conjugate())) == 0,
     "lemma instance for the concrete real matrix j")

# ============================================================================ B4
print("== B4 T2/T3 face classification ==")
a_s, c_s = symbols('a c', real=True)
F = a_s * eye8 + c_s * (sy_I * jm)
gate("B4.1", zmat(F - F.conjugate().T),
     "F = a I + c (i j) is Hermitian for real a,c")
gate("B4.2", (not zmat((eye8 + jm) - (eye8 + jm).conjugate().T))
     and (not zmat((sy_I * eye8) - (sy_I * eye8).conjugate().T)),
     "rejectors: I + j is NOT Hermitian; i I is NOT Hermitian")
gate("B4.3a", zmat(F.conjugate() - F + 2 * c_s * sy_I * jm),
     "conjugate(F) - F == -2 c (i j) (identity)")
gate("B4.3b", not zmat((F.conjugate() - F).subs(c_s, 1)),
     "at c==1 the K-defect -2 c (i j) is nonzero: K-reality of F forces c==0")
gate("B4.3c", (not real_entries(sy_I * jm)) and real_entries(eye8),
     "entrywise reality: i j FAILS the all-real test, I PASSES")
gate("B4.4", zmat((sy_I * jm) - (sy_I * jm).conjugate().T)
     and zmat((sy_I * jm).conjugate() + sy_I * jm),
     "i j is Hermitian (a=0 case) and K-odd (conjugate(i j) == -(i j))")
PW = (eye8 - sy_I * jm) / 2
PWb = (eye8 + sy_I * jm) / 2
gate("B4.5", zmat(PW * PW - PW) and zmat(PWb * PWb - PWb) and zmat(PW * PWb)
     and zmat(PW + PWb - eye8) and zmat((PWb - PW) - sy_I * jm),
     "P_W=(I - i j)/2, P_Wbar=(I + i j)/2 orthogonal idempotents; sum I; diff == i j")
gate("B4.6", zmat(jm * PW - sy_I * PW) and zmat(jm * PWb + sy_I * PWb),
     "eigenaction: j P_W == i P_W and j P_Wbar == -i P_Wbar")
gate("B4.7", PW.rank() == 4 and PWb.rank() == 4,
     "rank(P_W)==4 and rank(P_Wbar)==4 (exact sympy rank)")
gate("B4.8", zmat(PW.conjugate() - PWb),
     "conjugate(P_W) == P_Wbar (the projectors are non-K-real)")
v0 = e0col - sy_I * (jm * e0col)
v0b = v0.conjugate()
nv0 = expand((v0.conjugate().T * v0)[0, 0])
gate("B4.9",
     nv0 == 2
     and E(PW, v0) == 2 and E(PW, v0b) == 0
     and E(PWb, v0) == 0 and E(PWb, v0b) == 2
     and E(sy_I * jm, v0) == -2 and E(sy_I * jm, v0b) == 2,
     "value table on (v0, conj v0): |v0|^2=2; P_W->(2,0); P_Wbar->(0,2); i j->(-2,+2)")
gate("B4.10",
     E(jm, v0) == 2 * sy_I and E(jm, v0b) == -2 * sy_I
     and expand(sy_re(E(jm, v0))) == 0 and expand(sy_re(E(jm, v0b))) == 0
     and real_entries(jm) and zmat(jm.T + jm),
     "E_j(w)=i|w|^2 on pair: E(j,v0)=2i, E(j,conj v0)=-2i; equal (zero) real parts; j real, j^T==-j")
u = Matrix(symbols('u0:8', real=True))
wu = u - sy_I * (jm * u)
gate("B4.11a", expand(E(jm, wu) - 2 * sy_I * (u.T * u)[0, 0]) == 0,
     "generic witness: E(j, u - i j u) == 2 i (u^T u)")
gate("B4.11b", expand((wu.conjugate().T * wu)[0, 0] - 2 * (u.T * u)[0, 0]) == 0,
     "generic norm: |u - i j u|^2 == 2 (u^T u)")

# ============================================================================ B5
print("== B5 T4 bilinear nullity (transpose pairing, NO conjugation) ==")
gate("B5.1", zmat(jm * v0 - sy_I * v0), "j v0 == i v0 (v0 lies in W)")
up = Matrix(symbols('up0:8', real=True))
wW = u - sy_I * jm * u
wpW = up - sy_I * jm * up
gate("B5.2", Bform(eye8, wW, wpW) == 0,
     "total isotropy: B(I, u - i j u, u' - i j u') == 0 on W")
cert = 0
zero88 = np.zeros((8, 8), dtype=np.int64)
for g in G:
    if eqm(g @ jm_int, jm_int @ g) and eqm(g + jm_int @ g @ jm_int, zero88):
        cert += 1
gate("B5.3", cert == 96,
     f"integer certificate g j == j g AND g + j g j == 0 holds for all 96 members (count {cert})")
g1n = Matrix(genpair[0].tolist()) / 64
wWb = u + sy_I * jm * u
wpWb = up + sy_I * jm * up
gate("B5.4a", Bform(g1n, wW, wpW) == 0,
     "spot-check: B(g1, w, w') == 0 on W (first normalized generator)")
gate("B5.4b", Bform(g1n, wWb, wpWb) == 0,
     "spot-check: B(g1, w, w') == 0 on Wbar")
gate("B5.5", Bform(eye8, e0col, e0col) == 1,
     "non-null control: B(I, e_0, e_0) == 1 (real vectors register)")
E00 = e0col * e0col.T
E00int = np.zeros((8, 8), dtype=np.int64)
E00int[0, 0] = 1
cert_E00 = eqm(E00int @ jm_int, jm_int @ E00int)
gate("B5.6", (not cert_E00) and Bform(E00, v0, v0) == 1,
     "discriminator: E_00=e_0 e_0^T fails the certificate and registers 1 on W")

# ============================================================================ B6
print("== B6 T5 neutrality, negative controls, ambient scale ==")
gate("B6.1", zmat((eye8 - sy_I * (-jm)) / 2 - PWb),
     "orientation swap: (I - i(-j))/2 == P_Wbar")
gate("B6.2", eqm(otherJ64, -J64),
     "the OTHER central square-root of -64 I8 equals -J64")
gG = [g for g in G if block_diag(g)]
gate("B6.3", len(gG) == 4 and all(eqm(g, np.diag(np.diag(g))) for g in gG),
     "exactly 4 graded members of G, all diagonal")
w1, w2, w3 = symbols('w1 w2 w3', real=True)
Wdiag = Matrix.diag(w1, w2, w3)
neutral = True
for g in gG:
    R = Matrix((g[np.ix_([1, 2, 3], [1, 2, 3])] // 64).tolist())
    if not zmat(R * Wdiag - Wdiag * R):
        neutral = False
gate("B6.4", neutral,
     "r-neutral: each graded triplet restriction commutes with diag(w1,w2,w3)")
Jx1 = axis_word(0, {1, 2}, 0)
Jx3 = axis_word(2, {0, 1}, 2)
gate("B6.5", any(not eqm(Jx1 @ g, g @ Jx1) for g in G),
     "wrong-axis rejector: axis-1 word fails centrality on some g in G")
gate("B6.6", any(not eqm(Jx3 @ g, g @ Jx3) for g in G),
     "wrong-axis rejector: axis-3 word fails centrality on some g in G")
gate("B6.7", zmat((PW - PWb) + sy_I * jm) and (not zmat((PW - PWb) - sy_I * jm)),
     "wrong-sign polarization rejector: P_W - P_Wbar == -(i j) and != i j")
gate("B6.8", not zmat(jm * v0 + sy_I * v0),
     "wrong-eigenvalue rejector: j v0 != -i v0")
gate("B6.9", real_entries(jm) and real_entries(eye8)
     and (not real_entries(sy_I * jm)) and (not real_entries(PW)),
     "K-reality battery: real for j and I; NOT real for i j and P_W")
M64 = V8 @ jm_int @ V8.T
M64s = Matrix(M64.tolist())
vc = Matrix(symbols('v0:8'))
big = V8s * vc
lhs610 = expand((big.conjugate().T * M64s * big)[0, 0])
rhs610 = expand(4096 * E(jm, vc))
gate("B6.10", expand(lhs610 - rhs610) == 0 and 4096 == 64 ** 2,
     "ambient scale: (V8 v)^dag (V8 j V8^T)(V8 v) == 4096 E(j,v), 4096 == 64^2")
big0 = V8s * v0
gate("B6.11", expand((big0.conjugate().T * big0)[0, 0]) == 128 and 128 == 64 * 2,
     "ambient norm: |V8 v0|^2 == 128 == 64*2")

# ============================================================================ B7
print("== B7 verbatim quote gates ==")
CARR_PATH = os.path.join(
    ROOT, "docs",
    "KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md")
MECH_PATH = os.path.join(
    ROOT, "docs",
    "KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md")
KERN_PATH = os.path.join(
    ROOT, "docs",
    "KCPT_KERNEL_INDUCED_REPRESENTATION_CENTRAL_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-18.md")
AX_PATH = os.path.join(ROOT, "docs", "MINIMAL_AXIOMS_2026-06-29.md")

FRAGMENTS = [
    ("B7.Q1", CARR_PATH, "graded by Hamming weight as `1 + 3 + 3 + 1`"),
    ("B7.Q2", CARR_PATH, "`eta_1 = 1`, `eta_2(x) = (-1)^{x_1}`, `eta_3(x) = (-1)^{x_1 + x_2}`"),
    ("B7.Q3", CARR_PATH, "its exact rank is `56`"),
    ("B7.Q4", CARR_PATH,
     "Antilinear and non-Hermitian functionals, interacting extensions, and lattice-wide readouts are untested and outside the claim."),
    ("B7.Q5", MECH_PATH,
     "**FLAG — two-model mechanism:** the entrywise-conjugate presentations in L-K2 satisfy the same named clauses and exchange every K-odd seed."),
    ("B7.Q6", MECH_PATH,
     "The memo's live Qualification leaves the unfixed choice conditional/open."),
    ("B7.Q7", KERN_PATH,
     "The exact commutant of `G` over the rationals is two-dimensional, `span{I, j}`"),
    ("B7.Q8", KERN_PATH,
     "entrywise complex conjugation fixes the entire real induced group `G`"),
    ("B7.Q9", KERN_PATH,
     "the two normalized central complex structures `+j` and `-j`"),
    ("B7.Q10", KERN_PATH,
     "It does NOT select the orientation: `+j` versus `-j` remains the two-presentation choice"),
    ("B7.Q11", AX_PATH, "standard translations, and proper cubic rotations"),
]
for tag, path, frag in FRAGMENTS:
    src = read_text(path)
    src_norm = normalize(src) if src is not None else ""
    frag_norm = normalize(frag)
    in_src = frag_norm in src_norm
    in_note = frag_norm in note_norm
    if not in_src:
        pos = src_norm.find(frag_norm[:28])
        near = src_norm[pos:pos + len(frag_norm) + 12] if pos >= 0 else "(anchor not found)"
        print(f"    [{tag}] source fragment missing; nearest actual text: {near!r}")
    gate(tag, in_src and in_note, "verbatim fragment present in source AND in the new note")

# ============================================================================ B8
print("== B8 sharded-ledger existence ==")
LEDGERS = [
    ("B8.1", "docs/audit/data/ledger/kc/kcpt_corner_carrier_lattice_delivery_hw1_doublet_pair_polarization_bounded_theorem_note_2026-07-17.json"),
    ("B8.2", "docs/audit/data/ledger/kc/kcpt_coupling_triple_two_presentation_derivable_class_spectral_pairing_bounded_theorem_note_2026-07-16.json"),
    ("B8.3", "docs/audit/data/ledger/mi/minimal_axioms.json"),
]
for tag, rel in LEDGERS:
    gate(tag, os.path.isfile(os.path.join(ROOT, rel)),
         f"ledger shard exists: {os.path.basename(rel)}")

# ============================================================================ B9
print("== B9 note hygiene ==")
if note_raw is None:
    for tag in ("B9.1", "B9.2", "B9.3", "B9.4", "B9.5"):
        gate(tag, False, "note file not found")
else:
    forbidden = ["only route", "last route", "exhaust", "closes the route",
                 "closes this route", "no other route", "final route",
                 "retained", "unaudited", "effective_status", "audit grade",
                 "Unit 3", "PR #", "unlanded", "spec file", "required for the record"]
    present_forbidden = [s for s in forbidden if s in note_norm]
    gate("B9.1", not present_forbidden,
         f"forbidden route/status strings absent (found: {present_forbidden})")
    dec = re.search(r'[0-9]\.[0-9]', note_raw)
    gate("B9.2", dec is None,
         f"no bare-decimal literal [0-9].[0-9] in note (match: {dec.group(0) if dec else None})")
    links = re.findall(r'\]\(([^)]+)\)', note_raw)
    dependency_links = {
        "KCPT_KERNEL_INDUCED_REPRESENTATION_CENTRAL_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-18.md",
        "KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md",
        "KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md",
        "MINIMAL_AXIOMS_2026-06-29.md",
    }
    artifact_links = {
        "../scripts/kcpt_kernel_kreal_readout_face_classification_2026_07_18.py",
        "../logs/runner-cache/kcpt_kernel_kreal_readout_face_classification_2026_07_18.txt",
    }
    expected_links = dependency_links | artifact_links
    deps_exist = all(os.path.isfile(os.path.join(ROOT, "docs", b)) for b in dependency_links)
    gate("B9.3",
         len(links) == len(expected_links) and set(links) == expected_links and deps_exist,
         "link set == exactly the 4 dependencies + 2 artifacts; each dependency exists in docs/")
    runner_rel = "kcpt_kernel_kreal_readout_face_classification_2026_07_18.py"
    cache_link = "../logs/runner-cache/kcpt_kernel_kreal_readout_face_classification_2026_07_18.txt"
    required = ["**Type:** bounded_theorem", "bounded theorem", "does NOT select",
                "Boundary", "K-real", runner_rel, cache_link]
    missing = [s for s in required if s not in note_raw]
    gate("B9.4", not missing, f"required strings present (missing: {missing})")
    verbatim_math = ["`span{I, j}`", "`i j = P_Wbar - P_W`", "`P_W = (I - i j)/2`",
                     "`E_j(w) = i |w|^2`", "`g + j g j = 0`", "`Z (x) iY (x) Z`",
                     "`{a I + c (i j)}`", "`conj(V8 c) = V8 conj(c)`"]
    missing_math = [s for s in verbatim_math if s not in note_raw]
    gate("B9.5", not missing_math,
         f"PRESERVE-VERBATIM math strings present (missing: {missing_math})")

# ================================================================= final tally
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
