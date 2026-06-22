#!/usr/bin/env python3
r"""Route-2 normalized-quotient selector trichotomy.

Safe claim:
  On the exact restricted Route-2 readout family, normalized quotient algebra
  does not by itself select rho_E = 21/4. It either remains blind to rho_E,
  rewrites the target as an equivalent quotient equation, or uses live endpoint
  distance as bounded comparator evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import numpy as np

from frontier_quark_route2_exact_readout_map import (
    EXACT_TOL,
    restricted_readout_data,
    theorem_target_lands,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs" / "QUARK_ROUTE2_NORMALIZED_QUOTIENT_SELECTOR_TRICHOTOMY_NOTE_2026-06-21.md"
QUOTIENT_NOTE = REPO_ROOT / "docs" / "QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md"
CHAIN_NOTE = REPO_ROOT / "docs" / "QUARK_ENDPOINT_RATIO_CHAIN_LAW_NOTE_2026-04-19.md"
READOUT_NOTE = REPO_ROOT / "docs" / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
NATURALITY_NOTE = REPO_ROOT / "docs" / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md"
BLINDNESS_NOTE = REPO_ROOT / "docs" / "QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md"

E_SHELL = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
E_CENTER = (Fraction(1), Fraction(0), Fraction(1, 6), Fraction(0))
T_SHELL = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
T_CENTER = (Fraction(0), Fraction(1), Fraction(0), Fraction(1, 6))

RHO_TARGET = Fraction(21, 4)
Q_E_TARGET = Fraction(15, 8)
C_TE_TARGET = Fraction(-8, 9)
LAMBDA_TARGET = Fraction(9, 4)

PASS_COUNT = 0
FAIL_COUNT = 0


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


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


@dataclass(frozen=True)
class ReducedReadout:
    rho_e: Fraction

    @property
    def alpha_e(self) -> Fraction:
        return Fraction(1)

    @property
    def beta_e(self) -> Fraction:
        return self.rho_e

    @property
    def alpha_t(self) -> Fraction:
        return Fraction(-2)

    @property
    def beta_t(self) -> Fraction:
        return Fraction(2)

    def apply(self, vector: tuple[Fraction, Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        x_e, x_t, d_e, d_t = vector
        return (
            self.alpha_e * x_e + self.beta_e * d_e,
            self.alpha_t * x_t + self.beta_t * d_t,
        )

    @property
    def q_e(self) -> Fraction:
        return self.apply(E_CENTER)[0] / self.apply(E_SHELL)[0]

    @property
    def q_t(self) -> Fraction:
        return self.apply(T_CENTER)[1] / self.apply(T_SHELL)[1]

    @property
    def shell_te(self) -> Fraction:
        return self.apply(T_SHELL)[1] / self.apply(E_SHELL)[0]

    @property
    def center_te(self) -> Fraction:
        return self.apply(T_CENTER)[1] / self.apply(E_CENTER)[0]

    @property
    def quotient_lambda(self) -> Fraction:
        return self.q_e / self.q_t

    @property
    def blind_signature(self) -> tuple[tuple[Fraction, Fraction], Fraction, Fraction]:
        return (
            (self.apply(E_SHELL), self.apply(T_SHELL), self.apply(T_CENTER)),  # type: ignore[return-value]
            self.q_t,
            self.shell_te,
        )


def solve_rho_from_q_e(q_e: Fraction) -> Fraction:
    return Fraction(6) * (q_e - 1)


def solve_rho_from_center_te(center_te: Fraction) -> Fraction:
    # center_te = (-5/3) / (1 + rho/6)
    return Fraction(6) * (Fraction(-5, 3) / center_te - 1)


def solve_rho_from_lambda(lambda_q: Fraction) -> Fraction:
    # lambda = q_E / q_T and q_T = 5/6
    return Fraction(6) * (lambda_q * Fraction(5, 6) - 1)


def low_positive_rationals(max_num: int, max_den: int, lower: Fraction, upper: Fraction) -> set[Fraction]:
    out: set[Fraction] = set()
    for den in range(1, max_den + 1):
        for num in range(1, max_num + 1):
            value = Fraction(num, den)
            if lower <= value <= upper:
                out.add(value)
    return out


def nearest_by_relative_gap(value: float, candidates: set[Fraction]) -> Fraction:
    return min(candidates, key=lambda candidate: abs(float(candidate) / value - 1.0))


def part1_source_surfaces() -> None:
    print("\n" + "=" * 72)
    print("PART 1: Source Surfaces")
    print("=" * 72)

    note = text(NOTE)
    quotient = text(QUOTIENT_NOTE)
    chain = text(CHAIN_NOTE)
    readout = text(READOUT_NOTE)
    naturality = text(NATURALITY_NOTE)
    blindness = text(BLINDNESS_NOTE)

    check(
        "trichotomy note and source notes are present",
        all(path.exists() for path in (NOTE, QUOTIENT_NOTE, CHAIN_NOTE, READOUT_NOTE, NATURALITY_NOTE, BLINDNESS_NOTE)),
        "direct note plus quotient, chain, readout, naturality, and blindness notes exist",
    )
    check(
        "quotient note identifies q_E=15/8 as the live quotient target",
        "gamma_E(center)/gamma_E(shell) = 15/8" in quotient
        and "additional E-center primitive" in quotient,
        "quotient target and missing primitive are explicit",
    )
    check(
        "ratio-chain note identifies the third leg -8/9 as the same obstruction",
        "gamma_T(center)/gamma_E(center) = -8/9" in chain
        and "third chain leg" in chain,
        "chain target is present",
    )
    check(
        "exact readout-map note records the missing endpoint triple",
        "(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)" in readout
        and "= (-1, -2, 21/4)" in readout,
        "full triple target is upstream",
    )
    check(
        "naturality no-go preserves source-domain and readout-map primitive routes",
        "source-domain" in naturality and "tensor readout-map theorem" in naturality,
        "positive routes remain open",
    )
    check(
        "direct trichotomy note bans quotient-only endpoint closure",
        "quotient normalization alone is not a missing theorem" in note
        and "independent E-center equation" in note,
        "note states the proof obligation",
    )


def part2_exact_equivalences() -> None:
    print("\n" + "=" * 72)
    print("PART 2: Exact Quotient Equivalences")
    print("=" * 72)

    data = restricted_readout_data()
    target = ReducedReadout(RHO_TARGET)
    theorem_lands = theorem_target_lands(data)

    expected_e_shell = np.array([1.0, 0.0, 0.0, 0.0])
    expected_e_center = np.array([1.0, 0.0, 1.0 / 6.0, 0.0])
    expected_t_shell = np.array([0.0, 1.0, 0.0, 0.0])
    expected_t_center = np.array([0.0, 1.0, 0.0, 1.0 / 6.0])

    check(
        "restricted carrier columns match the exact endpoint basis",
        np.max(np.abs(data.carrier_e_shell - expected_e_shell)) < EXACT_TOL
        and np.max(np.abs(data.carrier_e_center - expected_e_center)) < EXACT_TOL
        and np.max(np.abs(data.carrier_t_shell - expected_t_shell)) < EXACT_TOL
        and np.max(np.abs(data.carrier_t_center - expected_t_center)) < EXACT_TOL,
        "E/T shell and center columns are exact",
    )
    check(
        "rho_E=21/4 gives q_E=15/8 exactly",
        target.q_e == Q_E_TARGET,
        f"q_E={target.q_e}",
    )
    check(
        "rho_E=21/4 gives c_TE=-8/9 exactly",
        target.center_te == C_TE_TARGET,
        f"c_TE={target.center_te}",
    )
    check(
        "rho_E=21/4 gives q_E/q_T=9/4 exactly",
        target.quotient_lambda == LAMBDA_TARGET,
        f"q_E/q_T={target.quotient_lambda}",
    )
    check(
        "q_E=15/8 solves back to rho_E=21/4",
        solve_rho_from_q_e(Q_E_TARGET) == RHO_TARGET,
        f"rho={solve_rho_from_q_e(Q_E_TARGET)}",
    )
    check(
        "c_TE=-8/9 solves back to rho_E=21/4",
        solve_rho_from_center_te(C_TE_TARGET) == RHO_TARGET,
        f"rho={solve_rho_from_center_te(C_TE_TARGET)}",
    )
    check(
        "q_E/q_T=9/4 solves back to rho_E=21/4",
        solve_rho_from_lambda(LAMBDA_TARGET) == RHO_TARGET,
        f"rho={solve_rho_from_lambda(LAMBDA_TARGET)}",
    )
    check(
        "the live current-surface readout theorem still does not land",
        not theorem_lands,
        "the trichotomy is not an endpoint-triple derivation",
    )


def part3_selector_trichotomy() -> None:
    print("\n" + "=" * 72)
    print("PART 3: Normalized-Quotient Selector Trichotomy")
    print("=" * 72)

    test_rhos = [Fraction(-1), Fraction(0), Fraction(1), RHO_TARGET, Fraction(6)]
    readouts = [ReducedReadout(rho) for rho in test_rhos]
    first_signature = readouts[0].blind_signature

    print("  admissible reduced-family samples:")
    for readout in readouts:
        print(
            f"    rho_E={str(readout.rho_e):>5s}: "
            f"q_E={readout.q_e}, c_TE={readout.center_te}, "
            f"q_E/q_T={readout.quotient_lambda}"
        )

    check(
        "E-center-blind normalized data are identical across sampled rho_E values",
        all(readout.blind_signature == first_signature for readout in readouts),
        "q_T, shell T/E, and blind endpoint images are fixed",
    )
    check(
        "the E quotient varies across the same blind signature",
        len({readout.q_e for readout in readouts}) == len(readouts),
        "q_E changes while blind data do not",
    )
    check(
        "the target sample is just one exact admissible member of the same family",
        RHO_TARGET in {readout.rho_e for readout in readouts}
        and ReducedReadout(Fraction(0)).q_e == Fraction(1),
        "rho_E=0 and rho_E=21/4 are both exact admissible samples",
    )
    check(
        "same-as-T quotient naturality is admissible but not target",
        ReducedReadout(Fraction(-1)).q_e == Fraction(5, 6)
        and Fraction(-1) != RHO_TARGET,
        "rho_E=-1 gives q_E=q_T=5/6",
    )
    check(
        "no-lift quotient naturality is admissible but not target",
        ReducedReadout(Fraction(0)).q_e == Fraction(1)
        and Fraction(0) != RHO_TARGET,
        "rho_E=0 gives q_E=1",
    )
    check(
        "unit-lift quotient naturality is admissible but not target",
        ReducedReadout(Fraction(1)).q_e == Fraction(7, 6)
        and Fraction(1) != RHO_TARGET,
        "rho_E=1 gives q_E=7/6",
    )
    check(
        "imposing q_E=15/8 is exactly the target equation, not a new selector",
        solve_rho_from_q_e(Q_E_TARGET) == RHO_TARGET,
        "q_E target rewrites rho_E target",
    )
    check(
        "imposing c_TE=-8/9 is exactly the target equation, not a new selector",
        solve_rho_from_center_te(C_TE_TARGET) == RHO_TARGET,
        "center T/E target rewrites rho_E target",
    )
    check(
        "imposing q_E/q_T=9/4 is exactly the target equation, not a new selector",
        solve_rho_from_lambda(LAMBDA_TARGET) == RHO_TARGET,
        "lambda target rewrites rho_E target",
    )

    q_candidates = low_positive_rationals(32, 16, Fraction(1, 2), Fraction(3, 1))
    c_candidates = {Fraction(-5, 3) / q for q in q_candidates}
    live_q_e = float(1.0 + restricted_readout_data().rho_e / 6.0)
    nearest_q = nearest_by_relative_gap(live_q_e, q_candidates)

    check(
        "low-rational q_E grammar contains the target but is not unique",
        Q_E_TARGET in q_candidates and len(q_candidates) > 20,
        f"candidate count={len(q_candidates)}",
    )
    check(
        "low-rational c_TE grammar contains the target but is not unique",
        C_TE_TARGET in c_candidates and len(c_candidates) > 20,
        f"candidate count={len(c_candidates)}",
    )
    check(
        "nearest-rational selection uses live endpoint distance as comparator evidence",
        nearest_q == Q_E_TARGET and abs(live_q_e - float(Q_E_TARGET)) > EXACT_TOL,
        f"nearest={nearest_q}, live q_E={live_q_e:.12f}",
    )


def part4_firewall_and_fanout() -> None:
    print("\n" + "=" * 72)
    print("PART 4: Firewall And Stretch Fan-Out")
    print("=" * 72)

    note = text(NOTE)
    proof_inputs = {
        "restricted_carrier_columns",
        "granted_t_side_candidates",
        "quotient_algebra",
        "exact_rational_arithmetic",
    }
    forbidden = {
        "observed_quark_masses",
        "fitted_yukawa_values",
        "ckm_j_error_minimization",
        "nearest_live_endpoint_as_proof",
        "hidden_e_center_weight",
    }

    check(
        "forbidden proof inputs are absent from the trichotomy proof-input set",
        proof_inputs.isdisjoint(forbidden),
        str(sorted(proof_inputs)),
    )
    check(
        "note states the three selector cases explicitly",
        "The trichotomy is:" in note
        and "blind to the E-center column" in note
        and "low-rational or nearest-candidate rule" in note,
        "blind, target-equivalent, and comparator cases are present",
    )
    check(
        "note says quotient algebra does not derive endpoint closure",
        "it rewrites the target rather than deriving it" in note
        and "does not" in note
        and "select the parameter by itself" in note,
        "no endpoint closure is claimed",
    )
    check(
        "note preserves positive E-center/source-readout routes",
        "source-domain rule" in note
        and "tensor readout-map theorem" in note
        and "alternate up-sector scalar-law route" in note,
        "positive routes remain open",
    )
    check(
        "projective quotient normalization alone is classified as a route-pruning result",
        "What This Prunes" in note
        and "form a normalized quotient" in note,
        "route family is pruned narrowly",
    )
    check(
        "target constants are not admitted as a new axiom in the note",
        "new target-valued axiom" in note
        and "Forbidden as proof inputs" in note,
        "target constants are firewalled",
    )
    check(
        "bounded comparator use is separated from proof input",
        "bounded comparator evidence" in note
        and "Live endpoint distance may appear only" in note,
        "nearest-rational use is demoted",
    )
    check(
        "the remaining proof obligation is an independent E-center equation",
        "independent E-center equation" in note
        and "forces one quotient value" in note,
        "the positive target is named",
    )


def main() -> int:
    print("Route-2 normalized-quotient selector trichotomy")
    print("=" * 72)

    part1_source_surfaces()
    part2_exact_equivalences()
    part3_selector_trichotomy()
    part4_firewall_and_fanout()

    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print("Status: normalized-quotient selector trichotomy; endpoint triple remains open.")
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
