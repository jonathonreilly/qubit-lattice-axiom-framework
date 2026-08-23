#!/usr/bin/env python3
"""Exact Schur-response bridge between the pincer action and Record grades.

The parent pincer fixture supplies a complex action matrix q and the positive
kernel W9 = herm(q^-1).  This runner proves that W9 has the positive precision
K_W = q^dagger herm(q)^-1 q, integrates exterior modes by an exact Schur
complement, and evaluates the resulting local Gaussian source response.  It
also keeps the distinct modulus-square completion and hard-pin formation law
separate, so an action-derived marginal is not silently renamed a formation
conditional.
"""

from __future__ import annotations

import inspect
from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_pincer_identity_cross_lane_2026_08_22 as b175


b174 = b175.b174
R = sp.Rational
ZERO = sp.Integer(0)
ONE = sp.Integer(1)
I2 = sp.eye(2)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_SCHUR_RECORD_RESPONSE_BRIDGE_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md"
)

AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SCHUR_RECORD_RESPONSE_BRIDGE_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md",
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


def matrix_zero(value: sp.Matrix) -> bool:
    return all(sp.expand(entry) == 0 for entry in value)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and matrix_zero(sp.expand(left - right))


def positive_completion(q: sp.Matrix) -> dict:
    """The W9 covariance and its positive precision, rebuilt from q."""
    q_inv = b175.exact_inv(q)
    symmetric = b175.herm(q)
    symmetric_inv = b175.exact_inv(symmetric)
    covariance = sp.expand((q_inv + q_inv.H) / 2)
    precision = sp.expand(q.H * symmetric_inv * q)
    return {
        "q_inv": q_inv,
        "symmetric": symmetric,
        "covariance": covariance,
        "precision": precision,
    }


def modulus_completion(q: sp.Matrix, q_inv: sp.Matrix | None = None) -> dict:
    """The distinct positive completion whose determinant is |det q|^2."""
    q_inv = b175.exact_inv(q) if q_inv is None else q_inv
    return {
        "covariance": sp.expand(q_inv * q_inv.H),
        "precision": sp.expand(q.H * q),
    }


def slice_rows(fixture: object, level: int) -> tuple[int, ...]:
    return tuple(fixture.lx * (level % fixture.T) + x for x in range(fixture.lx))


def normalized_block(covariance: sp.Matrix, rows: tuple[int, ...]) -> sp.Matrix:
    block = covariance.extract(rows, rows)
    return sp.expand(block / sp.trace(block))


def schur_precision(
    precision: sp.Matrix, rows: tuple[int, ...]
) -> tuple[sp.Matrix, sp.Matrix]:
    exterior = tuple(index for index in range(precision.rows) if index not in rows)
    local = precision.extract(rows, rows)
    local_exterior = precision.extract(rows, exterior)
    exterior_local = precision.extract(exterior, rows)
    exterior_precision = precision.extract(exterior, exterior)
    schur = sp.expand(
        local
        - local_exterior
        * b175.exact_inv(exterior_precision)
        * exterior_local
    )
    return schur, exterior_precision


def source_grade(precision: sp.Matrix, effect: sp.Matrix):
    covariance = b175.exact_inv(precision)
    return sp.cancel(sp.trace(covariance * effect) / sp.trace(covariance))


def basis_projector(index: int, dimension: int = 4) -> sp.Matrix:
    return sp.diag(*(ONE if position == index else ZERO for position in range(dimension)))


def normalize(values: tuple) -> tuple:
    total = sp.cancel(sum(values, ZERO))
    return tuple(sp.cancel(value / total) for value in values)


def projectively_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    ratio = None
    for l_value, r_value in zip(left, right):
        if r_value != 0:
            ratio = sp.cancel(l_value / r_value)
            break
        if l_value != 0:
            return False
    if ratio is None or ratio <= 0:
        return False
    return matrix_equal(left, sp.expand(ratio * right))


def response_state(precision: sp.Matrix) -> sp.Matrix:
    inverse = b175.exact_inv(precision)
    return sp.expand(inverse / sp.trace(inverse))


def raw_response(precision: sp.Matrix, effect: sp.Matrix):
    partition = sp.cancel(sp.pi**4 / precision.det() ** 2)
    return sp.cancel(2 * partition * sp.trace(b175.exact_inv(precision) * effect))


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

    fixture = b174.Fixture(b175.LX, tag="b176-schur")
    q = fixture.q({})
    completion = positive_completion(q)
    covariance = completion["covariance"]
    precision = completion["precision"]

    check(
        "positive-action-completion",
        b174.ldl_certificate(completion["symmetric"])["pd"]
        and matrix_equal(
            covariance,
            sp.expand(
                completion["q_inv"]
                * completion["symmetric"]
                * completion["q_inv"].H
            ),
        )
        and matrix_equal(precision * covariance, sp.eye(fixture.N))
        and b174.ldl_certificate(precision)["pd"],
        "W=Herm(q^-1)=q^-1 Herm(q) q^-dagger has exact positive precision K_W=q^dagger Herm(q)^-1 q",
    )

    rows = slice_rows(fixture, fixture.tstar)
    block = covariance.extract(rows, rows)
    schur, exterior_precision = schur_precision(precision, rows)
    check(
        "exact-local-schur-inverse",
        b174.ldl_certificate(exterior_precision)["pd"]
        and matrix_equal(schur, b175.exact_inv(block)),
        "integrating the twenty exterior modes gives the exact inverse of the four-mode W9 block",
    )

    density = normalized_block(covariance, rows)
    pincer_profile = tuple(b174.profile_of(fixture, {})[0])
    schur_profile = tuple(source_grade(schur, basis_projector(j)) for j in range(4))
    check(
        "action-derived-pincer-marginal",
        schur_profile == pincer_profile
        and schur_profile == tuple(density[j, j] for j in range(4)),
        "the local Gaussian source response reproduces the parent pincer marginal entry for entry",
    )

    level_profiles = []
    level_ok = True
    for level in fixture.free_levels:
        level_rows = slice_rows(fixture, level)
        level_block = covariance.extract(level_rows, level_rows)
        level_schur, level_exterior = schur_precision(precision, level_rows)
        level_density = normalized_block(covariance, level_rows)
        level_profile = tuple(level_density[j, j] for j in range(fixture.lx))
        level_profiles.append(level_profile)
        level_ok = level_ok and (
            b174.ldl_certificate(level_exterior)["pd"]
            and matrix_equal(level_schur, b175.exact_inv(level_block))
            and all(
                level_block[i, j] == 0
                for i in range(fixture.lx)
                for j in range(fixture.lx)
                if i != j
            )
            and all(value > 0 for value in level_profile)
            and sp.cancel(sum(level_profile, ZERO)) == ONE
            and tuple(
                source_grade(level_schur, basis_projector(j))
                for j in range(fixture.lx)
            )
            == level_profile
        )
    check(
        "four-free-level-ladder",
        level_ok
        and len(level_profiles) == 4
        and len(set(level_profiles)) == 4,
        "all four free levels are S-DIAG, positive, Schur-derived, response-consistent, and pairwise distinct",
    )

    dial_ok = True
    dial_count = 0
    block_count = 0
    for index, (_label, config) in enumerate(b174.DIAL_POINTS):
        if index == b174.ZERO_MASS_INDEX:
            continue
        dial_count += 1
        dial_q = fixture.q({}, **config)
        dial_completion = positive_completion(dial_q)
        dial_ok = dial_ok and b174.ldl_certificate(dial_completion["symmetric"])["pd"]
        dial_ok = dial_ok and matrix_equal(
            dial_completion["precision"] * dial_completion["covariance"],
            sp.eye(fixture.N),
        )
        for level in fixture.free_levels:
            block_count += 1
            dial_rows = slice_rows(fixture, level)
            dial_block = dial_completion["covariance"].extract(dial_rows, dial_rows)
            dial_schur, _ = schur_precision(dial_completion["precision"], dial_rows)
            dial_density = normalized_block(dial_completion["covariance"], dial_rows)
            dial_ok = dial_ok and matrix_equal(dial_schur, b175.exact_inv(dial_block))
            dial_ok = dial_ok and all(
                dial_block[i, j] == 0
                for i in range(fixture.lx)
                for j in range(fixture.lx)
                if i != j
            )
            dial_ok = dial_ok and all(dial_density[j, j] > 0 for j in range(fixture.lx))
    check(
        "nonzero-mass-action-ladder",
        dial_ok and dial_count == 14 and block_count == 56,
        "fourteen exact nonzero-mass action dials give 56 positive S-DIAG blocks with zero Schur residual",
    )

    zero_mass_q = fixture.q({}, mass=ZERO)
    check(
        "zero-mass-boundary",
        matrix_zero(b175.herm(zero_mass_q)),
        "at m=0 the Hermitian action vanishes, so the positive W precision construction honestly has no inverse",
    )

    modulus = modulus_completion(q, completion["q_inv"])
    w_profile = tuple(normalized_block(covariance, rows)[j, j] for j in range(4))
    v_profile = tuple(
        normalized_block(modulus["covariance"], rows)[j, j] for j in range(4)
    )
    det_q = b174.dm_det(q)
    det_symmetric = b174.dm_det(completion["symmetric"])
    check(
        "two-positive-completions",
        matrix_equal(modulus["precision"] * modulus["covariance"], sp.eye(fixture.N))
        and b174.ldl_certificate(modulus["precision"])["pd"]
        and b174.dm_det(modulus["precision"]) == b174.norm2(det_q)
        and sp.cancel(b174.dm_det(precision) - b174.norm2(det_q) / det_symmetric) == 0
        and w_profile != v_profile,
        "K_mod=q^dagger q and K_W=q^dagger Herm(q)^-1 q are distinct exact positive completions of one complex q",
    )

    pinned = []
    raw_modulus = []
    raw_w = []
    for value in b175.MENU:
        pinned_q = fixture.q({b175.RECORD_CELL: value})
        pinned_completion = positive_completion(pinned_q)
        pinned_modulus = modulus_completion(pinned_q, pinned_completion["q_inv"])
        pinned.append((pinned_completion, pinned_modulus))
        pinned_det = b174.dm_det(pinned_q)
        pinned_det_symmetric = b174.dm_det(pinned_completion["symmetric"])
        raw_modulus.append(sp.cancel(ONE / b174.norm2(pinned_det)))
        raw_w.append(sp.cancel(pinned_det_symmetric / b174.norm2(pinned_det)))
    modulus_law = normalize(tuple(raw_modulus))
    w_partition_law = normalize(tuple(raw_w))
    check(
        "completion-partition-split",
        all(value > 0 for value in raw_modulus)
        and all(value > 0 for value in raw_w)
        and modulus_law != w_partition_law
        and tuple(
            sp.sign(sp.cancel(w_partition_law[j] - modulus_law[j]))
            for j in range(4)
        )
        == (-1, -1, 1, 1),
        "the squared-amplitude formation law is the K_mod partition, while the W9-positive completion carries a distinct determinant factor",
    )

    pinned_densities = tuple(
        normalized_block(item[0]["covariance"], rows) for item in pinned
    )
    formation_mix = sp.expand(
        sum(
            (modulus_law[j] * pinned_densities[j] for j in range(4)),
            sp.zeros(4),
        )
    )
    formation_residual = sp.expand(density - formation_mix)
    check(
        "formation-law-total-mixture-fails",
        not matrix_zero(formation_residual)
        and tuple(sp.sign(formation_residual[j, j]) for j in range(4))
        == (1, -1, -1, 1),
        "averaging pinned W9 densities with the determinant formation law does not reconstruct the unpinned marginal",
    )

    weights = sp.symbols("p0:4", real=True)
    equations = [
        sum(weights[a] * pinned_densities[a][j, j] for a in range(4))
        - density[j, j]
        for j in range(4)
    ] + [sum(weights, ZERO) - ONE]
    solution = next(iter(sp.linsolve(equations, weights)))
    derivatives = tuple(sp.sign(sp.diff(entry, weights[3])) for entry in solution)
    at_default = tuple(sp.cancel(entry.subs(weights[3], ONE)) for entry in solution)
    check(
        "only-nonnegative-reconstruction-is-default",
        sp.Matrix(
            [
                [pinned_densities[a][j, j] - pinned_densities[3][j, j] for a in range(3)]
                for j in range(4)
            ]
        ).rank()
        == 2
        and derivatives == (-1, 1, -1, 1)
        and at_default == (ZERO, ZERO, ZERO, ONE)
        and matrix_equal(density, pinned_densities[3])
        and all(value > 0 for value in modulus_law),
        "the affine solution is one-dimensional but positivity forces delta at the default sigma=3/5, not the four-positive formation law",
    )

    field_source = inspect.getsource(b174.Fixture.field)
    check(
        "fixed-background-not-value-union",
        "records.get((t, x), sigma)" in field_source
        and matrix_equal(q, fixture.q({b175.RECORD_CELL: b175.MENU[-1]})),
        "an unrecorded cell uses the fixed default sigma=3/5; the present q is not a sum or integral over Record alternatives",
    )

    w_joint_block = sum(
        (
            raw_w[j] * pinned[j][0]["covariance"].extract(rows, rows)
            for j in range(4)
        ),
        sp.zeros(4),
    )
    w_joint_density = sp.expand(w_joint_block / sp.trace(w_joint_block))
    mod_joint_block = sum(
        (
            raw_modulus[j] * pinned[j][1]["covariance"].extract(rows, rows)
            for j in range(4)
        ),
        sp.zeros(4),
    )
    mod_joint_density = sp.expand(mod_joint_block / sp.trace(mod_joint_block))
    check(
        "candidate-joint-ensembles-are-new",
        not matrix_equal(w_joint_density, density)
        and not matrix_equal(
            mod_joint_density,
            normalized_block(modulus["covariance"], rows),
        )
        and not matrix_equal(w_joint_density, mod_joint_density),
        "both explicit sum-over-pin ensembles differ from the fixed-background object and from each other",
    )

    center = sp.diag(R(3, 5), R(2, 5))
    shared_effect = sp.diag(R(1, 2), ZERO)
    mixed = I2 / 2
    inverse_grade = source_grade(b175.exact_inv(center), shared_effect)
    square_grade = source_grade(b175.exact_inv(center**2), shared_effect)
    check(
        "strict-neighbor-equivariant-counterfamily",
        inverse_grade == R(3, 10)
        and square_grade == R(9, 26)
        and source_grade(b175.exact_inv(mixed), shared_effect) == R(1, 4)
        and source_grade(b175.exact_inv(mixed**2), shared_effect) == R(1, 4),
        "C and C^2 response states agree at I/2 but differ by 3/65 on the existing non-scalar nearest-neighbor effect",
    )

    transform = sp.Matrix([[2, 1], [0, 1]])
    transformed_center = sp.expand(
        transform * center * transform.H
        / sp.trace(transform * center * transform.H)
    )
    inverse_pullback = sp.expand(
        transform.inv().H * b175.exact_inv(center) * transform.inv()
    )

    def alpha_precision(value: sp.Matrix, alpha=ONE) -> sp.Matrix:
        inverse = b175.exact_inv(value)
        raw = sp.expand(inverse + alpha * sp.trace(inverse) * I2)
        return sp.expand(raw / (2 * sp.trace(value * raw)))

    check(
        "projective-congruence-selector",
        projectively_equal(b175.exact_inv(transformed_center), inverse_pullback)
        and not projectively_equal(
            alpha_precision(transformed_center),
            sp.expand(transform.inv().H * alpha_precision(center) * transform.inv()),
        ),
        "contravariant GL congruence selects the inverse ray and rejects an exact positive unitary-covariant counterfamily",
    )

    scale = sp.Integer(3)
    base_raw = raw_response(b175.exact_inv(center), shared_effect)
    scaled_raw = raw_response(scale * b175.exact_inv(center), shared_effect)
    base_identity = raw_response(b175.exact_inv(center), I2)
    scaled_identity = raw_response(scale * b175.exact_inv(center), I2)
    check(
        "scalar-action-gauge",
        sp.cancel(scaled_raw - base_raw / scale**5) == 0
        and source_grade(scale * b175.exact_inv(center), shared_effect) == inverse_grade
        and sp.cancel(
            scaled_raw / scaled_identity - base_raw / base_identity
        )
        == 0,
        "Q->gQ rescales raw DZ by g^-5 but leaves the identity-normalized grade and calibrated hazard unchanged",
    )

    check(
        "pure-boundary-separation",
        response_state(sp.diag(2, 3)).det() > 0
        and sp.diag(ONE, ZERO).det() == 0,
        "a finite positive precision has a full-rank response state, so an exact pure preparation needs a singular or limiting prescription",
    )

    check(
        "source-contract-and-input-closure",
        NOTE.exists()
        and all((ROOT / path).exists() for path in AUDIT_INPUT_PATHS)
        and "zero TOE-percentage movement" in NOTE.read_text(encoding="utf-8"),
        "the final theorem note and every declared action, axiom, and parent input exist with the no-score boundary explicit",
    )

    print("per_element: every local projector source, pinned alternative, response grade, and mixture coefficient is checked exactly")
    print("per_site: four free slices and the hard-pin versus fixed-background semantics at the selected Record cell are checked")
    print("per_mode: all 24 complex action modes, two positive completions, exterior integrations, and source-response quotients are checked")
    print("per_block: fourteen nonzero-mass action dials produce 56 exact Schur-response blocks plus the m=0 boundary")
    print("lattice_wide: checked and not executed — no autonomous global Record history or infinite-volume selector is claimed")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return failed


if __name__ == "__main__":
    raise SystemExit(main())
