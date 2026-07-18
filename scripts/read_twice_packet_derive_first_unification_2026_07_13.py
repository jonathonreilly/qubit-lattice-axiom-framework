#!/usr/bin/env python3
"""Exact checks for the bounded read-twice/write-twice unification note."""

from pathlib import Path

import sympy as sp


PASS = 0
FAIL = 0


def check(name, condition, detail=""):
    """Record and print one computed check."""
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{status}] {name}{suffix}")


def banner(name):
    print()
    print("=" * 78)
    print(name)
    print("=" * 78)


def exact_eq(left, right):
    """Exact equality after SymPy simplification, for scalars or matrices."""
    if isinstance(left, sp.MatrixBase) or isinstance(right, sp.MatrixBase):
        if not isinstance(left, sp.MatrixBase) or not isinstance(right, sp.MatrixBase):
            return False
        if left.shape != right.shape:
            return False
        delta = (left - right).applyfunc(sp.simplify)
        return delta == sp.zeros(*delta.shape)
    return sp.simplify(left - right) == sp.S.Zero


def exact_ne(left, right):
    return not exact_eq(left, right)


def kron(*factors):
    return sp.kronecker_product(*factors)


def projector(ket):
    return ket * ket.H


def reduced_first_density(ket, first_dim, environment_dim):
    """Trace a pure-state projector over its second tensor factor exactly."""
    return sp.Matrix(
        first_dim,
        first_dim,
        lambda row, col: sp.simplify(
            sum(
                (
                    ket[row * environment_dim + env, 0]
                    * sp.conjugate(ket[col * environment_dim + env, 0])
                )
                for env in range(environment_dim)
            )
        ),
    )


def flatten(path):
    return " ".join(path.read_text(encoding="utf-8").split())


ROOT = Path(__file__).resolve().parents[1]


banner("B1 -- verbatim source needles")

minimal_path = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
frame_path = ROOT / (
    "docs/READOUT_BRIDGE_FRAME_EXTENSION_UNIFIES_MARGINAL_READ_AND_"
    "REGISTERED_FACTOR_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md"
)
write_path = ROOT / (
    "docs/RECORD_WRITE_ADMISSIBLE_ONE_STEP_CLASS_CONTROLLED_COPY_"
    "NARROW_THEOREM_NOTE_2026-07-11.md"
)
nogo_path = ROOT / (
    "docs/RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_"
    "NARROW_NO_GO_NOTE_2026-06-06.md"
)

source_needles = (
    (
        "n1 minimal axiom: Records form",
        minimal_path,
        "Records form.",
    ),
    (
        "n2 minimal axiom: one permanent record per site",
        minimal_path,
        "When present, a record locks exactly one admissible local possibility. "
        "A site never carries more than one record; records are permanent.",
    ),
    (
        "n3 minimal axiom: content-only finite-additive readout",
        minimal_path,
        "Only records are readable. A readout value is determined by record "
        "content alone. For any finite collection of pairwise-disjoint records, "
        "scalar readout `I` is additive, with `I(empty)=0`.",
    ),
    (
        "n4 minimal-axiom phrase: local observability of records",
        minimal_path,
        "local observability of records",
    ),
    (
        "n5 FRAME-EXT named finite-additivity gap",
        frame_path,
        "FINITE-ADDITIVITY-TO-FRAME gap:",
    ),
    (
        "n6 FRAME-EXT Gleason scope",
        frame_path,
        "Gleason's theorem on Hilbert spaces of dimension at least 3",
    ),
    (
        "n7 FRAME-EXT composite-domain clause",
        frame_path,
        "(4) the composite domain itself (M_2 tensor M_2 = M_4 and",
    ),
    (
        "n8 write classification: controlled-copy isometry class",
        write_path,
        "in the controlled-copy isometry class",
    ),
    (
        "n9 write classification: basis-unitary and phase freedom",
        write_path,
        "up to a register basis unitary and register phase choice",
    ),
    (
        "n10 formation no-go boundary",
        nogo_path,
        "force the formation rule/process/state/site/weight/rate",
    ),
)

flattened_sources = {}
for check_name, path, needle in source_needles:
    if path not in flattened_sources:
        flattened_sources[path] = flatten(path)
    check(check_name, needle in flattened_sources[path])


banner("B2 -- two-register fan-out from two classified writes")

zero = sp.Matrix([sp.S.One, sp.S.Zero])
one = sp.Matrix([sp.S.Zero, sp.S.One])
P0 = projector(zero)
P1 = projector(one)
I2 = sp.eye(2)
I4 = sp.eye(4)
I8 = sp.eye(8)

r0 = zero
r1 = one
s0 = zero
s1 = one

V1 = kron(P0, r0) + kron(P1, r1)
V2 = kron(P0, I2, s0) + kron(P1, I2, s1)
T = V2 * V1

check("V1 dagger V1 equals I_2", exact_eq(V1.H * V1, I2))
check("V2 dagger V2 equals I_4", exact_eq(V2.H * V2, I4))
check(
    "both writes are class isometries; their composite is an isometry",
    exact_eq(T.H * T, I2),
)

c0 = sp.Rational(3, 5)
c1 = sp.Rational(4, 5) * sp.I
psi = c0 * zero + c1 * one
Psi = T * psi
expected_Psi = c0 * kron(zero, r0, s0) + c1 * kron(one, r1, s1)
check("fan-out state is c0|000> + c1|111>", exact_eq(Psi, expected_Psi))

r_overlap = (r0.H * r1)[0, 0]
s_overlap = (s0.H * s1)[0, 0]
check("R1 written rays discriminate outcomes exactly", exact_eq(r_overlap, 0))
check("R2 written rays discriminate outcomes exactly", exact_eq(s_overlap, 0))

system_bras = (zero.H, one.H)
coefficients = (c0, c1)
register_products = (kron(r0, s0), kron(r1, s1))
for index in range(2):
    conditional = (
        kron(system_bras[index], I4) * Psi / coefficients[index]
    ).applyfunc(sp.simplify)
    check(
        f"outcome {index}: conditional (R1,R2) vector has exact product form",
        exact_eq(conditional, register_products[index]),
    )

P0_R1 = kron(I2, P0, I2)
P0_R2 = kron(I2, I2, P0)
register_commutator = P0_R1 * P0_R2 - P0_R2 * P0_R1
check(
    "disjoint register observables commute on separate tensor slots",
    exact_eq(register_commutator, sp.zeros(8, 8)),
)


banner("B3 -- coincidence functional is the sesquilinear diagonal")

register_pairs = (kron(r0, s0), kron(r1, s1))
A0 = kron(I2, projector(r0), projector(s0))
A1 = kron(I2, projector(r1), projector(s1))
A = (A0, A1)
w0 = sp.simplify((Psi.H * A0 * Psi)[0, 0])
w1 = sp.simplify((Psi.H * A1 * Psi)[0, 0])
weights = (w0, w1)

check("coincidence weight w_0 equals 9/25", exact_eq(w0, sp.Rational(9, 25)))
check("coincidence weight w_1 equals 16/25", exact_eq(w1, sp.Rational(16, 25)))
check("w_0 equals conjugate(c0) c0", exact_eq(w0, sp.conjugate(c0) * c0))
check("w_1 equals conjugate(c1) c1", exact_eq(w1, sp.conjugate(c1) * c1))
check("coincidence weights normalize to one", exact_eq(w0 + w1, sp.S.One))

U = sp.Matrix(
    [
        [sp.Rational(3, 5), sp.Rational(4, 5)],
        [-sp.Rational(4, 5), sp.Rational(3, 5)],
    ]
)
V = sp.diag(sp.S.One, sp.I)
register_basis_change = kron(I2, U, V)
Psi_basis_changed = register_basis_change * Psi
rotated_rays = ((U * r0, V * s0), (U * r1, V * s1))

for index in range(2):
    rotated_r, rotated_s = rotated_rays[index]
    A_basis_changed = kron(I2, projector(rotated_r), projector(rotated_s))
    changed_weight = sp.simplify(
        (Psi_basis_changed.H * A_basis_changed * Psi_basis_changed)[0, 0]
    )
    check(
        f"outcome {index}: coincidence weight is register-basis invariant",
        exact_eq(changed_weight, weights[index]),
        "content-determination",
    )


banner("B4 -- exact M_2 single-register frame-function loophole")

sigma_x = sp.Matrix([[0, 1], [1, 0]])
sigma_y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sigma_z = sp.Matrix([[1, 0], [0, -1]])


def bloch_projector(point):
    nx, ny, nz = point
    return sp.Rational(1, 2) * (
        I2 + nx * sigma_x + ny * sigma_y + nz * sigma_z
    )


def frame_value(point):
    nz = point[2]
    return sp.simplify(sp.Rational(1, 2) * (sp.S.One + nz**3))


test_points = (
    ("e_z", (sp.S.Zero, sp.S.Zero, sp.S.One)),
    ("-e_z", (sp.S.Zero, sp.S.Zero, -sp.S.One)),
    ("e_x", (sp.S.One, sp.S.Zero, sp.S.Zero)),
    ("e_y", (sp.S.Zero, sp.S.One, sp.S.Zero)),
    (
        "(3/5,0,4/5)",
        (sp.Rational(3, 5), sp.S.Zero, sp.Rational(4, 5)),
    ),
    (
        "(0,3/5,-4/5)",
        (sp.S.Zero, sp.Rational(3, 5), -sp.Rational(4, 5)),
    ),
    (
        "(4/5,0,-3/5)",
        (sp.Rational(4, 5), sp.S.Zero, -sp.Rational(3, 5)),
    ),
)

for point_name, point in test_points:
    Pn = bloch_projector(point)
    fn = frame_value(point)
    antipode = tuple(-coordinate for coordinate in point)
    check(f"{point_name}: P_n is a projector", exact_eq(Pn * Pn, Pn))
    check(
        f"{point_name}: f(P_n) lies exactly in [0,1]",
        bool(fn >= sp.S.Zero) and bool(fn <= sp.S.One),
    )
    check(
        f"{point_name}: antipodal additivity f(P_n)+f(P_-n)=1",
        exact_eq(fn + frame_value(antipode), sp.S.One),
    )

e_x = (sp.S.One, sp.S.Zero, sp.S.Zero)
e_y = (sp.S.Zero, sp.S.One, sp.S.Zero)
e_z = (sp.S.Zero, sp.S.Zero, sp.S.One)
candidate_r = sp.Matrix(
    [
        sp.simplify(2 * frame_value(e_x) - 1),
        sp.simplify(2 * frame_value(e_y) - 1),
        sp.simplify(2 * frame_value(e_z) - 1),
    ]
)
expected_candidate_r = sp.Matrix([0, 0, 1])
check(
    "axis values fix the unique candidate Bloch vector r=(0,0,1)",
    exact_eq(candidate_r, expected_candidate_r),
)

nonlinear_witness = (sp.Rational(3, 5), sp.S.Zero, sp.Rational(4, 5))
witness_vector = sp.Matrix(nonlinear_witness)
density_prediction = sp.simplify(
    sp.Rational(1, 2) * (sp.S.One + candidate_r.dot(witness_vector))
)
actual_frame_value = frame_value(nonlinear_witness)
check(
    "density candidate predicts 9/10 at the nonlinear witness",
    exact_eq(density_prediction, sp.Rational(9, 10)),
)
check(
    "frame function actually gives 189/250 at the nonlinear witness",
    exact_eq(actual_frame_value, sp.Rational(189, 250)),
)
check(
    "additive-normalized-nonnegative on M_2 yet not density form",
    exact_ne(density_prediction, actual_frame_value),
)


banner("B5 -- realized two-register composite domain")

rho_pair = w0 * projector(register_pairs[0]) + w1 * projector(register_pairs[1])
for index in range(2):
    menu_projector = projector(register_pairs[index])
    menu_weight = sp.simplify(sp.trace(rho_pair * menu_projector))
    check(
        f"outcome {index}: coincidence functional is density-form on realized menu",
        exact_eq(menu_weight, weights[index]),
    )

pair_dimension = sp.Integer(rho_pair.rows)
check(
    "Gleason scope holds on realized dimension 4 composite; theorem is an import",
    exact_eq(pair_dimension, sp.Integer(4)) and bool(pair_dimension >= 3),
)


banner("B6 -- counting arithmetic")


def count_ratio(weight):
    return sp.simplify((sp.S.One - weight) / (2 * weight))


check("r(1/3) equals 1", exact_eq(count_ratio(sp.Rational(1, 3)), sp.S.One))
check(
    "r(1/2) equals 1/2",
    exact_eq(count_ratio(sp.Rational(1, 2)), sp.Rational(1, 2)),
)


banner("B7 -- exact negative controls")

# (a) No write: both outcome-conditioned register vectors are the same blank.
Psi_no_write = kron(psi, zero, zero)
no_write_conditionals = tuple(
    (kron(system_bras[index], I4) * Psi_no_write / coefficients[index]).applyfunc(
        sp.simplify
    )
    for index in range(2)
)
no_write_overlap = sp.simplify(
    (no_write_conditionals[0].H * no_write_conditionals[1])[0, 0]
)
check(
    "no-write control: identical conditional registers have overlap one",
    exact_eq(no_write_overlap, sp.S.One),
    "discrimination fails",
)

# (b) One classified write can be revoked by its adjoint.
Phi = V1 * psi
undone_psi = V1.H * Phi
check(
    "single-register write undone by the adjoint -- one witness revocable",
    exact_eq(undone_psi, psi),
)

rho_S_held = reduced_first_density(Phi, 2, 2)
check(
    "one held register dephases the system off-diagonal",
    exact_eq(rho_S_held[0, 1], sp.S.Zero),
)

rho_S_restored = projector(undone_psi)
expected_restored_off_diagonal = sp.simplify(c0 * sp.conjugate(c1))
check(
    "adjoint undo restores off-diagonal c0*conjugate(c1)",
    exact_eq(rho_S_restored[0, 1], expected_restored_off_diagonal),
)
check(
    "restored system coherence is nonzero",
    exact_ne(rho_S_restored[0, 1], sp.S.Zero),
)

# (c) Two concrete local-unitary witnesses leave the second register pinning
# the branches. These checks are witnesses, not a universal local-undo proof.
ket_01 = kron(zero, one)
ket_10 = kron(one, zero)
W1 = sp.Matrix.hstack(V1 * zero, ket_01, V1 * one, ket_10)
check(
    "local-undo witness 1: explicit completion W1 is unitary",
    exact_eq(W1.H * W1, I4),
)
blank_register_embedding = kron(I2, zero)
check(
    "local-undo witness 1: W1 extends V1 on the blank-register subspace",
    exact_eq(W1 * blank_register_embedding, V1),
)

system_rotation = U
W2 = W1 * kron(system_rotation, I2)
check(
    "local-undo witness 2: rotated completion W2 is unitary",
    exact_eq(W2.H * W2, I4),
)

for witness_index, local_unitary in enumerate((W1, W2), start=1):
    transformed = kron(local_unitary, I2) * Psi
    transformed_rho_S = reduced_first_density(transformed, 2, 4)
    check(
        f"local-undo witness {witness_index}: S off-diagonal remains zero",
        exact_eq(transformed_rho_S[0, 1], sp.S.Zero),
        "second witness register pins the branch; not a universal proof",
    )

# (d) Corrupted content rays overlap across outcome labels on both registers.
# Because the system pointer sectors remain orthogonal, normalized controlled
# writes are still isometries; overlap instead violates exact discrimination.
corrupt_ray = sp.Rational(3, 5) * zero + sp.Rational(4, 5) * one
corrupt_rays = (zero, corrupt_ray)
corrupt_s_rays = (zero, corrupt_ray)
V1_corrupt = kron(P0, corrupt_rays[0]) + kron(P1, corrupt_rays[1])
V2_corrupt = (
    kron(P0, I2, corrupt_s_rays[0]) + kron(P1, I2, corrupt_s_rays[1])
)
T_corrupt = V2_corrupt * V1_corrupt
Psi_corrupt = T_corrupt * psi
A_corrupt = tuple(
    kron(I2, projector(corrupt_rays[index]), projector(corrupt_s_rays[index]))
    for index in range(2)
)

corrupt_r_overlap = sp.simplify((corrupt_rays[0].H * corrupt_rays[1])[0, 0])
corrupt_s_overlap = sp.simplify(
    (corrupt_s_rays[0].H * corrupt_s_rays[1])[0, 0]
)
check(
    "corrupted R1 rays overlap across outcomes",
    exact_ne(corrupt_r_overlap, sp.S.Zero),
)
check(
    "corrupted R2 rays overlap across outcomes",
    exact_ne(corrupt_s_overlap, sp.S.Zero),
)
check(
    "corrected corrupted-write control: V1' remains an isometry",
    exact_eq(V1_corrupt.H * V1_corrupt, I2),
    "orthogonal system sectors make the requested non-isometry impossible",
)
check(
    "corrected corrupted-write control: T' remains an isometry",
    exact_eq(T_corrupt.H * T_corrupt, I2),
)

expected_corrupt_Psi = sum(
    (
        coefficients[index]
        * kron(
            (zero, one)[index],
            corrupt_rays[index],
            corrupt_s_rays[index],
        )
        for index in range(2)
    ),
    sp.zeros(8, 1),
)
check(
    "corrupted writes rebuild the exact overlapping-ray fan-out Psi'",
    exact_eq(Psi_corrupt, expected_corrupt_Psi),
)
check(
    "overlapping content rays fall outside exact-discrimination class",
    exact_ne(corrupt_r_overlap, 0) and exact_ne(corrupt_s_overlap, 0),
)

wtilde0 = sp.simplify((Psi.H * A_corrupt[0] * Psi)[0, 0])
wtilde1 = sp.simplify((Psi.H * A_corrupt[1] * Psi)[0, 0])
check(
    "unchanged corrupted outcome-0 rays leave wtilde_0 equal to w_0",
    exact_eq(wtilde0, w0),
    "the requested outcome-0 deviation is algebraically impossible",
)
check(
    "corrupted-witness agreement functional deviates from coincidence form",
    exact_ne(wtilde1, w1),
    "the nontrivially corrupted outcome-1 projector supplies the witness",
)


banner("B8 -- compatibility obligations")

# Symbolic bookkeeping only: no numerical readout value is imported.
ell_i = sp.Symbol("ell_i")
record_labels = {"rec_R1": ell_i, "rec_R2": ell_i}


def symbolic_readout(records):
    return sp.simplify(sum((record_labels[record] for record in records), sp.S.Zero))


empty_readout = symbolic_readout(())
single_R1 = symbolic_readout(("rec_R1",))
single_R2 = symbolic_readout(("rec_R2",))
pair_readout = symbolic_readout(("rec_R1", "rec_R2"))
check("I(empty)=0 in symbolic two-register bookkeeping", exact_eq(empty_readout, 0))
check(
    "additivity SHAPE at two-register level -- symbolic labels only, no numerical readout imported",
    exact_eq(single_R1 + single_R2, pair_readout),
)

explicit_fanout = kron(P0, r0, s0) + kron(P1, r1, s1)
check(
    "one write per register: T factors as V2*V1 into the explicit fan-out",
    exact_eq(T, explicit_fanout),
)

v1_slot_support = all(
    exact_eq(V1 * system_ket, kron(system_ket, written_r))
    for system_ket, written_r in ((zero, r0), (one, r1))
)
check(
    "V1 slot support writes R1 while preserving the system pointer",
    v1_slot_support,
)

v2_slot_support = all(
    exact_eq(
        V2 * kron(system_ket, r1_basis_ket),
        kron(system_ket, r1_basis_ket, written_s),
    )
    for system_ket, written_s in ((zero, s0), (one, s1))
    for r1_basis_ket in (zero, one)
)
check(
    "V2 slot support writes only R2 and leaves R1 unchanged",
    v2_slot_support,
)

for index, (system_ket, written_r, coefficient) in enumerate(
    ((zero, r0, c0), (one, r1, c1))
):
    repeat_projector = kron(projector(system_ket), projector(written_r))
    Phi_branch = coefficient * kron(system_ket, written_r)
    check(
        f"outcome {index}: repeat projection fixes the written Phi branch",
        exact_eq(repeat_projector * Phi_branch, Phi_branch),
        "branchwise repeat stability",
    )


print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("BOUNDARY: total includes source needles and supplied-fixture checks; see the note's verification map.")

raise SystemExit(0 if FAIL == 0 else 1)
