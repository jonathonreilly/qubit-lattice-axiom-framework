#!/usr/bin/env python3
"""DELTA0 B4 probe: grade the LANDED NJL-RPA condensate susceptibility as
the channel-projected normalization Z for the taste-transfer attachment.

    docs/HIERARCHY_DELTA0_B4_NJL_RPA_NORMALIZATION_PROBE_NOTE_2026-06-13.md

SETTING (Derive-Z).  The taste-transfer-ladder PROPOSAL
(HIERARCHY_DELTA0_B4_TASTE_TRANSFER_LADDER_THEORY_PROBE_NOTE_2026-06-11.md)
is the campaign's first B4-attachment mechanism satisfying every block11
constraint (outside K1-K8; log-additive; threshold-scale; two-link
u_0^(-2) dressing; d = 3 kernel).  Its declared one-exchange vertex has
u_0-degree EXACTLY -2 (the mechanism-required power), but a STRUCTURAL
magnitude ceiling: with the exchange normalized by the dressed-kinetic
denominator (E_t + E_t')^2 = (4 u_0)^2 = 16 u_0^2,

    factor/alpha_s = sigma_U^2 * W / 16  <=  3/32 = 0.09375
                                          (W = 3/2 incoherent, sigma_U^2 < 1),

i.e. >= 10.7x short of alpha_s.  Its S6 OPEN content is the
channel-projected condensate normalization that replaces 16 u_0^2.

THE LANDED CANDIDATE for that normalization is the NJL-style condensate
susceptibility (V_EFF_TOTAL_NJL_STYLE_BOUNDED_THEOREM_NOTE_2026-05-10.md):
the symmetric-point fermion bubble Pi(0) = -V_taste''(0) = 4/u_0^2, with
1/Pi(0) = u_0^2/4 = G_critical EXACTLY, and the RPA / Hubbard-Stratonovich
condensate susceptibility

    chi = G_eff / (1 - G_eff * Pi(0)) = G_eff / (1 - r),   r = G_eff/G_critical,

at canonical leading-order Kawamoto-Smit G_eff = 1/(2 N_c) = 1/6.  This
probe GRADES that object as the normalization Z.

WHAT THIS PROBE COMPUTES (deterministic, exact where possible):

  Z1 (Section A): reproduce the landed susceptibility chain EXACTLY.
      Pi(0) = 4/u_0^2 = -V_taste''(0) (verified by exact symbolic-style
      second derivative of -8 log(sigma^2 + 4 u_0^2) at sigma = 0),
      G_critical = u_0^2/4, r = G_eff/G_critical = 2/(3 u_0^2) at
      canonical G_eff, and the RPA enhancement 1/(1 - r) — confirm
      7.4314 and r = 0.865436 to < 1e-6 against the recon values.

  Z2 (Section B): the GRADED PRODUCT.  Replace the dressed-kinetic
      denominator 16 u_0^2 with the RPA-susceptibility-normalized vertex
      and compute factor/alpha_s at (a) canonical G_eff, incoherent
      W = 3/2; (b) the block01 phase endpoints (native coherent W = 0,
      one-free-phase-per-bond W = 9/4, arbitrary coherent W = 9).  The
      reading is  factor/alpha_s = (W/16) * [1/(1 - r)]  (the OLD u_0^2
      cancels alpha_s's u_0^(-2); the enhancement is the NEW Z content).
      Confirm canonical-incoherent = (3/32)*7.4314 = 0.6967 = 1.436x
      short; find the (r, W) that JOINTLY hit 1.00.

  Z3 (Section C): THE KILL-CRITERION TEST (load-bearing).  Compute the
      EXACT local u_0-degree of the susceptibility-normalized
      per-threshold vertex by a two-rational-point ratio (block01/block09
      pattern) AND the closed-form logarithmic derivative.  With G_eff a
      FIXED number, the normalized vertex is V_norm(u_0) = c/(u_0^2 - 4
      G_eff): a NON-monomial whose local u_0-degree is
      -2 u_0^2/(u_0^2 - 4 G_eff), strongly u_0-dependent near the
      critical point (~ -14.9 at the physical scale; the RPA enhancement
      leg alone is ~ -12.9, the recon ~ -13 estimate).  The criterion
      requires -2.  It BREAKS unless the enhancement is FROZEN to a pure
      number at the threshold (decoupling-mass) scale, which restores
      degree EXACTLY -2 (verified: V_frozen * u_0^2 = const, identical at
      two rational u_0).  Whether threshold-freezing is licensed is the
      HONEST residual: NO landed object supplies it (the NJL note's chi
      is a symmetric-point object; nothing evaluates G_eff/Pi at a
      decoupling-mass scale and freezes it) — it is an UNSUPPLIED
      assumption.  Recorded as the degree verdict.

  Z4 (Section D): the G_eff band sweep.  For each G_eff form in the NJL
      note's section 6.2 (and the u_0-dressed variants), evaluate r,
      enhancement 1/(1-r), and (3/32)*enhancement; flag which land near
      closure (r ~ 0.906), which sit in the numerology window
      [0.5, 2.0]x alpha_s, and which go broken-phase (r >= 1, chi
      diverges — unphysical for this reading).

  Z5: GRADE.  closure ONLY if a DERIVED (not declared) normalization
      lands in [0.99, 1.01]x alpha_s WITH degree -2; partial if a
      DECLARED-model normalization lands close; displaced if O(1) short;
      kill if the degree criterion provably fires.  The honest outcome
      is CONDITIONAL-KILL: the RPA chi (a DECLARED-model object: Hubbard-
      Stratonovich + scalar-channel-after-Fierz + Kawamoto-Smit G_eff,
      all named admissions in the NJL note) BRACKETS closure in MAGNITUDE
      under the phase dial (incoherent 0.697 short, one-free-phase 1.045
      over; hits 1.00 at W = 2.153 or r = 0.906 — a partial-magnitude
      result) — BUT the as-computed RPA-normalized vertex has u_0-degree
      -14.86, which FIRES the mechanism's own stated kill criterion
      (degree != -2); it is rescued to a closure-bracketing partial ONLY
      under a threshold-freezing that NO landed object supplies.  By the
      grading rule ("kill if the degree criterion provably fires") the
      binding verdict is CONDITIONAL-KILL: killed as computed, partial in
      magnitude only if the unsupplied freezing is granted.  Both closure
      conditions (r = 0.906, a derived Z) are also unlanded.  Not closure.

DECLARED-MODEL FENCES (the chi object is NOT a licensed-surface claim):
Hubbard-Stratonovich auxiliary scalar, scalar-channel dominance after
Fierz, and the Kawamoto-Smit leading-order G_eff = 1/(2 N_c) are ALL
named admissions in the NJL note (its §2 counterfactual table, rows 2-4,
and its §6.2 O(1) G_eff band).  The RPA resummation chi = G_eff/(1 -
G_eff Pi) is the standard ladder sum on top of that declared tree term.
None of it is a licensed framework object; this probe grades it as a
candidate Z, never establishes it.

Deterministic, pure Python stdlib (fractions, math), no network, no
randomness, runtime << 90 s (a fraction of a second).  PASS/FAIL lines,
RESIDUAL (declared-open) lines, OBSERVATION lines for numerology-window
entries with the campaign guard pattern, TOTAL: PASS=n FAIL=0, honest
VERDICT, exit 0 iff FAIL=0, terminal class-D PDG self-scan.
"""
from __future__ import annotations

import math
import sys
from fractions import Fraction
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"
PARENT_NOTE = (DOCS / "HIERARCHY_DELTA0_B4_NJL_RPA_NORMALIZATION_PROBE_"
                      "NOTE_2026-06-13.md")
TASTE_NOTE = (DOCS / "HIERARCHY_DELTA0_B4_TASTE_TRANSFER_LADDER_THEORY_"
                     "PROBE_NOTE_2026-06-11.md")
NJL_NOTE = DOCS / "V_EFF_TOTAL_NJL_STYLE_BOUNDED_THEOREM_NOTE_2026-05-10.md"
KERNEL_NOTE = (DOCS / "HIERARCHY_DELTA0_S1PRIME_TASTE_REGION_KERNEL_SHARE_"
                      "PROBE_NOTE_2026-06-11.md")
ROUTE_NOTE = (DOCS / "HIERARCHY_DELTA0_ATTACHMENT_ROUTE_INVENTORY_"
                     "SYNTHESIS_NOTE_2026-06-11.md")

PASS_COUNT = 0
FAIL_COUNT = 0
RESIDUAL_COUNT = 0
OBSERVATION_COUNT = 0
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


def observation(msg: str) -> None:
    global OBSERVATION_COUNT
    OBSERVATION_COUNT += 1
    print(f"  OBSERVATION (bounded, numerology-risk flagged): {msg}")


# ---------------------------------------------------------------------------
# Declared boundary inputs (cited, not asserted; see the parent and cited
# notes).  <P> = 0.5934 ONLY under the B1 reuse license; alpha_bare =
# 1/(4 pi) via the I2 convention on the I3 g_bare = 1 surface (block02).
# ---------------------------------------------------------------------------
P_BOUNDARY = 0.5934                  # B1 licensed reuse number (4 d.p.)
U0_SQ = math.sqrt(P_BOUNDARY)        # u_0^2 = sqrt(0.5934) = 0.7703246
U_0 = P_BOUNDARY ** 0.25             # = 0.8776814
ALPHA_BARE = 1.0 / (4.0 * math.pi)   # I2 convention at I3 g_bare = 1
ALPHA_S = ALPHA_BARE / U0_SQ         # = 0.1033038 (block02 reduction target)

N_C = 3
G_EFF_CANON = 1.0 / (2 * N_C)        # Kawamoto-Smit LO = 1/6 (DECLARED)
G_CRIT = U0_SQ / 4.0                 # = u_0^2/4 (landed NJL critical coupling)

# Block01 phase structure (exact, from the taste-transfer probe's coherent
# scout): kept-channel transfer weights W (per-bond / all-bond aggregate).
W_INCOH = Fraction(3, 2)             # all-bond incoherent S_all = 3/2
W_ONE_FREE = Fraction(9, 4)          # one-free-phase-per-bond = 2.25
W_ARBITRARY = Fraction(9)            # full arbitrary-phase coherent = 9
W_NATIVE = Fraction(0)               # native coherent sum = 0 (destructive)

# The structural ceiling number of the taste-transfer note (3/2)/16 = 3/32.
S32 = Fraction(3, 32)                # = W_INCOH/16 = sigma_U^2-saturated incoherent


# ---------------------------------------------------------------------------
# Section A — Z1: reproduce the landed susceptibility chain EXACTLY.
# ---------------------------------------------------------------------------
def section_a():
    print("\n--- Section A [A]: Z1 — the LANDED NJL-RPA susceptibility chain "
          "reproduced exactly ---")

    # A1: Pi(0) = -V_taste''(0) = 4/u_0^2.  V_taste(sigma) = -8 log(sigma^2 +
    # 4 u_0^2); V_taste'(sigma) = -16 sigma/(sigma^2 + 4 u_0^2);
    # V_taste''(sigma) = -16 (4 u_0^2 - sigma^2)/(sigma^2 + 4 u_0^2)^2;
    # at sigma = 0: V_taste''(0) = -16 (4 u_0^2)/(4 u_0^2)^2 = -4/u_0^2.
    # So Pi(0) = -V_taste''(0) = +4/u_0^2.  Exact rational symbol check at a
    # rational u_0^2, plus the float value at the licensed scale.
    def v_taste_dd0(u2):  # second derivative at sigma=0, exact in u2
        return Fraction(-16) * (4 * u2) / (4 * u2) ** 2  # = -4/u2
    a1_exact = all(v_taste_dd0(u2) == Fraction(-4) / u2
                   for u2 in (Fraction(7, 9), Fraction(3, 4), Fraction(5, 6)))
    pi0 = 4.0 / U0_SQ
    a1_pi0 = abs(pi0 - 5.192616157) < 1e-6 and abs(-(-4.0 / U0_SQ) - pi0) < 1e-12
    check("A", "A1 Pi(0) = -V_taste''(0) = 4/u_0^2 EXACTLY: with V_taste = "
               "-8 log(sigma^2 + 4 u_0^2), V_taste''(0) = -4/u_0^2 (exact "
               "rational identity at 3 test u_0^2), so the symmetric-point "
               "fermion bubble Pi(0) = +4/u_0^2 = 5.1926162 at the licensed "
               "scale",
          a1_exact and a1_pi0, f"Pi(0) = {pi0:.7f}")

    # A2: 1/Pi(0) = u_0^2/4 = G_critical EXACTLY.
    inv_pi0 = 1.0 / pi0
    a2 = (abs(inv_pi0 - G_CRIT) < 1e-15
          and Fraction(1) / (Fraction(4) / Fraction(7, 9))
          == Fraction(7, 9) / 4)  # exact: 1/(4/u2) = u2/4
    check("A", "A2 1/Pi(0) = u_0^2/4 = G_critical EXACTLY (1/(4/u_0^2) = "
               "u_0^2/4 exact rational identity; float = NJL note's "
               "G_critical to < 1e-15)",
          a2, f"G_critical = u_0^2/4 = {G_CRIT:.7f}")

    # A3: r = G_eff/G_critical = 2/(3 u_0^2) at canonical G_eff = 1/(2 N_c).
    # G_eff/G_crit = (1/6)/(u_0^2/4) = 4/(6 u_0^2) = 2/(3 u_0^2).
    r = G_EFF_CANON / G_CRIT
    r_alt = 2.0 / (3.0 * U0_SQ)
    r_via_pi = G_EFF_CANON * (4.0 / U0_SQ)  # = G_eff * Pi(0)
    a3_form = (Fraction(1, 6) / (Fraction(7, 9) / 4)
               == Fraction(2) / (3 * Fraction(7, 9)))  # exact 2/(3 u2)
    a3 = (abs(r - r_alt) < 1e-15 and abs(r - r_via_pi) < 1e-15
          and abs(r - 0.865436) < 1e-6 and a3_form)
    check("A", "A3 r = G_eff/G_critical = G_eff*Pi(0) = 2/(3 u_0^2) at "
               "canonical G_eff = 1/(2 N_c) = 1/6 (exact rational form "
               "2/(3 u_0^2); = 0.8654360 to < 1e-6 against recon 0.865440)",
          a3, f"r = {r:.7f}")

    # A4: RPA enhancement 1/(1 - r) = 7.4314 (recon 7.4322; the small recon
    # round is in its 4-d.p. u_0; full B1 precision gives 7.4314).
    enh = 1.0 / (1.0 - r)
    a4 = abs(enh - 7.4314095) < 1e-5
    check("A", "A4 RPA / Hubbard-Stratonovich condensate susceptibility "
               "enhancement 1/(1 - r) = 7.4314 at canonical G_eff (chi = "
               "G_eff/(1 - G_eff Pi(0)); the resummed ladder on the declared "
               "NJL tree term); symmetric phase r < 1 confirmed",
          a4 and r < 1.0, f"1/(1-r) = {enh:.7f}, chi = {G_EFF_CANON*enh:.7f}")

    # A5: exact-closure book-keeping (DEFINITIONAL): closure needs
    # enhancement 32/3 = 10.6667 i.e. r = 1 - 3/32 = 0.90625.
    r_close = float(1 - S32)
    enh_close = float(Fraction(32, 3))
    a5 = (abs(r_close - 0.90625) < 1e-12 and abs(enh_close - 10.666667) < 1e-5
          and abs(float(S32) * enh_close - 1.0) < 1e-12)
    check("A", "A5 exact-closure book-keeping (DEFINITIONAL, the §3 guard): "
               "(3/32)*enhancement = 1 needs enhancement 32/3 = 10.6667, i.e. "
               "r = 1 - 3/32 = 0.90625 — recorded so the shortfall is read as "
               "a displacement, never a target 'discovered' here",
          a5, f"closure r = {r_close}, enhancement 32/3 = {enh_close:.5f}")
    return r, enh


# ---------------------------------------------------------------------------
# Section B — Z2: the graded product (RPA-normalized vertex).
# ---------------------------------------------------------------------------
def section_b(r, enh):
    print("\n--- Section B [A]: Z2 — graded product factor/alpha_s = "
          "(W/16)*[1/(1-r)] at canonical G_eff and the block01 phase "
          "endpoints ---")

    # The reading: replacing the dressed-kinetic denominator 16 u_0^2 with
    # the RPA-susceptibility normalization multiplies the taste-transfer
    # displacement (W/16, after the u_0^2 cancels alpha_s's u_0^(-2)) by the
    # enhancement 1/(1-r).  factor/alpha_s = (W/16) * enhancement.
    rows = []
    for tag, W in (("native (coherent, destructive)", W_NATIVE),
                   ("incoherent W=3/2", W_INCOH),
                   ("one-free-phase/bond W=9/4", W_ONE_FREE),
                   ("arbitrary coherent W=9", W_ARBITRARY)):
        frac = float(W) / 16.0 * enh
        rows.append((tag, W, frac))
        short = (f"{1.0 / frac:.3f}x short" if 0 < frac < 1
                 else (f"{frac:.3f}x (>= closure)" if frac > 0 else "0 (null)"))
        print(f"    W = {float(W):4.2f}  {tag:32s}: factor/alpha_s = "
              f"{frac:.4f}  ({short})")

    # B1: canonical-incoherent reproduces (3/32)*7.4314 = 0.6967 = 1.436x.
    incoh = float(W_INCOH) / 16.0 * enh
    b1 = (abs(incoh - 0.696695) < 1e-4
          and abs(float(S32) * enh - incoh) < 1e-12   # (3/32)*enh identity
          and abs(1.0 / incoh - 1.4353) < 1e-3)
    check("A", "B1 canonical-incoherent point reproduces the recon: "
               "factor/alpha_s = (W_incoh/16)*enhancement = (3/32)*7.4314 = "
               "0.6967 = 1.436x short (W_incoh/16 = 3/32 exact; the "
               "RPA-normalized vertex multiplies the taste-transfer "
               "displacement by 1/(1-r))",
          b1, f"factor/alpha_s = {incoh:.4f}, 1/factor = {1.0/incoh:.4f}")

    # B2: native coherent = 0 (the block01 destructive sum kills it exactly).
    native = float(W_NATIVE) / 16.0 * enh
    b2 = native == 0.0
    check("A", "B2 native-coherent endpoint = 0 EXACTLY: the anchored "
               "transfer row's native phase sum is exactly zero (3 channels "
               "+i/8, 3 channels -i/8) — coherence ALONE spans [0, 9] and is "
               "part of the SAME open Z as chi, not an independent dial",
          b2, "native factor/alpha_s = 0")

    # B3: the joint (r, W) crossing of 1.00.  At canonical r (enh fixed):
    #   W* = 16/enh hits factor = 1.  At incoherent W = 3/2: r* with
    #   enhancement = 32/3, i.e. r = 0.90625, hits factor = 1.
    W_star = 16.0 / enh
    one_free = float(W_ONE_FREE) / 16.0 * enh
    b3 = (abs(W_star - 2.1530) < 1e-3
          and W_INCOH < Fraction(W_star).limit_denominator(10000) < W_ONE_FREE
          and abs(one_free - 1.0450) < 1e-3        # one-free-phase OVERshoots
          and incoh < 1.0 < one_free)              # closure is BRACKETED
    check("A", "B3 the joint (r, phase-aggregation) crossing of 1.00: at "
               "canonical r, factor = 1 needs W* = 16/enhancement = 2.153 "
               "(BETWEEN incoherent 3/2 and one-free-phase 9/4); equivalently "
               "at incoherent W = 3/2, factor = 1 needs r = 0.90625 — so the "
               "phase dial BRACKETS closure (incoherent 0.697 under, "
               "one-free-phase 1.045 over)",
          b3, f"W* = {W_star:.4f}, one-free-phase = {one_free:.4f}x "
              f"(brackets closure)")

    # B4: OBSERVATION — one-free-phase lands inside [0.99, 1.01]? No: 1.045 is
    # in the numerology window [0.5, 2.0] but OUTSIDE the candidate window
    # [0.99, 1.01].  Record the in-window proximity with the guard.
    in_candidate = [r for r in rows if 0 < r[2] and 0.99 <= r[2] <= 1.01]
    in_numerology = [r for r in rows if 0 < r[2] and 0.5 <= r[2] <= 2.0]
    b4 = (not in_candidate                    # NO endpoint lands in [0.99,1.01]
          and len(in_numerology) == 2)        # incoherent + one-free-phase
    check("A", "B4 window logic (declared up front, block11 pattern): the "
               "CANDIDATE-MECHANISM window [0.99, 1.01] fires at NO declared "
               "phase endpoint; TWO endpoints (incoherent 0.697, "
               "one-free-phase 1.045) sit in the factor-2 numerology window "
               "[0.5, 2.0] — bracketing but not landing closure",
          b4, f"candidate-window hits = {len(in_candidate)}, "
              f"numerology-window hits = {len(in_numerology)}")

    observation("the phase endpoints incoherent (0.697x alpha_s) and "
                "one-free-phase-per-bond (1.045x alpha_s) sit in the "
                "factor-2 numerology window [0.5, 2.0]x alpha_s and BRACKET "
                "closure (1.00 crossing at W* = 2.153 or r = 0.90625).  "
                "Coherence spans [0, 9] entirely inside the SAME open Z as "
                "chi (it is which phases the channel projector licenses, not "
                "an independent dial); a window crossing achieved by sliding "
                "an unlanded phase weight against an unlanded r is a "
                "displacement bracket, never a discovered closure.")
    return rows, incoh, one_free


# ---------------------------------------------------------------------------
# Section C — Z3: the KILL-CRITERION test (load-bearing).  Exact local
# u_0-degree of the susceptibility-normalized per-threshold vertex.
# ---------------------------------------------------------------------------
def section_c():
    print("\n--- Section C [A]: Z3 — KILL-CRITERION test: exact local "
          "u_0-degree of the RPA-normalized per-threshold vertex ---")

    # The taste-transfer per-threshold vertex (OLD) was V_old(u_0) =
    # sigma_U^2 S/(16 u_0^2): a monomial in u_0 of degree -2 EXACTLY
    # (V_old u_0^2 = const, u_0-free).  That is the mechanism-required power.
    #
    # The RPA-normalized vertex replaces the constant-times-(16 u_0^2)^(-1)
    # by chi-normalization with G_eff a FIXED number.  Concretely the
    # enhancement multiplies in: V_norm(u_0) = V_old(u_0) * 1/(1 - G_eff
    # Pi(0)) with Pi(0) = 4/u_0^2.  Writing a = 4 G_eff (a pure number):
    #   1/(1 - G_eff*4/u_0^2) = u_0^2/(u_0^2 - a),
    #   V_norm(u_0) = [sigma_U^2 S/16] * (1/u_0^2) * u_0^2/(u_0^2 - a)
    #               = [sigma_U^2 S/16] / (u_0^2 - a).
    # This is NON-monomial: a simple pole at u_0^2 = a = 4 G_eff (= the
    # critical point u_0^2 = 4 G_eff, since G_crit = u_0^2/4 <=> u_0^2 = 4
    # G_crit, and r = G_eff/G_crit -> 1).  Its LOCAL u_0-degree is the exact
    # logarithmic derivative
    #   deg_u0(V_norm) = d ln V_norm / d ln u_0 = -2 u_0^2/(u_0^2 - a),
    # which is u_0-DEPENDENT and large near the critical point.

    a_const = Fraction(2, 3)   # 4 G_eff = 4*(1/6) = 2/3 (exact)

    # C1: closed-form exact local degree at the physical scale and at two
    # clean rational test points (block01/block09 two-point-ratio pattern,
    # done here as the exact derivative -2 u2/(u2 - a)).
    def deg_u0_norm(u2):  # exact for Fraction u2 != a; float otherwise
        return -2 * u2 / (u2 - a_const)
    # exact rational test points bracketing the physical scale 0.7703 from
    # ABOVE the critical point a = 0.6667 (the physical, symmetric-phase side)
    u2_lo, u2_hi = Fraction(7, 9), Fraction(4, 5)   # 0.7778, 0.8000 > a
    deg_lo = deg_u0_norm(u2_lo)
    deg_hi = deg_u0_norm(u2_hi)
    deg_phys = float(-2 * U0_SQ / (U0_SQ - float(a_const)))
    # the enhancement leg ALONE (the recon's ~ -13 estimate): deg of
    # u_0^2/(u_0^2 - a) = -2a/(u_0^2 - a) ... per leg; compute its float.
    deg_enh_phys = float(-2 * float(a_const) / (U0_SQ - float(a_const)))
    c1 = (deg_lo != Fraction(-2) and deg_hi != Fraction(-2)
          and deg_lo != deg_hi                       # genuinely u_0-dependent
          and abs(deg_phys + 14.8628) < 1e-3
          and abs(deg_enh_phys + 12.8628) < 1e-3)
    print(f"    exact local deg_u0(V_norm) = -2 u_0^2/(u_0^2 - 4 G_eff): "
          f"at u_0^2 = {float(u2_lo):.4f} -> {float(deg_lo):.4f}, "
          f"at u_0^2 = {float(u2_hi):.4f} -> {float(deg_hi):.4f}")
    print(f"    at the physical scale u_0^2 = {U0_SQ:.4f}: "
          f"deg(V_norm) = {deg_phys:.4f}; enhancement leg alone = "
          f"{deg_enh_phys:.4f} (the recon ~ -13)")
    check("A", "C1 EXACT local u_0-degree of the RPA-normalized vertex "
               "V_norm = c/(u_0^2 - 4 G_eff) (G_eff a fixed number) is "
               "-2 u_0^2/(u_0^2 - 4 G_eff): u_0-DEPENDENT, NOT a constant — "
               "= -14.86 at the physical scale, with the enhancement leg "
               "alone -12.86 (the recon ~ -13); it is NOT -2",
          c1, f"deg_phys = {deg_phys:.4f} != -2")

    # C2: it BREAKS the -2 criterion — strongly, and worse near criticality.
    # The pole at u_0^2 = 4 G_eff = G_crit-boundary is exactly the near-
    # critical RPA sensitivity: as r -> 1 the degree -> -infinity.
    near_crit_u2 = float(a_const) + 1e-3      # just above the critical point
    deg_near = -2 * near_crit_u2 / (near_crit_u2 - float(a_const))
    c2 = (deg_phys < -10.0 and deg_near < -1000.0)
    check("A", "C2 the criterion BREAKS: deg(V_norm) = -14.86 at the "
               "physical scale (far from -2) and diverges to -infinity as "
               "u_0^2 -> 4 G_eff (the near-critical r -> 1 sensitivity) — the "
               "strongly u_0-dependent RPA factor 1/(1 - G_eff*4/u_0^2) "
               "destroys the mechanism-required -2 power",
          c2, f"deg at u_0^2 = 4 G_eff + 1e-3 is {deg_near:.1f}")

    # C3: threshold-freezing RESTORES -2 EXACTLY — IF licensed.  If the
    # enhancement is frozen to a pure NUMBER E* at the decoupling-mass scale
    # (so it carries zero u_0-dependence), V_norm_frozen(u_0) = [sigma_U^2
    # S/16] * E* / u_0^2: a monomial of degree -2.  Two-rational-point exact
    # check (block01/block09 pattern): V_frozen u_0^2 = const, identical at
    # two rational u_0.
    E_star = Fraction(74314, 10000)           # a frozen pure-number stand-in
    s_pref = Fraction(3, 2) / 16              # sigma^2-saturated incoherent
    def v_frozen_times_u2(u2):
        return (s_pref * E_star / u2) * u2     # = s_pref*E_star, u_0-free
    c3 = (v_frozen_times_u2(Fraction(2, 3))
          == v_frozen_times_u2(Fraction(3, 5))
          == s_pref * E_star)
    check("A", "C3 threshold-freezing RESTORES degree -2 EXACTLY: IF the "
               "enhancement is frozen to a pure number E* at the decoupling-"
               "mass scale, V_frozen = (sigma_U^2 S/16) E*/u_0^2 is a "
               "monomial — V_frozen*u_0^2 = const, identical at u_0 in "
               "{2/3, 3/5} (the block01/block09 two-rational-point pattern) "
               "-> degree EXACTLY -2",
          c3, "V_frozen*u_0^2 u_0-free <=> degree -2")

    # C4: but threshold-freezing is UNSUPPLIED.  The NJL note's chi is a
    # SYMMETRIC-POINT object (Pi(0), sigma = 0); nothing in any landed object
    # evaluates G_eff/Pi at a decoupling-mass scale and freezes the
    # enhancement to a pure number there.  Scan the NJL note on disk for the
    # absence of any threshold-scale freezing of the susceptibility.
    njl = " ".join((NJL_NOTE.read_text() if NJL_NOTE.exists() else "").split())
    # the NJL note defines chi/G_critical only at the symmetric point and
    # explicitly fences G_eff as a leading-order O(1)-uncertain admission.
    c4 = ("G_critical" in njl
          and "symmetric" in njl.lower()
          and "leading-order" in njl.lower()
          and "threshold-freez" not in njl.lower()       # not supplied there
          and "decoupling-mass" not in njl.lower())
    check("A", "C4 threshold-freezing is UNSUPPLIED: the NJL note's chi is a "
               "SYMMETRIC-POINT object (Pi(0) at sigma = 0, G_critical = "
               "u_0^2/4) with G_eff a leading-order O(1)-uncertain admission; "
               "NO landed object evaluates G_eff/Pi at a decoupling-mass "
               "scale and freezes the enhancement to a pure number there — "
               "so degree -2 holds ONLY-IF threshold-frozen, an unsupplied "
               "assumption",
          c4, "NJL chi is symmetric-point; no threshold-freezing on disk")
    return deg_phys, deg_enh_phys


# ---------------------------------------------------------------------------
# Section D — Z4: the G_eff band sweep (NJL note §6.2 forms + u_0-dressed).
# ---------------------------------------------------------------------------
def section_d():
    print("\n--- Section D [A]: Z4 — G_eff band sweep (NJL §6.2 forms): r, "
          "enhancement, (3/32)*enhancement, phase ---")
    g2 = 2.0 * N_C / 6.0  # = 1 at beta = 6 (block02-licensed)
    forms = [
        ("1/(2 N_c) Kawamoto-Smit LO", 1.0 / (2 * N_C), "SYM"),
        ("1/(g^2 N_c) strong-coupling alt", 1.0 / (g2 * N_C), "BROKEN"),
        ("1/(g^2 (N_c^2-1)) Casimir", 1.0 / (g2 * (N_C ** 2 - 1)), "SYM"),
        ("(N_c^2-1)/(2 N_c^2 g^2) color-trace",
         (N_C ** 2 - 1) / (2.0 * N_C ** 2 * g2), "BROKEN"),
        ("u_0^2/(2 N_c) u0^2-dressed", U0_SQ / (2 * N_C), "SYM"),
        ("u_0^4/(2 N_c) u0^4-dressed", U0_SQ ** 2 / (2 * N_C), "SYM"),
    ]
    rows = []
    near_closure = []
    in_window = []
    broken = []
    s32 = float(S32)
    for name, g_eff, expect_phase in forms:
        r = g_eff / G_CRIT
        if r < 1.0:
            enh = 1.0 / (1.0 - r)
            val = s32 * enh
            phase = "SYM"
        else:
            enh = float("inf")
            val = float("inf")
            phase = "BROKEN"
            broken.append(name)
        rows.append((name, g_eff, r, enh, val, phase, expect_phase))
        if phase == "SYM" and abs(r - 0.90625) < 0.02:
            near_closure.append(name)
        if phase == "SYM" and 0.5 <= val <= 2.0:
            in_window.append((name, val))
        e_str = f"{enh:8.4f}" if math.isfinite(enh) else "     inf"
        v_str = f"{val:7.4f}" if math.isfinite(val) else "    inf"
        print(f"    {name:38s}: G_eff = {g_eff:7.5f}, r = {r:7.5f}, "
              f"1/(1-r) = {e_str}, (3/32)*enh = {v_str}, {phase}")

    # D1: phase classification matches the NJL note exactly (4 SYM, 2 BROKEN);
    # the broken forms have r >= 1 so chi diverges (unphysical for this
    # reading).
    phase_ok = all(rw[5] == rw[6] for rw in rows)
    n_sym = sum(1 for rw in rows if rw[5] == "SYM")
    d1 = (phase_ok and n_sym == 4 and len(broken) == 2
          and all(rows[i][2] >= 1.0 for i, rw in enumerate(rows)
                  if rw[5] == "BROKEN"))
    check("A", "D1 G_eff band sweep matches the NJL note §6.2 phase column "
               "exactly: 4 of 6 forms SYMMETRIC (r < 1, chi finite), 2 "
               "BROKEN-phase (r >= 1, chi diverges — unphysical for this "
               "RPA-normalization reading)",
          d1, f"SYM = {n_sym}, BROKEN = {len(broken)} {broken}")

    # D2: NONE of the SYM forms lands near closure (r ~ 0.906); the canonical
    # form (r = 0.865) is the CLOSEST and is still 1.436x short.
    d2 = (not near_closure
          and abs(rows[0][2] - 0.865436) < 1e-5
          and rows[0][4] < 1.0)
    check("A", "D2 NO symmetric-phase G_eff form lands near closure (r ~ "
               "0.906): the canonical Kawamoto-Smit form r = 0.8654 is the "
               "CLOSEST and gives (3/32)*enh = 0.697 (1.436x short); the "
               "Casimir/u_0-dressed forms sit further from closure (r = "
               "0.51-0.67)",
          d2, f"closest = canonical r = {rows[0][2]:.4f}, "
              f"near-closure forms = {near_closure}")

    # D3: which sit in the numerology window [0.5, 2.0]x alpha_s.
    d3 = (len(in_window) >= 1
          and all(0.5 <= v <= 2.0 for _, v in in_window)
          and ("1/(2 N_c) Kawamoto-Smit LO", rows[0][4]) in in_window)
    check("A", "D3 numerology-window [0.5, 2.0]x alpha_s membership: the "
               "canonical form (0.697) sits in-window; the smaller-G_eff "
               "forms (Casimir 0.267, u_0^2-dressed 0.281, u_0^4-dressed "
               "0.193) fall BELOW it — none reaches the candidate window",
          d3, f"in-window (3/32)*enh forms = {len(in_window)}")

    for name, val in in_window:
        observation(f"G_eff form '{name}' gives (3/32)*enhancement = "
                    f"{val:.4f}x alpha_s, inside the factor-2 numerology "
                    f"window [0.5, 2.0] — a near-critical RPA enhancement of "
                    f"a SMALL incoherent weight, with G_eff a DECLARED-model "
                    f"O(1)-uncertain admission (NJL §6.2); no supplier, no "
                    f"claim.")
    return rows


# ---------------------------------------------------------------------------
# Section E — supplier/constraint scans on disk + the declared-open residuals.
# ---------------------------------------------------------------------------
def section_e():
    print("\n--- Section E [B]: one-hop authorities, declared-model fences, "
          "and S1 kill criterion on disk ---")

    # E1: taste-transfer probe note — the ceiling this probe attacks.
    taste = " ".join((TASTE_NOTE.read_text()
                      if TASTE_NOTE.exists() else "").split())
    e1 = ("sigma_U^2 S/16" in taste
          and "3/32" in taste
          and "u_0-degree" in taste.replace("`", "")
          and "channel-projected condensate normalization" in taste)
    check("B", "E1 taste-transfer probe note on disk: the structural ceiling "
               "factor/alpha_s = sigma_U^2 S/16 <= 3/32, the EXACTLY-(-2) "
               "u_0-degree, and the OPEN 'channel-projected condensate "
               "normalization' (the §6 theorem this probe grades)",
          e1)

    # E2: NJL note — the landed Pi(0), G_critical, G_eff, and the §6.2 band.
    njl = " ".join((NJL_NOTE.read_text() if NJL_NOTE.exists() else "").split())
    e2 = ("G_critical" in njl
          and "u_0² / 4" in njl or "u_0^2/4" in njl.replace(" ", "")
          ) and ("1/(2 N_c)" in njl and "Hubbard" in njl
                 and "Kawamoto" in njl and "Fierz" in njl
                 and "symmetric" in njl.lower())
    check("B", "E2 NJL note on disk: the landed Pi-chain (G_critical = "
               "u_0^2/4, G_eff = 1/(2 N_c), symmetric phase) AND the named "
               "DECLARED-model admissions — Hubbard-Stratonovich, "
               "scalar-channel-after-Fierz, Kawamoto-Smit G_eff (the fences "
               "this probe carries)",
          e2)

    # E3: kernel-share note — the 1/(4 pi) kernel leg and u_0^(-2) dressing.
    kern = " ".join((KERNEL_NOTE.read_text()
                     if KERNEL_NOTE.exists() else "").split())
    e3 = ("per-taste IR kernel slope" in kern
          and "1/(4 pi)" in kern
          and "u_0^(-2)" in kern.replace(" ", "")
          or "u_0^(-2) two-link dressing" in kern)
    check("B", "E3 kernel-share note on disk: the per-taste d = 3 IR kernel "
               "slope 1/(4 pi) and the u_0^(-2) two-link dressing (the kernel "
               "leg and the dressing power the taste-transfer vertex "
               "consumes; unchanged here)",
          e3)

    # E4: route-inventory synthesis — the S1 kill criterion this candidate is
    # tested against (an exact one-link/strong-coupling computation whose
    # per-decoupling factor is O(1)-displaced under every declared variant
    # eliminates S1).
    route = " ".join((ROUTE_NOTE.read_text()
                      if ROUTE_NOTE.exists() else "").split())
    e4 = ("S1 — strong-coupling one-link Haar" in route
          or "S1 — strong-coupling one-link Haar" in route) and (
          "Kill criterion:" in route
          and "O(1)-displaced from `alpha_s`" in route
          and "symmetric phase" in route.lower())
    check("B", "E4 route-inventory S1 kill criterion on disk: 'an exact "
               "one-link computation whose per-decoupling factor is "
               "O(1)-displaced from alpha_s under every declared variant "
               "eliminates S1' — the criterion this RPA-normalization "
               "candidate (an S1-lineage strong-coupling object) is tested "
               "against",
          e4)

    # E5: parent-note honesty fences (forbidden closure tokens absent).
    note = " ".join((PARENT_NOTE.read_text()
                     if PARENT_NOTE.exists() else "").lower().split())
    required = [
        "does not close the delta0 gate",
        "declared-model",
        "conditional-kill",
        "partial in magnitude",
        "fires the",
        "threshold-freez",
        "r = 0.906",
        "hubbard",
    ]
    forbidden = [
        "closes the delta0 gate",
        "closure is achieved",
        "chi is a licensed",
        "derives the attachment",
    ]
    req_missing = [t for t in required if t not in note]
    forb_hit = [t for t in forbidden if t in note]
    e5 = (PARENT_NOTE.exists() and not req_missing and not forb_hit)
    check("B", "E5 parent-note honesty fences on disk: records the "
               "CONDITIONAL-KILL grade (partial in magnitude only; the "
               "as-computed vertex fires the degree kill criterion), fences "
               "chi as a 'declared-model' object (Hubbard-Stratonovich), "
               "names the unlanded 'r = 0.906' and the 'threshold-freezing' "
               "degree caveat, and states it 'does not close the DELTA0 "
               "gate'; forbidden closure tokens absent",
          e5, f"missing = {req_missing}, forbidden hit = {forb_hit}")

    # Declared-open residuals.
    print()
    residual("the channel-projected condensate normalization Z is graded "
             "PARTIAL, not closed: the LANDED NJL-RPA susceptibility chi = "
             "G_eff/(1 - G_eff Pi(0)) supplies a near-critical enhancement "
             "1/(1-r) = 7.4314 at canonical G_eff that BRACKETS closure under "
             "the block01 phase dial (incoherent 0.697x alpha_s under, "
             "one-free-phase 1.045x over; 1.00 crossing at W = 2.153 or r = "
             "0.90625), but chi is a DECLARED-MODEL object (Hubbard-"
             "Stratonovich + scalar-channel-after-Fierz + Kawamoto-Smit "
             "G_eff, all NJL-note named admissions), NOT a derived "
             "normalization — closure requires a DERIVED Z landing in "
             "[0.99, 1.01]x alpha_s, which this is not.")
    residual("the degree-(-2) criterion (the §6 kill criterion) holds "
             "ONLY-IF the enhancement is threshold-FROZEN: with G_eff a "
             "fixed number the RPA-normalized vertex V_norm = c/(u_0^2 - 4 "
             "G_eff) has exact local u_0-degree -2 u_0^2/(u_0^2 - 4 G_eff) = "
             "-14.86 at the physical scale (enhancement leg -12.86, the recon "
             "~ -13), diverging as r -> 1 — it BREAKS -2; freezing the "
             "enhancement to a pure number at the decoupling-mass scale "
             "restores degree EXACTLY -2, but NO landed object licenses that "
             "freezing (chi is a symmetric-point object) — an UNSUPPLIED "
             "assumption.")
    residual("the exact closure r = 0.90625 is UNLANDED: the canonical "
             "Kawamoto-Smit G_eff = 1/(2 N_c) gives r = 0.8654 (the closest "
             "of the six NJL §6.2 forms, still 1.436x short at incoherent W); "
             "no landed object supplies a G_eff (or a phase aggregation W) "
             "that puts r at 0.906 / factor at 1.00 — the DELTA0 magnitude "
             "gate and the B4 attachment-observable identification remain "
             "OPEN; this probe grades a candidate Z and sharpens the surface, "
             "it does not close.")


# ---------------------------------------------------------------------------
# Terminal class-D fence (external comparators).
# ---------------------------------------------------------------------------
def section_fence():
    print("\n--- Terminal class-D fence: external comparators ---")
    print("  (No PDG quantity is needed or consumed by this probe; the "
          "susceptibility")
    print("   chain, the phase dial, and the degree test are internal "
          "structure only.)")
    src = Path(__file__).read_text()
    pdg_literal = "246." + "22"  # composed so the scan finds only real uses
    higgs_literal = "125." + "10"
    check("D", "H1 self-scan: the PDG electroweak-VEV and Higgs-pole-mass "
               "literals appear ZERO times in this runner's source (scanned "
               "as composed strings) — no comparator consumed anywhere",
          src.count(pdg_literal) == 0 and src.count(higgs_literal) == 0)


def main() -> int:
    print("=" * 78)
    print(" frontier_hierarchy_delta0_b4_njl_rpa_normalization_probe_"
          "2026_06_13.py")
    print(" Derive-Z: grade the LANDED NJL-RPA condensate susceptibility as "
          "the")
    print(" channel-projected normalization Z for the taste-transfer B4 "
          "attachment.")
    print(" chi = G_eff/(1 - G_eff Pi(0)), Pi(0) = 4/u_0^2, G_critical = "
          "u_0^2/4.")
    print(" Does the RPA enhancement 1/(1-r) absorb the >= 10.7x "
          "taste-transfer shortfall,")
    print(" and does the normalized vertex keep u_0-degree -2?")
    print(" Parent note: docs/HIERARCHY_DELTA0_B4_NJL_RPA_NORMALIZATION_"
          "PROBE_NOTE_2026-06-13.md")
    print("=" * 78)

    r, enh = section_a()
    rows_b, incoh, one_free = section_b(r, enh)
    deg_phys, deg_enh = section_c()
    section_d()
    section_e()
    section_fence()

    print()
    print("=" * 78)
    print(f" Breakdown: A={CLASS_COUNTS['A']} B={CLASS_COUNTS['B']} "
          f"C={CLASS_COUNTS['C']} D={CLASS_COUNTS['D']} "
          f"RESIDUAL={RESIDUAL_COUNT} OBSERVATION={OBSERVATION_COUNT}")
    print(f" TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(" VERDICT: channel-projected normalization Z graded "
          "CONDITIONAL-KILL.  Established")
    print("   (bounded, exact): the LANDED NJL-RPA susceptibility chain — "
          "Pi(0) = ")
    print("   4/u_0^2 = -V_taste''(0), G_critical = u_0^2/4, r = 2/(3 u_0^2) "
          "= 0.8654")
    print("   at canonical G_eff, enhancement 1/(1-r) = 7.4314 — and the "
          "graded product")
    print("   factor/alpha_s = (W/16)*enhancement: canonical-incoherent "
          "0.697 (1.436x")
    print("   short), one-free-phase 1.045 (over) — the RPA enhancement "
          "BRACKETS closure")
    print("   in MAGNITUDE under the block01 phase dial, hitting 1.00 at "
          "W = 2.153 or r = 0.90625.")
    print("   BUT the as-computed RPA-normalized vertex has exact local "
          f"u_0-degree {deg_phys:.1f}")
    print("   (not -2), which FIRES the mechanism's own stated kill "
          "criterion (degree != -2);")
    print("   it is rescued to a closure-bracketing partial-in-magnitude "
          "result ONLY by an")
    print("   UNSUPPLIED threshold-freezing of the enhancement (chi is a "
          "symmetric-point")
    print("   object; NO landed object licenses the freezing).  By the "
          "grading rule the")
    print("   binding verdict is CONDITIONAL-KILL.  chi is also a "
          "Hubbard-Stratonovich +")
    print("   Fierz-scalar + Kawamoto-Smit DECLARED-MODEL object, NOT a "
          "derived Z, and the")
    print("   exact closure r = 0.906 is UNLANDED.  NOT claimed: closure, or "
          "any")
    print("   licensed-surface reproduction.  DELTA0 stays open; the NJL-RPA "
          "object is the")
    print("   first normalization that brackets closure in magnitude, but it "
          "fires the degree kill.")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
