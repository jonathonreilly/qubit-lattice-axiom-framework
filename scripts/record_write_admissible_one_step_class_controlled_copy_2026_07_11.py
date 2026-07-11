#!/usr/bin/env python3
"""Exact checks for the admissible one-step controlled-copy class note."""

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
MEMO = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
CONTROLLED_COPY = (
    ROOT
    / "docs"
    / "RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md"
)
KRAUS_BRIDGE = (
    ROOT / "docs" / "RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md"
)

pass_count = 0
fail_count = 0


def flatten(text):
    return " ".join(text.split())


def scalar_zero(expr):
    reduced = sp.trigsimp(sp.simplify(sp.expand_complex(expr)))
    return reduced == sp.Integer(0)


def matrix_equal(left, right):
    difference = sp.Matrix(left) - sp.Matrix(right)
    return all(scalar_zero(entry) for entry in difference)


def check(label, condition):
    global pass_count, fail_count
    outcome = bool(condition)
    if outcome:
        pass_count += 1
        print(f"PASS {label}")
    else:
        fail_count += 1
        print(f"FAIL {label}")


I = sp.I
I2 = sp.eye(2)
e0 = sp.Matrix([1, 0])
e1 = sp.Matrix([0, 1])
P0 = e0 * e0.T
P1 = e1 * e1.T
Q0 = sp.kronecker_product(P0, I2)
Q1 = sp.kronecker_product(P1, I2)


# R1: the note's four quotations are verbatim Record-memo text.
memo_flat = flatten(MEMO.read_text(encoding="utf-8"))
record_clauses = (
    (
        "C1",
        "When present, a record locks exactly one admissible local possibility.",
    ),
    (
        "C2",
        "A site never carries more than one record; records are permanent.",
    ),
    (
        "C3",
        "Only records are readable. A readout value is determined by record content alone.",
    ),
    (
        "C4",
        "For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`.",
    ),
)
for clause_label, clause_text in record_clauses:
    check(
        f"R1 {clause_label} quotation occurs verbatim in the flattened memo",
        flatten(clause_text) in memo_flat,
    )


# R2: solve C3 on a fully general joint 4 x 4 operator, restricted to |b>.
# A register basis change sets the blank to e0 for this calculation.
g = sp.symbols("g0:16", complex=1)
K_general = sp.Matrix(4, 4, g)
B_blank = sp.kronecker_product(I2, e0)
A_blank = K_general * B_blank

# Pointer non-demolition forbids P0 -> P1 and P1 -> P0 system blocks.
c3_matrices = (Q1 * A_blank * P0, Q0 * A_blank * P1)
c3_equations = [
    sp.expand(entry)
    for matrix in c3_matrices
    for entry in matrix
    if entry != sp.Integer(0)
]
c3_coefficients, c3_rhs = sp.linear_eq_to_matrix(c3_equations, g)
c3_solution_set = sp.linsolve((c3_coefficients, c3_rhs), g)
c3_solution = next(iter(c3_solution_set))
c3_substitution = dict(zip(g, c3_solution))
A_c3 = A_blank.subs(c3_substitution)

v0_general = sp.Matrix([g[0], g[4]])
v1_general = sp.Matrix([g[10], g[14]])
A_c3_expected = sp.kronecker_product(P0, v0_general) + sp.kronecker_product(
    P1, v1_general
)

check(
    "R2 C3 has four independent blank-input demolition constraints",
    c3_coefficients.rank() == sp.Integer(4),
)
check(
    "R2 symbolic solution has exactly the two conditional register vectors",
    matrix_equal(A_c3, A_c3_expected),
)
check(
    "R2 the surviving blank-input parameters are precisely v_0 and v_1",
    A_c3.free_symbols == {g[0], g[4], g[10], g[14]},
)
check(
    "R2 the solved family has zero off-diagonal pointer blocks",
    matrix_equal(Q1 * A_c3 * P0, sp.zeros(4, 2))
    and matrix_equal(Q0 * A_c3 * P1, sp.zeros(4, 2)),
)


# R3: impose the declared C1 reading and blank-input normalization.
z00, z01, z10, z11 = sp.symbols("z00 z01 z10 z11", complex=1)
v0_raw = sp.Matrix([z00, z01])
v1_raw = sp.Matrix([z10, z11])
V_raw = sp.kronecker_product(P0, v0_raw) + sp.kronecker_product(P1, v1_raw)
n0_raw = (v0_raw.H * v0_raw)[0]
n1_raw = (v1_raw.H * v1_raw)[0]

check(
    "R3 blank-input completeness reduces to the two conditional norms",
    matrix_equal(V_raw.H * V_raw, sp.diag(n0_raw, n1_raw)),
)

n0_symbol, n1_symbol = sp.symbols("n0_symbol n1_symbol", real=1)
normalization_solution = sp.solve(
    (n0_symbol - 1, n1_symbol - 1),
    (n0_symbol, n1_symbol),
    dict=1,
)
check(
    "R3 trace preservation forces both conditional norms to one",
    normalization_solution
    == [{n0_symbol: sp.Integer(1), n1_symbol: sp.Integer(1)}],
)

# This is a general two-vector orthonormal frame, including both column phases.
theta, alpha, beta, gamma = sp.symbols(
    "theta alpha beta gamma", real=1
)
r0 = sp.exp(I * beta) * sp.Matrix(
    [sp.cos(theta), sp.exp(I * alpha) * sp.sin(theta)]
)
r1 = sp.exp(I * gamma) * sp.Matrix(
    [-sp.exp(-I * alpha) * sp.sin(theta), sp.cos(theta)]
)
V = sp.kronecker_product(P0, r0) + sp.kronecker_product(P1, r1)

check(
    "R3 C1 gives perfectly distinguishable conditional register vectors",
    scalar_zero((r0.H * r1)[0]),
)
check(
    "R3 the C1 register frame is normalized",
    scalar_zero((r0.H * r0)[0] - 1)
    and scalar_zero((r1.H * r1)[0] - 1),
)
check(
    "R3 the resulting controlled-copy block column is an isometry",
    matrix_equal(V.H * V, I2),
)

# The flagged C1 reading excludes a possibility-dependent hidden Kraus label.
# Thus every blank-input family member is a common scalar times the same V.
kraus_angle, kraus_phase0, kraus_phase1 = sp.symbols(
    "kraus_angle kraus_phase0 kraus_phase1", real=1
)
c0 = sp.exp(I * kraus_phase0) * sp.cos(kraus_angle)
c1 = sp.exp(I * kraus_phase1) * sp.sin(kraus_angle)
coefficient_norm = sp.conjugate(c0) * c0 + sp.conjugate(c1) * c1
A0 = c0 * V
A1 = c1 * V

check(
    "R3 the normalized common-vector Kraus completeness is identity",
    scalar_zero(coefficient_norm - 1)
    and matrix_equal(A0.H * A0 + A1.H * A1, I2),
)

rho_symbols = sp.symbols("rho00 rho01 rho10 rho11", complex=1)
rho = sp.Matrix(2, 2, rho_symbols)
family_output = A0 * rho * A0.H + A1 * rho * A1.H
check(
    "R3 the declared rank-one Kraus family is exactly the V channel",
    matrix_equal(family_output, V * rho * V.H),
)

# This exact witness explains why the flagged C1 rank-one reading is needed.
D0 = sp.kronecker_product(P0, e0)
D1 = sp.kronecker_product(P1, e1)
check(
    "R3 weaker constraints admit a dephasing family excluded by declared C1",
    matrix_equal(D0.H * D0 + D1.H * D1, I2)
    and not matrix_equal(
        D0 * rho * D0.H + D1 * rho * D1.H,
        (D0 + D1) * rho * (D0 + D1).H,
    ),
)


# R4: C2 fixes each already-written record ray (phase is immaterial).
label0 = e0
label1 = e1
W_canonical = sp.kronecker_product(P0, label0) + sp.kronecker_product(
    P1, label1
)
q0 = sp.kronecker_product(e0, label0)
q1 = sp.kronecker_product(e1, label1)
rho_q0 = q0 * q0.H
rho_q1 = q1 * q1.H


def apply_channel(kraus_family, state):
    output = sp.zeros(state.rows, state.cols)
    for operator in kraus_family:
        output += operator * state * operator.H
    return output


# This CPTP extension is used only to certify the action on admissible matched
# written branches; no uniqueness is asserted away from those branches.
L0 = sp.kronecker_product(P0, label0 * e0.T) + sp.kronecker_product(
    P1, label1 * e0.T
)
L1 = sp.kronecker_product(P0, label0 * e1.T) + sp.kronecker_product(
    P1, label1 * e1.T
)
repeat_family = (L0, L1)

check(
    "R4 a trace-preserving repeat extension exists",
    matrix_equal(L0.H * L0 + L1.H * L1, sp.eye(4)),
)
check(
    "R4 repeat application fixes the written P_0 record",
    matrix_equal(apply_channel(repeat_family, rho_q0), rho_q0),
)
check(
    "R4 repeat application fixes the written P_1 record",
    matrix_equal(apply_channel(repeat_family, rho_q1), rho_q1),
)

mix = sp.symbols("mix", real=1)
written_mixture = mix * rho_q0 + (1 - mix) * rho_q1
check(
    "R4 the classical written-record sector is idempotently stable",
    matrix_equal(
        apply_channel(repeat_family, written_mixture), written_mixture
    ),
)

# On a one-dimensional record ray, no leakage fixes the content uniquely;
# normalization leaves only a phase.
xr, xi, yr, yi = sp.symbols("xr xi yr yi", real=1)
generic_record_output = (xr + I * xi) * label0 + (yr + I * yi) * label1
leakage = (label1.T * generic_record_output)[0]
no_leakage_solution = sp.solve(
    (sp.re(leakage), sp.im(leakage)), (yr, yi), dict=1
)
check(
    "R4 C2 leaves no cross-record component on a fixed record ray",
    no_leakage_solution == [{yr: sp.Integer(0), yi: sp.Integer(0)}],
)

record_phase = sp.symbols("record_phase", real=1)
phase_shifted_label = sp.exp(I * record_phase) * label0
check(
    "R4 the remaining phase freedom fixes the record content projector",
    matrix_equal(phase_shifted_label * phase_shifted_label.H, P0),
)

# A reset-to-blank channel is CPTP but fails permanence on both written rays.
blank_record = (label0 + label1) / sp.sqrt(2)
E0 = sp.kronecker_product(I2, blank_record * label0.T)
E1 = sp.kronecker_product(I2, blank_record * label1.T)
eraser_family = (E0, E1)
erased_q0 = apply_channel(eraser_family, rho_q0)
erased_q1 = apply_channel(eraser_family, rho_q1)

check(
    "R4 the eraser negative control is a normalized channel",
    matrix_equal(E0.H * E0 + E1.H * E1, sp.eye(4)),
)
check(
    "R4 the eraser moves written content back to the blank ray",
    (not matrix_equal(erased_q0, rho_q0))
    and (not matrix_equal(erased_q1, rho_q1)),
)


# R5: all orthonormal record frames lie in one register-unitary orbit.
U_register = sp.Matrix.hstack(r0, r1)
check(
    "R5 the general record-frame matrix is unitary",
    matrix_equal(U_register.H * U_register, I2),
)

rotated_write = sp.kronecker_product(I2, U_register) * W_canonical
expected_rotated_write = sp.kronecker_product(
    P0, U_register * label0
) + sp.kronecker_product(P1, U_register * label1)
check(
    "R5 register-unitary conjugation preserves the controlled-copy class",
    matrix_equal(rotated_write, expected_rotated_write),
)
check(
    "R5 the unitary orbit sends the canonical labels to the general pair",
    matrix_equal(U_register * label0, r0)
    and matrix_equal(U_register * label1, r1),
)


# R6: negative controls must be rejected by the named constraints.
noncorrelating_v0 = label0
noncorrelating_v1 = label0
noncorrelating_overlap = (noncorrelating_v0.H * noncorrelating_v1)[0]
check(
    "R6a a non-correlating write is rejected by C1",
    not scalar_zero(noncorrelating_overlap),
)

pointer_flip_10 = e1 * e0.T
demolition_write = sp.kronecker_product(
    pointer_flip_10, label0
) + sp.kronecker_product(P1, label1)
demolition_block = Q1 * demolition_write * P0
check(
    "R6b a pointer-demolishing write is rejected by C3",
    not matrix_equal(demolition_block, sp.zeros(4, 2)),
)

check(
    "R6c an eraser is rejected by C2",
    (not matrix_equal(erased_q0, rho_q0))
    and (not matrix_equal(erased_q1, rho_q1)),
)

contraction = sp.Rational(1, 2)
contracting_write = sp.kronecker_product(
    P0, contraction * label0
) + sp.kronecker_product(P1, label1)
contracted_input_norm = (
    e0.H * contracting_write.H * contracting_write * e0
)[0]
check(
    "R6d a non-isometric contraction is rejected by normalization",
    not scalar_zero(contracted_input_norm - 1),
)


# R7: consumed audited-row surfaces are present verbatim.
controlled_copy_flat = flatten(CONTROLLED_COPY.read_text(encoding="utf-8"))
kraus_bridge_flat = flatten(KRAUS_BRIDGE.read_text(encoding="utf-8"))
controlled_copy_scope_quote = flatten(
    "In the explicit finite pointer-record model of "
    "[`RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`]"
    "(RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md), "
    "the nonzero controlled-copy kick on a fresh blank fragment derives the "
    "projective record-write isometry used by the target bridge "
    "`RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md`."
)
kraus_bridge_scope_quote = flatten(
    "The extracted blocks are exactly projective Kraus operators: "
    "`K_r = <r| W = P_r`."
)
check(
    "R7 controlled-copy dependency states the derived write-isometry surface",
    controlled_copy_scope_quote in controlled_copy_flat,
)
check(
    "R7 Kraus dependency states the projective extracted-block form",
    kraus_bridge_scope_quote in kraus_bridge_flat,
)


print(f"TOTAL: PASS={pass_count} FAIL={fail_count}")
raise SystemExit(1 if fail_count else 0)
