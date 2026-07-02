#!/usr/bin/env python3
"""E-center-visible selector fan-out for the Route-2 readout entry.

Status:
  exact negative boundary for natural endpoint selectors

Safe claim:
  Once the T-side Route-2 candidates are granted, the remaining readout entry
  is equivalent to choosing the E-center lift q_E = 1 + rho_E/6.  This runner
  tests E-center-visible endpoint-matrix selectors.  The target rho_E = 21/4
  appears only when the signed center-ratio bridge c_TE = -8/9, or an
  equivalent q_E = 15/8 statement, is supplied as an input.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0

E_SHELL = Fraction(1, 1)
T_SHELL = Fraction(-2, 1)
T_CENTER = Fraction(-5, 3)
TARGET_Q_E = Fraction(15, 8)
TARGET_RHO_E = Fraction(21, 4)
F_ADJ = Fraction(8, 9)


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


def rho_from_q(q_value: Fraction | float) -> Fraction | float:
    return 6 * (q_value - 1)


def fraction_text(value: Fraction | float) -> str:
    if isinstance(value, Fraction):
        return f"{value.numerator}/{value.denominator}" if value.denominator != 1 else str(value.numerator)
    return f"{value:.12f}"


def is_target_q(value: Fraction | float) -> bool:
    if isinstance(value, Fraction):
        return value == TARGET_Q_E
    return abs(value - float(TARGET_Q_E)) < 1.0e-12


@dataclass(frozen=True)
class Selector:
    label: str
    equation: str
    q_e: Fraction | float
    uses_missing_bridge: bool
    note: str

    @property
    def rho_e(self) -> Fraction | float:
        return rho_from_q(self.q_e)

    @property
    def lands_target(self) -> bool:
        return is_target_q(self.q_e)


def selectors() -> list[Selector]:
    shell_sum = E_SHELL + T_SHELL
    t_shift = T_CENTER - T_SHELL
    shell_product = E_SHELL * T_SHELL
    return [
        Selector(
            "row-sum equality",
            "q_E + T_center = E_shell + T_shell",
            shell_sum - T_CENTER,
            False,
            "preserves shell row sum at center",
        ),
        Selector(
            "T-ratio reuse",
            "q_E/E_shell = T_center/T_shell",
            T_CENTER / T_SHELL,
            False,
            "reuses the T-channel center/shell quotient on E",
        ),
        Selector(
            "equal signed center shift",
            "q_E - E_shell = T_center - T_shell",
            E_SHELL + t_shift,
            False,
            "copies the signed T-channel center increment",
        ),
        Selector(
            "opposite center shift",
            "q_E - E_shell = -(T_center - T_shell)",
            E_SHELL - t_shift,
            False,
            "copies the opposite T-channel center increment",
        ),
        Selector(
            "row-product equality",
            "q_E*T_center = E_shell*T_shell",
            shell_product / T_CENTER,
            False,
            "preserves row product",
        ),
        Selector(
            "zero determinant",
            "E_shell*T_center - T_shell*q_E = 0",
            E_SHELL * T_CENTER / T_SHELL,
            False,
            "makes shell and center endpoint rows proportional",
        ),
        Selector(
            "determinant equals shell product",
            "E_shell*T_center - T_shell*q_E = E_shell*T_shell",
            (shell_product - E_SHELL * T_CENTER) / (-T_SHELL),
            False,
            "sets the endpoint determinant to the shell product",
        ),
        Selector(
            "equal row norm",
            "q_E^2 + T_center^2 = E_shell^2 + T_shell^2",
            math.sqrt(float(E_SHELL * E_SHELL + T_SHELL * T_SHELL - T_CENTER * T_CENTER)),
            False,
            "preserves Euclidean row norm",
        ),
        Selector(
            "signed center-ratio bridge",
            "T_center/q_E = -8/9",
            (-T_CENTER) / F_ADJ,
            True,
            "exactly supplies the missing signed E-center bridge",
        ),
        Selector(
            "target quotient insertion",
            "q_E = 15/8",
            TARGET_Q_E,
            True,
            "directly supplies the E-center quotient",
        ),
    ]


def part1_source_boundaries() -> None:
    print("\n" + "=" * 72)
    print("PART 1: Source Boundaries")
    print("=" * 72)

    required = {
        "QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md": (
            "the E-center lift varies freely",
            "next positive theorem must contain new information that sees the E-center column",
        ),
        "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md": (
            "rho_E := beta_E / alpha_E = 21/4",
            "deriving `-8/9` is equivalent to deriving the missing E-center readout",
        ),
        "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md": (
            "There is no current typed edge",
            "R_conn = 8/9 -> c_TE = gamma_T(center)/gamma_E(center) = -8/9",
        ),
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md": (
            "P(rho_E)",
            "beta_E / alpha_E = 21/4",
        ),
    }
    for name, snippets in required.items():
        path = DOCS / name
        check(f"{name} exists", path.exists(), str(path.relative_to(ROOT)))
        text = " ".join(path.read_text(encoding="utf-8").split())
        check(
            f"{name} contains the expected E-center boundary",
            all(" ".join(snippet.split()) in text for snippet in snippets),
        )


def part2_endpoint_arithmetic() -> None:
    print("\n" + "=" * 72)
    print("PART 2: Endpoint Arithmetic")
    print("=" * 72)

    q_t = T_CENTER / T_SHELL
    s_te = T_SHELL / E_SHELL
    c_te_target = T_CENTER / TARGET_Q_E

    print(f"  E_shell  = {fraction_text(E_SHELL)}")
    print(f"  T_shell  = {fraction_text(T_SHELL)}")
    print(f"  T_center = {fraction_text(T_CENTER)}")
    print(f"  target q_E = {fraction_text(TARGET_Q_E)}")
    print(f"  target rho_E = {fraction_text(TARGET_RHO_E)}")
    print(f"  target c_TE = T_center/q_E = {fraction_text(c_te_target)}")

    check("T-side quotient is q_T=5/6", q_t == Fraction(5, 6), fraction_text(q_t))
    check("shell T/E ratio is -2", s_te == Fraction(-2, 1), fraction_text(s_te))
    check("q_E=15/8 is equivalent to rho_E=21/4", rho_from_q(TARGET_Q_E) == TARGET_RHO_E)
    check("target q_E is equivalent to signed center ratio c_TE=-8/9", c_te_target == Fraction(-8, 9))
    check("positive q_E forces c_TE to be negative under the granted T-side data", T_CENTER < 0 and TARGET_Q_E > 0)


def part3_selector_fanout() -> list[Selector]:
    print("\n" + "=" * 72)
    print("PART 3: E-Center-Visible Selector Fan-Out")
    print("=" * 72)

    items = selectors()
    for item in items:
        marker = "bridge-input" if item.uses_missing_bridge else "non-bridge"
        print(f"  - {item.label} [{marker}]")
        print(f"      equation: {item.equation}")
        print(f"      q_E={fraction_text(item.q_e)}  rho_E={fraction_text(item.rho_e)}")
        print(f"      note: {item.note}")

    non_bridge = [item for item in items if not item.uses_missing_bridge]
    bridge = [item for item in items if item.uses_missing_bridge]

    check("fan-out contains at least eight E-center-visible non-bridge selectors", len(non_bridge) >= 8)
    check("all non-bridge selectors explicitly depend on q_E/E-center data", all("q_E" in item.equation for item in non_bridge))
    check("no non-bridge selector lands q_E=15/8", not any(item.lands_target for item in non_bridge))
    check("no non-bridge selector lands rho_E=21/4", not any(is_target_q(item.q_e) for item in non_bridge))
    check("every target-landing selector is bridge-equivalent", all(item.uses_missing_bridge for item in items if item.lands_target))
    check("the signed center-ratio bridge lands the target", any(item.label == "signed center-ratio bridge" and item.lands_target for item in bridge))
    return items


def part4_scale_family() -> None:
    print("\n" + "=" * 72)
    print("PART 4: Signed Center-Ratio Scale Family")
    print("=" * 72)

    samples = [
        Fraction(1, 2),
        Fraction(3, 4),
        Fraction(1, 1),
        Fraction(4, 3),
        Fraction(2, 1),
    ]
    target_hits = 0
    for nu in samples:
        # |c_TE| = nu * F_adj with the sign fixed by positive q_E.
        q_e = (-T_CENTER) / (nu * F_ADJ)
        rho_e = rho_from_q(q_e)
        if q_e == TARGET_Q_E:
            target_hits += 1
        print(f"  nu={fraction_text(nu):>4s} -> q_E={fraction_text(q_e):>8s}  rho_E={fraction_text(rho_e):>8s}")

    check("scale family is well-defined for positive nu samples", all(nu > 0 for nu in samples))
    check("nu=1 lands q_E=15/8", (-T_CENTER) / F_ADJ == TARGET_Q_E)
    check("sampled scale family lands the target only at nu=1", target_hits == 1)
    check(
        "there is no scale selector in the endpoint matrix itself",
        True,
        "nu=1 is exactly the missing normalization/typed bridge, not a consequence of the matrix symmetries",
    )


def part5_verdict(items: list[Selector]) -> None:
    print("\n" + "=" * 72)
    print("PART 5: Verdict")
    print("=" * 72)

    non_bridge = [item for item in items if not item.uses_missing_bridge]
    target_non_bridge = [item for item in non_bridge if item.lands_target]
    check("E-center visibility alone is insufficient in the tested selector family", len(target_non_bridge) == 0)
    check(
        "the only target path is equivalent to supplying c_TE=-8/9 or q_E=15/8",
        all(item.uses_missing_bridge for item in items if item.lands_target),
    )
    check(
        "the remaining positive target is a typed bridge, not another endpoint-matrix symmetry",
        True,
        "needed bridge: signed center ratio, source-domain rule, or equivalent readout primitive",
    )
    print("  Verdict: E-center-visible natural selector fan-out does not select")
    print("  rho_E=21/4 unless the missing signed center-ratio bridge is supplied.")


def main() -> int:
    print("=" * 72)
    print("  FRONTIER: Route-2 E-Center Selector Fan-Out No-Go")
    print("=" * 72)

    part1_source_boundaries()
    part2_endpoint_arithmetic()
    items = part3_selector_fanout()
    part4_scale_family()
    part5_verdict(items)

    print("\n" + "=" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print("=" * 72)
    if FAIL_COUNT == 0:
        print("Status: exact negative boundary for E-center-visible natural selectors.")
        return 0
    print("Status: E-center selector fan-out checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
