#!/usr/bin/env python3
"""Exact finite-mode checks for the second-quantization log bridge."""

import itertools

import sympy as sp


EXPECTED_LABELS = [
    "exterior-functor-multiplicativity",
    "canonical-creation-intertwiner",
    "positive-log-realization",
    "trace-determinant-identity",
    "logarithmic-generator-identity",
    "channel-direct-sum-factorization",
    "free-corner-three-channel-composition",
    "counterfeit-functor-rejection",
    "singular-log-boundary",
]


class CheckRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.labels = []

    def check(self, label, condition, detail):
        self.labels.append(label)
        if bool(condition):
            self.passed += 1
            print(f"PASS: {label} {detail}")
        else:
            self.failed += 1
            print(f"FAIL: {label} {detail}")

    def finish(self):
        if self.labels != EXPECTED_LABELS:
            self.failed += 1
            print("FAIL: descriptive-label-manifest")
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


def block_diag(*blocks):
    return sp.diag(*blocks)


def gamma_two(A):
    """Exterior action on (vacuum, e1, e2, e1 wedge e2)."""
    return block_diag(sp.ones(1, 1), A, sp.Matrix([[sp.det(A)]]))


def dgamma_two(X):
    """Infinitesimal exterior action in the same ordered basis."""
    return block_diag(sp.zeros(1, 1), X, sp.Matrix([[sp.trace(X)]]))


def creation_two(f):
    """Exterior multiplication by f in the ordered two-mode basis."""
    out = sp.zeros(4, 4)
    out[1, 0] = f[0]
    out[2, 0] = f[1]
    out[3, 1] = -f[1]
    out[3, 2] = f[0]
    return out


def diagonal_gamma_values(values):
    """Occupation eigenvalues in lexicographic bit order."""
    out = []
    for occupation in itertools.product((0, 1), repeat=len(values)):
        value = sp.Integer(1)
        for bit, eigenvalue in zip(occupation, values):
            if bit:
                value *= eigenvalue
        out.append(sp.simplify(value))
    return out


def main():
    checks = CheckRunner()

    # The exterior functor is multiplicative even for noncommuting maps.
    A = sp.Matrix([[2, 1], [0, 1]])
    B = sp.Matrix([[1, 0], [1, 2]])
    checks.check(
        "exterior-functor-multiplicativity",
        A * B != B * A
        and gamma_two(A) * gamma_two(B) == gamma_two(A * B),
        "Gamma(A)Gamma(B)=Gamma(AB) for a noncommuting invertible pair",
    )

    # The canonical creation intertwiner, including a complex vector.
    f = sp.Matrix([1 + sp.I, 2 - sp.I])
    vacuum = sp.Matrix([1, 0, 0, 0])
    gamma_A = gamma_two(A)
    checks.check(
        "canonical-creation-intertwiner",
        gamma_A * creation_two(f) == creation_two(A * f) * gamma_A
        and gamma_A * vacuum == vacuum,
        "vacuum fixing and Gamma(A)a^dag(f)=a^dag(Af)Gamma(A)",
    )

    # A non-diagonal positive matrix with exact spectral data.
    rotation = sp.Rational(1, 5) * sp.Matrix([[3, -4], [4, 3]])
    eigenvalues = sp.diag(sp.Rational(1, 4), sp.Integer(8))
    t = sp.simplify(rotation * eigenvalues * rotation.T)
    log_t = sp.simplify(
        rotation * sp.diag(-sp.log(4), sp.log(8)) * rotation.T
    )
    exp_dgamma_log = sp.simplify(sp.exp(dgamma_two(log_t)))
    checks.check(
        "positive-log-realization",
        sp.det(t) == 2
        and exp_dgamma_log == gamma_two(t)
        and dgamma_two(log_t)
        == block_diag(sp.zeros(1, 1), log_t, sp.Matrix([[sp.log(2)]])),
        "Gamma(t)=exp(dGamma(log t)) on a rotated positive spectrum",
    )

    # The trace identity also detects the determinant sector for a nonnormal map.
    nonnormal = sp.Matrix([[2, 1], [0, 3]])
    checks.check(
        "trace-determinant-identity",
        sp.trace(gamma_two(nonnormal)) == (sp.eye(2) + nonnormal).det()
        and sp.trace(gamma_two(nonnormal)) == 12,
        "Tr Gamma(A)=det(1+A)=12 for a nonnormal matrix",
    )

    # The principal logarithm identity and free dimensionless generator.
    E1, E2 = sp.symbols("E1 E2", positive=True)
    energy = sp.diag(E1, E2)
    transfer = sp.diag(sp.exp(-2 * E1), sp.exp(-2 * E2))
    gamma_transfer = gamma_two(transfer)
    minus_log_gamma = sp.diag(0, 2 * E1, 2 * E2, 2 * (E1 + E2))
    checks.check(
        "logarithmic-generator-identity",
        sp.simplify(minus_log_gamma / 2 - dgamma_two(energy))
        == sp.zeros(4, 4)
        and sp.simplify(
            gamma_transfer
            - sp.diag(
                1,
                sp.exp(-2 * E1),
                sp.exp(-2 * E2),
                sp.exp(-2 * (E1 + E2)),
            )
        )
        == sp.zeros(4, 4),
        "-log Gamma(exp(-2E))/2=dGamma(E)",
    )

    # Direct sums become tensor products under the canonical Fock identification.
    x, y = sp.symbols("x y", positive=True)
    direct_values = diagonal_gamma_values((x, y))
    tensor_values = [1, y, x, x * y]
    checks.check(
        "channel-direct-sum-factorization",
        direct_values == tensor_values
        and sp.simplify(sum(direct_values) - (1 + x) * (1 + y)) == 0,
        "Gamma(x direct-sum y)=Gamma(x) tensor Gamma(y)",
    )

    # Three supplied free channels: t_k=exp(-2E_k).
    E3 = sp.symbols("E3", positive=True)
    energies = (E1, E2, E3)
    transfers = tuple(sp.exp(-2 * e) for e in energies)
    gamma_values = diagonal_gamma_values(transfers)
    log_energies = []
    for occupation in itertools.product((0, 1), repeat=3):
        log_energies.append(
            sp.simplify(sum(bit * e for bit, e in zip(occupation, energies)))
        )
    recovered = [
        sp.simplify(-sp.log(value) / 2) for value in gamma_values
    ]
    checks.check(
        "free-corner-three-channel-composition",
        recovered == log_energies
        and sp.simplify(sum(gamma_values) - sp.prod(1 + t_k for t_k in transfers))
        == 0,
        "three-channel tensor log is the sum of occupation energies",
    )

    # Conjugation inside the two-particle sector preserves trace and products
    # but does not preserve the standard dGamma(log t) identification.
    spectrum = (sp.Integer(2), sp.Integer(3), sp.Integer(5))
    standard = diagonal_gamma_values(spectrum)
    occupations = list(itertools.product((0, 1), repeat=3))
    i_110 = occupations.index((1, 1, 0))
    i_101 = occupations.index((1, 0, 1))
    permutation = list(range(8))
    permutation[i_110], permutation[i_101] = permutation[i_101], permutation[i_110]
    counterfeit = [standard[j] for j in permutation]
    second_spectrum = (sp.Integer(7), sp.Integer(11), sp.Integer(13))
    standard_second = diagonal_gamma_values(second_spectrum)
    counterfeit_second = [standard_second[j] for j in permutation]
    product_standard = diagonal_gamma_values(
        tuple(a * b for a, b in zip(spectrum, second_spectrum))
    )
    counterfeit_product = [product_standard[j] for j in permutation]
    checks.check(
        "counterfeit-functor-rejection",
        sum(counterfeit) == sum(standard) == 72
        and all(v > 0 for v in counterfeit)
        and [a * b for a, b in zip(counterfeit, counterfeit_second)]
        == counterfeit_product
        and counterfeit[i_110] == 10
        and standard[i_110] == 6,
        "trace and multiplication survive a sector swap while standard dGamma does not",
    )

    # Exterior action survives a zero mode, but the bounded logarithm does not.
    singular = sp.diag(1, 0)
    checks.check(
        "singular-log-boundary",
        sp.det(gamma_two(singular)) == 0
        and sp.trace(gamma_two(singular)) == (sp.eye(2) + singular).det()
        and 0 in gamma_two(singular).eigenvals(),
        "Gamma(t) and its trace remain defined but log Gamma(t) is singular",
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
