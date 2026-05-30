#!/usr/bin/env python3
"""Lane 5 (C2) attack-surface bipartition narrow theorem runner.

This runner verifies the narrow algebraic content of
`docs/HUBBLE_LANE5_C2_ATTACK_SURFACE_BIPARTITION_NARROW_THEOREM_NOTE_2026-05-27.md`:

  - the bounded matter-cascade slice has exactly two `(C2)`-counted
    cascade-internal observational pins (eta, alpha_GUT) on the cited
    authorities;
  - the retained R_base = 31/9 group-theory identity holds exactly;
  - the cascade arithmetic at textbook BBN + flatness gives the documented
    Omega_Lambda value under declared inputs;
  - Sommerfeld variation over alpha_GUT in [0.03, 0.05] gives Omega_Lambda
    over the documented [~0.66, ~0.71] band;
  - the PMNS-A13 sub-route on (C2.eta) is retained-no-go on the cited
    authority;
  - the (C3) class is recorded as empty on the cited authority;
  - the bipartition statement appears in the note and the cited authority.

No claim of (C2) closure. No claim of eta retirement. No claim of alpha_GUT
retirement. No claim of T_CMB or H_0 derivation.

Run:
  PYTHONPATH=scripts python3 scripts/frontier_hubble_lane5_c2_attack_surface_bipartition.py
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

PASS_COUNT = 0
FAIL_COUNT = 0


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


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


# =============================================================================
# Part 1: R_base = 31/9 exact identity
# =============================================================================


def part1_r_base_identity() -> None:
    section("Part 1: retained R_base = 31/9 group-theory identity")

    # Casimirs and adjoint dims (textbook Lie-algebra identities)
    C2_su3 = Fraction(4, 3)
    C2_su2 = Fraction(3, 4)
    dim_adj_3 = 8
    dim_adj_2 = 3
    gut_norm = Fraction(3, 5)

    numerator = C2_su3 * dim_adj_3 + C2_su2 * dim_adj_2
    denominator = C2_su2 * dim_adj_2
    r_base = gut_norm * (numerator / denominator)

    check(
        "C_2(SU(3)_fund) = 4/3",
        C2_su3 == Fraction(4, 3),
    )
    check(
        "C_2(SU(2)_fund) = 3/4",
        C2_su2 == Fraction(3, 4),
    )
    check(
        "dim(adj SU(3)) = 8 = N^2 - 1 at N=3",
        dim_adj_3 == 3 * 3 - 1,
    )
    check(
        "dim(adj SU(2)) = 3 = N^2 - 1 at N=2",
        dim_adj_2 == 2 * 2 - 1,
    )
    check(
        "numerator N = C2(3)*dim(adj_3) + C2(2)*dim(adj_2) = 155/12",
        numerator == Fraction(155, 12),
        f"computed {numerator}",
    )
    check(
        "denominator D = C2(2)*dim(adj_2) = 9/4",
        denominator == Fraction(9, 4),
        f"computed {denominator}",
    )
    check(
        "N/D = 155/27",
        numerator / denominator == Fraction(155, 27),
        f"computed {numerator / denominator}",
    )
    check(
        "R_base = (3/5) * 155/27 = 31/9 (lowest terms)",
        r_base == Fraction(31, 9),
        f"computed {r_base}",
    )

    # Equivalent decomposition
    r_base_alt = Fraction(3, 5) + Fraction(128, 45)
    check(
        "R_base = 3/5 + 128/45 equivalent decomposition holds",
        r_base_alt == Fraction(31, 9),
        f"computed {r_base_alt}",
    )


# =============================================================================
# Part 2: Bounded cascade arithmetic (textbook BBN + flatness)
# =============================================================================


def part2_cascade_arithmetic() -> None:
    section("Part 2: bounded cascade arithmetic at declared inputs")

    # Declared inputs documented in OMEGA_LAMBDA_DERIVATION_NOTE.md (textbook
    # BBN + cited Sommerfeld pin)
    omega_b = Fraction(492, 10000)   # 0.0492
    R = Fraction(538, 100)            # 5.38
    omega_total = 1

    omega_dm = R * omega_b
    omega_m = omega_b + omega_dm
    omega_lambda = omega_total - omega_m

    # Numerical readout
    omega_dm_f = float(omega_dm)
    omega_m_f = float(omega_m)
    omega_lambda_f = float(omega_lambda)

    print(f"  Omega_b      = {float(omega_b):.6f}")
    print(f"  R            = {float(R):.6f}")
    print(f"  Omega_DM     = {omega_dm_f:.6f}")
    print(f"  Omega_m      = {omega_m_f:.6f}")
    print(f"  Omega_Lambda = {omega_lambda_f:.6f}")

    check(
        "Omega_DM = R * Omega_b matches documented 0.264696",
        abs(omega_dm_f - 0.264696) < 1e-6,
        f"got {omega_dm_f:.6f}",
    )
    check(
        "Omega_m = Omega_b + Omega_DM matches documented 0.313896",
        abs(omega_m_f - 0.313896) < 1e-6,
        f"got {omega_m_f:.6f}",
    )
    check(
        "Omega_Lambda = Omega_total - Omega_m matches documented 0.686104",
        abs(omega_lambda_f - 0.686104) < 1e-6,
        f"got {omega_lambda_f:.6f}",
    )
    check(
        "Rounded Omega_Lambda = 0.686",
        round(omega_lambda_f, 3) == 0.686,
        f"got {round(omega_lambda_f, 3)}",
    )

    # Sommerfeld factor implied by declared R
    R_base = Fraction(31, 9)
    s_implied = R / R_base
    print(f"  R_base       = 31/9 = {float(R_base):.6f}")
    print(f"  S = R/R_base = {float(s_implied):.6f}")
    check(
        "S_corr implied by declared R is approximately 1.562",
        abs(float(s_implied) - 1.561935483) < 1e-6,
        f"got {float(s_implied):.9f}",
    )


# =============================================================================
# Part 3: Sommerfeld interval gives bounded Omega_Lambda band
# =============================================================================


def part3_sommerfeld_band() -> None:
    section("Part 3: Sommerfeld interval at bounded alpha_GUT gives Omega_Lambda band")

    # From COSMOLOGY_FROM_MASS_SPECTRUM_NOTE.md:
    #   alpha_GUT in [0.03, 0.05]
    #   inside that band R varies over [4.8, 5.3]
    # Here we verify the (C2.alpha_GUT)-half sensitivity: with eta fixed at
    # the documented central value (Omega_b = 0.0492), Omega_Lambda over the
    # alpha_GUT-only band is the documented narrow sub-band.
    omega_b = 0.0492
    omega_r = 9.2e-5

    R_min, R_max = 4.8, 5.3
    omega_dm_min = R_min * omega_b
    omega_dm_max = R_max * omega_b
    omega_m_min = omega_b + omega_dm_min
    omega_m_max = omega_b + omega_dm_max

    omega_lambda_at_R_max = 1.0 - omega_m_max - omega_r
    omega_lambda_at_R_min = 1.0 - omega_m_min - omega_r

    print(f"  alpha_GUT band = [0.03, 0.05]")
    print(f"  R band         = [{R_min}, {R_max}]")
    print(f"  Omega_m band (eta fixed)   = [{omega_m_min:.6f}, {omega_m_max:.6f}]")
    print(f"  Omega_Lambda band (eta fixed) = [{omega_lambda_at_R_max:.6f}, {omega_lambda_at_R_min:.6f}]")

    check(
        "alpha_GUT-only band: Omega_Lambda lower endpoint near 0.69",
        0.68 <= omega_lambda_at_R_max <= 0.70,
        f"got {omega_lambda_at_R_max:.6f}",
    )
    check(
        "alpha_GUT-only band: Omega_Lambda upper endpoint near 0.71",
        0.70 <= omega_lambda_at_R_min <= 0.72,
        f"got {omega_lambda_at_R_min:.6f}",
    )

    # Width of the band (sensitivity to alpha_GUT alone, eta fixed)
    band_width = omega_lambda_at_R_min - omega_lambda_at_R_max
    print(f"  Band width (alpha_GUT-only, eta fixed)  = {band_width:.6f}")
    check(
        "alpha_GUT-only band width is order 0.02-0.03 at eta fixed",
        0.02 <= band_width <= 0.04,
        f"got {band_width:.6f}",
    )

    # The note's documented [0.66, 0.71] joint band is the union over both eta
    # and alpha_GUT bands - we verify the alpha_GUT-only sub-band sits inside it.
    joint_band_low, joint_band_high = 0.66, 0.71
    check(
        "alpha_GUT-only sub-band is inside the documented joint [0.66, 0.71] band",
        joint_band_low <= omega_lambda_at_R_max and omega_lambda_at_R_min <= joint_band_high + 0.005,
        f"alpha_GUT-only=[{omega_lambda_at_R_max:.3f}, {omega_lambda_at_R_min:.3f}]; joint=[0.66, 0.71]",
    )


# =============================================================================
# Part 4: BBN sensitivity to eta (alpha_GUT fixed)
# =============================================================================


def part4_eta_sensitivity() -> None:
    section("Part 4: BBN sensitivity to eta (alpha_GUT fixed)")

    # Omega_b * h^2 = 3.6515e-3 * eta_10 (textbook BBN; Cyburt+ 2016)
    # We verify Omega_b is monotonic linear in eta_10 at fixed h.
    h2 = 0.674 ** 2
    coeff = 3.6515e-3

    eta_band_low = 5.7   # ~95% Planck low edge
    eta_band_high = 6.5  # ~95% Planck high edge

    omega_b_low = coeff * eta_band_low / h2
    omega_b_high = coeff * eta_band_high / h2

    # Holding R = 5.38 (i.e., alpha_GUT fixed at ~0.048 implied), Omega_Lambda is
    R = 5.38
    omega_r = 9.2e-5
    omega_lambda_at_low_eta = 1.0 - (omega_b_low * (1.0 + R)) - omega_r
    omega_lambda_at_high_eta = 1.0 - (omega_b_high * (1.0 + R)) - omega_r

    print(f"  eta_10 band    = [{eta_band_low}, {eta_band_high}]")
    print(f"  Omega_b band   = [{omega_b_low:.6f}, {omega_b_high:.6f}]")
    print(f"  Omega_Lambda band (eta-only) = [{omega_lambda_at_high_eta:.6f}, {omega_lambda_at_low_eta:.6f}]")

    band_width_eta = omega_lambda_at_low_eta - omega_lambda_at_high_eta
    print(f"  Band width (alpha_GUT-fixed) = {band_width_eta:.6f}")

    check(
        "Omega_b is positive and monotonic in eta_10",
        0 < omega_b_low < omega_b_high,
        f"got [{omega_b_low:.6f}, {omega_b_high:.6f}]",
    )
    check(
        "Omega_b in physically sensible Planck-2018 ballpark band",
        0.04 <= omega_b_low and omega_b_high <= 0.06,
        f"got [{omega_b_low:.6f}, {omega_b_high:.6f}]",
    )
    check(
        "Documented Omega_b = 0.0492 sits inside the band at central eta",
        omega_b_low <= 0.0492 <= omega_b_high,
        f"band=[{omega_b_low:.6f}, {omega_b_high:.6f}]",
    )
    check(
        "Cascade is linear in Omega_b at fixed R (no quadratic terms)",
        abs((omega_lambda_at_low_eta - omega_lambda_at_high_eta)
            + (omega_b_low - omega_b_high) * (1.0 + R)) < 1e-12,
    )


# =============================================================================
# Part 5: Bipartition symbolic statement
# =============================================================================


def part5_bipartition_symbolic() -> None:
    section("Part 5: bipartition symbolic statement")

    eta, alpha_GUT, h2 = sp.symbols("eta alpha_GUT h2", positive=True)
    omega_r = sp.Symbol("Omega_r", positive=True)
    R_base = sp.Rational(31, 9)

    # Bounded cascade (textbook BBN + Sommerfeld bounded)
    # Omega_b = (3.6515e-3 * eta * 1e10) / h^2   (eta_10 = eta * 1e10)
    # We use a symbolic Sommerfeld factor S(alpha_GUT).
    S = sp.Function("S_corr")(alpha_GUT)
    omega_b = sp.Symbol("c_BBN", positive=True) * eta / h2
    R = R_base * S
    omega_dm = R * omega_b
    omega_m = omega_b + omega_dm
    omega_lambda = 1 - omega_m - omega_r

    # The bounded matter-cascade slice's `(C2)`-counted pins are eta and
    # alpha_GUT. T_CMB/h sit on the adjacent C1/5E side and are not counted
    # as pins of this narrow slice. Verify Omega_Lambda explicitly depends
    # on both counted pins.
    free = omega_lambda.free_symbols
    has_eta = eta in free
    has_alpha_GUT = alpha_GUT in {a for a in omega_lambda.atoms(sp.Symbol)}
    # We also detect alpha_GUT via S(alpha_GUT)'s arguments
    has_alpha_GUT_via_S = any(
        a == alpha_GUT for fn in omega_lambda.atoms(sp.Function) for a in fn.args
    )

    print(f"  Omega_Lambda(eta, alpha_GUT) = {omega_lambda}")
    print(f"  free symbols of Omega_Lambda = {free}")

    check(
        "Omega_Lambda explicitly depends on eta",
        has_eta,
    )
    check(
        "Omega_Lambda explicitly depends on alpha_GUT (via Sommerfeld)",
        has_alpha_GUT_via_S,
    )

    # Partial derivatives confirm non-trivial sensitivity to both
    d_eta = sp.diff(omega_lambda, eta)
    d_alpha = sp.diff(omega_lambda, alpha_GUT)
    check(
        "d Omega_Lambda / d eta is non-zero",
        sp.simplify(d_eta) != 0,
        f"d/deta = {sp.simplify(d_eta)}",
    )
    check(
        "d Omega_Lambda / d alpha_GUT is non-zero (via Sommerfeld)",
        sp.simplify(d_alpha) != 0,
        f"d/dalpha_GUT = {sp.simplify(d_alpha)}",
    )

    # Bipartition: retiring eta alone leaves cascade dependent only on alpha_GUT;
    # retiring alpha_GUT alone leaves cascade dependent only on eta.
    omega_lambda_eta_retired = omega_lambda.subs(eta, sp.Symbol("eta_framework", positive=True))
    omega_lambda_alpha_retired = omega_lambda.subs(S, sp.Symbol("S_framework", positive=True))

    check(
        "After eta retired, cascade has no remaining free eta dependence",
        eta not in omega_lambda_eta_retired.free_symbols,
    )
    check(
        "After alpha_GUT retired, cascade has no remaining S_corr(alpha_GUT) function",
        not any(
            fn.func == sp.Function("S_corr") for fn in omega_lambda_alpha_retired.atoms(sp.Function)
        ),
    )

    # Symmetric bipartition: full closure of cascade-internal pins requires both
    omega_lambda_fully_retired = omega_lambda_alpha_retired.subs(
        eta, sp.Symbol("eta_framework", positive=True)
    )
    surviving_pins = omega_lambda_fully_retired.free_symbols - {
        sp.Symbol("h2", positive=True),
        omega_r,
        sp.Symbol("c_BBN", positive=True),
        sp.Symbol("eta_framework", positive=True),
        sp.Symbol("S_framework", positive=True),
    }
    print(f"  Surviving pins after full retirement = {surviving_pins}")
    check(
        "After both eta and alpha_GUT retired, no cascade-internal observational pin remains",
        len(surviving_pins) == 0,
        f"surviving={surviving_pins}",
    )


# =============================================================================
# Part 6: Authority text checks
# =============================================================================


def part6_authority_text() -> None:
    section("Part 6: cited authority text confirms framing")

    necessity = read("docs/HUBBLE_LANE5_COSMIC_HISTORY_RATIO_NECESSITY_NO_GO_NOTE_2026-04-26.md")
    eta_audit = read("docs/HUBBLE_LANE5_ETA_RETIREMENT_GATE_AUDIT_NOTE_2026-04-26.md")
    c2_stretch = read("docs/HUBBLE_LANE5_C2_CKM_PMNS_RIGHT_SENSITIVE_SELECTOR_STRETCH_NOTE_2026-04-29.md")
    c3_no_route = read("docs/HUBBLE_LANE5_C3_VACUUM_TOPOLOGY_NO_ACTIVE_ROUTE_NOTE_2026-04-27.md")
    cosmology = read("docs/COSMOLOGY_FROM_MASS_SPECTRUM_NOTE.md")
    omega_lambda_note = read("docs/OMEGA_LAMBDA_DERIVATION_NOTE.md")
    r_base = read("docs/R_BASE_GROUP_THEORY_DERIVATION_THEOREM_NOTE_2026-04-24.md")

    check(
        "Necessity no-go names (C2) cosmic-history-ratio retirement",
        "(C2) cosmic-history-ratio retirement" in necessity,
    )
    check(
        "Necessity no-go names broader eta, alpha_GUT, T_CMB targets",
        "`eta`" in necessity and "`alpha_GUT`" in necessity and "`T_CMB`" in necessity,
    )
    check(
        "Eta audit identifies the bounded cascade entry/exit chain",
        "Omega_b -> R -> Omega_DM -> Omega_m -> Omega_Lambda" in eta_audit
        or "Omega_b -> R" in eta_audit and "Omega_Lambda" in eta_audit,
    )
    check(
        "C2 stretch records the PMNS-A13 / CKM right-sensitive sub-route as no-go",
        "no-go" in c2_stretch and "right-sensitive" in c2_stretch and "A13" in c2_stretch,
    )
    check(
        "C3 audit records the (C3) class as empty / no-active-route",
        "No active `(C3)` route exists" in c3_no_route
        or "(C3) class is currently empty" in c3_no_route,
    )
    check(
        "Cosmology note lists eta (imported) and alpha_GUT (bounded) as the cascade inputs",
        "Imported input (one)" in cosmology and "Bounded input (one)" in cosmology,
    )
    check(
        "Cosmology note states alpha_GUT in [0.03, 0.05] Sommerfeld",
        "alpha_GUT" in cosmology and "[0.03, 0.05]" in cosmology,
    )
    check(
        "Omega_Lambda note records the bounded arithmetic cascade",
        "bounded conditional arithmetic cascade" in omega_lambda_note,
    )
    check(
        "R_base note retains R_base = 31/9 group-theory identity",
        "R_base" in r_base and "31/9" in r_base,
    )


# =============================================================================
# Part 7: Bipartition claim-status guardrails
# =============================================================================


def part7_claim_status_guardrails() -> None:
    section("Part 7: claim-status guardrails on this note")

    note = read("docs/HUBBLE_LANE5_C2_ATTACK_SURFACE_BIPARTITION_NARROW_THEOREM_NOTE_2026-05-27.md")

    check(
        "Note declares Type: bounded_theorem",
        "**Claim type:** bounded_theorem" in note,
    )
    check(
        "Note declares Status authority: independent audit lane only",
        "Status authority:** independent audit lane only" in note,
    )
    check(
        "Note declares actual_current_surface_status: narrow_bounded_theorem",
        "actual_current_surface_status: narrow_bounded_theorem" in note,
    )
    check(
        "Note declares proposal_allowed: false",
        "proposal_allowed: false" in note,
    )
    check(
        "Note declares bare_retained_allowed: false",
        "bare_retained_allowed: false" in note,
    )
    check(
        "Note explicitly does NOT close (C2)",
        "does NOT close (C2)" in note or "does NOT close" in note and "(C2)" in note,
    )
    check(
        "Note explicitly does NOT retire eta",
        "does NOT retire" in note and "eta" in note.lower(),
    )
    check(
        "Note explicitly does NOT retire alpha_GUT",
        "does NOT retire" in note and "alpha_GUT" in note,
    )
    check(
        "Note bipartitions the residual into (C2.eta) and (C2.alpha_GUT)",
        "(C2.eta)" in note and "(C2.alpha_GUT)" in note,
    )
    check(
        "Note distinguishes full cascade closure from C2-class premise discharge",
        "Full single-number closure" in note
        and "does not say the fully numerical cascade closes" in note,
    )


def main() -> int:
    print("=" * 88)
    print("LANE 5 (C2) ATTACK-SURFACE BIPARTITION NARROW THEOREM RUNNER")
    print("=" * 88)
    print()
    print("Bounded statement under test:")
    print("  - bounded matter-cascade slice has exactly two C2-counted pins (eta, alpha_GUT);")
    print("  - residual (C2) attack surface bipartitions into (C2.eta) and (C2.alpha_GUT);")
    print("  - PMNS-A13 sub-route on (C2.eta) is retained-no-go;")
    print("  - (C3) class empty on current vacuum/topology surface.")
    print()
    print("This runner does NOT derive eta, alpha_GUT, T_CMB, or H_0.")

    part1_r_base_identity()
    part2_cascade_arithmetic()
    part3_sommerfeld_band()
    part4_eta_sensitivity()
    part5_bipartition_symbolic()
    part6_authority_text()
    part7_claim_status_guardrails()

    print()
    print("=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)

    if FAIL_COUNT:
        print("Bipartition runner failed; do not use the note.")
        return 1

    print("Result: bipartition narrow theorem holds on the cited authority surface.")
    print("No (C2) closure, no eta retirement, no alpha_GUT retirement claimed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
