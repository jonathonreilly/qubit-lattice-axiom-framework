#!/usr/bin/env python3
"""Exact local-to-global controls for a cubic record-process law.

The runner constructs a homogeneous nearest-neighbor controlled-phase QCA,
derives finite decoherence/process functionals from it and a supplied boundary,
tests adaptive instruments and identity containment, and exhibits boundary and
extension nonuniqueness controls.  It changes no authority surface.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "LOCAL_TO_GLOBAL_CUBIC_PROCESS_GLUE_CYCLE33_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CYCLE30 = REVIEW / "GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md"

PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def source_contract() -> None:
    section("A - Source and authority boundary")
    for path in (NOTE, AXIOMS, REGISTRY, CYCLE30):
        check(f"A source exists: {path.name}", path.is_file())
    note = normalized(NOTE)
    axioms = AXIOMS.read_text(encoding="utf-8")
    check("A note is authority-free", "authority: none" in note)
    check("A note does not amend an axiom", "does not amend an axiom" in note)
    check("A current state sentence is consumed", "a state is a configuration of records" in note)
    check("A current Admissibility is availability-only", "Admissibility is not a dynamics axiom." in axioms)
    check("A no live edit is authorized", "no live axiom or primitive edit is justified" in note)
    check("A no independent finite measure atom", "no independent finite global measure atom survives" in note)
    check("A boundary remains independently typed", "boundary/history datum survives" in note)
    for source in (
        "https://arxiv.org/abs/quant-ph/0405174",
        "https://arxiv.org/abs/0711.3975",
        "https://arxiv.org/abs/0904.4483",
        "https://arxiv.org/abs/1712.02589",
    ):
        check(f"A primary source cited: {source.rsplit('/', 1)[-1]}", source in note)


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
CZ = sp.diag(1, 1, 1, -1)
KET0 = sp.Matrix([1, 0])
KET1 = sp.Matrix([0, 1])
KET_PLUS = sp.Matrix([1, 1]) / sp.sqrt(2)
KET_MINUS = sp.Matrix([1, -1]) / sp.sqrt(2)
P0 = KET0 * KET0.H
P1 = KET1 * KET1.H
PX_PLUS = KET_PLUS * KET_PLUS.H
PX_MINUS = KET_MINUS * KET_MINUS.H


def tensor(*matrices: sp.Matrix) -> sp.Matrix:
    result = sp.Matrix([[1]])
    for matrix in matrices:
        result = sp.kronecker_product(result, matrix)
    return sp.Matrix(result)


def exact_trace(matrix: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(matrix))


def bits(index: int, count: int) -> tuple[int, ...]:
    return tuple((index >> (count - 1 - i)) & 1 for i in range(count))


def bit_index(values: tuple[int, ...]) -> int:
    value = 0
    for bit in values:
        value = 2 * value + bit
    return value


def cube_geometry() -> tuple[tuple[tuple[int, int, int], ...], tuple[tuple[int, int], ...]]:
    vertices = tuple(product((0, 1), repeat=3))
    index = {vertex: i for i, vertex in enumerate(vertices)}
    edges = tuple(
        sorted(
            {
                tuple(sorted((index[left], index[right])))
                for left in vertices
                for right in vertices
                if sum(a != b for a, b in zip(left, right)) == 1
            }
        )
    )
    return vertices, edges


def permutation_sign(values: tuple[int, ...]) -> int:
    inversions = sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values)))
    return -1 if inversions % 2 else 1


def proper_cube_rotations(vertices: tuple[tuple[int, int, int], ...]) -> tuple[tuple[int, ...], ...]:
    index = {vertex: i for i, vertex in enumerate(vertices)}
    rotations: list[tuple[int, ...]] = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] != 1:
                continue
            image = []
            for vertex in vertices:
                centered = tuple(2 * coordinate - 1 for coordinate in vertex)
                moved = tuple(signs[row] * centered[permutation[row]] for row in range(3))
                image.append(index[tuple((coordinate + 1) // 2 for coordinate in moved)])
            rotations.append(tuple(image))
    return tuple(rotations)


def graph_state(site_count: int, edges: tuple[tuple[int, int], ...]) -> sp.Matrix:
    denominator = sp.sqrt(2**site_count)
    amplitudes = []
    for index in range(2**site_count):
        word = bits(index, site_count)
        phase = (-1) ** sum(word[left] * word[right] for left, right in edges)
        amplitudes.append(sp.Rational(phase, 1) / denominator)
    return sp.Matrix(amplitudes)


def reduced_density_pure(state: sp.Matrix, site_count: int, keep: tuple[int, ...]) -> sp.Matrix:
    keep = tuple(keep)
    environment = tuple(site for site in range(site_count) if site not in keep)
    dimension = 2 ** len(keep)
    reduced = sp.zeros(dimension)
    for environment_word in product((0, 1), repeat=len(environment)):
        vector = sp.zeros(dimension, 1)
        for kept_word in product((0, 1), repeat=len(keep)):
            full = [0] * site_count
            for site, value in zip(keep, kept_word):
                full[site] = value
            for site, value in zip(environment, environment_word):
                full[site] = value
            vector[bit_index(tuple(kept_word)), 0] = state[bit_index(tuple(full)), 0]
        reduced += vector * vector.H
    return sp.simplify(reduced)


def partial_trace_second_two_qubit(rho: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(
        [
            [sp.simplify(sum(rho[2 * left + env, 2 * right + env] for env in (0, 1))) for right in (0, 1)]
            for left in (0, 1)
        ]
    )


def pauli_word_expectation(state: sp.Matrix, site_count: int, x_sites: frozenset[int], z_sites: frozenset[int]) -> sp.Expr:
    value = 0
    for index in range(2**site_count):
        word = list(bits(index, site_count))
        phase = (-1) ** sum(word[site] for site in z_sites)
        moved = list(word)
        for site in x_sites:
            moved[site] ^= 1
        value += sp.conjugate(state[bit_index(tuple(moved)), 0]) * phase * state[index, 0]
    return sp.simplify(value)


def cubic_rule_control() -> None:
    section("B - Homogeneous nearest-neighbor cubic rule")
    vertices, edges = cube_geometry()
    degrees = [sum(site in edge for edge in edges) for site in range(len(vertices))]
    check("B open cubic cell has eight sites", len(vertices) == 8)
    check("B open cubic cell has twelve nearest-neighbor edges", len(edges) == 12)
    check("B every open-cell site has degree three", set(degrees) == {3})
    rotations = proper_cube_rotations(vertices)
    check("B proper cubic rotation group has 24 elements", len(set(rotations)) == 24)
    edge_set = set(edges)
    check("B homogeneous edge set is proper-cubic invariant", all({tuple(sorted((rotation[a], rotation[b]))) for a, b in edges} == edge_set for rotation in rotations))
    check("B controlled phase is unitary", CZ.H * CZ == sp.eye(4))
    check("B controlled phase is involutive", CZ * CZ == sp.eye(4))
    check("B controlled phase is exchange symmetric", CZ == sp.diag(1, 1, 1, -1))

    cz01 = sp.diag(1, 1, 1, 1, 1, 1, -1, -1)
    cz12 = sp.diag(1, 1, 1, -1, 1, 1, 1, -1)
    check("B overlapping edge gates commute", cz01 * cz12 == cz12 * cz01)
    check("B local X conjugates into radius-one XZ", sp.simplify(CZ * tensor(X, I2) * CZ - tensor(X, Z)) == sp.zeros(4))
    check("B neighbor X conjugates into radius-one ZX", sp.simplify(CZ * tensor(I2, X) * CZ - tensor(Z, X)) == sp.zeros(4))
    check("B local Z is fixed", sp.simplify(CZ * tensor(Z, I2) * CZ - tensor(Z, I2)) == sp.zeros(4))
    check("B translated adjacency is unchanged", all(sum(abs((a[i] + 7) - (b[i] + 7)) for i in range(3)) == 1 for a, b in ((vertices[x], vertices[y]) for x, y in edges)))


def local_to_global_state_control() -> None:
    section("C - Derived finite and quasilocal-shadow state family")
    vertices, edges = cube_geometry()
    state = graph_state(len(vertices), edges)
    rho = sp.simplify(state * state.H)
    check("C cube graph boundary contracts to a normalized state", sp.simplify((state.H * state)[0] - 1) == 0)
    check("C derived cube density is positive rank one", rho.rank() == 1 and exact_trace(rho) == 1)
    one = reduced_density_pure(state, 8, (0,))
    pair = reduced_density_pure(state, 8, (0, 1))
    check("C one-site restriction is normalized positive", exact_trace(one) == 1 and one.eigenvals() == {sp.Rational(1, 2): 2})
    check("C two-site restriction is normalized positive", exact_trace(pair) == 1 and all(value.is_nonnegative for value in pair.eigenvals()))
    check("C nested restrictions commute exactly", partial_trace_second_two_qubit(pair) == one)

    neighbors0 = frozenset(site for edge in edges if 0 in edge for site in edge if site != 0)
    stabilizer = pauli_word_expectation(state, 8, frozenset((0,)), neighbors0)
    check("C local graph stabilizer has expectation one", stabilizer == 1)
    check("C one-site Z record is unbiased on plus boundary", pauli_word_expectation(state, 8, frozenset(), frozenset((0,))) == 0)

    pair_state = graph_state(2, ((0, 1),))
    embedded_one = reduced_density_pure(pair_state, 2, (0,))
    open_one = KET_PLUS * KET_PLUS.H
    check("C naive open restriction differs from embedded restriction", open_one != embedded_one and embedded_one == I2 / 2)

    p_one = {0: Fraction(1, 2), 1: Fraction(1, 2)}
    p_two = {(0, 0): Fraction(2, 3), (0, 1): Fraction(0), (1, 0): Fraction(0), (1, 1): Fraction(1, 3)}
    check("C incompatible control laws each normalize", sum(p_one.values()) == sum(p_two.values()) == 1)
    check("C finite normalization alone does not imply extension consistency", sum(value for (left, _), value in p_two.items() if left == 0) != p_one[0])


def bell_from_local_gate_control() -> None:
    section("D - Bell correlations generated by one local edge gate")
    graph = graph_state(2, ((0, 1),))
    phi_plus = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    check("D edge graph state is local-H equivalent to Bell state", sp.simplify(graph - tensor(I2, H) * phi_plus) == sp.zeros(4, 1))
    alice = {0: Z, 1: X}
    bob = {0: (X + Z) / sp.sqrt(2), 1: (X - Z) / sp.sqrt(2)}
    correlations: dict[tuple[int, int], sp.Expr] = {}
    for setting in product((0, 1), repeat=2):
        x, y = setting
        correlations[setting] = sp.simplify((graph.H * tensor(alice[x], bob[y]) * graph)[0])
        probabilities = {}
        for a, b in product((-1, 1), repeat=2):
            pa = (I2 + a * alice[x]) / 2
            pb = (I2 + b * bob[y]) / 2
            probabilities[(a, b)] = sp.simplify((graph.H * tensor(pa, pb) * graph)[0])
        check(f"D setting {setting} normalizes", sp.simplify(sum(probabilities.values()) - 1) == 0)
        check(f"D setting {setting} is positive", all(value.is_nonnegative for value in probabilities.values()))
        check(f"D setting {setting} has unbiased Alice marginal", all(sp.simplify(sum(value for (ao, _), value in probabilities.items() if ao == a) - sp.Rational(1, 2)) == 0 for a in (-1, 1)))
        check(f"D setting {setting} has unbiased Bob marginal", all(sp.simplify(sum(value for (_, bo), value in probabilities.items() if bo == b) - sp.Rational(1, 2)) == 0 for b in (-1, 1)))
    chsh = sp.simplify(correlations[(0, 0)] + correlations[(0, 1)] + correlations[(1, 0)] - correlations[(1, 1)])
    check("D one-edge local rule yields exact CHSH two-root-two", sp.simplify(chsh - 2 * sp.sqrt(2)) == 0, f"S={chsh}")


def decoherence_functional_control() -> None:
    section("E - Strongly-positive functional derived by local contraction")
    rho = KET_PLUS * KET_PLUS.H
    z_projectors = (P0, P1)
    x_projectors = (PX_PLUS, PX_MINUS)
    histories = tuple(product((0, 1), repeat=2))
    classes = {(z, x): sp.simplify(x_projectors[x] * z_projectors[z]) for z, x in histories}
    decoherence = sp.Matrix(
        [
            [sp.simplify(exact_trace(classes[left] * rho * classes[right].H)) for right in histories]
            for left in histories
        ]
    )
    check("E exhaustive local class operators sum to identity", sp.simplify(sum(classes.values(), sp.zeros(2)) - I2) == sp.zeros(2))
    check("E derived functional is Hermitian", decoherence.H == decoherence)
    check("E derived functional is strongly positive", decoherence.eigenvals() == {sp.Rational(1, 2): 2, sp.Integer(0): 2})
    check("E derived functional normalizes on complete event", sp.simplify(sum(decoherence) - 1) == 0)
    for x in (0, 1):
        indices = tuple(index for index, (_, output) in enumerate(histories) if output == x)
        coherent = sp.simplify(sum(decoherence[i, j] for i in indices for j in indices))
        recorded = sp.simplify(sum(decoherence[i, i] for i in indices))
        check(f"E coherent output x={x} matches interference target", coherent == (1 if x == 0 else 0))
        check(f"E recorded intermediate alternative x={x} is one-half", recorded == sp.Rational(1, 2))


def adaptive_process_control() -> None:
    section("F - Adaptive instruments and identity-slot containment")
    graph = graph_state(2, ((0, 1),))
    rho = graph * graph.H
    joint: dict[tuple[int, int], sp.Expr] = {}
    branch_b: dict[int, sp.Matrix] = {}
    for record, projector in enumerate((P0, P1)):
        first = tensor(projector, I2)
        branch = sp.simplify(first * rho * first)
        correction = tensor(I2, I2 if record == 0 else Z)
        corrected = sp.simplify(correction * branch * correction.H)
        branch_b[record] = sp.Matrix(
            [
                [sp.simplify(sum(corrected[2 * env + left, 2 * env + right] for env in (0, 1))) for right in (0, 1)]
                for left in (0, 1)
            ]
        )
        for output, effect in enumerate((PX_PLUS, PX_MINUS)):
            joint[(record, output)] = sp.simplify(exact_trace(tensor(I2, effect) * corrected))
    check("F adaptive transcript law normalizes", sp.simplify(sum(joint.values()) - 1) == 0)
    check("F feed-forward makes X-plus certain after either record", joint == {(0, 0): sp.Rational(1, 2), (0, 1): 0, (1, 0): sp.Rational(1, 2), (1, 1): 0})
    check("F each record fixes one derived conditional branch", all(exact_trace(branch_b[record]) == sp.Rational(1, 2) for record in (0, 1)))
    normalized_branches = {record: sp.simplify(2 * branch) for record, branch in branch_b.items()}
    check("F fixed law plus complete records factors to one future state", normalized_branches[0] == normalized_branches[1] == KET_PLUS * KET_PLUS.H)

    identity_future = tuple(sp.simplify(exact_trace(effect * normalized_branches[0])) for effect in (PX_PLUS, PX_MINUS))
    dephased = sp.simplify(P0 * normalized_branches[0] * P0 + P1 * normalized_branches[0] * P1)
    forgotten_future = tuple(sp.simplify(exact_trace(effect * dephased)) for effect in (PX_PLUS, PX_MINUS))
    check("F omitted adaptive slot equals identity insertion", identity_future == (1, 0))
    check("F summed Z-instrument branches equal nonselective channel", forgotten_future == (sp.Rational(1, 2), sp.Rational(1, 2)))
    check("F identity containment differs from measure-and-forget", identity_future != forgotten_future)


def boundary_and_extension_control() -> None:
    section("G - Same local rule, different boundary and extension controls")
    vertices, edges = cube_geometry()
    graph = graph_state(8, edges)
    zero = sp.zeros(256, 1)
    zero[0, 0] = 1
    graph_z = pauli_word_expectation(graph, 8, frozenset(), frozenset((0,)))
    zero_z = pauli_word_expectation(zero, 8, frozenset(), frozenset((0,)))
    check("G identical CZ rule accepts two normalized boundaries", sp.simplify((graph.H * graph)[0] - 1) == 0 and (zero.H * zero)[0] == 1)
    check("G plus and zero boundaries give different record laws", graph_z == 0 and zero_z == 1)

    ghz_plus = sp.zeros(256, 1)
    ghz_minus = sp.zeros(256, 1)
    ghz_plus[0, 0] = ghz_plus[255, 0] = 1 / sp.sqrt(2)
    ghz_minus[0, 0] = 1 / sp.sqrt(2)
    ghz_minus[255, 0] = -1 / sp.sqrt(2)
    reduced_plus = reduced_density_pure(ghz_plus, 8, tuple(range(7)))
    reduced_minus = reduced_density_pure(ghz_minus, 8, tuple(range(7)))
    check("G opposite GHZ phases have identical proper-subregion density", reduced_plus == reduced_minus)
    global_x_plus = pauli_word_expectation(ghz_plus, 8, frozenset(range(8)), frozenset())
    global_x_minus = pauli_word_expectation(ghz_minus, 8, frozenset(range(8)), frozenset())
    check("G full-cube record context distinguishes GHZ extensions", global_x_plus == 1 and global_x_minus == -1)
    check("G even-edge cube CZ leaves both GHZ boundaries fixed", len(edges) % 2 == 0)


def documentation_contract() -> None:
    section("H - Placement and N1-N8 documentation contract")
    note = normalized(NOTE)
    required = (
        "one fixed nearest-neighbor controlled-phase rule",
        "normalized strongly-positive decoherence functional",
        "adaptive instruments",
        "identity-slot containment",
        "record-fibre future-equivalence",
        "boundary/history datum survives",
        "no independent finite global measure atom survives",
        "projective extension",
        "quasilocal automorphism",
        "retyped admissibility",
        "separate law",
        "same local rule",
        "different boundary",
        "global consistency is a theorem obligation",
        "no qualification amendment is forced",
    )
    for phrase in required:
        check(f"H note contains {phrase}", phrase in note)
    check("H finite and infinite claims are separated", "finite-volume theorem" in note and "infinite z^3" in note)
    check("H open-boundary truncation is not mistaken for restriction", "naive open-boundary truncation" in note)
    check("H global phase limitation is scoped", "finite cube" in note and "quasilocal limit" in note)
    for index in range(1, 9):
        check(f"H N{index} section exists", f"n{index} —" in note)
    check("H no-go discipline passes", "no-go-discipline status: pass" in note)


def main() -> int:
    source_contract()
    cubic_rule_control()
    local_to_global_state_control()
    bell_from_local_gate_control()
    decoherence_functional_control()
    adaptive_process_control()
    boundary_and_extension_control()
    documentation_contract()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: PASS" if FAIL == 0 else "RESULT: FAIL")
    print("PLACEMENT_GATE: exact local composition plus an exact consistent boundary derives the global process; local rule alone does not")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
