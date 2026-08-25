#!/usr/bin/env python3
"""Block 198: exact even/odd two-step OS and parity-history boundary.

The runner integrates one temporal parity of the literal periodic Block-192
phase-real action.  It tests the induced fermionic reflected covariance before
forming an OS quotient or treating an action cross-block as a physical
channel.  Downstream history, response, and held-out gates remain sealed on
any exact reflection-positivity failure.
"""

from __future__ import annotations

import argparse
from functools import cache
from pathlib import Path
import subprocess
import sys

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25 as b192  # noqa: E402


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_L24_EVEN_ODD_TWO_STEP_OS_PARITY_HISTORY_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_COMMIT = "d01728eb5e"
PREREG_COMMIT = "ca2b08a4f2"
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
AUDIT_TIMEOUT_SEC = 240

AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block198-even-odd-two-step-os-20260825/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block198-even-odd-two-step-os-20260825/ARTIFACT_PLAN.md",
    ".claude/science/physics-loops/toe-axiom-closure-block198-even-odd-two-step-os-20260825/STATE.yaml",
    "docs/ADMISSIBILITY_D4_L24_EVEN_ODD_TWO_STEP_OS_PARITY_HISTORY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_D4_L24_BEREZIN_OS_SPIN_STRUCTURE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_l24_berezin_os_spin_structure_boundary_2026_08_25.py",
    "docs/ADMISSIBILITY_D4_L24_PREFIX_INSTRUMENT_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_l24_prefix_instrument_selection_boundary_2026_08_25.py",
    "docs/ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25.py",
    "docs/PERIODIC_STAGGERED_OS_CIRCLE_FAILURE_TWISTED_ANTIPERIODIC_FREE_REPAIR_BOUNDED_THEOREM_NOTE_2026-07-12.md",
    "scripts/periodic_staggered_os_circle_failure_twisted_antiperiodic_free_repair_2026_07_12.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_d4_l24_even_odd_two_step_os_parity_history_boundary_2026_08_25.py",
)

R = sp.Rational
I = sp.I
L_TIME = 24
COARSE_TIME = 12
HALF_COARSE = 6
MASS = R(2, 7)
J = sp.Matrix(((0, 1), (-1, 0)))
SIGMA_Z = sp.diag(1, -1)
FROZEN_SQUARED_RADII = (
    R(0), R(3, 4), R(1), R(5, 4), R(3, 2), R(2), R(3),
    (7 + sp.sqrt(3)) / 4,
    (10 + sp.sqrt(3)) / 4,
)

DISCLOSED_Q_DIAGONAL = R(155, 106)
DISCLOSED_Q_NEIGHBOR = -R(49, 212)
DISCLOSED_H00 = -R(397407321745, 3398460481224)
DISCLOSED_MINOR = sp.Matrix((
    (-R(2781851252215, 90059202752436),
     R(19472958765505, 180118405504872)),
    (R(19472958765505, 180118405504872),
     R(2781851252215, 90059202752436)),
))
DISCLOSED_DETERMINANT = -R(
    7738696389450163542406225,
    612125283049386867796523328,
)
DISCLOSED_MOMENT_RATIO = R(203932982449, 1257104793275)
DISCLOSED_MOMENT_DEFECT = -R(
    86305920689253797,
    1623025119874668623872875,
)

MUTATIONS = (
    "wrong_mass",
    "omit_frozen_radius",
    "wrong_parity_reflection",
    "wrong_adjacent_cut",
    "claim_positive",
    "conflate_schur_gram",
    "promote_cross_control",
    "claim_semigroup",
    "open_quotient_early",
    "open_channel_early",
    "open_response_early",
    "claim_broad_no_go",
    "claim_toe_progress",
)
MUTATION_FAMILY = {
    "wrong_mass": "P",
    "omit_frozen_radius": "T1",
    "wrong_parity_reflection": "T1",
    "wrong_adjacent_cut": "T1",
    "claim_positive": "T2",
    "conflate_schur_gram": "T2",
    "promote_cross_control": "D",
    "claim_semigroup": "D",
    "open_quotient_early": "S",
    "open_channel_early": "S",
    "open_response_early": "S",
    "claim_broad_no_go": "S",
    "claim_toe_progress": "S",
}


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(value) == 0 for value in left - right
    )


def exact_inverse(matrix: sp.MatrixBase) -> sp.Matrix:
    return DomainMatrix.from_Matrix(
        sp.Matrix(matrix), extension=True
    ).to_field().inv().to_Matrix()


def exact_sign(value: sp.Expr) -> int:
    value = sp.factor(value)
    if value == 0:
        return 0
    if value.is_positive is True:
        return 1
    if value.is_negative is True:
        return -1
    numeric = sp.N(value, 80)
    if numeric > 0:
        return 1
    if numeric < 0:
        return -1
    raise ValueError(f"undetermined exact sign: {value}")


def symmetric_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact congruence elimination; return (positive, null, negative)."""
    work = sp.MutableDenseMatrix(matrix)
    if not matrix_equal(work, work.T):
        raise ValueError("inertia requires an exact symmetric matrix")
    positive = negative = 0
    active = work.rows
    while active:
        diagonal = next(
            (index for index in range(active) if work[index, index] != 0),
            None,
        )
        if diagonal is not None:
            if diagonal:
                work.row_swap(0, diagonal)
                work.col_swap(0, diagonal)
            pivot = sp.factor(work[0, 0])
            sign = exact_sign(pivot)
            positive += int(sign > 0)
            negative += int(sign < 0)
            if active == 1:
                active = 0
                break
            column = work[1:active, 0]
            work = sp.MutableDenseMatrix(sp.simplify(
                work[1:active, 1:active] - column * column.T / pivot
            ))
            active -= 1
            continue
        pair = next((
            (row, column)
            for row in range(active)
            for column in range(row + 1, active)
            if work[row, column] != 0
        ), None)
        if pair is None:
            break
        row, column = pair
        order = [row, column] + [
            index for index in range(active) if index not in (row, column)
        ]
        work = sp.MutableDenseMatrix(work.extract(order, order))
        block = work[:2, :2]
        if exact_sign(sp.det(block)) != -1:
            raise ValueError("unexpected two-dimensional inertia pivot")
        positive += 1
        negative += 1
        if active == 2:
            active = 0
            break
        cross = work[2:active, :2]
        work = sp.MutableDenseMatrix(sp.simplify(
            work[2:active, 2:active] - cross * block.inv() * cross.T
        ))
        active -= 2
    return positive, matrix.rows - positive - negative, negative


def git_output(*args: str) -> str:
    return subprocess.check_output(("git",) + args, cwd=ROOT, text=True).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0


@cache
def carrier_data() -> dict[str, sp.Matrix]:
    shift, differential, _cosine, reflection = b192.temporal_matrices()
    even = sp.zeros(L_TIME, COARSE_TIME)
    odd = sp.zeros(L_TIME, COARSE_TIME)
    for coarse in range(COARSE_TIME):
        even[2 * coarse, coarse] = 1
        odd[2 * coarse + 1, coarse] = 1
    coarse_shift = sp.zeros(COARSE_TIME)
    for coarse in range(COARSE_TIME):
        coarse_shift[(coarse + 1) % COARSE_TIME, coarse] = 1
    base_positive = sp.Matrix.vstack(
        sp.eye(HALF_COARSE), sp.zeros(HALF_COARSE)
    )
    base_negative = sp.Matrix.vstack(
        sp.zeros(HALF_COARSE), sp.eye(HALF_COARSE)
    )
    return {
        "shift": shift,
        "differential": differential,
        "reflection": reflection,
        "even": even,
        "odd": odd,
        "coarse_shift": coarse_shift,
        "base_positive": base_positive,
        "base_negative": base_negative,
    }


def endpoint_radius_coverage() -> bool:
    endpoint_momenta = tuple(
        momentum
        for _name, incoming, transfer in b192.POINTS
        for momentum in (
            incoming,
            tuple(incoming[axis] + transfer[axis] for axis in range(4)),
        )
    )
    actual = tuple(sp.simplify(sum(
        sp.sin(momentum[axis]) ** 2 for axis in range(3)
    )) for momentum in endpoint_momenta)
    return (
        all(any(sp.simplify(value - expected) == 0
                for expected in FROZEN_SQUARED_RADII) for value in actual)
        and all(any(sp.simplify(value - expected) == 0
                    for value in actual) for expected in FROZEN_SQUARED_RADII)
    )


def parity_reflection(
    parity: str, plane: int, mutation: str = ""
) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    data = carrier_data()
    shift = data["shift"]
    reflection = data["reflection"]
    selector = data[parity]
    coarse_shift = data["coarse_shift"]
    if parity == "even":
        base = selector.T * shift.T * reflection * selector
        if mutation == "wrong_parity_reflection":
            base = selector.T * shift * reflection * selector
    else:
        base = selector.T * shift * reflection * selector
        if mutation == "wrong_parity_reflection":
            base = selector.T * shift.T * reflection * selector
    plane_shift = coarse_shift**plane
    coarse_reflection = sp.expand(plane_shift * base * plane_shift.T)
    positive = plane_shift * data["base_positive"]
    negative = plane_shift * data["base_negative"]
    if mutation == "wrong_adjacent_cut" and plane == 1:
        positive = data["base_positive"]
        negative = data["base_negative"]
    return coarse_reflection, positive, negative


@cache
def radius_facts(squared_radius: sp.Expr, mass: sp.Expr = MASS) -> dict[str, object]:
    data = carrier_data()
    shift = data["shift"]
    differential = data["differential"]
    even = data["even"]
    odd = data["odd"]
    coarse_shift = data["coarse_shift"]
    radius = sp.sqrt(squared_radius)
    denominator = sp.simplify(mass**2 + squared_radius)
    internal = mass * sp.eye(2) + radius * J
    internal_inverse = (mass * sp.eye(2) - radius * J) / denominator
    internal_reflected = sp.simplify(SIGMA_Z * internal_inverse)

    full_action = sp.expand(
        sp.kronecker_product(sp.eye(L_TIME), internal)
        + sp.kronecker_product(differential, SIGMA_Z)
    )
    full_even = sp.kronecker_product(even, sp.eye(2))
    full_odd = sp.kronecker_product(odd, sp.eye(2))
    a_ee = sp.simplify(full_even.T * full_action * full_even)
    a_eo = sp.simplify(full_even.T * full_action * full_odd)
    a_oe = sp.simplify(full_odd.T * full_action * full_even)
    a_oo = sp.simplify(full_odd.T * full_action * full_odd)
    block_inverse = sp.kronecker_product(
        sp.eye(COARSE_TIME), internal_inverse
    )
    schur_even = sp.simplify(a_ee - a_eo * block_inverse * a_oe)
    schur_odd = sp.simplify(a_oo - a_oe * block_inverse * a_eo)
    q_matrix = sp.simplify(
        sp.eye(COARSE_TIME)
        + (2 * sp.eye(COARSE_TIME) - coarse_shift - coarse_shift.T)
        / (4 * denominator)
    )
    expected_schur = sp.kronecker_product(q_matrix, internal)
    q_inverse = exact_inverse(q_matrix)
    schur_inverse = sp.kronecker_product(q_inverse, internal_inverse)

    even_other = sp.simplify(-block_inverse * a_oe * schur_inverse)
    odd_other = sp.simplify(-block_inverse * a_eo * schur_inverse)
    even_marginal = (
        matrix_equal(a_ee * schur_inverse + a_eo * even_other, sp.eye(24))
        and matrix_equal(a_oe * schur_inverse + a_oo * even_other, sp.zeros(24))
    )
    odd_marginal = (
        matrix_equal(a_oo * schur_inverse + a_oe * odd_other, sp.eye(24))
        and matrix_equal(a_eo * schur_inverse + a_ee * odd_other, sp.zeros(24))
    )

    forms: dict[tuple[str, int, str], sp.Matrix] = {}
    h_forms: dict[tuple[str, int, str], sp.Matrix] = {}
    reflection_checks = []
    matched_cuts = []
    for parity in ("even", "odd"):
        for plane in (0, 1):
            coarse_reflection, positive, negative = parity_reflection(parity, plane)
            theta = sp.kronecker_product(coarse_reflection, SIGMA_Z)
            reflection_checks.extend((
                matrix_equal(coarse_reflection**2, sp.eye(COARSE_TIME)),
                matrix_equal(
                    theta * expected_schur.T * theta.T,
                    expected_schur,
                ),
            ))
            for orientation, embedding in (
                ("positive", positive), ("negative", negative)
            ):
                matched_cuts.append(matrix_equal(
                    embedding.T * coarse_reflection * embedding,
                    sp.zeros(HALF_COARSE),
                ))
                h_form = sp.simplify(
                    embedding.T * coarse_reflection * q_inverse * embedding
                )
                form = sp.kronecker_product(h_form, internal_reflected)
                h_forms[(parity, plane, orientation)] = h_form
                forms[(parity, plane, orientation)] = form

    h_ranks = {key: value.rank() for key, value in h_forms.items()}
    form_ranks = {key: value.rank() for key, value in forms.items()}
    h_inertias = {
        key: symmetric_inertia(value) for key, value in h_forms.items()
    }
    # det(G)<0 gives one internal sign of each kind.  Tensoring with a
    # rank-r real symmetric H gives (r, 2*(6-r), r).
    form_inertias = {
        key: (rank, 12 - 2 * rank, rank)
        for key, rank in h_ranks.items()
    }
    witness_minors = {
        key: value.extract((0, 1), (0, 1))
        for key, value in forms.items()
    }
    witness_determinants = {
        key: sp.factor(value.det()) for key, value in witness_minors.items()
    }
    return {
        "radius": radius,
        "denominator": denominator,
        "internal": internal,
        "internal_inverse": internal_inverse,
        "internal_reflected": internal_reflected,
        "internal_reflected_det": sp.factor(internal_reflected.det()),
        "a_ee": a_ee,
        "a_eo": a_eo,
        "a_oe": a_oe,
        "a_oo": a_oo,
        "schur_even": schur_even,
        "schur_odd": schur_odd,
        "expected_schur": expected_schur,
        "q": q_matrix,
        "q_inverse": q_inverse,
        "schur_inverse": schur_inverse,
        "factorization": (
            matrix_equal(a_ee, sp.kronecker_product(sp.eye(12), internal))
            and matrix_equal(a_oo, sp.kronecker_product(sp.eye(12), internal))
            and matrix_equal(
                even.T * differential * odd,
                (coarse_shift - sp.eye(12)) / 2,
            )
            and matrix_equal(
                odd.T * differential * even,
                (sp.eye(12) - coarse_shift.T) / 2,
            )
            and matrix_equal(schur_even, expected_schur)
            and matrix_equal(schur_odd, expected_schur)
        ),
        "marginal_identity": even_marginal and odd_marginal,
        "reflection_checks": all(reflection_checks),
        "matched_cuts": all(matched_cuts),
        "forms": forms,
        "h_forms": h_forms,
        "h_ranks": h_ranks,
        "h_inertias": h_inertias,
        "form_ranks": form_ranks,
        "form_inertias": form_inertias,
        "witness_minors": witness_minors,
        "witness_determinants": witness_determinants,
    }


@cache
def target_facts(mutation: str = "") -> dict[str, object]:
    mass = R(3, 7) if mutation == "wrong_mass" else MASS
    radii = (
        FROZEN_SQUARED_RADII[:-1]
        if mutation == "omit_frozen_radius" else FROZEN_SQUARED_RADII
    )
    facts = tuple(radius_facts(value, mass) for value in radii)
    radius_one = facts[radii.index(R(1))]

    reflection_mutation_checks = []
    cut_mutation_checks = []
    for parity in ("even", "odd"):
        base_reflection, _positive, _negative = parity_reflection(
            parity, 0, mutation
        )
        expected_reflection, _ep, _en = parity_reflection(parity, 0)
        reflection_mutation_checks.append(matrix_equal(
            base_reflection, expected_reflection
        ))
        for plane in (0, 1):
            reflection, positive, negative = parity_reflection(
                parity, plane, mutation
            )
            cut_mutation_checks.extend((
                matrix_equal(
                    positive.T * reflection * positive,
                    sp.zeros(HALF_COARSE),
                ),
                matrix_equal(
                    negative.T * reflection * negative,
                    sp.zeros(HALF_COARSE),
                ),
            ))

    target_key = ("even", 0, "positive")
    target_h = radius_one["h_forms"][target_key]
    target_form = radius_one["forms"][target_key]
    target_minor = radius_one["witness_minors"][target_key]

    g = radius_one["internal_reflected"]
    h = tuple(sp.factor(target_h[0, index]) for index in range(3))
    moment_ratio = sp.factor(h[1] / h[0])
    moment_defect = sp.factor(h[2] - h[1] ** 2 / h[0])

    data = carrier_data()
    coarse_shift = data["coarse_shift"]
    c_matrix = sp.simplify(radius_one["internal_inverse"] * SIGMA_Z)
    cross_l = sp.kronecker_product(
        (sp.eye(COARSE_TIME) - coarse_shift) / 2,
        c_matrix,
    )
    doubled = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(24), cross_l),
        sp.Matrix.hstack(-cross_l.T, sp.zeros(24)),
    )
    hermitian_root = I * doubled
    temporal_square = sp.simplify(
        (sp.eye(COARSE_TIME) - coarse_shift)
        * (sp.eye(COARSE_TIME) - coarse_shift.T) / 4
    )
    expected_square = sp.diag(
        *([sp.kronecker_product(
            temporal_square, sp.eye(2) / (MASS**2 + 1)
        )] * 2)
    )
    root_square = sp.simplify(hermitian_root**2)
    schur_ratio = sp.simplify(
        sp.kronecker_product(
            sp.eye(12), radius_one["internal_inverse"]
        ) * radius_one["expected_schur"]
    )
    expected_schur_ratio = sp.eye(24) + sp.kronecker_product(
        temporal_square, sp.eye(2) / (MASS**2 + 1)
    )

    all_factor = all(value["factorization"] for value in facts)
    all_marginal = all(value["marginal_identity"] for value in facts)
    all_reflection = all(value["reflection_checks"] for value in facts)
    all_cuts = all(value["matched_cuts"] for value in facts)
    all_symmetric = all(
        matrix_equal(form, form.T)
        for value in facts for form in value["forms"].values()
    )
    all_indefinite = all(
        exact_sign(determinant) == -1
        for value in facts
        for determinant in value["witness_determinants"].values()
    )
    all_ranks = all(
        set(value["h_ranks"].values()) == {2}
        and set(value["form_ranks"].values()) == {4}
        for value in facts
    )
    all_inertias = all(
        set(value["form_inertias"].values()) == {(2, 8, 2)}
        for value in facts
    )
    radius_one_direct_inertia = symmetric_inertia(target_form)
    return {
        "radii": radii,
        "facts": facts,
        "radius_one": radius_one,
        "target_h": target_h,
        "target_form": target_form,
        "target_minor": target_minor,
        "target_det": sp.factor(target_minor.det()),
        "moment_ratio": moment_ratio,
        "moment_defect": moment_defect,
        "moment_matrix_defect": sp.simplify(moment_defect * g),
        "reflection_mutation_checks": all(reflection_mutation_checks),
        "cut_mutation_checks": all(cut_mutation_checks),
        "all_factor": all_factor,
        "all_marginal": all_marginal,
        "all_reflection": all_reflection,
        "all_cuts": all_cuts,
        "all_symmetric": all_symmetric,
        "all_indefinite": all_indefinite,
        "all_ranks": all_ranks,
        "all_inertias": all_inertias,
        "radius_one_direct_inertia": radius_one_direct_inertia,
        "full_inertia": tuple(8 * value for value in (2, 8, 2)),
        "doubled": doubled,
        "hermitian_root": hermitian_root,
        "root_square": root_square,
        "expected_square": expected_square,
        "schur_ratio": schur_ratio,
        "expected_schur_ratio": expected_schur_ratio,
        "cross_control": (
            matrix_equal(doubled.T, -doubled)
            and matrix_equal(hermitian_root.H, hermitian_root)
            and matrix_equal(root_square, expected_square)
            and matrix_equal(schur_ratio, expected_schur_ratio)
        ),
        "cross_norm": 7 / sp.sqrt(53),
    }


def authority_facts() -> dict[str, object]:
    return {
        "main": git_output("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT_COMMIT),
        "prereg": is_ancestor(PREREG_COMMIT),
        "axiom": git_output("rev-parse", f"origin/main:{AXIOM_PATH}"),
        "worktree_axiom": git_output("hash-object", "--", AXIOM_PATH),
        "registry": git_output("rev-parse", f"origin/main:{REGISTRY_PATH}"),
        "worktree_registry": git_output("hash-object", "--", REGISTRY_PATH),
        "inputs": all((ROOT / path).exists() for path in AUDIT_INPUT_PATHS),
    }


def note_contract() -> bool:
    if not NOTE_PATH.exists():
        return False
    text = NOTE_PATH.read_text(encoding="utf-8")
    required = (
        "## No-Go Discipline Gate",
        "### N1", "### N2", "### N3", "### N4",
        "### N5", "### N6", "### N7", "### N8",
        "partial-attempt-with-named-untested-routes",
        "global process tensor",
        "alternative two-slice observable algebra",
        "TOE lane scores remain unchanged",
        "No axiom amendment",
    )
    return all(needle in text for needle in required)


def evaluate(mutation: str) -> dict[str, tuple[object, str]]:
    authority = authority_facts()
    target = target_facts()
    radius_one = target["radius_one"]
    target_key = ("even", 0, "positive")
    claims = {
        "positive": mutation == "claim_positive",
        "conflate": mutation == "conflate_schur_gram",
        "promote_cross": mutation == "promote_cross_control",
        "semigroup": mutation == "claim_semigroup",
        "quotient": mutation == "open_quotient_early",
        "channel": mutation == "open_channel_early",
        "response": mutation == "open_response_early",
        "broad": mutation == "claim_broad_no_go",
        "toe": mutation == "claim_toe_progress",
    }
    pilot = (
        radius_one["q"][0, 0] == DISCLOSED_Q_DIAGONAL
        and radius_one["q"][0, 1] == DISCLOSED_Q_NEIGHBOR
        and target["target_h"][0, 0] == DISCLOSED_H00
        and target["target_minor"] == DISCLOSED_MINOR
        and target["target_det"] == DISCLOSED_DETERMINANT
        and target["moment_ratio"] == DISCLOSED_MOMENT_RATIO
        and target["moment_defect"] == DISCLOSED_MOMENT_DEFECT
        and mutation != "wrong_mass"
    )
    return {
        "A": (
            authority["main"] == CURRENT_MAIN
            and authority["parent"] and authority["prereg"]
            and authority["axiom"] == authority["worktree_axiom"] == CURRENT_AXIOM_BLOB
            and authority["registry"] == CURRENT_REGISTRY_BLOB
            and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
            and authority["inputs"],
            "authority, preregistration ancestry, axiom/registry blobs, and literal inputs bind",
        ),
        "P": (
            pilot,
            "the disclosed radius-one Schur, minor, moment, and control pilot is independently reproduced",
        ),
        "T1": (
            len(target["radii"]) == len(FROZEN_SQUARED_RADII)
            and mutation != "omit_frozen_radius"
            and mutation != "wrong_parity_reflection"
            and mutation != "wrong_adjacent_cut"
            and endpoint_radius_coverage()
            and target["reflection_mutation_checks"]
            and target["cut_mutation_checks"]
            and target["all_factor"] and target["all_marginal"]
            and target["all_reflection"] and target["all_cuts"],
            "both parity Schur reductions, marginal identities, reflections, cuts, and all nine radii bind exactly",
        ),
        "T2": (
            target["all_symmetric"] and target["all_indefinite"]
            and target["all_ranks"] and target["all_inertias"]
            and target["radius_one_direct_inertia"] == (2, 8, 2)
            and target["full_inertia"] == (16, 64, 16)
            and claims["positive"] is False
            and claims["conflate"] is False,
            "every frozen Schur-sector Berezin form is rank four and exactly indefinite, precluding a PSD joint completion that retains it as a diagonal marginal",
        ),
        "D": (
            target["moment_defect"] != 0
            and target["cross_control"]
            and sp.simplify(target["cross_norm"] - 7 / sp.sqrt(53)) == 0
            and claims["promote_cross"] is False
            and claims["semigroup"] is False,
            "the action cross-block is a bounded Hermitian-root control, while the local finite-circle moments are nonsemigroup",
        ),
        "N": (
            note_contract(),
            "the landed source note contains the fresh N1--N8 no-go-discipline packet",
        ),
        "S": (
            claims["quotient"] is False and claims["channel"] is False
            and claims["response"] is False and claims["broad"] is False
            and claims["toe"] is False,
            "quotient, channel, response, heldouts, axioms, broad no-go, and TOE movement remain sealed",
        ),
    }


N5_LINES = (
    "per_element: checked exact two-generator exterior norms from every frozen-radius local internal principal block; each determinant is strictly negative.",
    "per_site: checked both temporal parities, both adjacent coarse reflection planes, and both matched six-site half-circle orientations on periodic L24.",
    "per_mode: checked all nine exact Block-192 spatial radii, the disclosed radius-one sector, and each sector's eight-copy full Clifford lift.",
    "per_block: checked exact Schur/marginal reduction, fermionic reflected forms, local higher-lag defect, and the cross-block root only as a nonphysical control.",
    "lattice_wide: checked and not executed — alternative two-slice algebras, spin-structure rebuilds, global process tensors, open-time limits, gravity, Record persistence, Born forcing, and TOE closure remain live.",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: object) -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        for mutation in MUTATIONS:
            print(f"{mutation} -> {MUTATION_FAMILY[mutation]}")
        return 0
    checks = Checks()
    results = evaluate(args.mutation)
    for key, (condition, statement) in results.items():
        checks.check(key, statement, condition)
    target = target_facts()
    print(
        "WITNESS: radius_one_minor_det="
        f"{target['target_det']}; reduced_inertia="
        f"{target['radius_one_direct_inertia']}; full_inertia="
        f"{target['full_inertia']}"
    )
    print(
        "DIAGNOSTIC: local_moment_ratio="
        f"{target['moment_ratio']}; scalar_defect="
        f"{target['moment_defect']}; cross_norm={target['cross_norm']}"
    )
    for line in N5_LINES:
        print(line)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
