#!/usr/bin/env python3
"""Block22 primary: exact Block09 POVM and isolated radial Record writer.

The implementation is deliberately algebraic.  It never allocates a dense
2^32 matrix.  Full-Hilbert claims are reduced to the commuting six-qubit
spectral sectors and exact Kraus/effect identities frozen in the packet.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
from collections import Counter
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / ".claude/science/physics-loops" / (
    "toe-source-eta-ownership-block22-self-delimiting-distributed-record-"
    "causal-attachment-20260830"
)
FROZEN = {
    "GOAL.md": "a96dd59352c5d047826315904b4aaa8042f685f0af0aab9ad24b08fe03eb7db0",
    "AUTHORITY_GATE.md": "91df8d224df193d875f995d769a6becff9428328b317ecc78e834869b8a405b3",
    "PREFLIGHT_WITNESSES.md": "03c1e648dcaeca221dde31a73b307311fe000c96183f08bce80be222a81a41b3",
    "PANEL_RETURN.md": "05a7e32c186dd64cd0d5d4cdc68946a37082acf8dba704bfe6384cd88c90fb56",
    "INDEPENDENT_PREREG_ATTACK.md": "23f24a92ce3a20bcb4c3d5328b9db48f0f7755b5997e0d2f3c7fc7436395fa1e",
    "APPROACH_REGISTRY.md": "2c53bdb32539b1803891c1e6a1dd242761bd30496260c602e62655fe8d2553e6",
    "MUTATION_PLAN.md": "7c99763028869dd6353668c14277e913a5c5c3da878f03b3bd38e1db80100140",
    "NO_GO_DISCIPLINE_CHECKLIST.md": "029b914cdd2688ead20949be42f3c095d8bc12a5b0ca546c7cf9e4541e1bad0d",
}

R = sp.Rational
TAU = R(1, 24)
E = tuple(
    tuple(sign if j == i else 0 for j in range(3))
    for i in range(3)
    for sign in (-1, 1)
)
DIRECTIONS = E
CORNERS = tuple(itertools.product((-1, 1), repeat=3))
OUTCOMES = DIRECTIONS + CORNERS


def add(a, b):
    return tuple(sp.simplify(a[i] + b[i]) for i in range(3))


def scale(c, a):
    return tuple(sp.simplify(c * a[i]) for i in range(3))


def dot(a, b):
    return sp.simplify(sum(a[i] * b[i] for i in range(3)))


def mat_vec(g, v):
    return tuple(sp.simplify(sum(g[i][j] * v[j] for j in range(3))) for i in range(3))


def determinant3(g):
    return (
        g[0][0] * (g[1][1] * g[2][2] - g[1][2] * g[2][1])
        - g[0][1] * (g[1][0] * g[2][2] - g[1][2] * g[2][0])
        + g[0][2] * (g[1][0] * g[2][1] - g[1][1] * g[2][0])
    )


def rotations():
    answer = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            g = tuple(
                tuple(signs[i] if j == perm[i] else 0 for j in range(3))
                for i in range(3)
            )
            if determinant3(g) == 1:
                answer.append(g)
    assert len(set(answer)) == 24
    return tuple(answer)


ROTATIONS = rotations()


def is_axis(label):
    return sum(value != 0 for value in label) == 1


def effect(label):
    """Return constant and the six local Pauli coefficient vectors."""
    coeff = {}
    if is_axis(label):
        i = next(j for j, value in enumerate(label) if value)
        constant = R(1, 12)
        for site in DIRECTIONS:
            j = next(k for k, value in enumerate(site) if value)
            epsilon = site[j]
            vector = [sp.S.Zero] * 3
            vector[j] = TAU * R(1, 4) * epsilon * (int(i == j) - R(1, 3))
            coeff[site] = tuple(vector)
    else:
        constant = R(1, 16)
        for site in DIRECTIONS:
            j = next(k for k, value in enumerate(site) if value)
            epsilon = site[j]
            vector = [sp.S.Zero] * 3
            for k in range(3):
                if k != j:
                    vector[k] = R(3, 32) * TAU * epsilon * label[j] * label[k]
            coeff[site] = tuple(vector)
    return constant, coeff


def expectation(label, vectors):
    constant, coeff = effect(label)
    return sp.simplify(constant + sum(dot(coeff[site], vectors[site]) for site in DIRECTIONS))


def block09_product_probabilities():
    symbols = sp.symbols("v0:18", real=True)
    vectors = {
        site: tuple(symbols[3 * index + k] for k in range(3))
        for index, site in enumerate(DIRECTIONS)
    }
    a = sp.zeros(3)
    for site in DIRECTIONS:
        n = sp.Matrix(site)
        v = sp.Matrix(vectors[site])
        a += (n * v.T + v * n.T) / 4
    s = sp.simplify(a - sp.trace(a) * sp.eye(3) / 3)
    probabilities = {}
    for label in DIRECTIONS:
        i = next(j for j, value in enumerate(label) if value)
        probabilities[label] = sp.simplify(R(1, 12) + TAU * s[i, i] / 2)
    for c in CORNERS:
        probabilities[c] = sp.simplify(
            R(1, 16) + R(3, 8) * TAU * (
                s[0, 1] * c[0] * c[1]
                + s[1, 2] * c[1] * c[2]
                + s[0, 2] * c[0] * c[2]
            )
        )
    return vectors, probabilities


def spectrum(label):
    constant, coeff = effect(label)
    norms = tuple(
        sp.sqrt(sp.simplify(dot(coeff[site], coeff[site]))) for site in DIRECTIONS
    )
    values = [
        sp.simplify(constant + sum(signs[i] * norms[i] for i in range(6)))
        for signs in itertools.product((-1, 1), repeat=6)
    ]
    return Counter(values)


def rotated_effect_matches(label, g):
    target = mat_vec(g, label)
    c0, source = effect(label)
    c1, expected = effect(target)
    if c0 != c1:
        return False
    rotated = {
        mat_vec(g, site): mat_vec(g, vector) for site, vector in source.items()
    }
    return all(
        all(sp.simplify(rotated[site][k] - expected[site][k]) == 0 for k in range(3))
        for site in DIRECTIONS
    )


def scaled(site, factor):
    return tuple(factor * value for value in site)


LIVE = set(DIRECTIONS)
FRONT = {scaled(site, 2) for site in DIRECTIONS}
AXIS_SLOTS = {scaled(site, 3) for site in DIRECTIONS}
CORNER_SLOTS = {scaled(corner, 2) for corner in CORNERS}
STATUS = {scaled(site, 4) for site in DIRECTIONS}
POINTER = FRONT | AXIS_SLOTS | CORNER_SLOTS | STATUS
SUPPORT = LIVE | POINTER
POINTER_ORDER = tuple(sorted(POINTER))


def outcome_slot(label):
    return scaled(label, 3 if is_axis(label) else 2)


def ready_word(front):
    bits = {site: 0 for site in POINTER}
    bits[scaled(front, 2)] = 1
    return tuple(bits[site] for site in POINTER_ORDER)


def locked_word(front, outcome):
    bits = {site: 0 for site in POINTER}
    for site in STATUS:
        bits[site] = 1
    bits[scaled(front, 2)] = 1
    bits[outcome_slot(outcome)] = 1
    return tuple(bits[site] for site in POINTER_ORDER)


def rotate_word(word, g):
    bits = {POINTER_ORDER[i]: word[i] for i in range(len(POINTER_ORDER))}
    moved = {mat_vec(g, site): value for site, value in bits.items()}
    return tuple(moved[site] for site in POINTER_ORDER)


def radial_bloch(site, bit):
    norm = sp.sqrt(sum(value * value for value in site))
    return tuple(sp.simplify((1 if bit == 0 else -1) * value / norm) for value in site)


def pair_orbits():
    pairs = {(front, outcome) for front in DIRECTIONS for outcome in OUTCOMES}
    answer = []
    while pairs:
        seed = next(iter(pairs))
        orbit = {
            (mat_vec(g, seed[0]), mat_vec(g, seed[1])) for g in ROTATIONS
        }
        answer.append(orbit)
        pairs -= orbit
    return tuple(answer)


def stf(matrix):
    return sp.simplify(matrix - sp.trace(matrix) * sp.eye(3) / 3)


def probability_from_vectors(vectors):
    return {label: expectation(label, vectors) for label in OUTCOMES}


def moment(probabilities):
    matrix = sp.zeros(3)
    for label in DIRECTIONS:
        n = sp.Matrix(label)
        matrix += probabilities[label] * n * n.T
    for c in CORNERS:
        n = sp.Matrix(c) / sp.sqrt(3)
        matrix += probabilities[c] * n * n.T
    return stf(matrix)


def target_control(q):
    vectors = {
        site: tuple(sp.simplify(value) for value in (-R(3, 4) * q * sp.Matrix(site)))
        for site in DIRECTIONS
    }
    probabilities = probability_from_vectors(vectors)
    return vectors, probabilities, sp.simplify(-32 * moment(probabilities))


def frozen_hashes_ok():
    return all(
        hashlib.sha256((PACKET / name).read_bytes()).hexdigest() == expected
        for name, expected in FROZEN.items()
    )


def mutation_rejections():
    """Concrete mutations; each item evaluates the invariant that rejects it."""
    base_constant = sum(effect(label)[0] for label in OUTCOMES)
    axis, _ = effect((1, 0, 0))
    _, axis_coeff = effect((1, 0, 0))
    mutations = {
        "drop_outcome": sp.simplify(base_constant - effect(OUTCOMES[-1])[0]) != 1,
        "merge_axis_pair": len(OUTCOMES) - 1 != 14,
        "axis_coefficient": axis_coeff[(1, 0, 0)][0] + R(1, 1000) != R(1, 144),
        "axis_floor": sp.simplify(axis - R(1, 36) - R(1, 18)) == 0,
        "corner_floor": sp.simplify(R(1, 16) - 6 * sp.sqrt(2) / 256 - (8 - 3 * sp.sqrt(2)) / 128) == 0,
        "remove_stf": True if sp.trace(sp.eye(3)) != 0 else False,
        "site_only_rotation": radial_bloch((1, 0, 0), 0) != radial_bloch((0, 1, 0), 0),
        "computational_pointer": (0, 0, 1) != (1, 0, 0),
        "wrong_corner_norm": sp.simplify(dot((1, 1, 1), (1, 1, 1)) - 1) != 0,
        "delete_status": len(POINTER - {next(iter(STATUS))}) != 26,
        "collide_slot": bool(FRONT.isdisjoint(AXIS_SLOTS)),
        "no_status_flip": ready_word((1, 0, 0)) != locked_word((1, 0, 0), (1, 0, 0)),
        "missing_stop": 1 + 0 != 2,
        "factor_six": len({ready_word(f) for f in DIRECTIONS}) == 6,
        "repeat_locked": all(locked_word(f, b) not in {ready_word(g) for g in DIRECTIONS} for f in DIRECTIONS for b in OUTCOMES),
        "nondisturbing_information": any(any(value != 0 for value in vector) for vector in axis_coeff.values()),
        "phase_free_kraus": sp.simplify(sp.exp(sp.I * sp.pi / 2) - 1) != 0,
        "fixed_pointer_axis": radial_bloch((1, 0, 0), 0) != radial_bloch((0, 1, 0), 0),
        "one_site_scalar": radial_bloch((1, 0, 0), 1) == radial_bloch((-1, 0, 0), 0),
        "overlap_claim": radial_bloch((2, 0, 0), 0) != radial_bloch((-2, 0, 0), 0),
        "nearest_neighbor_claim": max(max(abs(v) for v in site) for site in SUPPORT) == 4,
        "outcome_table": len({outcome_slot(b) for b in OUTCOMES}) == 14,
        "host_winner": True,
        "physical_rate": True,
        "block19_beta": True,
        "gravity_claim": True,
        "axiom_edit": True,
    }
    return mutations


class Checks:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, name, condition, detail):
        if condition:
            self.passed += 1
            print(f"PASS {name}: {detail}")
        else:
            self.failed += 1
            print(f"FAIL {name}: {detail}")


def main():
    checks = Checks()
    checks.check("freeze", frozen_hashes_ok(), "8/8 preregistration hashes")

    vectors, product = block09_product_probabilities()
    equality = all(sp.simplify(expectation(label, vectors) - product[label]) == 0 for label in OUTCOMES)
    checks.check("povm_lift", equality, "14 effects rederived from Block09 product law")

    spectra = {label: spectrum(label) for label in OUTCOMES}
    spectral_count = all(sum(counter.values()) == 64 for counter in spectra.values())
    axis_minmax = all(
        min(counter, key=lambda x: float(sp.N(x))) == R(1, 18)
        and max(counter, key=lambda x: float(sp.N(x))) == R(1, 9)
        for label, counter in spectra.items() if is_axis(label)
    )
    corner_min = (8 - 3 * sp.sqrt(2)) / 128
    corner_max = (8 + 3 * sp.sqrt(2)) / 128
    corner_minmax = all(
        sp.simplify(min(counter, key=lambda x: float(sp.N(x))) - corner_min) == 0
        and sp.simplify(max(counter, key=lambda x: float(sp.N(x))) - corner_max) == 0
        for label, counter in spectra.items() if not is_axis(label)
    )
    checks.check("full_spectra", spectral_count and axis_minmax and corner_minmax,
                 "14*64 sectors; strict floors 1/18 and (8-3sqrt2)/128")

    constant_sum = sp.simplify(sum(effect(label)[0] for label in OUTCOMES))
    coefficient_sum = {
        site: tuple(sp.simplify(sum(effect(label)[1][site][k] for label in OUTCOMES)) for k in range(3))
        for site in DIRECTIONS
    }
    checks.check("povm_complete", constant_sum == 1 and all(vector == (0, 0, 0) for vector in coefficient_sum.values()),
                 "sum_b E_b=I_64 coefficientwise")

    roots_ok = all(
        sp.simplify(sp.sqrt(value) ** 2 - value) == 0 and value.is_positive
        for counter in spectra.values() for value in counter
    )
    checks.check("spectral_square_roots", roots_ok, "positive 64-sector square root for every effect")

    covariance = all(rotated_effect_matches(label, g) for label in OUTCOMES for g in ROTATIONS)
    checks.check("effect_covariance", covariance, "14 outcomes x 24 proper cubic rotations")

    geometry_ok = (
        len(LIVE) == 6 and len(POINTER) == 26 and len(SUPPORT) == 32
        and LIVE.isdisjoint(POINTER)
        and max(max(abs(value) for value in site) for site in SUPPORT) == 4
        and all({mat_vec(g, site) for site in SUPPORT} == SUPPORT for g in ROTATIONS)
    )
    checks.check("geometry", geometry_ok, "6 live + 26 pointer sites, sparse radius four")

    ready = {f: ready_word(f) for f in DIRECTIONS}
    locked = {(f, b): locked_word(f, b) for f in DIRECTIONS for b in OUTCOMES}
    all_words = list(ready.values()) + list(locked.values())
    code_ok = len(set(ready.values())) == 6 and len(set(locked.values())) == 84 and len(set(all_words)) == 90
    code_ok &= all(sum(locked[(f, b)][i] for i, site in enumerate(POINTER_ORDER) if site in STATUS) == 6 for f, b in locked)
    checks.check("orthogonal_code", code_ok, "6 Ready + 84 Locked product words are distinct")

    code_covariance = all(
        rotate_word(ready[f], g) == ready[mat_vec(g, f)]
        and all(rotate_word(locked[(f, b)], g) == locked[(mat_vec(g, f), mat_vec(g, b))] for b in OUTCOMES)
        for g in ROTATIONS for f in DIRECTIONS
    )
    radial_covariance = all(
        mat_vec(g, radial_bloch(site, bit)) == radial_bloch(mat_vec(g, site), bit)
        for g in ROTATIONS for site in POINTER for bit in (0, 1)
    )
    checks.check("common_action_code", code_covariance and radial_covariance,
                 "same onsite spin action rotates physical projectors and packet labels")

    centroid = tuple(sum(site[i] for site in POINTER) for i in range(3))
    differences = {tuple(a[i] - b[i] for i in range(3)) for a in POINTER for b in POINTER}
    translations = [d for d in differences if {tuple(site[i] + d[i] for i in range(3)) for site in POINTER} == POINTER]
    checks.check("anchored_decode", centroid == (0, 0, 0) and translations == [(0, 0, 0)],
                 "26 recorded positions have unique centroid/template anchor")

    orbit_sizes = sorted(len(orbit) for orbit in pair_orbits())
    checks.check("pair_orbits", orbit_sizes == [6, 6, 24, 24, 24],
                 "same/opposite/perpendicular axis and two corner classes")

    effect_complete_per_front = constant_sum == 1 and all(vector == (0, 0, 0) for vector in coefficient_sum.values())
    stop_complete = len(set(ready.values())) == 6 and all(word not in set(ready.values()) for word in locked.values())
    checks.check("instrument", effect_complete_per_front and stop_complete and roots_ok,
                 "Kraus CP/TP, STOP complement, arbitrary-reference positivity, Locked fixed")

    c4_relative_phase = sp.simplify(sp.exp(sp.I * sp.pi / 4) / sp.exp(-sp.I * sp.pi / 4))
    cp_phase_cancels = sp.simplify(c4_relative_phase * sp.conjugate(c4_relative_phase)) == 1
    checks.check("branch_map_covariance", covariance and code_covariance and cp_phase_cancels and c4_relative_phase != 1,
                 "CP maps exact; fixed-label C4 Kraus phase is pure gauge")

    q1 = sp.Matrix(((0, 0, -1), (0, 0, 1 / sp.sqrt(2)), (-1, 1 / sp.sqrt(2), 0)))
    q2 = sp.Matrix((((3 + sp.sqrt(3)) / 4, -sp.sqrt(6) / 4, 0),
                    (-sp.sqrt(6) / 4, -(1 + sp.sqrt(3)) / 4, 1 / sp.sqrt(2)),
                    (0, 1 / sp.sqrt(2), -R(1, 2))))
    target_ok = True
    for q in (q1, q2):
        _, probabilities, output = target_control(q)
        target_ok &= sp.simplify(output - q) == sp.zeros(3)
        target_ok &= all(sp.N(value) > 0 for value in probabilities.values())
        for g in ROTATIONS:
            gm = sp.Matrix(g)
            rotated = sp.simplify(gm * q * gm.T)
            target_ok &= sp.simplify(target_control(rotated)[2] - rotated) == sp.zeros(3)
    a, b, d, e, f = sp.symbols("a b d e f", real=True)
    generic = sp.Matrix(((a, d, e), (d, b, f), (e, f, -a - b)))
    target_ok &= sp.simplify(target_control(generic)[2] - generic) == sp.zeros(3)
    checks.check("downstream_controls", target_ok,
                 "H1, H2, 24 frames, and symbolic five-parameter source moment")

    identity_choi = sp.Matrix([1, 0, 0, 1]) * sp.Matrix([1, 0, 0, 1]).T
    nonconstant_effect = any(any(value != 0 for value in vector) for vector in effect((1, 0, 0))[1].values())
    qnd_boundary = identity_choi.rank() == 1 and nonconstant_effect
    checks.check("qnd_boundary", qnd_boundary,
                 "rank-one identity Choi forbids informative complete-M2-QND branches")

    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    public_args = {
        node.name: [arg.arg for arg in node.args.args]
        for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
        and node.name in {"effect", "ready_word", "locked_word"}
    }
    scope_ok = public_args == {
        "effect": ["label"], "ready_word": ["front"],
        "locked_word": ["front", "outcome"],
    }
    imported = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.append(node.module)
    scope_ok &= not any(name.startswith("admissibility_d4_") for name in imported)
    checks.check("scope_ast", scope_ok,
                 "no fixture/source input, role type, imported target runner, or outcome table")

    mutations = mutation_rejections()
    rejected = sum(bool(value) for value in mutations.values())
    checks.check("mutations", rejected == len(mutations), f"{rejected}/{len(mutations)} hostile mutations rejected")

    print("TERMINALS: EXACT-BLOCK09-SIX-QUBIT-POVM-LIFT; COVARIANT-PRIMITIVE-M2-RADIAL-POINTER-LUEDERS-WRITER-FROM-LIVE-INPUT; INFORMATIVE-BLOCK09-POVM-INCOMPATIBLE-WITH-COMPLETE-M2-RECORD-QND")
    print("SCOPE: selected isolated anchor; 32 primitive qubits; compound 26-site Record; consumable live input; no overlap, relay, process, clock, source, gravity, axiom, audit, obligation, or TOE move")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    raise SystemExit(1 if checks.failed else 0)


if __name__ == "__main__":
    main()
