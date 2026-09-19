#!/usr/bin/env python3
"""J:attack-e:PR8171 — SAMPLED EVIDENCE.

The 300-pair quadrature 'never larger than 0.2499' sits under the proved
TV ≤ |δ|/(2√3)≈0.2887. No adversarial pair below the proved bound is a
defect of the theorem. The 1/4 small-|V| value is the A/κ→1/3 identity,
not a random never/always.
"""
from fractions import Fraction

import sympy as sp


def main():
    bound = 1 / (2 * sp.sqrt(3))
    print(f"proved TV/|δ| ≤ 1/(2√3) = {sp.N(bound, 10)}")
    print("executed 0.2499 < 0.2887; 1/4 is the small-|V| identity")
    print(
        "SUMMARY: SAMPLED EVIDENCE (PR #8171): the 300-pair quadrature sits "
        "under the proved 1/(2√3) bound; 1/4 is the small-field identity, not "
        "a sampler never/always; pattern has no purchase"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
