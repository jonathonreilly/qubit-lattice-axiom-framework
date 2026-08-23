#!/usr/bin/env python3
"""Exact joint-sector attack on the pincer marginal/conditional split.

For each hard-pin alternative a, the runner combines the Block 41 W9
precision K_W(a) with the positive Hermitian action S(a).  Their determinant
factors cancel, so the disjoint-sector partition has the parent
|det q(a)|^-2 formation weights while a normalized source in the K_W sector
has the pinned W9 trace response.  The runner also measures the exact prices:
the true outcome marginal is not the fixed-default density, counting
measure is not invariant under a duplicate-label refinement, the positive
spectator is not determinant-unique, and the K_W temporal range grows with
the cover even though q, S, and q^dagger q remain bounded-range.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_schur_record_response_bridge_2026_08_23 as b41


b175 = b41.b175
b174 = b41.b174
R = sp.Rational
ZERO = sp.Integer(0)
ONE = sp.Integer(1)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_PIN_FAITHFUL_JOINT_SECTOR_ACTION_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md"
)

AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_PIN_FAITHFUL_JOINT_SECTOR_ACTION_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SCHUR_RECORD_RESPONSE_BRIDGE_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_dirac_kahler_schur_record_response_bridge_"
    "2026_08_23.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_PINCER_IDENTITY_CROSS_LANE_"
    "BOUNDED_THEOREM_NOTE_2026-08-22.md",
    "scripts/admissibility_dirac_kahler_pincer_identity_cross_lane_"
    "2026_08_22.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_CONDITIONAL_LAW_FAMILY_"
    "BOUNDED_THEOREM_NOTE_2026-08-22.md",
    "scripts/admissibility_dirac_kahler_site_conditional_law_family_"
    "2026_08_22.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(values: tuple) -> tuple:
    total = sp.cancel(sum(values, ZERO))
    return tuple(sp.cancel(value / total) for value in values)


def matrix_zero(value: sp.Matrix) -> bool:
    return all(sp.expand(entry) == 0 for entry in value)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and matrix_zero(sp.expand(left - right))


def arm_data(fixture: object, value, rows: tuple[int, ...]) -> dict:
    q = fixture.q({b175.RECORD_CELL: value})
    w = b41.positive_completion(q)
    modulus = b41.modulus_completion(q, w["q_inv"])
    det_q = b174.dm_det(q)
    det_s = b174.dm_det(w["symmetric"])
    det_kw = b174.dm_det(w["precision"])
    w_block = w["covariance"].extract(rows, rows)
    m_block = modulus["covariance"].extract(rows, rows)
    trace_w = sp.cancel(sp.trace(w_block))
    trace_m = sp.cancel(sp.trace(m_block))
    return {
        "value": value,
        "q": q,
        "S": w["symmetric"],
        "KW": w["precision"],
        "W": w["covariance"],
        "KM": modulus["precision"],
        "V": modulus["covariance"],
        "det_q": det_q,
        "det_s": det_s,
        "det_kw": det_kw,
        "z_joint": sp.cancel(ONE / (det_kw * det_s)),
        "z_mod": sp.cancel(ONE / b174.norm2(det_q)),
        "z_w": sp.cancel(det_s / b174.norm2(det_q)),
        "block_w": w_block,
        "block_m": m_block,
        "trace_w": trace_w,
        "trace_m": trace_m,
        "rho_w": sp.expand(w_block / trace_w),
        "rho_m": sp.expand(m_block / trace_m),
    }


def temporal_range(matrix: sp.Matrix, fixture: object) -> int:
    distances = []
    for row in range(matrix.rows):
        t_row = row // fixture.lx
        for column in range(matrix.cols):
            if matrix[row, column] == 0:
                continue
            t_column = column // fixture.lx
            distances.append(
                min(
                    (t_row - t_column) % fixture.T,
                    (t_column - t_row) % fixture.T,
                )
            )
    return max(distances)


def source_derivative(block: sp.Matrix, effect: sp.Matrix):
    """Derivative of the normalized determinant-lemma source ratio."""
    source = sp.symbols("source", real=True)
    scale = sp.cancel(ONE / sp.trace(block))
    ratio = sp.cancel(
        ONE / (sp.eye(block.rows) - source * scale * block * effect).det()
    )
    return sp.cancel(sp.diff(ratio, source).subs(source, ZERO))


def main() -> int:
    passed = 0
    failed = 0

    def check(name: str, condition: bool, detail: str) -> None:
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"PASS {name}: {detail}")
        else:
            failed += 1
            print(f"FAIL {name}: {detail}")

    fixture = b174.Fixture(b175.LX, tag="b177-joint")
    rows = b41.slice_rows(fixture, fixture.tstar)
    arms = tuple(arm_data(fixture, value, rows) for value in b175.MENU)

    check(
        "positive-joint-sector-completion",
        all(
            b174.ldl_certificate(arm["S"])["pd"]
            and b174.ldl_certificate(arm["KW"])["pd"]
            for arm in arms
        ),
        "every K_W(a) direct-summed with S(a) is an exact positive two-field Gaussian sector",
    )

    check(
        "determinant-compensation-identity",
        all(
            sp.cancel(
                arm["det_kw"] * arm["det_s"]
                - b174.norm2(arm["det_q"])
            )
            == 0
            and sp.cancel(arm["z_joint"] - arm["z_mod"]) == 0
            for arm in arms
        ),
        "det(K_W(a)) det(S(a))=|det q(a)|^2, so the positive product sector has the determinant formation weight",
    )

    p_joint = normalize(tuple(arm["z_joint"] for arm in arms))
    p_det = normalize(tuple(arm["z_mod"] for arm in arms))
    p_w = normalize(tuple(arm["z_w"] for arm in arms))
    check(
        "formation-law-from-one-positive-partition",
        p_joint == p_det
        and all(value > 0 for value in p_joint)
        and p_joint != p_w,
        "the four alternative-sector masses reproduce the parent |det q_a|^-2 law without fitted pin weights",
    )

    all_level_source_ok = True
    for level in fixture.free_levels:
        level_rows = b41.slice_rows(fixture, level)
        level_arms = tuple(
            arm_data(fixture, value, level_rows) for value in b175.MENU
        )
        for arm in level_arms:
            for slot in range(fixture.lx):
                effect = b41.basis_projector(slot, fixture.lx)
                derivative = source_derivative(arm["block_w"], effect)
                all_level_source_ok = all_level_source_ok and (
                    derivative == arm["rho_w"][slot, slot]
                )
    check(
        "normalized-source-conditionals",
        all_level_source_ok,
        "the imposed per-arm identity calibration 1/Tr(W_RR), computed from the action, makes each sector source derivative equal its W9 trace conditional at all four free levels",
    )

    event = sp.Matrix(
        [
            [p_joint[a] * arms[a]["rho_w"][slot, slot] for slot in range(4)]
            for a in range(4)
        ]
    )
    marginal = sp.diag(*(sum(event[a, slot] for a in range(4)) for slot in range(4)))
    expected_marginal = sp.expand(
        sum(
            (p_joint[a] * arms[a]["rho_w"] for a in range(4)),
            sp.zeros(4),
        )
    )
    check(
        "joint-normalization-and-total-probability",
        all(event[a, slot] > 0 for a in range(4) for slot in range(4))
        and sp.cancel(sum(event, ZERO)) == ONE
        and all(
            sp.cancel(sum(event[a, slot] for slot in range(4)) - p_joint[a])
            == 0
            for a in range(4)
        )
        and matrix_equal(marginal, expected_marginal),
        "P(a,j)=p_det(a) Tr(C_a E_j) is positive, normalized, and obeys ordinary marginalization exactly",
    )

    alternative_parts = ((0, 1), (2, 3))
    effect_parts = ((0, 2), (1, 3))
    refinement_ok = True
    for a_part in alternative_parts:
        for e_part in effect_parts:
            direct = sum(event[a, j] for a in a_part for j in e_part)
            separate = sum(
                p_joint[a]
                * sp.trace(
                    arms[a]["rho_w"]
                    * sum(
                        (b41.basis_projector(j, 4) for j in e_part),
                        sp.zeros(4),
                    )
                )
                for a in a_part
            )
            refinement_ok = refinement_ok and sp.cancel(direct - separate) == 0
    check(
        "coarse-event-refinement-additivity",
        refinement_ok,
        "coarse alternative cells and union effects inherit their joint probabilities by exact finite addition",
    )

    traces = tuple(arm["trace_w"] for arm in arms)
    source_weights = normalize(
        tuple(p_joint[a] * traces[a] for a in range(4))
    )
    identity_source_density = sp.expand(
        sum(
            (source_weights[a] * arms[a]["rho_w"] for a in range(4)),
            sp.zeros(4),
        )
    )
    check(
        "branch-source-normalization-is-load-bearing",
        len(set(traces)) == 4
        and source_weights != p_joint
        and not matrix_equal(identity_source_density, expected_marginal)
        and all(sp.cancel((ONE / traces[a]) * traces[a] - ONE) == 0 for a in range(4)),
        "without the per-arm 1/Tr(W_RR) scale an outcome-blind source reweights the formation law, while identity certainty fixes that scalar uniquely",
    )

    z_values = tuple(arm["z_joint"] for arm in arms)
    duplicated = normalize((z_values[0], z_values[0], *z_values[1:]))
    split = R(2, 5)
    refined = normalize(
        (split * z_values[0], (ONE - split) * z_values[0], *z_values[1:])
    )
    check(
        "alternative-base-measure-refinement-price",
        sp.cancel(duplicated[0] + duplicated[1] - p_joint[0]) != 0
        and sp.cancel(refined[0] + refined[1] - p_joint[0]) == 0
        and tuple(refined[index + 1] for index in range(1, 4)) == p_joint[1:],
        "uniform duplicate-label counting changes the law; representation-preserving refinement needs additive base-measure shares",
    )

    q_unpinned = fixture.q({})
    default_completion = b41.positive_completion(q_unpinned)
    default_density = b41.normalized_block(default_completion["covariance"], rows)
    fixed_residual = sp.expand(default_density - expected_marginal)
    check(
        "true-joint-marginal-retypes-fixed-default",
        matrix_equal(default_density, arms[-1]["rho_w"])
        and not matrix_zero(fixed_residual)
        and tuple(sp.sign(fixed_residual[j, j]) for j in range(4))
        == (1, -1, -1, 1),
        "the pin-faithful joint marginal is new and differs exactly from the fixed sigma=3/5 W9 density",
    )

    exposing_effect = sp.diag(ZERO, R(4, 7), R(3, 7), ZERO)
    w_exposure = tuple(
        sp.sign(sp.factor(sp.trace((arm["rho_w"] - default_density) * exposing_effect)))
        for arm in arms
    )
    m_exposure = tuple(
        sp.sign(sp.factor(sp.trace((arm["rho_m"] - default_density) * exposing_effect)))
        for arm in arms
    )
    check(
        "default-density-exposed-endpoint",
        w_exposure == (1, 1, 1, 0) and m_exposure == (1, 1, 1, 1),
        "one proper effect exposes the default W endpoint from the convex hull of all eight W and modulus conditional states",
    )

    decoupled_event = sp.Matrix(
        [
            [p_joint[a] * default_density[j, j] for j in range(4)]
            for a in range(4)
        ]
    )
    check(
        "only-endpoint-preserving-route-is-decoupled",
        sp.cancel(sum(decoupled_event, ZERO)) == ONE
        and all(
            sp.cancel(sum(decoupled_event[a, j] for j in range(4)) - p_joint[a])
            == 0
            for a in range(4)
        )
        and any(not matrix_equal(arms[a]["rho_w"], default_density) for a in range(3)),
        "retaining the old density with positive endpoint responses forces every pin to use the same default response and abandons pin faithfulness",
    )

    base_s = arms[-1]["S"]
    congruence = sp.eye(fixture.N)
    congruence[0, 0] = 2
    congruence[1, 1] = R(1, 2)
    alternate_spectator = sp.expand(congruence.H * base_s * congruence)
    check(
        "spectator-determinant-does-not-select-unique-kernel",
        b174.ldl_certificate(alternate_spectator)["pd"]
        and b174.dm_det(alternate_spectator) == b174.dm_det(base_s)
        and not matrix_equal(alternate_spectator, base_s),
        "determinant compensation fixes det(H)=det(S) but not the positive spectator H; choosing the existing S remains downstream content",
    )

    cover_values = (8, 12, 16, 20, 24)
    locality_rows = []
    for cover in cover_values:
        cover_fixture = b174.Fixture(4, tag=f"b177-cover-{cover}", cover_t=cover)
        cover_q = cover_fixture.q({})
        cover_w = b41.positive_completion(cover_q)
        cover_m = b41.modulus_completion(cover_q, cover_w["q_inv"])
        locality_rows.append(
            (
                cover_fixture.T,
                temporal_range(cover_q, cover_fixture),
                temporal_range(cover_w["symmetric"], cover_fixture),
                temporal_range(cover_m["precision"], cover_fixture),
                temporal_range(cover_w["precision"], cover_fixture),
            )
        )
    check(
        "uniform-temporal-locality-tradeoff",
        tuple(row[0] for row in locality_rows) == (4, 6, 8, 10, 12)
        and tuple(row[1] for row in locality_rows) == (1, 1, 1, 1, 1)
        and tuple(row[2] for row in locality_rows) == (1, 1, 1, 1, 1)
        and tuple(row[3] for row in locality_rows) == (2, 2, 2, 2, 2)
        and tuple(row[4] for row in locality_rows) == (2, 3, 4, 5, 6),
        "on the default-carrier ladder q and S stay temporal range one and K_mod range two, while K_W reaches half-cover",
    )

    twin_pattern = b174.twin_pattern(8)
    twin_fixture = b174.Fixture(8, pattern=twin_pattern, tag="b177-twin")
    twin_left_states = b174.menu_states(twin_fixture, b174.RECORD_LEVEL, 0)
    twin_right_states = b174.menu_states(twin_fixture, b174.RECORD_LEVEL, 4)
    twin_det_left = b174.readout_laws(twin_left_states)["sq"]["law"]
    twin_det_right = b174.readout_laws(twin_right_states)["sq"]["law"]
    twin_w_left = normalize(
        tuple(sp.cancel(state["cert"]["det"] / state["n2"]) for state in twin_left_states)
    )
    twin_w_right = normalize(
        tuple(sp.cancel(state["cert"]["det"] / state["n2"]) for state in twin_right_states)
    )
    det_gap = max(
        sp.Abs(sp.cancel(left - right))
        for left, right in zip(twin_det_left, twin_det_right)
    )
    w_gap = max(
        sp.Abs(sp.cancel(left - right))
        for left, right in zip(twin_w_left, twin_w_right)
    )
    check(
        "matched-blanket-finite-locality-failure",
        b174.pattern_certificate(twin_pattern)["same_blanket"]
        and R(4931, 100000000) < det_gap < R(1233, 25000000)
        and R(209783, 10000000000) < w_gap < R(26223, 1250000000),
        "both determinant and W-sector alternative laws differ exactly at a matched-nearest-neighbor twin fixture",
    )

    zero_q = fixture.q({}, mass=ZERO)
    zero_modulus = b41.modulus_completion(zero_q)
    check(
        "zero-mass-domain-separation",
        matrix_zero(b175.herm(zero_q))
        and b174.dm_det(zero_q) != 0
        and b174.ldl_certificate(zero_modulus["precision"])["pd"],
        "at m=0 the W/S product sector stops because S=0, while the local modulus completion remains positive",
    )

    check(
        "source-contract-and-input-closure",
        NOTE.exists()
        and all((ROOT / path).exists() for path in AUDIT_INPUT_PATHS)
        and "zero TOE-percentage movement" in NOTE.read_text(encoding="utf-8"),
        "the bounded note and every declared action, parent, and axiom input exist with the no-score boundary explicit",
    )

    print("per_element: every alternative-effect atom, normalized sector source, endpoint exposure, and refinement coefficient is checked exactly")
    print("per_site: four hard pins, four free response slices, the fixed-default cell, and a matched-blanket twin pair are checked")
    print("per_mode: full positive K_W/S and K_mod sectors, determinant compensation, source blocks, and temporal supports are checked")
    print("per_block: four baseline joint sectors and five default-carrier cover extents separate the algebraic construction from uniform locality")
    print("lattice_wide: checked and not executed — no homogeneous nearest-neighbor Record history or physical sector selector is constructed")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return failed


if __name__ == "__main__":
    raise SystemExit(main())
