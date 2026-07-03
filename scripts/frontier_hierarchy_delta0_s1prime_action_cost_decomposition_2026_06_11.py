#!/usr/bin/env python3
"""DELTA0 block10a: action-cost decomposition of the S1' composite target
+ landed-supplier displacement scan

    docs/HIERARCHY_DELTA0_S1PRIME_ACTION_COST_DECOMPOSITION_
    NOTE_2026-06-11.md

Block10a of the DELTA0 attachment campaign (the formulation-tightening
half of the attack wave).  Block02
(docs/HIERARCHY_DELTA0_RATIO_NORMALIZED_ALPHA_S_PER_DECOUPLING_
REDUCTION_NOTE_2026-06-11.md) reduced B4/DELTA0 closure to ONE factor
alpha_s = alpha_bare/u_0^2 = 0.1033038 per taste decoupling; block09
(docs/HIERARCHY_DELTA0_S1_EXACT_ONE_LINK_STRONG_COUPLING_PROBE_
NOTE_2026-06-11.md) eliminated standalone S1 and refined the surviving
route to the composite S1' (rationals from the links, the 4 pi only
from the Green-kernel/Plancherel chain).

What this runner establishes (bounded, exact arithmetic over declared
inputs; REFORMULATION, not progress on the attachment itself):

  Section A (T1, classes [C]/[A]/[B]): EXACT REWRITE.  The reduced
      per-decoupling target alpha_s = 1/(4 pi u_0^2) at g_bare = 1 is
      equivalent, in effective-action units, to a per-decoupling action
      cost
          Delta_S := ln(1/alpha_s) = ln(4 pi) + 2 ln(u_0)
                   = ln(4 pi) + (1/2) ln(<P>)
                   = 2.531024 - 0.260943 = 2.270081,
      with exp(-Delta_S) = 0.1033038 (signs: u_0 < 1 so ln u_0 < 0;
      1/alpha_s = 4 pi u_0^2).  STRUCTURAL CONSEQUENCE: the composite
      S1' target is ADDITIVE in action units with BOTH summands landed
      AS VALUES — ln(4 pi) is the Green-kernel/Plancherel chain's
      normalization constant (its only landed supplier) and
      (1/2) ln(<P>) is half the log of the B1-licensed plaquette.  What
      remains open is ONLY the per-threshold attachment.  This is the
      narrowest posing of B4 to date — and it is a REFORMULATION, not
      progress on the attachment itself.

  Section B (T2, classes [A]/[B]): FULL-CHAIN ACTION BOOKKEEPING
      (exact, over declared inputs, class-fenced, no closure claim).
      From v_cand = M_Pl (7/8)^(1/4) alpha_LM^16 with
      alpha_LM = 1/(4 pi u_0):
          ln(M_Pl/v_cand) = 16 [ln(4 pi) + ln(u_0)] - (1/4) ln(7/8)
                          = 40.4964 - 2.0875 + 0.0334 = 38.4422,
      per-rung ln(1/alpha_LM) = 2.400553 (the YT-P2 retained 2.4006).
      Per-rung budget: kernel-normalization share ln(4 pi) = 2.5310
      (105.4% of the rung), tadpole share ln(u_0) = -0.1304 (-5.4%);
      transport split (block02): determinant-supplied ln(1/u_0) =
      +0.1304 + transport-required Delta_S = 2.2701.  HEADLINE (exact
      bookkeeping over declared inputs, NOT a derivation): the 4 pi
      kernel normalization alone supplies 16 x ln(4 pi) = 40.50 of the
      total 38.44 log-suppression — MORE than all of it; the tadpole
      gives the negative correction (-2.0875) and the (7/8)^(1/4)
      selector a small POSITIVE one (+0.0334; it suppresses v_cand
      further).  The hierarchy's magnitude, in the framework's own
      decomposition, IS sixteen kernel normalizations.

  Section C (T3, classes [A]/[B]): LANDED-SUPPLIER DISPLACEMENT SCAN
      (the falsifiable content).  Every landed or computable per-mode
      action-like quantity in the campaign's rows, with displacement
      from Delta_S = 2.2701 and from the rung 2.4006:
        (a) ln(2 u_0)        = 0.5627  (block01 per-mode determinant log)
        (b) ln(u_0)          = -0.1304 (block02 ratio-normalized log)
        (c) ln((2 pi)^4/16)  = 4.5789; ln((2 pi)^3/8) = 3.4342 (BZ Haar
            cells on the 2^4 / 2^3 blocks)
        (d) ln(4 pi)         = 2.5310 (the kernel normalization itself)
        (e) ln(1/G(0))       = 1.3754 (Z^3 return Green value, computed
            deterministically: BZ sums L = 24, 32, 40 + Richardson)
        (f) ln(1/c0)         = 3.6251 (block08 one-loop bubble c0)
        (g) ln(N_c) = 1.0986, ln(2 N_c) = 1.7918, ln(N_c^2) = 2.1972.
      Exact identities surfaced by the scan: (b)'s displacement from
      Delta_S is EXACTLY the rung (Delta_S - ln u_0 = ln(4 pi u_0));
      (a)'s displacement from the rung is EXACTLY ln(2 pi); (d)'s
      displacement from Delta_S is EXACTLY |2 ln u_0| (exp gap u_0^2) —
      NOT numerology: 'one kernel normalization per decoupling,
      tadpole-corrected by the two dressed links' is the S1' composite
      target RESTATED, i.e. the DEFINITION of Delta_S; (g)'s
      displacement exponentiates to exactly block09's flagged
      4 pi u_0^2/9 = 1.075576 (the 7.56% 1/N_c^2 observation restated
      in action units).  VERDICT LOGIC: NO scanned object matches
      Delta_S inside the action tolerance 0.01 (1% multiplicative);
      nearest is ln(N_c^2) at 0.0729.  The structurally exact
      decomposition remains (d) + tadpole: ln(4 pi) + 2 ln(u_0), both
      values landed, attachment open.

  Section D (T4, class [B] + residuals): WHAT AN ATTACHMENT DERIVATION
      MUST NOW LOOK LIKE (boundary-setting, not speculation).  The open
      theorem: 'each taste-threshold decoupling inserts exactly one
      static-source kernel readout (supplying ln 4 pi) across exactly
      two tadpole-dressed links (supplying 2 ln u_0)'.  Testable
      consequences and the kill criterion are printed as RESIDUAL
      (declared-open) lines, never as PASSes and never as FAILs.

  Terminal class-D fence: no PDG comparator is needed or consumed; a
      self-scan certifies the PDG VEV literal is absent from this
      runner's source.

Vocabulary discipline: nothing here is 'derived' past its declared
premises.  T1-T3 are exact arithmetic over declared inputs (B1
plaquette license; I2 alpha convention on the I3 g_bare = 1 surface,
cited through block02); the T2 headline is bookkeeping over the
declared candidate map, never a derivation of the hierarchy; T4 is
boundary-setting; all unsupplied content is declared as RESIDUAL lines.

Deterministic, pure Python stdlib (fractions, math), no network, no
randomness, runtime seconds (Watson BZ sums are the largest item,
L = 40 -> 64000 terms).  Exit code 0 iff TOTAL: PASS=n FAIL=0.
"""
from __future__ import annotations

import math
import sys
from fractions import Fraction
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"
PARENT_NOTE = (DOCS / "HIERARCHY_DELTA0_S1PRIME_ACTION_COST_"
                      "DECOMPOSITION_NOTE_2026-06-11.md")

PASS_COUNT = 0
FAIL_COUNT = 0
RESIDUAL_COUNT = 0
CLASS_COUNTS = {"A": 0, "B": 0, "C": 0, "D": 0}


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


def residual(msg: str) -> None:
    global RESIDUAL_COUNT
    RESIDUAL_COUNT += 1
    print(f"  RESIDUAL (declared-open): {msg}")


# ---------------------------------------------------------------------------
# Declared boundary inputs (cited, not asserted; see the parent note).
#   <P> = 0.5934 consumed ONLY under the B1 reuse license of
#   docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md; alpha_bare = 1/(4 pi) enters
#   via the I2 convention row + I3 g_bare = 1 surface (cited through
#   block02); c0 is block08's lattice-regulated one-loop bubble constant
#   (declared input, cited); the Watson reference value is a
#   parallel-reference cross-check ONLY (the runner computes G(0) itself).
# ---------------------------------------------------------------------------
P_BOUNDARY = 0.5934                  # B1 licensed reuse number (4 d.p.)
U_0 = P_BOUNDARY ** 0.25             # = 0.877681381
ALPHA_BARE = 1.0 / (4.0 * math.pi)   # I2 convention at I3 g_bare = 1
ALPHA_LM = ALPHA_BARE / U_0          # = 0.0906678
ALPHA_S = ALPHA_BARE / U_0 ** 2      # = 0.1033038 (the block02 target)
C0_BLOCK08 = 0.0266477               # block08 one-loop bubble constant
G0_WATSON_REF = 0.2527310098         # parallel-reference Watson value
N_C = 3

LN_4PI = math.log(4.0 * math.pi)     # = 2.531024
LN_U0 = math.log(U_0)                # = -0.130472 (u_0 < 1: negative)
DELTA_S = LN_4PI + 2.0 * LN_U0       # = 2.270081 (the action cost)
RUNG = LN_4PI + LN_U0                # = 2.400553 (= ln(1/alpha_LM))


# ---------------------------------------------------------------------------
# Section A — T1: the exact action-cost rewrite.
# ---------------------------------------------------------------------------
def section_a():
    print("\n--- Section A [C]/[A]/[B]: T1 — exact rewrite of the "
          "reduced target as a per-decoupling action cost ---")

    # A1 [C]: exact multiplicative skeleton at rational stand-ins.  With
    # Fraction stand-ins q (for 4 pi) and u (for u_0), the identities
    # whose logs Sections A/B take are exact rational algebra:
    #   1/alpha_s = q u^2;  1/alpha_LM = q u = (q u^2)/u;
    #   (q u)^16 = q^16 u^16  (kernel^16 x tadpole^16 rung split).
    skel_ok = True
    for q in (Fraction(22, 7), Fraction(355, 113)):
        for u in (Fraction(2, 3), Fraction(7, 8)):
            a_s = 1 / (q * u ** 2)
            a_lm = 1 / (q * u)
            skel_ok = skel_ok and (1 / a_s == q * u ** 2)
            skel_ok = skel_ok and (1 / a_lm == (q * u ** 2) / u)
            skel_ok = skel_ok and ((q * u) ** 16 == q ** 16 * u ** 16)
            skel_ok = skel_ok and (a_lm ** 16 == a_s ** 16 * u ** 16)
    check("C", "A1 exact multiplicative skeleton (Fraction stand-ins q "
               "for 4 pi, u for u_0; 4 rational test points): "
               "1/alpha_s = q u^2, 1/alpha_LM = q u = (q u^2)/u, "
               "(q u)^16 = q^16 u^16, alpha_LM^16 = alpha_s^16 u^16 — "
               "the additive action identities of A2/B1/B4/B5 are the "
               "exact logs of these", skel_ok,
          "exact Fraction arithmetic")

    # A2 [A]: the action-cost identity, three routes.
    ds_route1 = math.log(1.0 / ALPHA_S)
    ds_route2 = LN_4PI + 2.0 * LN_U0
    ds_route3 = LN_4PI + 0.5 * math.log(P_BOUNDARY)
    check("A", "A2 ACTION-COST IDENTITY: Delta_S := ln(1/alpha_s) = "
               "ln(4 pi) + 2 ln(u_0) = ln(4 pi) + (1/2) ln(<P>) = "
               "2.531024 + (-0.260943) = 2.270081 — three routes agree "
               "< 1e-12; the composite target is ADDITIVE in action "
               "units",
          abs(ds_route1 - ds_route2) < 1e-12
          and abs(ds_route1 - ds_route3) < 1e-12
          and abs(ds_route1 - 2.270081) < 5e-7
          and abs(LN_4PI - 2.531024) < 5e-7
          and abs(2.0 * LN_U0 + 0.260943) < 5e-7,
          f"Delta_S = {ds_route1:.10f}")

    # A3 [A]: sign honesty + exact inversion.
    check("A", "A3 sign honesty + inversion: u_0 < 1 so ln(u_0) < 0 "
               "(the tadpole REDUCES the cost of the 4 pi piece); "
               "1/alpha_s = 4 pi u_0^2 < 1e-12 relative; "
               "exp(-Delta_S) = 0.1033038 = alpha_s < 1e-12",
          U_0 < 1.0 and LN_U0 < 0.0
          and abs(1.0 / ALPHA_S / (4.0 * math.pi * U_0 ** 2) - 1.0) < 1e-12
          and abs(math.exp(-DELTA_S) / ALPHA_S - 1.0) < 1e-12
          and abs(math.exp(-DELTA_S) - 0.1033038) < 5e-8,
          f"exp(-Delta_S) = {math.exp(-DELTA_S):.7f}")

    # A4 [B]: both summands are landed AS VALUES.
    planch = (DOCS / "ALPHA_BARE_FOUR_PI_FROM_Z3_PLANCHEREL_BRIDGE_"
                     "BOUNDED_NOTE_2026-05-26.md")
    plaq = DOCS / "PLAQUETTE_SELF_CONSISTENCY_NOTE.md"
    planch_text = planch.read_text() if planch.exists() else ""
    plaq_text = plaq.read_text() if plaq.exists() else ""
    check("B", "A4 both summands landed AS VALUES, suppliers on disk: "
               "ln(4 pi) — the Plancherel/Green-kernel bridge "
               "(alpha_bare = 1/(4 pi) at g_bare = 1, the 4 pi's only "
               "landed supplier); (1/2) ln(<P>) — the B1-licensed "
               "plaquette (<P> = 0.5934, 'admitted comparison/reuse "
               "number')",
          "alpha_bare = 1 / (4 pi)" in planch_text
          and "Green-Kernel Composition Bridge" in planch_text
          and "admitted comparison/reuse number" in plaq_text
          and "0.5934" in plaq_text)

    # A5 [B]: reformulation honesty in the parent note.
    note_text = PARENT_NOTE.read_text() if PARENT_NOTE.exists() else ""
    lowered = " ".join(note_text.lower().split())
    required = [
        "reformulation",
        "not progress on the attachment",
        "does not close the delta0 gate",
        "narrowest posing",
    ]
    forbidden = [
        "closes the delta0 gate",
        "derives the attachment",
    ]
    req_missing = [t for t in required if t not in lowered]
    forb_hit = [t for t in forbidden if t in lowered]
    check("B", "A5 reformulation honesty: parent note on disk declares "
               "the rewrite a REFORMULATION ('not progress on the "
               "attachment'), the 'narrowest posing' of B4 to date, and "
               "that it 'does not close the DELTA0 gate'; forbidden "
               "closure tokens absent", not req_missing and not forb_hit,
          f"missing = {req_missing}, hit = {forb_hit}")


# ---------------------------------------------------------------------------
# Section B — T2: full-chain action bookkeeping.
# ---------------------------------------------------------------------------
def section_b():
    print("\n--- Section B [A]/[B]: T2 — full-chain action bookkeeping "
          "(exact over declared inputs; class-fenced, no closure "
          "claim) ---")

    selector = -0.25 * math.log(7.0 / 8.0)        # = +0.033383 (positive)
    total_decomp = 16.0 * (LN_4PI + LN_U0) + selector
    total_direct = -math.log((7.0 / 8.0) ** 0.25 * ALPHA_LM ** 16)

    # B1 [A]: the full-chain identity.
    check("A", "B1 FULL-CHAIN IDENTITY: ln(M_Pl/v_cand) = "
               "16 [ln(4 pi) + ln(u_0)] - (1/4) ln(7/8) = 38.442225, "
               "verified < 1e-12 against the direct evaluation of "
               "v_cand/M_Pl = (7/8)^(1/4) alpha_LM^16",
          abs(total_decomp - total_direct) < 1e-12
          and abs(total_decomp - 38.442225) < 5e-6,
          f"decomp = {total_decomp:.12f}, direct = {total_direct:.12f}")

    # B2 [A]: the per-rung log-interval cross-check.
    check("A", "B2 per-rung cross-check: ln(4 pi) + ln(u_0) = "
               "ln(1/alpha_LM) = 2.400553 — the YT-P2 note's retained "
               "per-rung log-interval 2.4006 at its quoted 4 d.p.; "
               "16 rungs span 38.408842",
          abs(RUNG - math.log(1.0 / ALPHA_LM)) < 1e-12
          and abs(RUNG - 2.4006) < 5e-5
          and abs(16.0 * RUNG - 38.408842) < 5e-6,
          f"rung = {RUNG:.10f}")

    # B3 [B]: the consumed chain objects on disk.
    yt = DOCS / "YT_P2_TASTE_STAIRCASE_BETA_FUNCTIONS_NOTE_2026-04-17.md"
    hs = DOCS / "HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md"
    yt_text = yt.read_text() if yt.exists() else ""
    hs_text = hs.read_text() if hs.exists() else ""
    check("B", "B3 chain objects on disk: YT-P2 retained per-rung "
               "constant 'ln(alpha_LM) = -2.4006' present; the "
               "honest-status note's declared candidate map "
               "v_cand = M_Pl x (7/8)^(1/4) x alpha_LM^16 present "
               "(declared boundary inputs, cited not asserted)",
          "ln(alpha_LM) = -2.4006" in yt_text
          and "(7/8)^(1/4)" in hs_text and "alpha_LM^16" in hs_text)

    # B4 [A]: the budget table + the headline.
    kernel_total = 16.0 * LN_4PI         # = 40.496388
    tadpole_total = 16.0 * LN_U0         # = -2.087546
    closes = abs(kernel_total + tadpole_total + selector
                 - total_direct) < 1e-12
    print("      per-rung budget: kernel ln(4 pi) = "
          f"{LN_4PI:.6f} ({LN_4PI / RUNG * 100:.1f}% of the rung), "
          f"tadpole ln(u_0) = {LN_U0:.6f} "
          f"({LN_U0 / RUNG * 100:.1f}%)")
    print("      full-chain budget: kernel 16 ln(4 pi) = "
          f"{kernel_total:.4f}, tadpole 16 ln(u_0) = "
          f"{tadpole_total:.4f}, selector -(1/4) ln(7/8) = "
          f"+{selector:.6f}, total = {total_direct:.4f}")
    check("A", "B4 HEADLINE (exact bookkeeping over declared inputs, "
               "NOT a derivation): the 4 pi kernel normalization ALONE "
               "supplies 16 x ln(4 pi) = 40.4964 of the total 38.4422 "
               "log-suppression (105.3%) — MORE than all of it; the "
               "tadpole supplies the negative correction (-2.0875) and "
               "the (7/8)^(1/4) selector a small POSITIVE one "
               "(+0.0334: it suppresses v_cand further).  The "
               "hierarchy's magnitude, in the framework's own "
               "decomposition, IS sixteen kernel normalizations",
          closes and kernel_total > total_direct
          and abs(kernel_total - 40.496388) < 5e-6
          and abs(tadpole_total + 2.087546) < 5e-6
          and abs(selector - 0.033383) < 5e-7
          and tadpole_total < 0.0 and selector > 0.0,
          f"16 ln(4 pi) = {kernel_total:.4f} > total = "
          f"{total_direct:.4f}; sum closes < 1e-12")

    # B5 [A]: the transport split of the rung (block02's split).
    det_share = -LN_U0                   # determinant supplies u_0 per rung
    check("A", "B5 transport split of the rung (block02): rung = "
               "Delta_S + ln(1/u_0) — determinant-supplied share "
               "ln(1/u_0) = +0.130472 (the block determinant's u_0 per "
               "rung), transport-required share Delta_S = 2.270081 "
               "(the open attachment) — closes < 1e-12; NOTE the u_0 "
               "role flips sign between the two exact rung splits "
               "(kernel + tadpole vs determinant + transport)",
          abs(DELTA_S + det_share - RUNG) < 1e-12
          and abs(det_share - 0.130472) < 5e-7,
          f"{DELTA_S:.6f} + {det_share:.6f} = {RUNG:.6f}")


# ---------------------------------------------------------------------------
# Section C — T3: landed-supplier displacement scan.
# ---------------------------------------------------------------------------
def watson_g0(L: int) -> float:
    """Z^3 return Green value G(0) on the half-shifted (zero-mode-free)
    L^3 BZ grid: G(0) = (1/L^3) sum_k 1/k_hat^2,
    k_hat^2 = sum_mu (2 - 2 cos k_mu), k_mu = 2 pi (n + 1/2)/L.
    Deterministic; finite-L error O(1/L) (alternating-image constant),
    removed by two-point Richardson in 1/L."""
    c = [2.0 - 2.0 * math.cos(2.0 * math.pi * (n + 0.5) / L)
         for n in range(L)]
    s = 0.0
    for a in c:
        for b in c:
            ab = a + b
            s += sum(1.0 / (ab + cc) for cc in c)
    return s / L ** 3


def section_c():
    print("\n--- Section C [A]/[B]: T3 — landed-supplier displacement "
          "scan vs Delta_S = 2.2701 and the rung 2.4006 ---")

    scanned = {}   # name -> action value (for the C9 verdict logic)

    # C1 [A]: (a) block01's per-mode determinant log ln(2 u_0).
    a_val = math.log(2.0 * U_0)
    scanned["(a) ln(2 u_0)"] = a_val
    check("A", "C1 scan (a), block01 per-mode determinant log: "
               "ln(2 u_0) = 0.562676; displacement from Delta_S = "
               "1.707405, from the rung = 1.837877 = ln(2 pi) EXACTLY "
               "(rung - ln(2 u_0) = ln(4 pi u_0/(2 u_0)) = ln(2 pi))",
          abs(a_val - 0.562676) < 5e-7
          and abs(DELTA_S - a_val - 1.707405) < 5e-7
          and abs(RUNG - a_val - math.log(2.0 * math.pi)) < 1e-12,
          f"ln(2 u_0) = {a_val:.6f}")

    # C2 [A]: (b) block02's ratio-normalized per-mode log ln(u_0).
    scanned["(b) ln(u_0)"] = LN_U0
    check("A", "C2 scan (b), block02 ratio-normalized per-mode log: "
               "ln(u_0) = -0.130472; displacement from Delta_S = "
               "2.400553 = the RUNG exactly (Delta_S - ln u_0 = "
               "ln(4 pi) + ln(u_0)), and from the rung = 2.531024 = "
               "ln(4 pi) exactly — both identities < 1e-12",
          abs((DELTA_S - LN_U0) - RUNG) < 1e-12
          and abs((RUNG - LN_U0) - LN_4PI) < 1e-12,
          f"ln(u_0) = {LN_U0:.6f}")

    # C3 [A]: (c) per-mode BZ Haar cells on the 2^4 and 2^3 blocks.
    h4 = math.log((2.0 * math.pi) ** 4 / 16.0)
    h3 = math.log((2.0 * math.pi) ** 3 / 8.0)
    scanned["(c) ln((2 pi)^4/16)"] = h4
    scanned["(c) ln((2 pi)^3/8)"] = h3
    check("A", "C3 scan (c), per-mode BZ Haar cells: "
               "ln((2 pi)^4/16) = 4 ln(pi) = 4.578920 (displacement "
               "from Delta_S = +2.308839); 3D variant ln((2 pi)^3/8) = "
               "3 ln(pi) = 3.434190 (displacement +1.164109) — both "
               "far above; note (2 pi/2)^d = pi^d exactly",
          abs(h4 - 4.578920) < 5e-6 and abs(h3 - 3.434190) < 5e-6
          and abs(h4 - 4.0 * math.log(math.pi)) < 1e-12
          and abs(h3 - 3.0 * math.log(math.pi)) < 1e-12
          and abs(h4 - DELTA_S - 2.308839) < 5e-6
          and abs(h3 - DELTA_S - 1.164109) < 5e-6,
          f"h4 = {h4:.6f}, h3 = {h3:.6f}")

    # C4 [A]: (d) the kernel normalization ln(4 pi) itself — the
    # near-miss that is EXACTLY the S1' composite restated.
    scanned["(d) ln(4 pi)"] = LN_4PI
    gap_d = LN_4PI - DELTA_S
    check("A", "C4 scan (d), the kernel normalization ln(4 pi) = "
               "2.531024 itself: displacement from Delta_S = 0.260943 "
               "= |2 ln u_0| EXACTLY (exp gap = u_0^2 = 0.770325, i.e. "
               "the kernel normalization ALONE overshoots Delta_S by "
               "exactly the two-link tadpole; 11.5% of Delta_S in "
               "action units); displacement from the rung = 0.130472 = "
               "|ln u_0| exactly.  NOT numerology — DEFINITIONALLY "
               "EXACT: 'one kernel normalization per decoupling, "
               "tadpole-corrected by the two dressed links' is the S1' "
               "composite target RESTATED, Delta_S = ln(4 pi) + "
               "2 ln(u_0) being its definition",
          abs(gap_d - (-2.0 * LN_U0)) < 1e-12
          and abs(math.exp(-gap_d) - U_0 ** 2) < 1e-12
          and abs((LN_4PI - RUNG) - (-LN_U0)) < 1e-12
          and abs(gap_d / DELTA_S - 0.114949) < 5e-6,
          f"gap = {gap_d:.6f} = |2 ln u_0|, exp gap = "
          f"{math.exp(-gap_d):.6f} = u_0^2")

    # C5 [A]: (e) the Z^3 return Green value G(0), computed.
    g = {L: watson_g0(L) for L in (24, 32, 40)}
    def rich(l1, l2):
        return (l2 * g[l2] - l1 * g[l1]) / (l2 - l1)
    r_lo, r_hi = rich(24, 32), rich(32, 40)
    g0 = r_hi                                # production estimate
    e_val = math.log(1.0 / g0)
    scanned["(e) ln(1/G(0))"] = e_val
    check("A", "C5 scan (e), Z^3 return Green value (computed here, "
               "deterministic): G(0) via half-shifted BZ sums at "
               "L = 24, 32, 40 with two-point Richardson in 1/L — "
               "pair estimates agree < 2e-5, production G(0) = "
               "0.252736 matches the parallel-reference Watson value "
               "0.2527310098 within the declared 5e-5; "
               "ln(1/G(0)) = 1.375409, displacement from Delta_S = "
               "0.894672",
          abs(r_lo - r_hi) < 2e-5
          and abs(g0 - G0_WATSON_REF) < 5e-5
          and abs(e_val - 1.375409) < 5e-5
          and abs(DELTA_S - e_val - 0.894672) < 5e-5,
          f"G(0) = {g0:.7f} (pairs {r_lo:.7f}/{r_hi:.7f}), "
          f"ln(1/G(0)) = {e_val:.6f}")

    # C6 [B]: (f) block08's one-loop bubble c0 — declared input on disk.
    s2 = (DOCS / "HIERARCHY_DELTA0_S2_READOUT_DRESSING_LEADING_ORDER_"
                 "PROBE_NOTE_2026-06-11.md")
    s2_text = s2.read_text() if s2.exists() else ""
    f_val = math.log(1.0 / C0_BLOCK08)
    scanned["(f) ln(1/c0)"] = f_val
    check("B", "C6 scan (f), block08 one-loop bubble constant "
               "c0 = 0.0266477 (declared input, literal verified on "
               "disk in the block08 note): ln(1/c0) = 3.625052, "
               "displacement from Delta_S = 1.354971",
          "0.0266477" in s2_text
          and abs(f_val - 3.625052) < 5e-6
          and abs(f_val - DELTA_S - 1.354971) < 5e-6,
          f"ln(1/c0) = {f_val:.6f}")

    # C7 [A]: (g) the strong-coupling weights.
    g_nc = math.log(N_C)
    g_2nc = math.log(2 * N_C)
    g_nc2 = math.log(N_C ** 2)
    scanned["(g) ln(N_c)"] = g_nc
    scanned["(g) ln(2 N_c)"] = g_2nc
    scanned["(g) ln(N_c^2)"] = g_nc2
    gap_g = DELTA_S - g_nc2
    check("A", "C7 scan (g), strong-coupling weights: ln(N_c) = "
               "1.098612 (displacement from Delta_S = 1.171469), "
               "ln(2 N_c) = 1.791759 (0.478321), ln(N_c^2) = 2.197225 "
               "(0.072856 — the NEAREST scanned object); "
               "exp(0.072856) = 1.075576 = block09's flagged "
               "4 pi u_0^2/9 EXACTLY: the 7.56% 1/N_c^2 numerology-risk "
               "observation RESTATED in action units, nothing more",
          abs(DELTA_S - g_nc - 1.171469) < 5e-7
          and abs(DELTA_S - g_2nc - 0.478321) < 5e-7
          and abs(gap_g - 0.072856) < 5e-7
          and abs(math.exp(gap_g)
                  - 4.0 * math.pi * U_0 ** 2 / 9.0) < 1e-12
          and abs(math.exp(gap_g) - 1.075576) < 5e-7,
          f"exp gap = {math.exp(gap_g):.6f}")

    # C8 [B]: block09's numerology flag on disk (cross-reference).
    s1 = (DOCS / "HIERARCHY_DELTA0_S1_EXACT_ONE_LINK_STRONG_COUPLING_"
                 "PROBE_NOTE_2026-06-11.md")
    s1_text = s1.read_text() if s1.exists() else ""
    check("B", "C8 cross-reference on disk: block09's §5 numerology-"
               "risk flag for the 1/N_c^2 proximity is present "
               "('4 pi u_0^2/9 = 1.075576', 'fails at 7.56%', "
               "'NUMEROLOGY RISK') — C7 restates that flagged "
               "observation in action units and adds NO content to it",
          "4 pi u_0^2/9 = 1.075576" in s1_text
          and "FAILS at 7.56%" in s1_text
          and "NUMEROLOGY RISK" in s1_text)

    # C9 [A]: the verdict logic.
    tol = 0.01    # action-units tolerance (1% multiplicative)
    gaps = {k: abs(v - DELTA_S) for k, v in scanned.items()}
    nearest = min(gaps, key=gaps.get)
    print("      displacement table (action units, vs Delta_S "
          f"= {DELTA_S:.6f} / rung = {RUNG:.6f}):")
    for k, v in scanned.items():
        print(f"        {k:24s} = {v:+.6f}   |gap Delta_S| = "
              f"{abs(v - DELTA_S):.6f}   |gap rung| = "
              f"{abs(v - RUNG):.6f}")
    check("A", "C9 VERDICT LOGIC: NO scanned landed/computable "
               "per-mode action-like quantity matches Delta_S inside "
               "the declared action tolerance 0.01 (1% multiplicative) "
               "— nearest is ln(N_c^2) at 0.0729, 7.3x outside; the "
               "structurally exact decomposition remains (d) + tadpole, "
               "Delta_S = ln(4 pi) + 2 ln(u_0), with both values landed "
               "and the attachment open",
          min(gaps.values()) > tol
          and nearest == "(g) ln(N_c^2)"
          and abs(gaps[nearest] - 0.072856) < 5e-7,
          f"min gap = {min(gaps.values()):.6f} ({nearest})")


# ---------------------------------------------------------------------------
# Section D — T4: what an attachment derivation must now look like
# (boundary-setting, not speculation) + declared-open residuals.
# ---------------------------------------------------------------------------
def section_d():
    print("\n--- Section D [B] + residuals: T4 — the open attachment "
          "theorem (boundary-setting, not speculation) ---")

    note_text = PARENT_NOTE.read_text() if PARENT_NOTE.exists() else ""
    lowered = " ".join(note_text.lower().split())
    required = [
        "exactly one static-source kernel readout",
        "exactly two tadpole-dressed links",
        "kill criterion",
        "k-dependent per-rung cost",
        "boundary-setting",
    ]
    req_missing = [t for t in required if t not in lowered]
    check("B", "D1 boundary-setting honesty: parent note on disk states "
               "the open theorem ('exactly one static-source kernel "
               "readout' across 'exactly two tadpole-dressed links'), "
               "its testable consequences, and its kill criterion "
               "('k-dependent per-rung cost'), all fenced as "
               "boundary-setting", not req_missing,
          f"missing = {req_missing}")

    print()
    residual("the PER-THRESHOLD ATTACHMENT theorem is UNSUPPLIED — the "
             "narrowest posing of B4 to date: 'each taste-threshold "
             "decoupling inserts exactly one static-source kernel "
             "readout (supplying ln 4 pi) across exactly two "
             "tadpole-dressed links (supplying 2 ln u_0)'.  Testable "
             "consequences if derived: the per-rung cost is exactly "
             "Delta_S = 2.270081 INDEPENDENT of the threshold index k "
             "(consistent with the exact integer-16 power law); it "
             "predicts ZERO per-rung drift, contrastable with any "
             "future MC threshold measurement; and it ties B4 closure "
             "to the SAME I1/M1 Green-kernel/Plancherel audit surface "
             "that closed the alpha_bare VALUE — one audit surface "
             "would carry both.  KILL CRITERION for this formulation: "
             "any derivation producing a k-dependent per-rung cost, or "
             "a kernel-insertion count different from 1 per threshold, "
             "eliminates it.")
    residual("the DELTA0/B4 magnitude gate "
             "(HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_"
             "2026-05-30.md) remains OPEN: this block REWRITES the "
             "block02 reduced target in action units (a reformulation "
             "with both summands landed as values) and scans the landed "
             "suppliers for a match (none inside tolerance); it "
             "supplies NO attachment rule and is NOT progress on the "
             "attachment itself.")


# ---------------------------------------------------------------------------
# Terminal class-D fence (external comparators).
# ---------------------------------------------------------------------------
def section_fence():
    print("\n--- Terminal class-D fence: external comparators ---")
    print("  (No PDG quantity is needed or consumed by this "
          "decomposition; the action")
    print("   bookkeeping and the displacement scan are internal "
          "structure only.)")
    src = Path(__file__).read_text()
    pdg_literal = "246." + "22"  # composed so the scan finds only real uses
    check("D", "G1 self-scan: the PDG VEV literal appears ZERO times in "
               "this runner's source — no comparator consumed anywhere",
          src.count(pdg_literal) == 0)


def main() -> int:
    print("=" * 78)
    print(" frontier_hierarchy_delta0_s1prime_action_cost_decomposition_"
          "2026_06_11.py")
    print(" Block10a of the DELTA0 attachment campaign: the S1' composite "
          "target")
    print(" rewritten EXACTLY as a per-decoupling action cost Delta_S = "
          "ln(4 pi) +")
    print(" 2 ln(u_0) = 2.270081 (both summands landed as values), the "
          "full-chain")
    print(" action budget (16 kernel normalizations), and the landed-"
          "supplier")
    print(" displacement scan.  REFORMULATION, not progress on the "
          "attachment itself.")
    print(" Parent note: docs/HIERARCHY_DELTA0_S1PRIME_ACTION_COST_"
          "DECOMPOSITION_")
    print("              NOTE_2026-06-11.md")
    print("=" * 78)

    section_a()
    section_b()
    section_c()
    section_d()
    section_fence()

    print()
    print("=" * 78)
    print(f" Breakdown: A={CLASS_COUNTS['A']} B={CLASS_COUNTS['B']} "
          f"C={CLASS_COUNTS['C']} D={CLASS_COUNTS['D']} "
          f"RESIDUAL={RESIDUAL_COUNT}")
    print(f" TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(" VERDICT: established (bounded, exact arithmetic over declared "
          "inputs): the")
    print("   block02 reduced target is EXACTLY the per-decoupling action "
          "cost Delta_S")
    print("   = ln(4 pi) + 2 ln(u_0) = ln(4 pi) + (1/2) ln(<P>) = "
          "2.270081, additive")
    print("   with both summands landed as values; the full hierarchy "
          "suppression is")
    print("   exact bookkeeping 16 [ln(4 pi) + ln(u_0)] - (1/4) ln(7/8) = "
          "38.4422, of")
    print("   which the kernel normalization alone supplies 40.4964 — "
          "sixteen kernel")
    print("   normalizations, tadpole-corrected; and NO scanned landed "
          "supplier matches")
    print("   Delta_S inside 0.01 action units (nearest: ln(N_c^2) at "
          "0.0729, block09's")
    print("   flagged observation restated).  NOT established: the "
          "per-threshold")
    print("   attachment theorem (one kernel readout across two dressed "
          "links per")
    print("   decoupling) — declared open with its kill criterion; this "
          "is the")
    print("   narrowest posing of B4 to date, a reformulation, NOT "
          "progress on the")
    print("   attachment itself.  DELTA0 stays open.")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
