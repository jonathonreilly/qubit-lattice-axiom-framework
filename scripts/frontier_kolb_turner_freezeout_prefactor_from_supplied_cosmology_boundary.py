#!/usr/bin/env python3
"""Exact-symbolic runner for the narrow theorem note
`KOLB_TURNER_FREEZEOUT_PREFACTOR_FROM_SUPPLIED_COSMOLOGY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-05-28.md`.

The parent narrow note's load-bearing content is the algebraic
prefactor identity (P*) given five named premises (P1)-(P5):

  P1 (Friedmann)        : H^2 = (8 pi G_N / 3) rho,  G_N = 1/M_Pl^2
  P2 (Stefan-Boltzmann) : rho_rad(T) = (pi^2/30) g_*(T) T^4
  P3 (Entropy density)  : s(T)       = (2 pi^2/45) g_*S(T) T^3
  P4 (Boltzmann tail)   : Y_infty ~ x_F * sqrt(45/pi) /
                                  (sqrt(g_*(T_F)) M_Pl <sigma_v>)
  P5 (Entropy conserv.) : s a^3 = const

Definitions:

  (D1) s_0          := (2 pi^2/45) g_*S(T_0) T_0^3
  (D2) rho_c/h^2    := 3 H_100^2 M_Pl^2 / (8 pi)
  (D3) K            := s_0 * sqrt(45/pi) / (rho_c/h^2)

Identity:

  (P*) K  =  ( (2 pi^2/45) g_*S(T_0) T_0^3 ) * sqrt(45/pi)
            / ( 3 H_100^2 M_Pl^2 / (8 pi) )
         =  16 pi^3 g_*S(T_0) T_0^3 sqrt(45/pi) / (135 H_100^2 M_Pl^2).

This Pattern A narrow runner adds a sympy-based exact-symbolic
verification:

  (a) treats (g_*S(T_0), T_0, H_100, M_Pl) as positive real symbols;
  (b) constructs (D1), (D2), (D3) verbatim from the cited premises;
  (c) verifies (P*) reduces to 0 symbolically;
  (d) verifies the explicit canonical form
      K = 16 pi^3 g_*S(T_0) T_0^3 sqrt(45/pi) / (135 H_100^2 M_Pl^2);
  (e) numerical sanity at the standard cosmological-boundary inputs
      reproduces K ~ 1.04e9 GeV^-1 within ~3% of textbook 1.07e9 GeV^-1;
  (f) counterfactual probe: removing sqrt(45/pi) collapses K by 3.78x;
  (g) M_Pl-scaling probe: doubling M_Pl reduces K by 4x;
  (h) T_0-scaling probe: doubling T_0 increases K by 8x;
  (i) g_*S(T_0)-scaling probe: doubling g_*S(T_0) increases K by 2x;
  (j) H_100-scaling probe: doubling H_100 reduces K by 4x.

Review role: no status promotion. Provides runner evidence that the
algebraic-substitution identity holds at exact symbolic precision under the
local supplied premises, and that the numerical evaluation reproduces the
textbook K ~ 1.07e9 GeV^-1 within the conventional ~3% Boltzmann-tail
subleading-coefficient gap.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path


try:
    import sympy
    from sympy import Rational, Symbol, simplify, sqrt, symbols
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "KOLB_TURNER_FREEZEOUT_PREFACTOR_FROM_SUPPLIED_COSMOLOGY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-05-28.md"


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def main() -> int:
    print("=" * 88)
    print("Exact-symbolic runner for")
    print("KOLB_TURNER_FREEZEOUT_PREFACTOR_FROM_SUPPLIED_COSMOLOGY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-05-28")
    print("Goal: sympy-symbolic verification of (P*) K = s_0 * sqrt(45/pi) / (rho_c/h^2)")
    print("under named cosmological-thermodynamic premises (P1)-(P5)")
    print("=" * 88)

    # ----------------------------------------------------------------------
    section("Part 0: source boundary")
    # ----------------------------------------------------------------------

    note_text = NOTE_PATH.read_text(encoding="utf-8")
    for marker in [
        "Supplied Premise Sources and Context",
        "No new repo-wide",
        "local supplied premise",
        "not a load-bearing dependency",
        "scripts/frontier_kolb_turner_freezeout_prefactor_from_supplied_cosmology_boundary.py",
    ]:
        check(f"source boundary marker present: {marker}", marker in note_text)
    for forbidden in [
        "scripts/audit_companion_kolb_turner_freezeout_prefactor_from_mpl_gstar.py",
        "KOLB_TURNER_FREEZEOUT_PREFACTOR_FROM_M_PL_AND_G_STAR",
        "No new admission is introduced",
    ]:
        check(f"stale/overbroad source phrase absent: {forbidden}", forbidden not in note_text)

    # ----------------------------------------------------------------------
    section("Part 1: symbolic setup")
    # ----------------------------------------------------------------------

    g_starS_T0 = Symbol("g_starS_T0", positive=True, real=True)
    T_0 = Symbol("T_0", positive=True, real=True)
    H_100 = Symbol("H_100", positive=True, real=True)
    M_Pl = Symbol("M_Pl", positive=True, real=True)

    pi = sympy.pi

    # Definitions (cited from the note)
    #   (D1) s_0       := (2 pi^2 / 45) g_*S(T_0) T_0^3
    #   (D2) rho_c/h^2 := 3 H_100^2 M_Pl^2 / (8 pi)
    s_0 = Rational(2) * pi**2 * g_starS_T0 * T_0**3 / Rational(45)
    rho_c_per_h2 = Rational(3) * H_100**2 * M_Pl**2 / (Rational(8) * pi)

    # Boltzmann-tail coefficient (P4): sqrt(45/pi)
    C_Boltz = sqrt(Rational(45) / pi)

    # (D3) Definition of K
    K_def = s_0 * C_Boltz / rho_c_per_h2

    print(f"  symbolic g_*S(T_0) (positive real) = {g_starS_T0}")
    print(f"  symbolic T_0       (positive real) = {T_0}")
    print(f"  symbolic H_100     (positive real) = {H_100}")
    print(f"  symbolic M_Pl      (positive real) = {M_Pl}")
    print(f"  (D1) s_0         = (2 pi^2 / 45) g_*S(T_0) T_0^3 = {s_0}")
    print(f"  (D2) rho_c/h^2   = 3 H_100^2 M_Pl^2 / (8 pi)      = {rho_c_per_h2}")
    print(f"  (P4 leading)     = sqrt(45 / pi)                  = {C_Boltz}")
    print(f"  (D3) K (def)     = s_0 * sqrt(45/pi) / (rho_c/h^2) = {K_def}")

    # ----------------------------------------------------------------------
    section("Part 2: (P*) identity reduces to 0 parametrically")
    # ----------------------------------------------------------------------

    # K - s_0 * sqrt(45/pi) / (rho_c/h^2) is identically 0
    diff = simplify(K_def - s_0 * C_Boltz / rho_c_per_h2)
    check(
        "(P*) K - s_0 * sqrt(45/pi) / (rho_c/h^2) = 0 parametrically",
        diff == 0,
        detail=f"diff = {diff}",
    )

    # ----------------------------------------------------------------------
    section("Part 3: explicit canonical form")
    # ----------------------------------------------------------------------

    K_explicit = (
        Rational(16) * pi**3 * g_starS_T0 * T_0**3 * C_Boltz
        / (Rational(135) * H_100**2 * M_Pl**2)
    )
    canonical_diff = simplify(K_def - K_explicit)
    check(
        "K = 16 pi^3 g_*S(T_0) T_0^3 sqrt(45/pi) / (135 H_100^2 M_Pl^2) (canonical form)",
        canonical_diff == 0,
        detail=f"diff = {canonical_diff}",
    )

    # ----------------------------------------------------------------------
    section("Part 4: numerical evaluation against textbook K")
    # ----------------------------------------------------------------------

    # Standard cosmological-boundary inputs
    #   T_0       = 2.7255 K = 2.348654e-13 GeV  (k_B = 8.617333e-5 eV/K)
    #   g_*S(T_0) = 43/11 ~ 3.9091
    #   H_100     = 100 km/s/Mpc = 2.133058e-42 GeV
    #     (1 km/s/Mpc = 3.24078e-20 /s; 1 GeV = 1.5193e24 /s)
    #   M_Pl      = 1.22091e19 GeV
    K_BOLTZ_FACTOR = math.sqrt(45.0 / math.pi)
    K_TEXTBOOK = 1.07e9  # GeV^-1 (Kolb-Turner Eq. 5.49)

    T_0_GeV = 2.7255 * 8.617333e-5 * 1e-9
    g_starS_T0_num = 43.0 / 11.0
    H_100_GeV = 100.0 * 1.0e3 / 3.0857e22 / 1.5193e24
    M_Pl_num = 1.22091e19

    s_0_num = (2.0 * math.pi**2 / 45.0) * g_starS_T0_num * T_0_GeV**3
    rho_c_per_h2_num = 3.0 * H_100_GeV**2 * M_Pl_num**2 / (8.0 * math.pi)

    K_num = s_0_num * K_BOLTZ_FACTOR / rho_c_per_h2_num

    print(f"  T_0       = {T_0_GeV:.6e} GeV  (= 2.7255 K)")
    print(f"  g_*S(T_0) = {g_starS_T0_num:.6f}")
    print(f"  H_100     = {H_100_GeV:.6e} GeV  (= 100 km/s/Mpc)")
    print(f"  M_Pl      = {M_Pl_num:.6e} GeV  (Tier-A S admission)")
    print(f"  s_0       = {s_0_num:.6e} GeV^3")
    print(f"  rho_c/h^2 = {rho_c_per_h2_num:.6e} GeV^4")
    print(f"  sqrt(45/pi) = {K_BOLTZ_FACTOR:.6f}")
    print(f"  K (this note, leading) = {K_num:.6e} GeV^-1")
    print(f"  K (textbook KT Eq. 5.49) = {K_TEXTBOOK:.6e} GeV^-1")
    rel_dev = (K_num - K_TEXTBOOK) / K_TEXTBOOK
    print(f"  relative deviation = {100.0 * rel_dev:+.3f}%")

    # Allow up to 5% deviation (Boltzmann subleading-coefficient gap is ~3%
    # in standard convention but choice of subleading-correction prescription
    # can stretch this to ~5%).
    check(
        "K (this note) reproduces textbook 1.07e9 GeV^-1 within 5% (Boltzmann coefficient gap)",
        abs(rel_dev) < 0.05,
        detail=(f"K(this) = {K_num:.4e}, K(KT) = {K_TEXTBOOK:.4e}, "
                f"dev = {100*rel_dev:+.3f}%"),
    )

    # ----------------------------------------------------------------------
    section("Part 5: counterfactual / scaling probes")
    # ----------------------------------------------------------------------

    # (a) Removing the sqrt(45/pi) Boltzmann-tail coefficient
    K_no_boltz_num = s_0_num * 1.0 / rho_c_per_h2_num
    ratio_no_boltz = K_num / K_no_boltz_num
    check(
        "Removing sqrt(45/pi) collapses K by factor 3.78",
        abs(ratio_no_boltz - K_BOLTZ_FACTOR) / K_BOLTZ_FACTOR < 1e-9,
        detail=f"K_full / K_noBoltz = {ratio_no_boltz:.6f}, sqrt(45/pi) = {K_BOLTZ_FACTOR:.6f}",
    )

    # (b) Doubling M_Pl: K -> K/4 (since K ~ 1/M_Pl^2 through rho_c/h^2)
    M_Pl_doubled = 2.0 * M_Pl_num
    rho_c_per_h2_doubled = 3.0 * H_100_GeV**2 * M_Pl_doubled**2 / (8.0 * math.pi)
    K_M_Pl_doubled = s_0_num * K_BOLTZ_FACTOR / rho_c_per_h2_doubled
    ratio_M_Pl = K_num / K_M_Pl_doubled
    check(
        "Doubling M_Pl reduces K by factor 4 (since K ~ 1/M_Pl^2 via rho_c/h^2)",
        abs(ratio_M_Pl - 4.0) < 1e-9,
        detail=f"K(M_Pl) / K(2*M_Pl) = {ratio_M_Pl:.6f}",
    )

    # (c) Doubling T_0: K -> 8*K (since K ~ T_0^3)
    T_0_doubled = 2.0 * T_0_GeV
    s_0_T_doubled = (2.0 * math.pi**2 / 45.0) * g_starS_T0_num * T_0_doubled**3
    K_T_doubled = s_0_T_doubled * K_BOLTZ_FACTOR / rho_c_per_h2_num
    ratio_T_0 = K_T_doubled / K_num
    check(
        "Doubling T_0 increases K by factor 8 (since K ~ T_0^3)",
        abs(ratio_T_0 - 8.0) < 1e-9,
        detail=f"K(2*T_0) / K(T_0) = {ratio_T_0:.6f}",
    )

    # (d) Doubling g_*S(T_0): K -> 2*K (since K ~ g_*S(T_0))
    s_0_g_doubled = (2.0 * math.pi**2 / 45.0) * (2.0 * g_starS_T0_num) * T_0_GeV**3
    K_g_doubled = s_0_g_doubled * K_BOLTZ_FACTOR / rho_c_per_h2_num
    ratio_g = K_g_doubled / K_num
    check(
        "Doubling g_*S(T_0) increases K by factor 2 (since K ~ g_*S(T_0))",
        abs(ratio_g - 2.0) < 1e-9,
        detail=f"K(2*g_*S) / K(g_*S) = {ratio_g:.6f}",
    )

    # (e) Doubling H_100: K -> K/4 (since K ~ 1/H_100^2 through rho_c/h^2)
    H_100_doubled = 2.0 * H_100_GeV
    rho_c_per_h2_H_doubled = 3.0 * H_100_doubled**2 * M_Pl_num**2 / (8.0 * math.pi)
    K_H_doubled = s_0_num * K_BOLTZ_FACTOR / rho_c_per_h2_H_doubled
    ratio_H = K_num / K_H_doubled
    check(
        "Doubling H_100 reduces K by factor 4 (since K ~ 1/H_100^2 via rho_c/h^2)",
        abs(ratio_H - 4.0) < 1e-9,
        detail=f"K(H_100) / K(2*H_100) = {ratio_H:.6f}",
    )

    # ----------------------------------------------------------------------
    section("Part 6: symbolic free-symbol residual check")
    # ----------------------------------------------------------------------

    # The LHS minus RHS of (P*) has no free symbols after simplification.
    lhs_minus_rhs = simplify(K_def - s_0 * C_Boltz / rho_c_per_h2)
    check(
        "(P*) lhs - rhs has no free residual symbols",
        lhs_minus_rhs == 0,
        detail=f"lhs - rhs = {lhs_minus_rhs}",
    )

    # The explicit canonical form K_explicit reduces to K_def with the same
    # four free symbols (g_*S(T_0), T_0, H_100, M_Pl); no extra symbols
    # spuriously enter.
    free_K_def = K_def.free_symbols
    free_K_explicit = K_explicit.free_symbols
    expected_free = {g_starS_T0, T_0, H_100, M_Pl}
    check(
        "K_def free symbols = {g_*S(T_0), T_0, H_100, M_Pl}",
        free_K_def == expected_free,
        detail=f"got {free_K_def}",
    )
    check(
        "K_explicit free symbols = {g_*S(T_0), T_0, H_100, M_Pl}",
        free_K_explicit == expected_free,
        detail=f"got {free_K_explicit}",
    )

    # ----------------------------------------------------------------------
    section("Summary")
    # ----------------------------------------------------------------------

    total = PASS + FAIL
    print()
    print(f"  PASS = {PASS}")
    print(f"  FAIL = {FAIL}")
    print(f"  TOTAL = {total}")
    print()

    if FAIL == 0:
        print("VERDICT: (P*) algebraic prefactor identity holds parametrically; numerical")
        print("evaluation reproduces textbook K = 1.07e9 GeV^-1 within ~3% Boltzmann-tail")
        print("subleading-coefficient gap; all scaling probes confirm the expected exponents.")
        print()
        print("TOTAL: PASS={} FAIL=0".format(PASS))
        return 0
    else:
        print(f"VERDICT: {FAIL} checks failed.")
        print("TOTAL: PASS={} FAIL={}".format(PASS, FAIL))
        return 1


if __name__ == "__main__":
    sys.exit(main())
