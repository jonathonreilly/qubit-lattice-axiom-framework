#!/usr/bin/env python3
"""Exact Block-177 falsifier for the proposed rank-one-only scalar theorem.

The parent (Block 176) explicitly asks whether every transport-sensitive
positive compression of its committed reflection form is rank one.  This
runner reconstructs that committed form through the landed Block-170 bench and
exhibits a rank-two isometric compression that is positive definite and has a
nonzero exact transport derivative at both retained cover extents.

The result is deliberately narrow.  It falsifies the literal successor thesis;
it does not select a readout, derive the Born rule, or exclude narrower
non-affine/non-convex readout categories.
"""

from __future__ import annotations

import ast
from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_closure_audit_two_2026_08_21 as b170
import admissibility_dirac_kahler_pincer_identity_cross_lane_2026_08_22 as b175


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RANK_TWO_SCALAR_TRANSPORT_"
    "COUNTEREXAMPLE_BOUNDED_THEOREM_NOTE_2026-08-23.md"
)

R = sp.Rational
ZERO = sp.Integer(0)
ONE = sp.Integer(1)
TRANSPORT = sp.symbols("s_t", real=True)
EXPECTED_ROWS = (4, 5, 6, 7, 8, 9, 10, 11)
EXPECTED_SCALAR = R(114, 125) + R(171, 250) * TRANSPORT
EXPECTED_GAP = R(513, 2000)
EXPECTED_DETERMINANT = (
    R(3249, 62500) * (3 * TRANSPORT + 4) ** 2
)

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, condition: bool, detail: str) -> None:
    CHECKS.append((name, bool(condition), detail))


def is_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.expand(entry) == 0 for entry in matrix)


def isometry() -> sp.Matrix:
    x0 = sp.zeros(8, 1)
    x2 = sp.zeros(8, 1)
    x0[0], x0[4] = R(4, 5), R(3, 5)
    x2[2], x2[6] = R(4, 5), R(3, 5)
    return x0.row_join(x2)


def committed_form(tag: str, cover_t: int) -> tuple[b170.Bench, sp.Matrix]:
    """F_T(s_t)=Herm(Sel_S^T r_T Q_T(s_t) Sel_S), from Block 170."""
    bench = b170.Bench(tag, cover_t, 4)
    return bench, sp.expand(bench.form.subs(bench.carrier(st=TRANSPORT)))


def exact_fixture_checks() -> dict[str, dict]:
    x = isometry()
    expected = EXPECTED_SCALAR * sp.eye(2)
    results: dict[str, dict] = {}
    for tag, cover_t in (("8x4", 8), ("12x4", 12)):
        bench, form = committed_form(tag, cover_t)
        compression = sp.expand(x.H * form * x)
        determinant = sp.factor(compression.det())
        at_small = sp.expand(compression.subs(TRANSPORT, R(1, 8)))
        at_large = sp.expand(compression.subs(TRANSPORT, R(1, 2)))
        derivative = sp.diff(sp.trace(compression) / 2, TRANSPORT)
        gap = sp.expand(sp.trace(at_large - at_small) / 2)
        results[tag] = {
            "rows": tuple(bench.rows),
            "shape": compression.shape,
            "compression": compression,
            "determinant": determinant,
            "at_small": at_small,
            "at_large": at_large,
            "derivative": derivative,
            "gap": gap,
        }
        check(
            f"{tag} committed row map",
            tuple(bench.rows) == EXPECTED_ROWS and form.shape == (8, 8),
            f"rows={tuple(bench.rows)}, form_shape={form.shape}",
        )
        check(
            f"{tag} exact rank-two scalar compression",
            is_zero(compression - expected),
            f"X^H F X={compression}",
        )
        check(
            f"{tag} positive and transport-sensitive",
            (
                compression.rank() == 2
                and at_small == R(399, 400) * sp.eye(2)
                and at_large == R(627, 500) * sp.eye(2)
                and derivative == R(171, 250)
                and gap == EXPECTED_GAP
                and determinant == EXPECTED_DETERMINANT
            ),
            (
                f"slope={derivative}, gap={gap}, "
                f"det={determinant}, endpoints=({at_small[0, 0]},"
                f"{at_large[0, 0]})"
            ),
        )
    check(
        "rank-two isometry",
        x.H * x == sp.eye(2) and x.rank() == 2,
        f"X^H X={x.H * x}, rank={x.rank()}",
    )
    check(
        "extent-independent compressed law",
        results["8x4"]["compression"] == results["12x4"]["compression"],
        "the exact 2x2 law agrees at cover extents 8x4 and 12x4",
    )
    return results


def affine_closure_checks() -> None:
    """The convex-affine obstruction and one exact normalized witness.

    If an affine effect P has response d != 0, adding epsilon Q changes the
    response to d+epsilon*q.  This affine polynomial is not identically zero
    and has at most one tuned root.  The concrete diagonal witness also shows
    that normalization by trace does not restore blindness.
    """
    epsilon, d, q = sp.symbols("epsilon d q", real=True)
    response = d + epsilon * q
    polynomial = sp.Poly(response, epsilon)
    check(
        "generic affine admixture obstruction",
        polynomial.degree() <= 1 and polynomial.eval(0) == d,
        "response d+epsilon*q has nonzero constant d and at most one tuned root",
    )

    p = sp.diag(1, 0)
    q_effect = sp.diag(0, 1)
    difference = sp.diag(1, -2)
    eps = R(1, 4)
    mixed = p + eps * q_effect
    raw = sp.trace(mixed * difference)
    normalized = sp.cancel(raw / sp.trace(mixed))
    check(
        "normalized rank-two affine witness",
        (
            mixed.rank() == 2
            and raw == R(1, 2)
            and normalized == R(2, 5)
            and mixed.is_positive_definite
        ),
        f"rank={mixed.rank()}, raw={raw}, normalized={normalized}",
    )


def native_effect_check() -> None:
    """Block 175 already uses rank-two union effects in its effect algebra."""
    density = sp.diag(
        *(
            R(n, b175.DENSITY_DENOMINATOR)
            for n in b175.DENSITY_NUMERATORS
        )
    )
    effect = b175.effect_for((b175.MENU[1], b175.MENU[2]))
    reading = b175.trace_reading(density, effect)
    expected = R(
        b175.DENSITY_NUMERATORS[1] + b175.DENSITY_NUMERATORS[2],
        b175.DENSITY_DENOMINATOR,
    )
    check(
        "native rank-two union effect",
        (
            effect.rank() == 2
            and effect == sp.diag(0, 1, 1, 0)
            and reading == expected
            and reading > 0
        ),
        f"rank={effect.rank()}, Tr(C E_12)={reading}",
    )


def source_hygiene_check() -> None:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    floats = [node for node in ast.walk(tree)
              if isinstance(node, ast.Constant) and isinstance(node.value, float)]
    note = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    required = tuple(f"## N{i}" for i in range(1, 9))
    check(
        "exact-source and no-go-discipline surface",
        not floats and all(section in note for section in required),
        f"float_literals={len(floats)}, N_sections={sum(s in note for s in required)}/8",
    )


def main() -> int:
    exact_fixture_checks()
    affine_closure_checks()
    native_effect_check()
    source_hygiene_check()

    for name, passed, detail in CHECKS:
        print(f"{'PASS' if passed else 'FAIL'}: {name} :: {detail}")

    # N5 resolution lines are intentionally explicit in cached stdout.
    print("per_element: exact affine-effect response and the rank-two isometry are proved, with no statement about nonlinear determinant categories")
    print("per_site: the committed eight-row reflection form is reconstructed exactly at both retained 8x4 and 12x4 finite fixtures")
    print("per_mode: the displayed rank-two scalar compression is positive definite and changes exactly with the supplied s_t transport dial")
    print("per_block: the literal Block-176 rank-one-only successor thesis is falsified; the parent proposal remains unadopted and unselected")
    print("lattice_wide: no infinite-volume, all-lattice, physical-readout-selection, Born-rule, gravity, or whole-TOE conclusion is licensed")

    passed = sum(ok for _, ok, _ in CHECKS)
    total = len(CHECKS)
    print(f"TOTAL: {passed}/{total} {'PASS' if passed == total else 'FAIL'}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
