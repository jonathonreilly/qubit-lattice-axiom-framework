#!/usr/bin/env python3
"""Check the 2026-10-21 arithmetic annotation on two historic hierarchy wrappers.

Scope (2026-11-14):
  This runner checks only the arithmetic of the "Arithmetic correction
  annotation (2026-10-21)" in

    docs/historic_intake/HISTORIC_HIERARCHY_HONEST_REVIEW_INTAKE_NOTE_2026-08-05.md
    docs/historic_intake/HISTORIC_HIERARCHY_WHY_226_NOTE_INTAKE_NOTE_2026-08-05.md

  for the model exactly as that annotation prints it,

    v = 2.435e18 * exp(-8*pi^2/(N_eff*y_t^2)) GeV,   N_eff = 12*Z_chi^2.

  It does not check the historical claim compressed below the annotation, the
  archived originals, the Sigma_1 mapping, the CW or gauge-sign argument, or
  any physical mechanism. The historical values it rejects (-22.31, 226 GeV,
  N_eff > 12, 5*10^5 GeV) are taken as the strings the annotation quotes; the
  runner does not read the archives.

Method:
  Decimal arithmetic at 60 significant digits, with pi from Machin's formula.
  Each number the annotation prints is read from each note and compared with
  the recomputed value rounded (half-even) to the printed digits. Controls:
  the comparison rejects every printed value moved by one unit in its last
  digit, and the historical claims are rejected for the printed model.
"""

from __future__ import annotations

import re
import sys
from decimal import ROUND_HALF_EVEN, Decimal, getcontext
from pathlib import Path

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = (
    "docs/historic_intake/HISTORIC_HIERARCHY_HONEST_REVIEW_INTAKE_NOTE_2026-08-05.md",
    "docs/historic_intake/HISTORIC_HIERARCHY_WHY_226_NOTE_INTAKE_NOTE_2026-08-05.md",
)

ROOT = Path(__file__).resolve().parents[1]
getcontext().prec = 60

PASS_COUNT = 0
FAIL_COUNT = 0

M_REF = Decimal("2.435e18")  # GeV, the reference mass the annotation prints
V_TARGET = Decimal("246")  # GeV
MODEL_LINE = "v = 2.435e18 * exp(-8*pi^2/(N_eff*y_t^2)) GeV,"
SECTION_HEADING = "## Arithmetic correction annotation (2026-10-21)"


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{'PASS' if condition else 'FAIL'}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return bool(condition)


def arctan_inv(n: int) -> Decimal:
    """arctan(1/n) by its alternating series, to the context precision."""
    x = Decimal(1) / n
    x2 = x * x
    term = x
    total = x
    k = 1
    eps = Decimal(10) ** (-(getcontext().prec + 2))
    while abs(term) > eps:
        term *= -x2
        total += term / (2 * k + 1)
        k += 1
    return total


PI = 16 * arctan_inv(5) - 4 * arctan_inv(239)
EIGHT_PI2 = 8 * PI * PI


def v_model(y_t: Decimal, n_eff: Decimal) -> Decimal:
    return M_REF * (-(EIGHT_PI2 / (n_eff * y_t * y_t))).exp()


def n_eff_for_log(log_ratio: Decimal, y_t: Decimal) -> Decimal:
    """Solve -8 pi^2/(N y^2) = log_ratio for N."""
    return -EIGHT_PI2 / (y_t * y_t * log_ratio)


def matches_printed(computed: Decimal, printed: str) -> bool:
    """True when computed rounds (half-even) to the printed decimal digits."""
    target = Decimal(printed)
    quantum = Decimal(1).scaleb(target.as_tuple().exponent)
    return computed.quantize(quantum, rounding=ROUND_HALF_EVEN) == target


def one_unit_off(printed: str) -> str:
    target = Decimal(printed)
    return str(target + Decimal(1).scaleb(target.as_tuple().exponent))


def annotation_section(rel: str) -> str:
    text = (ROOT / rel).read_text(encoding="utf-8")
    start = text.index(SECTION_HEADING)
    end = text.find("\n## ", start + len(SECTION_HEADING))
    return text[start:end if end != -1 else len(text)]


def one(pattern: str, text: str) -> str:
    found = re.findall(pattern, text)
    if len(found) != 1:
        raise ValueError(f"expected one match for {pattern!r}, found {len(found)}")
    return found[0]


def check_note(rel: str, label: str) -> None:
    print(f"\n=== {label}: {rel} ===\n")
    sec = annotation_section(rel)
    printed: list[tuple[str, Decimal, str]] = []

    check(f"{label}: the annotation prints the model this runner evaluates (text binding)",
          MODEL_LINE in sec and "N_eff = 12*Z_chi^2." in sec)

    # Direct-substitution table.
    rows = re.findall(r"^\|\s*([0-9.]+)\s*\|\s*([0-9.]+)\s*\|\s*([0-9.eE+-]+)\s*\|\s*$",
                      sec, flags=re.MULTILINE)
    expected_inputs = [("0.439", "10.64"), ("0.439", "12"), ("0.9369", "10.64")]
    check(f"{label}: the table has the three supplied (y_t, N_eff) rows",
          [(y, n) for y, n, _ in rows] == expected_inputs,
          f"rows {[(y, n) for y, n, _ in rows]}")
    for y, n, v_str in rows:
        v = v_model(Decimal(y), Decimal(n))
        printed.append((f"v({y}, {n})", v, v_str))
        check(f"{label}: v(y_t={y}, N_eff={n}) = {v_str} GeV at the printed digits",
              matches_printed(v, v_str), f"computed {v:.12E}")

    # Consistent-unit inverse calculation.
    log_ok = (V_TARGET / M_REF).ln()
    log_str = one(r"ln\(246/2\.435e18\) = (-?[0-9.]+),", sec)
    n_need = n_eff_for_log(log_ok, Decimal("0.439"))
    n_str = one(r"N_eff = -8\*pi\^2/\(0\.439\^2\*ln\(246/2\.435e18\)\) = ([0-9.]+),", sec)
    z_need = (n_need / 12).sqrt()
    z_str = one(r"Z_chi = sqrt\(N_eff/12\) = ([0-9.]+)\.", sec)
    for name, val, s in (("ln(246/2.435e18)", log_ok, log_str),
                         ("N_eff for 246 GeV at y_t=0.439", n_need, n_str),
                         ("Z_chi = sqrt(N_eff/12)", z_need, z_str)):
        printed.append((name, val, s))
        check(f"{label}: {name} = {s} at the printed digits", matches_printed(val, s),
              f"computed {val:.14f}")
    check(f"{label}: the solved inputs reproduce 246 GeV in the printed model",
          abs(v_model(Decimal("0.439"), n_need) - V_TARGET) < Decimal("1e-40"),
          f"v = {v_model(Decimal('0.439'), n_need):.6f} GeV")

    # The archive's mixed-unit literal.
    lit_str, hist_str = re.findall(
        r"literal `ln\(246e9/2\.435e18\)` is (-?[0-9.]+), not (-?[0-9.]+)", sec)[0]
    log_lit = (Decimal("246e9") / M_REF).ln()
    printed.append(("ln(246e9/2.435e18)", log_lit, lit_str))
    check(f"{label}: literal ln(246e9/2.435e18) = {lit_str} at the printed digits",
          matches_printed(log_lit, lit_str), f"computed {log_lit:.14f}")

    # Controls rejecting the historical claims for the printed model.
    hist = Decimal(hist_str)
    check(f"{label}: control: the historical {hist_str} is neither logarithm",
          abs(hist - log_lit) > 1 and abs(hist - log_ok) > 1,
          f"mixed-unit {log_lit:.4f}, consistent-unit {log_ok:.4f}")
    n_hist = n_eff_for_log(hist, Decimal("0.439"))
    n_mixed = n_eff_for_log(log_lit, Decimal("0.439"))
    check(f"{label}: control: N_eff > 12 (Z_chi > 1) is not required by the printed model",
          n_need < 12 and z_need < 1 and n_hist > 12 and n_mixed > 12,
          f"consistent units give N_eff={n_need:.4f}, Z_chi={z_need:.4f}; "
          f"N_eff > 12 appears only from {hist_str} ({n_hist:.2f}) or the mixed-unit log "
          f"({n_mixed:.2f})")
    v_sm = v_model(Decimal("0.9369"), Decimal("10.64"))
    check(f"{label}: control: y_t=0.9369, N_eff=10.64 does not give 226 GeV",
          abs((v_sm / Decimal(226)).log10()) > 10,
          f"v = {v_sm:.6E} GeV, log10(v/226) = {(v_sm / Decimal(226)).log10():.3f}")

    if "5*10^5 GeV" in sec:
        check(f"{label}: control: the same inputs do not give the historical 5*10^5 GeV",
              abs((v_sm / Decimal("5e5")).log10()) > 1,
              f"log10(v/5e5) = {(v_sm / Decimal('5e5')).log10():.3f}")

    if "exp(-8.45)*2.435e18" in sec:
        exponent = EIGHT_PI2 / (Decimal("10.64") * Decimal("0.9369") ** 2)
        approx_str = one(r"literal `exp\(-8\.45\)\*2\.435e18` is approximately ([0-9.eE+]+) GeV", sec)
        approx = M_REF * Decimal("-8.45").exp()
        printed.append(("exp(-8.45)*2.435e18", approx, approx_str))
        check(f"{label}: 8.45 is the two-decimal rounding of 8 pi^2/(10.64*0.9369^2)",
              exponent.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN) == Decimal("8.45"),
              f"exponent = {exponent:.10f}")
        check(f"{label}: exp(-8.45)*2.435e18 = {approx_str} GeV at the printed digits, not 226",
              matches_printed(approx, approx_str) and approx > Decimal("1e14"),
              f"computed {approx:.6E}")

    # Control on the comparator itself: one unit off in the last digit fails.
    rejected = [name for name, val, s in printed if not matches_printed(val, one_unit_off(s))]
    check(f"{label}: control: every printed value moved by one last-digit unit is rejected",
          len(rejected) == len(printed),
          f"{len(rejected)}/{len(printed)} perturbed values rejected")


def main() -> int:
    print("=" * 78)
    print("HISTORIC HIERARCHY WRAPPERS: 2026-10-21 ARITHMETIC ANNOTATION CHECK")
    print("=" * 78)
    print("Scope: the annotation's arithmetic for its printed model only. Not the")
    print("historical claim below it, not the archived originals, not physics.")
    print(f"pi (Machin, Decimal) = {PI:.30f}")

    check("pi from Machin's formula agrees with its first 30 published digits",
          str(PI).startswith("3.141592653589793238462643383279"))
    check_note(AUDIT_INPUT_PATHS[0], "HONEST_REVIEW")
    check_note(AUDIT_INPUT_PATHS[1], "WHY_226")

    print()
    print("=" * 78)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 78)
    if FAIL_COUNT:
        print("The annotation's arithmetic does not match its printed values.")
        return 1
    print("The 2026-10-21 annotation's printed numbers match the recomputation for the")
    print("printed model. This says nothing about the historical claim or the physics.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
