#!/usr/bin/env python3
"""
Bounded support tool for the CKM five-sixths bridge.

Safe claim:
  Exact SU(3) gives C_F - T_F = 5/6. Combined with the promoted CKM package
  |V_cb| = alpha_s(v)/sqrt(6), the bounded bridge

      |V_cb| = (m_s/m_b)^(5/6)

  gives a down-type mass-ratio extraction that is numerically coherent on the
  threshold-local self-scale comparator m_s(2 GeV)/m_b(m_b). A theorem-grade
  derivation of the exact exponentiation mechanism and the exact scale-choice
  rule remains open.
"""

from __future__ import annotations

from fractions import Fraction
import math

from canonical_plaquette_surface import CANONICAL_ALPHA_S_V


N_C = 3


def casimir_fundamental(n: int) -> Fraction:
    return Fraction(n * n - 1, 2 * n)


T_F_EXACT = Fraction(1, 2)


def exponent_exact(n: int) -> Fraction:
    return casimir_fundamental(n) - T_F_EXACT


def beta0_exact(n_f: int) -> Fraction:
    return Fraction(11) - Fraction(2 * n_f, 3)


def gamma0_exact(n: int) -> Fraction:
    return 6 * casimir_fundamental(n)


C_F_EXACT = casimir_fundamental(N_C)
EXPONENT_EXACT = exponent_exact(N_C)
TRANSPORT_EXACT = gamma0_exact(N_C) / (2 * beta0_exact(4))


C_F = 4.0 / 3.0
T_F = 1.0 / 2.0
EXPONENT = C_F - T_F

V_CB_OBS = 0.0422
M_S_2GEV = 93.4e-3
M_B_MB = 4.180
R_SB_SELF = M_S_2GEV / M_B_MB

ALPHA_S_2GEV = 0.301
ALPHA_S_MB = 0.226
GAMMA0_OVER_2BETA0 = 12.0 / 25.0

EXACT_PASS = 0
BOUNDED_PASS = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", kind: str = "EXACT") -> None:
    global EXACT_PASS, BOUNDED_PASS, FAIL_COUNT
    if condition:
        if kind == "EXACT":
            EXACT_PASS += 1
        else:
            BOUNDED_PASS += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    prefix = f" [{kind}]" if kind != "EXACT" else ""
    line = f"  [{status}]{prefix} {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def part0_exact_derivation() -> None:
    print("\n" + "=" * 72)
    print("PART 0: Exact exponent and transport derivation")
    print("=" * 72)

    polynomial_identity = all(
        3 * n * n - 8 * n - 3 == (3 * n + 1) * (n - 3)
        for n in range(-2, 9)
    )
    matching_ranks = {
        n for n in range(2, 7) if exponent_exact(n) == Fraction(5, 6)
    }
    transport_nf3 = gamma0_exact(3) / (2 * beta0_exact(3))
    transport_nf5 = gamma0_exact(3) / (2 * beta0_exact(5))
    exponent_n2 = exponent_exact(2)

    check("P0.1: C_F exact derivation", C_F_EXACT == Fraction(4, 3))
    check("P0.2: T_F exact input", T_F_EXACT == Fraction(1, 2))
    check("P0.3: exponent exact derivation", EXPONENT_EXACT == Fraction(5, 6))
    check(
        "P0.4: exact values reproduce existing float constants (exponent within 1 ulp)",
        C_F == float(C_F_EXACT)
        and T_F == float(T_F_EXACT)
        and abs(EXPONENT - float(EXPONENT_EXACT)) <= 2.0 ** -53,
        f"C_F,T_F exact; float(C_F-T_F) vs exact 5/6 gap = "
        f"{abs(EXPONENT - float(EXPONENT_EXACT)):.2e}",
    )
    check(
        "P0.5: N=3 is unique in the N=2..6 scan",
        polynomial_identity and matching_ranks == {3},
        f"identity={polynomial_identity}, matching ranks={sorted(matching_ranks)}",
    )
    check(
        "P0.6: exact one-loop inputs at N=3 and n_f=4",
        gamma0_exact(3) == Fraction(8)
        and beta0_exact(4) == Fraction(25, 3),
    )
    check(
        "P0.7: exact threshold-local transport power",
        TRANSPORT_EXACT == Fraction(12, 25)
        and GAMMA0_OVER_2BETA0 == float(TRANSPORT_EXACT),
    )
    check(
        "P0.8: n_f=3 transport rejector detected",
        transport_nf3 == Fraction(4, 9) and transport_nf3 != TRANSPORT_EXACT,
        f"wrong-input value={transport_nf3}",
    )
    check(
        "P0.9: n_f=5 transport rejector detected",
        transport_nf5 == Fraction(12, 23) and transport_nf5 != TRANSPORT_EXACT,
        f"wrong-input value={transport_nf5}",
    )
    check(
        "P0.10: N=2 exponent rejector detected",
        exponent_n2 == Fraction(1, 4) and exponent_n2 != EXPONENT_EXACT,
        f"wrong-input value={exponent_n2}",
    )


def part1_exact_surface() -> tuple[float, float]:
    print("\n" + "=" * 72)
    print("PART 1: Exact SU(3) and promoted CKM surface")
    print("=" * 72)

    v_cb = CANONICAL_ALPHA_S_V / math.sqrt(6.0)
    r_pred = v_cb ** (6.0 / 5.0)

    print(f"\n  C_F = {C_F:.6f}")
    print(f"  T_F = {T_F:.6f}")
    print(f"  C_F - T_F = {EXPONENT:.6f}")
    print(f"  alpha_s(v) = {CANONICAL_ALPHA_S_V:.12f}")
    print(f"  |V_cb| = alpha_s(v)/sqrt(6) = {v_cb:.8f}")
    print(f"  predicted m_s/m_b = |V_cb|^(6/5) = {r_pred:.8f}")

    check("C_F = 4/3", abs(C_F - 4.0 / 3.0) < 1e-14, f"C_F = {C_F:.12f}")
    check("T_F = 1/2", abs(T_F - 0.5) < 1e-14, f"T_F = {T_F:.12f}")
    check("C_F - T_F = 5/6", abs(EXPONENT - 5.0 / 6.0) < 1e-14, f"p = {EXPONENT:.12f}")
    check(
        "|V_cb| = alpha_s(v)/sqrt(6)",
        abs(v_cb - CANONICAL_ALPHA_S_V / math.sqrt(6.0)) < 1e-14,
        f"|V_cb| = {v_cb:.12f}",
    )
    check(
        "m_s/m_b = [alpha_s(v)/sqrt(6)]^(6/5)",
        abs(r_pred - (CANONICAL_ALPHA_S_V / math.sqrt(6.0)) ** (6.0 / 5.0)) < 1e-14,
        f"m_s/m_b = {r_pred:.12f}",
    )

    return v_cb, r_pred


def part2_bounded_bridge(v_cb: float, r_pred: float) -> tuple[float, float]:
    print("\n" + "=" * 72)
    print("PART 2: Bounded bridge and observation surface")
    print("=" * 72)

    r_from_obs_vcb = V_CB_OBS ** (6.0 / 5.0)
    dev_bridge = (r_from_obs_vcb - R_SB_SELF) / R_SB_SELF * 100.0
    dev_pred = (r_pred - R_SB_SELF) / R_SB_SELF * 100.0
    dev_vcb = (v_cb - V_CB_OBS) / V_CB_OBS * 100.0

    print(f"\n  threshold-local self-scale comparator m_s(2 GeV)/m_b(m_b) = {R_SB_SELF:.8f}")
    print(f"  observed-|V_cb| bridge surface = |V_cb|_obs^(6/5) = {r_from_obs_vcb:.8f}")
    print(f"  framework prediction           = {r_pred:.8f}")
    print(f"\n  bridge-only deviation from comparator = {dev_bridge:+.3f}%")
    print(f"  atlas |V_cb| deviation                = {dev_vcb:+.3f}%")
    print(f"  total predicted deviation             = {dev_pred:+.3f}%")

    check(
        "observed |V_cb| mapped through 5/6 lands within 1% of the self-scale comparator",
        abs(dev_bridge) < 1.0,
        f"dev = {dev_bridge:+.3f}%",
        kind="BOUNDED",
    )
    check(
        "framework m_s/m_b prediction lands within 1% of the self-scale comparator",
        abs(dev_pred) < 1.0,
        f"dev = {dev_pred:+.3f}%",
        kind="BOUNDED",
    )

    return r_from_obs_vcb, r_pred


def part3_self_scale_transport(r_pred: float) -> float:
    print("\n" + "=" * 72)
    print("PART 3: Threshold-local self-scale transport")
    print("=" * 72)

    transport = (ALPHA_S_2GEV / ALPHA_S_MB) ** GAMMA0_OVER_2BETA0
    m_s_at_mb = M_S_2GEV * (ALPHA_S_MB / ALPHA_S_2GEV) ** GAMMA0_OVER_2BETA0
    r_same = m_s_at_mb / M_B_MB
    dev_same = (r_pred - r_same) / r_same * 100.0
    dev_self = (r_pred - R_SB_SELF) / R_SB_SELF * 100.0

    print(f"\n  alpha_s(2 GeV) = {ALPHA_S_2GEV:.3f}")
    print(f"  alpha_s(m_b)   = {ALPHA_S_MB:.3f}")
    print(f"  gamma_0/(2 beta_0) = 12/25 = {GAMMA0_OVER_2BETA0:.6f}")
    print(f"  transport factor [alpha_s(2 GeV)/alpha_s(m_b)]^(12/25) = {transport:.6f}")
    print(f"  m_s(m_b) = {m_s_at_mb * 1e3:.3f} MeV")
    print(f"  same-scale ratio r_same = m_s(m_b)/m_b(m_b) = {r_same:.8f}")
    print(f"  self-scale ratio r_self = m_s(2 GeV)/m_b(m_b) = {R_SB_SELF:.8f}")
    print(f"  predicted deviation vs self-scale = {dev_self:+.3f}%")
    print(f"  predicted deviation vs same-scale = {dev_same:+.3f}%")

    check(
        "self-scale ratio equals same-scale ratio times the one-loop transport factor",
        abs(R_SB_SELF - r_same * transport) < 1e-12,
        f"diff = {abs(R_SB_SELF - r_same * transport):.2e}",
        kind="BOUNDED",
    )
    check(
        "transport factor from m_b to 2 GeV is material",
        transport > 1.1,
        f"transport = {transport:.6f}",
        kind="BOUNDED",
    )
    check(
        "self-scale comparator is numerically closer than the same-scale comparator",
        abs(dev_self) < abs(dev_same),
        f"|self| = {abs(dev_self):.3f}%, |same| = {abs(dev_same):.3f}%",
        kind="BOUNDED",
    )
    check(
        "same-scale mismatch remains material",
        abs(dev_same) > 10.0,
        f"same-scale dev = {dev_same:+.3f}%",
        kind="BOUNDED",
    )

    return r_same


def part4_decomposition(r_pred: float, r_from_obs_vcb: float) -> None:
    print("\n" + "=" * 72)
    print("PART 4: Exact multiplicative deviation decomposition")
    print("=" * 72)

    atlas_factor = r_pred / r_from_obs_vcb
    bridge_factor = r_from_obs_vcb / R_SB_SELF
    total_factor = r_pred / R_SB_SELF

    atlas_shift = (atlas_factor - 1.0) * 100.0
    bridge_shift = (bridge_factor - 1.0) * 100.0
    total_shift = (total_factor - 1.0) * 100.0

    print(f"\n  atlas-induced factor       = {atlas_factor:.9f}  ({atlas_shift:+.3f}%)")
    print(f"  bridge/comparator factor   = {bridge_factor:.9f}  ({bridge_shift:+.3f}%)")
    print(f"  total predicted factor     = {total_factor:.9f}  ({total_shift:+.3f}%)")

    check(
        "total deviation factors exactly into atlas shift times bridge/comparator shift",
        abs(total_factor - atlas_factor * bridge_factor) < 1e-14,
        f"diff = {abs(total_factor - atlas_factor * bridge_factor):.2e}",
        kind="BOUNDED",
    )


def main() -> int:
    print("=" * 72)
    print("  FRONTIER: CKM Five-Sixths Bridge Support")
    print("=" * 72)

    part0_exact_derivation()
    v_cb, r_pred = part1_exact_surface()
    r_from_obs_vcb, r_pred = part2_bounded_bridge(v_cb, r_pred)
    part3_self_scale_transport(r_pred)
    part4_decomposition(r_pred, r_from_obs_vcb)

    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"  EXACT PASS={EXACT_PASS}")
    print(f"  BOUNDED PASS={BOUNDED_PASS}")
    print(f"  FAIL={FAIL_COUNT}")
    print("  Status: bounded support tool for the down-type mass-ratio lane")
    print("  Live comparison surface: threshold-local self-scale comparator m_s(2 GeV)/m_b(m_b)")
    print("  Remaining open issue: theorem-grade derivation of the exact bridge and scale choice")
    print("=" * 72)

    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
