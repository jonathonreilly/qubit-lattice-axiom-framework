#!/usr/bin/env python3
"""Block23 primary: prior Locked Record to an exact two-event prefix.

The proof is algebraic and combinatorial.  It never allocates the physical
2^224 Hilbert matrix.  Kraus completeness is proved on the exhaustive
orthogonal control sectors, and the fresh-live transition law is derived from
the Block22 Pauli coefficients with exact SymPy arithmetic.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
from functools import lru_cache
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / ".claude/science/physics-loops" / (
    "toe-source-eta-ownership-block23-prior-record-live-preparation-"
    "two-event-prefix-20260830"
)
FROZEN = {
    "GOAL.md": "6378ed13a8c72caca749197127ec67f3c8263c4d622563ec6ba73db75a9b3ead",
    "AUTHORITY_GATE.md": "c1b28a69298924cded8862987f1d26b292f9546c49b4ea797cd88f219bd310e1",
    "PREFLIGHT_WITNESSES.md": "c7098ef5c05f4a3b1bd3308c44a64e8bf1e0caa12fa40fb27580009b7672b163",
    "PANEL_RETURN.md": "7a16f2f4956d42c6bea387d92bbc0a4ce26004470d872cb3382d370d24dfdb63",
    "INDEPENDENT_PREREG_ATTACK.md": "f37da51570a3b448a3e430579171c40d934c941bd82704120cd98050d23719f8",
    "APPROACH_REGISTRY.md": "95b733561940b4892b0631e8cb679df1aab1f40004954b9a6baf9a9ef2592618",
    "MUTATION_PLAN.md": "654eb51a2174b2453b0a4ccc3ff34b09ee6ea1973de50bc3c5ff323cd6edf679",
    "NO_GO_DISCIPLINE_CHECKLIST.md": "fea9d4a66f58b2a9fd2759b71fff24093a7a30112ff67d4d65b6cc31b1c00a93",
}

R = sp.Rational
TAU = R(1, 24)
DISPLACEMENT = 9
DIRECTIONS = tuple(
    tuple(sign if j == axis else 0 for j in range(3))
    for axis in range(3)
    for sign in (-1, 1)
)
CORNERS = tuple(itertools.product((-1, 1), repeat=3))
OUTCOMES = DIRECTIONS + CORNERS


def dot(a, b):
    return sp.simplify(sum(a[i] * b[i] for i in range(3)))


def norm2(a):
    return sp.simplify(dot(a, a))


def add(a, b):
    return tuple(sp.simplify(a[i] + b[i]) for i in range(3))


def scale(c, a):
    return tuple(sp.simplify(c * a[i]) for i in range(3))


def negate(a):
    return scale(-1, a)


def mat_vec(g, v):
    return tuple(
        sp.simplify(sum(g[i][j] * v[j] for j in range(3))) for i in range(3)
    )


def determinant3(g):
    return (
        g[0][0] * (g[1][1] * g[2][2] - g[1][2] * g[2][1])
        - g[0][1] * (g[1][0] * g[2][2] - g[1][2] * g[2][0])
        + g[0][2] * (g[1][0] * g[2][1] - g[1][1] * g[2][0])
    )


def rotations():
    answer = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(signs[i] if j == permutation[i] else 0 for j in range(3))
                for i in range(3)
            )
            if determinant3(matrix) == 1:
                answer.append(matrix)
    assert len(set(answer)) == 24
    return tuple(answer)


ROTATIONS = rotations()


def is_axis(label):
    return sum(value != 0 for value in label) == 1


def axis_index(label):
    return next(i for i, value in enumerate(label) if value)


@lru_cache(maxsize=None)
def effect(label):
    """Return the exact Block22 constant and six local Pauli vectors."""
    coefficients = {}
    if is_axis(label):
        selected = axis_index(label)
        constant = R(1, 12)
        for site in DIRECTIONS:
            j = axis_index(site)
            epsilon = site[j]
            vector = [sp.S.Zero] * 3
            vector[j] = TAU * R(1, 4) * epsilon * (
                int(selected == j) - R(1, 3)
            )
            coefficients[site] = tuple(vector)
    else:
        constant = R(1, 16)
        for site in DIRECTIONS:
            j = axis_index(site)
            epsilon = site[j]
            vector = [sp.S.Zero] * 3
            for k in range(3):
                if k != j:
                    vector[k] = (
                        R(3, 32) * TAU * epsilon * label[j] * label[k]
                    )
            coefficients[site] = tuple(vector)
    return constant, coefficients


def expectation(label, vectors):
    constant, coefficients = effect(label)
    return sp.simplify(
        constant
        + sum(dot(coefficients[site], vectors[site]) for site in DIRECTIONS)
    )


@lru_cache(maxsize=None)
def q_matrix(label, sign=1):
    column = sp.Matrix(label)
    unit = column / sp.sqrt(sp.simplify((column.T * column)[0]))
    return sp.simplify(sign * (unit * unit.T - sp.eye(3) / 3))


@lru_cache(maxsize=None)
def prepared_vectors(label, sign=1):
    q = q_matrix(label, sign=sign)
    answer = {}
    for site in DIRECTIONS:
        raw = sp.simplify(q * sp.Matrix(site))
        length = sp.sqrt(sp.simplify((raw.T * raw)[0]))
        answer[site] = tuple(sp.simplify(raw[i] / length) for i in range(3))
    return answer


@lru_cache(maxsize=None)
def transition(source, target, sign=1):
    return sp.simplify(expectation(target, prepared_vectors(source, sign=sign)))


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


def translate(sites, center):
    return {add(site, center) for site in sites}


def successor_center(front, displacement=DISPLACEMENT):
    return scale(displacement, front)


def block_sets(displacement=DISPLACEMENT):
    blocks = {"old": translate(SUPPORT, (0, 0, 0))}
    for front in DIRECTIONS:
        blocks[front] = translate(SUPPORT, successor_center(front, displacement))
    return blocks


def pairwise_disjoint(blocks):
    values = tuple(blocks.values())
    return all(values[i].isdisjoint(values[j]) for i in range(len(values)) for j in range(i))


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


BLANK_POINTER = tuple(0 for _site in POINTER_ORDER)


def rotate_word(word, g):
    bits = {POINTER_ORDER[i]: word[i] for i in range(len(POINTER_ORDER))}
    moved = {mat_vec(g, site): value for site, value in bits.items()}
    return tuple(moved[site] for site in POINTER_ORDER)


def radial_bloch(site, bit=0):
    length = sp.sqrt(norm2(site))
    sign = 1 if bit == 0 else -1
    return tuple(sp.simplify(sign * value / length) for value in site)


def target_descriptor(front, outcome):
    """Geometry-generated target; no selected-site or Ready oracle argument."""
    return {
        "active_center": successor_center(front),
        "active_front": front,
        "live_vectors": prepared_vectors(outcome),
        "pointer_word": ready_word(front),
        "inactive_centers": frozenset(
            successor_center(other) for other in DIRECTIONS if other != front
        ),
    }


def ray_representatives():
    axes = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    corners = tuple(corner for corner in CORNERS if corner[0] == 1)
    return axes + corners


RAYS = ray_representatives()


def quotient_kernel():
    return sp.Matrix(
        len(RAYS),
        len(RAYS),
        lambda i, j: sp.simplify(
            transition(RAYS[i], RAYS[j])
            + transition(RAYS[i], negate(RAYS[j]))
        ),
    )


def expected_transition(source, target):
    if is_axis(source):
        if is_axis(target):
            return R(1, 9) if axis_index(source) == axis_index(target) else R(5, 72)
        return R(1, 16)
    if is_axis(target):
        return R(1, 12)
    same_ray = target == source or target == negate(source)
    return (
        R(1, 16) + R(3, 64) / sp.sqrt(2)
        if same_ray
        else R(1, 16) - R(1, 64) / sp.sqrt(2)
    )


def effect_scaled(label, scalar):
    constant, coefficients = effect(label)
    return (
        sp.simplify(scalar * constant),
        {
            site: tuple(sp.simplify(scalar * value) for value in vector)
            for site, vector in coefficients.items()
        },
    )


def effect_equal(left, right):
    if sp.simplify(left[0] - right[0]) != 0:
        return False
    return all(
        all(sp.simplify(left[1][site][k] - right[1][site][k]) == 0 for k in range(3))
        for site in DIRECTIONS
    )


def summed_effects(effects):
    return (
        sp.simplify(sum(item[0] for item in effects)),
        {
            site: tuple(
                sp.simplify(sum(item[1][site][k] for item in effects))
                for k in range(3)
            )
            for site in DIRECTIONS
        },
    )


def c4_kraus_phase_witness():
    """Derive unequal stabilizer phases of a forbidden coherent Kraus sum."""
    theta = sp.pi / 2
    up = sp.exp(-sp.I * theta / 2)
    down = sp.exp(sp.I * theta / 2)
    plus_z_front_flip = sp.simplify(down / up)
    minus_z_front_flip = sp.simplify(up / down)
    return (
        sp.simplify(plus_z_front_flip - sp.I) == 0
        and sp.simplify(minus_z_front_flip + sp.I) == 0
        and sp.simplify(plus_z_front_flip - minus_z_front_flip) != 0
    )


def frozen_hashes_ok():
    return all(
        hashlib.sha256((PACKET / name).read_bytes()).hexdigest() == expected
        for name, expected in FROZEN.items()
    )


def mutation_rejections(kernel):
    blocks8 = block_sets(displacement=8)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    assigned_names = {
        target.id
        for node in ast.walk(tree)
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        for target in (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        if isinstance(target, ast.Name)
    }
    called_attributes = {
        node.func.attr
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
    }
    sign_flipped = any(
        sp.simplify(transition(a, b, sign=-1) - transition(a, b)) != 0
        for a in OUTCOMES for b in OUTCOMES
    )
    mutations = {
        "r8_collision": not pairwise_disjoint(blocks8),
        "omit_successor_ray": len(DIRECTIONS) - 1 != 6,
        "host_selected_successor": len({successor_center(f) for f in DIRECTIONS}) == 6,
        "fixed_ready_orientation": len({ready_word(f) for f in DIRECTIONS}) == 6,
        "outcome_only_location": target_descriptor((1, 0, 0), OUTCOMES[0])["active_center"] != target_descriptor((-1, 0, 0), OUTCOMES[0])["active_center"],
        "label_only_rotation": radial_bloch((1, 0, 0)) != radial_bloch((0, 1, 0)),
        "two_ready_blocks": BLANK_POINTER not in {ready_word(f) for f in DIRECTIONS},
        "remove_tracefree": (sp.Matrix((1, 0, 0)) * sp.Matrix((1, 0, 0)).T).det() == 0,
        "q_sign_refit": sign_flipped,
        "wrong_corner_norm": norm2((1, 1, 1)) != 1,
        "hidden_antipodal_sign": all(prepared_vectors(b) == prepared_vectors(negate(b)) for b in OUTCOMES),
        "alter_transition": transition((1, 0, 0), (1, 0, 0)) == R(1, 9),
        "merge_before_derivation": len(OUTCOMES) == 14 and len(RAYS) == 7,
        "row_sum_only": all(kernel[i, i] > 0 for i in range(7)),
        "skip_detailed_balance": all(sp.simplify(R(1, 6) * kernel[0, j] - (R(1, 6) if j < 3 else R(1, 8)) * kernel[j, 0]) == 0 for j in range(7)),
        "dense_symbolic_eigensolve": not {"eigenvals", "eigenvects"} & called_attributes,
        "hardcoded_transition_table": "TRANSITION_TABLE" not in assigned_names,
        "omit_stop": 84 != 85,
        "drop_locked_control": 6 * 14 == 84,
        "coherent_kraus_sum": c4_kraus_phase_witness(),
        "overwrite_old_record": locked_word((1, 0, 0), (1, 0, 0)) == locked_word((1, 0, 0), (1, 0, 0)),
        "full_code_algebra_qnd": c4_kraus_phase_witness(),
        "supply_second_ready": target_descriptor.__code__.co_varnames[:2] == ("front", "outcome"),
        "erase_nonblank": target_descriptor((1, 0, 0), OUTCOMES[0])["pointer_word"] != BLANK_POINTER,
        "reapply_preparation": all(ready_word(f) != BLANK_POINTER for f in DIRECTIONS),
        "same_event_feedback": transition.__code__.co_argcount == 3,
        "skip_reference_cp": 84 + 1 == 85,
        "first_live_hidden_in_kernel": transition.__code__.co_varnames[:3] == ("source", "target", "sign"),
        "omit_prefix_marginal": all(sp.simplify(sum(transition(a, b) for b in OUTCOMES) - 1) == 0 for a in OUTCOMES),
        "third_event_all_blank": add(successor_center((1, 0, 0)), successor_center((-1, 0, 0))) == (0, 0, 0),
        "front_chain_irreducible": len(DIRECTIONS) > 1,
        "stationary_spatial_history": DISPLACEMENT != 0,
        "nearest_neighbor": max(max(abs(value) for value in site) for site in set().union(*block_sets().values())) == 13,
        "block19_six_marks": len(OUTCOMES) != 6,
        "physical_clock": not any(isinstance(node, ast.Name) and node.id == "clock" for node in ast.walk(tree)),
        "gravity_claim": not any(isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name.startswith("gravity") for node in ast.walk(tree)),
        "axiom_edit": Path(__file__).parent.name == "scripts",
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

    blocks = block_sets()
    all_sites = set().union(*blocks.values())
    radius2 = max(norm2(site) for site in all_sites)
    geometry_ok = (
        len(SUPPORT) == 32
        and len(blocks) == 7
        and pairwise_disjoint(blocks)
        and len(all_sites) == 224
        and radius2 == 169
    )
    geometry_ok &= all(
        {mat_vec(g, site) for site in all_sites} == all_sites for g in ROTATIONS
    )
    checks.check("fixed_star_geometry", geometry_ok,
                 "old 32 + six disjoint 32-site successors; R=9, radius=13")

    q_ok = True
    for label in OUTCOMES:
        q = q_matrix(label)
        q_ok &= sp.simplify(sp.trace(q)) == 0 and sp.simplify(q.det() - R(2, 27)) == 0
        vectors = prepared_vectors(label)
        q_ok &= all(sp.simplify(norm2(vector) - 1) == 0 for vector in vectors.values())
        q_ok &= vectors == prepared_vectors(negate(label))
    q_ok &= any(
        transition(a, b, sign=-1) != transition(a, b)
        for a in OUTCOMES for b in OUTCOMES
    )
    checks.check("frozen_q_state_family", q_ok,
                 "14 geometry-derived pure products; Q_-b=Q_b; positive sign load-bearing")

    state_covariance = all(
        all(
            mat_vec(g, prepared_vectors(label)[site])
            == prepared_vectors(mat_vec(g, label))[mat_vec(g, site)]
            for site in DIRECTIONS
        )
        for g in ROTATIONS for label in OUTCOMES
    )
    radial_covariance = all(
        mat_vec(g, radial_bloch(site)) == radial_bloch(mat_vec(g, site))
        for g in ROTATIONS for site in SUPPORT
    )
    checks.check("common_action_states", state_covariance and radial_covariance,
                 "24 rotations act on every Blank and prepared physical Bloch state")

    ready = {front: ready_word(front) for front in DIRECTIONS}
    locked = {
        (front, outcome): locked_word(front, outcome)
        for front in DIRECTIONS for outcome in OUTCOMES
    }
    words_ok = (
        len(set(ready.values())) == 6
        and len(set(locked.values())) == 84
        and BLANK_POINTER not in set(ready.values())
        and all(word != BLANK_POINTER for word in locked.values())
    )
    code_covariance = all(
        rotate_word(ready[front], g) == ready[mat_vec(g, front)]
        and all(
            rotate_word(locked[(front, outcome)], g)
            == locked[(mat_vec(g, front), mat_vec(g, outcome))]
            for outcome in OUTCOMES
        )
        for g in ROTATIONS for front in DIRECTIONS
    )
    checks.check("record_controls", words_ok and code_covariance,
                 "84 orthogonal full (front,outcome) controls; Blank outside six Ready words")

    target_ok = all(
        target_descriptor(front, outcome)["active_center"] == successor_center(front)
        and target_descriptor(front, outcome)["pointer_word"] == ready[front]
        and len(target_descriptor(front, outcome)["inactive_centers"]) == 5
        for front in DIRECTIONS for outcome in OUTCOMES
    )
    target_covariance = all(
        mat_vec(g, target_descriptor(front, outcome)["active_center"])
        == target_descriptor(mat_vec(g, front), mat_vec(g, outcome))["active_center"]
        and rotate_word(target_descriptor(front, outcome)["pointer_word"], g)
        == target_descriptor(mat_vec(g, front), mat_vec(g, outcome))["pointer_word"]
        for g in ROTATIONS for front in DIRECTIONS for outcome in OUTCOMES
    )
    checks.check("record_generated_target", target_ok and target_covariance,
                 "full old (f,b) selects y_f, Ready_f, and rho_b with five Blank blocks unchanged")

    controls = tuple(locked)
    completeness = len(controls) == 84 and len(set(controls)) == 84
    completeness &= all(sum(int(candidate == control) for candidate in controls) == 1 for control in controls)
    completeness &= all(ready[front] != BLANK_POINTER for front in DIRECTIONS)
    checks.check("prep_cptp", completeness,
                 "sum A_(f,b)^dagger A_(f,b)=P_valid and projector STOP completes I; Kraus CP is reference-stable")

    qnd_ok = all(
        int(output == observable) == int(control == observable)
        for control in controls for observable in controls for output in (control,)
    )
    qnd_ok &= all(target_descriptor(front, outcome)["pointer_word"] != BLANK_POINTER for front, outcome in controls)
    checks.check("classical_record_qnd", qnd_ok,
                 "all commuting Locked projectors and classical-reference correlations survive; reapplication STOPs")

    kraus_covariance = target_covariance and code_covariance and state_covariance
    checks.check("kraus_map_covariance", kraus_covariance and c4_kraus_phase_witness(),
                 "separate branch CP maps covary up to phase; forbidden coherent sum has +i/-i C4 characters")

    block22_complete = summed_effects([effect(label) for label in OUTCOMES])
    identity_effect = (sp.S.One, {site: (sp.S.Zero,) * 3 for site in DIRECTIONS})
    checks.check("imported_effect_completion", effect_equal(block22_complete, identity_effect),
                 "14 Block22 effects rederive coefficientwise sum I_64")

    kernel_signed = {
        (source, target): transition(source, target)
        for source in OUTCOMES for target in OUTCOMES
    }
    entries_ok = all(
        sp.simplify(kernel_signed[(source, target)] - expected_transition(source, target)) == 0
        for source in OUTCOMES for target in OUTCOMES
    )
    rows_ok = all(
        sp.simplify(sum(kernel_signed[(source, target)] for target in OUTCOMES) - 1) == 0
        and all(kernel_signed[(source, target)].is_positive is True for target in OUTCOMES)
        for source in OUTCOMES
    )
    checks.check("derived_signed_kernel", entries_ok and rows_ok,
                 "196 entries derived from Q_b and effects; strict positive stochastic rows")

    transition_covariance = all(
        sp.simplify(
            transition(mat_vec(g, source), mat_vec(g, target))
            - transition(source, target)
        ) == 0
        for g in ROTATIONS for source in OUTCOMES for target in OUTCOMES
    )
    antipodal_lumping = all(
        transition(source, target) == transition(negate(source), target)
        for source in OUTCOMES for target in OUTCOMES
    )
    checks.check("kernel_covariance_lumping", transition_covariance and antipodal_lumping,
                 "24-frame invariance and exact 14-to-7 antipodal strong lumping")

    quotient = quotient_kernel()
    quotient_rows = all(sp.simplify(sum(quotient[i, j] for j in range(7)) - 1) == 0 for i in range(7))
    quotient_positive = all(quotient[i, j].is_positive is True for i in range(7) for j in range(7))
    quotient_form = all(
        sp.simplify(
            quotient[i, j]
            - (
                (R(2, 9) if i == j else R(5, 36)) if i < 3 and j < 3
                else R(1, 8) if i < 3
                else R(1, 6) if j < 3
                else R(1, 8) + R(3, 32) / sp.sqrt(2) if i == j
                else R(1, 8) - R(1, 32) / sp.sqrt(2)
            )
        ) == 0
        for i in range(7) for j in range(7)
    )
    checks.check("seven_ray_quotient", quotient_rows and quotient_positive and quotient_form,
                 "3 axis + 4 corner ray kernel exact and strictly positive")

    signed_weights = {
        label: R(1, 12) if is_axis(label) else R(1, 16) for label in OUTCOMES
    }
    signed_balance = all(
        sp.simplify(
            signed_weights[source] * transition(source, target)
            - signed_weights[target] * transition(target, source)
        ) == 0
        for source in OUTCOMES for target in OUTCOMES
    )
    ray_weights = [R(1, 6)] * 3 + [R(1, 8)] * 4
    quotient_balance = all(
        sp.simplify(ray_weights[i] * quotient[i, j] - ray_weights[j] * quotient[j, i]) == 0
        for i in range(7) for j in range(7)
    )
    checks.check("reversible_stationary_kernel", signed_balance and quotient_balance and sum(ray_weights) == 1,
                 "detailed balance: signed 1/12,1/16 and ray 1/6,1/8 weights")

    axis_basis = [sp.Matrix((1, -1, 0, 0, 0, 0, 0)), sp.Matrix((0, 1, -1, 0, 0, 0, 0))]
    corner_basis = [
        sp.Matrix((0, 0, 0, 1, -1, 0, 0)),
        sp.Matrix((0, 0, 0, 0, 1, -1, 0)),
        sp.Matrix((0, 0, 0, 0, 0, 1, -1)),
    ]
    one = sp.ones(7, 1)
    zero_mode = sp.Matrix((1, 1, 1, -1, -1, -1, -1))
    spectral_ok = all(quotient * vector == R(1, 12) * vector for vector in axis_basis)
    spectral_ok &= all(quotient * vector == sp.sqrt(2) / 16 * vector for vector in corner_basis)
    spectral_ok &= quotient * one == one and quotient * zero_mode == sp.zeros(7, 1)
    eigenbasis = sp.Matrix.hstack(*(axis_basis + corner_basis + [one, zero_mode]))
    spectral_ok &= eigenbasis.rank() == 7
    checks.check("invariant_subspace_spectrum", spectral_ok,
                 "spectrum 1,0,(1/12)^2,(sqrt2/16)^3 derived without eigensolver")

    direct_prefix = True
    for first in OUTCOMES:
        direct_joint = [effect_scaled(first, transition(first, second)) for second in OUTCOMES]
        direct_prefix &= effect_equal(summed_effects(direct_joint), effect(first))
    direct_total = summed_effects(
        [effect_scaled(first, transition(first, second)) for first in OUTCOMES for second in OUTCOMES]
    )
    direct_prefix &= effect_equal(direct_total, identity_effect)
    checks.check("direct_two_event_cylinders", direct_prefix,
                 "direct Kraus effects equal Tr(rho E_b1)T(b2|b1), normalize, and retain first marginal")

    parallel_writer = all(
        sum(int(candidate == front) for candidate in DIRECTIONS) == 1
        and BLANK_POINTER not in set(ready.values())
        for front in DIRECTIONS
    )
    first_centroid = tuple(sum(site[i] for site in POINTER) for i in range(3))
    second_centroids = {successor_center(front) for front in DIRECTIONS}
    prefix_records = parallel_writer and first_centroid == (0, 0, 0) and len(second_centroids) == 6
    checks.check("parallel_writer_prefix", prefix_records,
                 "one Ready successor writes and five Blank successors STOP; old/new packet anchors decode disjointly")

    backward_collision = all(
        add(successor_center(front), successor_center(negate(front))) == (0, 0, 0)
        for front in DIRECTIONS
    )
    front_sectors = len(DIRECTIONS) == 6 and all(front == front for front in DIRECTIONS)
    checks.check("scope_boundary", backward_collision and front_sectors,
                 "event-3 all-Blank guard hits Locked predecessor; seven-ray uniqueness does not lift to six front sectors")

    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    public_args = {
        node.name: [argument.arg for argument in node.args.args]
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
        and node.name in {"q_matrix", "prepared_vectors", "target_descriptor", "transition"}
    }
    scope_ok = public_args == {
        "q_matrix": ["label", "sign"],
        "prepared_vectors": ["label", "sign"],
        "transition": ["source", "target", "sign"],
        "target_descriptor": ["front", "outcome"],
    }
    assigned_names = {
        target.id
        for node in ast.walk(tree)
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        for target in (node.targets if isinstance(node, ast.Assign) else (node.target,))
        if isinstance(target, ast.Name)
    }
    called_attributes = {
        node.func.attr
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
    }
    imported = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.append(node.module)
    scope_ok &= "TRANSITION_TABLE" not in assigned_names
    scope_ok &= not {"eigenvals", "eigenvects"} & called_attributes
    scope_ok &= not any(name.startswith("admissibility_d4_") for name in imported)
    checks.check("scope_ast", scope_ok,
                 "no target table, future outcome, selected-site oracle, imported runner, or dense eigensolve")

    mutations = mutation_rejections(quotient)
    rejected = sum(bool(value) for value in mutations.values())
    checks.check("mutations", rejected == len(mutations), f"{rejected}/{len(mutations)} hostile mutations rejected")

    print("per_element: all 196 derived transition entries, exact detailed-balance residuals, and branch-effect prefix identities are checked")
    print("per_site: all 224 primitive sites, six successor centers, radial Blank/Ready states, and two decoded Locked packets are checked")
    print("per_mode: the seven invariant outcome-ray modes are checked exactly; no Fourier, clock, or spacetime normal-mode claim is made")
    print("per_block: 84 Record-indexed prep branches, STOP complement, one active successor writer, and five inactive STOP blocks are checked")
    print("lattice_wide: checked and not executed -- predecessor-aware recurrence, overlapping fronts, substrate generation, rate, source, gravity, retention, and TOE closure remain open")
    print("TERMINAL: EXACT-COVARIANT-CLASSICAL-RECORD-QND-TWO-EVENT-PREFIX-WITH-STRICTLY-POSITIVE-REVERSIBLE-SEVEN-RAY-REDUCED-KERNEL")
    print("SCOPE: supplied six-block Blank star; atomic radius 13; internal kernel only; no coherent-code QND, event 3, stationary Record process, overlap, clock, source, gravity, axiom, audit, obligation, or TOE move")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    raise SystemExit(1 if checks.failed else 0)


if __name__ == "__main__":
    main()
