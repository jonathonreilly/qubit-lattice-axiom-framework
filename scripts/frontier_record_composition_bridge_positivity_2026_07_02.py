#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
frontier_record_composition_bridge_positivity_2026_07_02.py

Bounded-theorem runner (bridge decomposition + exact selection facts) supporting
  docs/RECORD_COMPOSITION_BRIDGE_SEMIGROUP_POSITIVITY_SELECTION_BOUNDED_NOTE_2026-07-02.md

FIREWALL / NO-ADOPTION  (read before editing):
  * C-add (record-composition -> two-step-kernel-is-the-convolution) is NAMED,
    GROUNDED, and NOT derived or adopted here.  It is dynamics-shaped content the
    four framework axioms EXPLICITLY do not supply (the quoted dynamics-section
    disclaimer is guarded by CHECK 03).  This runner adopts no action, edits no
    axiom / policy / primitive / registry, and sets NO audit status.  The audit
    lane owns all statuses.
  * The parent relocation note (ACTION_FORM_NO_GO_..._2026-06-08) is UNAUDITED;
    its caveat is inherited.  All campaign citations are REVIEW-PENDING:
    #4819 (block04, n^2-law/semigroup discriminator), #4824 (block09, class-only
    selection + jump witness), #4825 (block10, single-step locality / signed
    weights / HK trichotomy), #4828 (block13, exact-Q-gen non-positivity +
    certified wrapped-Gaussian corrections), #4829 (block14, closed-form Metzler
    violation), #4843 (docs-only banked Dynamics-axiom PROPOSAL, no status).
  * The T3 selection is FAMILY-LEVEL among the NAMED candidates
    {Wilson, HK/wrapped-Gaussian, Manton, exact-Q-gen}; a hostile UNNAMED positive
    semigroup member is NOT generically excluded.

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
# T1 helpers: two-step record-growth toy on the class group Z_3
# --------------------------------------------------------------------------
def conv(a, b, N):
    """Cyclic convolution on Z_N with exact Fraction weights."""
    out = [F(0)] * N
    for i in range(N):
        for k in range(N):
            out[(i + k) % N] += a[i] * b[k]
    return out


def class_sum_dist(joint, N):
    """Distribution of (a + b) mod N induced by a joint law joint[a][b]."""
    out = [F(0)] * N
    for a in range(N):
        for b in range(N):
            out[(a + b) % N] += joint[a][b]
    return out


def marg_first(joint, N):
    return [sum((joint[a][b] for b in range(N)), F(0)) for a in range(N)]


def marg_second(joint, N):
    return [sum((joint[a][b] for a in range(N)), F(0)) for b in range(N)]


# --------------------------------------------------------------------------
# T2 helpers: wrapped-Gaussian Fourier coefficients c_n = q^(n^2) on Z_5
# --------------------------------------------------------------------------
def cn_wrapped(q, n):
    """c_n = q^(bal(n)^2), n in 0..4, bal = balanced residue (symmetric kernel)."""
    b = n if n <= 2 else n - 5
    return q ** (b * b)


# --------------------------------------------------------------------------
# T3 helpers: exact quadratic ("Q-gen") generator on Z_5 and wrapped positivity
# --------------------------------------------------------------------------
_BAL5 = [-2, -1, 0, 1, 2]  # balanced residue / frequency labels for Z_5


def Lgen(d):
    """Off-diagonal (0,d) entry of the exact quadratic generator on Z_5:
       L_{0,d} = -(1/5) * sum_{n in balanced residues} n^2 * cos(2*pi*n*d/5),
       returned as an exact Q[sqrt(5)] element."""
    acc = s5(0, 0)
    for n in _BAL5:
        acc = s5_add(acc, s5_scale(cos_2pi_k_over_5(n * d), F(n * n)))
    return s5_scale(acc, F(-1, 5))


def wrapped_partial_and_tail(q, j, N=5, M=3):
    """K_t(j) = sum_{m in Z} q^((j+N m)^2).  Returns (S_M, tail_bound) where
       S_M is the exact |m|<=M truncation and tail_bound is an EXACT geometric
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
# CHECKS 05-08 : T1  --  C-add named & grounded, NOT derived
#   readout additivity is axiom-supplied; the kernel-convolution clause is NOT.
# ==========================================================================
# Readout additivity (Record axiom leg): I additive over disjoint record union.
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

# Class-weight kernels on Z_3.  One-step kernel p; two successive steps compose.
_N1 = 3
_p = [F(1, 2), F(1, 4), F(1, 4)]

# (a) Independent composition  ==>  two-step kernel = convolution (the C-add clause).
_joint_indep = [[_p[a] * _p[b] for b in range(_N1)] for a in range(_N1)]
_K_indep = class_sum_dist(_joint_indep, _N1)
chk(
    _K_indep == conv(_p, _p, _N1),
    "T1 C-add clause: under INDEPENDENT composition the two-step kernel = one-step convolution",
)

# (b) A correlated process with the SAME one-step marginals and the SAME readout
#     additivity.  Perfect correlation: second increment equals the first.
_joint_corr = [[(_p[a] if b == a else F(0)) for b in range(_N1)] for a in range(_N1)]
chk(
    marg_first(_joint_corr, _N1) == _p and marg_second(_joint_corr, _N1) == _p,
    "T1 control: correlated process has IDENTICAL one-step marginals (both steps) as the independent one",
)

# (c) Its two-step kernel is NOT the convolution => C-add's kernel clause has
#     content beyond readout additivity + marginals: it is dynamics-shaped, NOT adopted.
_K_corr = class_sum_dist(_joint_corr, _N1)
chk(
    _K_corr != conv(_p, _p, _N1),
    "T1 independent content: readout-additive, same-marginal correlated process has two-step kernel != convolution (C-add is NOT supplied)",
)

# ==========================================================================
# CHECKS 09-12 : T2  --  under C-add the semigroup CLASS (and only the class)
# ==========================================================================
# Convolution semigroup <=> Fourier-coefficient multiplicativity c_n(t+s)=c_n(t)c_n(s).
_qt, _qs = F(1, 2), F(1, 3)
_qts = _qt * _qs  # q_{t+s} = q_t q_s
chk(
    all(cn_wrapped(_qts, n) == cn_wrapped(_qt, n) * cn_wrapped(_qs, n) for n in range(5)),
    "T2 multiplicativity: c_n(t+s)=c_n(t)c_n(s) EXACT for c_n=q^(n^2), all n in Z_5",
)
chk(
    all(cn_wrapped(_qt * _qt, n) == cn_wrapped(_qt, n) ** 2 for n in range(5)),
    "T2 doubling: c_n(2t)=c_n(t)^2 EXACT (q -> q^2) for the wrapped-Gaussian family",
)
chk(
    all(cn_wrapped(_qt, n) * cn_wrapped(_qs, n) == cn_wrapped(_qt * _qs, n) for n in range(5)),
    "T2 closure: convolution of two wrapped Gaussians stays in family, q^(n^2)*r^(n^2)=(qr)^(n^2)",
)
# Failure witness (block09, review-pending): a rational coefficient vector that is
# composable in the CLASS but violates the n^2-law -> not a wrapped-Gaussian MEMBER.
_w = [F(1), F(1, 2), F(1, 2), F(1, 2), F(1, 2)]  # symmetric, w_2 != w_1^4
_genuine = cn_wrapped(F(1, 2), 2) == cn_wrapped(F(1, 2), 1) ** 4  # true member obeys law
chk(
    (_w[2] != _w[1] ** 4) and _genuine,
    "T2 class-not-member: witness violates n^2-law (w_2 != w_1^4) while a genuine member obeys it (block09, review-pending)",
)

# ==========================================================================
# CHECKS 13-20 : T3  --  positivity + locality select the wrapped Gaussian
#                        among all NAMED candidates (family-level)
# ==========================================================================
# --- Q[sqrt(5)] exactness sanity ---
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

# --- (i) exact quadratic generator on Z_5 is NOT Metzler (block14/block13, review-pending) ---
_L01 = Lgen(1)
_L02 = Lgen(2)
chk(
    s5_eq(_L01, s5(F(1, 2), F(3, 10))) and s5_sign(_L01) == 1,
    "T3(i) Metzler-OK at j=1: L_{0,1} = 1/2 + (3/10)sqrt5 > 0 (exact)",
)
chk(
    s5_eq(_L02, s5(F(1, 2), F(-3, 10))) and s5_sign(_L02) == -1,
    "T3(i) Metzler VIOLATION at j=2: L_{0,2} = (5-3sqrt5)/10 < 0 strictly => exp(tL) not positivity-preserving (block14, review-pending)",
)

# --- (ii) wrapped-Gaussian positivity with EXACT geometric tail bound (block13) ---
def wrapped_positive_all_j(q, N=5, M=3):
    ok = True
    for j in range(N):
        S, tail = wrapped_partial_and_tail(q, j, N=N, M=M)
        # K_t(j) = S + (true tail in (0, tail]); S contains the m=0 term q^(j^2) > 0.
        if not (S > 0 and tail > 0 and (S + tail) > S):
            ok = False
    return ok

chk(
    wrapped_positive_all_j(F(1, 2)),
    "T3(ii) wrapped positivity q=1/2: K_t(j) >= S_M(j) > 0 for all j in Z_5, tail geometrically bounded (exact)",
)
chk(
    wrapped_positive_all_j(F(1, 3)),
    "T3(ii) wrapped positivity q=1/3: K_t(j) >= S_M(j) > 0 for all j in Z_5, tail geometrically bounded (exact)",
)

# --- locality leg: single-step locality deficit 4 sin^2(pi/5) nonzero (block10) ---
_sin2 = s5_scale(s5_sub(s5(1, 0), COS_2PI5), F(1, 2))  # sin^2(pi/5) = (1 - cos(2pi/5))/2
_deficit = s5_scale(_sin2, 4)                          # 4 sin^2(pi/5) = 4*(5-sqrt5)/8
chk(
    s5_eq(_deficit, s5(F(5, 2), F(-1, 2))) and s5_sign(_deficit) == 1,
    "T3 locality: single-step deficit 4 sin^2(pi/5) = (5-sqrt5)/2 != 0 => single-step locality excludes exact Q-gen (block10, review-pending)",
)

# ==========================================================================
# CHECKS 21-23 : T4/T5  --  governance hand-off + end-state boundary (note greps)
# ==========================================================================
_note = _read(_NOTE).lower()
chk(
    ("not adopted" in _note) and ("no wall is closed" in _note),
    "T5 boundary: note asserts C-add 'not adopted' and 'no wall is closed'",
)
chk(
    "review-pending" in _note,
    "T5 boundary: note flags all campaign citations 'review-pending'",
)
chk(
    ("owner decision" in _note) and ("morning" in _note),
    "T4 governance: note routes the residual as an 'owner decision' on the 'morning' list",
)

# --------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------
print("=" * 78)
print("frontier_record_composition_bridge_positivity_2026_07_02")
print("bounded theorem (bridge decomposition + exact selection facts)")
print("EXACT arithmetic only (Fraction; Q[sqrt5] as Fraction pairs); no floats.")
print("NO action adopted; C-add named/grounded NOT derived; audit lane owns status.")
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
