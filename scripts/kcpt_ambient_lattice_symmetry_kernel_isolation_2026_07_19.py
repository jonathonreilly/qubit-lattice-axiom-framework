#!/usr/bin/env python3
"""KCPT ambient lattice symmetry: kernel-block isolation, the averaged complex
structure, and lattice-wide K-real registration.

Class-A finite check on the fixed 4^3 staggered surface. The staggered adjacency
D2, the corner-wave kernel frame V8, the induced integer group, and the central
complex structure are rebuilt from the construction (machinery copied from the
landed kernel runner); the ambient D2-commuting dressed closure of order 768 is
produced by scan plus BFS closure; the induced homomorphism onto the 96-element
group is checked against an independent regeneration; character sums exhibit the
kernel-image isolation split; the group average of the corner transition is the
lifted complex structure; and the lattice-wide invariant readout faces are
registered on the kernel doublet. Every load-bearing gate uses exact integer
numpy (int64, with Python-int / object arithmetic for the character sums and the
sesquilinear values) and exact sympy Rational / symbolic conjugation; no floating
point enters any gate. Each gate prints one line; the script prints a final
TOTAL line and exits nonzero on any failure.
"""
import os
import re
import itertools
import numpy as np
import sympy as sp

# ----------------------------------------------------------------------------
# Bookkeeping
# ----------------------------------------------------------------------------
PASS = 0
FAIL = 0


def gate(tag, cond, desc):
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{tag}] {'PASS' if ok else 'FAIL'} - {desc}")
    return ok


def eqm(a, b):
    return np.array_equal(a, b)


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOCS = os.path.join(ROOT, "docs")

# ----------------------------------------------------------------------------
# Construction (copied verbatim from the landed kernel runner)
# ----------------------------------------------------------------------------
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
HW = [len(S) for S in SUBSETS]
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

eye8 = np.eye(8, dtype=np.int64)
I8 = 64 * eye8
ZERO = np.zeros((N, N), dtype=np.int64)


def induced(U):
    return V8.T @ U @ V8


def mul(A, B):
    P = A @ B
    assert np.all(P % 64 == 0)
    return P // 64


def closure_mul(gs):
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


def closure_amb(gs):
    gs = [g.copy() for g in gs]
    elts = {g.tobytes(): g for g in gs}
    frontier = list(elts.values())
    while frontier:
        nf = []
        for x in frontier:
            for g in gs:
                p = x @ g
                k = p.tobytes()
                if k not in elts:
                    elts[k] = p
                    nf.append(p)
        frontier = nf
    return list(elts.values())


# ============================================================================
# B1 - construction (copied machinery re-gated)
# ============================================================================
gate("B1.1", eqm(D2, -D2.T) and set(np.unique(D2)).issubset({-1, 0, 1}),
     "D2 integer, antisymmetric (D2 == -D2.T), entries in {-1,0,1}")
gate("B1.2", sp.Matrix(D2.tolist()).rank() == 56,
     "exact rank(D2) == 56 via sympy (kernel dimension 8)")
gate("B1.3", eqm(D2 @ V8, np.zeros((N, 8), dtype=np.int64)),
     "D2 @ V8 == 0 exactly")
gate("B1.4", eqm(V8.T @ V8, I8),
     "V8.T @ V8 == 64 * I8 exactly")
gate("B1.5", HW == [0, 1, 1, 1, 2, 2, 2, 3]
     and [HW.count(w) for w in (0, 1, 2, 3)] == [1, 3, 3, 1],
     "Hamming-weight grading of SUBSETS == [0,1,1,1,2,2,2,3] (counts 1+3+3+1)")
_csym = sp.Matrix(sp.symbols("c0:8"))
_V8s = sp.Matrix(V8.tolist())
_lhs = (_V8s * _csym).applyfunc(sp.conjugate)
_rhs = _V8s * _csym.applyfunc(sp.conjugate)
gate("B1.6", sp.expand(_lhs - _rhs) == sp.zeros(N, 1),
     "symbolic conj(V8 c) == V8 conj(c) entrywise (V8 real)")

# ============================================================================
# B2 - the ambient group (scan + BFS closure; nothing hardcoded)
# ============================================================================
commuting = {}
for name, base in BASES.items():
    lst = []
    for bits in ALLBITS:
        dd = np.diag(SF[bits])
        for t in itertools.product(range(L), repeat=3):
            U = dd @ base @ TR[t]
            if eqm(U @ D2, D2 @ U):
                lst.append(U.copy())
    commuting[name] = lst
per_class = {n: len(commuting[n]) for n in BASES}
amb_scan = [U for n in BASES for U in commuting[n]]
gate("B2.1", sum(per_class.values()) == 192 and all(v == 64 for v in per_class.values()),
     f"scan keeps 192 D2-commuting members, 64 per class ({per_class})")


# B2.2 representation self-check: dense matmul vs an independently coded
# signed-permutation index formula (index-formula conjugation is a known bug
# source, so it is cross-checked here). E_test is the named construction
# outer(V8[:,0], V8[:,2]); the named object is 64 x 64 (V8 columns are length 64).
def perm_sign(U):
    cols = np.argmax(np.abs(U), axis=1)
    signs = U[np.arange(N), cols]
    return cols, signs


def conj_index(U, M):
    cols, signs = perm_sign(U)
    out = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        si = signs[i]
        ci = cols[i]
        for j in range(N):
            out[i, j] = si * signs[j] * M[ci, cols[j]]
    return out


def prod_index(Ua, Ub):
    ca, sa = perm_sign(Ua)
    cb, sb = perm_sign(Ub)
    out = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        c = cb[ca[i]]
        out[i, c] = sa[i] * sb[ca[i]]
    return out


E_test = np.outer(V8[:, 0], V8[:, 2])
b22 = True
for U in amb_scan[:5]:
    if not eqm(U @ E_test @ U.T, conj_index(U, E_test)):
        b22 = False
for Ua, Ub in zip(amb_scan[:5], amb_scan[5:10]):
    if not eqm(Ua @ Ub, prod_index(Ua, Ub)):
        b22 = False
gate("B2.2", b22,
     "representation self-check: dense matmul == signed-perm index formula "
     "(conjugation on E_test and 5 products)")

Gamb = closure_amb(amb_scan)
keys = [U.tobytes() for U in Gamb]
gate("B2.3", len(Gamb) == 768 and len(set(keys)) == 768,
     "BFS closure of the 192 has order exactly 768, all distinct")
gate("B2.4", all(eqm(U @ D2, D2 @ U) for U in Gamb),
     "every one of the 768 commutes with D2 exactly")
gate("B2.5", all(eqm(64 * (U @ V8), V8 @ (V8.T @ U @ V8)) for U in Gamb),
     "kernel preserved: 64*(U@V8) == V8@(V8.T@U@V8) for all 768")

ind_all = [induced(U) for U in Gamb]
ker_pi = [U for U, ind in zip(Gamb, ind_all) if eqm(ind, I8)]
gate("B2.6", len(ker_pi) == 8,
     "exactly 8 members induce the identity V8.T@U@V8 == 64*I8 (ker pi)")
exp_ker = {TR[t].tobytes() for t in itertools.product([0, 2], repeat=3)}
gate("B2.7", set(U.tobytes() for U in ker_pi) == exp_ker,
     "ker pi is exactly the 8 pure translations TR[t], t in {0,2}^3")
kerset = set(U.tobytes() for U in ker_pi)
eye64 = np.eye(N, dtype=np.int64)
b28 = (all(eqm(U @ U, eye64) for U in ker_pi)
       and all(eqm(A @ B, B @ A) and (A @ B).tobytes() in kerset
               for A in ker_pi for B in ker_pi))
gate("B2.8", b28,
     "every ker pi member squares to I; the 8 form elementary abelian (Z/2)^3")
gate("B2.9a", all((U @ T @ U.T).tobytes() in kerset for U in Gamb for T in ker_pi),
     "normality: U @ T @ U.T in ker pi for all 768 U and all 8 T")
gate("B2.9b", all(eqm(U @ U.T, eye64) for U in Gamb),
     "orthogonality: U @ U.T == I64 for all 768 (signed permutations)")

# ============================================================================
# B3 - induced image equals the landed group (independent regeneration)
# ============================================================================
image = {m.tobytes(): m for m in ind_all}
n96 = len(image)
gate("B3.1", n96 == 96,
     "the induced set {V8.T@U@V8} has exactly 96 distinct raw matrices")
# B2.10 needs the image count n96, so it is gated here
gate("B2.10", len(Gamb) == 8 * n96 and len(Gamb) == len(ker_pi) * n96,
     "count identity: 768 == 8 * 96 == |ker pi| * |induced image|")
GEN = list({induced(U).tobytes(): induced(U)
            for n in BASES for U in commuting[n]}.values())
Greg = closure_mul(GEN)
gate("B3.2", set(g.tobytes() for g in Greg) == set(image.keys()),
     "independent regeneration (generator scan + mul-closure) set-equals image")
imlist = list(image.values())
b33 = all(mul(A, B).tobytes() in image for A in imlist for B in imlist)
gate("B3.3", b33,
     "induced set is mul-closed over all 96 x 96 pairs (exact divisibility)")
gate("B3.4", I8.tobytes() in image and (-I8).tobytes() in image,
     "induced set contains 64*I8 and -64*I8")
gate("B3.5", all(eqm(K.T @ K, (64 ** 2) * eye8) for K in imlist),
     "every induced K8 satisfies K8.T @ K8 == 64^2 * I8")
center = [K for K in imlist if all(eqm(mul(K, H), mul(H, K)) for H in imlist)]
central_sq = [K for K in center if eqm(mul(K, K), -I8)]
gate("B3.6", len(central_sq) == 2,
     "exactly 2 central square roots of -I in the induced set")
i_vac = sub_index[()]
i_x2 = sub_index[(1,)]
cand = [K for K in central_sq if K[i_vac, i_x2] > 0]
gate("B3.7", len(cand) == 1
     and any(eqm(K, -cand[0]) for K in central_sq if not eqm(K, cand[0])),
     "selection: exactly one candidate with entry [i_vac,i_x2] > 0 is J64; "
     "the other is -J64")
J64 = cand[0]
b38 = True
for c, S in enumerate(SUBSETS):
    r = sub_index[sub_xor(S, (1,))]
    val = 64 * ((-1) ** len(set(S) & {0, 2})) * (1 if 1 in S else -1)
    if int(J64[r, c]) != val:
        b38 = False
gate("B3.8", b38 and int(np.count_nonzero(J64)) == 8,
     "closed-form gate against the found J64; exactly 8 nonzero entries")
gate("B3.9", eqm(J64.T, -J64) and eqm(mul(J64, J64), -I8) and int(np.trace(J64)) == 0,
     "J64.T == -J64; mul(J64,J64) == -64*I8; trace(J64) == 0")

# ============================================================================
# B4 - the ambient lift (raw integers Jr = V8@J64@V8.T, Pr = V8@V8.T)
# ============================================================================
Jr = V8 @ J64 @ V8.T
Pr = V8 @ V8.T
gate("B4.1", eqm(Jr.T, -Jr) and eqm(Jr @ Jr, -(64 ** 3) * Pr),
     "Jr antisymmetric integer; Jr @ Jr == -(64^3) * Pr")
gate("B4.2", eqm(Jr @ D2, ZERO) and eqm(D2 @ Jr, ZERO),
     "Jr @ D2 == 0 and D2 @ Jr == 0 (annihilates the image block)")
gate("B4.3", all(eqm(U @ Jr, Jr @ U) for U in Gamb),
     "Jr commutes with all 768 ambient members exactly")
gate("B4.4", eqm(Pr @ Jr, 64 * Jr) and eqm(Jr @ Pr, 64 * Jr),
     "kernel support: Pr @ Jr == 64*Jr == Jr @ Pr")
gate("B4.5", eqm(V8.T @ Jr @ V8, (64 ** 2) * J64),
     "compression: V8.T @ Jr @ V8 == 64^2 * J64")
M8 = np.array([[3 * i + j + 1 for j in range(8)] for i in range(8)], dtype=np.int64)
gate("B4.6", eqm(V8.T @ (V8 @ M8 @ V8.T) @ V8, (64 ** 2) * M8),
     "lift bijection: V8.T @ (V8 @ M8 @ V8.T) @ V8 == 64^2 * M8")

# ============================================================================
# B5 - character sums, isolation, averaging discriminators
# ============================================================================
t_all = [int(np.trace(U)) for U in Gamb]
k_all = [int(np.trace(m)) for m in ind_all]
gate("B5.1", len(t_all) == 768 and len(k_all) == 768,
     "per-member ambient and induced traces collected over all 768")
G = 768
S1 = sum(t * t for t in t_all)
S2 = sum(k * k for k in k_all)
S3 = sum((64 * t - k) * k for t, k in zip(t_all, k_all))
S4 = sum((64 * t - k) ** 2 for t, k in zip(t_all, k_all))
D = 64 ** 2 * G
gate("B5.2a", S1 % G == 0 and S1 // G == 12,
     "sum(t^2)/768 == 12 (total commutant dimension)")
gate("B5.2b", S2 % D == 0 and S2 // D == 2,
     "sum(k^2)/(64^2*768) == 2 (kernel-block commutant, span{I,j})")
gate("B5.2c", S3 % D == 0 and S3 // D == 0,
     "sum((64t-k)k)/(64^2*768) == 0 (kernel-image cross blocks vanish)")
gate("B5.2d", S4 % D == 0 and S4 // D == 10,
     "sum((64t-k)^2)/(64^2*768) == 10 (image-block commutant)")
gate("B5.3", (S1 // G) == (S2 // D) + 2 * (S3 // D) + (S4 // D)
     and (S1 // G) == 2 + 2 * 0 + 10,
     "consistency: 12 == 2 + 2*0 + 10")
trt = [int(np.trace(TR[t])) for t in itertools.product(range(L), repeat=3)]
St = sum(x * x for x in trt)
gate("B5.4", St == 64 ** 2 and St // 64 == 64,
     "translation-only control: sum(tr^2) == 64^2, commutant 64 (>> 12)")

a_all = [U @ V8[:, 0] for U in Gamb]
c_all = [U @ V8[:, 2] for U in Gamb]
d_all = [U @ D2[:, 0] for U in Gamb]
E_cross = np.outer(V8[:, 0], D2[:, 0])
S_cross = sum(np.outer(a, d) for a, d in zip(a_all, d_all))
gate("B5.5", np.any(E_cross != 0) and eqm(S_cross, ZERO),
     "cross average vanishes: E_cross nonzero but sum_U U@E_cross@U.T == 0")
E = np.outer(V8[:, 0], V8[:, 2])
S_kk = sum(np.outer(a, c) for a, c in zip(a_all, c_all))
gate("B5.6a", eqm(2 * S_kk, 3 * Jr),
     "corner average: 2 * S_kk == 3 * Jr exactly")
gate("B5.6b", eqm(S_kk, 96 * (V8 @ (J64 // 64) @ V8.T)),
     "corner average: S_kk == 96 * (V8 @ (J64//64) @ V8.T)")
gate("B5.7", int(np.trace(E)) == 0 and int(np.trace(Pr @ S_kk)) == 0
     and int(np.trace(Jr.T @ S_kk)) != 0,
     "alpha = 0 forced: trace(E) == 0, trace(Pr@S_kk) == 0, trace(Jr.T@S_kk) != 0")
gate("B5.8", (not eqm(S_kk, ZERO)) and (not eqm(S_kk, S_kk.T)) and eqm(S_cross, ZERO),
     "discriminators: S_kk != 0, S_kk has nonzero antisymmetric part, "
     "same code gives 0 on E_cross")

# ============================================================================
# B6 - lattice-wide K-real registration and value tables
# ============================================================================
F_re = np.outer(V8[:, 0], V8[:, 0])
F_im = E - E.T
gate("B6.1", eqm(F_re, F_re.T) and eqm(F_im, -F_im.T),
     "F0 = (F_re, F_im): F_re symmetric, F_im antisymmetric (Hermitian pair)")
S_re = sum(np.outer(a, a) for a in a_all)
S_im = sum(np.outer(a, c) - np.outer(c, a) for a, c in zip(a_all, c_all))
C_re = V8.T @ S_re @ V8
C_im = V8.T @ S_im @ V8
tr_re = int(np.trace(C_re))
a_c = tr_re // 8
ccn = int(np.trace(J64.T @ C_im))
ccd = int(np.trace(J64.T @ J64))
c_c = ccn // ccd
gate("B6.2a", tr_re % 8 == 0 and eqm(C_re, a_c * eye8),
     "averaged compression: C_re == a_c * I8 (exact, residual zero)")
gate("B6.2b", ccn % ccd == 0 and eqm(C_im, c_c * J64),
     "averaged compression: C_im == c_c * J64 (exact, residual zero)")
gate("B6.3", a_c != 0 and c_c != 0,
     f"both axes live: a_c != 0 and c_c != 0 (a_c={a_c}, c_c={c_c})")
gate("B6.4", eqm(C_re, a_c * eye8) and int(np.trace(J64.T @ C_re)) == 0,
     "K-real specialization: F_real = F_re averages to a_c*I8, J64-component zero")

# B6.5 imported forcing re-gated locally (exact sympy)
a_s, c_s = sp.symbols("a c", real=True)
jm = sp.Matrix(J64.tolist()) / 64
F_face = a_s * sp.eye(8) + c_s * (sp.I * jm)
gate("B6.5", sp.expand(F_face.applyfunc(sp.conjugate) - F_face - (-2 * c_s * sp.I * jm))
     == sp.zeros(8, 8) and jm[i_x2, i_vac] != 0,
     "sympy forcing: conj(F_face) - F_face == -2 c (i j); nonzero j entry forces c == 0")

UF = V8.T @ F_re @ V8
gate("B6.6", not eqm(UF, (int(UF[0, 0])) * eye8),
     f"rejector: unaveraged V8.T@F_re@V8 not a multiple of I8 "
     f"(UF[0,0]={int(UF[0,0])} != UF[1,1]={int(UF[1,1])})")

# Sesquilinear value of a Hermitian pair M = (Mre, Mim) on w = wr + i wi
# (real integer vectors), computed exactly on the split parts (object dtype).
def sesq(Mre, Mim, wr, wi):
    Mre = Mre.astype(object)
    Mim = Mim.astype(object)
    wr = wr.astype(object)
    wi = wi.astype(object)
    return int(wr @ Mre @ wr + wi @ Mre @ wi + 2 * (wi @ Mim @ wr))


A0 = 64 * V8[:, 0]
B0 = (V8 @ J64)[:, 0]
normw = int(A0.astype(object) @ A0.astype(object)) + int(B0.astype(object) @ B0.astype(object))
gate("B6.7", normw == 2 * 64 ** 3,
     "doublet norm: |w0|^2 = A0.A0 + B0.B0 == 2 * 64^3")
# w0 = A0 - i B0 -> (wr, wi) = (A0, -B0); conj w0 -> (A0, +B0)
gate("B6.8", sesq(ZERO, Jr, A0, -B0) == -2 * 64 ** 5
     and sesq(ZERO, Jr, A0, B0) == 2 * 64 ** 5,
     "K-odd separator: E_{iJr}(w0) == -2*64^5, E_{iJr}(conj w0) == +2*64^5")
PWre = 64 * Pr
gate("B6.9", sesq(PWre, -Jr, A0, -B0) == 4 * 64 ** 5
     and sesq(PWre, -Jr, A0, B0) == 0
     and sesq(PWre, Jr, A0, -B0) == 0
     and sesq(PWre, Jr, A0, B0) == 4 * 64 ** 5,
     "projector table: E_{PW}(w0)==4*64^5, E_{PW}(conj)==0; PWbar swaps the pair")
# B6.10 flag: Jr -> -Jr swaps PW/PWbar rows, flips B6.8 signs, leaves B6.11 fixed
Jr2 = -Jr
flag_swap = (sesq(PWre, -Jr2, A0, -B0) == 0
             and sesq(PWre, -Jr2, A0, B0) == 4 * 64 ** 5)
flag_flip = (sesq(ZERO, Jr2, A0, -B0) == 2 * 64 ** 5
             and sesq(ZERO, Jr2, A0, B0) == -2 * 64 ** 5)
Esre = sesq(S_re, ZERO, A0, -B0)
# rebuild the doublet member with J64 -> -J64 and recompute: the K-real value
# is unchanged on both members of the flipped pair
B0_flip = (V8 @ (-J64))[:, 0]
flag_fixed = (sesq(S_re, ZERO, A0, -B0_flip) == Esre
              and sesq(S_re, ZERO, A0, B0_flip) == Esre)
gate("B6.10", flag_swap and flag_flip and flag_fixed,
     "flag registration: Jr->-Jr swaps projector rows, flips K-odd signs, "
     "leaves the K-real norm-form value fixed")
# B6.11 norm-form registration: link three independently computed quantities
# (the sesquilinear value, the compressed coefficient, the compressed doublet norm)
z0r = 64 * eye8[:, 0]
z0i = -J64[:, 0]
z0_norm = (int(z0r.astype(object) @ z0r.astype(object))
           + int(z0i.astype(object) @ z0i.astype(object)))
gate("B6.11", z0_norm == 2 * 64 ** 2 and Esre == a_c * z0_norm
     and sesq(S_re, ZERO, A0, B0) == Esre,
     f"K-real norm form: E_{{S_re}}(w0) == a_c * |z0|^2 == E_{{S_re}}(conj w0), "
     f"|z0|^2 == 2*64^2 (Esre={Esre})")
BB = D2 @ D2.T
gate("B6.12", sesq(BB, ZERO, A0, -B0) == 0 and sesq(BB, ZERO, A0, B0) == 0
     and not eqm(BB, ZERO),
     "bulk-blindness: E_{BB}(w0) == 0 == E_{BB}(conj w0); BB != 0")

# ============================================================================
# B7 - verbatim quote gates (fragment substring of normalize(SOURCE) and note)
# ============================================================================
def normalize(text):
    lines = [re.sub(r"^\s*>\s?", "", ln) for ln in text.splitlines()]
    return re.sub(r"\s+", " ", " ".join(lines)).strip()


def read_doc(name):
    with open(os.path.join(DOCS, name), encoding="utf-8") as fh:
        return fh.read()


CARR = "KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md"
KERN = "KCPT_KERNEL_INDUCED_REPRESENTATION_CENTRAL_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-18.md"
KREAL = "KCPT_KERNEL_KREAL_READOUT_FACE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-18.md"
MECH = "KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md"
AX = "MINIMAL_AXIOMS_2026-06-29.md"

NOTE_NAME = "KCPT_AMBIENT_LATTICE_SYMMETRY_KERNEL_ISOLATION_AVERAGED_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-19.md"
note_raw = read_doc(NOTE_NAME)
note_n = normalize(note_raw)
src_n = {name: normalize(read_doc(name)) for name in (CARR, KERN, KREAL, MECH, AX)}

QUOTES = [
    (CARR, "graded by Hamming weight as `1 + 3 + 3 + 1`"),
    (CARR, "`eta_1 = 1`, `eta_2(x) = (-1)^{x_1}`, `eta_3(x) = (-1)^{x_1 + x_2}`"),
    (CARR, "its exact rank is `56`"),
    (CARR, "Antilinear and non-Hermitian functionals, interacting extensions, and lattice-wide readouts are untested and outside the claim."),
    (KERN, "The exact commutant of `G` over the rationals is two-dimensional, `span{I, j}`"),
    (KERN, "the two normalized central complex structures `+j` and `-j`"),
    (KERN, "It does NOT select the orientation: `+j` versus `-j` remains the two-presentation choice"),
    (KERN, "entrywise complex conjugation fixes the entire real induced group `G`"),
    (KREAL, "The `G`-invariant Hermitian face is exactly `{a I + c (i j)}` with `a, c` real, a two-dimensional real space."),
    (KREAL, "K-reality of `a I + c (i j)` forces `c = 0`, since `conj(F) - F = -2 c (i j)` is nonzero whenever `c` is."),
    (KREAL, "Genuinely antilinear readout functionals remain untested, as do interacting and lattice-wide readouts."),
    (MECH, "**FLAG — two-model mechanism:** the entrywise-conjugate presentations in L-K2 satisfy the same named clauses and exchange every K-odd seed."),
    (MECH, "The memo's live Qualification leaves the unfixed choice conditional/open."),
    (AX, "standard translations, and proper cubic rotations"),
]
for n, (name, frag) in enumerate(QUOTES, 1):
    fn = normalize(frag)
    gate(f"B7.{n}", fn in src_n[name] and fn in note_n,
         f"quote Q{n} present in source and note")

# ============================================================================
# B8 - ledger shard existence (3 gates)
# ============================================================================
shards = [
    "docs/audit/data/ledger/kc/kcpt_corner_carrier_lattice_delivery_hw1_doublet_pair_polarization_bounded_theorem_note_2026-07-17.json",
    "docs/audit/data/ledger/kc/kcpt_coupling_triple_two_presentation_derivable_class_spectral_pairing_bounded_theorem_note_2026-07-16.json",
    "docs/audit/data/ledger/mi/minimal_axioms.json",
]
for n, sh in enumerate(shards, 1):
    gate(f"B8.{n}", os.path.isfile(os.path.join(ROOT, sh)),
         f"ledger shard exists: {os.path.basename(sh)}")

# ============================================================================
# B9 - note hygiene
# ============================================================================
FORBIDDEN = ["only route", "last route", "exhaust", "closes the route",
             "closes this route", "no other route", "final route", "retained",
             "unaudited", "effective_status", "audit grade", "PR #", "unlanded",
             "spec file", "required for the record", "decoher", "collapse",
             "Born rule", "protected subspace", "physically decoupled"]
present_forbidden = [s for s in FORBIDDEN if s in note_n]
gate("B9.1", present_forbidden == [],
     f"forbidden substrings absent from note ({present_forbidden or 'none'})")
gate("B9.2", re.search(r"[0-9]\.[0-9]", note_raw) is None,
     "no bare decimal digit-dot-digit anywhere in the note")

link_targets = set(re.findall(r"\]\(([^)]+)\)", note_raw))
expected_links = {
    CARR, KERN, KREAL, MECH, AX,
    "../scripts/kcpt_ambient_lattice_symmetry_kernel_isolation_2026_07_19.py",
    "../logs/runner-cache/kcpt_ambient_lattice_symmetry_kernel_isolation_2026_07_19.txt",
}
deps_exist = all(os.path.isfile(os.path.join(DOCS, d)) for d in (CARR, KERN, KREAL, MECH, AX))
gate("B9.3", link_targets == expected_links and deps_exist,
     "link inventory equals the five deps plus the two artifact paths; deps exist")

required = ["**Type:** bounded_theorem", "bounded theorem", "does NOT select",
            "Boundary", "K-real",
            "kcpt_ambient_lattice_symmetry_kernel_isolation_2026_07_19.py",
            "../logs/runner-cache/kcpt_ambient_lattice_symmetry_kernel_isolation_2026_07_19.txt"]
missing_req = [s for s in required if s not in note_raw]
gate("B9.4", missing_req == [],
     f"required strings present ({missing_req or 'all present'})")

PINNED = ["`conj(V8 c) = V8 conj(c)`", "`span{I, j}`", "`{a I + c (i j)}`",
          "`768 = 8 * 96`", "`(Z/2)^3`", "`J = V8 j V8^T / 64`", "`J^2 = -P_ker`",
          "`Phi(E) = 8 J`", "`12 = 2 + 2*0 + 10`"]
missing_pin = [s for s in PINNED if s not in note_raw]
gate("B9.5", missing_pin == [],
     f"pinned math strings present verbatim ({missing_pin or 'all present'})")

# ----------------------------------------------------------------------------
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
import sys
sys.exit(0 if FAIL == 0 else 1)
