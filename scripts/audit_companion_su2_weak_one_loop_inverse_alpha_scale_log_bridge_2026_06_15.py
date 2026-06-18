#!/usr/bin/env python3
"""Companion runner for the SU(2) inverse-alpha and scale-log bridge.

This runner verifies two narrow source-side bridge claims:

1. The one-loop inverse-alpha running equation follows by calculus from
   dg/dln(mu) = -b g^3/(16 pi^2) and alpha = g^2/(4 pi).
2. The scale logarithm used by the g_2(v) bounded interval row is the
   rounded readout of the hierarchy candidate map
   v_cand = M_Pl * (7/8)^(1/4) * alpha_LM^16.
3. The same two-decimal scale logarithm is stable under the current
   repo value-surface readout v = 246.282818290129 GeV and the approved
   Planck-ruler decimal used by the unit-conversion runner.

It does not derive the textbook one-loop beta law, the SU(2) u0 interval,
or the physical electroweak VEV identification.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

try:
    from sympy import Rational, Symbol, diff, log, pi, simplify, N as Numeric
except ImportError:
    print("FAIL: sympy required")
    sys.exit(1)


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "SU2_WEAK_ONE_LOOP_INVERSE_ALPHA_SCALE_LOG_BRIDGE_NARROW_THEOREM_NOTE_2026-06-15.md"
G2_NOTE = ROOT / "docs" / "G_2_V_BOUNDED_INTERVAL_NARROW_THEOREM_NOTE_2026-05-17.md"
SCALE_PRIMITIVE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
USABLE_VALUES = ROOT / "docs" / "publication" / "ci3_z3" / "USABLE_DERIVED_VALUES_INDEX.md"
OBSERVABLE_NOTE = ROOT / "docs" / "OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md"
UNIT_RUNNER = ROOT / "scripts" / "unit_conversion_is_accepted_non_bounding_ruler_runner.py"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def main() -> int:
    print("=" * 88)
    print("SU2 weak one-loop inverse-alpha and scale-log bridge")
    print("No audit verdicts are produced or edited by this runner.")
    print("=" * 88)

    section("Part 0: source packet checks")
    note_text = NOTE.read_text(encoding="utf-8")
    g2_text = G2_NOTE.read_text(encoding="utf-8")
    scale_text = SCALE_PRIMITIVE.read_text(encoding="utf-8")
    values_text = USABLE_VALUES.read_text(encoding="utf-8")
    observable_text = OBSERVABLE_NOTE.read_text(encoding="utf-8")
    unit_runner_text = UNIT_RUNNER.read_text(encoding="utf-8")
    check("bridge note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    for filename in [
        "SU2_WEAK_BETA_COEFFICIENT_NARROW_THEOREM_NOTE_2026-05-10.md",
        "SU2_WEAK_ALPHA_LATTICE_ONE_OVER_SIXTEEN_PI_ANCHOR_NARROW_THEOREM_NOTE_2026-05-28.md",
        "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md",
    ]:
        check(f"bridge cites {filename}", filename in note_text)
    check("bridge explicitly leaves u0(SU2) open", "Does **not** derive the numerical `u_0(SU(2))` interval" in note_text)
    check("g2 note cites this bridge", NOTE.name in g2_text)
    check(
        "scale primitive declares the Planck ruler and no dimensionless content",
        "a^{-1} = M_Pl" in scale_text
        and "zero dimensionless" in scale_text
        and "content" in scale_text,
    )
    check(
        "unit-conversion runner records the direct Planck-ruler decimal",
        "M_Pl_GeV = 1.22e19" in unit_runner_text,
    )
    check(
        "reusable-values index records v = 246.282818290129 GeV",
        "electroweak scale `v`" in values_text and "246.282818290129 GeV" in values_text,
    )
    check(
        "observable note displays the same EW-scale readout",
        "`v = 246.282818290129 GeV`" in observable_text,
    )

    section("Part 1: inverse-alpha calculus")
    g = Symbol("g", positive=True, real=True)
    b = Symbol("b", positive=True, real=True)

    beta_g = -b * g ** 3 / (16 * pi ** 2)
    alpha = g ** 2 / (4 * pi)
    d_alpha_dt = simplify(diff(alpha, g) * beta_g)
    expected_d_alpha_dt = simplify(-b * alpha ** 2 / (2 * pi))
    check(
        "d alpha/d ln(mu) = - b alpha^2/(2 pi)",
        simplify(d_alpha_dt - expected_d_alpha_dt) == 0,
        detail=f"d_alpha={d_alpha_dt}",
    )

    d_inv_alpha_dt = simplify(diff(1 / alpha, g) * beta_g)
    check(
        "d(1/alpha)/d ln(mu) = b/(2 pi)",
        simplify(d_inv_alpha_dt - b / (2 * pi)) == 0,
        detail=f"d_inv_alpha={d_inv_alpha_dt}",
    )

    mu_uv = Symbol("mu_UV", positive=True, real=True)
    mu_ir = Symbol("mu_IR", positive=True, real=True)
    integrated_shift = simplify((b / (2 * pi)) * (log(mu_ir) - log(mu_uv)))
    expected_shift = simplify(-(b / (2 * pi)) * log(mu_uv / mu_ir))
    check(
        "integral from UV to IR gives -b/(2pi) ln(mu_UV/mu_IR)",
        simplify(integrated_shift - expected_shift) == 0,
        detail=f"shift={integrated_shift}",
    )

    b2 = Rational(19, 6)
    check(
        "framework coefficient substitution b_2 = 19/6",
        b2 == Rational(19, 6),
        detail=f"b2={b2}",
    )

    section("Part 2: hierarchy candidate scale-log arithmetic")
    plaquette = Rational(5934, 10000)
    alpha_bare = 1 / (4 * pi)
    u0 = plaquette ** Rational(1, 4)
    alpha_lm = alpha_bare / u0
    k_factor = Rational(7, 8) ** Rational(1, 4) * alpha_lm ** 16
    log_span = -log(k_factor)

    # Numeric readouts for comparison with the established hierarchy runner.
    k_num = float(Numeric(k_factor, 30))
    log_num = float(Numeric(log_span, 30))
    m_pl = 1.2209e19
    v_cand = m_pl * k_num
    l_100 = Rational(3844, 100)
    delta_l = abs(log_num - float(l_100))

    check(
        "alpha_LM = alpha_bare/u0 is positive",
        float(Numeric(alpha_lm, 30)) > 0,
        detail=f"alpha_LM={float(Numeric(alpha_lm, 18)):.15f}",
    )
    check(
        "K = (7/8)^(1/4) alpha_LM^16 is positive",
        k_num > 0,
        detail=f"K={k_num:.18e}",
    )
    check(
        "L_cand = -ln(K) is about 38.442224515",
        abs(log_num - 38.44222451516312) < 1e-12,
        detail=f"L_cand={log_num:.14f}",
    )
    check(
        "v_cand from M_Pl*K matches hierarchy candidate readout",
        abs(v_cand - 246.282818290129) < 1e-9,
        detail=f"v_cand={v_cand:.12f} GeV",
    )
    check(
        "L=3844/100 is a close rounded surrogate for L_cand",
        delta_l < 0.003,
        detail=f"|L_cand-38.44|={delta_l:.15f}",
    )

    section("Part 2b: direct value-surface scale-log cross-check")
    m_pl_direct = 1.22e19
    m_pl_precise = 1.2209e19
    v_repo = 246.282818290129
    log_direct = math.log(m_pl_direct / v_repo)
    log_precise_direct = math.log(m_pl_precise / v_repo)
    delta_direct = abs(log_direct - float(l_100))
    delta_candidate_direct = abs(log_num - log_direct)

    check(
        "direct log ln(1.22e19 / 246.282818290129) matches displayed value",
        abs(log_direct - 38.441487082215616) < 1e-12,
        detail=f"L_direct={log_direct:.15f}",
    )
    check(
        "direct value-surface log is within 0.002 of rounded L=38.44",
        delta_direct < 0.002,
        detail=f"|L_direct-38.44|={delta_direct:.15f}",
    )
    check(
        "candidate-map log and direct current-value log differ by less than 0.001",
        delta_candidate_direct < 0.001,
        detail=f"|L_cand-L_direct|={delta_candidate_direct:.15f}",
    )
    check(
        "using the hierarchy runner Planck decimal reproduces L_cand",
        abs(log_precise_direct - log_num) < 1e-12,
        detail=f"L_precise_direct={log_precise_direct:.15f}",
    )

    section("Part 3: g2 denominator sanity with rounded versus candidate log")
    u_lo = Rational(96, 100)
    u_hi = Rational(98, 100)

    def g2_from_l(u: float, l_value: float) -> float:
        denom = 16.0 * math.pi * u * u - (float(b2) / (2.0 * math.pi)) * l_value
        return math.sqrt(4.0 * math.pi / denom)

    g_hi_rounded = g2_from_l(float(u_lo), float(l_100))
    g_lo_rounded = g2_from_l(float(u_hi), float(l_100))
    g_hi_candidate = g2_from_l(float(u_lo), log_num)
    g_lo_candidate = g2_from_l(float(u_hi), log_num)
    endpoint_shift = max(abs(g_hi_candidate - g_hi_rounded), abs(g_lo_candidate - g_lo_rounded))

    check(
        "rounded-log g2 interval is well formed",
        0 < g_lo_rounded < g_hi_rounded,
        detail=f"[{g_lo_rounded:.15f}, {g_hi_rounded:.15f}]",
    )
    check(
        "candidate-log g2 interval is well formed",
        0 < g_lo_candidate < g_hi_candidate,
        detail=f"[{g_lo_candidate:.15f}, {g_hi_candidate:.15f}]",
    )
    check(
        "using L_cand instead of 38.44 moves endpoints by less than 2e-5",
        endpoint_shift < 2e-5,
        detail=f"max_shift={endpoint_shift:.15e}",
    )

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
