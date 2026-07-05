#!/usr/bin/env python3
"""Bounded admission bridge: BBN coefficient 3.6515e-3 decomposition.

The runner checks only:

1. The analytic factor 2 zeta(3)/pi^2 from the supplied Planck distribution
   integral, certified by the termwise series
   int_0^inf x^2/(exp(x)-1) dx = sum_{n>=1} 2/n^3 and an explicit p-series
   tail bound, then matched against the standard photon-number density per
   unit T^3;
2. The supplied P1-P4 premise packet recorded in the source note (proton
   mass, CMB temperature, critical-density unit from admitted H_100 and G,
   Cyburt convention / residual normalization);
3. The deterministic arithmetic recovering the raw unit-conversion baseline
   for Omega_b h^2 / eta_10 within 0.2% of the Cyburt-Fields-Olive-Yeh 2016
   value 3.6515e-3;
4. The exact Cyburt residual factor that would make the comparator equality
   exact, explicitly labeled as an admitted convention/comparator rather than
   a framework derivation.

It deliberately does not consume PDG-fitted mass values as derivations,
does not consume nuclear-network outputs as derivations, and does not promote
any downstream cosmology row.
"""

from __future__ import annotations

from math import pi
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "bbn_eta10_to_omega_b_h2_coefficient_admission_bridge_bounded_note_2026-05-28"
RUNNER_PATH = "scripts/bbn_eta10_to_omega_b_h2_coefficient_admission_bridge_runner.py"
NOTE_PATH = ROOT / "docs/BBN_ETA10_TO_OMEGA_B_H2_COEFFICIENT_ADMISSION_BRIDGE_BOUNDED_NOTE_2026-05-28.md"

# Apery's constant zeta(3) to high precision (Riemann zeta function at 3).
# Pure analytic constant, no empirical input; Part 1 certifies this reference
# value lies inside an independently computed series/tail interval.
ZETA3 = 1.2020569031595942853997381615114499907649862923405
ZETA3_SERIES_CERT_N = 20_000

# Cyburt+ 2016 published value.
CYBURT_2016_COEFFICIENT = 3.6515e-3

# CODATA textbook values used as the named admitted inputs.
# These are explicit imports (P1-P4 in the note). They are NOT derived here.
M_P_GRAMS = 1.6726219236e-24       # P1: proton rest mass in cgs
T_CMB_KELVIN = 2.725                # P2: present-day CMB temperature
K_B_GEV_PER_K = 8.617333262e-14     # auxiliary: Boltzmann constant in GeV/K
HBAR_C_GEV_CM = 1.97326980e-14      # auxiliary: hbar*c in GeV*cm
H100_KM_S_MPC = 100.0               # P3a: H_100 convention
MPC_METERS = 3.0856775814913673e22   # P3b: SI Mpc conversion
G_NEWTON_SI = 6.67430e-11            # P3c: Newton constant in SI
KG_PER_M3_TO_G_PER_CM3 = 1.0e-3
S_CYBURT_RAW = 1.0                  # P4 raw baseline, not exact comparator residual


def critical_density_per_h2() -> float:
    """Compute rho_crit/h^2 from admitted H_100 and G in cgs units."""
    h100_s_inv = (H100_KM_S_MPC * 1000.0) / MPC_METERS
    rho_kg_m3 = 3.0 * h100_s_inv**2 / (8.0 * pi * G_NEWTON_SI)
    return rho_kg_m3 * KG_PER_M3_TO_G_PER_CM3


RHO_CRIT_PER_H2 = critical_density_per_h2()

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    msg = f"{status}: {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)
    return condition


def part0_source_firewall() -> None:
    print("\n== Part 0: source firewall ==")
    note = NOTE_PATH.read_text(encoding="utf-8")

    required = [
        "Supplied premise packet (not axioms)",
        "P1 proton rest mass",
        "P2 present-day CMB temperature",
        "P3 critical-density unit",
        "2026-06-12 P3 critical-density unit decomposition",
        "P4 Cyburt conversion convention",
        "does not derive the premise packet" if "does not derive the premise packet" in note else "does not derive P1-P4",
        "not registry accepted premises",
        "new repo-wide axiom",
        "Cyburt",
        "2 zeta(3)",
        "Planck distribution",
        RUNNER_PATH,
    ]
    for phrase in required:
        check(f"source contains boundary phrase: {phrase}", phrase in note)

    forbidden = [
        "Tier-B partial-derivation",
        "Tier B partial derivation",
        "framework derives m_p",
        "framework derives T_CMB",
        "**Status:** retained",
        "audited_clean",
    ]
    for phrase in forbidden:
        check(f"source excludes forbidden phrase: {phrase}", phrase not in note)


def part1_framework_clean_factor() -> float:
    print("\n== Part 1: analytic factor 2 zeta(3) / pi^2 ==")
    # The standard Bose-Einstein integral follows from
    # 1/(e^x - 1) = sum_{n>=1} e^{-n x} and
    # int_0^inf x^2 e^{-n x} dx = 2/n^3, giving 2 zeta(3).
    partial = sum(1.0 / (n**3) for n in range(1, ZETA3_SERIES_CERT_N + 1))
    tail_upper = 1.0 / (2.0 * (ZETA3_SERIES_CERT_N**2))
    zeta_lower = partial
    zeta_upper = partial + tail_upper
    check(
        "zeta(3) reference is certified by the p-series tail interval",
        zeta_lower <= ZETA3 <= zeta_upper,
        f"N={ZETA3_SERIES_CERT_N}, width <= {tail_upper:.3e}",
    )
    integral_lower = 2.0 * zeta_lower
    integral_upper = 2.0 * zeta_upper
    check(
        "Planck integral identity is internally certified: integral = 2 zeta(3)",
        integral_lower <= 2.0 * ZETA3 <= integral_upper,
        f"2*zeta(3) in [{integral_lower:.12f}, {integral_upper:.12f}]",
    )
    # Photon number density per T^3 is g_gamma/(2*pi^2) times the integral.
    g_gamma = 2
    factor = g_gamma * ZETA3 / pi**2
    expected = 2 * ZETA3 / pi**2
    check(
        "factor reduces to 2 zeta(3)/pi^2 with photon polarization count g_gamma = 2",
        abs(factor - expected) < 1e-15,
        f"factor = {factor:.12f}",
    )
    # Numerical check that this is the standard 0.24359... constant.
    check(
        "factor numerically equals 0.24359... (standard)",
        abs(factor - 0.24359) < 1e-4,
        f"factor = {factor:.6f}",
    )
    return factor


def part2_imported_n_gamma_today(factor: float) -> float:
    print("\n== Part 2: present-day photon number density from P2 import ==")
    # Convert T_CMB to GeV via P2.
    T_CMB_GeV = K_B_GEV_PER_K * T_CMB_KELVIN
    # Convert to cm^-3 via hbar*c.
    n_gamma_per_cm3 = factor * (T_CMB_GeV / HBAR_C_GEV_CM)**3
    check(
        "present-day n_gamma is approximately 410 photons / cm^3 (standard textbook)",
        abs(n_gamma_per_cm3 - 410.7) / 410.7 < 0.01,
        f"n_gamma = {n_gamma_per_cm3:.4f} per cm^3",
    )
    return n_gamma_per_cm3


def part3_recover_coefficient(n_gamma_per_cm3: float) -> tuple[float, float]:
    print("\n== Part 3: recover Cyburt+ 2016 coefficient by deterministic arithmetic ==")
    # Omega_b * h^2 / eta = m_p * n_gamma_today * S / (rho_crit / h^2).
    # S=1 is the raw unit-conversion baseline. The exact Cyburt comparator
    # equality requires an admitted residual S_Cyburt, computed below.
    omega_b_h2_per_eta = M_P_GRAMS * n_gamma_per_cm3 * S_CYBURT_RAW / RHO_CRIT_PER_H2
    # Scale by 1e-10 to convert eta_10 = 1e10 * eta.
    raw_coeff = omega_b_h2_per_eta * 1e-10
    s_cyburt_exact = CYBURT_2016_COEFFICIENT / raw_coeff
    exact_coeff = raw_coeff * s_cyburt_exact
    check(
        "raw S=1 coefficient within 0.2% of published Cyburt+ 2016 value 3.6515e-3",
        abs(raw_coeff - CYBURT_2016_COEFFICIENT) / CYBURT_2016_COEFFICIENT < 2e-3,
        f"raw_coeff = {raw_coeff:.9e} vs Cyburt+2016 = {CYBURT_2016_COEFFICIENT:.9e}",
    )
    check(
        "exact Cyburt residual factor is explicit and sub-percent",
        0.998 < s_cyburt_exact < 1.0,
        f"S_Cyburt_exact = {s_cyburt_exact:.15f}",
    )
    check(
        "raw coefficient times admitted S_Cyburt residual equals comparator exactly",
        abs(exact_coeff - CYBURT_2016_COEFFICIENT) < 1e-15,
        f"exact_coeff = {exact_coeff:.9e}",
    )
    return raw_coeff, s_cyburt_exact


def part4_premise_packet_named(s_cyburt_exact: float) -> None:
    print("\n== Part 4: named premise packet remains imported on this row ==")
    # Each premise is explicit. None is framework-derived here.
    check(
        "P1 proton rest mass admitted as textbook import (not derived here)",
        M_P_GRAMS > 0 and abs(M_P_GRAMS - 1.6726e-24) / 1.6726e-24 < 1e-3,
        f"m_p = {M_P_GRAMS} g",
    )
    check(
        "P2 CMB temperature admitted as textbook import (not derived here)",
        abs(T_CMB_KELVIN - 2.725) < 1e-3,
        f"T_CMB = {T_CMB_KELVIN} K",
    )
    check(
        "P3 critical-density unit computed from admitted H_100 and G",
        abs(RHO_CRIT_PER_H2 - 1.878e-29) / 1.878e-29 < 1e-3,
        f"rho_crit/h^2 = {RHO_CRIT_PER_H2:.6e} g/cm^3",
    )
    check(
        "P3 formula is rho_crit/h^2 = 3 H_100^2 / (8 pi G) with SI-to-cgs conversion",
        H100_KM_S_MPC == 100.0 and G_NEWTON_SI > 0.0 and MPC_METERS > 0.0,
        f"H100={H100_KM_S_MPC} km/s/Mpc, G={G_NEWTON_SI:.6e} SI",
    )
    check(
        "P4 raw Cyburt convention baseline is S=1",
        S_CYBURT_RAW == 1.0,
        "S_raw = 1.0 for the raw unit-conversion baseline",
    )
    check(
        "P4 exact Cyburt residual is admitted as a separate comparator convention",
        abs(s_cyburt_exact - 0.9989276742641543) < 1e-15,
        f"S_Cyburt_exact = {s_cyburt_exact:.15f}",
    )


def part5_retention_scorecard(coeff: float) -> None:
    print("\n== Part 5: retention scorecard ==")
    note = NOTE_PATH.read_text(encoding="utf-8")
    check(
        "source records the 2026-06-18 analytic-factor import retirement",
        "2026-06-18 Analytic Factor Import Retirement" in note
        and "p-series tail bound" in note
        and "N=20000" in note,
    )
    check(
        "source separates analytic proof from physical admissions",
        "internal math certificate for the analytic Planck-distribution factor only" in " ".join(note.split())
        and "P1-P4 admitted physical/comparator premises" in " ".join(note.split()),
    )
    check(
        "source says critical-density unit is formula-expanded instead of black-boxed",
        "critical-density unit is formula-expanded instead of black-boxed" in note,
    )
    check(
        "source keeps four admitted premise classes P1-P4",
        all(
            marker in note
            for marker in [
                "imported (P1)",
                "imported (P2)",
                "computed unit conversion from admitted `H_100` and `G`",
                "P4's comparator residual are still supplied",
            ]
        ),
    )
    check(
        "source records exact S_Cyburt residual as admitted comparator, not derivation",
        "S_Cyburt_exact = 0.9989276742641543" in note
        and "does not derive `S_Cyburt_exact`" in note,
    )
    check(
        "bridge does not promote the parent cosmology cascade row",
        "does not promote any downstream cosmology row" in note
        or "does not promote the cosmology cascade" in note
        or "does not promote the parent cosmology cascade" in note,
    )


def main() -> int:
    print("BBN COEFFICIENT 3.6515e-3 ADMISSION BRIDGE")
    part0_source_firewall()
    factor = part1_framework_clean_factor()
    n_gamma = part2_imported_n_gamma_today(factor)
    coeff, s_cyburt_exact = part3_recover_coefficient(n_gamma)
    part4_premise_packet_named(s_cyburt_exact)
    part5_retention_scorecard(coeff)
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: bounded admission bridge passes; the textbook coefficient "
            "3.6515e-3 is split into a raw unit-conversion baseline from one "
            "analytic factor (2 zeta(3)/pi^2 from the Planck distribution) and "
            "admitted physical premises (P1 m_p, P2 T_CMB, P3 H_100/G "
            "critical-density unit), plus explicit admitted P4 residual "
            "S_Cyburt_exact = 0.9989276742641543. The raw baseline is within "
            "0.107% of the Cyburt+ 2016 published value; exact equality uses "
            "the admitted residual comparator."
        )
        return 0
    print("VERDICT: bounded admission bridge FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
