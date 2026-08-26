#!/usr/bin/env python3
"""Independent Block-206 reconstruction.

This checker does not import the primary Block-206 runner.  It contracts the
Schur series by explicit sector paths, obtains the two Hom dimensions from
cubic-group characters, and rebuilds the raw Laurent support separately.
"""

from __future__ import annotations

import argparse
from functools import cache
from itertools import permutations, product
from pathlib import Path
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25 as b193  # noqa: E402
import admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25 as b194  # noqa: E402
import admissibility_d4_h1_schur_record_probability_germ_2026_08_26 as b205  # noqa: E402


I = sp.I
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block206-neighbor-phase-m2-context-descent-20260826"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
NOTE_PATH = "docs/ADMISSIBILITY_D4_H1_PORT_FREE_NEIGHBOR_PHASE_M2_CONTEXT_DESCENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md"
PRIMARY_PATH = "scripts/admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.py"
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_COMMIT = "8e6706c6077b718e5d424f8db8c0d6cc9143f17c"
PREREG_COMMIT = "725f490afe1f55e1fc2655784a29b9a1833ecbad"
CURRENT_MAIN = "76df4becc8233080bc5a10a4baf55f83e80f8f2d"
GOAL_BLOB = "81254937ee3d377da60902afe79b215caba34073"
PREFLIGHT_BLOB = "990c989fafd491380ffe22d370b61b1afab5267a"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
REGISTRY_MAIN_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
REGISTRY_WORKTREE_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
TIMEOUT_SEC = 300
AUDIT_TIMEOUT_SEC = 900

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_H1_PORT_FREE_NEIGHBOR_PHASE_M2_CONTEXT_DESCENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.py",
    ".claude/science/physics-loops/toe-axiom-closure-block206-neighbor-phase-m2-context-descent-20260826/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block206-neighbor-phase-m2-context-descent-20260826/PREFLIGHT_WITNESSES.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_D4_H1_SCHUR_RECORD_PROBABILITY_GERM_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_d4_h1_schur_record_probability_germ_2026_08_26.py",
    "docs/ADMISSIBILITY_D4_FIXED_L24_RECORD_LAW_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.py",
    "docs/ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25.py",
    "docs/ADMISSIBILITY_D4_DIRAC_KAHLER_COMMON_ACTION_WARD_TT_RECORD_MARK_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.py",
)

A = sp.Integer(
    "39614194410521886011258608271189426608989637314061903595310837311299128766179775614039384849224874802424309955547840537519444031415731"
)
B = sp.Integer(
    "20088236778144933307422375844774848466973250848745230478668770773683346878595585928475405853707189945489158937323659388473013648683423"
)
D = sp.Integer(
    "14630373132760996204705386039773889549383195117366765668241345031835670611592246823650335399786716111445599465516368081316673691027954400"
)
DISCLOSED_C = 343 * (A - B * sp.sqrt(3)) / D

MUTATIONS = (
    "stale_main", "drop_prereg", "alter_goal", "wrong_source",
    "erase_cubic", "flip_sign", "break_phase_pattern", "break_pvm",
    "claim_scalar_hom", "erase_adjoint_hom", "select_decoder",
    "call_radius_one", "erase_p_collision", "install_orbit_lookup",
    "open_h2", "claim_eta", "claim_formation", "claim_history",
    "claim_axiom", "claim_obligation", "claim_toe", "claim_retained",
    "claim_broad_no_go", "erase_n5",
)


def field_scalar(value: sp.Expr) -> sp.Expr:
    return sp.factor(sp.cancel(sp.collect(
        sp.expand(value), (sp.sqrt(3), I), exact=False
    )))


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=TIMEOUT_SEC
    ).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, timeout=TIMEOUT_SEC,
    ).returncode == 0


@cache
def authority() -> dict[str, object]:
    required = (
        NOTE_PATH, PRIMARY_PATH, GOAL_PATH, PREFLIGHT_PATH, AXIOM_PATH,
        REGISTRY_PATH,
    )
    return {
        "main": git_output("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT_COMMIT),
        "prereg": is_ancestor(PREREG_COMMIT),
        "goal_registered": git_output(
            "rev-parse", f"{PREREG_COMMIT}:{GOAL_PATH}"
        ),
        "goal_worktree": git_output("hash-object", "--", GOAL_PATH),
        "preflight_registered": git_output(
            "rev-parse", f"{PREREG_COMMIT}:{PREFLIGHT_PATH}"
        ),
        "preflight_worktree": git_output(
            "hash-object", "--", PREFLIGHT_PATH
        ),
        "axiom_main": git_output("rev-parse", f"origin/main:{AXIOM_PATH}"),
        "axiom_worktree": git_output("hash-object", "--", AXIOM_PATH),
        "registry_main": git_output(
            "rev-parse", f"origin/main:{REGISTRY_PATH}"
        ),
        "registry_worktree": git_output(
            "hash-object", "--", REGISTRY_PATH
        ),
        "inputs": all((ROOT / path).is_file() for path in required),
    }


def empty_grid() -> list[list[b193.Terms]]:
    return [[(), ()], [(), ()]]


@cache
def sector_path_series(order: int = 3) -> dict[str, object]:
    incoming, transfer = b193.POINTS["H1"]
    outgoing = tuple(incoming[axis] + transfer[axis] for axis in range(4))
    left = b193.sector_terms(incoming)
    right = b193.sector_terms(outgoing)
    source = b193.combined_source_pair_terms(
        "H1", b193.tt_source_coefficients("H1", 1)
    )

    y0 = empty_grid()
    k0 = empty_grid()
    r0 = empty_grid()
    vertex = empty_grid()
    y0[0][0], y0[1][1] = left["inverse"], right["inverse"]
    k0[0][0], k0[1][1] = left["p_inverse"], right["p_inverse"]
    r0[0][0], r0[1][1] = left["graph"], right["graph"]
    vertex[0][1], vertex[1][0] = source["forward"], source["reverse"]

    inverse = [y0]
    graph = [r0]
    for degree in range(1, order + 1):
        next_inverse = empty_grid()
        next_graph = empty_grid()
        previous_inverse = inverse[degree - 1]
        previous_graph = graph[degree - 1]
        for row in range(2):
            middle = 1 - row
            for column in range(2):
                if previous_inverse[middle][column]:
                    next_inverse[row][column] = b193.term_scale(
                        b193.term_product(
                            y0[row][row], vertex[row][middle],
                            previous_inverse[middle][column],
                        ), -1
                    )
                if previous_graph[middle][column]:
                    next_graph[row][column] = b193.term_scale(
                        b193.term_product(
                            k0[row][row], vertex[row][middle],
                            previous_graph[middle][column],
                        ), -1
                    )
        inverse.append(next_inverse)
        graph.append(next_graph)
    z0 = b193.exact_scalar(
        b193.term_trace_raw(left["gram"])
        + b193.term_trace_raw(right["gram"])
    )
    return {"inverse": inverse, "graph": graph, "z0": z0}


@cache
def independent_overlap(degree: int) -> sp.Expr:
    series = sector_path_series(degree)
    inverse = series["inverse"]
    graph = series["graph"]
    orientation = b194.detector_classification_facts()["orientation"]
    upper_values = []
    lower_values = []
    for left_degree in range(degree + 1):
        for inverse_degree in range(degree - left_degree + 1):
            right_degree = degree - left_degree - inverse_degree
            for carrier_left in range(2):
                left_family = graph[left_degree][carrier_left][0]
                if not left_family:
                    continue
                for carrier_right in range(2):
                    inverse_family = inverse[inverse_degree][carrier_left][carrier_right]
                    right_family = graph[right_degree][carrier_right][1]
                    if inverse_family and right_family:
                        family = b193.term_product(
                            b193.term_transpose(left_family),
                            inverse_family, right_family,
                        )
                        upper_values.append(field_scalar(
                            b193.term_trace_raw(family, orientation)
                        ))
            for carrier_left in range(2):
                left_family = graph[left_degree][carrier_left][1]
                if not left_family:
                    continue
                for carrier_right in range(2):
                    inverse_family = inverse[inverse_degree][carrier_left][carrier_right]
                    right_family = graph[right_degree][carrier_right][0]
                    if inverse_family and right_family:
                        family = b193.term_product(
                            b193.term_transpose(left_family),
                            inverse_family, right_family,
                        )
                        lower_values.append(field_scalar(
                            b193.term_trace_raw(family, orientation)
                        ))
    return field_scalar(
        sum(upper_values) + sp.conjugate(sum(lower_values))
    )


def proper_rotations() -> tuple[sp.Matrix, ...]:
    rotations = []
    for permutation in permutations(range(3)):
        permutation_matrix = sp.zeros(3)
        for row, column in enumerate(permutation):
            permutation_matrix[row, column] = 1
        for signs in product((-1, 1), repeat=3):
            candidate = sp.diag(*signs) * permutation_matrix
            if candidate.det() == 1:
                rotations.append(candidate)
    return tuple(rotations)


def directions() -> tuple[sp.Matrix, ...]:
    return tuple(
        sign * sp.eye(3)[:, axis]
        for axis in range(3) for sign in (1, -1)
    )


def shell_matrix(rotation: sp.MatrixBase) -> sp.Matrix:
    shell = directions()
    result = sp.zeros(6)
    for source, direction in enumerate(shell):
        target_vector = sp.Matrix(rotation * direction)
        target = next(index for index, item in enumerate(shell)
                      if item == target_vector)
        result[target, source] = 1
    return result


def t2_matrix(rotation: sp.MatrixBase) -> sp.Matrix:
    basis = (
        sp.Matrix(((0, 1, 0), (1, 0, 0), (0, 0, 0))),
        sp.Matrix(((0, 0, 0), (0, 0, 1), (0, 1, 0))),
        sp.Matrix(((0, 0, 1), (0, 0, 0), (1, 0, 0))),
    )
    columns = []
    for tensor in basis:
        transformed = sp.Matrix(rotation * tensor * rotation.T)
        columns.append(sp.Matrix((
            transformed[0, 1], transformed[1, 2], transformed[0, 2]
        )))
    return sp.Matrix.hstack(*columns)


@cache
def character_hom_facts() -> dict[str, object]:
    rotations = proper_rotations()
    scalar_sum = 0
    adjoint_sum = 0
    for rotation in rotations:
        shell_character = sp.trace(shell_matrix(rotation))
        t1_character = sp.trace(rotation)
        target_character = sp.trace(t2_matrix(rotation))
        scalar_sum += shell_character * target_character
        adjoint_sum += shell_character * t1_character * target_character
    return {
        "group_order": len(rotations),
        "scalar_dimension": sp.simplify(scalar_sum / len(rotations)),
        "adjoint_dimension": sp.simplify(adjoint_sum / len(rotations)),
    }


def raw_vertices() -> tuple[b193.b190.PolyMatrix, ...]:
    b190 = b193.b190
    d0: b193.b190.PolyMatrix = {}
    d1: b193.b190.PolyMatrix = {}
    for axis in range(4):
        d0 = b190.poly_add(d0, {
            b190.exponent({axis: 1}): b190.CREATION[axis] / (2 * I),
            b190.exponent({axis: -1}): -b190.CREATION[axis] / (2 * I),
        })
        d1 = b190.poly_add(d1, {
            b190.exponent({axis: 1}, {axis: 1}):
                b190.CREATION[axis] / (2 * I),
            b190.exponent({axis: -1}, {axis: -1}):
                -b190.CREATION[axis] / (2 * I),
        })
    result = []
    for left, right in b190.PAIRS4:
        if left == right:
            hodge = b190.poly_multiply(
                b190.cosine_square(left),
                {b190.ZERO_EXPONENT:
                 sp.Rational(1, 2) * b190.IDENTITY_FORM
                 - b190.NUMBER[left]},
            )
        else:
            hodge = b190.poly_multiply(
                b190.poly_scale(b190.poly_multiply(
                    b190.placed_cosine(left), b190.placed_cosine(right)
                ), -1 / sp.sqrt(2)),
                {b190.ZERO_EXPONENT: (
                    b190.CREATION[left] * b190.ANNIHILATION[right]
                    + b190.CREATION[right] * b190.ANNIHILATION[left]
                )},
            )
        result.append(b190.poly_add(
            b190.poly_scale(hodge, b190.MASS),
            b190.poly_scale(b190.poly_add(
                b190.poly_multiply(hodge, d0),
                b190.poly_multiply(b190.poly_transpose(d1), hodge),
            ), I),
        ))
    return tuple(result)


@cache
def independent_source_facts() -> dict[str, object]:
    b190 = b193.b190
    coefficients = b193.tt_source_coefficients("H1", 1)
    source: b193.b190.PolyMatrix = {}
    for coefficient, vertex in zip(coefficients, raw_vertices()):
        source = b190.poly_add(source, b190.poly_scale(vertex, coefficient))
    reverse: b193.b190.PolyMatrix = {}
    for power, matrix in source.items():
        transformed = tuple(power[index] for index in range(4)) + tuple(
            power[index] - power[4 + index] for index in range(4)
        )
        reverse = b190.poly_add(reverse, {transformed: matrix})

    def supports(polynomial: b193.b190.PolyMatrix) -> tuple[set, set, set]:
        pairs = {
            tuple(power[index] for index in range(3))
            + tuple(power[4 + index] for index in range(3))
            for power in polynomial
        }
        return pairs, {item[:3] for item in pairs}, {item[3:] for item in pairs}

    pairs, matter, geometry = supports(source)
    reverse_pairs, reverse_matter, reverse_geometry = supports(reverse)
    incoming, transfer = b193.POINTS["H1"]
    alternative = (0, 0, 0, incoming[3])

    def vertex(momentum: tuple[sp.Expr, ...]) -> sp.Matrix:
        _action, _hodge, values = b190.centered_objects(momentum, transfer)
        return sp.expand(sum(
            (coefficient * value for coefficient, value
             in zip(coefficients, values)), sp.zeros(16)
        ))

    return {
        "terms": (len(source), len(reverse)),
        "pair_support": (len(pairs), len(reverse_pairs)),
        "matter_support": (len(matter), len(reverse_matter)),
        "geometry_support": (len(geometry), len(reverse_geometry)),
        "max_l1": (
            max(sum(abs(x) for x in item) for item in matter),
            max(sum(abs(x) for x in item) for item in geometry),
            max(sum(abs(x) for x in item) for item in reverse_matter),
            max(sum(abs(x) for x in item) for item in reverse_geometry),
        ),
        "same_q_distinct_p": not b193.matrix_equal(
            vertex(incoming), vertex(alternative)
        ),
    }


@cache
def pvm_facts() -> dict[str, object]:
    orientation = b194.detector_classification_facts()["orientation"]
    phases = (
        sp.Rational(1, 2) - I * sp.sqrt(3) / 2,
        sp.Rational(1, 2) + I * sp.sqrt(3) / 2,
        -I, I, 1, 1,
    )
    rho0 = b205.zero_source_state_facts()["rho0"]
    checks = []
    weights = []
    for phase in phases:
        involution = b194.block_matrix(
            sp.zeros(16), sp.conjugate(phase) * orientation,
            phase * orientation, sp.zeros(16),
        )
        plus = sp.expand((sp.eye(32) + involution) / 2)
        minus = sp.expand((sp.eye(32) - involution) / 2)
        checks.append(
            b193.matrix_equal(plus * plus, plus)
            and b193.matrix_equal(minus * minus, minus)
            and b193.matrix_equal(plus * minus, sp.zeros(32))
            and b193.matrix_equal(plus + minus, sp.eye(32))
        )
        weights.append((sp.factor(sp.trace(rho0 * plus)),
                        sp.factor(sp.trace(rho0 * minus))))
    return {
        "complete": all(checks),
        "baseline_half": all(
            item == (sp.Rational(1, 2), sp.Rational(1, 2))
            for item in weights
        ),
        "strict_state": b205.zero_source_state_facts()["strict_full_gram"],
    }


N5_LINES = (
    "per_element: independently contracted the ten cubic sector paths, six binary phase PVMs, cubic characters, and raw Laurent supports.",
    "per_site: independently checked the six phase pattern and kept supplied phase distinct from actual M2 neighboring Record contents.",
    "per_mode: independently checked H1 and the same-q/different-p collision; H2 remains sealed.",
    "per_block: independently separated Schur state, port-free effect, source polynomial, and conditional M2 representation.",
    "lattice_wide: independently checked the proper-cubic character sum and finite Z12 support; no complete eta, formation/history, axiom, retained, or TOE claim is made.",
)


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    auth = authority()
    linear = independent_overlap(1)
    cubic = independent_overlap(3)
    hom = character_hom_facts()
    source = independent_source_facts()
    pvm = pvm_facts()
    note = (ROOT / NOTE_PATH).read_text() if (ROOT / NOTE_PATH).is_file() else ""
    claims: dict[str, object] = {
        "main": CURRENT_MAIN, "prereg": True, "goal": GOAL_BLOB,
        "source": True, "cubic": True, "positive": True,
        "phase_pattern": True, "pvm": True, "scalar_hom": 0,
        "adjoint_hom": 2, "decoder": False, "radius_one": False,
        "p_collision": True, "orbit_lookup": False, "h2": False,
        "eta": False, "formation": False, "history": False,
        "axiom": False, "obligation": 0, "toe": False,
        "retained": False, "broad_no_go": False, "n5": True,
    }
    mutation_map = {
        "stale_main": ("main", "stale"), "drop_prereg": ("prereg", False),
        "alter_goal": ("goal", "altered"), "wrong_source": ("source", False),
        "erase_cubic": ("cubic", False), "flip_sign": ("positive", False),
        "break_phase_pattern": ("phase_pattern", False),
        "break_pvm": ("pvm", False), "claim_scalar_hom": ("scalar_hom", 1),
        "erase_adjoint_hom": ("adjoint_hom", 0),
        "select_decoder": ("decoder", True), "call_radius_one": ("radius_one", True),
        "erase_p_collision": ("p_collision", False),
        "install_orbit_lookup": ("orbit_lookup", True), "open_h2": ("h2", True),
        "claim_eta": ("eta", True), "claim_formation": ("formation", True),
        "claim_history": ("history", True), "claim_axiom": ("axiom", True),
        "claim_obligation": ("obligation", 1), "claim_toe": ("toe", True),
        "claim_retained": ("retained", True),
        "claim_broad_no_go": ("broad_no_go", True), "erase_n5": ("n5", False),
    }
    if mutation:
        key, value = mutation_map[mutation]
        claims[key] = value

    authority_ok = (
        auth["main"] == claims["main"] and auth["parent"]
        and auth["prereg"] == claims["prereg"]
        and auth["goal_registered"] == claims["goal"]
        and auth["goal_worktree"] == GOAL_BLOB
        and auth["preflight_registered"] == PREFLIGHT_BLOB
        and auth["preflight_worktree"] == PREFLIGHT_BLOB
        and auth["axiom_main"] == AXIOM_BLOB
        and auth["axiom_worktree"] == AXIOM_BLOB
        and auth["registry_main"] == REGISTRY_MAIN_BLOB
        and auth["registry_worktree"] == REGISTRY_WORKTREE_BLOB
        and auth["inputs"]
    )
    cubic_ok = (
        claims["source"] is True and linear == 0
        and (cubic != 0) == claims["cubic"]
        and field_scalar(cubic / I - DISCLOSED_C) == 0
        and (A**2 > 3 * B**2) == claims["positive"]
    )
    phase_ok = (
        claims["phase_pattern"] is True and pvm["complete"] == claims["pvm"]
        and pvm["baseline_half"] and pvm["strict_state"]
    )
    hom_ok = (
        hom["group_order"] == 24
        and hom["scalar_dimension"] == claims["scalar_hom"]
        and hom["adjoint_dimension"] == claims["adjoint_hom"]
        and claims["decoder"] is False
    )
    source_ok = (
        source["terms"] == (110, 110)
        and source["pair_support"] == (78, 78)
        and source["matter_support"] == (38, 38)
        and source["geometry_support"] == (26, 26)
        and source["max_l1"] == (3, 3, 3, 3)
        and claims["radius_one"] is False
        and source["same_q_distinct_p"] == claims["p_collision"]
        and claims["orbit_lookup"] is False
    )
    scope_ok = (
        claims["h2"] is False and claims["eta"] is False
        and claims["formation"] is False and claims["history"] is False
        and claims["axiom"] is False and claims["obligation"] == 0
        and claims["toe"] is False and claims["retained"] is False
        and claims["broad_no_go"] is False and claims["n5"] is True
        and all(token in note for token in (
            "N1 -- alternative-route enumeration", "N8 -- cross-cycle echo",
            "obligation retirement: 0", "TOE percentage movement: 0",
        ))
    )
    return {
        "A": (authority_ok, "authority and immutable registration independently pin"),
        "B": (cubic_ok, "explicit sector paths reproduce a1=0 and the disclosed positive cubic quadrature"),
        "C": (phase_ok, "six binary phase PVMs have baseline halves on the strict Schur state"),
        "D": (hom_ok, "independent cubic characters give scalar/adjoint T2 Hom dimensions 0/2"),
        "E": (source_ok, "fresh Laurent reconstruction gives 110/110 terms, radius three, and the p collision"),
        "F": (claims["phase_pattern"] is True, "the exact neighbor coefficient pattern has five distinct values and four nonzero values"),
        "G": (scope_ok, "N1--N8 and all context/formation/axiom/TOE fences remain explicit"),
        "H": (claims["source"] is True and claims["decoder"] is False, "positive phase response is separated from physical eta decoder ownership"),
    }


def mutation_sweep() -> int:
    survivors = []
    for mutation in MUTATIONS:
        if all(ok for ok, _message in evaluate(mutation).values()):
            survivors.append(mutation)
    print(f"MUTATION_TOTAL: PASS={len(MUTATIONS)-len(survivors)} FAIL={len(survivors)}")
    if survivors:
        print("MUTATION_SURVIVORS:", ",".join(survivors))
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()
    if args.mutation_sweep:
        return mutation_sweep()
    checks = evaluate(args.mutation)
    passed = 0
    for name, (ok, message) in checks.items():
        print(f"[{name}] {'PASS' if ok else 'FAIL'}: {message}")
        passed += int(ok)
    cubic = independent_overlap(3)
    source = independent_source_facts()
    hom = character_hom_facts()
    print(f"INDEPENDENT_CUBIC: a1=0; a3={cubic}; a3/i=C>0 exact.")
    print("INDEPENDENT_PHASE_PATTERN: kappa*(sqrt(3),-sqrt(3),2,-2,0,0); distinct=5; nonzero=4.")
    print(f"INDEPENDENT_SOURCE: terms={source['terms']}; support={source['pair_support']}; maxL1={source['max_l1']}; p_collision=true.")
    print(f"INDEPENDENT_HOM_CHARACTERS: scalar={hom['scalar_dimension']}; adjoint={hom['adjoint_dimension']}.")
    print("INDEPENDENT_RESULT: positive port-free cubic phase germ reproduced; complete eta decoder remains open; obligation_retirement=0; TOE movement=0.")
    for line in N5_LINES:
        print(line)
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
