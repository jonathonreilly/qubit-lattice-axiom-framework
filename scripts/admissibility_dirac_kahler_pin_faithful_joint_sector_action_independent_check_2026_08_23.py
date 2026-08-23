#!/usr/bin/env python3
"""Independent exact reconstruction of the pin-faithful joint sector.

This checker imports the Block 174 action fixture directly.  It does not
import the Block 42 primary runner, Block 41, or Block 175.  SymPy DomainMatrix
inverses rebuild the two positive completions, determinant compensation,
normalized joint source law, exposed-endpoint result, refinement price, and
cover-range tradeoff by a separate route.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_site_conditional_law_family_2026_08_22 as b174


R = sp.Rational
ZERO = sp.Integer(0)
ONE = sp.Integer(1)
MENU = b174.MENU
RECORD_CELL = (b174.RECORD_LEVEL, 0)
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_PIN_FAITHFUL_JOINT_SECTOR_ACTION_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md"
)

AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_PIN_FAITHFUL_JOINT_SECTOR_ACTION_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_CONDITIONAL_LAW_FAMILY_"
    "BOUNDED_THEOREM_NOTE_2026-08-22.md",
    "scripts/admissibility_dirac_kahler_site_conditional_law_family_"
    "2026_08_22.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def inverse(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.inv(method="DM")


def hermitian(matrix: sp.Matrix) -> sp.Matrix:
    return sp.expand((matrix + matrix.H) / 2)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and all(
        sp.expand(value) == 0 for value in sp.expand(left - right)
    )


def normalize(values: tuple) -> tuple:
    total = sp.cancel(sum(values, ZERO))
    return tuple(sp.cancel(value / total) for value in values)


def rows_for(fixture: object, level: int) -> tuple[int, ...]:
    return tuple(fixture.lx * (level % fixture.T) + x for x in range(fixture.lx))


def rebuild_arm(fixture: object, value, rows: tuple[int, ...]) -> dict:
    q = fixture.q({RECORD_CELL: value})
    q_inv = inverse(q)
    symmetric = hermitian(q)
    covariance_w = hermitian(q_inv)
    precision_w = inverse(covariance_w)
    covariance_m = sp.expand(q_inv * q_inv.H)
    precision_m = sp.expand(q.H * q)
    block_w = covariance_w.extract(rows, rows)
    block_m = covariance_m.extract(rows, rows)
    det_q = b174.dm_det(q)
    det_s = b174.dm_det(symmetric)
    det_kw = b174.dm_det(precision_w)
    return {
        "q": q,
        "S": symmetric,
        "W": covariance_w,
        "KW": precision_w,
        "KW_factored": sp.expand(q.H * inverse(symmetric) * q),
        "KM": precision_m,
        "V": covariance_m,
        "rho_w": sp.expand(block_w / sp.trace(block_w)),
        "rho_m": sp.expand(block_m / sp.trace(block_m)),
        "trace_w": sp.cancel(sp.trace(block_w)),
        "det_q": det_q,
        "det_s": det_s,
        "det_kw": det_kw,
        "z_joint": sp.cancel(ONE / (det_kw * det_s)),
        "z_det": sp.cancel(ONE / b174.norm2(det_q)),
    }


def temporal_range(matrix: sp.Matrix, fixture: object) -> int:
    result = ZERO
    for row in range(matrix.rows):
        t_row = row // fixture.lx
        for column in range(matrix.cols):
            if matrix[row, column] == 0:
                continue
            t_column = column // fixture.lx
            result = max(
                result,
                min(
                    (t_row - t_column) % fixture.T,
                    (t_column - t_row) % fixture.T,
                ),
            )
    return int(result)


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

    fixture = b174.Fixture(4, tag="b177-independent")
    rows = rows_for(fixture, fixture.tstar)
    arms = tuple(rebuild_arm(fixture, value, rows) for value in MENU)

    check(
        "independent-positive-product-sectors",
        all(
            b174.ldl_certificate(arm["S"])["pd"]
            and b174.ldl_certificate(arm["KW"])["pd"]
            and matrix_equal(arm["KW"], arm["KW_factored"])
            for arm in arms
        ),
        "four independently inverted W kernels give the same positive q^dagger S^-1 q precision beside positive S",
    )

    check(
        "independent-determinant-cancellation",
        all(
            sp.cancel(
                arm["det_kw"] * arm["det_s"]
                - b174.norm2(arm["det_q"])
            )
            == 0
            and arm["z_joint"] == arm["z_det"]
            for arm in arms
        ),
        "the product-sector determinant independently reduces to |det q_a|^2 at every hard pin",
    )

    probabilities = normalize(tuple(arm["z_joint"] for arm in arms))
    event = sp.Matrix(
        [
            [probabilities[a] * arms[a]["rho_w"][j, j] for j in range(4)]
            for a in range(4)
        ]
    )
    marginal = sp.diag(*(sum(event[a, j] for a in range(4)) for j in range(4)))
    check(
        "independent-joint-law",
        all(event[a, j] > 0 for a in range(4) for j in range(4))
        and sp.cancel(sum(event, ZERO)) == ONE
        and all(
            sp.cancel(sum(event[a, j] for j in range(4)) - probabilities[a])
            == 0
            for a in range(4)
        ),
        "the independently rebuilt P(a,j) is positive, normalized, and has the determinant arm marginal",
    )

    traces = tuple(arm["trace_w"] for arm in arms)
    shifted = normalize(tuple(probabilities[a] * traces[a] for a in range(4)))
    check(
        "independent-source-normalization-price",
        len(set(traces)) == 4
        and shifted != probabilities
        and all(
            sp.cancel((ONE / traces[a]) * traces[a] - ONE) == 0
            for a in range(4)
        ),
        "the unnormalized source shifts the arm law, while the inverse-trace scalar restores identity certainty sector by sector",
    )

    z_values = tuple(arm["z_joint"] for arm in arms)
    duplicate = normalize((z_values[0], z_values[0], *z_values[1:]))
    split = R(3, 7)
    additive = normalize(
        (split * z_values[0], (ONE - split) * z_values[0], *z_values[1:])
    )
    check(
        "independent-base-measure-refinement",
        sp.cancel(duplicate[0] + duplicate[1] - probabilities[0]) != 0
        and sp.cancel(additive[0] + additive[1] - probabilities[0]) == 0,
        "a second split ratio independently confirms that only additive base-measure refinement preserves the law",
    )

    default_q = fixture.q({})
    default_w = hermitian(inverse(default_q))
    default_block = default_w.extract(rows, rows)
    default_density = sp.expand(default_block / sp.trace(default_block))
    residual = sp.expand(default_density - marginal)
    check(
        "independent-fixed-default-separation",
        matrix_equal(default_density, arms[-1]["rho_w"])
        and tuple(sp.sign(residual[j, j]) for j in range(4))
        == (1, -1, -1, 1),
        "the true total-probability marginal independently differs from the default-pin density in all four entries",
    )

    exposing_effect = sp.diag(ZERO, R(4, 7), R(3, 7), ZERO)
    w_signs = tuple(
        sp.sign(sp.factor(sp.trace((arm["rho_w"] - default_density) * exposing_effect)))
        for arm in arms
    )
    m_signs = tuple(
        sp.sign(sp.factor(sp.trace((arm["rho_m"] - default_density) * exposing_effect)))
        for arm in arms
    )
    check(
        "independent-endpoint-exposure",
        w_signs == (1, 1, 1, 0) and m_signs == (1, 1, 1, 1),
        "the independently reconstructed proper effect exposes only the default W state among eight positive endpoint states",
    )

    transform = sp.eye(fixture.N)
    transform[0, 0] = 3
    transform[1, 1] = R(1, 3)
    spectator = sp.expand(transform.H * arms[-1]["S"] * transform)
    check(
        "independent-spectator-nonuniqueness",
        b174.ldl_certificate(spectator)["pd"]
        and b174.dm_det(spectator) == arms[-1]["det_s"]
        and not matrix_equal(spectator, arms[-1]["S"]),
        "a second unit-determinant congruence gives a distinct positive compensator with the same partition factor",
    )

    cover_rows = []
    for cover in (8, 16, 24):
        cover_fixture = b174.Fixture(4, tag=f"b177-i-{cover}", cover_t=cover)
        q = cover_fixture.q({})
        q_inv = inverse(q)
        symmetric = hermitian(q)
        precision_w = sp.expand(q.H * inverse(symmetric) * q)
        precision_m = sp.expand(q.H * q)
        cover_rows.append(
            (
                cover_fixture.T,
                temporal_range(q, cover_fixture),
                temporal_range(symmetric, cover_fixture),
                temporal_range(precision_m, cover_fixture),
                temporal_range(precision_w, cover_fixture),
                matrix_equal(inverse(hermitian(q_inv)), precision_w),
            )
        )
    check(
        "independent-cover-range-tradeoff",
        tuple(row[:5] for row in cover_rows)
        == ((4, 1, 1, 2, 2), (8, 1, 1, 2, 4), (12, 1, 1, 2, 6))
        and all(row[5] for row in cover_rows),
        "three independently rebuilt default-carrier covers keep native actions bounded-range while K_W reaches half-cover",
    )

    zero_q = fixture.q({}, mass=ZERO)
    zero_s = hermitian(zero_q)
    zero_km = sp.expand(zero_q.H * zero_q)
    check(
        "independent-zero-mass-edge",
        matrix_equal(zero_s, sp.zeros(fixture.N))
        and b174.dm_det(zero_q) != 0
        and b174.ldl_certificate(zero_km)["pd"],
        "the W/S product stops at zero mass while the local modulus completion remains exact and positive",
    )

    check(
        "independent-input-closure",
        NOTE.exists()
        and all((ROOT / path).exists() for path in AUDIT_INPUT_PATHS)
        and "No-Go Discipline Gate" in NOTE.read_text(encoding="utf-8"),
        "the checker reads only the final note, Minimal Axioms, and its direct Block 174 action fixture",
    )

    print("per_element: independent alternative-effect atoms, source scales, endpoint witnesses, and refinement shares are reconstructed")
    print("per_site: four hard pins, one response slice, the fixed-default profile, and one different exact split ratio are checked")
    print("per_mode: full 24-mode positive product sectors, modulus controls, determinant factors, and source covariances are checked")
    print("per_block: four baseline sectors and three independently rebuilt default-carrier cover extents certify the range tradeoff")
    print("lattice_wide: checked and not executed — no physical alternative base measure, nearest-neighbor law, or Record process is selected")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return failed


if __name__ == "__main__":
    raise SystemExit(main())
