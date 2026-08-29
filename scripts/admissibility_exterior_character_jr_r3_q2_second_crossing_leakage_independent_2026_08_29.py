#!/usr/bin/env python3
"""Independent representation-ring check of the added-action residual.

This checker does not import the original-link Brauer runner.  It reconstructs
the physical conditional-Haar subtraction from exact O(3) representation-ring
arithmetic at fixed coarse delta0 and evaluates a separate one-variable Haar
selection rule for every proper fine-plaquette product.
"""

from __future__ import annotations


AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_SECOND_CROSSING_ACTION_LEAKAGE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_SIX_HISTORY_GRAM_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

V = (1, -1)  # (spin, inversion parity)
TRIVIAL = (0, 1)
V_SQUARED = {(0, 1): 1, (1, 1): 1, (2, 1): 1}
OLD_LOCAL_ALPHABET = {(0, 1), (1, -1)}
RESIDUAL = {(1, 1): 1, (2, 1): 1}
V_RING = {V: 1}
PROPER = (
    frozenset((0,)),
    frozenset((1,)),
    frozenset((2,)),
    frozenset((0, 1)),
    frozenset((0, 2)),
    frozenset((1, 2)),
)


def physical_residual():
    result = dict(V_SQUARED)
    result[TRIVIAL] -= 1
    return {irrep: multiplicity for irrep, multiplicity in result.items()
            if multiplicity}


def tensor_product(left, right):
    """Exact O(3) Clebsch--Gordan product with inversion parity."""
    result = {}
    for (spin_a, parity_a), multiplicity_a in left.items():
        for (spin_b, parity_b), multiplicity_b in right.items():
            for spin in range(abs(spin_a - spin_b), spin_a + spin_b + 1):
                irrep = (spin, parity_a * parity_b)
                result[irrep] = result.get(irrep, 0) + multiplicity_a * multiplicity_b
    return result


def tensor_factors(factors):
    result = {TRIVIAL: 1}
    for factor in factors:
        result = tensor_product(result, factor)
    return result


def conditional_zero_reductions():
    """Evaluate the six one-variable Haar trivial-multiplicity tests.

    With W2=delta0 W0^-1 W1^-1, Haar invariance lets a single W2 vector
    character be integrated as a single V factor in W1.  In the two remaining
    cases the W0-dependent factors are r=(1,+)+(2,+) and V=(1,-).  The integral
    is the trivial-irrep multiplicity of the displayed factor product.
    """
    routes = {
        frozenset((0,)): ("W0", (RESIDUAL, V_RING)),
        frozenset((1,)): ("W0", (RESIDUAL,)),
        frozenset((2,)): ("W1", (V_RING,)),
        frozenset((0, 1)): ("W1", (V_RING,)),
        frozenset((0, 2)): ("W1", (V_RING,)),
        frozenset((1, 2)): ("W0", (RESIDUAL, V_RING)),
    }
    return {
        sector: {
            "integrated_variable": variable,
            "decomposition": tensor_factors(factors),
            "trivial_multiplicity": tensor_factors(factors).get(TRIVIAL, 0),
        }
        for sector, (variable, factors) in routes.items()
    }


def run_checks():
    residual = physical_residual()
    reductions = conditional_zero_reductions()
    checks = [
        ("dimension identity 3x3=1+3+5", 3 * 3 == 1 + 3 + 5),
        ("two defining vectors have even inversion parity", V[1] * V[1] == 1),
        ("physical Q removes exactly the trivial component", residual == RESIDUAL),
        ("residual character norm is exactly two",
         sum(multiplicity * multiplicity for multiplicity in residual.values()) == 2),
        ("new irreps are disjoint from the old local scalar/vector alphabet",
         set(residual).isdisjoint(OLD_LOCAL_ALPHABET)),
        ("all six proper products are evaluated", set(reductions) == set(PROPER)),
    ]
    for sector in PROPER:
        checks.append((
            f"conditional Haar trivial multiplicity vanishes for {sorted(sector)}",
            reductions[sector]["trivial_multiplicity"] == 0,
        ))
    return residual, reductions, checks


def all_checks_pass():
    return all(passed for _label, passed in run_checks()[2])


def main() -> int:
    residual, reductions, checks = run_checks()
    failures = 0
    print("residual_irreps", residual)
    print("conditional_reductions", reductions)
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(checks)-failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
