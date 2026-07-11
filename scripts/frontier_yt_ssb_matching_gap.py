#!/usr/bin/env python3
"""Verifier for the scoped YT SSB matching-gap arithmetic boundary note.

This runner intentionally checks only the finite-dimensional H_unit
normalization and component overlap. It starts from the unnormalized
equal-weight diagonal direction

    S_D = sum_i E_i = I_D

on an orthonormal contractor basis. It solves the positive unit-norm equation

    1 = ||c S_D||_HS^2 = c^2 D

before checking that

    <alpha_0,a_0 | H_unit | alpha_0,a_0> = 1 / sqrt(N_iso * N_c).

It does not claim to derive the physical Standard Model Yukawa trilinear or to
close the SSB matching gap. The physical matching theorem remains open until
HS/source normalization, SSB VEV division, chirality projection, LSZ/external
state normalization, and absence of extra factors are derived separately.
"""

from __future__ import annotations

import inspect
import math
import sys
from dataclasses import dataclass


PASS_COUNT = 0
FAIL_COUNT = 0
TOL = 1.0e-14


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"

    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


@dataclass(frozen=True)
class PairSpace:
    n_iso: int
    n_c: int

    def __post_init__(self) -> None:
        if self.n_iso <= 0 or self.n_c <= 0:
            raise ValueError("n_iso and n_c must be positive")

    @property
    def dim(self) -> int:
        return self.n_iso * self.n_c

    @property
    def equal_weight_coefficients(self) -> tuple[int, ...]:
        """Coordinates of S_D in the orthonormal contractor basis."""
        return (1,) * self.dim

    @staticmethod
    def hs_norm_squared(
        coefficients: tuple[complex | float | int, ...],
    ) -> float:
        return float(sum(abs(value) ** 2 for value in coefficients))

    @property
    def unnormalized_norm_squared(self) -> float:
        return self.hs_norm_squared(self.equal_weight_coefficients)

    @property
    def positive_unit_coefficient(self) -> float:
        """Solve 1 = c^2 ||S_D||^2 on the positive ray."""
        return 1.0 / math.sqrt(self.unnormalized_norm_squared)

    @property
    def h_unit_coefficients(self) -> tuple[float, ...]:
        coefficient = self.positive_unit_coefficient
        return tuple(
            coefficient * value for value in self.equal_weight_coefficients
        )

    @property
    def h_unit_norm_squared(self) -> float:
        return self.hs_norm_squared(self.h_unit_coefficients)

    def index(self, alpha: int, color: int) -> int:
        if not (1 <= alpha <= self.n_iso):
            raise ValueError(f"alpha={alpha} outside 1..{self.n_iso}")
        if not (1 <= color <= self.n_c):
            raise ValueError(f"color={color} outside 1..{self.n_c}")
        return (alpha - 1) * self.n_c + (color - 1)

    def h_unit_matrix_element(
        self,
        alpha_left: int,
        color_left: int,
        alpha_right: int,
        color_right: int,
    ) -> float:
        left = self.index(alpha_left, color_left)
        right = self.index(alpha_right, color_right)
        if left != right:
            return 0.0
        return self.h_unit_coefficients[left]

    def component_overlap(self, alpha: int, color: int) -> float:
        return self.h_unit_matrix_element(alpha, color, alpha, color)


def close(a: float, b: float) -> bool:
    return abs(a - b) < TOL


def block_1_normalization_derivation() -> PairSpace:
    print("\n=== Block 1: derive the H_unit normalization coefficient ===\n")

    space = PairSpace(n_iso=2, n_c=3)

    check("1.1  N_iso is positive", space.n_iso > 0, f"N_iso={space.n_iso}")
    check("1.2  N_c is positive", space.n_c > 0, f"N_c={space.n_c}")
    check(
        "1.3  D = N_iso * N_c = 6",
        space.dim == 6,
        f"D={space.dim}",
    )
    check(
        "1.4  ||S_D||_HS^2 = D from six unit contractor coordinates",
        close(space.unnormalized_norm_squared, float(space.dim)),
        f"norm_squared={space.unnormalized_norm_squared:.1f}",
    )
    check(
        "1.5  positive unit-norm equation derives c = 1/sqrt(6)",
        close(space.positive_unit_coefficient, 1.0 / math.sqrt(6.0)),
        f"c={space.positive_unit_coefficient:.12f}",
    )
    check(
        "1.6  derived H_unit has Hilbert-Schmidt norm squared 1",
        close(space.h_unit_norm_squared, 1.0),
        f"norm_squared={space.h_unit_norm_squared:.12f}",
    )
    check(
        "1.7  derived coefficient satisfies c^2 D = 1",
        close(space.positive_unit_coefficient**2 * space.dim, 1.0),
        f"c^2 D={space.positive_unit_coefficient**2 * space.dim:.12f}",
    )

    return space


def block_2_matrix_form(space: PairSpace) -> None:
    print("\n=== Block 2: explicit H_unit matrix form ===\n")

    diag = [
        space.h_unit_matrix_element(alpha, color, alpha, color)
        for alpha in range(1, space.n_iso + 1)
        for color in range(1, space.n_c + 1)
    ]
    off_diag = []
    for alpha_l in range(1, space.n_iso + 1):
        for color_l in range(1, space.n_c + 1):
            for alpha_r in range(1, space.n_iso + 1):
                for color_r in range(1, space.n_c + 1):
                    if (alpha_l, color_l) != (alpha_r, color_r):
                        off_diag.append(
                            space.h_unit_matrix_element(
                                alpha_l,
                                color_l,
                                alpha_r,
                                color_r,
                            )
                        )

    expected = 1.0 / math.sqrt(6.0)
    check(
        "2.1  all six diagonal entries equal 1/sqrt(6)",
        all(close(value, expected) for value in diag),
        f"diag entries={[round(value, 12) for value in diag]}",
    )
    check(
        "2.2  all off-diagonal entries vanish",
        all(close(value, 0.0) for value in off_diag),
        f"off-diagonal count={len(off_diag)}",
    )
    check(
        "2.3  trace(H_unit) = sqrt(6)",
        close(sum(diag), math.sqrt(6.0)),
        f"trace={sum(diag):.12f}",
    )


def block_3_component_overlaps(space: PairSpace) -> None:
    print("\n=== Block 3: independently evaluated component overlaps ===\n")

    expected = 1.0 / math.sqrt(6.0)
    overlaps = []
    for alpha in range(1, space.n_iso + 1):
        for color in range(1, space.n_c + 1):
            overlaps.append(space.component_overlap(alpha, color))

    check(
        "3.1  every basis component overlap is 1/sqrt(6)",
        all(close(value, expected) for value in overlaps),
        f"overlaps={[round(value, 12) for value in overlaps]}",
    )

    first_component = space.component_overlap(1, 1)
    last_component = space.component_overlap(space.n_iso, space.n_c)
    check(
        "3.2  distinct first and last components are evaluated separately",
        close(first_component, last_component),
        (
            f"F(1,1)={first_component:.12f}, "
            f"F({space.n_iso},{space.n_c})={last_component:.12f}"
        ),
    )
    check(
        "3.3  both separately evaluated values equal 1/sqrt(6)",
        close(first_component, expected) and close(last_component, expected),
        f"value={first_component:.12f}",
    )


def block_4_general_dimensions() -> None:
    print("\n=== Block 4: general positive-dimension spot checks ===\n")

    alt = PairSpace(n_iso=3, n_c=4)
    alt_expected = 1.0 / math.sqrt(12.0)
    alt_values = [
        alt.component_overlap(alpha, color)
        for alpha in range(1, alt.n_iso + 1)
        for color in range(1, alt.n_c + 1)
    ]
    check(
        "4.1  (N_iso,N_c)=(3,4) gives 1/sqrt(12) on every component",
        all(close(value, alt_expected) for value in alt_values),
        f"value={alt_values[0]:.12f}",
    )

    minimal = PairSpace(n_iso=1, n_c=1)
    check(
        "4.2  (N_iso,N_c)=(1,1) gives component overlap 1",
        close(minimal.component_overlap(1, 1), 1.0),
        f"value={minimal.component_overlap(1, 1):.12f}",
    )


def block_5_falsifiers(space: PairSpace) -> None:
    print("\n=== Block 5: normalization and representative falsifiers ===\n")

    c = space.positive_unit_coefficient
    doubled_norm_squared = (2.0 * c) ** 2 * space.unnormalized_norm_squared
    negative_norm_squared = (-c) ** 2 * space.unnormalized_norm_squared

    check(
        "5.1  doubling c fails the unit-norm equation",
        not close(doubled_norm_squared, 1.0),
        f"||2c S_D||^2={doubled_norm_squared:.1f}",
    )
    check(
        "5.2  sign reversal preserves norm but violates c > 0",
        close(negative_norm_squared, 1.0) and -c < 0.0,
        f"||-c S_D||^2={negative_norm_squared:.1f}, -c={-c:.12f}",
    )

    perturbed = list(space.h_unit_coefficients)
    perturbed[0] *= 2.0
    perturbation_norm = math.sqrt(PairSpace.hs_norm_squared(tuple(perturbed)))
    normalized_perturbation = tuple(
        value / perturbation_norm for value in perturbed
    )
    check(
        "5.3  a normalized nonuniform diagonal vector fails component equality",
        not close(normalized_perturbation[0], normalized_perturbation[-1]),
        (
            f"first={normalized_perturbation[0]:.12f}, "
            f"last={normalized_perturbation[-1]:.12f}"
        ),
    )


def block_6_forbidden_imports() -> None:
    print("\n=== Block 6: forbidden physical-readout imports are absent ===\n")

    forbidden_symbols = {
        "g_bare",
        "y_t_phys",
        "V_EWSB",
        "Z_LSZ",
        "P_chiral",
        "sigma_HS",
        "source_normalization",
    }

    normalization_implementation = inspect.getsource(PairSpace)
    leaked = sorted(
        symbol for symbol in forbidden_symbols if symbol in normalization_implementation
    )
    check(
        "6.1  normalization implementation uses no physical-readout symbols",
        not leaked,
        f"leaked={leaked}",
    )

    print("  [INFO] physical Yukawa matching closure is not claimed")
    print("  [INFO] HS/source normalization remains outside this proof")
    print("  [INFO] SSB VEV division remains outside this proof")
    print("  [INFO] chirality projection remains outside this proof")
    print("  [INFO] LSZ/external-state normalization remains outside this proof")
    print("  [INFO] absence of extra physical factors remains outside this proof")


def main() -> int:
    print("=" * 72)
    print("YT SSB matching-gap arithmetic boundary verifier")
    print("=" * 72)

    space = block_1_normalization_derivation()
    block_2_matrix_form(space)
    block_3_component_overlaps(space)
    block_4_general_dimensions()
    block_5_falsifiers(space)
    block_6_forbidden_imports()

    print("\n" + "=" * 72)
    print(f"RESULT: {PASS_COUNT} PASS, {FAIL_COUNT} FAIL")
    print("=" * 72)

    if FAIL_COUNT == 0:
        print(
            "\n  OUTCOME: exact H_unit component-overlap arithmetic verified.\n"
            "  Stated instance: <component|H_unit|component> = 1/sqrt(6).\n"
            "  Boundary: this does NOT close the physical SSB/Yukawa matching\n"
            "  theorem; that operator-matching problem remains open."
        )
        return 0

    print("\n  OUTCOME: arithmetic verifier FAILED.\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
