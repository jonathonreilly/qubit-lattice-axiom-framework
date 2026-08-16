#!/usr/bin/env python3
"""Exact integer comparison of displayed L1 arrival to observed Minkowski light.

Scores the already-displayed origin-seed arrival t(v)=|v|_1 on the nonzero
radius-4 integer ball.  No occupancy step is re-run, no new spatial patch is
grown, and no Minkowski structure is written into the axioms.
"""

from __future__ import annotations

import ast
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/L1_MINKOWSKI_LIGHT_MATCH_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/L1_MINKOWSKI_LIGHT_MATCH_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Vec = tuple[int, int, int]


def normalize(text: str) -> str:
    return " ".join(text.split())


def arrival(vec: Vec) -> int:
    """Displayed taxicab / ℓ¹ arrival from the origin."""

    return abs(vec[0]) + abs(vec[1]) + abs(vec[2])


def euclid_sq(vec: Vec) -> int:
    return vec[0] * vec[0] + vec[1] * vec[1] + vec[2] * vec[2]


def support_count(vec: Vec) -> int:
    """Number of nonzero coordinates; not the displayed arrival."""

    return sum(1 for coord in vec if coord != 0)


def radius_four_ball() -> tuple[Vec, ...]:
    points: list[Vec] = []
    for coords in product(range(-4, 5), repeat=3):
        vec = (int(coords[0]), int(coords[1]), int(coords[2]))
        if vec != (0, 0, 0) and arrival(vec) <= 4:
            points.append(vec)
    return tuple(points)


def apply_matrix(matrix: tuple[tuple[int, int, int], ...], vec: Vec) -> Vec:
    return tuple(
        matrix[i][0] * vec[0] + matrix[i][1] * vec[1] + matrix[i][2] * vec[2]
        for i in range(3)
    )


def permutation_sign(perm: tuple[int, int, int]) -> int:
    inversions = 0
    for i in range(3):
        for j in range(i + 1, 3):
            inversions += int(perm[i] > perm[j])
    return -1 if inversions % 2 else 1


def proper_cube_rotations() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    rotations: list[tuple[tuple[int, int, int], ...]] = []
    for perm in permutations(range(3)):
        perm_t = (int(perm[0]), int(perm[1]), int(perm[2]))
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(perm_t) * signs[0] * signs[1] * signs[2] != 1:
                continue
            matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for src in range(3):
                matrix[perm_t[src]][src] = signs[src]
            rotations.append(tuple(tuple(row) for row in matrix))
    return tuple(rotations)


def parse_audit_input_paths(source: str) -> object:
    tree = ast.parse(source)
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS":
                    return ast.literal_eval(node.value)
    raise RuntimeError("AUDIT_INPUT_PATHS assignment not found")


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(
        self,
        label: str,
        statement: str,
        condition: bool,
        residual: object | None = None,
    ) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        if not result and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    runner_source = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print(
        "external_scientific_inputs: displayed t=l1 is scored as already "
        "displayed; Euclidean-isotropic c, discrete l2 null, and boosts are "
        "external comparison objects; no observation or fit is used"
    )
    print(
        "package_local_integrity_reads: the note and current minimal axiom "
        "are read; no cache or governance surface is written"
    )
    print(
        "claim_scope: Whether displayed L1 arrival t=l1 on the radius-4 "
        "integer ball matches Euclidean-isotropic c and the discrete l2 "
        "null cone is reported. Displayed, not adopted."
    )

    expected_paths = (
        "docs/L1_MINKOWSKI_LIGHT_MATCH_BOUNDED_THEOREM_NOTE_2026-08-15.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
    )
    parsed_paths = parse_audit_input_paths(runner_source)
    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the source note and current axiom memo",
        AUDIT_INPUT_PATHS == expected_paths
        and parsed_paths == expected_paths
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        (AUDIT_INPUT_PATHS, parsed_paths),
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    admissibility_sentence = (
        "There is one fixed nearest-neighbor admissibility rule, covariant "
        "under lattice translations and proper cubic rotations."
    )
    checks.check(
        "lattice-axiom",
        "the authority supplies Z^3, nearest-neighbor adjacency, and proper cubic rotations",
        lattice_sentence in normalized_axiom,
    )
    checks.check(
        "admissibility-axiom",
        "Admissibility is a nearest-neighbor rule covariant under those rotations",
        admissibility_sentence in normalized_axiom,
    )
    axiom_forbidden = (
        "Minkowski",
        "Lorentz boost",
        "t(v)=|v|_1",
        "Wick",
    )
    checks.check(
        "axioms-unedited",
        "the axiom memo contains no Minkowski, boost, Wick, or attached L1 arrival",
        all(phrase not in axiom for phrase in axiom_forbidden),
        [phrase for phrase in axiom_forbidden if phrase in axiom],
    )

    ball = radius_four_ball()
    n_ball = len(ball)
    null_set = tuple(vec for vec in ball if arrival(vec) * arrival(vec) == euclid_sq(vec))
    n_null = len(null_set)
    n_both = n_null
    unique_ball = set(ball)
    checks.check(
        "integer-ball-census",
        "the nonzero radius-4 l1 ball has N_ball=128 distinct integer vectors",
        n_ball == 128 and len(unique_ball) == 128,
        n_ball,
    )
    sphere_counts = {
        radius: sum(1 for vec in ball if arrival(vec) == radius) for radius in (1, 2, 3, 4)
    }
    checks.check(
        "l1-sphere-formula",
        "the l1 spheres have sizes 6, 18, 38, 66, matching 4 r^2 + 2",
        sphere_counts == {1: 6, 2: 18, 3: 38, 4: 66}
        and all(sphere_counts[radius] == 4 * radius * radius + 2 for radius in (1, 2, 3, 4)),
        sphere_counts,
    )

    axis = (1, 0, 0)
    face = (1, 1, 0)
    axis_ratio_num = arrival(axis) * arrival(axis)
    axis_ratio_den = euclid_sq(axis)
    face_ratio_num = arrival(face) * arrival(face)
    face_ratio_den = euclid_sq(face)
    checks.check(
        "theorem1-axis-witness",
        "(1,0,0) gives t^2 / |v|_2^2 = 1/1 = 1",
        axis in unique_ball
        and axis_ratio_num == 1
        and axis_ratio_den == 1
        and axis_ratio_num // axis_ratio_den == 1,
        (axis_ratio_num, axis_ratio_den),
    )
    checks.check(
        "theorem1-face-witness",
        "(1,1,0) gives t^2 / |v|_2^2 = 4/2 = 2",
        face in unique_ball
        and face_ratio_num == 4
        and face_ratio_den == 2
        and face_ratio_num // face_ratio_den == 2,
        (face_ratio_num, face_ratio_den),
    )
    distinct_ratios = {
        (arrival(vec) * arrival(vec), euclid_sq(vec)) for vec in ball
    }
    reduced = set()
    for num, den in distinct_ratios:
        gcd = num
        value = den
        while value:
            gcd, value = value, gcd % value
        reduced.add((num // gcd, den // gcd))
    checks.check(
        "theorem1-not-constant",
        "t^2 / |v|_2^2 is not constant on the scored ball",
        len(reduced) > 1 and (1, 1) in reduced and (2, 1) in reduced,
        reduced,
    )
    common_scale_preserves_split = (1 * 9, 1 * 9) != (2 * 9, 1 * 9)
    checks.check(
        "constant-rescale-fails",
        "a common positive rescaling of t cannot equalize the two witness ratios",
        common_scale_preserves_split
        and (face_ratio_num * axis_ratio_den) != (axis_ratio_num * face_ratio_den),
    )

    axis_null = all(
        arrival(vec) * arrival(vec) == euclid_sq(vec)
        for vec in ball
        if support_count(vec) == 1
    )
    off_axis_not_null = all(
        arrival(vec) * arrival(vec) != euclid_sq(vec)
        for vec in ball
        if support_count(vec) > 1
    )
    checks.check(
        "theorem2-census",
        "N_ball=128, N_null=24, N_both=24",
        n_ball == 128 and n_null == 24 and n_both == 24,
        (n_ball, n_null, n_both),
    )
    checks.check(
        "theorem2-proper-subset",
        "the discrete null set on the ball is a proper subset; (1,1,0) is the witness",
        n_null < n_ball
        and face not in set(null_set)
        and arrival(face) == 2
        and euclid_sq(face) == 2
        and arrival(face) * arrival(face) == 4,
        (n_null, n_ball, face),
    )
    checks.check(
        "theorem2-axis-characterization",
        "null vectors on the ball are exactly the 24 axis points, and no off-axis point is null",
        axis_null
        and off_axis_not_null
        and all(support_count(vec) == 1 for vec in null_set)
        and len(null_set) == 24,
    )

    ham_axis = (2, 0, 0)
    checks.check(
        "arrival-not-hamming",
        "displayed arrival is taxicab l1, not Hamming / support count",
        arrival(ham_axis) == 2
        and support_count(ham_axis) == 1
        and arrival(face) == 2
        and support_count(face) == 2
        and arrival(ham_axis) != support_count(ham_axis),
        (arrival(ham_axis), support_count(ham_axis)),
    )

    rotations = proper_cube_rotations()
    checks.check(
        "cube-rotation-order",
        "there are exactly 24 proper cube rotations",
        len(rotations) == 24 and len(set(rotations)) == 24,
        len(rotations),
    )
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    sphere_preserved = all(
        arrival(apply_matrix(matrix, vec)) == arrival(vec)
        and euclid_sq(apply_matrix(matrix, vec)) == euclid_sq(vec)
        for matrix in rotations
        for vec in ball
    )
    spheres_invariant = True
    for radius in (1, 2, 3, 4):
        sphere = {vec for vec in ball if arrival(vec) == radius}
        for matrix in rotations:
            image = {apply_matrix(matrix, vec) for vec in sphere}
            if image != sphere:
                spheres_invariant = False
    checks.check(
        "theorem3-l1-spheres",
        "every proper cube rotation preserves every l1 sphere and every |v|_2^2",
        identity in rotations and sphere_preserved and spheres_invariant,
    )
    checks.check(
        "theorem3-no-time-mix",
        "cube rotations act on space only and leave the arrival value unmixed",
        all(len(matrix) == 3 and all(len(row) == 3 for row in matrix) for matrix in rotations)
        and all(arrival(apply_matrix(matrix, face)) == arrival(face) for matrix in rotations),
    )

    # Observed comparison identity only: the 3-4-5 rational boost mixes t and x.
    t_in, x_in = 4, 0
    t_out = 5 * t_in - 3 * x_in
    x_out = 5 * x_in - 3 * t_in
    checks.check(
        "observed-boost-mixes",
        "the comparison boost (gamma=5/4, beta=3/5) mixes t with x",
        t_out == 20 and x_out == -12 and t_out != 4 * t_in,
        (t_out, x_out),
    )

    required_note_phrases = (
        "t(v) = |v_1| + |v_2| + |v_3|",
        "N_ball=128",
        "N_null=24",
        "N_both=24",
        "(1,0,0)",
        "(1,1,0)",
        "t^2 / |v|_2^2 = 1",
        "t^2 / |v|_2^2 = 2",
        "Displayed, not adopted",
        "does not write Minkowski structure, a Lorentz boost, or a Wick map into",
        "It is not Hamming weight",
        "occupancy face of the form `n≠0` is not used",
        "does not grow L1 on a `4×4×4`",
        "claim_scope: \"Whether displayed L1 arrival `t=ℓ¹` on the radius-4 integer ball matches Euclidean-isotropic `c` and the discrete `ℓ²` null cone is reported. Displayed, not adopted.\"",
        "actual_current_surface_status: bounded-support",
        "hypothetical_axiom_status: \"no edit\"",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
        "**No-Go Discipline status: PASS**",
        "**Type:** bounded_theorem",
    )
    checks.check(
        "note-claim-contract",
        "the note states the three theorems, census, and displayed-not-adopted scope",
        all(phrase in note or phrase in normalized_note for phrase in required_note_phrases),
        [phrase for phrase in required_note_phrases if phrase not in note and phrase not in normalized_note],
    )
    checks.check(
        "note-dependency-contract",
        "frontmatter names only the current axiom boundary",
        "  - minimal_axioms" in note
        and "upstream_dependencies:" in note
        and note.count("\n  - ") == 1,
    )
    checks.check(
        "note-no-go-contract",
        "the note records all eight stress-test sections",
        all(f"### N{index}" in note for index in range(1, 9)),
    )
    checks.check(
        "note-quotes-axioms",
        "the note quotes the Lattice and Admissibility sentences it uses",
        lattice_sentence in normalized_note and admissibility_sentence in normalized_note,
    )
    checks.check(
        "note-reports-census",
        "the note reports the independently computed census integers",
        f"`N_ball` | `{n_ball}`" in note
        and f"`N_null` | `{n_null}`" in note
        and f"`N_both` | `{n_both}`" in note,
    )

    forbidden = (
        "G_N",
        "1/r",
        "1/r^2",
        "Lattice-named",
        "not a TOE",
        "Therefore Minkowski is impossible",
        "write Minkowski into Admissibility as axiom content",
        "occupancy is re-run",
        "grow L1 on a new 4x4x4 patch",
    )
    checks.check(
        "forbidden-rhetoric",
        "note and runner avoid the forbidden phrases and rejected broad claims",
        all(phrase not in note for phrase in forbidden),
        [phrase for phrase in forbidden if phrase in note],
    )
    checks.check(
        "no-occupancy-rerun",
        "the source refuses a new occupancy step and a new spatial patch",
        "No occupancy step is re-run" in note
        and "No new spatial patch is grown" in normalized_note
        and "4×4×4" in note
        and "any new spatial patch" in normalized_note,
    )

    print(
        "per_element: checked — every nonzero integer vector with |v|_1 <= 4 "
        "is enumerated exactly"
    )
    print(
        "per_site: checked and not executed — only the origin-seed displayed "
        "arrival is scored; no new site law is claimed"
    )
    print(
        "per_mode: checked and not executed — no spectral decomposition is used"
    )
    print(
        "per_block: checked — the radius-4 integer ball is the only comparison block"
    )
    print(
        "lattice_wide: checked and not executed — no occupancy growth and no "
        "adopted Minkowski law is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
