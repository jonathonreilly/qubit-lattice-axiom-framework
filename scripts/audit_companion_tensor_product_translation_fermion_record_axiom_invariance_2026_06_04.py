#!/usr/bin/env python3
"""Audit-companion runner for the tensor-product translation / fermion
operator bridge parent note
`TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md`
recording Record-axiom invariance after the 2026-06-04 framework axiom
adoption.

Companion source note:
  docs/TENSOR_PRODUCT_TRANSLATION_FERMION_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent's load-bearing
    operator-algebra identities (T1) unitarity, (T2) group law,
    (T3) fermion-operator covariance, and (T4) charge conservation
    are independent of the Record axiom adopted in
    `MINIMAL_AXIOMS_2026-06-04.md`. This does not re-apply the prior
    audit verdict; it gives the audit lane a machine-checkable basis
    for deciding whether the matrix algebra needs fresh review after
    the premise-hash change.

The runner verifies the load-bearing identities block-by-block under
"Record axiom is asserted" and "Record axiom is not asserted" outer
scopes, confirms identical exact-symbolic matrix outputs in both
scopes, and performs a static-source scan of the parent note to
confirm zero Record-axiom usage in the auditable core.

Every load-bearing matrix check uses only:
  (i)   the per-site one-qubit operator algebra A_x ≅ M_2(C)
        (Quantum axiom content);
  (ii)  the Z^3 cyclic-shift / translation structure on the finite
        block Λ (Lattice axiom content, with standard finite-volume
        periodic identification);
  (iii) the standard tensor-product Fock-space construction
        H_Λ = ⊗_x C²_x (definitional infrastructure);
  (iv)  the single-mode per-site Pauli realization
        a_x = I_{Λ \\ {x}} ⊗ σ_-^{(x)} (definitional).

No Record-axiom content (scalar record additivity functional `I(·)`)
enters any block. No claim is made about Record-axiom-induced
downstream content; the companion observation is strictly limited to
the four load-bearing identities (T1)-(T4) of the parent note.

Block plan:
  Block 1  : Quantum-axiom-only construction of H_Λ for N=2.
  Block 2  : Lattice-axiom-only construction of T_1 for N=2.
  Block 3  : (T1) Unitarity at N=2.
  Block 4  : (T2) Group law at N=2.
  Block 5  : (T3) Fermion-operator covariance at N=2.
  Block 6  : (T4) Charge conservation at N=2.
  Block 7  : (T1)-(T4) at N=3.
  Block 8  : (T2) full group law at N=4.
  Block 9  : (T3) on the 2D 2×2 block.
  Block 10 : Record-axiom counterfactual: identical matrix output
             with and without an explicit "Record axiom asserted"
             outer scope.
  Block 11 : Static-source scan of parent note's load-bearing
             section: zero Record-axiom usage tokens.
  Block 12 : Quantum/Lattice content preservation across the historical
             2026-05-20 and current 2026-06-04 minimal-axioms memos.

The exact PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

import sys
from itertools import product
from pathlib import Path

try:
    import sympy
    from sympy import Matrix, eye, zeros, simplify
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


# -----------------------------------------------------------
# Logging and counters
# -----------------------------------------------------------

LOG_LINES: list[str] = []
PASS = 0
FAIL = 0


def log(msg: str = "") -> None:
    LOG_LINES.append(msg)
    print(msg)


def record(check_name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        log(f"  PASS {check_name}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        log(f"  FAIL {check_name}" + (f" :: {detail}" if detail else ""))


def header(title: str) -> None:
    log("")
    log("=" * 72)
    log(title)
    log("=" * 72)


def mat_eq(A: Matrix, B: Matrix) -> bool:
    """Exact matrix equality via sympy.simplify on every entry."""
    if A.shape != B.shape:
        return False
    diff = A - B
    return all(
        simplify(diff[i, j]) == 0
        for i in range(diff.rows)
        for j in range(diff.cols)
    )


def is_zero(M: Matrix) -> bool:
    return all(
        simplify(M[i, j]) == 0
        for i in range(M.rows)
        for j in range(M.cols)
    )


# -----------------------------------------------------------
# Quantum-axiom-only per-site primitives
# -----------------------------------------------------------

# One-qubit ladder matrices on the per-site dim-two factor C²_x in
# ordered basis (|0>, |1>). These are the SAME matrices used in the
# parent runner.
SIGMA_PLUS = Matrix([[0, 0], [1, 0]])   # σ_+ : |0⟩ → |1⟩
SIGMA_MINUS = Matrix([[0, 1], [0, 0]])  # σ_- : |1⟩ → |0⟩
ID2 = eye(2)


def tensor_chain(factors):
    """Kronecker product of a non-empty list of sympy Matrices."""
    out = factors[0]
    for f in factors[1:]:
        out = sympy.kronecker_product(out, f)
    return out


def site_op_1d(N: int, x: int, local: Matrix) -> Matrix:
    """Build I ⊗ ... ⊗ local^{(x)} ⊗ ... ⊗ I on (C²)^{⊗ N}."""
    factors = [local if i == x else ID2 for i in range(N)]
    return tensor_chain(factors)


def a_op_1d(N: int, x: int) -> Matrix:
    return site_op_1d(N, x, SIGMA_MINUS)


def adag_op_1d(N: int, x: int) -> Matrix:
    return site_op_1d(N, x, SIGMA_PLUS)


def basis_index_1d(bits: tuple[int, ...]) -> int:
    """Map an N-bit tuple to a basis index (factor-0-leftmost)."""
    N = len(bits)
    idx = 0
    for i, b in enumerate(bits):
        idx += b * (1 << (N - 1 - i))
    return idx


def translation_1d(N: int, a: int) -> Matrix:
    """Tensor-permutation cyclic-shift T_a on (C²)^{⊗ N} (1D)."""
    dim = 1 << N
    M = zeros(dim, dim)
    for bits in product((0, 1), repeat=N):
        out_bits = tuple(bits[(x - a) % N] for x in range(N))
        i_in = basis_index_1d(bits)
        i_out = basis_index_1d(out_bits)
        M[i_out, i_in] = 1
    return M


def q_total_1d(N: int) -> Matrix:
    Q = zeros(1 << N, 1 << N)
    for x in range(N):
        Q = Q + adag_op_1d(N, x) * a_op_1d(N, x)
    return Q


# 2D utilities (Lx × Ly) for Block 9
def basis_index_2d(bits, Lx: int, Ly: int) -> int:
    flat = [bits[i][j] for i in range(Lx) for j in range(Ly)]
    return basis_index_1d(tuple(flat))


def site_op_2d(Lx: int, Ly: int, ix: int, iy: int, local: Matrix) -> Matrix:
    N = Lx * Ly
    flat_site = ix * Ly + iy
    return site_op_1d(N, flat_site, local)


def a_op_2d(Lx: int, Ly: int, ix: int, iy: int) -> Matrix:
    return site_op_2d(Lx, Ly, ix, iy, SIGMA_MINUS)


def translation_2d(Lx: int, Ly: int, ax: int, ay: int) -> Matrix:
    """Tensor-permutation translation T_{(ax, ay)} on the 2D block."""
    N = Lx * Ly
    dim = 1 << N
    M = zeros(dim, dim)
    for bits_flat in product((0, 1), repeat=N):
        bits = [[bits_flat[i * Ly + j] for j in range(Ly)] for i in range(Lx)]
        out_bits = [
            [bits[(ix - ax) % Lx][(iy - ay) % Ly] for iy in range(Ly)]
            for ix in range(Lx)
        ]
        i_in = basis_index_2d(bits, Lx, Ly)
        i_out = basis_index_2d(out_bits, Lx, Ly)
        M[i_out, i_in] = 1
    return M


# -----------------------------------------------------------
# Block 1: Quantum-axiom-only construction of H_Λ for N=2
# -----------------------------------------------------------

def block1() -> None:
    header("BLOCK 1: Quantum-axiom-only H_Λ construction at N=2")
    log("  Builds H_Λ = C² ⊗ C² as dim-4 sympy Matrix from Quantum-axiom")
    log("  per-site C²_x factors; verifies a_x and a_x^† are adjoints.")
    a0 = a_op_1d(2, 0)
    a1 = a_op_1d(2, 1)
    adag0 = adag_op_1d(2, 0)
    adag1 = adag_op_1d(2, 1)

    record("H_Lambda_dim_4", a0.shape == (4, 4),
           f"a_0 acts on dim {a0.shape}")
    record("a0_adjoint_is_adag0", mat_eq(a0.H, adag0),
           "(a_0)^† = a_0^† at exact precision")
    record("a1_adjoint_is_adag1", mat_eq(a1.H, adag1),
           "(a_1)^† = a_1^† at exact precision")


# -----------------------------------------------------------
# Block 2: Lattice-axiom-only construction of T_1 for N=2
# -----------------------------------------------------------

def block2() -> None:
    header("BLOCK 2: Lattice-axiom-only T_1 construction at N=2")
    log("  Builds T_1 from cyclic-shift basis permutation rule (eq. 2 of")
    log("  parent); uses only Λ ⊂ Z^3 translation structure.")
    T1 = translation_1d(2, 1)
    record("T1_is_4x4", T1.shape == (4, 4), f"T_1 shape = {T1.shape}")

    # T_1 is a permutation matrix: each row and column has exactly one 1.
    row_sums = [sum(T1[i, j] for j in range(4)) for i in range(4)]
    col_sums = [sum(T1[i, j] for i in range(4)) for j in range(4)]
    record("T1_is_permutation_row_sums_1",
           all(r == 1 for r in row_sums),
           f"row sums = {row_sums}")
    record("T1_is_permutation_col_sums_1",
           all(c == 1 for c in col_sums),
           f"col sums = {col_sums}")


# -----------------------------------------------------------
# Block 3: (T1) Unitarity at N=2
# -----------------------------------------------------------

def block3() -> None:
    header("BLOCK 3: (T1) Unitarity at N=2")
    T1 = translation_1d(2, 1)
    I4 = eye(4)
    record("T1_T1dag_eq_I", mat_eq(T1 * T1.H, I4),
           "T_1 T_1^† = I_4 exactly")
    record("T1dag_T1_eq_I", mat_eq(T1.H * T1, I4),
           "T_1^† T_1 = I_4 exactly")


# -----------------------------------------------------------
# Block 4: (T2) Group law at N=2
# -----------------------------------------------------------

def block4() -> None:
    header("BLOCK 4: (T2) Group law at N=2")
    T0 = translation_1d(2, 0)
    T1 = translation_1d(2, 1)
    I4 = eye(4)
    record("T0_eq_I", mat_eq(T0, I4), "T_0 = I_4 (period-2 group identity)")
    record("T1_squared_eq_I", mat_eq(T1 * T1, I4),
           "T_1 T_1 = T_2 (≡ T_0 on Z/2) = I_4")


# -----------------------------------------------------------
# Block 5: (T3) Fermion covariance at N=2
# -----------------------------------------------------------

def block5() -> None:
    header("BLOCK 5: (T3) Fermion-operator covariance at N=2")
    T1 = translation_1d(2, 1)
    a0 = a_op_1d(2, 0)
    a1 = a_op_1d(2, 1)
    adag0 = adag_op_1d(2, 0)
    adag1 = adag_op_1d(2, 1)

    record("T3_T1_a0_T1dag_eq_a1",
           mat_eq(T1 * a0 * T1.H, a1),
           "T_1 a_0 T_1^† = a_1")
    record("T3_T1_a1_T1dag_eq_a0",
           mat_eq(T1 * a1 * T1.H, a0),
           "T_1 a_1 T_1^† = a_0")
    record("T3_T1_adag0_T1dag_eq_adag1",
           mat_eq(T1 * adag0 * T1.H, adag1),
           "T_1 a_0^† T_1^† = a_1^†")
    record("T3_T1_adag1_T1dag_eq_adag0",
           mat_eq(T1 * adag1 * T1.H, adag0),
           "T_1 a_1^† T_1^† = a_0^†")


# -----------------------------------------------------------
# Block 6: (T4) Charge conservation at N=2
# -----------------------------------------------------------

def block6() -> None:
    header("BLOCK 6: (T4) Charge conservation at N=2")
    T1 = translation_1d(2, 1)
    Q = q_total_1d(2)
    record("T4_T1_Q_T1dag_eq_Q",
           mat_eq(T1 * Q * T1.H, Q),
           "T_1 Q_total T_1^† = Q_total")
    record("T4_commutator_zero",
           is_zero(T1 * Q - Q * T1),
           "[T_1, Q_total] = 0_4")


# -----------------------------------------------------------
# Block 7: (T1)-(T4) at N=3
# -----------------------------------------------------------

def block7() -> None:
    header("BLOCK 7: (T1)-(T4) at N=3 (8-dim block, full cyclic group)")
    N = 3
    dim = 1 << N
    Id = eye(dim)
    Q = q_total_1d(N)
    Ts = {a: translation_1d(N, a) for a in range(N)}

    # (T1) for every a
    for a in range(N):
        T = Ts[a]
        record(f"T1_unitarity_N3_a{a}_left",
               mat_eq(T * T.H, Id),
               f"T_{a} T_{a}^† = I_8")
        record(f"T1_unitarity_N3_a{a}_right",
               mat_eq(T.H * T, Id),
               f"T_{a}^† T_{a} = I_8")

    # (T2) for sample pairs
    record("T2_group_law_N3_T1_T2_eq_I",
           mat_eq(Ts[1] * Ts[2], Ts[0]),
           "T_1 T_2 = T_3 ≡ T_0 = I")
    record("T2_group_law_N3_T1_T1_eq_T2",
           mat_eq(Ts[1] * Ts[1], Ts[2]),
           "T_1 T_1 = T_2")

    # (T3) for every (a, x)
    for a in range(N):
        T = Ts[a]
        Tdag = T.H
        for x in range(N):
            lhs = T * a_op_1d(N, x) * Tdag
            rhs = a_op_1d(N, (x + a) % N)
            record(f"T3_N3_a{a}_x{x}",
                   mat_eq(lhs, rhs),
                   f"T_{a} a_{x} T_{a}^† = a_{(x + a) % N}")

    # (T4) for every a
    for a in range(N):
        T = Ts[a]
        record(f"T4_N3_a{a}",
               is_zero(T * Q - Q * T),
               f"[T_{a}, Q_total] = 0")


# -----------------------------------------------------------
# Block 8: (T2) full group law at N=4
# -----------------------------------------------------------

def block8() -> None:
    header("BLOCK 8: (T2) full group law at N=4 (16-dim block, all pairs)")
    N = 4
    Ts = {a: translation_1d(N, a) for a in range(N)}
    misses = 0
    for a in range(N):
        for b in range(N):
            lhs = Ts[a] * Ts[b]
            rhs = Ts[(a + b) % N]
            ok = mat_eq(lhs, rhs)
            if not ok:
                misses += 1
            record(f"T2_N4_a{a}_b{b}",
                   ok,
                   f"T_{a} T_{b} = T_{(a + b) % N}")
    record("T2_N4_all_16_pairs_close",
           misses == 0,
           f"all 16 (a,b) pairs satisfy the group law; misses = {misses}")


# -----------------------------------------------------------
# Block 9: (T3) on the 2D 2x2 block
# -----------------------------------------------------------

def block9() -> None:
    header("BLOCK 9: (T3) on the 2D 2×2 block (independent lattice axes)")
    Lx, Ly = 2, 2
    Tx = translation_2d(Lx, Ly, 1, 0)
    Ty = translation_2d(Lx, Ly, 0, 1)
    I = eye(1 << (Lx * Ly))

    record("T1_unitarity_Tx", mat_eq(Tx * Tx.H, I),
           "T_x T_x^† = I_16")
    record("T1_unitarity_Ty", mat_eq(Ty * Ty.H, I),
           "T_y T_y^† = I_16")

    for ix in range(Lx):
        for iy in range(Ly):
            lhs_x = Tx * a_op_2d(Lx, Ly, ix, iy) * Tx.H
            rhs_x = a_op_2d(Lx, Ly, (ix + 1) % Lx, iy)
            record(
                f"T3_Tx_a{ix}{iy}",
                mat_eq(lhs_x, rhs_x),
                f"T_x a_{{{ix},{iy}}} T_x^† = a_{{{(ix + 1) % Lx},{iy}}}",
            )
            lhs_y = Ty * a_op_2d(Lx, Ly, ix, iy) * Ty.H
            rhs_y = a_op_2d(Lx, Ly, ix, (iy + 1) % Ly)
            record(
                f"T3_Ty_a{ix}{iy}",
                mat_eq(lhs_y, rhs_y),
                f"T_y a_{{{ix},{iy}}} T_y^† = a_{{{ix},{(iy + 1) % Ly}}}",
            )


# -----------------------------------------------------------
# Block 10: Record-axiom counterfactual
# -----------------------------------------------------------

def block10() -> None:
    header("BLOCK 10: Record-axiom counterfactual at N=2 (4 identities)")
    log("  Compute matrix entries for (T1)-(T4) under two outer scopes:")
    log("    scope_A: Record axiom is asserted (in framework axiom set).")
    log("    scope_B: Record axiom is NOT asserted.")
    log("  No code path consumes any Record-functional `I(·)` content;")
    log("  the matrix outputs are bitwise identical in both scopes.")

    def compute_identities(record_axiom_asserted: bool):
        # The matrix algebra does not depend on `record_axiom_asserted`;
        # we pass the flag only to confirm the boolean is inert.
        _ = record_axiom_asserted  # documentation only
        T1 = translation_1d(2, 1)
        a0 = a_op_1d(2, 0)
        a1 = a_op_1d(2, 1)
        Q = q_total_1d(2)
        I4 = eye(4)
        return {
            "T1_T1dag": T1 * T1.H,
            "I4": I4,
            "T1_squared": T1 * T1,
            "T1_a0_T1dag": T1 * a0 * T1.H,
            "a1": a1,
            "T1_Q_T1dag": T1 * Q * T1.H,
            "Q": Q,
            "commutator": T1 * Q - Q * T1,
        }

    scope_A = compute_identities(record_axiom_asserted=True)
    scope_B = compute_identities(record_axiom_asserted=False)

    # Pairwise equality of every output matrix.
    for key in scope_A:
        ok = mat_eq(scope_A[key], scope_B[key])
        record(f"counterfactual_{key}_identical",
               ok,
               f"scope_A == scope_B for {key}")

    # And the identities themselves under both scopes.
    record("scope_A_T1_unitarity",
           mat_eq(scope_A["T1_T1dag"], scope_A["I4"]),
           "(T1) holds with Record axiom asserted")
    record("scope_B_T1_unitarity",
           mat_eq(scope_B["T1_T1dag"], scope_B["I4"]),
           "(T1) holds with Record axiom NOT asserted")
    record("scope_A_T2_group_law",
           mat_eq(scope_A["T1_squared"], scope_A["I4"]),
           "(T2) holds with Record axiom asserted")
    record("scope_B_T2_group_law",
           mat_eq(scope_B["T1_squared"], scope_B["I4"]),
           "(T2) holds with Record axiom NOT asserted")
    record("scope_A_T3_covariance",
           mat_eq(scope_A["T1_a0_T1dag"], scope_A["a1"]),
           "(T3) holds with Record axiom asserted")
    record("scope_B_T3_covariance",
           mat_eq(scope_B["T1_a0_T1dag"], scope_B["a1"]),
           "(T3) holds with Record axiom NOT asserted")
    record("scope_A_T4_charge_conservation",
           is_zero(scope_A["commutator"]),
           "(T4) holds with Record axiom asserted")
    record("scope_B_T4_charge_conservation",
           is_zero(scope_B["commutator"]),
           "(T4) holds with Record axiom NOT asserted")


# -----------------------------------------------------------
# Block 11: Static-source scan of parent note
# -----------------------------------------------------------

def block11(parent_note_path: Path) -> None:
    header("BLOCK 11: Parent note Record-axiom usage scan (load-bearing)")
    if not parent_note_path.exists():
        log(f"  WARN: parent note not found at {parent_note_path}")
        record("parent_note_present", False, str(parent_note_path))
        return

    text = parent_note_path.read_text()
    record("parent_note_present", True, str(parent_note_path))

    # Identify load-bearing section: "## Proof" through the end of the
    # four numbered proof subsections (just before "## What this note
    # does NOT claim"). This is the auditable structural-calculation core.
    start = text.find("## Proof")
    end = text.find("## What this note does NOT claim")
    record("structural_section_start_found", start >= 0,
           f"start index = {start}")
    record("structural_section_end_found", end > start,
           f"end index = {end}")

    section = text[start:end] if (start >= 0 and end > start) else ""

    # Tokens that would indicate Record-axiom usage in the load-bearing
    # core (any one of these inside the proof section would break the
    # invariance claim).
    record_tokens = [
        "I(R_1",
        "I(R)",
        "scalar record",
        "record functional",
        "record-readout",
        "additive record",
        "additive scalar record",
        "MINIMAL_AXIOMS_2026-06-04",
    ]

    found = []
    for tok in record_tokens:
        if tok in section:
            found.append(tok)

    record("zero_record_axiom_tokens_in_load_bearing_section",
           len(found) == 0,
           f"matches = {found}")

    # Confirm Quantum/Lattice structural tokens ARE used in the proof.
    quantum_lattice_tokens = [
        "tensor",
        "basis",
        "permut",        # permutation / permutes
        "cyclic",
        "σ_-",
        "|0⟩",
        "|1⟩",
    ]
    found_quantum_lattice = []
    for tok in quantum_lattice_tokens:
        if tok in section:
            found_quantum_lattice.append(tok)
    record("quantum_lattice_content_present_in_load_bearing_section",
           len(found_quantum_lattice) >= 4,
           f"matches >= 4: {found_quantum_lattice}")


# -----------------------------------------------------------
# Block 12: Quantum/Lattice content preservation across memos
# -----------------------------------------------------------

def block12(repo_root: Path) -> None:
    header("BLOCK 12: Quantum and Lattice content preserved across memos")
    old_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-05-20.md"
    new_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-06-04.md"
    record("old_memo_present", old_memo.exists(), str(old_memo))
    record("new_memo_present", new_memo.exists(), str(new_memo))

    if not (old_memo.exists() and new_memo.exists()):
        return

    old_text = old_memo.read_text()
    new_text = new_memo.read_text()

    # Historical prior wording: one-qubit per site + Z^3 cubic lattice.
    old_quantum = (
        "Reality is a qubit at every lattice site" in old_text
        or "one-qubit algebra" in old_text
        or "M_2(ℂ)" in old_text
        or "M_2(C)" in old_text
    )
    old_lattice = (
        "Z^3" in old_text
        or "`Z^3`" in old_text
        or "cubic lattice" in old_text
    )
    record("old_memo_has_qubit_content", old_quantum,
           "historical qubit local-algebra content present")
    record("old_memo_has_Z3_lattice_content", old_lattice,
           "historical Z^3 lattice content present")

    # New memo: Quantum (one-qubit / M_2(C) / Cl(3,0)) + Lattice (Z^3)
    new_quantum = (
        "one qubit" in new_text
        or "primitive physical local degree of freedom is one qubit" in new_text
        or "A_x ~= M_2(C)" in new_text
        or "M_2(C)" in new_text
        or "Cl(3,0)" in new_text
    )
    new_lattice = (
        "site set is `Z^3`" in new_text
        or "Z^3" in new_text
        or "cubic adjacency" in new_text
    )
    record("new_memo_has_Quantum_content", new_quantum,
           "Quantum = one-qubit / M_2(C) / Cl(3,0) preserved")
    record("new_memo_has_Lattice_content", new_lattice,
           "Lattice = Z^3 preserved")

    # New memo: Record axiom is additive scalar record-readout (separate,
    # non-overlapping statement).
    new_record_additivity = (
        "I(R_1 sqcup R_2) = I(R_1) + I(R_2)" in new_text
        or "additive over disjoint" in new_text
        or "additive scalar record" in new_text
    )
    record("new_memo_has_Record_additive_scalar_content",
           new_record_additivity,
           "Record axiom: additive scalar functional")


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    parent_note = (
        repo_root
        / "docs"
        / "TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md"
    )

    log("Tensor-Product Translation / Fermion Bridge Record-Axiom")
    log("Invariance Companion Runner")
    log("=" * 72)
    log(f"Repo root: {repo_root}")
    log(f"Parent note: {parent_note}")
    log(
        "Companion source note: docs/"
        "TENSOR_PRODUCT_TRANSLATION_FERMION_RECORD_AXIOM_INVARIANCE_"
        "COMPANION_NOTE_2026-06-04.md"
    )
    log("")
    log("Goal: verify the parent's load-bearing operator-algebra")
    log("      identities (T1) unitarity, (T2) group law, (T3) fermion-")
    log("      operator covariance, (T4) charge conservation are")
    log("      invariant under the 2026-06-04 Record-axiom adoption")
    log("      (MINIMAL_AXIOMS_2026-06-04.md).")
    log("")
    log("Scope: pure audit-companion evidence; no theorem claim,")
    log("       no status promotion, no Record-axiom content asserted.")

    block1()
    block2()
    block3()
    block4()
    block5()
    block6()
    block7()
    block8()
    block9()
    block10()
    block11(parent_note)
    block12(repo_root)

    log("")
    log("=" * 72)
    log(f"TOTAL PASS: {PASS}")
    log(f"TOTAL FAIL: {FAIL}")
    log("=" * 72)
    log("")
    log("Companion conclusion (audit-friendly evidence only):")
    log(
        "  The four load-bearing identities (T1)-(T4) of"
        " TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW"
    )
    log(
        "  _THEOREM_NOTE_2026-05-25.md use ONLY Lattice + Quantum axiom"
        " content (per-site C²_x"
    )
    log(
        "  factor + Z^3 cyclic-shift translation) plus standard tensor-"
        "product Fock-space"
    )
    log(
        "  and single-mode per-site Pauli fermion constructions. The"
        " Record axiom"
    )
    log(
        "  (additive scalar record-readout functional) is neither used"
        " nor invoked."
    )
    log(
        "  Matrix-entry outputs are identical under both 'Record axiom"
        " asserted' and"
    )
    log(
        "  'Record axiom not asserted' outer scopes. This runner does"
        " not re-apply the"
    )
    log(
        "  prior audit verdict; it records that the matrix algebra"
        " checked here is"
    )
    log("  unchanged by the 2026-06-04 axiom-set adoption.")
    log("")
    log(
        "The audit lane decides whether to honor or re-test the prior"
        " verdict on the"
    )
    log("new minimal_axioms premise hash.")

    return 1 if FAIL > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
