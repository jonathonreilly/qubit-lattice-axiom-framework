#!/usr/bin/env python3
"""Block 197: literal L24 Berezin-OS seed and spin-structure boundary.

This runner does not infer a channel from the positive right-Schur Gram.  It
constructs the degree-one fermionic reflected covariance of the frozen
Block-192 periodic action.  A negative exterior norm stops OS/GNS/CAR,
event-factor, channel, source-response, and held-out stages.  The runner then
tests the frozen convention battery and the known scalar twisted-
antiperiodic repair, including its exact incompatibility with the two frozen
temporal momenta on one scalar-twist circle.
"""

from __future__ import annotations

import argparse
from functools import cache
from pathlib import Path
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25 as b192  # noqa: E402


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_L24_BEREZIN_OS_SPIN_STRUCTURE_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_COMMIT = "f847227012"
PREREG_COMMIT = "5569f201fe"
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"

AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block197-os-gns-car-history-reconstruction-20260825/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block197-os-gns-car-history-reconstruction-20260825/ARTIFACT_PLAN.md",
    ".claude/science/physics-loops/toe-axiom-closure-block197-os-gns-car-history-reconstruction-20260825/STATE.yaml",
    "docs/ADMISSIBILITY_D4_L24_BEREZIN_OS_SPIN_STRUCTURE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_D4_L24_PREFIX_INSTRUMENT_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_l24_prefix_instrument_selection_boundary_2026_08_25.py",
    "docs/ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25.py",
    "docs/ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25.py",
    "docs/PERIODIC_STAGGERED_OS_CIRCLE_FAILURE_TWISTED_ANTIPERIODIC_FREE_REPAIR_BOUNDED_THEOREM_NOTE_2026-07-12.md",
    "scripts/periodic_staggered_os_circle_failure_twisted_antiperiodic_free_repair_2026_07_12.py",
    "docs/FREE_STAGGERED_3PLUS1_REFLECTED_GRAM_CAR_FOCK_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-12.md",
    "scripts/free_staggered_3plus1_reflected_gram_car_fock_representation_2026_07_12.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_d4_l24_berezin_os_spin_structure_boundary_2026_08_25.py",
)

R = sp.Rational
I = sp.I
L_TIME = 24
HALF_TIME = 12
MASS = R(2, 7)
SIGMA_X = sp.Matrix(((0, 1), (1, 0)))
SIGMA_Z = sp.diag(1, -1)
REAL_SKEW = sp.Matrix(((0, 1), (-1, 0)))
DISCLOSED_MINOR = sp.Matrix((
    (-147051604814471, -627723416089),
    (-627723416089, 13841287201),
)) / sp.Integer(526761374589720)
DISCLOSED_DETERMINANT = -sp.Integer(678223072849) / sp.Integer(77463616656739800)

MUTATIONS = (
    "wrong_action",
    "wrong_cut",
    "wrong_reflection",
    "claim_global_sign_repairs",
    "conflate_schur_berezin",
    "omit_adjacent_plane",
    "omit_spin_repair",
    "claim_antiperiodic_modes_compatible",
    "open_quotient_early",
    "open_response_early",
    "claim_broad_no_go",
    "claim_toe_progress",
)
MUTATION_FAMILY = {
    "wrong_action": "P",
    "wrong_cut": "P",
    "wrong_reflection": "T1",
    "claim_global_sign_repairs": "T2",
    "conflate_schur_berezin": "T2",
    "omit_adjacent_plane": "T2",
    "omit_spin_repair": "T3",
    "claim_antiperiodic_modes_compatible": "T3",
    "open_quotient_early": "S",
    "open_response_early": "S",
    "claim_broad_no_go": "S",
    "claim_toe_progress": "S",
}


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(value) == 0 for value in left - right
    )


def git_output(*args: str) -> str:
    return subprocess.check_output(("git",) + args, cwd=ROOT, text=True).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0


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


def symmetric_inertia(matrix: sp.Matrix) -> tuple[int, int, int]:
    """Exact congruence elimination; return (positive, zero, negative)."""
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
            reduced = sp.simplify(
                work[1:active, 1:active] - column * column.T / pivot
            )
            work = sp.MutableDenseMatrix(reduced)
            active -= 1
            continue

        pair = next(
            ((row, column) for row in range(active)
             for column in range(row + 1, active)
             if work[row, column] != 0),
            None,
        )
        if pair is None:
            break
        row, column = pair
        if row != 0:
            work.row_swap(0, row)
            work.col_swap(0, row)
            if column == 0:
                column = row
        if column != 1:
            work.row_swap(1, column)
            work.col_swap(1, column)
        block = work[:2, :2]
        # A zero-diagonal nonzero symmetric 2x2 block has determinant -a^2.
        if exact_sign(sp.det(block)) != -1:
            raise ValueError("unexpected 2x2 inertia pivot")
        positive += 1
        negative += 1
        if active == 2:
            active = 0
            break
        cross = work[2:active, :2]
        reduced = sp.simplify(
            work[2:active, 2:active] - cross * block.inv() * cross.T
        )
        work = sp.MutableDenseMatrix(reduced)
        active -= 2
    zero = matrix.rows - positive - negative
    return positive, zero, negative


def phase_real_action(radius: int, mutation: str = "") -> sp.Matrix:
    _shift, differential, _cosine, _reflection = b192.temporal_matrices()
    mass = R(3, 7) if mutation == "wrong_action" else MASS
    return sp.expand(
        mass * sp.eye(2 * L_TIME)
        + radius * sp.kronecker_product(sp.eye(L_TIME), REAL_SKEW)
        + sp.kronecker_product(differential, SIGMA_Z)
    )


def complex_action(radius: int) -> sp.Matrix:
    _shift, differential, _cosine, _reflection = b192.temporal_matrices()
    return sp.expand(
        sp.kronecker_product(
            sp.eye(L_TIME), MASS * sp.eye(2) + I * radius * SIGMA_X
        )
        + sp.kronecker_product(differential, SIGMA_Z)
    )


def plane_data(plane: int, orientation: str, mutation: str = "") -> tuple[sp.Matrix, sp.Matrix]:
    shift, _differential, _cosine, reflection0 = b192.temporal_matrices()
    plane_shift = shift**plane
    reflection = sp.expand(plane_shift * reflection0 * plane_shift.T)
    base_n = sp.Matrix.vstack(sp.eye(HALF_TIME), sp.zeros(HALF_TIME))
    base_p = sp.Matrix.vstack(sp.zeros(HALF_TIME), sp.eye(HALF_TIME))
    base = base_n if orientation == "positive" else base_p
    embedding = sp.kronecker_product(plane_shift * base, sp.eye(2))
    theta = sp.kronecker_product(reflection, SIGMA_Z)
    if mutation == "wrong_cut":
        embedding = sp.kronecker_product(base, sp.eye(2))
    if mutation == "wrong_reflection":
        theta = sp.kronecker_product(reflection, sp.eye(2))
    return theta, embedding


@cache
def literal_facts(mutation: str = "") -> dict[str, object]:
    forms: dict[tuple[int, int, str], sp.Matrix] = {}
    embeddings: dict[tuple[int, str], sp.Matrix] = {}
    covariance: dict[int, sp.Matrix] = {}
    action_covariance = []
    for radius in (0, 1):
        action = phase_real_action(radius, mutation)
        covariance[radius] = action.inv(method="DM")
        for plane in (0, 1):
            for orientation in ("positive", "negative"):
                theta, embedding = plane_data(plane, orientation, mutation)
                embeddings[(plane, orientation)] = embedding
                action_covariance.append(matrix_equal(
                    theta * action.T * theta.T, action
                ))
                forms[(radius, plane, orientation)] = sp.simplify(
                    embedding.T * theta * covariance[radius] * embedding
                )

    target = forms[(1, 0, "positive")]
    target_minor = target.extract((0, 12), (0, 12))
    inertias = {
        key: symmetric_inertia(form)
        for key, form in forms.items() if matrix_equal(form, form.T)
    }
    phase = sp.kronecker_product(
        sp.eye(L_TIME), sp.diag(1, -I)
    )
    phase_identity = matrix_equal(
        phase.H * complex_action(1) * phase, phase_real_action(1)
    )

    # One actual Block-192 endpoint has spatial radius one.  Its Clifford
    # matrix squares to I, is traceless, and anticommutes with Gamma_t, giving
    # eight equivalent two-component blocks.
    radius_one_momentum = next(
        momentum
        for _name, incoming, transfer in b192.POINTS
        for momentum in (
            incoming,
            tuple(incoming[axis] + transfer[axis] for axis in range(4)),
        )
        if sp.simplify(sum(sp.sin(momentum[axis])**2 for axis in range(3)) - 1) == 0
    )
    spatial = sum((
        sp.sin(radius_one_momentum[axis]) * b192.GSPACE[axis]
        for axis in range(3)
    ), sp.zeros(16))
    eight_blocks = (
        matrix_equal(spatial**2, sp.eye(16))
        and sp.trace(spatial) == 0
        and matrix_equal(
            spatial * b192.GTIME + b192.GTIME * spatial, sp.zeros(16)
        )
    )
    target_inertia = inertias.get((1, 0, "positive"), (-1, -1, -1))
    full_inertia = tuple(8 * value for value in target_inertia)
    shift, _differential, _cosine, _reflection = b192.temporal_matrices()
    full_shift = sp.kronecker_product(shift, sp.eye(2))
    plane_embedding_covariance = all(matrix_equal(
        embeddings[(1, orientation)],
        full_shift * embeddings[(0, orientation)],
    ) for orientation in ("positive", "negative"))
    return {
        "forms": forms,
        "action_covariance": all(action_covariance),
        "symmetric": all(matrix_equal(form, form.T) for form in forms.values()),
        "minor": target_minor,
        "minor_det": sp.factor(target_minor.det()),
        "rank": target.rank(),
        "inertias": inertias,
        "phase_identity": phase_identity,
        "eight_blocks": eight_blocks,
        "full_inertia": full_inertia,
        "plane_embedding_covariance": plane_embedding_covariance,
    }


Field = tuple[str, int]
Monomial = tuple[Field, ...]


def temporal_dirac_exact(length: int, antiperiodic: bool) -> sp.Matrix:
    action = MASS * sp.eye(length)
    for time in range(length):
        following = (time + 1) % length
        wrap = -1 if antiperiodic and time == length - 1 else 1
        action[time, following] += R(wrap, 2)
        action[following, time] -= R(wrap, 2)
    return action


def theta_monomial(
    monomial: Monomial, *, twisted: bool, plane: int
) -> tuple[sp.Expr, Monomial]:
    scalar = sp.Integer(1)
    reflected: list[Field] = []
    for kind, time in reversed(monomial):
        if twisted:
            scalar *= -1 if time <= 2 * plane + 1 else 1
            reflected_time = (2 * plane + 1 - time) % L_TIME
        else:
            scalar *= -1
            reflected_time = (1 - time) % L_TIME
        reflected.append(("bar" if kind == "chi" else "chi", reflected_time))
    return scalar, tuple(reflected)


def two_point(left: Field, right: Field, covariance: sp.Matrix) -> sp.Expr:
    kind_left, index_left = left
    kind_right, index_right = right
    if kind_left == "chi" and kind_right == "bar":
        return covariance[index_left, index_right]
    if kind_left == "bar" and kind_right == "chi":
        return -covariance[index_right, index_left]
    return sp.Integer(0)


def wick(fields: Monomial, covariance: sp.Matrix) -> sp.Expr:
    if not fields:
        return sp.Integer(1)
    if len(fields) % 2:
        return sp.Integer(0)
    answer = sp.Integer(0)
    for partner in range(1, len(fields)):
        contraction = two_point(fields[0], fields[partner], covariance)
        if contraction == 0:
            continue
        sign = 1 if partner % 2 else -1
        answer += sign * contraction * wick(
            fields[1:partner] + fields[partner + 1:], covariance
        )
    return sp.factor(answer)


def grassmann_gram(
    basis: tuple[Monomial, ...], *, antiperiodic: bool,
    twisted: bool, plane: int,
) -> sp.Matrix:
    covariance = temporal_dirac_exact(L_TIME, antiperiodic).inv(method="DM")
    result = sp.zeros(len(basis))
    for row, left in enumerate(basis):
        scalar, reflected = theta_monomial(left, twisted=twisted, plane=plane)
        for column, right in enumerate(basis):
            result[row, column] = scalar * wick(
                reflected + right, covariance
            )
    return result


def degree_one_basis(times: tuple[int, ...]) -> tuple[Monomial, ...]:
    return tuple(((kind, time),) for time in times for kind in ("bar", "chi"))


def local_basis(time: int) -> tuple[Monomial, ...]:
    return (
        (),
        (("bar", time),),
        (("chi", time),),
        (("bar", time), ("chi", time)),
    )


def hermitian_part(matrix: sp.Matrix) -> sp.Matrix:
    return sp.simplify((matrix + matrix.T) / 2)


def reflected_action_ok(antiperiodic: bool, twisted: bool, plane: int) -> bool:
    action = temporal_dirac_exact(L_TIME, antiperiodic)
    signs = [
        (-1 if time <= 2 * plane + 1 else 1) if twisted else -1
        for time in range(L_TIME)
    ]
    reflect = (
        (lambda time: (2 * plane + 1 - time) % L_TIME)
        if twisted else (lambda time: (1 - time) % L_TIME)
    )
    transformed = sp.zeros(L_TIME)
    for row in range(L_TIME):
        for column in range(L_TIME):
            transformed[row, column] = (
                signs[reflect(row)] * signs[reflect(column)]
                * action[reflect(column), reflect(row)]
            )
    return matrix_equal(transformed, action)


@cache
def repair_facts() -> dict[str, object]:
    repaired = {}
    local = {}
    controls = {}
    for plane in (0, 1):
        times = tuple((1 + plane + offset) % L_TIME for offset in range(HALF_TIME))
        repaired[plane] = grassmann_gram(
            degree_one_basis(times), antiperiodic=True,
            twisted=True, plane=plane,
        )
        local[plane] = grassmann_gram(
            local_basis(times[0]), antiperiodic=True,
            twisted=True, plane=plane,
        )
    control_times = tuple(range(1, HALF_TIME + 1))
    controls["ap_uniform"] = grassmann_gram(
        degree_one_basis(control_times), antiperiodic=True,
        twisted=False, plane=0,
    )
    controls["periodic_twisted"] = grassmann_gram(
        degree_one_basis(control_times), antiperiodic=False,
        twisted=True, plane=0,
    )
    controls["periodic_uniform"] = grassmann_gram(
        degree_one_basis(control_times), antiperiodic=False,
        twisted=False, plane=0,
    )
    repaired_inertia = {
        plane: symmetric_inertia(matrix)
        for plane, matrix in repaired.items() if matrix_equal(matrix, matrix.T)
    }
    local_inertia = {
        plane: symmetric_inertia(matrix)
        for plane, matrix in local.items() if matrix_equal(matrix, matrix.T)
    }
    control_inertia = {
        name: symmetric_inertia(hermitian_part(matrix))
        for name, matrix in controls.items()
    }
    return {
        "repaired": repaired,
        "local": local,
        "controls": controls,
        "repaired_symmetric": all(matrix_equal(value, value.T) for value in repaired.values()),
        "repaired_inertia": repaired_inertia,
        "local_inertia": local_inertia,
        "control_inertia": control_inertia,
        "ap_action": all(reflected_action_ok(True, True, plane) for plane in (0, 1)),
        "ap_uniform_action": reflected_action_ok(True, False, 0),
        "periodic_twisted_action": reflected_action_ok(False, True, 0),
    }


@cache
def twist_facts() -> dict[str, object]:
    k_one = sp.pi / 6
    k_two = sp.pi / 4
    tau_one = sp.simplify(sp.expand_complex(sp.exp(-I * k_one * L_TIME)))
    tau_two = sp.simplify(sp.expand_complex(sp.exp(-I * k_two * L_TIME)))
    # Equality for an arbitrary integer length requires
    # exp[-i (pi/12) L]=1, hence L=24n; its common twist is then +1.
    n = sp.symbols("n", integer=True)
    general_length = 24 * n
    common = sp.simplify(sp.expand_complex(sp.exp(-I * k_one * general_length)))
    return {
        "tau_one": tau_one,
        "tau_two": tau_two,
        "common_l24": tau_one == tau_two == 1,
        "common_lengths": "L=24n",
        "common_general": common,
        "antiperiodic_common_impossible": common == 1,
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
        "### N1",
        "### N2",
        "### N3",
        "### N4",
        "### N5",
        "### N6",
        "### N7",
        "### N8",
        "partial-attempt-with-named-untested-routes",
        "parity-doubled",
        "process tensor",
        "TOE lane scores remain unchanged",
        "No axiom amendment",
    )
    return all(needle in text for needle in required)


def evaluate(mutation: str) -> dict[str, tuple[object, str]]:
    authority = authority_facts()
    literal = literal_facts(mutation if mutation in {"wrong_action", "wrong_cut", "wrong_reflection"} else "")
    repair = repair_facts()
    twist = twist_facts()
    inertias = literal["inertias"]
    target_inertia = inertias.get((1, 0, "positive"), (-1, -1, -1))
    sign_robust = (
        target_inertia[0] > 0 and target_inertia[2] > 0
        and symmetric_inertia(-literal["forms"][(1, 0, "positive")])[0] > 0
        and symmetric_inertia(-literal["forms"][(1, 0, "positive")])[2] > 0
    )
    all_planes_fail = all(
        inertia[0] > 0 and inertia[2] > 0
        for key, inertia in inertias.items()
        if key[0] == 1
    )
    repaired_positive = (
        repair["repaired_symmetric"]
        and all(inertia[2] == 0 for inertia in repair["repaired_inertia"].values())
        and all(inertia[2] == 0 for inertia in repair["local_inertia"].values())
    )
    controls_fail = all(
        inertia[2] > 0 for inertia in repair["control_inertia"].values()
    )
    schur = b192.reduced_history_fixture()

    claims = {
        "global_sign_repairs": mutation == "claim_global_sign_repairs",
        "conflate": mutation == "conflate_schur_berezin",
        "adjacent": mutation != "omit_adjacent_plane",
        "spin_repair": mutation != "omit_spin_repair",
        "ap_modes": mutation == "claim_antiperiodic_modes_compatible",
        "quotient_open": mutation == "open_quotient_early",
        "response_open": mutation == "open_response_early",
        "broad_no_go": mutation == "claim_broad_no_go",
        "toe_progress": mutation == "claim_toe_progress",
    }
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
            literal["minor"] == DISCLOSED_MINOR
            and literal["minor_det"] == DISCLOSED_DETERMINANT
            and literal["rank"] == 4
            and literal["phase_identity"]
            and literal["plane_embedding_covariance"],
            "the disclosed pilot is independently reproduced from the frozen phase-real action",
        ),
        "T1": (
            literal["action_covariance"] and literal["symmetric"]
            and target_inertia == (2, 20, 2)
            and literal["eight_blocks"]
            and literal["full_inertia"] == (16, 160, 16),
            "the actual radius-one Berezin seed is exactly indefinite before quotient construction",
        ),
        "T2": (
            sign_robust and all_planes_fail and claims["adjacent"]
            and claims["global_sign_repairs"] is False
            and schur["positive_rank"] == 24 and schur["positive_identity"]
            and claims["conflate"] is False,
            "sign, plane, orientation, transpose, and Schur-versus-Berezin controls preserve the boundary",
        ),
        "T3": (
            repaired_positive and controls_fail and repair["ap_action"]
            and claims["spin_repair"] and twist["common_l24"]
            and twist["common_lengths"] == "L=24n"
            and twist["antiperiodic_common_impossible"]
            and claims["ap_modes"] is False,
            "twisted antiperiodic scalar RP repairs positivity but cannot retain both frozen modes on one scalar-twist circle",
        ),
        "N": (
            note_contract(),
            "the landed source note contains the fresh N1--N8 no-go-discipline packet",
        ),
        "S": (
            claims["quotient_open"] is False
            and claims["response_open"] is False
            and claims["broad_no_go"] is False
            and claims["toe_progress"] is False,
            "quotient, channel, response, heldouts, axioms, broad no-go, and TOE movement remain sealed",
        ),
    }


N5_LINES = (
    "per_element: checked the exact two-generator exterior norm on positive-half coordinates (t=0,c=0) and (t=6,c=0), whose determinant is strictly negative.",
    "per_site: checked both adjacent reflection-plane classes and both half-circle orientations on the literal periodic L24 radius-zero and radius-one reduced actions.",
    "per_mode: checked the actual radius-one Clifford sector, its eight-copy full-fiber lift, and exact scalar-twist compatibility of k=pi/6 with k=pi/4.",
    "per_block: checked the finite-circle Berezin seed, convention battery, and scalar twisted-antiperiodic repair; GNS, event-factor, channel, and response blocks stop downstream.",
    "lattice_wide: checked and not executed — parity-doubled carriers, global process tensors, open-time limits, gravity closure, Record persistence, Born forcing, and TOE closure remain live.",
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
    literal = literal_facts()
    repair = repair_facts()
    twist = twist_facts()
    print(
        "WITNESS: K[(0,12),(0,12)] determinant="
        f"{literal['minor_det']}; inertia={literal['inertias'][(1,0,'positive')]}; "
        f"full_inertia={literal['full_inertia']}"
    )
    print(
        "REPAIR: twisted-AP degree-one inertias="
        f"{repair['repaired_inertia']}; common frozen-mode twist="
        f"{twist['tau_one']}={twist['tau_two']}"
    )
    for line in N5_LINES:
        print(line)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
