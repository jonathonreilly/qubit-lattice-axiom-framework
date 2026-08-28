#!/usr/bin/env python3
"""Independent exact checks for the Haar-compressed generated crossing."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product


AUDIT_TIMEOUT_SEC = 120


Permutation = tuple[int, int, int]


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[i]] for i in range(3))


def inverse(value: Permutation) -> Permutation:
    result = [0, 0, 0]
    for i, image in enumerate(value):
        result[image] = i
    return tuple(result)


def parity(value: Permutation) -> int:
    inversions = sum(value[i] > value[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


def cycle_class(value: Permutation) -> str:
    if value == (0, 1, 2):
        return "e"
    return "t" if parity(value) == -1 else "c"


def character(name: str, value: Permutation) -> int:
    kind = cycle_class(value)
    table = {
        "triv": {"e": 1, "t": 1, "c": 1},
        "sign": {"e": 1, "t": -1, "c": 1},
        "std": {"e": 2, "t": 0, "c": -1},
    }
    return table[name][kind]


def fourier_scalar(values: dict[Permutation, Fraction], name: str) -> Fraction:
    dimension = {"triv": 1, "sign": 1, "std": 2}[name]
    return sum((values[g] * character(name, g) for g in values), Fraction(0)) / (6 * dimension)


def independent_facts() -> dict[str, object]:
    group = list(permutations(range(3)))
    names = ("triv", "sign", "std")
    dimensions = {"triv": 1, "sign": 1, "std": 2}

    # A normalized positive central crossing and a positive nonconstant half multiplier.
    a_hat = {"triv": Fraction(1), "sign": Fraction(1, 2), "std": Fraction(1, 3)}
    a = {
        g: sum(
            (Fraction(dimensions[name]) * a_hat[name] * character(name, g) for name in names),
            Fraction(0),
        )
        for g in group
    }
    m_by_class = {"e": Fraction(1), "t": Fraction(1, 2), "c": Fraction(1, 3)}
    m = {g: m_by_class[cycle_class(g)] for g in group}
    mu = {name: fourier_scalar(m, name) for name in names}

    # Direct double-Haar fiber integral H(delta)=int m(x')a(x'delta x^-1)m(x).
    h_direct: dict[Permutation, Fraction] = {}
    for delta in group:
        total = Fraction(0)
        for x_prime, x in product(group, repeat=2):
            word = compose(compose(x_prime, delta), inverse(x))
            total += m[x_prime] * a[word] * m[x]
        h_direct[delta] = total / 36
    h_hat = {name: fourier_scalar(h_direct, name) for name in names}
    h_hat_expected = {name: a_hat[name] * mu[name] ** 2 for name in names}

    # Character-ring fusion derived by exact Haar character products.
    fusion: dict[tuple[str, str, str], int] = {}
    for rho, lam, sigma in product(names, repeat=3):
        multiplicity = sum(
            character(rho, g) * character(lam, g) * character(sigma, g)
            for g in group
        ) // 6
        fusion[(rho, lam, sigma)] = multiplicity

    k_point = {g: a[g] * h_direct[g] for g in group}
    k_hat = {name: fourier_scalar(k_point, name) for name in names}
    k_hat_fusion = {}
    for sigma in names:
        total = Fraction(0)
        for rho, lam in product(names, repeat=2):
            total += (
                dimensions[rho]
                * dimensions[lam]
                * fusion[(rho, lam, sigma)]
                * a_hat[rho]
                * a_hat[lam]
                * mu[lam] ** 2
            )
        k_hat_fusion[sigma] = total / dimensions[sigma]

    z = k_hat["triv"]
    p_hat = {name: k_hat[name] / z for name in names}

    # Exact Z2 quotient control.
    z2 = (1, -1)
    a_z2 = {s: Fraction(1) + Fraction(1, 2) * s for s in z2}
    m_z2 = {1: Fraction(1), -1: Fraction(1, 2)}
    h_z2 = {}
    for delta in z2:
        h_z2[delta] = sum(
            (m_z2[xp] * a_z2[xp * delta * x] * m_z2[x] for xp, x in product(z2, repeat=2)),
            Fraction(0),
        ) / 4
    k_z2 = {s: a_z2[s] * h_z2[s] for s in z2}
    z_z2 = sum(k_z2.values(), Fraction(0)) / 2
    determinant_multiplier = (k_z2[1] - k_z2[-1]) / (2 * z_z2)

    # The n=1 small-beta/kappa coefficient chain, derived from dimensions.
    q_coefficients = {"triv": 14, "sign": -2, "std_minus": -2, "std_plus": -2}
    mu_linear = {
        "triv": Fraction(-q_coefficients["triv"], 2),
        "sign": Fraction(-q_coefficients["sign"], 2),
        "std_minus": Fraction(-q_coefficients["std_minus"], 2 * 3),
        "std_plus": Fraction(-q_coefficients["std_plus"], 2 * 3),
    }
    r_det_linear = Fraction(2)
    r_vector_linear = r_det_linear / 3
    a_det_quadratic = r_det_linear**2
    a_vector_quadratic = r_vector_linear**2
    induced_det = mu_linear["sign"] ** 2 * a_det_quadratic
    induced_vector = 3 * mu_linear["std_minus"] ** 2 * a_vector_quadratic

    return {
        "group_size": len(group),
        "a_positive": all(value > 0 for value in a.values()),
        "a_normalized": fourier_scalar(a, "triv") == 1,
        "mu": mu,
        "h_hat": h_hat,
        "h_hat_expected": h_hat_expected,
        "fusion": fusion,
        "k_hat": k_hat,
        "k_hat_fusion": k_hat_fusion,
        "p_hat": p_hat,
        "p_strict": all(value > 0 for value in p_hat.values()),
        "z2_k": k_z2,
        "z2_z": z_z2,
        "z2_det": determinant_multiplier,
        "mu_linear": mu_linear,
        "induced_det": induced_det,
        "induced_vector": induced_vector,
    }


def main() -> int:
    facts = independent_facts()
    checks = (
        ("S3 carrier and positive normalized crossing", facts["group_size"] == 6 and facts["a_positive"] and facts["a_normalized"]),
        ("independent half-action Fourier coefficients", facts["mu"] == {"triv": Fraction(19, 36), "sign": Fraction(1, 36), "std": Fraction(1, 9)}),
        ("double-Haar convolution coefficients", facts["h_hat"] == facts["h_hat_expected"]),
        ("character fusion coefficients", facts["fusion"][("std", "std", "triv")] == 1 and facts["fusion"][("std", "std", "sign")] == 1 and facts["fusion"][("std", "std", "std")] == 1),
        ("pointwise-product fusion formula", facts["k_hat"] == facts["k_hat_fusion"]),
        ("normalized generated crossing is strict", facts["p_hat"]["triv"] == 1 and facts["p_strict"]),
        ("Z2 direct fiber values", facts["z2_k"] == {1: Fraction(57, 64), -1: Fraction(17, 64)}),
        ("Z2 normalization and determinant multiplier", facts["z2_z"] == Fraction(37, 64) and facts["z2_det"] == Fraction(20, 37)),
        ("n=1 half-action feature coefficients", facts["mu_linear"] == {"triv": Fraction(-7), "sign": Fraction(1), "std_minus": Fraction(1, 3), "std_plus": Fraction(1, 3)}),
        ("n=1 induced determinant/vector coefficients", facts["induced_det"] == 4 and facts["induced_vector"] == Fraction(4, 27)),
    )
    failures = 0
    for name, condition in checks:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] independent: {name}")
        failures += int(not ok)
    print(f"TOTAL: PASS={len(checks)-failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
