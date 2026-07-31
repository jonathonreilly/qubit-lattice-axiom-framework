#!/usr/bin/env python3
"""Verify the narrow Schur covariance inheritance theorem at exact rational
precision via sympy.

Claim scope: U M U† = M block-diagonal (U = U_1 ⊕ U_W) on V = V_1 ⊕ W with
M = [[A, B], [B†, D]] and D invertible ⇒ U_1 S U_1† = S where S = A - B D⁻¹ B†.

Load-bearing step is class (A) algebraic identity on block matrix relations.
"""

from pathlib import Path
import json
from random import Random
import sys

AUDIT_INPUT_PATHS = (
    "docs/SCHUR_COVARIANCE_INHERITANCE_NARROW_THEOREM_NOTE_2026-05-02.md",
    "docs/audit/data/ledger/si/site_phase_cube_shift_intertwiner_note.json",
)

try:
    from sympy import Matrix, eye, zeros
except ImportError:
    print("FAIL: sympy required for exact rational matrix algebra")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
DEPENDENCY_LEDGER_PATH = (
    ROOT / AUDIT_INPUT_PATHS[1]
)
RETAINED_GRADES = {"retained", "retained_bounded", "retained_no_go"}

PASS = 0
FAIL = 0


def check(label, ok, detail="", check_class="A"):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = f"PASS ({check_class})" if ok else f"FAIL ({check_class})"
    print(f"  [{tag}] {label}  ({detail})")


def section(title):
    print("\n" + "-" * 88 + f"\n{title}\n" + "-" * 88)


# ============================================================================
section("Part 1: note structure and scope discipline")
# ============================================================================
note_text = NOTE_PATH.read_text()
required = [
    "Schur Complement Covariance Inheritance — Narrow Theorem",
    "Type:** positive_theorem",
    "U M U† = M",
    "S = A − B D⁻¹ B†",
    "U_1 S U_1† = S",
    "not** claim",  # \"**does\\nnot** claim\" (line-wrapped)
    "SITE_PHASE_CUBE_SHIFT_INTERTWINER_NOTE.md",
    "class (A)",
    "target_claim_type: positive_theorem",
]
for s in required:
    check(f"contains: {s!r}", s in note_text, check_class="B")

# Scope discipline: ensure no physical-applicability claim is load-bearing
forbidden = [
    "applies to physical charged leptons unconditionally",
    "the Schur reduction IS the physical reduction map",
    "D is invertible for the physical effective operator",
]
for f in forbidden:
    check(f"narrow scope avoids forbidden claim: {f!r}",
          f not in note_text,
          check_class="B")


# ============================================================================
section("Part 2: lemma on 3+1 split with V_1 = C³, W = C¹")
# ============================================================================
# C_3 cyclic action on V_1 = C³:
# C: e_0 -> e_1 -> e_2 -> e_0
C3 = Matrix([[0, 0, 1],
             [1, 0, 0],
             [0, 1, 0]])

# Verify C³ = I
check("C₃³ = I (group order 3)",
      C3**3 == eye(3),
      detail="canonical cyclic shift on V_1")

# Build a positive Hermitian M = [[A, B], [B†, D]] with A 3x3, B 3x1, D 1x1.
# Need M C-covariant: U M U† = M with U = C_3 ⊕ U_W.
# Choose U_W = 1 (trivial 1x1 unitary).

# A must commute with C_3 (so be circulant). Pick A = aI + bC + b*C^T circulant.
# Simplification: A = sum c_k C^k for real c_k giving Hermitian circulant.
# Take A = I + C + C^T (Hermitian, commutes with C).
A = eye(3) + C3 + C3.T

# B must satisfy U_1 B U_W† = B, i.e. C_3 B = B (since U_W = 1).
# So B is in the C_3-fixed subspace of C³ ⊗ C¹ = C³.
# Fixed vectors of C_3 on C³ are multiples of (1, 1, 1)^T.
B = Matrix([[1], [1], [1]])  # C_3-invariant vector

# D 1x1: any positive number; commutes trivially with U_W = 1.
D = Matrix([[2]])  # positive scalar

# Build M
def build_M(A, B, D):
    n1 = A.shape[0]
    n2 = D.shape[0]
    M = zeros(n1+n2, n1+n2)
    for i in range(n1):
        for j in range(n1):
            M[i, j] = A[i, j]
        for j in range(n2):
            M[i, n1+j] = B[i, j]
    for i in range(n2):
        for j in range(n1):
            M[n1+i, j] = B.conjugate().T[i, j]
        for j in range(n2):
            M[n1+i, n1+j] = D[i, j]
    return M

M = build_M(A, B, D)

# U = C_3 ⊕ U_W
U_W_PLUS = Matrix([[1]])
U = zeros(4, 4)
U[:3, :3] = C3
U[3, 3] = 1

# Verify Hermiticity and invertibility premises.
check("3+1 split: M is Hermitian and D is invertible",
      M.H == M and D.det() != 0)

# Verify U M U^† = M (covariance of full M)
M_rotated = U * M * U.H
check("U M U† = M (full M is C₃-covariant)",
      M_rotated == M,
      detail="block-diagonal U preserves the assumed covariance")
check("3+1 split: U_W D⁻¹ U_W† = D⁻¹",
      U_W_PLUS * D.inv() * U_W_PLUS.H == D.inv())

# Compute Schur complement S = A - B D^{-1} B†
S = A - B * D.inv() * B.H

# Verify S is C_3-covariant on V_1
S_rotated = C3 * S * C3.H
check("U_1 S U_1† = S (Schur complement covariance inheritance)",
      S_rotated == S,
      detail="this is the narrow theorem's claim")

# Direct check: S is a circulant matrix
def is_circulant(M, U_action, n):
    return M * U_action == U_action * M
check("S commutes with C_3 (equivalently circulant on V_1 = C³)",
      is_circulant(S, C3, 3))


# ============================================================================
section("Part 3: 3+1 split with the nontrivial sign action U_W = -1")
# ============================================================================
# With U_1 = C_3 and U_W = -1, the intertwining condition is C_3 B = -B.
# Since -1 is not an eigenvalue of C_3, this forces B = 0.  This is still a
# genuine edge case of the theorem and directly exercises the sign action
# claimed in the note.  These actions define a common C_6 representation:
# the V_1 action factors through C_3 and the W action factors through C_2.
# The combined generator has exact order six.
U_W_MINUS = Matrix([[-1]])
B_MINUS = zeros(3, 1)
D_MINUS = Matrix([[3]])
M_MINUS = build_M(A, B_MINUS, D_MINUS)
U_MINUS = zeros(4, 4)
U_MINUS[:3, :3] = C3
U_MINUS[3, 3] = -1

check("U_W = -1: combined block action is unitary",
      U_MINUS * U_MINUS.H == eye(4))
check("U_W = -1: combined generator has order six",
      U_MINUS**6 == eye(4)
      and all(U_MINUS**k != eye(4) for k in range(1, 6)))
check("U_W = -1: -1 is absent from the C₃ spectrum, so covariance forces B = 0",
      (C3 + eye(3)).det() == 2 and B_MINUS == zeros(3, 1),
      detail=f"det(C₃ + I) = {(C3 + eye(3)).det()}")
check("U_W = -1: off-diagonal intertwining relation holds",
      C3 * B_MINUS * U_W_MINUS.H == B_MINUS)
check("U_W = -1: M is Hermitian and D is invertible",
      M_MINUS.H == M_MINUS and D_MINUS.det() != 0)
check("U_W = -1: U M U† = M",
      U_MINUS * M_MINUS * U_MINUS.H == M_MINUS)
check("U_W = -1: U_W D⁻¹ U_W† = D⁻¹",
      U_W_MINUS * D_MINUS.inv() * U_W_MINUS.H == D_MINUS.inv())
S_MINUS = A - B_MINUS * D_MINUS.inv() * B_MINUS.H
check("U_W = -1: U_1 S U_1† = S",
      C3 * S_MINUS * C3.H == S_MINUS)


# ============================================================================
section("Part 4: lemma on 3+3 split with distinct C₃ actions")
# ============================================================================
# V_1 carries C_3 while W carries C_3².  Orbit-summing B under
# X -> U_1 X U_W† constructs an exact, nonzero intertwiner for these distinct
# representations.  A and D are invariant under their respective actions.

A2 = eye(3) + 3 * C3 + 3 * C3.T  # Hermitian circulant
U1_2 = C3
UW_2 = C3**2
B2_seed = Matrix([[1, 2, 0],
                  [0, -1, 3],
                  [4, 0, 2]])
B2 = sum(
    [(U1_2**k) * B2_seed * (UW_2.H**k) for k in range(3)],
    zeros(3, 3),
)
D2 = 5 * eye(3) + 1 * C3 + 1 * C3.T  # Hermitian invertible circulant

# Construct M2
M2 = zeros(6, 6)
M2[:3, :3] = A2
M2[:3, 3:] = B2
M2[3:, :3] = B2.H
M2[3:, 3:] = D2

# U2 = C_3 ⊕ C_3²
U2 = zeros(6, 6)
U2[:3, :3] = U1_2
U2[3:, 3:] = UW_2

# Verify U2 M2 U2^† = M2
M2_rotated = U2 * M2 * U2.H
check("3+3 split: U_1 = C₃ and U_W = C₃² are distinct",
      U1_2 != UW_2 and U1_2**3 == eye(3) and UW_2**3 == eye(3))
check("3+3 split: orbit-averaged B is a nonzero intertwiner",
      B2 != zeros(3, 3) and U1_2 * B2 * UW_2.H == B2)
check("3+3 split: U M U† = M",
      M2_rotated == M2)
check("3+3 split: M is Hermitian",
      M2.H == M2)

# D must be invertible
check("3+3 split: D₂ is invertible",
      D2.det() != 0,
      detail=f"det(D₂) = {D2.det()}")
check("3+3 split: U_W D⁻¹ U_W† = D⁻¹",
      UW_2 * D2.inv() * UW_2.H == D2.inv())

# Schur complement
S2 = A2 - B2 * D2.inv() * B2.H

# Verify covariance inheritance
S2_rotated = U1_2 * S2 * U1_2.H
check("3+3 split: U_1 S U_1† = S (covariance inheritance)",
      S2_rotated == S2)


# ============================================================================
section("Part 5: deterministic random exact C₃-covariant matrix suite")
# ============================================================================
RNG = Random(20260502)
RANDOM_CASES = 12


def random_integer_matrix(rows, cols):
    return Matrix([
        [RNG.randint(-4, 4) for _ in range(cols)]
        for _ in range(rows)
    ])


for case in range(RANDOM_CASES):
    p1, pw = ((1, 1), (1, 2), (2, 1), (2, 2))[case % 4]
    U1_random = C3**p1
    UW_random = C3**pw

    QA = random_integer_matrix(3, 3)
    QD = random_integer_matrix(3, 3)
    X = random_integer_matrix(3, 3) + 5 * eye(3)
    A0 = QA.T * QA + eye(3)
    D0 = QD.T * QD + eye(3)

    A_random = sum(
        [(U1_random**k) * A0 * (U1_random.H**k) for k in range(3)],
        zeros(3, 3),
    )
    D_random = sum(
        [(UW_random**k) * D0 * (UW_random.H**k) for k in range(3)],
        zeros(3, 3),
    )
    B_random = sum(
        [(U1_random**k) * X * (UW_random.H**k) for k in range(3)],
        zeros(3, 3),
    )

    M_random = build_M(A_random, B_random, D_random)
    U_random = zeros(6, 6)
    U_random[:3, :3] = U1_random
    U_random[3:, 3:] = UW_random
    S_random = A_random - B_random * D_random.inv() * B_random.H

    exact_conditions = [
        U1_random**3 == eye(3),
        UW_random**3 == eye(3),
        A_random.H == A_random,
        D_random.H == D_random,
        M_random.H == M_random,
        B_random != zeros(3, 3),
        U1_random * B_random * UW_random.H == B_random,
        D_random.det() != 0,
        UW_random * D_random.inv() * UW_random.H == D_random.inv(),
        U_random * M_random * U_random.H == M_random,
        U1_random * S_random * U1_random.H == S_random,
    ]
    check(
        f"random exact case {case + 1:02d}/{RANDOM_CASES}: full and Schur covariance",
        all(exact_conditions),
        detail=f"actions=(C₃^{p1}, C₃^{pw}), det(D)={D_random.det()}",
    )


# ============================================================================
section("Part 6: premise-rejection controls")
# ============================================================================
# Control 1: U is not block-diagonal, so the theorem is inapplicable.
U_bad = zeros(4, 4)
U_bad[0, 3] = 1  # mixes V_1 with W
U_bad[1, 1] = 1
U_bad[2, 2] = 1
U_bad[3, 0] = 1

check("control: mixing action is unitary but not block-diagonal",
      U_bad * U_bad.H == eye(4)
      and (U_bad[:3, 3:] != zeros(3, 1) or U_bad[3:, :3] != zeros(1, 3)),
      detail="the theorem requires preservation of V_1 ⊕ W")
check("control: mixing action does not satisfy covariance for the fixture",
      U_bad * M * U_bad.H != M)

# Control 2: M is not C_3-covariant and its Schur complement is not either.
M_bad = M.copy()
M_bad[0, 0] = 99  # break A's circulant structure
check("control: non-covariant M does not satisfy U M U† = M (premise fails)",
      U * M_bad * U.H != M_bad,
      detail="premise of theorem requires U M U† = M")
S_bad = M_bad[:3, :3] - M_bad[:3, 3:] * M_bad[3:, 3:].inv() * M_bad[3:, :3]
check("control: this non-covariant fixture also has a non-covariant Schur complement",
      C3 * S_bad * C3.H != S_bad)


# ============================================================================
section("Part 7: cited authority is retained-grade (packet-safe shard read)")
# ============================================================================
dep_id = "site_phase_cube_shift_intertwiner_note"
check("canonical dependency ledger shard is present",
      DEPENDENCY_LEDGER_PATH.is_file(),
      detail=str(DEPENDENCY_LEDGER_PATH.relative_to(ROOT)),
      check_class="B")
dep_row = json.loads(DEPENDENCY_LEDGER_PATH.read_text(encoding="utf-8"))
check("dependency shard identifies the cited authority",
      dep_row.get("claim_id") == dep_id,
      detail=f"observed = {dep_row.get('claim_id')!r}",
      check_class="B")
dep_es = dep_row.get("effective_status")
check(f"{dep_id} effective_status is retained-grade",
      dep_es in RETAINED_GRADES,
      detail=f"observed = {dep_es!r}",
      check_class="B")


print(f"\n{'='*88}\n  TOTAL: PASS={PASS}, FAIL={FAIL}\n{'='*88}")
sys.exit(1 if FAIL > 0 else 0)
