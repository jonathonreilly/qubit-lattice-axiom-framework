#!/usr/bin/env python3
"""Clifford-gamma versus lattice-species-corner decoupling.

This runner checks a narrow algebra/counting distinction:

* adjoining a fourth Clifford gamma changes the spinor algebra from the
  2-component Pauli/Weyl representation to a 4-component Dirac representation
  with a balanced gamma_5 grading;
* adding a fourth discrete lattice direction changes the naive lattice species
  count from 2^3=8 to 2^4=16; and
* those are different mathematical objects.

It does not prove that emergent time supplies a gamma, build a massive field,
derive partner chirality as a physical degree of freedom, or close any magnitude
wall. It only prevents the missing fourth lattice corner from being confused
with the retained Cl(3,1) gamma algebra.
"""

from __future__ import annotations

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(ok))
    FAIL += int(not ok)
    return bool(ok)


def block(A: np.ndarray, B: np.ndarray, C: np.ndarray, D: np.ndarray) -> np.ndarray:
    return np.block([[A, B], [C, D]])


def naive_species_count(discrete_lattice_dims: int) -> int:
    return 2 ** discrete_lattice_dims


def main() -> int:
    print("CLIFFORD GAMMA / LATTICE SPECIES-CORNER DECOUPLING")
    print("=" * 72)

    pauli = [
        np.array([[0, 1], [1, 0]], complex),
        np.array([[0, -1j], [1j, 0]], complex),
        np.array([[1, 0], [0, -1]], complex),
    ]
    check(
        "A Cl(3) Pauli/Weyl spinor representation is 2-component",
        all(s.shape == (2, 2) for s in pauli),
        "three Pauli matrices act on C^2",
    )

    I2 = np.eye(2, dtype=complex)
    Z2 = np.zeros((2, 2), complex)
    gamma0 = block(I2, Z2, Z2, -I2)
    gamma_spatial = [block(Z2, s, -s, Z2) for s in pauli]
    gamma5 = 1j * gamma0 @ gamma_spatial[0] @ gamma_spatial[1] @ gamma_spatial[2]
    check(
        "A adjoining the fourth Clifford gamma gives a 4-component Dirac algebra",
        gamma0.shape == (4, 4)
        and all(g.shape == (4, 4) for g in gamma_spatial)
        and np.allclose(gamma5 @ gamma5, np.eye(4))
        and abs(np.trace(gamma5)) < 1e-12,
        "spinor algebra dimension doubles 2 -> 4 and gamma5 is balanced",
    )

    zeros_one_direction = np.array([0.0, np.pi])
    check(
        "B one discrete naive-lattice direction has two doubler zeros",
        np.allclose(np.sin(zeros_one_direction), 0) and len(zeros_one_direction) == 2,
        "sin(k)=0 at k=0 and k=pi",
    )
    check(
        "B three spatial lattice directions give eight naive species corners",
        naive_species_count(3) == 8,
        "2^3=8",
    )
    check(
        "B a fourth discrete lattice direction would give sixteen species corners",
        naive_species_count(4) == 16,
        "2^4=16",
    )

    spinor_dim_after_gamma = gamma0.shape[0]
    species_after_four_lattice_dims = naive_species_count(4)
    check(
        "DISTINCT gamma extension and species-corner extension are different counts",
        spinor_dim_after_gamma == 4 and species_after_four_lattice_dims == 16,
        "Clifford spinor dimension 4 is not lattice species count 16",
    )
    check(
        "DISTINCT a gamma matrix is not a momentum-space corner",
        gamma0.shape == (4, 4) and zeros_one_direction.shape == (2,),
        "matrix generator versus zeros of sin(k)",
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: the fourth Clifford gamma / Dirac spinor doubling and the fourth discrete "
        "lattice species-corner doubling are distinct structures. A missing k4 lattice corner "
        "does not by itself block use of the retained Cl(3,1) gamma algebra, but this runner "
        "does not prove that emergent time supplies the gamma or that any massive field is built."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
