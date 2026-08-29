#!/usr/bin/env python3
"""Independent path/enumeration check of the H1 source-ownership boundary."""

from __future__ import annotations

import argparse
from functools import cache
import itertools
from pathlib import Path
import subprocess
import sys

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26 as parent  # noqa: E402


b193 = parent.b193
b190 = b193.b190
I = sp.I
PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block01-"
    "action-factorized-six-record-decoder-20260828"
)
GOAL = f"{PACKET}/GOAL.md"
PREFLIGHT = f"{PACKET}/PREFLIGHT_WITNESSES.md"
PREREG = "4971d278f3bd23bf9c6d4225a2a308edd6b5e2de"
PARENT = "42b25280486363e9c2017698b813edf182d1a1a3"
MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"
GOAL_BLOB = "a91331d17f5e159ba9ab2f9b368c7d4b717a94b9"
PREFLIGHT_BLOB = "16981bb34a1d6f1f2d40f5cfe4454c77d89f8029"
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block01-action-factorized-six-record-decoder-20260828/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block01-action-factorized-six-record-decoder-20260828/PREFLIGHT_WITNESSES.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.py",
    "scripts/admissibility_d4_h1_schur_record_probability_germ_2026_08_26.py",
    "scripts/admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25.py",
    "scripts/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.py",
    "scripts/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.py",
)

MUTATIONS = (
    "stale_authority",
    "unpin_goal",
    "alias_six_conditions",
    "lose_forward_term",
    "lose_reverse_term",
    "lower_effective_radius",
    "raise_primitive_radius",
    "erase_source_rank",
    "erase_hom_dimension",
    "select_decoder",
    "erase_phase_fits",
    "merge_phase_fits",
    "erase_heldout_witness",
    "derive_internal_action",
    "claim_physical_compiler",
    "open_h2",
    "claim_eta_closure",
    "claim_axiom_change",
    "claim_toe_change",
    "claim_retained",
)


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True
    ).strip()


def add(*items: b190.PolyMatrix) -> b190.PolyMatrix:
    return b190.poly_add(*items)


def scale(item: b190.PolyMatrix, value: sp.Expr) -> b190.PolyMatrix:
    return b190.poly_scale(item, value)


def multiply(
    left: b190.PolyMatrix, right: b190.PolyMatrix
) -> b190.PolyMatrix:
    return b190.poly_multiply(left, right)


def equal(left: b190.PolyMatrix, right: b190.PolyMatrix) -> bool:
    return not add(left, scale(right, -1))


def rotations() -> tuple[sp.Matrix, ...]:
    result = []
    for rows in itertools.permutations((0, 1, 2)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for column in range(3):
                matrix[rows[column], column] = signs[column]
            if matrix.det() == 1:
                result.append(matrix)
    return tuple(result)


def shell_action(rotation: sp.MatrixBase) -> sp.Matrix:
    directions = tuple(
        sign * sp.eye(3)[:, axis]
        for axis in range(3) for sign in (1, -1)
    )
    answer = sp.zeros(6)
    for column, direction in enumerate(directions):
        image = sp.Matrix(rotation * direction)
        row = directions.index(image)
        answer[row, column] = 1
    return answer


def t2_action(rotation: sp.MatrixBase) -> sp.Matrix:
    tensors = []
    for left, right in ((0, 1), (1, 2), (0, 2)):
        tensor = sp.zeros(3)
        tensor[left, right] = 1
        tensor[right, left] = 1
        tensors.append(tensor)
    columns = []
    for tensor in tensors:
        image = rotation * tensor * rotation.T
        columns.append(sp.Matrix((
            image[0, 1], image[1, 2], image[0, 2]
        )))
    return sp.Matrix.hstack(*columns)


def stated_decoders() -> tuple[sp.Matrix, sp.Matrix]:
    odd = sp.zeros(3, 18)
    even = sp.zeros(3, 18)
    odd[0, 1], odd[0, 4], odd[0, 6], odd[0, 9] = -1, 1, -1, 1
    odd[1, 8], odd[1, 11], odd[1, 13], odd[1, 16] = -1, 1, -1, 1
    odd[2, 2], odd[2, 5], odd[2, 12], odd[2, 15] = -1, 1, -1, 1
    even[0, 2], even[0, 5], even[0, 8], even[0, 11] = 1, 1, -1, -1
    even[1, 6], even[1, 9], even[1, 12], even[1, 15] = 1, 1, -1, -1
    even[2, 1], even[2, 4], even[2, 13], even[2, 16] = -1, -1, 1, 1
    return odd, even


def reverse_exponents(source: b190.PolyMatrix) -> b190.PolyMatrix:
    answer: b190.PolyMatrix = {}
    for exponent, matrix in source.items():
        new_exponent = exponent[:4] + tuple(
            exponent[index] - exponent[index + 4]
            for index in range(4)
        )
        answer = add(answer, {new_exponent: matrix})
    return answer


def max_support(item: b190.PolyMatrix) -> tuple[int, int, int]:
    return (
        len(item),
        max(sum(abs(value) for value in exponent[:4])
            for exponent in item),
        max(sum(abs(value) for value in exponent[4:])
            for exponent in item),
    )


def polynomial_rank(polynomials: tuple[b190.PolyMatrix, ...]) -> int:
    exponents = sorted(set().union(*(item.keys() for item in polynomials)))
    columns = []
    for polynomial in polynomials:
        data = []
        for exponent in exponents:
            data.extend(list(polynomial.get(exponent, sp.zeros(16))))
        columns.append(sp.Matrix(data))
    return sp.Matrix.hstack(*columns).rank()


@cache
def authority() -> dict[str, object]:
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": subprocess.run(
            ("git", "merge-base", "--is-ancestor", PARENT, "HEAD"),
            cwd=ROOT,
            check=False,
        ).returncode == 0,
        "prereg": subprocess.run(
            ("git", "merge-base", "--is-ancestor", PREREG, "HEAD"),
            cwd=ROOT,
            check=False,
        ).returncode == 0,
        "goal": git("rev-parse", f"{PREREG}:{GOAL}"),
        "preflight": git("rev-parse", f"{PREREG}:{PREFLIGHT}"),
    }


@cache
def path_factorization() -> dict[str, object]:
    d_in: b190.PolyMatrix = {}
    d_out: b190.PolyMatrix = {}
    for axis in range(4):
        d_in = add(d_in, {
            b190.exponent({axis: 1}): b190.CREATION[axis] / (2 * I),
            b190.exponent({axis: -1}): -b190.CREATION[axis] / (2 * I),
        })
        d_out = add(d_out, {
            b190.exponent({axis: 1}, {axis: 1}):
                b190.CREATION[axis] / (2 * I),
            b190.exponent({axis: -1}, {axis: -1}):
                -b190.CREATION[axis] / (2 * I),
        })

    coefficients = b193.tt_source_coefficients("H1", 1)
    assembled: b190.PolyMatrix = {}
    hodge_sum: b190.PolyMatrix = {}
    incoming_sum: b190.PolyMatrix = {}
    outgoing_sum: b190.PolyMatrix = {}
    for slot in (8, 9):
        left, right = b190.PAIRS4[slot]
        left_cosine = {
            b190.exponent({left: 1}, {left: 1}):
                sp.Rational(1, 2) * b190.IDENTITY_FORM,
            b190.exponent({left: -1}):
                sp.Rational(1, 2) * b190.IDENTITY_FORM,
        }
        right_cosine = {
            b190.exponent({right: 1}, {right: 1}):
                sp.Rational(1, 2) * b190.IDENTITY_FORM,
            b190.exponent({right: -1}):
                sp.Rational(1, 2) * b190.IDENTITY_FORM,
        }
        local_tensor = {
            b190.ZERO_EXPONENT: (
                b190.CREATION[left] * b190.ANNIHILATION[right]
                + b190.CREATION[right] * b190.ANNIHILATION[left]
            )
        }
        hodge = multiply(
            scale(multiply(left_cosine, right_cosine), -1 / sp.sqrt(2)),
            local_tensor,
        )
        incoming = scale(multiply(hodge, d_in), I)
        outgoing = scale(
            multiply(b190.poly_transpose(d_out), hodge), I
        )
        vertex = add(scale(hodge, b190.MASS), incoming, outgoing)
        coefficient = coefficients[slot]
        assembled = add(assembled, scale(vertex, coefficient))
        hodge_sum = add(hodge_sum, scale(hodge, coefficient))
        incoming_sum = add(incoming_sum, scale(incoming, coefficient))
        outgoing_sum = add(outgoing_sum, scale(outgoing, coefficient))

    inherited = parent.combined_raw_source()
    reverse_assembled = reverse_exponents(assembled)
    reverse_inherited = reverse_exponents(inherited)
    raw_vertices = parent.raw_action_vertices()
    t2_polynomials = (
        scale(raw_vertices[7], sp.sqrt(2)),
        scale(raw_vertices[9], sp.sqrt(2)),
        scale(raw_vertices[8], sp.sqrt(2)),
    )
    return {
        "forward_equal": equal(assembled, inherited),
        "reverse_equal": equal(reverse_assembled, reverse_inherited),
        "forward_terms": len(assembled),
        "reverse_terms": len(reverse_assembled),
        "hodge_support": max_support(hodge_sum),
        "incoming_support": max_support(incoming_sum),
        "outgoing_support": max_support(outgoing_sum),
        "source_support": max_support(assembled),
        "primitive_support": (
            max_support(d_in), max_support(d_out)
        ),
        "t2_rank": polynomial_rank(t2_polynomials),
    }


@cache
def representation_and_fit() -> dict[str, object]:
    group = rotations()
    constraints = []
    for rotation in group:
        domain = sp.kronecker_product(
            shell_action(rotation), rotation
        )
        target = t2_action(rotation)
        constraints.append(
            sp.kronecker_product(sp.eye(18), target)
            - sp.kronecker_product(domain.T, sp.eye(3))
        )
    constraint = sp.Matrix.vstack(*constraints)
    rank = DomainMatrix.from_Matrix(constraint).rank()
    hom_dimension = 54 - rank

    odd, even = stated_decoders()
    basis_equivariant = all(
        t2_action(rotation) * decoder
        == decoder * sp.kronecker_product(
            shell_action(rotation), rotation
        )
        for rotation in group
        for decoder in (odd, even)
    )
    basis_dimension = sp.Matrix.hstack(
        odd.reshape(54, 1), even.reshape(54, 1)
    ).rank()

    phases = (
        sp.Rational(1, 2) - I * sp.sqrt(3) / 2,
        sp.Rational(1, 2) + I * sp.sqrt(3) / 2,
        -I, I, sp.Integer(1), sp.Integer(1),
    )
    candidate = sp.Matrix.vstack(*(
        sp.Matrix((sp.re(phase), sp.im(phase), 0))
        for phase in phases
    ))
    target = sp.Matrix((0, 1 / sp.sqrt(2), -1))
    maps = []
    for rotation in group:
        internal = sp.kronecker_product(sp.eye(6), rotation)
        columns = sp.Matrix.hstack(
            odd * internal * candidate,
            even * internal * candidate,
        )
        if columns.rank() != 2:
            continue
        if columns.row_join(target).rank() != 2:
            continue
        weights = columns.gauss_jordan_solve(target)[0]
        maps.append(sp.simplify(
            (weights[0] * odd + weights[1] * even) * internal
        ))
    distinct_maps = {tuple(item) for item in maps}
    pair_witnesses = 0
    for left in range(len(maps)):
        for right in range(left):
            if any(
                maps[left][:, column] != maps[right][:, column]
                for column in range(18)
            ):
                pair_witnesses += 1
    return {
        "group_order": len(group),
        "constraint_rank": rank,
        "hom_dimension": hom_dimension,
        "basis_dimension": basis_dimension,
        "basis_equivariant": basis_equivariant,
        "fits": len(maps),
        "distinct_maps": len(distinct_maps),
        "all_fit_target": all(item * candidate == target for item in maps),
        "pair_witnesses": pair_witnesses,
        "expected_pair_witnesses": len(maps) * (len(maps) - 1) // 2,
    }


def checks(mutation: str = "") -> dict[str, tuple[bool, str]]:
    auth = dict(authority())
    path = dict(path_factorization())
    rep = dict(representation_and_fit())
    claims: dict[str, object] = {
        "six_conditions_are_eta": False,
        "source_rank": path["t2_rank"],
        "hom_dimension": rep["hom_dimension"],
        "decoder_selected": False,
        "internal_action_derived": False,
        "physical_compiler": False,
        "h2_open": False,
        "eta_closed": False,
        "axiom_change": False,
        "toe_change": 0,
        "retained": False,
    }
    if mutation == "stale_authority":
        auth["main"] = "stale"
    elif mutation == "unpin_goal":
        auth["goal"] = "changed"
    elif mutation == "alias_six_conditions":
        claims["six_conditions_are_eta"] = True
    elif mutation == "lose_forward_term":
        path["forward_terms"] -= 1
    elif mutation == "lose_reverse_term":
        path["reverse_terms"] -= 1
    elif mutation == "lower_effective_radius":
        path["source_support"] = (110, 1, 1)
    elif mutation == "raise_primitive_radius":
        path["primitive_support"] = ((8, 2, 0), (8, 1, 1))
    elif mutation == "erase_source_rank":
        claims["source_rank"] = 2
    elif mutation == "erase_hom_dimension":
        claims["hom_dimension"] = 1
    elif mutation == "select_decoder":
        claims["decoder_selected"] = True
    elif mutation == "erase_phase_fits":
        rep["fits"] = 0
    elif mutation == "merge_phase_fits":
        rep["distinct_maps"] = 1
    elif mutation == "erase_heldout_witness":
        rep["pair_witnesses"] = 0
    elif mutation == "derive_internal_action":
        claims["internal_action_derived"] = True
    elif mutation == "claim_physical_compiler":
        claims["physical_compiler"] = True
    elif mutation == "open_h2":
        claims["h2_open"] = True
    elif mutation == "claim_eta_closure":
        claims["eta_closed"] = True
    elif mutation == "claim_axiom_change":
        claims["axiom_change"] = True
    elif mutation == "claim_toe_change":
        claims["toe_change"] = 1
    elif mutation == "claim_retained":
        claims["retained"] = True

    authority_ok = (
        auth["main"] == MAIN
        and auth["parent"]
        and auth["prereg"]
        and auth["goal"] == GOAL_BLOB
        and auth["preflight"] == PREFLIGHT_BLOB
    )
    typing_ok = not claims["six_conditions_are_eta"]
    factor_ok = (
        path["forward_equal"]
        and path["reverse_equal"]
        and path["forward_terms"] == 110
        and path["reverse_terms"] == 110
        and path["hodge_support"] == (8, 2, 2)
        and path["incoming_support"] == (60, 3, 2)
        and path["outgoing_support"] == (60, 3, 3)
        and path["source_support"] == (110, 3, 3)
        and path["primitive_support"] == ((8, 1, 0), (8, 1, 1))
    )
    source_ok = path["t2_rank"] == 3 and claims["source_rank"] == 3
    hom_ok = (
        rep["group_order"] == 24
        and rep["constraint_rank"] == 52
        and rep["hom_dimension"] == 2
        and claims["hom_dimension"] == 2
        and rep["basis_dimension"] == 2
        and rep["basis_equivariant"]
        and not claims["decoder_selected"]
    )
    fit_ok = (
        rep["fits"] == 8
        and rep["distinct_maps"] == 8
        and rep["all_fit_target"]
        and rep["pair_witnesses"] == rep["expected_pair_witnesses"] == 28
    )
    boundary_ok = (
        not claims["internal_action_derived"]
        and not claims["physical_compiler"]
        and not claims["h2_open"]
        and not claims["eta_closed"]
        and not claims["axiom_change"]
        and claims["toe_change"] == 0
        and not claims["retained"]
    )
    return {
        "independent_authority": (
            authority_ok,
            "main, parent, preregistration, goal, and preflight are pinned",
        ),
        "independent_input_typing": (
            typing_ok,
            "alternative displacement conditions are not simultaneous eta",
        ),
        "independent_path_factorization": (
            factor_ok,
            "fresh monomial paths reconstruct 110 forward/reverse terms and "
            "radius-three effective support from unit factors",
        ),
        "independent_t2_injection": (
            source_ok,
            "the Laurent source map has exact rank three on T2",
        ),
        "independent_hom_solve": (
            hom_ok,
            "fresh 54-variable covariance constraints have rank 52 and "
            "two decoder classes",
        ),
        "independent_phase_fit_falsifier": (
            fit_ok,
            "eight distinct fitted maps agree on H1 and all 28 pairs differ "
            "on a one-site basis witness",
        ),
        "independent_scope": (
            boundary_ok,
            "no internal action, physical compiler, H2, eta, axiom, TOE, or "
            "retained closure is imported",
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", default="")
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()
    if args.mutation and args.mutation not in MUTATIONS:
        raise SystemExit(f"unknown mutation: {args.mutation}")
    mutation_failures = 0
    if args.mutation_sweep:
        survivors = [
            mutation for mutation in MUTATIONS
            if all(ok for ok, _message in checks(mutation).values())
        ]
        mutation_failures = len(survivors)
        print(
            f"MUTATION_TOTAL: PASS={len(MUTATIONS)-len(survivors)} "
            f"FAIL={len(survivors)}"
        )
        if survivors:
            print("MUTATION_SURVIVORS:", ",".join(survivors))
    results = checks(args.mutation)
    passed = 0
    for name, (ok, message) in results.items():
        print(f"[{name}] {'PASS' if ok else 'FAIL'}: {message}")
        passed += int(ok)
    path = path_factorization()
    rep = representation_and_fit()
    print(
        "INDEPENDENT_RESULT: support="
        f"{path['source_support']}; T2 rank={path['t2_rank']}; "
        f"Hom={rep['hom_dimension']}; phase fits/maps="
        f"{rep['fits']}/{rep['distinct_maps']}."
    )
    failures = len(results) - passed + mutation_failures
    print(f"TOTAL: PASS={passed} FAIL={failures}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
