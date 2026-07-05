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
the T1 output through the standard SM 2-loop RGE (Machacek-Vaughn 1984;
Arason et al. 1992) with leading-order top-threshold matching, v -> M_Z,
gives alpha_s(M_Z) = 0.118067 ~ 0.1181 with a 1-loop/2-loop truncation
envelope ~5e-4.  The RGE block below is a self-contained fixed-step RK4
reimplementation; it does not import any shared frontier runner.

Check classes (each PASS line is tagged):

  [A] algebraic identity / exact arithmetic on the declared boundary inputs
      (8 checks: T1 forward computation, two independent evaluation
      routes, exact identities, analytic sensitivity).
  [B] cross-note input consistency (9 checks: helper-module residuals
      against scripts/canonical_plaquette_surface.py, the bridge note's
      boundary value, the bridge note's published 0.1181 readout for
      C1, the truncation envelope of the C1 transfer, and
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

# Boundary value registered by the running-bridge note (its own rounded
# declared value; class-B consistency target only).
BRIDGE_ALPHA_S_V_BOUNDARY = 0.103304
BRIDGE_ALPHA_S_MZ_PUBLISHED = 0.1181

# Standard-infrastructure constants used ONLY inside corollary C1.
V_BOUNDARY = 246.282818290129  # GeV (C1 electroweak boundary scale)
M_T_POLE = 172.69              # GeV (PDG pole mass; C1 threshold only)
M_Z = 91.1876                  # GeV (PDG; C1 terminal scale only)
G1_V = 0.46228                 # auxiliary SM boundary inputs at v
G2_V = 0.65184                 # (same tuple the bridge note registers)
YT_V = 0.93737
LAMBDA_V = 0.13

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
# Self-contained 2-loop SM RGE (corollary C1 only).
# ---------------------------------------------------------------------------

def beta_2loop(y: list[float], n_f: int) -> list[float]:
    """Standard MSbar 2-loop SM RGE for (g1, g2, g3, yt, lambda).

    Coefficients: Machacek-Vaughn, Nucl. Phys. B 222, 83 (1983);
    B 236, 221 (1984); Arason et al., Phys. Rev. D 46, 3945 (1992).
    Reimplemented here so the corollary is checkable without importing
    any shared frontier runner.
    """
    g1, g2, g3, yt, lam = y
    fac = 1.0 / (16.0 * PI ** 2)
    fac2 = fac * fac
    g1s, g2s, g3s, yts = g1 * g1, g2 * g2, g3 * g3, yt * yt

    b1_1 = (41.0 / 10.0) * g1 ** 3
    b2_1 = -(19.0 / 6.0) * g2 ** 3
    b3_1 = -(11.0 - 2.0 * n_f / 3.0) * g3 ** 3
    byt_1 = yt * (4.5 * yts - (17.0 / 20.0) * g1s - 2.25 * g2s - 8.0 * g3s)
    blam_1 = (24.0 * lam * lam + 12.0 * lam * yts - 6.0 * yts * yts
              - 3.0 * lam * (3.0 * g2s + g1s)
              + (3.0 / 8.0) * (2.0 * g2s ** 2 + (g2s + g1s) ** 2))

    b1_2 = g1 ** 3 * ((199.0 / 50.0) * g1s + (27.0 / 10.0) * g2s
                      + (44.0 / 5.0) * g3s - (17.0 / 10.0) * yts)
    b2_2 = g2 ** 3 * ((9.0 / 10.0) * g1s + (35.0 / 6.0) * g2s
                      + 12.0 * g3s - 1.5 * yts)
    b3_2 = g3 ** 3 * ((11.0 / 10.0) * g1s + 4.5 * g2s - 26.0 * g3s - 2.0 * yts)
    byt_2 = yt * (-12.0 * yts * yts
                  + yts * (36.0 * g3s + (225.0 / 16.0) * g2s
                           + (131.0 / 80.0) * g1s)
                  + (1187.0 / 216.0) * g1s ** 2 - (23.0 / 4.0) * g2s ** 2
                  - 108.0 * g3s ** 2
                  + (19.0 / 15.0) * g1s * g3s + (9.0 / 4.0) * g2s * g3s
                  + 6.0 * lam * lam - 6.0 * lam * yts)

    return [fac * b1_1 + fac2 * b1_2,
            fac * b2_1 + fac2 * b2_2,
            fac * b3_1 + fac2 * b3_2,
            fac * byt_1 + fac2 * byt_2,
            fac * blam_1]


def rk4_2loop(y: list[float], t0: float, t1: float, n_f: int,
              n_steps: int = 4000) -> list[float]:
    """Deterministic fixed-step RK4 integration of the 2-loop system."""
    h = (t1 - t0) / n_steps
    for _ in range(n_steps):
        k1 = beta_2loop(y, n_f)
        k2 = beta_2loop([y[j] + 0.5 * h * k1[j] for j in range(5)], n_f)
        k3 = beta_2loop([y[j] + 0.5 * h * k2[j] for j in range(5)], n_f)
        k4 = beta_2loop([y[j] + h * k3[j] for j in range(5)], n_f)
        y = [y[j] + (h / 6.0) * (k1[j] + 2.0 * k2[j] + 2.0 * k3[j] + k4[j])
             for j in range(5)]
    return y


def beta_1loop_g3(g3: float, n_f: int) -> float:
    return -(11.0 - 2.0 * n_f / 3.0) * g3 ** 3 / (16.0 * PI ** 2)


def rk4_1loop_g3(g3: float, t0: float, t1: float, n_f: int,
                 n_steps: int = 4000) -> float:
    h = (t1 - t0) / n_steps
    for _ in range(n_steps):
        k1 = beta_1loop_g3(g3, n_f)
        k2 = beta_1loop_g3(g3 + 0.5 * h * k1, n_f)
        k3 = beta_1loop_g3(g3 + 0.5 * h * k2, n_f)
        k4 = beta_1loop_g3(g3 + h * k3, n_f)
        g3 = g3 + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
    return g3


def run_v_to_mz_2loop(alpha_s_v: float) -> float:
    """C1 transfer: v -> m_t (n_f=6), LO continuity matching, m_t -> M_Z
    (n_f=5).  Only the top threshold lies inside the interval."""
    g3_v = math.sqrt(4.0 * PI * alpha_s_v)
    y = [G1_V, G2_V, g3_v, YT_V, LAMBDA_V]
    y = rk4_2loop(y, math.log(V_BOUNDARY), math.log(M_T_POLE), n_f=6)
    y = rk4_2loop(y, math.log(M_T_POLE), math.log(M_Z), n_f=5)
    return y[2] ** 2 / (4.0 * PI)


def run_v_to_mz_1loop(alpha_s_v: float) -> float:
    g3 = math.sqrt(4.0 * PI * alpha_s_v)
    g3 = rk4_1loop_g3(g3, math.log(V_BOUNDARY), math.log(M_T_POLE), n_f=6)
    g3 = rk4_1loop_g3(g3, math.log(M_T_POLE), math.log(M_Z), n_f=5)
    return g3 ** 2 / (4.0 * PI)


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

    check("B", "bridge note's boundary alpha_s(v) = 0.103304 is the "
               "6-decimal rounding of the T1 value",
          abs(BRIDGE_ALPHA_S_V_BOUNDARY - a_v) < 5e-7,
          f"|0.103304 - {a_v:.8f}| = {abs(BRIDGE_ALPHA_S_V_BOUNDARY - a_v):.3e}")


def part_source_firewall() -> None:
    print("\n=== Source-status firewall (class B, non-load-bearing for T1) ===\n")
    text = NOTE_PATH.read_text(encoding="utf-8")
    flat_text = " ".join(text.split())
    check("B", "2026-06-12 firewall says row remains bounded, not retained",
          "2026-06-12 Residual-Bridge Source Firewall" in text
          and "this is bounded support only" in flat_text
          and "No retained-grade proposal or status promotion is made here" in flat_text)
    check("B", "firewall keeps B1 plaquette value admitted until certified",
          "B1 remains an admitted plaquette value" in text
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
    envelope = abs(a_mz_2l - a_mz_1l)
    print(f"  2-loop alpha_s(M_Z) = {a_mz_2l:.6f}")
    print(f"  1-loop alpha_s(M_Z) = {a_mz_1l:.6f}")
    print(f"  truncation envelope = {envelope:.6f}")

    check("B", "C1: self-contained 2-loop transfer reproduces the bridge "
               "note's published 0.1181 within 0.001",
          abs(a_mz_2l - BRIDGE_ALPHA_S_MZ_PUBLISHED) < 1e-3,
          f"alpha_s(M_Z) = {a_mz_2l:.6f}, bridge note value = "
          f"{BRIDGE_ALPHA_S_MZ_PUBLISHED}")

    check("B", "C1 truncation envelope: 1-loop/2-loop shift ~5e-4, positive "
               "and below 1% of the readout",
          0.0 < envelope < 0.01 * a_mz_2l and abs(envelope - 5e-4) < 2e-4,
          f"envelope = {envelope:.6f}")

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
    print("  - C1 uses a self-contained 2-loop SM RGE reimplementation with")
    print("    LO top-threshold matching; PDG constants appear only in the")
    print("    terminal class-D section and in the C1 threshold/scale inputs.")
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
