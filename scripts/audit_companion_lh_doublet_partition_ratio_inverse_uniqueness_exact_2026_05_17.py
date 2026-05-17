#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`LH_DOUBLET_PARTITION_RATIO_INVERSE_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-17`.

The narrow theorem's load-bearing content is the *inverse* direction of
the LH-doublet traceless abelian eigenvalue algebra:

  (R1) For positive integers (m, n) and real alpha != 0, the unique beta
       solving m * alpha + n * beta = 0 gives beta / alpha = -m / n.
  (R2) Setting beta / alpha = -k for fixed positive integer k forces
       m = k * n. With trace-surface state count m + n = N,
         n = N / (k + 1),
         m = k * N / (k + 1).
  (R3) (m, n) lies in P(N) (positive integers summing to N) iff
         (k + 1) | N    and    N >= k + 1.
  (R4) When (R3) holds, the pair (m, n) is unique within P(N) with
       ratio -k.

The runner verifies (R1)-(R4) at exact sympy precision over abstract
positive integers (parametric), then specializes to the framework
instance (N, k) = (8, 3) and a sweep of (N, k) pairs including
both admissible and non-admissible cases.

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence that the narrow note's
load-bearing class-A algebra holds at exact symbolic precision.
"""

from fractions import Fraction
from pathlib import Path
import sys

try:
    import sympy
    from sympy import Rational, Symbol, simplify, symbols, expand, gcd, sympify
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT
    / "docs"
    / "LH_DOUBLET_PARTITION_RATIO_INVERSE_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-17.md"
)


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    print(f"  [{tag}] {label}  ({detail})")


def section(title: str) -> None:
    print("\n" + "-" * 88 + f"\n{title}\n" + "-" * 88)


# ============================================================================
section("Part 1: note structure and scope discipline")
# ============================================================================
note_text = NOTE_PATH.read_text()

required = [
    "LH-Doublet Trace-Surface Partition / Ratio Inverse Uniqueness",
    "Type:** bounded_theorem",
    "n  =  N / (k + 1)",
    "m  =  k * N / (k + 1)",
    "(k + 1) divides N",
    "(N, k) = (8, 3)",
    "(m, n) = (6, 2)",
    "Does **not** derive `N = 8`",
    "Does **not** derive `k = 3`",
    "Does **not** identify the partition `(6, 2)`",
    "Does **not** consume any PDG observed quark charges",
]
for s in required:
    check(f"contains: {s!r}", s in note_text)

# Scope discipline: no SM identification, no admitted convention
# load-bearing.
forbidden_in_scope = [
    "Q = T_3 + Y/2 then matches",
    "identifies the structural 3+1 abelian eigenspaces with the Standard Model",
]
for f in forbidden_in_scope:
    check(
        f"narrow scope avoids forbidden load-bearing claim: {f!r}",
        f not in note_text,
        detail="SM identification out of scope",
    )

# ============================================================================
section("Part 2: (R1) parametric ratio identity beta/alpha = -m/n")
# ============================================================================
# Symbolic check: for positive integer m, n and real alpha != 0, the
# unique beta solving m * alpha + n * beta = 0 gives beta / alpha = -m/n.
m_sym, n_sym, alpha_sym = symbols("m n alpha", positive=True, integer=False)
beta_sym = symbols("beta", real=True)

trace_eq = m_sym * alpha_sym + n_sym * beta_sym
# Solve for beta:
beta_solution = sympy.solve(trace_eq, beta_sym)[0]
ratio_symbolic = simplify(beta_solution / alpha_sym)
expected_ratio = -m_sym / n_sym
check(
    "(R1) parametric beta/alpha = -m/n via sympy symbolic solve",
    simplify(ratio_symbolic - expected_ratio) == 0,
    detail=f"beta = {beta_solution}, ratio = {ratio_symbolic}",
)

# Explicit numeric check at several (m, n, alpha):
test_triples = [
    (6, 2, Fraction(1)),
    (6, 2, Fraction(7, 11)),
    (4, 4, Fraction(-5)),
    (7, 1, Fraction(3, 2)),
    (3, 5, Fraction(-3, 17)),
    (12, 4, Fraction(100, 1)),
]
all_pass = True
for m, n, alpha in test_triples:
    beta = -Fraction(m) * alpha / Fraction(n)
    ratio = beta / alpha if alpha != 0 else None
    expected = Fraction(-m, n)
    if ratio != expected:
        all_pass = False
        break
check(
    "(R1) explicit Fraction sweep across (m, n, alpha) tests",
    all_pass,
    detail=f"{len(test_triples)} triples, all confirm beta/alpha = -m/n",
)

# ============================================================================
section("Part 3: (R2) closed-form (m, n) from (N, k) given divisibility")
# ============================================================================
# For (N, k) with (k+1) | N, the pair (m, n) = (k * N / (k+1), N / (k+1))
# satisfies m + n = N and m / n = k.
nk_pairs_divisible = [
    (8, 3),
    (8, 1),
    (8, 7),
    (10, 4),
    (12, 5),
    (12, 2),
    (12, 3),
    (14, 6),
    (16, 7),
    (16, 3),
    (24, 7),
]
for N, k in nk_pairs_divisible:
    if N % (k + 1) != 0:
        check(
            f"(R2) divisibility precondition holds at (N, k) = ({N}, {k})",
            False,
            detail=f"({k}+1)={k+1} does not divide N={N}; test setup error",
        )
        continue
    n = N // (k + 1)
    m = k * N // (k + 1)
    sum_ok = (m + n == N)
    ratio_ok = (Fraction(m, n) == Fraction(k, 1))
    check(
        f"(R2) at (N, k) = ({N}, {k}): (m, n) = ({m}, {n}), m+n=N, m/n=k",
        sum_ok and ratio_ok,
        detail=f"m+n={m+n}={N}, m/n={m/n}, expected k={k}",
    )

# ============================================================================
section("Part 4: (R3) admissibility iff (k+1) | N and N >= k+1")
# ============================================================================
# Sweep (N, k) with N in 2..32, k in 1..15. Predict admissibility from
# (R3) and verify by direct construction.
fail_count = 0
total = 0
for N in range(2, 33):
    for k in range(1, 16):
        total += 1
        predicted = (N % (k + 1) == 0) and (N >= k + 1)
        if predicted:
            # Closed form
            n = N // (k + 1)
            m = k * N // (k + 1)
            actual_admissible = (n >= 1 and m >= 1 and m + n == N)
        else:
            # Either non-integer n or n=0, or m=0 — not in P(N).
            # Confirm: no exact-integer partition (m, n) with m+n=N and m/n=k.
            actual_admissible = False
            for n_test in range(1, N):
                m_test = N - n_test
                # Need m_test == k * n_test (integer relation)
                if m_test == k * n_test:
                    actual_admissible = True
                    break
        if predicted != actual_admissible:
            fail_count += 1

check(
    "(R3) admissibility prediction matches exhaustive enumeration",
    fail_count == 0,
    detail=f"swept {total} (N, k) pairs, fail = {fail_count}",
)

# Spot checks of the divisibility logic.
specific = [
    (8, 3, True),   # (k+1)=4 | 8 -> (6, 2) admissible
    (8, 1, True),   # (k+1)=2 | 8 -> (4, 4) admissible
    (8, 7, True),   # (k+1)=8 | 8 -> (7, 1) admissible
    (8, 2, False),  # (k+1)=3 does not divide 8
    (8, 4, False),  # (k+1)=5 does not divide 8
    (8, 5, False),  # (k+1)=6 does not divide 8
    (8, 6, False),  # (k+1)=7 does not divide 8
]
for N, k, expected in specific:
    pred = (N % (k + 1) == 0) and (N >= k + 1)
    check(
        f"(R3) spot check at (N, k) = ({N}, {k})",
        pred == expected,
        detail=f"predicted={pred}, expected={expected}",
    )

# ============================================================================
section("Part 5: (R4) uniqueness within P(N=8); enumerate all ratios")
# ============================================================================
# Enumerate ordered partitions (m, n) of N = 8 with m, n >= 1.
N = 8
partitions_8 = [(m, N - m) for m in range(1, N)]
expected_ratios = {
    (1, 7): Fraction(-1, 7),
    (2, 6): Fraction(-1, 3),
    (3, 5): Fraction(-3, 5),
    (4, 4): Fraction(-1, 1),
    (5, 3): Fraction(-5, 3),
    (6, 2): Fraction(-3, 1),
    (7, 1): Fraction(-7, 1),
}
all_ratios_match = True
ratio_to_partitions = {}
for (m, n) in partitions_8:
    r = Fraction(-m, n)
    if r != expected_ratios[(m, n)]:
        all_ratios_match = False
    ratio_to_partitions.setdefault(r, []).append((m, n))

check(
    "(R4) all 7 ordered partitions of N=8 give expected ratios",
    all_ratios_match,
    detail=f"ratios = {sorted([(str(k), v) for k, v in expected_ratios.items()])}",
)

# Uniqueness: every ratio appears in exactly one partition.
each_ratio_unique = all(len(v) == 1 for v in ratio_to_partitions.values())
check(
    "(R4) each ratio in P(8) corresponds to exactly one partition",
    each_ratio_unique,
    detail=f"{len(ratio_to_partitions)} distinct ratios from 7 partitions, all unique",
)

# Integer ratios among the 7 partitions.
integer_ratio_partitions = [
    (m, n) for (m, n) in partitions_8 if (Fraction(-m, n).denominator == 1)
]
expected_integer_ratio_partitions = [(4, 4), (6, 2), (7, 1)]
check(
    "(R4) integer-ratio partitions of N=8 are exactly {(4,4), (6,2), (7,1)}",
    sorted(integer_ratio_partitions) == sorted(expected_integer_ratio_partitions),
    detail=f"found = {integer_ratio_partitions}",
)

# Framework instance: (6, 2) is the unique partition with ratio -3.
six_two_ratio_minus_three = (Fraction(-6, 2) == Fraction(-3, 1))
only_six_two = (ratio_to_partitions[Fraction(-3, 1)] == [(6, 2)])
check(
    "(R4) framework instance: (6, 2) is the unique partition of N=8 with ratio -3",
    six_two_ratio_minus_three and only_six_two,
    detail=f"ratio_to_partitions[-3] = {ratio_to_partitions[Fraction(-3, 1)]}",
)

# ============================================================================
section("Part 6: framework readout (N, k) = (8, 3) -> (m, n) = (6, 2)")
# ============================================================================
N_fw, k_fw = 8, 3
n_fw = N_fw // (k_fw + 1)
m_fw = k_fw * N_fw // (k_fw + 1)
check(
    f"framework: divisibility (k+1)={k_fw + 1} divides N={N_fw}",
    N_fw % (k_fw + 1) == 0,
    detail=f"{N_fw} mod {k_fw + 1} = {N_fw % (k_fw + 1)}",
)
check(
    f"framework: closed-form n = N/(k+1) = {n_fw}",
    n_fw == 2,
    detail=f"n = {n_fw}",
)
check(
    f"framework: closed-form m = k*N/(k+1) = {m_fw}",
    m_fw == 6,
    detail=f"m = {m_fw}",
)
check(
    "framework: (m, n) = (6, 2) and m + n = 8 (LH-doublet state count)",
    (m_fw, n_fw) == (6, 2) and (m_fw + n_fw) == 8,
    detail=f"(m, n) = ({m_fw}, {n_fw})",
)

# ============================================================================
section("Part 7: counterfactuals — non-admissible (N, k) and corollaries")
# ============================================================================
# (C4) (N, k) = (8, 2): (k+1) = 3 does not divide 8.
check(
    "(C4) (N, k) = (8, 2) is non-admissible",
    8 % 3 != 0,
    detail=f"8 mod 3 = {8 % 3}",
)
# Confirm no partition of 8 yields ratio -2 (m/n = 2).
no_ratio_minus_two = all(
    Fraction(-m, n) != Fraction(-2, 1) for (m, n) in partitions_8
)
check(
    "(C4) no partition of N=8 has ratio -2",
    no_ratio_minus_two,
    detail="exhaustive over P(8)",
)

# (C5) (N, k) = (8, 4): (k+1) = 5 does not divide 8.
check(
    "(C5) (N, k) = (8, 4) is non-admissible",
    8 % 5 != 0,
    detail=f"8 mod 5 = {8 % 5}",
)
no_ratio_minus_four = all(
    Fraction(-m, n) != Fraction(-4, 1) for (m, n) in partitions_8
)
check(
    "(C5) no partition of N=8 has ratio -4",
    no_ratio_minus_four,
    detail="exhaustive over P(8)",
)

# (C6) (N, k) = (8, 5): (k+1) = 6 does not divide 8.
check(
    "(C6) (N, k) = (8, 5) is non-admissible",
    8 % 6 != 0,
    detail=f"8 mod 6 = {8 % 6}",
)
no_ratio_minus_five = all(
    Fraction(-m, n) != Fraction(-5, 1) for (m, n) in partitions_8
)
check(
    "(C6) no partition of N=8 has ratio -5",
    no_ratio_minus_five,
    detail="exhaustive over P(8)",
)

# (C7) (N, k) = (8, 6): (k+1) = 7 does not divide 8.
check(
    "(C7) (N, k) = (8, 6) is non-admissible",
    8 % 7 != 0,
    detail=f"8 mod 7 = {8 % 7}",
)
no_ratio_minus_six = all(
    Fraction(-m, n) != Fraction(-6, 1) for (m, n) in partitions_8
)
check(
    "(C7) no partition of N=8 has ratio -6",
    no_ratio_minus_six,
    detail="exhaustive over P(8)",
)

# (C2) (N, k) = (8, 1): (k+1) = 2 divides 8, giving (m, n) = (4, 4).
n_c2 = 8 // 2
m_c2 = 1 * 8 // 2
check(
    "(C2) (N, k) = (8, 1) -> (m, n) = (4, 4)",
    (m_c2, n_c2) == (4, 4),
    detail=f"(m, n) = ({m_c2}, {n_c2})",
)

# (C3) (N, k) = (8, 7): (k+1) = 8 divides 8, giving (m, n) = (7, 1).
n_c3 = 8 // 8
m_c3 = 7 * 8 // 8
check(
    "(C3) (N, k) = (8, 7) -> (m, n) = (7, 1)",
    (m_c3, n_c3) == (7, 1),
    detail=f"(m, n) = ({m_c3}, {n_c3})",
)

# ============================================================================
section("Part 8: forward/inverse pair consistency check")
# ============================================================================
# Forward direction (from LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02):
#   partition (6, 2) + tracelessness 6*alpha + 2*beta = 0  =>  ratio -3.
# Inverse direction (this note):
#   N = 8 + ratio target -3                                 =>  partition (6, 2).
# Composing forward(inverse(8, -3)) and inverse(8, forward(6, 2)) should
# give back the input.
alpha_test = Fraction(1, 3)
beta_test = -Fraction(6) * alpha_test / Fraction(2)
forward_ratio = beta_test / alpha_test
check(
    "forward: (m, n) = (6, 2), alpha = 1/3 -> beta = -1, ratio = -3",
    beta_test == Fraction(-1) and forward_ratio == Fraction(-3),
    detail=f"beta = {beta_test}, ratio = {forward_ratio}",
)

# Inverse: (N, k) = (8, 3) -> (m, n) = (6, 2)
N_inv, k_inv = 8, 3
n_inv = N_inv // (k_inv + 1)
m_inv = k_inv * N_inv // (k_inv + 1)
check(
    "inverse: (N, k) = (8, 3) -> (m, n) = (6, 2)",
    (m_inv, n_inv) == (6, 2),
    detail=f"(m, n) = ({m_inv}, {n_inv})",
)

# forward(inverse(N=8, k=3)) = -3
N_round, k_round = 8, 3
n_r = N_round // (k_round + 1)
m_r = k_round * N_round // (k_round + 1)
alpha_r = Fraction(1)
beta_r = -Fraction(m_r) * alpha_r / Fraction(n_r)
ratio_r = beta_r / alpha_r
check(
    "forward(inverse(8, 3)) recovers ratio -3",
    ratio_r == Fraction(-3),
    detail=f"(m, n) = ({m_r}, {n_r}), ratio = {ratio_r}",
)

# inverse(N=8, forward(6, 2)) = (6, 2)
alpha_b = Fraction(1)
beta_b = -Fraction(6) * alpha_b / Fraction(2)
ratio_b = beta_b / alpha_b
k_b = -int(ratio_b)
n_b = N_round // (k_b + 1)
m_b = k_b * N_round // (k_b + 1)
check(
    "inverse(8, forward(6, 2)) recovers partition (6, 2)",
    (m_b, n_b) == (6, 2),
    detail=f"forward ratio = {ratio_b}, k = {k_b}, recovered (m, n) = ({m_b}, {n_b})",
)

# ============================================================================
section("Part 9: cited authorities are retained-grade (cross-references only)")
# ============================================================================
# The note's cross-references to LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02
# and GRAPH_FIRST_SU3_INTEGRATION_NOTE are NON-load-bearing on the
# abstract algebra. But for audit hygiene, confirm both are retained-grade
# (so the optional framework readout sub-section does not introduce a
# below-grade dependency).
import json
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
ledger_data = json.loads(LEDGER.read_text())
ledger_rows = ledger_data["rows"]

retained_grades = {"retained", "retained_bounded", "retained_no_go"}
cited = [
    "lh_doublet_traceless_abelian_eigenvalue_ratio_narrow_theorem_note_2026-05-02",
    "graph_first_su3_integration_note",
]
for cid in cited:
    actual_es = ledger_rows.get(cid, {}).get("effective_status")
    check(
        f"cross-reference {cid} is retained-grade",
        actual_es in retained_grades,
        detail=f"observed = {actual_es!r}",
    )

# ============================================================================
section("Summary")
# ============================================================================
print("  Verified at exact sympy/Fraction precision:")
print("    (R1) parametric ratio identity beta/alpha = -m/n")
print("    (R2) closed-form (m, n) = (k*N/(k+1), N/(k+1)) under divisibility")
print("    (R3) admissibility iff (k+1) | N and N >= k+1 across (N, k) sweep")
print("    (R4) uniqueness within P(N=8); only (6, 2) has ratio -3")
print("    Framework readout (N, k) = (8, 3) -> (m, n) = (6, 2)")
print("    Counterfactuals (C4)-(C7): no partition of N=8 with ratio in {-2,-4,-5,-6}")
print("    Forward/inverse pair consistency: round-trips recover both halves")
print("    Cross-referenced authorities all retained-grade")

print(f"\n{'='*88}")
print(f"  TOTAL: PASS={PASS}, FAIL={FAIL}")
print(f"{'='*88}")

sys.exit(1 if FAIL > 0 else 0)
