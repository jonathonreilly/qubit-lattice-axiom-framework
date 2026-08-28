#!/usr/bin/env python3
"""Independent exact reconstruction for the exterior-character action block.

This checker deliberately does not import the primary runner.  It reconstructs
the character from principal minors, differentiates explicit one-parameter
families, and uses a two-state convolution model for the transfer sign and
injectivity controls.
"""

from __future__ import annotations

import sympy as sp


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_EXTERIOR_CHARACTER_ACTION_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_PLAQUETTE_HOLONOMY_CONNECTION_CURVATURE_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
)


def principal_minor_character(matrix: sp.MatrixBase) -> sp.Expr:
    """Trace on the full exterior algebra, reconstructed without a lift."""
    degree_two = sum(
        matrix.extract((i, j), (i, j)).det()
        for i, j in ((0, 1), (0, 2), (1, 2))
    )
    return sp.expand(1 + sp.trace(matrix) + degree_two + matrix.det())


def rotation_z(cosine: sp.Expr, sine: sp.Expr) -> sp.Matrix:
    return sp.Matrix(((cosine, -sine, 0),
                      (sine, cosine, 0),
                      (0, 0, 1)))


def independent_facts() -> dict[str, bool]:
    entries = sp.symbols("m00:03 m10:13 m20:23")
    generic = sp.Matrix(3, 3, entries)
    character_identity = sp.expand(
        principal_minor_character(generic) - (sp.eye(3) + generic).det()
    ) == 0

    proper = rotation_z(sp.Rational(3, 5), sp.Rational(4, 5))
    improper = sp.diag(1, 1, -1) * proper
    proper_q = sp.expand(16 - 2 * principal_minor_character(proper))
    improper_q = sp.expand(16 - 2 * principal_minor_character(improper))

    theta = sp.symbols("theta", real=True)
    q_theta = 8 * (1 - sp.cos(theta))
    flat_second_derivative = sp.diff(q_theta, theta, 2).subs(theta, 0)
    improper_path = sp.diag(1, 1, -1) * rotation_z(
        sp.cos(theta), sp.sin(theta)
    )
    improper_path_q = sp.simplify(
        16
        - principal_minor_character(improper_path)
        - principal_minor_character(improper_path.inv())
    )

    # Positive- and inverse-occurrence link variations, reconstructed directly.
    left = rotation_z(sp.Rational(5, 13), sp.Rational(12, 13))
    link = sp.Matrix(((1, 0, 0),
                      (0, sp.Rational(7, 25), -sp.Rational(24, 25)),
                      (0, sp.Rational(24, 25), sp.Rational(7, 25))))
    right = sp.Matrix(((sp.Rational(3, 5), 0, sp.Rational(4, 5)),
                       (0, 1, 0),
                       (-sp.Rational(4, 5), 0, sp.Rational(3, 5))))
    generator = sp.Matrix(((0, -1, 0), (1, 0, 0), (0, 0, 0)))
    # Left variation link(t)=exp(tX) link, matching the source-note convention.
    direct_positive = sp.trace(left * generator * link * right)
    cyclic_positive = sp.trace(generator * link * right * left)
    direct_inverse = -sp.trace(left * link.inv() * generator * right)
    cyclic_inverse = -sp.trace(generator * right * left * link.inv())

    # Exact two-history controls.  kappa=log(2)/16 gives exp(-16*kappa)=1/2.
    positive_transfer = sp.Matrix(((1, sp.Rational(1, 2)),
                                   (sp.Rational(1, 2), 1)))
    normalized_transfer = sp.Rational(2, 3) * positive_transfer
    negative_transfer = sp.Matrix(((1, 2), (2, 1)))
    zero_transfer = sp.ones(2)

    a, q = sp.symbols("a q", positive=True)
    nonlinear = (1 - sp.exp(-a * q)) / a
    cosine = sp.Rational(3, 5)
    sine = sp.Rational(4, 5)
    finite_q_one = 8 * (1 - cosine)
    finite_q_two = 8 * (1 + cosine)
    finite_nonlinear_residual = sp.simplify(
        (1 - finite_q_one / 16) * sine
        - (1 - finite_q_two / 16) * sine
    )

    return {
        "generic exterior character equals det(I+W)": character_identity,
        "proper rational rotation has Wilson-form Q": (
            proper_q == 4 * (3 - sp.trace(proper)) == sp.Rational(16, 5)
        ),
        "improper rational family representative has Q=16": improper_q == 16,
        "improper tangent family has zero force and stiffness": (
            improper_path_q == 16
            and sp.diff(improper_path_q, theta) == 0
            and sp.diff(improper_path_q, theta, 2) == 0
        ),
        "flat one-plaquette Hessian coefficient is eight": (
            flat_second_derivative == 8
        ),
        "positive and inverse link variations have the stated cyclic form": (
            sp.simplify(direct_positive - cyclic_positive) == 0
            and sp.simplify(direct_inverse - cyclic_inverse) == 0
        ),
        "positive-sign two-history transfer is positive and injective": (
            positive_transfer.det() == sp.Rational(3, 4)
            and positive_transfer.is_positive_definite
        ),
        "normalized transfer has exact Hamiltonian levels zero and log(3)": (
            normalized_transfer.eigenvals() == {sp.Integer(1): 1,
                                                sp.Rational(1, 3): 1}
        ),
        "negative-sign Gram has an exact negative eigenvalue": (
            negative_transfer.eigenvals() == {sp.Integer(3): 1,
                                              sp.Integer(-1): 1}
        ),
        "zero-coupling two-history transfer is noninjective": (
            zero_transfer.det() == 0 and zero_transfer.rank() == 1
        ),
        "nonlinear action family keeps unit flat slope": (
            sp.simplify(sp.diff(nonlinear, q).subs(q, 0) - 1) == 0
            and sp.simplify(sp.diff(nonlinear, q, 2).subs(q, 0) + a) == 0
        ),
        "same flat slope does not preserve finite-curvature stationarity": (
            finite_q_one == sp.Rational(16, 5)
            and finite_q_two == sp.Rational(64, 5)
            and finite_nonlinear_residual == sp.Rational(12, 25)
        ),
    }


def main() -> int:
    facts = independent_facts()
    passed = 0
    failed = 0
    for name, condition in facts.items():
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        passed += int(ok)
        failed += int(not ok)
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
