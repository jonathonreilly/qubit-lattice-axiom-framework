#!/usr/bin/env python3
"""Independent exact check of the Block 177 rank-two scalar witness.

The committed two-slice forms are reconstructed through Block 170's ``Bench``
objects.  This checker then builds its compression witness independently and
also proves a separate symbolic affine-admixture lemma.  No floating-point
arithmetic is used.
"""

from __future__ import annotations

import importlib
import sys
from dataclasses import dataclass
from pathlib import Path

import sympy as sp


sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

BLOCK170_MODULE = "admissibility_dirac_kahler_closure_audit_two_2026_08_21"
BLOCK170_PATH = SCRIPTS / f"{BLOCK170_MODULE}.py"

R = sp.Rational
I = sp.I


@dataclass
class Reporter:
    passed: int = 0
    failed: int = 0

    def check(self, name: str, condition: bool, detail: str) -> None:
        if bool(condition):
            self.passed += 1
            status = "PASS"
        else:
            self.failed += 1
            status = "FAIL"
        print(f"{status} {name}: {detail}")

    def total(self) -> None:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    """Exact entrywise matrix equality, with no numerical fallback."""
    if left.shape != right.shape:
        return False
    return all(sp.simplify(a - b) == 0 for a, b in zip(left, right))


def is_exact_pd_2x2(matrix: sp.MatrixBase) -> bool:
    """Sylvester's criterion, evaluated exactly for a Hermitian 2x2 matrix."""
    return bool(
        matrix.shape == (2, 2)
        and matrix_equal(matrix, matrix.H)
        and sp.simplify(matrix[0, 0]).is_positive is True
        and sp.simplify(matrix.det()).is_positive is True
    )


def witness_isometry(size: int) -> sp.Matrix:
    """X=[(4e0+3e4)/5,(4e2+3e6)/5] in the two-slice support."""
    identity = sp.eye(size)
    e0, e2 = identity.col(0), identity.col(2)
    e4, e6 = identity.col(4), identity.col(6)
    return sp.Matrix.hstack((4 * e0 + 3 * e4) / 5,
                            (4 * e2 + 3 * e6) / 5)


def reconstruct_fixture(b170, fixture: tuple[str, int, int]) -> dict:
    """Reconstruct F_T(s_t) directly from one committed Block 170 Bench."""
    tag, cover_t, width = fixture
    bench = b170.Bench(tag, cover_t, width)
    environment = bench.carrier(st=None)
    form = sp.expand(bench.form.subs(environment))
    witness = witness_isometry(form.rows)
    compression = sp.expand(witness.H * form * witness)
    return {
        "tag": tag,
        "form": form,
        "witness": witness,
        "compression": compression,
    }


def check_fixture(reconstruction: dict, st: sp.Symbol,
                  reporter: Reporter) -> None:
    tag = reconstruction["tag"]
    form = reconstruction["form"]
    witness = reconstruction["witness"]
    compression = reconstruction["compression"]
    identity_two = sp.eye(2)
    expected_scalar = R(114, 125) + R(171, 250) * st
    expected_compression = expected_scalar * identity_two

    reporter.check(
        f"{tag}_FORM",
        form.shape == (8, 8) and form.free_symbols == {st}
        and matrix_equal(form, form.H),
        f"shape={form.shape}, free_symbols={sorted(map(str, form.free_symbols))}",
    )
    reporter.check(
        f"{tag}_ISOMETRY",
        matrix_equal(witness.H * witness, identity_two),
        "X^dagger X=I_2",
    )
    reporter.check(
        f"{tag}_COMPRESSION",
        matrix_equal(compression, expected_compression),
        f"X^dagger F_T X=({expected_scalar}) I_2",
    )

    points = (sp.Integer(0), R(1, 8), R(1, 2), sp.Integer(1))
    point_results = []
    point_ok = True
    for point in points:
        evaluated = sp.simplify(compression.subs(st, point))
        scalar = sp.simplify(expected_scalar.subs(st, point))
        determinant = sp.simplify(evaluated.det())
        point_ok = bool(
            point_ok
            and determinant == scalar ** 2
            and is_exact_pd_2x2(evaluated)
        )
        point_results.append(f"{point}:{determinant}")
    reporter.check(
        f"{tag}_RATIONAL_PD",
        point_ok,
        "det(s_t)=" + ",".join(point_results) + "; all PD",
    )

    slope = compression.applyfunc(lambda entry: sp.diff(entry, st))
    gap = sp.expand(compression.subs(st, R(1, 2))
                    - compression.subs(st, R(1, 8)))
    reporter.check(
        f"{tag}_TRANSPORT_RESPONSE",
        matrix_equal(slope, R(171, 250) * identity_two)
        and matrix_equal(gap, R(513, 2000) * identity_two)
        and not matrix_equal(gap, sp.zeros(2)),
        "slope=(171/250)I_2; gap[1/8->1/2]=(513/2000)I_2",
    )


def check_affine_admixture_lemma(reporter: Reporter) -> None:
    """Construct a rank-two sensitive effect from any sensitive rank-one one.

    For a generic Hermitian response Delta, P sees ``d != 0``.  The positive
    choice epsilon*=d^2/[2(d^2+q^2)] lies in (0,1), makes P+epsilon*Q a
    rank-two effect, and leaves the affine response nonzero with the sign of d.
    """
    d = sp.Symbol("d", real=True, nonzero=True)
    q, x, y = sp.symbols("q x y", real=True)
    epsilon = sp.Symbol("epsilon", real=True, positive=True)

    delta = sp.Matrix([[d, x + I * y], [x - I * y, q]])
    rank_one = sp.diag(1, 0)
    added_ray = sp.diag(0, 1)
    rank_two = rank_one + epsilon * added_ray
    response = sp.expand(sp.trace(rank_two * delta))

    reporter.check(
        "AFFINE_RESPONSE_IDENTITY",
        matrix_equal(delta, delta.H)
        and sp.simplify(sp.trace(rank_one * delta) - d) == 0
        and sp.simplify(response - (d + epsilon * q)) == 0,
        "Tr[(P+epsilon Q)Delta]=d+epsilon q with Tr[P Delta]=d!=0",
    )
    reporter.check(
        "GENERIC_RANK_TWO_PSD",
        rank_one.rank() == 1 and rank_two.rank() == 2
        and sp.simplify(rank_two.det() - epsilon) == 0
        and epsilon.is_positive is True,
        "P+epsilon Q has determinant epsilon>0 and rank 2",
    )

    sum_squares = d ** 2 + q ** 2
    epsilon_star = sp.factor(d ** 2 / (2 * sum_squares))
    effect_gap = sp.factor(1 - epsilon_star)
    persisted = sp.factor(response.subs(epsilon, epsilon_star))
    positive_numerator = sp.expand(2 * sum_squares + d * q)
    positive_certificate = (
        R(3, 2) * sum_squares + R(1, 2) * (d + q) ** 2)
    expected_persisted = d * positive_numerator / (2 * sum_squares)
    rank_two_star = rank_two.subs(epsilon, epsilon_star)

    reporter.check(
        "AFFINE_ADMIXTURE_EFFECT",
        epsilon_star.is_positive is True
        and effect_gap.is_positive is True
        and rank_two_star.rank() == 2
        and sp.simplify(rank_two_star.det() - epsilon_star) == 0,
        "epsilon*=d^2/[2(d^2+q^2)] gives 0<epsilon*<1 and a rank-2 effect",
    )
    reporter.check(
        "AFFINE_SENSITIVITY_PERSISTS",
        sp.simplify(positive_numerator - positive_certificate) == 0
        and positive_certificate.is_positive is True
        and sp.simplify(persisted - expected_persisted) == 0,
        "response=d[2(d^2+q^2)+dq]/[2(d^2+q^2)] is nonzero",
    )


def main() -> int:
    reporter = Reporter()
    try:
        b170 = importlib.import_module(BLOCK170_MODULE)
        reporter.check(
            "BLOCK170_IMPORT",
            Path(b170.__file__).resolve() == BLOCK170_PATH.resolve(),
            str(Path(b170.__file__).resolve()),
        )

        fixtures = tuple(b170.PRIMARY)
        reporter.check(
            "BLOCK170_FIXTURES",
            fixtures == (("8x4", 8, 4), ("12x4", 12, 4)),
            f"PRIMARY={fixtures}",
        )
        reconstructions = [reconstruct_fixture(b170, fixture)
                           for fixture in fixtures]
        for reconstruction in reconstructions:
            check_fixture(reconstruction, b170.ST, reporter)

        reporter.check(
            "CROSS_EXTENT_COMPRESSION",
            matrix_equal(reconstructions[0]["compression"],
                         reconstructions[1]["compression"]),
            "8x4 and 12x4 give the same exact rank-2 affine compression",
        )
        check_affine_admixture_lemma(reporter)
    except Exception as exc:  # fail closed and preserve a final TOTAL line
        reporter.check(
            "UNCAUGHT_EXCEPTION",
            False,
            f"{type(exc).__name__}: {exc}",
        )

    reporter.total()
    return 1 if reporter.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
