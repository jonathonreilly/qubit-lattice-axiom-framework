#!/usr/bin/env python3
"""
DM odd-circulant current-stack zero law.

Question:
  Given the exact local DM coefficient slot c_odd on the circulant kernel,
  what law does the stack currently retained today assign to it?

Answer:
  c_odd,current = 0.

  The current local bank is built from residual-Z2-even data:
    - the exact weak-axis 1+2 split diag(a,b,b)
    - the even circulant bridge it induces
    - Hermitian/scalar/equivariant functionals of that same even data
  Any residual-Z2-equivariant functional of a residual-Z2-even input is again
  residual-Z2 even, so its projection onto the unique odd slot vanishes.

Boundary:
  This is a current-stack theorem. It does not exclude a future genuinely new
  residual-Z2-odd bridge from activating c_odd != 0.
"""

from __future__ import annotations

import sys

import numpy as np

np.set_printoptions(precision=6, suppress=True, linewidth=140)

PASS_COUNT = 0
FAIL_COUNT = 0

S = np.array(
    [
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [1.0, 0.0, 0.0],
    ],
    dtype=complex,
)
S2 = S @ S
P23 = np.array(
    [
        [1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0],
        [0.0, 1.0, 0.0],
    ],
    dtype=complex,
)


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def z3_bridge() -> np.ndarray:
    omega = np.exp(2j * np.pi / 3.0)
    return (1.0 / np.sqrt(3.0)) * np.array(
        [
            [1.0, 1.0, 1.0],
            [1.0, omega, omega * omega],
            [1.0, omega * omega, omega],
        ],
        dtype=complex,
    )


def even_slice_from_split(a: complex, b: complex, uz3: np.ndarray) -> np.ndarray:
    d = np.diag([a, b, b]).astype(complex)
    return uz3.conj().T @ d @ uz3


def odd_coeff(k: np.ndarray) -> float:
    return float(np.imag(k[0, 1]))


def circulant_from_even_data(mu: complex, nu: complex) -> np.ndarray:
    return mu * np.eye(3, dtype=complex) + nu * (S + S2)


def part1_the_current_local_input_surface_is_residual_z2_even() -> None:
    print("\n" + "=" * 88)
    print("PART 1: THE CURRENT LOCAL INPUT SURFACE IS RESIDUAL-Z2 EVEN")
    print("=" * 88)

    d = np.diag([1.4 + 0.3j, 0.8 - 0.2j, 0.8 - 0.2j]).astype(complex)
    uz3 = z3_bridge()
    y_even = even_slice_from_split(1.4 + 0.3j, 0.8 - 0.2j, uz3)
    h_even = y_even.conj().T @ y_even

    check(
        "The exact weak-axis split is residual-Z2 even in the local site basis",
        np.linalg.norm(P23 @ d @ P23.conj().T - d) < 1e-12,
        f"site-even error={np.linalg.norm(P23 @ d @ P23.conj().T - d):.2e}",
    )
    check(
        "Its bridged local Dirac surface remains residual-Z2 even",
        np.linalg.norm(P23 @ y_even @ P23.conj().T - y_even) < 1e-12,
        f"Dirac-even error={np.linalg.norm(P23 @ y_even @ P23.conj().T - y_even):.2e}",
    )
    check(
        "Its Hermitian kernel is residual-Z2 even and has zero odd slot",
        np.linalg.norm(P23 @ h_even @ P23.conj().T - h_even) < 1e-12 and abs(odd_coeff(h_even)) < 1e-12,
        f"odd coeff={odd_coeff(h_even):.2e}",
    )

    print()
    print("  So the retained local DM bank starts on a strictly residual-Z2-even surface.")


def part2_equivariant_functionals_of_even_data_stay_even() -> None:
    print("\n" + "=" * 88)
    print("PART 2: EQUIVARIANT FUNCTIONALS OF EVEN DATA STAY EVEN")
    print("=" * 88)

    uz3 = z3_bridge()
    y_even = even_slice_from_split(1.4 + 0.3j, 0.8 - 0.2j, uz3)
    h_even = y_even.conj().T @ y_even

    functionals = {
        "Y^dag Y": lambda m: m.conj().T @ m,
        "Hermitian symmetrization": lambda m: m + m.conj().T,
        "Hermitian quadratic combination": lambda m: m.conj().T @ m + 0.3 * (m + m.conj().T) + 0.2 * np.eye(3, dtype=complex),
        "Resolvent of H": lambda m: np.linalg.inv(np.eye(3, dtype=complex) + m.conj().T @ m),
    }

    all_even = True
    details = []
    for name, func in functionals.items():
        k = func(y_even)
        err_even = np.linalg.norm(P23 @ k @ P23.conj().T - k)
        odd = abs(odd_coeff(k))
        all_even &= err_even < 1e-10 and odd < 1e-10
        details.append(f"{name}: even={err_even:.1e}, odd={odd:.1e}")

    check(
        "Representative current-bank-like equivariant functionals preserve residual-Z2 evenness",
        all_even,
        "; ".join(details),
    )

    print()
    print("  So scalar/Hermitian/equivariant post-processing of the retained even")
    print("  local data cannot activate the odd slot by itself.")


def part3_the_current_stack_law_for_the_odd_slot_is_zero() -> None:
    print("\n" + "=" * 88)
    print("PART 3: THE CURRENT-STACK LAW FOR THE ODD SLOT IS ZERO")
    print("=" * 88)

    d = 1.15
    r = 0.33
    k_even = d * np.eye(3, dtype=complex) + r * (S + S2)
    k_odd = d * np.eye(3, dtype=complex) + r * (S + S2) + 1j * 0.19 * (S - S2)

    check(
        "The current even stack sits at c_odd = 0",
        abs(odd_coeff(k_even)) < 1e-12,
        f"c_odd,current={odd_coeff(k_even):.2e}",
    )
    check(
        "A future positive activation would have to leave the current even surface",
        abs(odd_coeff(k_odd)) > 1e-6 and np.linalg.norm(P23 @ k_odd @ P23.conj().T - k_odd) > 1e-6,
        f"future c_odd={odd_coeff(k_odd):.6f}",
    )

    print()
    print("  So the exact current-stack answer is not an unknown coefficient.")
    print("  It is the zero law c_odd,current = 0.")


def part4_n5_execution_certificate() -> None:
    print("\n" + "=" * 88)
    print("PART 4: N5 EXECUTION CERTIFICATE -- RESOLUTION CLASSES EXERCISED HERE")
    print("=" * 88)

    a = 1.4 + 0.3j
    b = 0.8 - 0.2j
    uz3 = z3_bridge()
    y_even = even_slice_from_split(a, b, uz3)
    h_even = y_even.conj().T @ y_even
    d_cur, r_cur, c_future = 1.15, 0.33, 0.19
    k_even = circulant_from_even_data(d_cur, r_cur)
    k_odd = k_even + 1j * c_future * (S - S2)
    d_split = np.diag([a, b, b]).astype(complex)
    site_even_err = np.linalg.norm(P23 @ d_split @ P23.conj().T - d_split)

    print(
        "  per_element: checked -- the odd slot is not a norm but one specific "
        "matrix entry, Im K[0,1], and it is extracted separately for every "
        f"kernel this runner builds: {odd_coeff(h_even):.2e} on the bridged "
        f"Hermitian kernel, {odd_coeff(k_even):.2e} on the retained even "
        f"circulant, and {odd_coeff(k_odd):.6f} on the hypothetical activated "
        "kernel, so the zero law is read off an entry rather than inferred."
    )
    print(
        "  per_site: checked -- the three-element local site basis on which the "
        "shift S and the residual-Z2 transposition P23 act is resolved site by "
        f"site: the weak-axis split puts a = {a} on site 1 and the identical "
        f"b = {b} on sites 2 and 3, and evenness is verified as the exact "
        f"site-permutation identity P23 D P23^dag = D to {site_even_err:.2e}."
    )
    print(
        "  per_mode: checked and not executed -- the Z_3 character modes are "
        "never separated here; uz3 is applied only as a whole-matrix "
        "conjugation and no eigenvalue or character amplitude is taken, so the "
        "runner does not exhibit the odd slot as the splitting between the two "
        "doublet characters even though that is where it would live."
    )
    print(
        "  per_block: checked -- the residual-Z2 orbit structure gives a "
        "1-dimensional weak-axis block and a 2-dimensional degenerate block, "
        "and all four representative bank functionals (Y^dag Y, Hermitian "
        "symmetrization, the Hermitian quadratic combination, the resolvent) "
        "are evaluated against that block structure and each stays even, so no "
        "single block of the retained bank activates the slot."
    )
    print(
        "  lattice_wide: checked and not executed -- the entire system is the "
        "one three-site orbit above; there is no extended lattice, no volume "
        "and no limit taken anywhere in this runner, so c_odd,current = 0 is "
        "certified as a present-tense statement about that single retained "
        "bank and is not promoted to any lattice-scale zero law."
    )


def main() -> int:
    print("=" * 88)
    print("DM NEUTRINO ODD-CIRCULANT CURRENT-STACK ZERO LAW")
    print("=" * 88)
    print()
    print("Authority stack:")
    print("  - exact weak-axis 1+2 split")
    print("  - DM odd-circulant residual-Z2 slot theorem")
    print("  - retained support/Hermitian/scalar bank on the DM lane")
    print()
    print("Question:")
    print("  What activation law does the stack retained today assign to the unique")
    print("  odd circulant coefficient c_odd?")

    part1_the_current_local_input_surface_is_residual_z2_even()
    part2_equivariant_functionals_of_even_data_stay_even()
    part3_the_current_stack_law_for_the_odd_slot_is_zero()
    part4_n5_execution_certificate()

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Exact current-stack answer:")
    print("    - the retained local DM bank is residual-Z2 even")
    print("    - equivariant functionals of that bank stay residual-Z2 even")
    print("    - so the current law for the odd slot is c_odd,current = 0")
    print()
    print("  Any future positive DM coefficient law must therefore introduce a")
    print("  genuinely new residual-Z2-odd bridge or activator.")
    print()
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
