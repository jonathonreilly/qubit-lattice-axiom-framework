#!/usr/bin/env python3
"""
Route-2 E-center blindness no-go for the quark endpoint chain.

Status:
  exact negative boundary for E-center-blind Route-2 endpoint repairs.

Source boundary:
  The reduced endpoint carrier and channelwise readout setup are supplied by
  QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md. This runner consumes
  that setup and proves only the E-center-blind negative boundary; it does
  not derive the granted T-side endpoint candidates or the missing E-center
  lift.

Safe claim:
  The Route-2 endpoint chain cannot derive the missing E-channel value
  rho_E = beta_E/alpha_E = 21/4 from constraints that never inspect the
  E-center column.  Shell normalization, T-side endpoint data, channel
  preservation, and low-rational/naturality filters are invariant under the
  one-parameter rho_E shift until an E-center primitive is supplied.

  This does not derive rho_E, quark masses, CKM/J, or any retained quark
  closure.  It sharpens the repair target: a positive repair must contain a
  genuine E-center lift or an equivalent source/readout primitive.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations


PASS_COUNT = 0
FAIL_COUNT = 0


Vector = tuple[Fraction, Fraction, Fraction, Fraction]

E_SHELL: Vector = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
E_CENTER: Vector = (Fraction(1), Fraction(0), Fraction(1, 6), Fraction(0))
T_SHELL: Vector = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
T_CENTER: Vector = (Fraction(0), Fraction(1), Fraction(0), Fraction(1, 6))


@dataclass(frozen=True)
class ReducedReadout:
    rho_e: Fraction
    alpha_e: Fraction = Fraction(1)
    alpha_t: Fraction = Fraction(-2)
    beta_t: Fraction = Fraction(2)

    @property
    def beta_e(self) -> Fraction:
        return self.rho_e * self.alpha_e

    def apply(self, v: Vector) -> tuple[Fraction, Fraction]:
        x_e, x_t, d_e, d_t = v
        return (
            self.alpha_e * x_e + self.beta_e * d_e,
            self.alpha_t * x_t + self.beta_t * d_t,
        )

    @property
    def q_t(self) -> Fraction:
        shell = self.apply(T_SHELL)[1]
        center = self.apply(T_CENTER)[1]
        return center / shell

    @property
    def q_e(self) -> Fraction:
        shell = self.apply(E_SHELL)[0]
        center = self.apply(E_CENTER)[0]
        return center / shell

    @property
    def shell_te(self) -> Fraction:
        return self.apply(T_SHELL)[1] / self.apply(E_SHELL)[0]

    @property
    def center_te(self) -> Fraction:
        return self.apply(T_CENTER)[1] / self.apply(E_CENTER)[0]


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


def rank(vectors: list[Vector]) -> int:
    matrix = [list(v) for v in vectors if any(v)]
    if not matrix:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    rank_count = 0
    pivot_row = 0
    for col in range(cols):
        pivot = None
        for row in range(pivot_row, rows):
            if matrix[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        pivot_val = matrix[pivot_row][col]
        matrix[pivot_row] = [x / pivot_val for x in matrix[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            factor = matrix[row][col]
            if factor != 0:
                matrix[row] = [
                    matrix[row][i] - factor * matrix[pivot_row][i]
                    for i in range(cols)
                ]
        rank_count += 1
        pivot_row += 1
        if pivot_row == rows:
            break
    return rank_count


def in_span(v: Vector, basis: list[Vector]) -> bool:
    return rank(basis + [v]) == rank(basis)


def e_center_blind_signature(readout: ReducedReadout) -> tuple[tuple[Fraction, Fraction], ...]:
    """All data seen by the E-center-blind endpoint constraints."""
    return (
        readout.apply(E_SHELL),
        readout.apply(T_SHELL),
        readout.apply(T_CENTER),
        (readout.q_t, readout.shell_te),
    )


def solve_rho_for_center_ratio(target: Fraction) -> Fraction:
    # target = (-5/3) / (1 + rho/6)
    return Fraction(6) * (Fraction(-5, 3) / target - Fraction(1))


def low_rational_family(max_num: int = 32, max_den: int = 16) -> set[Fraction]:
    out: set[Fraction] = set()
    for den in range(1, max_den + 1):
        for num in range(-max_num, max_num + 1):
            out.add(Fraction(num, den))
    return out


def part1_geometry() -> None:
    print("\n" + "=" * 72)
    print("PART 1: Endpoint Carrier Geometry")
    print("=" * 72)

    blind_basis = [E_SHELL, T_SHELL, T_CENTER]
    e_center_direction: Vector = tuple(E_CENTER[i] - E_SHELL[i] for i in range(4))  # type: ignore[assignment]
    full_basis = [E_SHELL, E_CENTER, T_SHELL, T_CENTER]

    print(f"\n  E-shell  = {E_SHELL}")
    print(f"  E-center = {E_CENTER}")
    print(f"  T-shell  = {T_SHELL}")
    print(f"  T-center = {T_CENTER}")
    print(f"  E-center lift direction = {e_center_direction}")

    check(
        "The E-center-blind endpoint subspace has rank 3",
        rank(blind_basis) == 3,
        f"rank = {rank(blind_basis)}",
    )
    check(
        "The full endpoint carrier basis has rank 4",
        rank(full_basis) == 4,
        f"rank = {rank(full_basis)}",
    )
    check(
        "The E-center lift direction is not in the E-center-blind endpoint subspace",
        not in_span(e_center_direction, blind_basis),
        "adding E-center raises rank from 3 to 4",
    )


def part2_invariance() -> None:
    print("\n" + "=" * 72)
    print("PART 2: Rho_E Invariance Under E-Center-Blind Constraints")
    print("=" * 72)

    test_rhos = [Fraction(-1), Fraction(0), Fraction(1), Fraction(21, 4)]
    signatures = [e_center_blind_signature(ReducedReadout(rho)) for rho in test_rhos]
    first = signatures[0]

    for rho, signature in zip(test_rhos, signatures):
        readout = ReducedReadout(rho)
        print(
            f"  rho_E={str(rho):>5s}: "
            f"E-shell={readout.apply(E_SHELL)}, "
            f"T-shell={readout.apply(T_SHELL)}, "
            f"T-center={readout.apply(T_CENTER)}, "
            f"q_T={readout.q_t}, shell T/E={readout.shell_te}, "
            f"E-center={readout.apply(E_CENTER)}"
        )
        check(
            f"rho_E={rho} preserves all E-center-blind endpoint data",
            signature == first,
        )

    check(
        "E-center values vary while all E-center-blind data are fixed",
        len({ReducedReadout(rho).apply(E_CENTER)[0] for rho in test_rhos}) == len(test_rhos),
        "the invisible coordinate is exactly beta_E/6",
    )


def part3_target_equivalence() -> None:
    print("\n" + "=" * 72)
    print("PART 3: Target Equivalence")
    print("=" * 72)

    target_rho = Fraction(21, 4)
    target_readout = ReducedReadout(target_rho)
    solved_rho = solve_rho_for_center_ratio(Fraction(-8, 9))

    print(f"\n  rho_E target = {target_rho}")
    print(f"  q_E target   = {target_readout.q_e}")
    print(f"  center T/E   = {target_readout.center_te}")
    print(f"  solved rho from center T/E = -8/9: {solved_rho}")

    check(
        "rho_E=21/4 is exactly equivalent to q_E=15/8",
        target_readout.q_e == Fraction(15, 8),
        f"q_E={target_readout.q_e}",
    )
    check(
        "rho_E=21/4 is exactly equivalent to center T/E=-8/9 under granted T-side data",
        target_readout.center_te == Fraction(-8, 9),
        f"center T/E={target_readout.center_te}",
    )
    check(
        "Solving the center-ratio equation recovers rho_E=21/4 uniquely",
        solved_rho == target_rho,
        f"solved rho={solved_rho}",
    )


def part4_low_rational_firewall() -> None:
    print("\n" + "=" * 72)
    print("PART 4: Low-Rational And Naturality Firewall")
    print("=" * 72)

    candidates = low_rational_family()
    admissible = [
        rho
        for rho in candidates
        if e_center_blind_signature(ReducedReadout(rho))
        == e_center_blind_signature(ReducedReadout(Fraction(0)))
    ]
    examples = [Fraction(-1), Fraction(0), Fraction(1), Fraction(21, 4)]

    print(f"\n  low-rational candidate count = {len(candidates)}")
    print(f"  E-center-blind admissible count = {len(admissible)}")
    print("  example admissible values:")
    for rho in examples:
        readout = ReducedReadout(rho)
        print(f"    rho_E={rho}: q_E={readout.q_e}, center T/E={readout.center_te}")

    check(
        "The low-rational grammar contains the target but does not select it",
        Fraction(21, 4) in candidates and len(admissible) > 200,
        f"admissible count={len(admissible)}",
    )
    check(
        "Simple naturality choices are exact admissible alternatives but not the target",
        all(rho in admissible for rho in [Fraction(-1), Fraction(0), Fraction(1)])
        and all(rho != Fraction(21, 4) for rho in [Fraction(-1), Fraction(0), Fraction(1)]),
    )
    check(
        "No E-center-blind pairwise equality among the four endpoint images fixes rho_E",
        all(
            e_center_blind_signature(ReducedReadout(rho_a))
            == e_center_blind_signature(ReducedReadout(rho_b))
            for rho_a, rho_b in combinations(examples, 2)
        ),
        "rho_E only appears when E-center is evaluated",
    )


def part5_summary() -> None:
    print("\n" + "=" * 72)
    print("PART 5: Summary")
    print("=" * 72)
    print(
        "\n  Exact result: E-center-blind endpoint constraints leave rho_E free.\n"
        "  Therefore the Route-2 ratio-chain repair cannot derive -8/9 from\n"
        "  shell normalization, T-side endpoint data, channel preservation,\n"
        "  or low-rational/naturality filtering alone. A positive repair must\n"
        "  supply an E-center lift, source-domain rule, or equivalent readout\n"
        "  primitive that evaluates the E-center column."
    )


def main() -> int:
    print("=" * 72)
    print("  FRONTIER: Quark Route-2 E-Center Blindness No-Go")
    print("=" * 72)
    print(
        "\n  Source boundary: carrier/readout setup supplied by "
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md; "
        "this runner proves only the E-center-blind no-go."
    )

    part1_geometry()
    part2_invariance()
    part3_target_equivalence()
    part4_low_rational_firewall()
    part5_summary()

    print("\n" + "=" * 72)
    print(f"  TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print("=" * 72)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
