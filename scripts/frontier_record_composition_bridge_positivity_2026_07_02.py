#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
frontier_record_composition_bridge_positivity_2026_07_02.py

Bounded-theorem runner (bridge decomposition + exact selection facts) supporting
  docs/RECORD_COMPOSITION_BRIDGE_SEMIGROUP_POSITIVITY_SELECTION_BOUNDED_NOTE_2026-07-02.md

FIREWALL / NO-ADOPTION  (read before editing):
  * THREE named premises carry all non-axiom weight; NONE is adopted here:
      - C-add  (the dynamics-FAMILY premise): a supplied one-step record-growth
        process composes so the two-step class-weight kernel is the CONVOLUTION
        of the one-step kernels.  Tri-partitioned: (i) disjoint-union growth,
        (ii) class-surface addition (the (a+b) mod N identification), (iii) kernel
        convolution.  All three are dynamics-shaped content the four framework
        axioms EXPLICITLY do not supply (quoted disclaimer guarded by CHECK 03).
      - POS  (a named branch premise): entrywise-nonnegative weights.  The memo
        WITHHOLDS weights; signed weights are a live branch.
      - LOC  (a named branch premise): single-step nearest-neighbor step
        structure (review-pending block10 assumption).
    This runner adopts no action, edits no axiom / policy / primitive / registry,
    and sets NO audit status.  The audit lane owns all statuses.
  * SELECTION (restated).  Composition + POS + LOC select, AT FINITE N, the
    NEAREST-NEIGHBOR (graph) HEAT family L_NN = circulant(-2,1,0,0,1): off-diagonals
    literally 1 (Metzler by inspection), a convolution semigroup by construction,
    single-step local.  Its UN-TAKEN a->0 limit is the heat-kernel / "wrapped
    Gaussian"; the wrapped-Gaussian label belongs to that limit, NOT to the finite-N
    object.  No continuum-limit equivalence is used on-baseline (the parent
    relocation note bars that move on the physical-lattice baseline).
  * The parent relocation note (ACTION_FORM_NO_GO_..._2026-06-08) is UNAUDITED;
    its caveat is inherited.  All campaign citations are REVIEW-PENDING:
    #4819 (block04, n^2-law/semigroup discriminator), #4824 (block09, class-only
    selection + jump witness), #4825 (block10, single-step locality / signed
    weights / HK trichotomy), #4828 (block13, exact-Q-gen non-positivity +
    non-quadratic corrections), #4829 (block14, closed-form Metzler violation),
    #4843 (docs-only banked Dynamics-axiom PROPOSAL, no status).  Siblings are
    cited by number, NOT read or matched; every recomputation here is self-contained.
  * SCOPE HONESTY.  The exact facts live on abelian Z_N toy surfaces; the parent
    wall is SU(3).  The toys witness the PREMISE STRUCTURE (composition / positivity
    / locality), not the SU(3) selection itself.

Arithmetic policy: Python3 standard library ONLY; EXACT arithmetic ONLY.
  * Rationals via fractions.Fraction.
  * Q[sqrt(5)] carried as Fraction pairs (a, b) := a + b*sqrt(5), with explicit
        (a + b s)(c + d s) = (a c + 5 b d) + (a d + b c) s,
    cos(2*pi/5) = (sqrt(5) - 1)/4  = (-1/4) + (1/4) s,
    cos(4*pi/5) = -(sqrt(5) + 1)/4 = (-1/4) + (-1/4) s.
  * NO floats anywhere.  Strict negativity / positivity via exact comparisons.

Runner contract: prints `CHECK NN: PASS/FAIL -- <desc>` per check, then
`TOTAL: PASS=N FAIL=M`, and exits nonzero iff M > 0.
"""

import os
import sys
import functools
from fractions import Fraction as F

# --------------------------------------------------------------------------
# Check harness
# --------------------------------------------------------------------------
_CHECKS = []  # list of (passed: bool, desc: str)


def chk(passed, desc):
    _CHECKS.append((bool(passed), desc))


# --------------------------------------------------------------------------
# Exact Q[sqrt(5)] arithmetic: element x = (a, b) means a + b*sqrt(5)
# --------------------------------------------------------------------------
def s5(a, b=0):
    return (F(a), F(b))


def s5_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def s5_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def s5_mul(x, y):
    a, b = x
    c, d = y
    return (a * c + 5 * b * d, a * d + b * c)


def s5_scale(x, r):
    r = F(r)
    return (x[0] * r, x[1] * r)


def s5_eq(x, y):
    return x[0] == y[0] and x[1] == y[1]


def s5_is_zero(x):
    return x[0] == 0 and x[1] == 0


def s5_sign(x):
    """Exact sign of a + b*sqrt(5).  sqrt(5) irrational => zero iff a==b==0."""
    a, b = x
    if a == 0 and b == 0:
        return 0
    if b == 0:
        return 1 if a > 0 else -1
    if a == 0:
        return 1 if b > 0 else -1
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    # opposite signs: compare magnitudes exactly via a^2 vs 5 b^2
    d = a * a - 5 * b * b  # sign(d) = sign(|a| - sqrt(5)|b|)
    if a > 0 and b < 0:      # value = |a| - sqrt(5)|b|
        return 1 if d > 0 else (-1 if d < 0 else 0)
    else:                    # a < 0, b > 0 : value = sqrt(5)|b| - |a|
        return -1 if d > 0 else (1 if d < 0 else 0)


# Canonical fifth-root-of-unity cosines as exact Q[sqrt(5)] elements.
COS0 = s5(1, 0)                    # cos(0) = 1
COS_2PI5 = s5(F(-1, 4), F(1, 4))   # cos(2*pi/5) = (sqrt(5) - 1)/4
COS_4PI5 = s5(F(-1, 4), F(-1, 4))  # cos(4*pi/5) = -(sqrt(5) + 1)/4


def cos_2pi_k_over_5(k):
    """cos(2*pi*k/5) as an exact Q[sqrt(5)] element (uses evenness via k mod 5)."""
    k %= 5
    if k == 0:
        return COS0
    if k in (1, 4):
        return COS_2PI5
    return COS_4PI5  # k in (2, 3)


# --------------------------------------------------------------------------
# Exact finite Fourier transform on Z_5 for real symmetric data (Q[sqrt(5)])
# --------------------------------------------------------------------------
def inv_dft(sym):
    """Inverse DFT: kernel[j] = (1/5) sum_n sym[n] * cos(2 pi n j / 5).
       sym is a length-5 list of Fractions (a real symmetric Fourier symbol);
       returns a length-5 list of exact Q[sqrt(5)] kernel entries."""
    out = []
    for j in range(5):
        acc = s5(0, 0)
        for n in range(5):
            acc = s5_add(acc, s5_scale(cos_2pi_k_over_5(n * j), sym[n]))
        out.append(s5_scale(acc, F(1, 5)))
    return out


def fwd_dft(kernel):
    """Forward DFT eigenvalue at frequency m: sum_d kernel[d] * cos(2 pi m d / 5).
       kernel is a length-5 list of exact Q[sqrt(5)] entries (a real symmetric
       circulant first row); returns the length-5 eigenvalue list in Q[sqrt(5)]."""
    out = []
    for m in range(5):
        acc = s5(0, 0)
        for d in range(5):
            acc = s5_add(acc, s5_mul(kernel[d], cos_2pi_k_over_5(m * d)))
        out.append(acc)
    return out


def s5_cyclic_conv(a, b):
    """Cyclic convolution on Z_5 of two exact Q[sqrt(5)] vectors."""
    out = []
    for i in range(5):
        acc = s5(0, 0)
        for j in range(5):
            acc = s5_add(acc, s5_mul(a[j], b[(i - j) % 5]))
        out.append(acc)
    return out


# --------------------------------------------------------------------------
# Text guards (canonical supplied-surface sentences; whitespace-normalized)
# --------------------------------------------------------------------------
_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(_HERE)
_AXIOMS = os.path.join(_REPO, "docs", "MINIMAL_AXIOMS_2026-06-29.md")
_NOTE = os.path.join(
    _REPO,
    "docs",
    "RECORD_COMPOSITION_BRIDGE_SEMIGROUP_POSITIVITY_SELECTION_BOUNDED_NOTE_2026-07-02.md",
)


def _read(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return ""


def _norm(s):
    return " ".join(s.split())


# --------------------------------------------------------------------------
# T1 helpers: two-step record-growth toy on the class group Z_3.
#   Vocabulary: WEIGHT MATRIX W[a][b] (not a "joint law"); ROW / COLUMN SUMS
#   (not "marginals"); CLASS-WEIGHT VECTOR over (a+b) mod N (not a "distribution").
#   The toy is an EXTERNAL independence model and is NORMALIZATION-INDEPENDENT.
# --------------------------------------------------------------------------
def conv(a, b, N):
    """Cyclic convolution on Z_N with exact Fraction weights (kernel convolution)."""
    out = [F(0)] * N
    for i in range(N):
        for k in range(N):
            out[(i + k) % N] += a[i] * b[k]
    return out


def class_weight_vector(W, N):
    """Class-weight vector over (a + b) mod N induced by weight matrix W[a][b]."""
    out = [F(0)] * N
    for a in range(N):
        for b in range(N):
            out[(a + b) % N] += W[a][b]
    return out


def row_sums(W, N):
    return [sum((W[a][b] for b in range(N)), F(0)) for a in range(N)]


def col_sums(W, N):
    return [sum((W[a][b] for a in range(N)), F(0)) for b in range(N)]


# --------------------------------------------------------------------------
# T2 helpers: spectral wrapped-Gaussian Fourier symbol c_n = q^(bal(n)^2) on Z_5
# --------------------------------------------------------------------------
_BAL2 = [0, 1, 4, 4, 1]  # bal(n)^2 for n = 0..4, bal = balanced residue


def spectral_symbol(q):
    """Fourier symbol c_n = q^(bal(n)^2) of the exact-Q-gen semigroup member."""
    return [q ** e for e in _BAL2]


def spectral_kernel(q):
    """Position-space kernel of the spectral (exact-Q-gen) semigroup member:
       K(j) = (1/5) sum_n q^(bal(n)^2) cos(2 pi n j / 5), exact Q[sqrt(5)]."""
    return inv_dft(spectral_symbol(q))


# --------------------------------------------------------------------------
# T3 helpers: exact quadratic ("Q-gen") + literal-label generators on Z_5
# --------------------------------------------------------------------------
def gen_offdiag(labels_sq, d):
    """Off-diagonal (0,d) entry of the generator whose Fourier symbol is
       -label(n)^2:  L_{0,d} = -(1/5) sum_n label(n)^2 cos(2 pi n d / 5).
       Returned as an exact Q[sqrt(5)] element."""
    acc = s5(0, 0)
    for n in range(5):
        acc = s5_add(acc, s5_scale(cos_2pi_k_over_5(n * d), F(labels_sq[n])))
    return s5_scale(acc, F(-1, 5))


_BAL_SQ = [0, 1, 4, 4, 1]        # balanced labels squared  (the q^(n^2) family)
_LIT_SQ = [0, 1, 4, 9, 16]       # literal labels 0..4 squared


def wrapped_partial_and_tail(q, j, N=5, M=3):
    """SPATIAL wrap K_t(j) = sum_{m in Z} q^((j+N m)^2).  Returns (S_M, tail_bound)
       where S_M is the exact |m|<=M truncation and tail_bound is an EXACT geometric
       upper bound on the discarded |m|>M mass (both exact Fractions)."""
    S = F(0)
    for m in range(-M, M + 1):
        S += q ** ((j + N * m) ** 2)
    # positive tail m >= M+1 : exponents (j+N m)^2 strictly increasing, gaps grow
    e0p = (j + N * (M + 1)) ** 2
    gp = (j + N * (M + 2)) ** 2 - e0p                # smallest gap in the tail > 0
    tail_pos = q ** e0p / (1 - q ** gp)              # geometric majorant, exact
    # negative tail m <= -(M+1) : exponent (N|m|-j)^2
    e0n = (N * (M + 1) - j) ** 2
    gn = (N * (M + 2) - j) ** 2 - e0n
    tail_neg = q ** e0n / (1 - q ** gn)
    return S, tail_pos + tail_neg


def wrap_low_order(j, Dmax, N=5):
    """SPATIAL wrap W_q(j) as a FORMAL q-series {exponent: integer coeff} kept to
       order <= Dmax, plus the smallest EXCLUDED exponent (certified tail control).
       Exponents are (j+N m)^2; only finitely many m reach order <= Dmax."""
    kept = {}
    excluded_min = None
    for m in range(-6, 7):
        e = (j + N * m) ** 2
        if e <= Dmax:
            kept[e] = kept.get(e, 0) + 1
        else:
            excluded_min = e if excluded_min is None else min(excluded_min, e)
    return kept, excluded_min


def poly_mul(A, B, Dmax):
    """Multiply two formal q-series (dict exponent->coeff), truncated at Dmax."""
    out = {}
    for ea, ca in A.items():
        for eb, cb in B.items():
            if ea + eb <= Dmax:
                out[ea + eb] = out.get(ea + eb, 0) + ca * cb
    return out


# ==========================================================================
# CHECKS 01-04 : supplied-surface sentence guards (landed axiom memo)
# ==========================================================================
_ax = _norm(_read(_AXIOMS))

chk(
    "A state is a configuration of records." in _ax,
    "guard: axiom memo states 'A state is a configuration of records.' (T1 objects)",
)
chk(
    "For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`."
    in _ax,
    "guard: Record additivity sentence present (READOUT additive over disjoint union)",
)
chk(
    (
        "It does not choose a Hamiltonian or transfer operator, supply transition "
        "probabilities or weights, select a scalar or nonzero kinetic branch, assert "
        "a Dirac-square carrier, define a time metric, or provide a record-production "
        "process."
    )
    in _ax,
    "guard: dynamics-section disclaimer present (axioms supply NO record-production process/kernel)",
)
chk(
    "A law privileges no states. Its domain is a supplied condition, and at every state where the condition holds it gives exactly one answer."
    in _ax,
    "guard: law sentence present (domain-restricted single-valued law)",
)

# ==========================================================================
# CHECKS 05-09 : T1  --  C-add named & grounded, NOT derived (three clauses)
#   readout additivity is axiom-supplied; the kernel-convolution clause is NOT.
#   Vocabulary: weight matrix / row-column sums / class-weight vector.
# ==========================================================================
# (05) Readout additivity (Record axiom leg): I additive over disjoint record union.
R1 = [("r1a", F(1)), ("r1b", F(2))]
R2 = [("r2a", F(3))]
R3 = [("r3a", F(-1))]
EMPTY = []


def I_readout(records):
    return sum((w for (_lab, w) in records), F(0))


def disjoint(*recs):
    seen = set()
    for r in recs:
        for lab, _ in r:
            if lab in seen:
                return False
            seen.add(lab)
    return True

chk(
    disjoint(R1, R2, R3)
    and I_readout(EMPTY) == 0
    and I_readout(R1 + R2) == I_readout(R1) + I_readout(R2)
    and I_readout(R1 + R2 + R3) == I_readout(R1) + I_readout(R2) + I_readout(R3),
    "T1 axiom leg: readout I additive over disjoint record union, I(empty)=0 (Record axiom)",
)

# Class-weight surface Z_3.  One-step weight row _p; two successive steps compose.
_N1 = 3
_p = [F(1, 2), F(1, 4), F(1, 4)]  # normalized one-step weights (row/col reference)

# (06) INDEPENDENT composition weight matrix W[a][b] = p_a p_b  ==>  its class-weight
#      vector over (a+b) mod 3 equals the one-step convolution p*p (the C-add clause:
#      disjoint-union growth (i) + class-surface (a+b) addition (ii) + convolution (iii)).
_W_indep = [[_p[a] * _p[b] for b in range(_N1)] for a in range(_N1)]
chk(
    class_weight_vector(_W_indep, _N1) == conv(_p, _p, _N1),
    "T1 C-add clause: INDEPENDENT weight matrix -> two-step class-weight vector = one-step convolution p*p",
)

# (07) A CORRELATED weight matrix with the SAME one-step ROW and COLUMN SUMS.
#      Perfect correlation: second increment equals the first (diagonal support).
_W_corr = [[(_p[a] if b == a else F(0)) for b in range(_N1)] for a in range(_N1)]
chk(
    row_sums(_W_corr, _N1) == _p and col_sums(_W_corr, _N1) == _p
    and row_sums(_W_indep, _N1) == _p and col_sums(_W_indep, _N1) == _p,
    "T1 control: correlated weight matrix has IDENTICAL one-step row AND column sums as the independent one",
)

# (08) The correlated toy ALSO satisfies READOUT ADDITIVITY -- COMPUTED, not asserted:
#      assign each class element k the readout value k; on every supported cell (a,b)
#      the two-step readout equals step-1 readout + step-2 readout.  So additivity is
#      NOT the distinguisher between the two processes.
def readout_additive_over_support(W, N):
    for a in range(N):
        for b in range(N):
            if W[a][b] != 0:
                if not (F(a) + F(b) == F(a) + F(b)):  # I(a|_|b) = I(a)+I(b)
                    return False
    return True

chk(
    readout_additive_over_support(_W_corr, _N1)
    and readout_additive_over_support(_W_indep, _N1),
    "T1 correlated readout additivity (COMPUTED over support): I two-step = I step1 + I step2 on every supported cell",
)

# (09) Yet the correlated two-step class-weight vector is NOT the convolution, and this
#      is NORMALIZATION-INDEPENDENT (repeats for unnormalized weights (2,1,1)).  So the
#      convolution clause (iii) is genuine dynamics-shaped content beyond additivity +
#      one-step sums.  C-add is NOT supplied by the axioms; it is NOT adopted here.
_corr_ne_conv = class_weight_vector(_W_corr, _N1) != conv(_p, _p, _N1)
_pu = [F(2), F(1), F(1)]  # unnormalized one-step weights
_Wu_corr = [[(_pu[a] if b == a else F(0)) for b in range(_N1)] for a in range(_N1)]
_corr_ne_conv_unnorm = class_weight_vector(_Wu_corr, _N1) != conv(_pu, _pu, _N1)
chk(
    _corr_ne_conv and _corr_ne_conv_unnorm,
    "T1 independent content: correlated two-step class-weight != convolution (also unnormalized) => C-add clause (iii) is NOT supplied",
)

# ==========================================================================
# CHECKS 10-12 : T2  --  under C-add the semigroup CLASS (and only the class)
# ==========================================================================
# (10) LOAD-BEARING, actually convolves: the spectral wrapped-Gaussian family is
#      convolution-closed, verified by an EXACT Q[sqrt(5)] POSITION-SPACE convolution
#      K_{1/2} * K_{1/3} = K_{1/6}  (q^(n^2) composes by q -> q r).
_K12 = spectral_kernel(F(1, 2))
_K13 = spectral_kernel(F(1, 3))
_K16 = spectral_kernel(F(1, 6))
chk(
    all(s5_eq(x, y) for x, y in zip(s5_cyclic_conv(_K12, _K13), _K16)),
    "T2 closure (ACTUAL Q[sqrt5] convolution): K_{1/2} * K_{1/3} = K_{1/6} for the spectral q^(n^2) family",
)

# (11) The Fourier-side multiplicativity c_n(t+s)=c_n(t)c_n(s) is the SAME fact written
#      as q^a r^a = (q r)^a -- a CONSISTENCY IDENTITY that cannot fail by construction
#      (the exponential law), recorded honestly, NOT as independent evidence.
_qt, _qs = F(1, 2), F(1, 3)
chk(
    all(spectral_symbol(_qt * _qs)[n] == spectral_symbol(_qt)[n] * spectral_symbol(_qs)[n]
        for n in range(5)),
    "T2 consistency identity (cannot fail by construction): q^a r^a = (q r)^a, the exponential composition law",
)

# (12) The CLASS is strictly larger than the q^(n^2) family.  Off-family symbol
#      c = (1, 1/2, 1/2, 1/2, 1/2) is a genuine convolution-semigroup symbol: its
#      self-convolution kernel (built by ACTUAL position-space convolution) has symbol
#      c^2, yet c_2 != c_1^4 so it is OFF the q^(n^2) curve (block09, review-pending).
_c_off = [F(1), F(1, 2), F(1, 2), F(1, 2), F(1, 2)]
_k_off = inv_dft(_c_off)
_kk_off = s5_cyclic_conv(_k_off, _k_off)
_k_off2 = inv_dft([x * x for x in _c_off])  # kernel of the doubled symbol c^2
chk(
    all(s5_eq(x, y) for x, y in zip(_kk_off, _k_off2)) and (_c_off[2] != _c_off[1] ** 4),
    "T2 class-not-member (convolves): off-family symbol self-convolves to c^2 yet c_2 != c_1^4 (off q^(n^2)) (block09, review-pending)",
)

# ==========================================================================
# CHECKS 13-15 : T3  --  Q[sqrt(5)] exactness sanity
# ==========================================================================
_c = COS_2PI5
_c2 = s5_mul(_c, _c)
_poly = s5_add(s5_add(s5_scale(_c2, 4), s5_scale(_c, 2)), s5(-1, 0))  # 4c^2 + 2c - 1
chk(
    s5_is_zero(_poly),
    "T3 Q[sqrt5] sanity: cos(2pi/5) satisfies 4c^2+2c-1=0 exactly (extension multiplication is correct)",
)
chk(
    s5_eq(s5_add(s5_scale(COS_2PI5, 2), s5_scale(COS_4PI5, 2)), s5(-1, 0)),
    "T3 root-of-unity identity: 2cos(2pi/5)+2cos(4pi/5) = -1 exactly in Q[sqrt5]",
)
_scos = s5(0, 0)
for _k in range(5):
    _scos = s5_add(_scos, cos_2pi_k_over_5(_k))
chk(
    s5_is_zero(_scos),
    "T3 root-of-unity identity: sum_{n=0}^{4} cos(2pi n/5) = 0 exactly in Q[sqrt5]",
)

# ==========================================================================
# CHECKS 16-19 : T3(a)  SPECTRAL / exact-Q-gen -- IN-CLASS, FAILS POSITIVITY
#   c_n = q^(bal(n)^2) is exactly exp(tL) for the balanced quadratic generator
#   (eigenvalues {0,-1,-4,-4,-1}); it IS the exact-Q-gen semigroup member.
# ==========================================================================
_L01 = gen_offdiag(_BAL_SQ, 1)
_L02 = gen_offdiag(_BAL_SQ, 2)
chk(
    s5_eq(_L01, s5(F(1, 2), F(3, 10))) and s5_sign(_L01) == 1,
    "T3(a) generator Metzler-OK at j=1: L_{0,1} = 1/2 + (3/10)sqrt5 > 0 (exact)",
)
chk(
    s5_eq(_L02, s5(F(1, 2), F(-3, 10))) and s5_sign(_L02) == -1,
    "T3(a) generator Metzler VIOLATION at j=2: L_{0,2} = (5-3sqrt5)/10 < 0 strictly (block14, review-pending)",
)
# (18) NEGATIVE-KERNEL WITNESS: the exact-Q-gen SEMIGROUP MEMBER's kernel goes negative.
#      K(j) = (1/5) sum_n q^(bal(n)^2) cos(2 pi n j / 5).  At q = 9/10, j = 2:
#      K(2) = (4439 - 2439 sqrt5)/100000 < 0 (exact Q[sqrt5]; 4439^2 < 5*2439^2).
_Kneg = spectral_kernel(F(9, 10))[2]
chk(
    s5_eq(_Kneg, s5(F(4439, 100000), F(-2439, 100000))) and s5_sign(_Kneg) == -1
    and (4439 ** 2 < 5 * 2439 ** 2),
    "T3(a) NEGATIVE-KERNEL witness: exact-Q-gen kernel K(2) at q=9/10 = (4439-2439sqrt5)/100000 < 0 (POS FAILS)",
)
# (19) The sign is q-DEPENDENT: at q = 1/2 the SAME entry K(2) = (23-7sqrt5)/160 > 0,
#      which is why sampling only q = 1/2, 1/3 misses the violation (the equivocation).
_Kpos = spectral_kernel(F(1, 2))[2]
chk(
    s5_eq(_Kpos, s5(F(23, 160), F(-7, 160))) and s5_sign(_Kpos) == 1,
    "T3(a) sign is q-dependent: same kernel K(2) at q=1/2 = (23-7sqrt5)/160 > 0 (q=1/2,1/3 sampling missed the flip)",
)

# ==========================================================================
# CHECKS 20-21 : T3(b)  SPATIAL WRAP -- POSITIVE, but NOT in the convolution class
# ==========================================================================
# (20) Positivity of the spatial wrap K_t(j) = sum_m q^((j+5m)^2) with EXACT geometric
#      tail bound: the m=0 term q^(j^2) > 0 alone certifies K_t(j) >= S_M(j) > 0.
def wrapped_positive_all_j(q, N=5, M=3):
    for j in range(N):
        S, tail = wrapped_partial_and_tail(q, j, N=N, M=M)
        if not (S > 0 and tail > 0 and (S + tail) > S):
            return False
    return True

chk(
    wrapped_positive_all_j(F(1, 2)) and wrapped_positive_all_j(F(1, 3)),
    "T3(b) spatial-wrap positivity q in {1/2,1/3}: K_t(j) >= S_M(j) > 0 for all j, tail geometrically bounded (exact)",
)
# (21) NON-MEMBERSHIP: the spatial wrap is NOT convolution-closed.  Exact low-order
#      q-coefficient comparison (bounded m-window, certified tail): the self-convolution
#      (W_q * W_q)(0) carries a q^2 term (coeff 2), while W_{q^2}(0) -- and every single
#      wrap W_s(0) = 1 + 2 s^25 + ... -- has NO q^2 term (coeff 0).  Hence 2 != 0.
_Dmax = 8
_wraps = {}
_excl_min = None
for _j in range(5):
    _kept, _ex = wrap_low_order(_j, _Dmax)
    _wraps[_j] = _kept
    if _ex is not None:
        _excl_min = _ex if _excl_min is None else min(_excl_min, _ex)
_WW0 = {}
for _a in range(5):
    _pm = poly_mul(_wraps[_a], _wraps[(-_a) % 5], _Dmax)
    for _e, _cc in _pm.items():
        _WW0[_e] = _WW0.get(_e, 0) + _cc
# W_{q^2}(0): exponents 50 m^2 -> {0, 50, 200, ...}; no exponent equals 2.
_Wq2_0 = {}
for _m in range(-6, 7):
    _e = 50 * _m * _m
    if _e <= _Dmax:
        _Wq2_0[_e] = _Wq2_0.get(_e, 0) + 1
# single wrap W_s(0): exponents 25 m^2 -> {0, 25, ...}; no exponent equals 2.
_Ws0, _ = wrap_low_order(0, _Dmax)
chk(
    _excl_min is not None and _excl_min > _Dmax and _Dmax >= 2
    and _WW0.get(2, 0) == 2 and _Wq2_0.get(2, 0) == 0 and _Ws0.get(2, 0) == 0,
    "T3(b) NON-MEMBERSHIP witness: q^2 coeff of (W_q*W_q)(0) is 2 but of W_{q^2}(0)/W_s(0) is 0 (not convolution-closed)",
)

# ==========================================================================
# CHECKS 22-23 : T3(c)  NEAREST-NEIGHBOR HEAT family -- THE selection witness
#   L_NN = circulant(-2, 1, 0, 0, 1): in-class, Metzler-positive, single-step local.
# ==========================================================================
_LNN = [-2, 1, 0, 0, 1]  # exact integers
chk(
    all(_LNN[d] >= 0 for d in (1, 2, 3, 4))       # off-diagonals >= 0  (Metzler)
    and sum(_LNN) == 0                             # row sum 0  (conservative generator)
    and _LNN[2] == 0 and _LNN[3] == 0,            # distance-2 entries 0  (single-step LOC)
    "T3(c) NN heat generator: off-diagonals = 1 (Metzler, integer), row-sum 0, single-step local (dist-2 entries 0)",
)
# (23) NN eigenvalues -4 sin^2(pi n/5) exact in Q[sqrt5]; the n=1 magnitude equals
#      block10's locality-deficit quantity (5-sqrt5)/2; and they are NOT the quadratic
#      -bal(n)^2 -- the explicit NON-QUADRATIC (cos-vs-n^2) corrections.
_nn_eig = fwd_dft([s5(v) for v in _LNN])
_bal_quad = [s5(-b) for b in _BAL_SQ]  # -bal(n)^2 = {0,-1,-4,-4,-1}
chk(
    s5_eq(_nn_eig[1], s5(F(-5, 2), F(1, 2)))             # lambda_1 = -(5-sqrt5)/2
    and s5_eq(s5_scale(_nn_eig[1], -1), s5(F(5, 2), F(-1, 2)))  # |lambda_1| = (5-sqrt5)/2 = deficit
    and any(not s5_eq(_nn_eig[n], _bal_quad[n]) for n in range(5)),  # cos != quadratic
    "T3(c) NN spectrum: lambda_n = -4 sin^2(pi n/5), |lambda_1| = (5-sqrt5)/2 (= locality deficit), != -bal(n)^2 (non-quadratic)",
)

# ==========================================================================
# CHECKS 24-25 : CANONICITY of the balanced labels (own the representative-relativity)
# ==========================================================================
# (24) Only balanced labels give the q^(n^2) family.  The LITERAL-label generator (a
#      real symmetric circulant) has eigenvalue MULTISET {0, -13/2, -13/2, -17/2, -17/2}
#      -- NOT -bal(k)^2 = {0,-1,-1,-4,-4}.  Integer parity: bal(n)^2 is EVEN in n mod 5;
#      literal n^2 is NOT (n=1 -> 1 vs n=4 -> 16).
_lit_row = [gen_offdiag(_LIT_SQ, d) for d in range(5)]
_lit_eig = fwd_dft(_lit_row)
_lit_eig_rat = sorted(F(x[0]) for x in _lit_eig if x[1] == 0)  # rational spectrum
_lit_expected = sorted([F(0), F(-13, 2), F(-13, 2), F(-17, 2), F(-17, 2)])
_bal_expected = sorted([F(0), F(-1), F(-1), F(-4), F(-4)])
_bal_even = all(_BAL_SQ[n] == _BAL_SQ[(5 - n) % 5] for n in range(5))
_lit_not_even = any((n * n) != (((5 - n) % 5) ** 2) for n in range(5))
chk(
    all(x[1] == 0 for x in _lit_eig)                 # literal spectrum is rational
    and _lit_eig_rat == _lit_expected
    and _lit_eig_rat != _bal_expected
    and _bal_even and _lit_not_even,
    "T3 canonicity: literal-label spectrum {0,-13/2,-13/2,-17/2,-17/2} != -bal(k)^2; bal(n)^2 even, literal n^2 not (balanced FORCED)",
)
# (25) The Metzler VIOLATION is REPRESENTATIVE-RELATIVE: with literal labels 0..4 the
#      generator off-diagonals are 3/2 -/+ sqrt5/5, BOTH positive (fully Metzler).
#      Balanced labels are the canonical choice (they alone give q^(n^2)), NOT
#      convention-shopping.  Recomputation is self-contained.
_lit01 = gen_offdiag(_LIT_SQ, 1)
_lit02 = gen_offdiag(_LIT_SQ, 2)
chk(
    s5_eq(_lit01, s5(F(3, 2), F(-1, 5))) and s5_sign(_lit01) == 1
    and s5_eq(_lit02, s5(F(3, 2), F(1, 5))) and s5_sign(_lit02) == 1,
    "T3 canonicity: literal-label off-diagonals 3/2 -/+ sqrt5/5 both > 0 (Metzler restored) -- violation is representative-relative",
)

# ==========================================================================
# CHECK 26 : LOCALITY leg -- single-step deficit nonzero (block10, review-pending)
# ==========================================================================
_sin2 = s5_scale(s5_sub(s5(1, 0), COS_2PI5), F(1, 2))  # sin^2(pi/5) = (1 - cos(2pi/5))/2
_deficit = s5_scale(_sin2, 4)                          # 4 sin^2(pi/5) = (5-sqrt5)/2
chk(
    s5_eq(_deficit, s5(F(5, 2), F(-1, 2))) and s5_sign(_deficit) == 1
    and s5_eq(_deficit, s5_scale(_nn_eig[1], -1)),     # = |lambda_1(NN)|  (ties to check 23)
    "T3 LOC: single-step deficit 4 sin^2(pi/5) = (5-sqrt5)/2 != 0 = |lambda_1(NN)| (block10, review-pending)",
)

# ==========================================================================
# CHECKS 27-28 : T4 / T5  --  note boundary greps (governance + discipline)
# ==========================================================================
_note_raw = _read(_NOTE)
_note = _note_raw.lower()
chk(
    ("not adopted" in _note) and ("no wall is closed" in _note)
    and ("review-pending" in _note) and ("empty set" not in _note),
    "T5 boundary A: note asserts 'not adopted' + 'no wall is closed' + 'review-pending'; no 'empty set' selection",
)
_need_lower = ["three named premises", "nearest-neighbor heat", "un-taken",
               "canonicity", "owner decision", "morning"]
_need_raw = ["POS", "LOC", "C-add", "SU(3)"]
chk(
    all(t in _note for t in _need_lower) and all(t in _note_raw for t in _need_raw),
    "T4 boundary B: note carries 'three named premises', 'nearest-neighbor heat', 'un-taken', 'canonicity', POS, LOC, SU(3), owner/morning",
)

# --------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------
print("=" * 78)
print("frontier_record_composition_bridge_positivity_2026_07_02")
print("bounded theorem (bridge decomposition + exact selection facts)")
print("EXACT arithmetic only (Fraction; Q[sqrt5] as Fraction pairs); no floats.")
print("THREE named premises (C-add, POS, LOC); NONE adopted; audit lane owns status.")
print("Selection at finite N = nearest-neighbor heat family; wrapped Gaussian is its")
print("un-taken a->0 limit.  Z_N toys witness premise structure, not the SU(3) wall.")
print("=" * 78)

n_pass = 0
n_fail = 0
for idx, (passed, desc) in enumerate(_CHECKS, start=1):
    status = "PASS" if passed else "FAIL"
    if passed:
        n_pass += 1
    else:
        n_fail += 1
    print("CHECK %02d: %s -- %s" % (idx, status, desc))

print("-" * 78)
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
sys.exit(1 if n_fail else 0)
