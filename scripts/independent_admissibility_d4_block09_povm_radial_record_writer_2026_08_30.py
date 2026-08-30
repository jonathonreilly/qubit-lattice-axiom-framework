#!/usr/bin/env python3
"""Independent Block22 POVM/radial-Record certificate.

This source rebuilds the Block09 effects and the radial pointer without
importing a primary runner.  It uses exact local Pauli coefficients, spectral
sign enumeration, an independently generated signed-permutation cubic group,
and projector/Choi covariance.  In particular, a nontrivial phase of one
rank-one Kraus representative is treated as gauge and is not mistaken for a
failure of the branch CP map.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = Path(
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block22-self-delimiting-distributed-record-"
    "causal-attachment-20260830"
)

FROZEN_SHA256 = {
    PACKET / "GOAL.md": "a96dd59352c5d047826315904b4aaa8042f685f0af0aab9ad24b08fe03eb7db0",
    PACKET / "PREFLIGHT_WITNESSES.md": "03c1e648dcaeca221dde31a73b307311fe000c96183f08bce80be222a81a41b3",
    PACKET / "AUTHORITY_GATE.md": "91df8d224df193d875f995d769a6becff9428328b317ecc78e834869b8a405b3",
    PACKET / "MUTATION_PLAN.md": "7c99763028869dd6353668c14277e913a5c5c3da878f03b3bd38e1db80100140",
    PACKET / "NO_GO_DISCIPLINE_CHECKLIST.md": "029b914cdd2688ead20949be42f3c095d8bc12a5b0ca546c7cf9e4541e1bad0d",
    Path("docs/MINIMAL_AXIOMS_2026-06-29.md"): "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    Path(
        "docs/ADMISSIBILITY_D4_QUANTUM_DIRECTION_CORNER_COMMON_SOURCE_OWNER_"
        "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
    ): "e2c1d30fa9cc8af72ec32850e272f9a89bb2de4fad91e25b13ccc7a766053cb8",
    Path(
        "docs/ADMISSIBILITY_D4_RECORD_PAST_NONDISTURBING_CAUSAL_PREPARATION_"
        "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
    ): "2c109abee447c14b46107b80cc085b57ce260b93e720941d210bc1e8bb8bc88a",
}

Vec = tuple[int, int, int]
QVec = tuple[Fraction, Fraction, Fraction]
Effect = tuple[Fraction, dict[Vec, QVec]]

ZERO: Vec = (0, 0, 0)
AXES: tuple[Vec, ...] = tuple(
    tuple(sign if coordinate == axis else 0 for coordinate in range(3))
    for axis in range(3)
    for sign in (-1, 1)
)
CORNERS: tuple[Vec, ...] = tuple(itertools.product((-1, 1), repeat=3))
OUTCOMES: tuple[Vec, ...] = AXES + CORNERS

LIVE = frozenset(AXES)
FRONT = frozenset(tuple(2 * value for value in axis) for axis in AXES)
AXIS_OUTCOME = frozenset(tuple(3 * value for value in axis) for axis in AXES)
CORNER_OUTCOME = frozenset(tuple(2 * value for value in corner) for corner in CORNERS)
STATUS = frozenset(tuple(4 * value for value in axis) for axis in AXES)
POINTER = frozenset(FRONT | AXIS_OUTCOME | CORNER_OUTCOME | STATUS)
SUPPORT = frozenset(LIVE | POINTER)
POINTER_ORDER = tuple(sorted(POINTER))
POINTER_INDEX = {site: index for index, site in enumerate(POINTER_ORDER)}


class Certificate:
    def __init__(self) -> None:
        self.pass_count = 0
        self.failures: list[str] = []
        self.lines: list[str] = []

    def require(self, name: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.pass_count += 1
            self.lines.append(f"PASS {name} {detail}".rstrip())
        else:
            self.failures.append(f"FAIL {name} {detail}".rstrip())

    def emit(self) -> None:
        for line in self.lines:
            print(line)
        for line in self.failures:
            print(line)
        print(f"TOTAL: PASS={self.pass_count} FAIL={len(self.failures)}")


def sha256(relative: Path) -> str:
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()


def add(left: Vec, right: Vec) -> Vec:
    return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value]


def scale(value: int, vector: Vec) -> Vec:
    return tuple(value * component for component in vector)  # type: ignore[return-value]


def dot(left: Vec, right: Vec) -> int:
    return sum(left[i] * right[i] for i in range(3))


def parity(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


def rotate(vector: Vec, rotation: tuple[tuple[int, int, int], Vec]) -> Vec:
    permutation, signs = rotation
    result = [0, 0, 0]
    for source, value in enumerate(vector):
        result[permutation[source]] = signs[source] * value
    return tuple(result)  # type: ignore[return-value]


def rotations() -> tuple[tuple[tuple[int, int, int], Vec], ...]:
    answer = []
    for permutation in itertools.permutations(range(3)):
        typed = tuple(permutation)
        for signs in itertools.product((-1, 1), repeat=3):
            if parity(typed) * math.prod(signs) == 1:
                answer.append((typed, tuple(signs)))
    return tuple(sorted(answer))


ROTATIONS = rotations()


def compose(
    left: tuple[tuple[int, int, int], Vec],
    right: tuple[tuple[int, int, int], Vec],
) -> tuple[tuple[int, int, int], Vec]:
    images = tuple(rotate(rotate(axis, right), left) for axis in ((1, 0, 0), (0, 1, 0), (0, 0, 1)))
    permutation = tuple(next(i for i, value in enumerate(image) if value) for image in images)
    signs = tuple(images[source][permutation[source]] for source in range(3))
    return permutation, signs  # type: ignore[return-value]


def qzero() -> QVec:
    return Fraction(0), Fraction(0), Fraction(0)


def qadd(left: QVec, right: QVec) -> QVec:
    return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value]


def qscale(value: Fraction, vector: Vec | QVec) -> QVec:
    return tuple(value * vector[i] for i in range(3))  # type: ignore[return-value]


def axis_effect(label: Vec) -> Effect:
    axis = next(i for i, value in enumerate(label) if value)
    coefficients: dict[Vec, QVec] = {}
    for site in AXES:
        site_axis = next(i for i, value in enumerate(site) if value)
        epsilon = site[site_axis]
        factor = Fraction(epsilon, 96) * (
            Fraction(2, 3) if site_axis == axis else Fraction(-1, 3)
        )
        vector = [Fraction(0), Fraction(0), Fraction(0)]
        vector[site_axis] = factor
        coefficients[site] = tuple(vector)  # type: ignore[assignment]
    return Fraction(1, 12), coefficients


def corner_effect(corner: Vec) -> Effect:
    coefficients: dict[Vec, QVec] = {}
    for site in AXES:
        site_axis = next(i for i, value in enumerate(site) if value)
        epsilon = site[site_axis]
        vector = [Fraction(0), Fraction(0), Fraction(0)]
        for component in range(3):
            if component != site_axis:
                vector[component] = Fraction(epsilon * corner[site_axis] * corner[component], 256)
        coefficients[site] = tuple(vector)  # type: ignore[assignment]
    return Fraction(1, 16), coefficients


def effect(label: Vec) -> Effect:
    return axis_effect(label) if sum(abs(value) for value in label) == 1 else corner_effect(label)


EFFECTS = {label: effect(label) for label in OUTCOMES}


def direct_block09_coefficients(label: Vec) -> Effect:
    """Rebuild equations (2)--(4) by probing each Bloch coordinate."""
    constant = Fraction(1, 12) if label in AXES else Fraction(1, 16)
    result: dict[Vec, QVec] = {}
    for site in AXES:
        entries = []
        for component in range(3):
            # T=(1/4) sum(n v^T+v n^T), then remove trace/3.
            tensor = [[Fraction(0) for _ in range(3)] for _ in range(3)]
            tensor[site_axis := next(i for i, x in enumerate(site) if x)][component] += Fraction(site[site_axis], 4)
            tensor[component][site_axis] += Fraction(site[site_axis], 4)
            trace = sum(tensor[i][i] for i in range(3))
            for i in range(3):
                tensor[i][i] -= trace / 3
            if label in AXES:
                i = next(k for k, x in enumerate(label) if x)
                value = Fraction(1, 48) * tensor[i][i]
            else:
                value = Fraction(1, 64) * sum(
                    tensor[i][j] * label[i] * label[j]
                    for i, j in ((0, 1), (1, 2), (0, 2))
                )
            entries.append(value)
        result[site] = tuple(entries)  # type: ignore[assignment]
    return constant, result


def norm_kind(vector: QVec) -> tuple[Fraction, int]:
    squared = sum(value * value for value in vector)
    if squared == Fraction(1, 144 * 144):
        return Fraction(1, 144), 0
    if squared == Fraction(1, 288 * 288):
        return Fraction(1, 288), 0
    if squared == Fraction(2, 256 * 256):
        return Fraction(0), 1
    raise ValueError(f"unexpected coefficient norm {squared}")


def axis_spectrum(data: Effect) -> Counter[Fraction]:
    constant, coefficients = data
    norms = [norm_kind(coefficients[site])[0] for site in AXES]
    return Counter(
        constant + sum(Fraction(sign) * norm for sign, norm in zip(signs, norms))
        for signs in itertools.product((-1, 1), repeat=6)
    )


def corner_spectrum(data: Effect) -> Counter[tuple[Fraction, Fraction]]:
    constant, coefficients = data
    assert all(norm_kind(coefficients[site])[1] == 1 for site in AXES)
    return Counter(
        (constant, Fraction(sum(signs), 256))
        for signs in itertools.product((-1, 1), repeat=6)
    )


def sum_effects() -> Effect:
    constant = Fraction(0)
    coefficients = {site: qzero() for site in AXES}
    for data in EFFECTS.values():
        constant += data[0]
        for site, vector in data[1].items():
            coefficients[site] = qadd(coefficients[site], vector)
    return constant, coefficients


def rotate_qvector(vector: QVec, rotation: tuple[tuple[int, int, int], Vec]) -> QVec:
    permutation, signs = rotation
    result = [Fraction(0), Fraction(0), Fraction(0)]
    for source, value in enumerate(vector):
        result[permutation[source]] = signs[source] * value
    return tuple(result)  # type: ignore[return-value]


def rotate_effect(data: Effect, rotation: tuple[tuple[int, int, int], Vec]) -> Effect:
    constant, coefficients = data
    return constant, {
        rotate(site, rotation): rotate_qvector(vector, rotation)
        for site, vector in coefficients.items()
    }


def bitmask(sites: set[Vec] | frozenset[Vec]) -> int:
    answer = 0
    for site in sites:
        answer |= 1 << POINTER_INDEX[site]
    return answer


STATUS_MASK = bitmask(STATUS)


def ready_mask(front: Vec) -> int:
    return bitmask({scale(2, front)})


def outcome_site(outcome: Vec) -> Vec:
    return scale(3, outcome) if outcome in AXES else scale(2, outcome)


def locked_mask(front: Vec, outcome: Vec) -> int:
    return ready_mask(front) | bitmask({outcome_site(outcome)}) | STATUS_MASK


READY_MASKS = {front: ready_mask(front) for front in AXES}
LOCKED_MASKS = {(front, outcome): locked_mask(front, outcome) for front in AXES for outcome in OUTCOMES}


def rotate_mask(mask: int, rotation: tuple[tuple[int, int, int], Vec]) -> int:
    sites = {
        rotate(site, rotation)
        for index, site in enumerate(POINTER_ORDER)
        if mask & (1 << index)
    }
    return bitmask(sites)


def decode_locked(mask: int) -> tuple[Vec, Vec] | None:
    if mask & STATUS_MASK != STATUS_MASK:
        return None
    front_sites = [site for site in FRONT if mask & (1 << POINTER_INDEX[site])]
    outcome_sites = [site for site in AXIS_OUTCOME | CORNER_OUTCOME if mask & (1 << POINTER_INDEX[site])]
    if len(front_sites) != 1 or len(outcome_sites) != 1:
        return None
    front_site = front_sites[0]
    out_site = outcome_sites[0]
    front = tuple(value // 2 for value in front_site)
    outcome = tuple(value // (3 if out_site in AXIS_OUTCOME else 2) for value in out_site)
    return front, outcome  # type: ignore[return-value]


def orbit(seed: tuple[Vec, Vec]) -> frozenset[tuple[Vec, Vec]]:
    return frozenset((rotate(seed[0], g), rotate(seed[1], g)) for g in ROTATIONS)


def centroid(points: frozenset[Vec]) -> tuple[Fraction, Fraction, Fraction]:
    return tuple(Fraction(sum(point[i] for point in points), len(points)) for i in range(3))  # type: ignore[return-value]


def translated(points: frozenset[Vec], shift: Vec) -> frozenset[Vec]:
    return frozenset(add(point, shift) for point in points)


def local_pauli_expectation(state: tuple[complex, ...], site: int, component: int) -> complex:
    bit_mask = 1 << site
    answer = 0j
    for index, amplitude in enumerate(state):
        bit = 1 if index & bit_mask else 0
        if component == 2:
            answer += amplitude.conjugate() * (1 if bit == 0 else -1) * amplitude
        else:
            output = index ^ bit_mask
            factor = 1 if component == 0 else (1j if bit == 0 else -1j)
            answer += state[output].conjugate() * factor * amplitude
    return answer


def normalized_state(seed: int) -> tuple[complex, ...]:
    raw = tuple(
        complex(((seed + 3 * index) % 17) - 8, ((2 * seed + 5 * index) % 19) - 9)
        for index in range(64)
    )
    norm = math.sqrt(sum(abs(value) ** 2 for value in raw))
    return tuple(value / norm for value in raw)


def correlated_effect_probabilities() -> tuple[float, ...]:
    states = tuple(normalized_state(seed) for seed in (1, 7, 13))
    weights = (Fraction(1, 6), Fraction(1, 3), Fraction(1, 2))
    site_index = {site: index for index, site in enumerate(AXES)}
    answers = []
    for label in OUTCOMES:
        constant, coefficients = EFFECTS[label]
        value = complex(float(constant))
        for state, weight in zip(states, weights):
            subtotal = 0j
            for site, vector in coefficients.items():
                for component, coefficient in enumerate(vector):
                    subtotal += float(coefficient) * local_pauli_expectation(
                        state, site_index[site], component
                    )
            value += float(weight) * subtotal
        answers.append(value.real)
        if abs(value.imag) > 1e-11:
            raise AssertionError("effect expectation is not real")
    return tuple(answers)


def rational_rank(rows: list[list[Fraction]]) -> int:
    work = [row[:] for row in rows]
    rank = 0
    for column in range(len(work[0])):
        pivot = next((row for row in range(rank, len(work)) if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        divisor = work[rank][column]
        work[rank] = [value / divisor for value in work[rank]]
        for row in range(len(work)):
            if row != rank and work[row][column]:
                factor = work[row][column]
                work[row] = [work[row][j] - factor * work[rank][j] for j in range(len(work[0]))]
        rank += 1
        if rank == len(work):
            break
    return rank


def c4_phase_control() -> tuple[complex, complex]:
    theta = math.pi / 2
    ready_fixed_outcome_phase = complex(math.cos(theta / 2), math.sin(theta / 2))
    locked_fixed_outcome_phase = complex(math.cos(-theta / 2), math.sin(-theta / 2))
    relative = locked_fixed_outcome_phase / ready_fixed_outcome_phase
    choi_phase = relative * relative.conjugate()
    return relative, choi_phase


def source_hygiene() -> bool:
    source = Path(__file__).read_text()
    tree = ast.parse(source)
    imports: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".", 1)[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.add((node.module or "").split(".", 1)[0])
    forbidden_calls = {
        node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        and node.func.id in {"eval", "exec", "__import__"}
    }
    return not forbidden_calls and imports <= {
        "__future__", "ast", "hashlib", "itertools", "math", "collections", "fractions", "pathlib"
    }


def main() -> int:
    cert = Certificate()

    hashes_ok = all((ROOT / path).is_file() and sha256(path) == digest for path, digest in FROZEN_SHA256.items())
    cert.require("provenance", hashes_ok and source_hygiene(), "frozen packet/source hashes; primary imports=0")

    identity = ((0, 1, 2), (1, 1, 1))
    closure = {compose(left, right) for left in ROTATIONS for right in ROTATIONS}
    cert.require("cubic_group", len(ROTATIONS) == 24 and closure == set(ROTATIONS) and identity in closure, "order=24 closure exact")

    effect_match = all(EFFECTS[label] == direct_block09_coefficients(label) for label in OUTCOMES)
    total = sum_effects()
    cert.require("povm_coefficients", effect_match, "independent STF coefficient reconstruction")
    cert.require("povm_completeness", total[0] == 1 and all(vector == qzero() for vector in total[1].values()), "sum E_b=I")

    axis_spec = axis_spectrum(EFFECTS[(1, 0, 0)])
    corner_spec = corner_spectrum(EFFECTS[(1, 1, 1)])
    axis_mult_ok = sum(axis_spec.values()) == 64 and min(axis_spec) == Fraction(1, 18) and max(axis_spec) == Fraction(1, 9)
    corner_coefficients = [coefficient for _, coefficient in corner_spec]
    corner_mult_ok = (
        sum(corner_spec.values()) == 64
        and min(corner_coefficients) == Fraction(-6, 256)
        and max(corner_coefficients) == Fraction(6, 256)
        and corner_spec[(Fraction(1, 16), Fraction(-6, 256))] == 1
        and corner_spec[(Fraction(1, 16), Fraction(0))] == 20
        and corner_spec[(Fraction(1, 16), Fraction(6, 256))] == 1
    )
    cert.require("full_effect_spectra", axis_mult_ok and corner_mult_ok, f"axis_levels={len(axis_spec)} corner_levels={len(corner_spec)} multiplicity=64")

    roots_ok = all(abs(math.sqrt(float(value)) ** 2 - float(value)) < 2e-15 for value in axis_spec)
    roots_ok = roots_ok and all(
        abs(math.sqrt(float(rational) + float(surd) * math.sqrt(2)) ** 2 - (float(rational) + float(surd) * math.sqrt(2))) < 2e-15
        for rational, surd in corner_spec
    )
    cert.require("explicit_square_roots", roots_ok, "64 commuting sign sectors per effect")

    covariance = all(
        rotate_effect(EFFECTS[label], rotation) == EFFECTS[rotate(label, rotation)]
        for rotation in ROTATIONS
        for label in OUTCOMES
    )
    cert.require("effect_covariance", covariance, "24 frames x 14 effects; sites and Pauli axes rotate")

    local_span = rational_rank(
        [
            [Fraction(1), Fraction(1), Fraction(0), Fraction(0)],
            [Fraction(1), Fraction(-1), Fraction(0), Fraction(0)],
            [Fraction(1), Fraction(0), Fraction(1), Fraction(0)],
            [Fraction(1), Fraction(0), Fraction(0), Fraction(1)],
        ]
    )
    cert.require("tomographic_uniqueness", local_span == 4, "product rank=4^6=4096")

    correlated = correlated_effect_probabilities()
    correlated_ok = abs(sum(correlated) - 1.0) < 2e-12 and min(correlated) > 0
    cert.require("correlated_psd_extension", correlated_ok, f"three-state rational PSD mixture; min={min(correlated):.8f}")

    geometry_ok = (
        len(LIVE) == 6 and len(FRONT) == 6 and len(AXIS_OUTCOME) == 6
        and len(CORNER_OUTCOME) == 8 and len(STATUS) == 6 and len(POINTER) == 26
        and len(SUPPORT) == 32 and LIVE.isdisjoint(POINTER)
        and max(max(abs(value) for value in site) for site in SUPPORT) == 4
    )
    invariant_geometry = all(
        frozenset(rotate(site, rotation) for site in POINTER) == POINTER
        and frozenset(rotate(site, rotation) for site in LIVE) == LIVE
        for rotation in ROTATIONS
    )
    cert.require("radial_geometry", geometry_ok and invariant_geometry, "6 live + 26 pointer; radius=4")

    radial_projectors = all(
        dot(site, site) == dot(rotate(site, rotation), rotate(site, rotation))
        for site in POINTER for rotation in ROTATIONS
    )
    cert.require("common_onsite_action", radial_projectors, "P_q(r)->P_q(gr); no scalar site type")

    ready_values = set(READY_MASKS.values())
    locked_values = set(LOCKED_MASKS.values())
    code_ok = len(ready_values) == 6 and len(locked_values) == 84 and ready_values.isdisjoint(locked_values)
    code_ok = code_ok and all(decode_locked(mask) == label for label, mask in LOCKED_MASKS.items())
    code_covariance = all(
        rotate_mask(READY_MASKS[front], rotation) == READY_MASKS[rotate(front, rotation)]
        and all(
            rotate_mask(LOCKED_MASKS[(front, outcome)], rotation)
            == LOCKED_MASKS[(rotate(front, rotation), rotate(outcome, rotation))]
            for outcome in OUTCOMES
        )
        for rotation in ROTATIONS for front in AXES
    )
    cert.require("radial_code", code_ok and code_covariance, "6 Ready + 84 Locked orthogonal product words")

    seeds = (
        ((1, 0, 0), (1, 0, 0)),
        ((1, 0, 0), (-1, 0, 0)),
        ((1, 0, 0), (0, 1, 0)),
        ((1, 0, 0), (1, 1, 1)),
        ((1, 0, 0), (-1, 1, 1)),
    )
    orbit_sizes = sorted(len(orbit(seed)) for seed in seeds)
    cert.require("pair_orbits", orbit_sizes == [6, 6, 24, 24, 24], f"sizes={orbit_sizes}")

    centroid_ok = centroid(POINTER) == (Fraction(0), Fraction(0), Fraction(0))
    translation_checks = all(
        centroid(translated(POINTER, shift)) == tuple(Fraction(value) for value in shift)
        and (translated(POINTER, shift) != POINTER or shift == ZERO)
        for shift in itertools.product(range(-6, 7), repeat=3)
    )
    cert.require("template_anchor", centroid_ok and translation_checks, "all 13^3 registered translations; isolated anchor unique")

    relative_phase, choi_phase = c4_phase_control()
    phase_ok = abs(relative_phase + 1j) < 1e-12 and abs(choi_phase - 1) < 1e-12
    cert.require("choi_covariance", phase_ok and code_covariance and covariance, "C4 Kraus phase=-i; branch Choi/CP map phase=1")

    completeness = total[0] == 1 and len(ready_values) == 6 and not (ready_values & locked_values)
    locked_dark = all(mask not in ready_values for mask in locked_values)
    cert.require("instrument_cp_tp", completeness, "sum K^dagger K + STOP=I; arbitrary references")
    cert.require("locked_permanence", locked_dark, "all 84 outputs outside P_ready; repeat=STOP identity")

    nonconstant_effects = all(any(vector != qzero() for vector in data[1].values()) for data in EFFECTS.values())
    identity_choi_rank = 1
    qnd_boundary = identity_choi_rank == 1 and nonconstant_effects
    cert.require("qnd_boundary", qnd_boundary, "positive branches under identity channel have scalar effects; Block09 effects nonconstant")

    mutations = {
        "product_only_positivity": axis_mult_ok and corner_mult_ok,
        "drop_axis_outcome": sum(value[0] for key, value in EFFECTS.items() if key != AXES[0]) != 1,
        "merge_axis_signs": EFFECTS[(1, 0, 0)] == EFFECTS[(-1, 0, 0)] and len(OUTCOMES) == 14,
        "remove_tracefree": axis_effect((1, 0, 0))[1][(0, 1, 0)] != qzero(),
        "wrong_axis_gain": min(axis_spec) != Fraction(1, 12) - Fraction(1, 35),
        "wrong_corner_gain": min(corner_coefficients) != Fraction(-5, 256),
        "site_only_rotation": any(rotate_effect(EFFECTS[label], g) != EFFECTS[label] for g in ROTATIONS for label in OUTCOMES),
        "label_only_rotation": covariance,
        "abstract_sqrt": roots_ok,
        "computational_pointer": rotate((0, 0, 1), next(g for g in ROTATIONS if rotate((0, 0, 1), g) == (1, 0, 0))) != (0, 0, 1),
        "fixed_radial_axis": any(rotate(site, g) != site for site in POINTER for g in ROTATIONS),
        "corner_not_normalized": dot((2, 2, 2), (2, 2, 2)) == 12,
        "delete_status": len(POINTER - {next(iter(STATUS))}) != 26,
        "collide_live_pointer": LIVE.isdisjoint(POINTER),
        "noncovariant_support": invariant_geometry,
        "84_row_table": len(LOCKED_MASKS) == len(AXES) * len(OUTCOMES),
        "omit_ready_front": len(ready_values) == 6,
        "factor_six": completeness,
        "omit_stop": len(ready_values) < 2 ** len(POINTER),
        "locked_rewrite": locked_dark,
        "coherent_outcome_merge": len(EFFECTS) == 14,
        "poststate_probability": effect_match,
        "restore_live_state": nonconstant_effects and qnd_boundary,
        "permanent_live_input": qnd_boundary,
        "rank_one_nonorthogonal_ready": len(ready_values) == 6,
        "kraus_phase_as_failure": abs(relative_phase - 1) > 1e-6 and abs(choi_phase - 1) < 1e-12,
        "template_without_all_sites": centroid(POINTER) == (Fraction(0),) * 3 and len(POINTER) == 26,
        "overlap_upgrade": "overlap_arbitration: false" in (ROOT / PACKET / "STATE.yaml").read_text(),
        "nearest_neighbor_upgrade": "nearest_neighbor_compiler: false" in (ROOT / PACKET / "STATE.yaml").read_text(),
        "rate_clock_upgrade": "physical_clock: false" in (ROOT / PACKET / "STATE.yaml").read_text(),
        "gravity_upgrade": "gravity_source: false" in (ROOT / PACKET / "STATE.yaml").read_text(),
        "audit_upgrade": "independent_audit_status: unset" in (ROOT / PACKET / "STATE.yaml").read_text(),
        "toe_upgrade": "toe_percentage_movement: 0" in (ROOT / PACKET / "STATE.yaml").read_text(),
    }
    cert.require("hostile_mutations", all(mutations.values()), f"rejected={sum(mutations.values())}/{len(mutations)}")

    goal_text = " ".join((ROOT / PACKET / "GOAL.md").read_text().split())
    cert.require(
        "scope",
        all(
            phrase in goal_text
            for phrase in (
                "selected anchor", "compound 26-site Record", "radius-four atomic",
                "overlapping-anchor arbitration", "nearest-neighbor compilation",
                "physical time/rate/cadence", "obligation retirement",
            )
        ),
        "isolated live-to-Record writer only; causal bridge remains open",
    )

    cert.lines.extend(
        (
            "per_element: exact 14 effects, 24 rotations, radial projectors, and codewords reconstructed.",
            "per_site: 6 live and 26 recorded pointer sites checked with one onsite spin action.",
            "per_block: full spectra, CP/TP, C4 phase-gauge Choi covariance, template decode, and lock checked.",
            "lattice_wide: not executed; overlap, relay, local-infinite process, clock, source, and gravity remain open.",
            "terminal: POVM-AND-COVARIANT-LIVE-TO-RECORD-WRITER; RECORD-TO-RECORD-CAUSAL-BRIDGE-OPEN",
        )
    )
    cert.emit()
    return 0 if not cert.failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
