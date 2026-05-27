#!/usr/bin/env python3
"""Bounded-input assembly certificate for reflection positivity.

This runner verifies only the narrowed support surface for
docs/AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md:
positive staggered determinant factors plus an abstract norm-square/PSD
identity. It does not certify full SU(3) Wilson-gauge reflection positivity,
staggered Grassmann half-action factorization, OS reconstruction, transfer
matrix positivity, or an energy-spectrum theorem.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  {tag} {name}{suffix}")


def staggered_det_factor(mass: float, sigmas: np.ndarray) -> float:
    return float(np.prod(mass * mass + np.asarray(sigmas, dtype=float) ** 2))


def weighted_gram(weights: np.ndarray, vectors: np.ndarray) -> np.ndarray:
    w = np.asarray(weights, dtype=float)
    v = np.asarray(vectors, dtype=float)
    return v.T @ np.diag(w) @ v


def check_source_firewall() -> None:
    text = Path("docs/AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md").read_text(
        encoding="utf-8"
    )
    required = [
        "**Claim type:** bounded_theorem",
        "bounded-input repair 2026-05-27",
        "That is the full binding claim of this repaired row.",
        "does not claim",
        "full finite-lattice reflection positivity",
        "physical transfer matrix",
        "outside the binding claim",
    ]
    for phrase in required:
        check(f"source contains boundary phrase: {phrase}", phrase in text)


def main() -> int:
    print("=" * 88)
    print("REFLECTION POSITIVITY BOUNDED INPUT ASSEMBLY")
    print("Binding scope: determinant positivity + abstract norm-square input")
    print("=" * 88)

    sigma_sets = [
        np.array([0.0, 0.25, 1.0, 1.75]),
        np.array([0.1, 0.4, 0.9]),
        np.array([2.0, 3.0]),
    ]
    for mass in [0.1, 0.5, 1.25]:
        for idx, sigmas in enumerate(sigma_sets):
            det = staggered_det_factor(mass, sigmas)
            check(
                f"staggered determinant product is positive m={mass}, set={idx}",
                det > 0.0,
                f"det_factor={det:.8g}",
            )

    rng = np.random.default_rng(20260527)
    base_vectors = rng.normal(size=(6, 4))
    psi_sq = np.array([0.4, 0.9, 1.1, 0.2, 0.7, 1.3], dtype=float)
    det_weights = np.array(
        [staggered_det_factor(0.3 + 0.1 * i, np.array([0.2, 0.8, 1.4])) for i in range(6)],
        dtype=float,
    )
    norm_weights = psi_sq * psi_sq
    product_weights = det_weights * norm_weights

    check("abstract norm-square weights are non-negative", np.all(norm_weights >= 0.0))
    check("product of determinant and norm-square weights is non-negative", np.all(product_weights >= 0.0))

    gram_norm = weighted_gram(norm_weights, base_vectors)
    gram_product = weighted_gram(product_weights, base_vectors)
    eig_norm = np.linalg.eigvalsh(0.5 * (gram_norm + gram_norm.T))
    eig_product = np.linalg.eigvalsh(0.5 * (gram_product + gram_product.T))
    check("abstract norm-square Gram matrix is PSD", float(eig_norm.min()) >= -1e-12, f"min={eig_norm.min():.3e}")
    check("product-weight Gram matrix is PSD", float(eig_product.min()) >= -1e-12, f"min={eig_product.min():.3e}")

    zero_vecs = np.zeros((6, 2), dtype=float)
    zero_gram = weighted_gram(product_weights, zero_vecs)
    check("null vectors remain null under product weighting", np.linalg.norm(zero_gram) == 0.0)

    check_source_firewall()

    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RUNNER STATUS: FAIL")
        return 1
    print("RUNNER STATUS: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
