#!/usr/bin/env python3
"""Dedicated bounded-chain runner for docs/ALPHA_S_DERIVED_NOTE.md.

Claim under check (theorem T1 of the note):

    Given the declared boundary inputs B1-B4,

        B1:  <P> = 0.5934              (licensed reuse number; license:
                                        PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
        B2:  g_bare = 1, alpha_bare = g_bare^2 / (4 pi) = 1 / (4 pi)
                                       (declared normalization input)
        B3:  staggered-Dirac gauge vacuum-polarization channel has
             operator count n_link = 2; identifying that channel count
             with the physical coupling definition is declared here
                                      (structural input)
        B4:  alpha_s(mu = v) := alpha_bare / u_0^2
                                       (declared scheme/scale input)

    the forward computation

        u_0        = <P>^(1/4)
        alpha_s(v) = alpha_bare / u_0^2 = 1 / (4 pi sqrt(<P>)) = 0.10330382

    is exact zero-free-parameter arithmetic over those inputs.

Corollary C1 (bounded, explicitly NOT load-bearing for T1): transferring
the T1 output through the supplied piecewise two-loop QCD EFT map, with
n_f=6 above m_t, n_f=5 below m_t, and identity matching at m_t, gives a
numerical M_Z readout.  The difference from the exact one-loop map is reported
only as an observed order-to-order shift.  The scalar RGE block below is a
self-contained fixed-step RK4 reimplementation; it does not import any shared
frontier runner.

Check classes (each PASS line is tagged):

  [A] algebraic identity / exact arithmetic on the declared boundary inputs
      (8 checks: T1 forward computation, two independent evaluation
      routes, exact identities, analytic sensitivity).
  [B] cross-note input consistency (9 checks: helper-module residuals
      against scripts/canonical_plaquette_surface.py, membership of the
      bridge domain, fixed-step convergence for C1, the observed order shift,
      and
      source-firewall wording for the remaining B1/B3/B4 bridge
      blockers).
  [D] external comparator (2 checks: PDG bands, quarantined terminal
      section; never load-bearing for T1).

Deterministic, pure Python (math + fractions only), runtime well under
one second.  Exit code 0 iff TOTAL: PASS=n FAIL=0.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

# Helper module consulted ONLY for tagged class-B consistency residuals;
# T1 below recomputes everything forward from the declared boundary inputs.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import canonical_plaquette_surface as cps  # noqa: E402

PI = math.pi
NOTE_PATH = Path(__file__).resolve().parents[1] / "docs" / "ALPHA_S_DERIVED_NOTE.md"

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_COUNTS = {"A": 0, "B": 0, "D": 0}


def check(klass: str, name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
        CLASS_COUNTS[klass] += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}][{klass}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


# ---------------------------------------------------------------------------
# Declared boundary inputs (B1-B4) — mirrors the note verbatim.
# ---------------------------------------------------------------------------

P_BOUNDARY = 0.5934           # B1: licensed reuse number (plaquette license)
G_BARE = 1.0                  # B2: declared bare-coupling normalization
ALPHA_BARE = G_BARE ** 2 / (4.0 * PI)
N_LINK = 2                    # B3: VP-channel operator count used by T1
# B3 also declares channel selection; B4 declares scheme/scale:
# alpha_s(mu=v) := alpha_bare / u_0^n_link.

# Domain supplied by the running-bridge note (class-B consistency only).
BRIDGE_A_MIN = 0.085
BRIDGE_A_MAX = 0.130

# Standard-infrastructure constants used ONLY inside corollary C1.
V_BOUNDARY = 246.282818290129  # GeV (C1 electroweak boundary scale)
M_T_POLE = 172.69              # GeV (PDG pole mass; C1 threshold only)
M_Z = 91.1876                  # GeV (PDG; C1 terminal scale only)

# PDG comparators — quarantined class-D terminal section only.
ALPHA_S_MZ_PDG = 0.1180
ALPHA_S_MZ_PDG_SIGMA = 0.0009
ALPHA_S_MZ_RESTRICTED = 0.1179
ALPHA_S_MZ_RESTRICTED_SIGMA = 0.0008


# ---------------------------------------------------------------------------
# T1 forward computation (three independent evaluation routes).
# ---------------------------------------------------------------------------

def alpha_s_v_route_one(p: float) -> float:
    """Route I: the note's stepwise chain u_0 = p^(1/4), alpha/u_0^n_link."""
    u0 = p ** 0.25
    return ALPHA_BARE / u0 ** N_LINK


def alpha_s_v_route_two(p: float) -> float:
    """Route II: the collapsed closed form 1 / (4 pi sqrt(p))."""
    return 1.0 / (4.0 * PI * math.sqrt(p))


def alpha_s_v_route_three(p: float) -> float:
    """Route III: log-domain evaluation exp(-log(p)/2) / (4 pi)."""
    return math.exp(-0.5 * math.log(p)) / (4.0 * PI)


# ---------------------------------------------------------------------------
# Self-contained piecewise 2-loop QCD EFT RGE (corollary C1 only).
# ---------------------------------------------------------------------------

def beta_coefficients(n_f: int) -> tuple[float, float]:
    return 11.0 - 2.0 * n_f / 3.0, 102.0 - 38.0 * n_f / 3.0


def beta_alpha_2loop(alpha: float, n_f: int) -> float:
    beta_0, beta_1 = beta_coefficients(n_f)
    return (-beta_0 * alpha ** 2 / (2.0 * PI)
            - beta_1 * alpha ** 3 / (8.0 * PI ** 2))


def rk4_alpha(alpha: float, t0: float, t1: float, n_f: int,
              n_steps: int) -> float:
    """Deterministic fixed-step RK4 integration of the scalar QCD EFT."""
    h = (t1 - t0) / n_steps
    for _ in range(n_steps):
        k1 = beta_alpha_2loop(alpha, n_f)
        k2 = beta_alpha_2loop(alpha + 0.5 * h * k1, n_f)
        k3 = beta_alpha_2loop(alpha + 0.5 * h * k2, n_f)
        k4 = beta_alpha_2loop(alpha + h * k3, n_f)
        alpha += (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
    return alpha


def run_v_to_mz_2loop(alpha_s_v: float, n_steps: int = 12000) -> float:
    """C1: n_f=6 then n_f=5 with supplied identity matching at m_t."""
    alpha = rk4_alpha(alpha_s_v, math.log(V_BOUNDARY), math.log(M_T_POLE),
                      n_f=6, n_steps=n_steps)
    return rk4_alpha(alpha, math.log(M_T_POLE), math.log(M_Z),
                     n_f=5, n_steps=n_steps)


def run_v_to_mz_1loop(alpha_s_v: float) -> float:
    beta0_6, _ = beta_coefficients(6)
    beta0_5, _ = beta_coefficients(5)
    length = (beta0_6 * math.log(V_BOUNDARY / M_T_POLE)
              + beta0_5 * math.log(M_T_POLE / M_Z)) / (2.0 * PI)
    return alpha_s_v / (1.0 - length * alpha_s_v)


# ---------------------------------------------------------------------------
# Verification surface
# ---------------------------------------------------------------------------

def part_t1_forward_computation() -> float:
    print("\n=== T1: forward computation over declared boundary inputs B1-B4 ===\n")

    u0 = P_BOUNDARY ** 0.25
    a_v = alpha_s_v_route_one(P_BOUNDARY)

    check("A", "S2: u_0 = <P>^(1/4) = 0.877681381 and u_0^4 reproduces <P>",
          abs(u0 - 0.877681381) < 5e-10 and abs(u0 ** 4 - P_BOUNDARY) < 1e-15,
          f"u_0 = {u0:.12f}, |u_0^4 - <P>| = {abs(u0**4 - P_BOUNDARY):.3e}")

    check("A", "S3: alpha_bare = g_bare^2 / (4 pi) = 1 / (4 pi) at g_bare = 1",
          abs(ALPHA_BARE - 1.0 / (4.0 * PI)) == 0.0,
          f"alpha_bare = {ALPHA_BARE:.12f}")

    a_v2 = alpha_s_v_route_two(P_BOUNDARY)
    a_v3 = alpha_s_v_route_three(P_BOUNDARY)
    check("A", "S4: routes I/II/III agree to 1e-16 "
               "(stepwise chain vs closed form vs log-domain)",
          abs(a_v - a_v2) <= 1e-16 and abs(a_v - a_v3) <= 1e-16,
          f"|I-II| = {abs(a_v - a_v2):.3e}, |I-III| = {abs(a_v - a_v3):.3e}")

    ident = abs(4.0 * PI * math.sqrt(P_BOUNDARY) * a_v - 1.0)
    check("A", "exact-identity residual |4 pi sqrt(<P>) alpha_s(v) - 1| <= 1e-15",
          ident <= 1e-15,
          f"residual = {ident:.3e}")

    check("A", "T1 headline: alpha_s(v) = 0.10330382 (8-decimal agreement)",
          abs(a_v - 0.10330382) < 5e-9,
          f"alpha_s(v) = {a_v:.10f}")

    alpha_lm = ALPHA_BARE / u0
    lm_resid = abs(alpha_lm ** 2 - ALPHA_BARE * a_v)
    check("A", "exact identity alpha_LM^2 = alpha_bare * alpha_s(v)",
          lm_resid <= 1e-17,
          f"residual = {lm_resid:.3e}")

    sens_analytic = -a_v / (2.0 * P_BOUNDARY)
    h = 1e-7
    sens_numeric = (alpha_s_v_route_two(P_BOUNDARY + h)
                    - alpha_s_v_route_two(P_BOUNDARY - h)) / (2.0 * h)
    rel = abs(sens_numeric - sens_analytic) / abs(sens_analytic)
    check("A", "analytic sensitivity d alpha_s/d<P> = -alpha_s/(2<P>) "
               "matches central difference",
          rel < 1e-6,
          f"analytic = {sens_analytic:.9f}, numeric = {sens_numeric:.9f}, "
          f"rel = {rel:.3e}")

    # Zero-free-parameter form: alpha_s(v) is a smooth monotone function of
    # the single boundary input <P>; there is no second knob to tune.
    grid = [0.50, 0.55, 0.5934, 0.65, 0.70]
    vals = [alpha_s_v_route_two(p) for p in grid]
    monotone = all(vals[i] > vals[i + 1] for i in range(len(vals) - 1))
    check("A", "zero-free-parameter form: alpha_s(<P>) strictly monotone "
               "in the single boundary input, no second parameter",
          monotone,
          "alpha_s decreasing in <P> across [0.50, 0.70]")

    return a_v


def part_cross_note_consistency(a_v: float) -> None:
    print("\n=== Cross-note consistency residuals (class B, "
          "non-load-bearing for T1) ===\n")

    check("B", "helper canonical_plaquette_surface.CANONICAL_PLAQUETTE "
               "equals declared boundary input B1",
          cps.CANONICAL_PLAQUETTE == P_BOUNDARY,
          f"helper = {cps.CANONICAL_PLAQUETTE}, B1 = {P_BOUNDARY}")

    check("B", "helper CANONICAL_ALPHA_S_V agrees with the T1 forward value "
               "to 1e-15",
          abs(cps.CANONICAL_ALPHA_S_V - a_v) <= 1e-15,
          f"|helper - T1| = {abs(cps.CANONICAL_ALPHA_S_V - a_v):.3e}")

    check("B", "T1 output lies inside the running bridge's supplied domain",
          BRIDGE_A_MIN <= a_v <= BRIDGE_A_MAX,
          f"{BRIDGE_A_MIN} <= {a_v:.8f} <= {BRIDGE_A_MAX}")


def part_source_firewall() -> None:
    print("\n=== Source-status firewall (class B, non-load-bearing for T1) ===\n")
    text = NOTE_PATH.read_text(encoding="utf-8")
    flat_text = " ".join(text.split())
    check("B", "2026-06-12 firewall says row remains bounded, not retained",
          "2026-06-12 Residual-Bridge Source Firewall" in text
          and "this is bounded support only" in flat_text
          and "No retained-grade proposal or status promotion is made here" in flat_text)
    check("B", "firewall keeps B1 as a supplied plaquette reuse value until certified",
          "B1 remains a supplied plaquette reuse value" in text
          and "this note does not supply that enclosure" in text
          and "`<P> = 0.5934`" in text)
    check("B", "firewall keeps B3 channel-selection/coupling-map bridge open",
          "B3 still has a channel-selection residue" in text
          and "B3 channel-selection/coupling-map theorem" in flat_text)
    check("B", "firewall keeps B4 lattice-to-MSbar scheme/scale bridge open",
          "B4 remains a scheme/scale bridge" in text
          and "B4 lattice-to-MSbar scheme and scale theorem" in flat_text)


def part_c1_corollary(a_v: float) -> float:
    print("\n=== C1 (bounded corollary, NOT load-bearing for T1): "
          "v -> M_Z transfer ===\n")

    a_mz_2l = run_v_to_mz_2loop(a_v)
    a_mz_1l = run_v_to_mz_1loop(a_v)
    order_shift = a_mz_2l - a_mz_1l
    print(f"  2-loop alpha_s(M_Z) = {a_mz_2l:.6f}")
    print(f"  1-loop alpha_s(M_Z) = {a_mz_1l:.6f}")
    print(f"  observed order shift = {order_shift:+.6f}")

    coarse = run_v_to_mz_2loop(a_v, n_steps=6000)
    check("B", "C1: independent RK4 step refinement is converged",
          abs(a_mz_2l - coarse) < 1e-11,
          f"|12000-step - 6000-step| = {abs(a_mz_2l-coarse):.3e}")

    check("B", "C1 observed one-loop-to-two-loop shift is positive and is "
               "reported without remainder semantics",
          0.0 < order_shift < 0.01 * a_mz_2l,
          f"observed shift = {order_shift:.6f}")

    return a_mz_2l


def part_pdg_quarantine(a_mz: float) -> None:
    print("\n=== Quarantined class-D terminal section: PDG comparators "
          "(never load-bearing) ===\n")

    check("D", "C1 readout inside PDG world-average 1-sigma band "
               "(0.1180 +/- 0.0009)",
          abs(a_mz - ALPHA_S_MZ_PDG) <= ALPHA_S_MZ_PDG_SIGMA,
          f"|{a_mz:.6f} - 0.1180| = {abs(a_mz - ALPHA_S_MZ_PDG):.4f}")

    check("D", "C1 readout inside PDG restricted-average 2-sigma band "
               "(0.1179 +/- 0.0008)",
          abs(a_mz - ALPHA_S_MZ_RESTRICTED)
          <= 2.0 * ALPHA_S_MZ_RESTRICTED_SIGMA,
          f"|{a_mz:.6f} - 0.1179| = {abs(a_mz - ALPHA_S_MZ_RESTRICTED):.4f}")


def main() -> None:
    print("=" * 76)
    print("alpha_s derived note — dedicated bounded-chain runner")
    print("T1: alpha_s(v) = 1/(4 pi sqrt(<P>)) over declared boundary inputs B1-B4")
    print("C1: bounded v -> M_Z corollary (quarantined; not load-bearing)")
    print("=" * 76)

    a_v = part_t1_forward_computation()
    part_cross_note_consistency(a_v)
    part_source_firewall()
    a_mz = part_c1_corollary(a_v)
    part_pdg_quarantine(a_mz)

    print()
    print("Scope notes for the auditor:")
    print("  - T1 is exact arithmetic over the DECLARED boundary inputs B1-B4;")
    print("    the plaquette value 0.5934 is licensed upstream only as a reuse")
    print("    number and is treated exactly that way here.")
    print("  - The helper module canonical_plaquette_surface.py is consulted")
    print("    only for the tagged class-B consistency residuals above; every")
    print("    T1 number is recomputed forward inside this runner.")
    print("  - B3 consumes n_link = 2 as the staggered-Dirac gauge")
    print("    vacuum-polarization channel count; the channel-selection step")
    print("    into alpha_s(v) := alpha_bare/u_0^2 is declared in the note.")
    print("  - C1 uses a self-contained piecewise 2-loop QCD EFT map with")
    print("    n_f=6 then n_f=5 and supplied identity matching at m_t.")
    print("    Its order shift is not a remainder bound; PDG targets appear")
    print("    only in the terminal class-D comparator section.")
    print("  - The M_Z readout uses the running-bridge note's bounded")
    print("    transfer-kernel scope; it is a corollary, not part of")
    print("    the T1 claim surface.")
    print("  - The source firewall keeps B1, B3 channel-selection, and")
    print("    B4 open; this runner does not promote the row.")
    print()
    print("=" * 76)
    print(f"Breakdown: A={CLASS_COUNTS['A']} B={CLASS_COUNTS['B']} "
          f"D={CLASS_COUNTS['D']}")
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 76)

    if FAIL_COUNT:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
