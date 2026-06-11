#!/usr/bin/env python3
"""DELTA0 block11: the B4-attachment OBSERVABLE-IDENTIFICATION ENUMERATION
— executing block10b's R2 kill criterion over the declared candidate
readouts K1-K8

    docs/HIERARCHY_DELTA0_B4_ATTACHMENT_OBSERVABLE_ENUMERATION_
    NOTE_2026-06-11.md

Block11 of the DELTA0 attachment campaign.  Block10b
(docs/HIERARCHY_DELTA0_S1PRIME_TASTE_REGION_KERNEL_SHARE_PROBE_
NOTE_2026-06-11.md) left the open theorem in its sharpest form (its
residual R2): identify the ratio-normalized readout observable in which
ONE decoupling taste contributes multiplicatively exactly

    [per-taste IR kernel slope 1/(4 pi)] x [dressed two-link vertex
    u_0^(-2)]  =  alpha_s  =  0.1033038,

and stated its kill criterion: a deterministic enumeration of the
declared candidate readouts on this surface finding EVERY candidate's
per-decoupling factor O(1)-displaced from alpha_s under every declared
variant eliminates the identification for that class (the
E3/block08/block09 pattern).  THIS RUNNER IS THAT ENUMERATION.

Candidate readout families (every normalization DECLARED; exact closed
forms where exact, declared-grid tolerance where computed):

  K1  ratio-normalized determinant-share family from block01's exact
      per-mode factor f(m) = sqrt(m^2 + 4 u_0^2): all f(m)/f_ref over
      m in {0, u_0, 2 u_0, u_0^2}, refs in {f(0), 1, 2, 2 u_0}, plus
      the dressed/undressed rows f(m; u_0)/f(m; 1).
  K2  IR-slope dressing grid: the block10b per-taste IR kernel
      coefficient m/(4 pi), m in {1, 2 u_0, u_0, u_0^2}, DIVIDED by
      normalizations N in {1, 1/8, 1/16, 2 u_0, f(m)}, each with and
      without the dressed two-link u_0^(-2) — 40 cells, all exact
      closed forms alpha_s x (algebraic factor in u_0 and rationals).
  K3  free-energy-density per mode on the landed Matsubara surface
      (docs/HIERARCHY_MATSUBARA_FREE_ENERGY_DENSITY_NARROW_THEOREM_
      NOTE_2026-05-16.md): at L_t = 2 the landed closed form equals
      block01's determinant EXACTLY, the per-entry density readout is
      exp(-Delta f) = 2 u_0 / f(m) exactly, and the direct
      n_matrix = 16 -> 15 reading is NOT constructible on the surface
      (n_matrix = 8 L_t, multiples of 8) — recorded honestly.
  K4  static-potential screening share at threshold separation:
      block08's landed R_S2 values imported (1.0123-1.0213, displaced
      9.80x-9.89x); the threshold separation r = 1/(2 u_0) = 0.5697 is
      SUB-LATTICE — scale-mismatch recorded, landed radii r = 4, 6, 8
      are the declared answer.
  K5  plaquette-action cost readouts exp(-Delta_S_candidate) for the
      block10a scan-table rows (imported + verified; G(0) recomputed
      deterministically here).
  K6  (this block's design) equal-share mode-sum ratio readouts from
      block10b's exact rational shares: 15/16, 1/8, 1/16, exp(-1/8),
      exp(-1/16).
  K7  (this block's design) threshold Yukawa-screening exponentials at
      r = 1 (the honest on-lattice reading of the sub-lattice
      threshold scale): exp(-2 u_0), exp(-u_0), exp(-1/(2 u_0)).
  K8  (this block's design) per-taste BZ log-det share readouts of the
      block10b mode sums: exp(-(1/8) V(m)) and the ratio-normalized
      dressed/undressed variant, V(m; u) = int d^3k/(2 pi)^3
      ln(1 + m^2/(u^2 s^2)), computed on declared half-shifted grids
      L = 32, 48.

WINDOW LOGIC (declared up front, the E3/block08 pattern):
  CANDIDATE MATCH window: factor/alpha_s in [0.99, 1.01] AND a
      derivable mechanism (the number alone is NOT enough);
  factor-2 observation window: factor/alpha_s in [0.5, 2.0] —
      numerology-risk flagged, never a residual, never a claim.

RESULT (computed below): the ONLY entries inside the match window are
the two K2 grid cells that are the supplier-chain identity
alpha_s = (1/(4 pi)) u_0^(-2) ITSELF written in grid coordinates
((m = 1, N = 1, dressed) and (m = 2 u_0, N = 2 u_0, dressed), where
the normalization cancels m) — DEFINITIONAL, by construction, zero
mechanism content (the mechanism IS the open identification).  NO
candidate readout lands in the window with a mechanism.  The block10b
kill criterion FIRES for the enumerated class: the attachment
observable, if it exists, is NOT among the K1-K8 declared readouts
under the declared normalizations.  The identification theorem gains
the constraint set 'not K1-K8'.  The DELTA0 gate stays open.

Vocabulary discipline: nothing here is 'derived' past its declared
premises (B1 plaquette license; I2 alpha convention on the I3
g_bare = 1 surface, cited through block02; block01/block08/block10a/
block10b values imported with on-disk literal verification); all
unsupplied content is declared as RESIDUAL lines; all factor-2 window
entries are OBSERVATION lines (numerology-risk flagged).

Deterministic, pure Python stdlib (math, fractions), no network, no
randomness; the largest computations are the L = 48 BZ log-det sums
(110k terms) and the L = 40 Watson sum — total runtime a few seconds,
well under 90 s.  Exit code 0 iff TOTAL: PASS=n FAIL=0.
"""
from __future__ import annotations

import math
import sys
from fractions import Fraction
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"
PARENT_NOTE = (DOCS / "HIERARCHY_DELTA0_B4_ATTACHMENT_OBSERVABLE_"
                      "ENUMERATION_NOTE_2026-06-11.md")

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
    print(f"  OBSERVATION (bounded, numerology-risk flagged — NOT a "
          f"residual, NOT a claim): {msg}")


# ---------------------------------------------------------------------------
# Declared boundary inputs (cited, not asserted; see the parent note).
#   <P> = 0.5934 consumed ONLY under the B1 reuse license of
#   docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md; alpha_bare = 1/(4 pi) enters
#   via the I2 convention row + I3 g_bare = 1 surface (cited through
#   block02); block08's R_S2 values and c0, and block10a's scan rows, are
#   imported with their literals verified on disk.
# ---------------------------------------------------------------------------
P_BOUNDARY = 0.5934                   # B1 licensed reuse number (4 d.p.)
U_0 = P_BOUNDARY ** 0.25              # = 0.877681381
ALPHA_BARE = 1.0 / (4.0 * math.pi)    # = 0.0795775 (I2 at I3 g_bare = 1)
ALPHA_LM = ALPHA_BARE / U_0           # = 0.0906678 (repo canonical literal)
ALPHA_S = ALPHA_BARE / U_0 ** 2       # = 0.1033038 (the block02 target)
DELTA_S = math.log(1.0 / ALPHA_S)     # = 2.270081 (block10a)
C0_BLOCK08 = 0.0266477                # block08 one-loop bubble constant
G0_WATSON_REF = 0.2527310098          # parallel-reference Watson value
N_C = 3

MATCH_LO, MATCH_HI = 0.99, 1.01       # CANDIDATE MATCH window (x alpha_s)
F2_LO, F2_HI = 0.5, 2.0               # factor-2 observation window
EPS = 1e-9                            # boundary tolerance for the windows

# The global candidate table: (id, definition, value, exact_note).
ROWS: list[tuple[str, str, float, str]] = []
# ids of DEFINITIONAL identity cells (exact chain members by construction).
DEFINITIONAL: set[str] = set()


def f_mode(m: float, u: float = U_0) -> float:
    """block01's exact per-mode determinant factor magnitude
    sqrt(m^2 + 4 u^2)."""
    return math.sqrt(m * m + 4.0 * u * u)


def add_row(rid: str, definition: str, value: float,
            exact_note: str = "") -> None:
    ROWS.append((rid, definition, value, exact_note))
    d_s = value / ALPHA_S
    d_lm = value / ALPHA_LM
    d_b = value / ALPHA_BARE
    if rid in DEFINITIONAL:
        flag = "EXACT-IDENTITY (by construction)"
    elif MATCH_LO - EPS <= d_s <= MATCH_HI + EPS:
        flag = "MATCH WINDOW"
    elif F2_LO - EPS <= d_s <= F2_HI + EPS:
        flag = "factor-2 obs"
    else:
        flag = "-"
    note = f"  [{exact_note}]" if exact_note else ""
    print(f"    {rid:34s} {value:12.7f}  /a_s={d_s:9.4f}  "
          f"/a_LM={d_lm:9.4f}  /a_bare={d_b:9.4f}  {flag}{note}")


def window_class(value: float) -> str:
    d_s = value / ALPHA_S
    if MATCH_LO - EPS <= d_s <= MATCH_HI + EPS:
        return "match"
    if F2_LO - EPS <= d_s <= F2_HI + EPS:
        return "factor2"
    return "out"


# ---------------------------------------------------------------------------
# Section A — declared inputs, exact skeleton, window declaration.
# ---------------------------------------------------------------------------
def section_a():
    print("\n--- Section A [C]/[A]/[B]: declared inputs, exact identity "
          "skeleton, window logic ---")

    # A1 [C]: exact Fraction skeleton of the K2 identity cells.  With
    # stand-ins q (for 4 pi) and u (for u_0): alpha_s = 1/(q u^2); the
    # grid cell (m/(q N)) x u^(-2) equals alpha_s EXACTLY at
    # (m = 1, N = 1) and at (m = 2u, N = 2u) (the normalization cancels
    # m), and equals alpha_s/2 exactly at (m = u, N = 2u) (block01's N).
    skel_ok = True
    for q in (Fraction(22, 7), Fraction(355, 113)):
        for u in (Fraction(2, 3), Fraction(7, 8)):
            a_s = 1 / (q * u ** 2)
            cell = lambda m, n: (m / (q * n)) / u ** 2  # noqa: E731
            skel_ok = skel_ok and cell(Fraction(1), Fraction(1)) == a_s
            skel_ok = skel_ok and cell(2 * u, 2 * u) == a_s
            skel_ok = skel_ok and cell(u, 2 * u) == a_s / 2
            skel_ok = skel_ok and (m_undr := (1 / (q * 1))) == a_s * u ** 2
    check("C", "A1 exact identity skeleton (Fraction stand-ins q for "
               "4 pi, u for u_0; 4 rational test points): the K2 grid "
               "cells (m=1, N=1, dressed) and (m=2u, N=2u, dressed) "
               "equal alpha_s = 1/(q u^2) EXACTLY (the normalization "
               "cancels m), and (m=u, N=2u, dressed) equals alpha_s/2 "
               "exactly (block01's N) — these cells are the supplier "
               "chain BY CONSTRUCTION, not discoveries", skel_ok,
          "exact Fraction arithmetic")

    # A2 [A]: the float chain and the cross-reference targets.
    check("A", "A2 supplier-chain values (B1 + I2 + I3, cited through "
               "block02): alpha_s = alpha_bare/u_0^2 = 0.1033038, "
               "alpha_LM = alpha_bare/u_0 = 0.0906678 (repo canonical), "
               "alpha_bare = 1/(4 pi) = 0.0795775; geometric-progression "
               "identity alpha_LM^2 = alpha_bare x alpha_s < 1e-14; "
               "exp(-Delta_S) = alpha_s < 1e-12 (block10a consistency)",
          abs(ALPHA_S - 0.1033038) < 5e-8
          and abs(ALPHA_LM - 0.0906678) < 5e-8
          and abs(ALPHA_BARE - 0.0795775) < 5e-8
          and abs(ALPHA_LM ** 2 - ALPHA_BARE * ALPHA_S) < 1e-14
          and abs(math.exp(-DELTA_S) - ALPHA_S) < 1e-12,
          f"alpha_s = {ALPHA_S:.7f}, alpha_LM = {ALPHA_LM:.7f}")

    # A3 [A]: the cross-reference displacements are exact u_0 powers.
    check("A", "A3 cross-reference honesty: the three comparison "
               "columns are one exact geometric progression — "
               "alpha_bare/alpha_s = u_0^2 = 0.770325 and "
               "alpha_LM/alpha_s = u_0 = 0.877681 EXACTLY (< 1e-14), "
               "so 'vs alpha_LM' and 'vs alpha_bare' displacements are "
               "u_0-power rescalings of 'vs alpha_s', never independent "
               "evidence",
          abs(ALPHA_BARE / ALPHA_S - U_0 ** 2) < 1e-14
          and abs(ALPHA_LM / ALPHA_S - U_0) < 1e-14,
          f"u_0 = {U_0:.6f}, u_0^2 = {U_0 ** 2:.6f}")

    # A4 [B]: suppliers and the kill criterion on disk.
    b10b = (DOCS / "HIERARCHY_DELTA0_S1PRIME_TASTE_REGION_KERNEL_SHARE_"
                   "PROBE_NOTE_2026-06-11.md")
    b02 = (DOCS / "HIERARCHY_DELTA0_RATIO_NORMALIZED_ALPHA_S_PER_"
                  "DECOUPLING_REDUCTION_NOTE_2026-06-11.md")
    b01 = (DOCS / "HIERARCHY_DELTA0_BLOCKING_SINGLE_MODE_DECIMATION_"
                  "PROBE_NOTE_2026-06-11.md")
    plaq = DOCS / "PLAQUETTE_SELF_CONSISTENCY_NOTE.md"
    t10b = b10b.read_text() if b10b.exists() else ""
    t02 = b02.read_text() if b02.exists() else ""
    t01 = b01.read_text() if b01.exists() else ""
    tpl = plaq.read_text() if plaq.exists() else ""
    check("B", "A4 suppliers + kill criterion on disk: block10b states "
               "the kill criterion this runner executes ('enumerates "
               "the declared candidate readouts', 'O(1)-displaced'); "
               "block02 states the target 0.1033038; block01 states the "
               "per-mode factor ('2 u_0'); the B1 plaquette license "
               "('admitted comparison/reuse number', 0.5934) is on disk",
          "enumerates" in t10b and "O(1)-displaced" in t10b
          and "Kill criterion (runner R2)" in t10b
          and "0.1033038" in t02
          and "2 u_0" in t01
          and "admitted comparison/reuse number" in tpl
          and "0.5934" in tpl)

    print(f"\n  DECLARED WINDOW LOGIC: CANDIDATE MATCH iff factor/alpha_s "
          f"in [{MATCH_LO}, {MATCH_HI}] AND a derivable mechanism (the "
          f"number alone is insufficient);")
    print(f"  factor-2 observation window [{F2_LO}, {F2_HI}] x alpha_s "
          f"(numerology-risk flagged, never a residual).")
    print("  Table columns: value, displacement vs alpha_s = "
          f"{ALPHA_S:.7f}, vs alpha_LM = {ALPHA_LM:.7f}, vs alpha_bare "
          f"= {ALPHA_BARE:.7f}.")


# ---------------------------------------------------------------------------
# Section B — K1: ratio-normalized determinant-share family.
# ---------------------------------------------------------------------------
def section_b():
    print("\n--- Section B [A]: K1 — block01 per-mode determinant-factor "
          "family f(m) = sqrt(m^2 + 4 u_0^2), all declared ratios ---")

    # B1 [A]: the exact closed forms of the family members.
    closed = (
        abs(f_mode(0.0) - 2.0 * U_0) < 1e-14
        and abs(f_mode(U_0) - U_0 * math.sqrt(5.0)) < 1e-14
        and abs(f_mode(2.0 * U_0) - 2.0 * math.sqrt(2.0) * U_0) < 1e-14
        and abs(f_mode(U_0 ** 2)
                - U_0 * math.sqrt(U_0 ** 2 + 4.0)) < 1e-14)
    check("A", "B1 exact closed forms: f(0) = 2 u_0 = 1.755363 "
               "(block01's per-mode factor at m = 0), f(u_0) = "
               "sqrt(5) u_0, f(2 u_0) = 2 sqrt(2) u_0 (threshold = mode "
               "gap), f(u_0^2) = u_0 sqrt(u_0^2 + 4) — all < 1e-14",
          closed, f"f(0) = {f_mode(0.0):.6f}, f(2u_0) = "
                  f"{f_mode(2.0 * U_0):.6f}")

    # B2 [A]: the full ratio table (16 declared ratios).
    masses = [("0", 0.0), ("u_0", U_0), ("2u_0", 2.0 * U_0),
              ("u_0^2", U_0 ** 2)]
    refs = [("f(0)", f_mode(0.0)), ("1", 1.0), ("2", 2.0),
            ("2u_0", 2.0 * U_0)]
    print("    (refs declared: f(0) and 2 u_0 coincide exactly — both "
          "kept as declared)")
    vals = []
    for mn, m in masses:
        for rn, rv in refs:
            v = f_mode(m) / rv
            vals.append(v)
            add_row(f"K1 f({mn})/{rn}",
                    f"per-mode determinant factor at m = {mn}, "
                    f"normalized by {rn}", v)
    min_disp = min(v / ALPHA_S for v in vals)
    check("A", "B2 K1 ratio table (16 declared ratios printed): every "
               "member is O(1) — minimum displacement is f(0)/2 = u_0 "
               "at 8.4961x alpha_s; NO member inside the factor-2 "
               "window, none anywhere near the match window",
          len(vals) == 16 and min_disp > F2_HI
          and abs(min_disp - U_0 / ALPHA_S) < 1e-12,
          f"min displacement = {min_disp:.4f}x")

    # B3 [A]: dressed/undressed (u_0 vs 1) ratio-normalized rows.
    rn_vals = []
    for mn, m in masses:
        v = f_mode(m, U_0) / f_mode(m, 1.0)
        rn_vals.append(v)
        add_row(f"K1 f({mn};u_0)/f({mn};1)",
                f"dressed/undressed per-mode factor at m = {mn} "
                f"(block02's ratio normalization)", v,
                "= u_0 exactly at m = 0" if m == 0.0 else "")
    check("A", "B3 dressed/undressed rows (block02's ratio "
               "normalization): f(0; u_0)/f(0; 1) = u_0 = 0.877681 "
               "EXACTLY (block02 T1 reproduced); all four rows in "
               "[0.8777, 0.9329] — displacements 8.50x-9.03x",
          abs(rn_vals[0] - U_0) < 1e-14
          and all(8.4 < v / ALPHA_S < 9.1 for v in rn_vals),
          f"values = {[round(v, 6) for v in rn_vals]}")

    # B4 [A]: K1 verdict.
    all_k1 = vals + rn_vals
    check("A", "B4 K1 VERDICT: eliminated — all 20 family members are "
               "O(1)-displaced (8.50x-24.03x above alpha_s); the "
               "determinant-share family cannot carry a per-decoupling "
               "0.1033 under any declared normalization",
          all(window_class(v) == "out" for v in all_k1)
          and max(v / ALPHA_S for v in all_k1) < 25.0,
          f"range = [{min(all_k1) / ALPHA_S:.2f}, "
          f"{max(all_k1) / ALPHA_S:.2f}]x")


# ---------------------------------------------------------------------------
# Section C — K2: the IR-slope dressing grid.
# ---------------------------------------------------------------------------
def section_c():
    print("\n--- Section C [A]: K2 — IR-slope dressing grid "
          "m/(4 pi N) x {1, u_0^-2}, all 40 cells ---")
    print("    (declared: factor = [m/(4 pi)] / N x dressing; "
          "normalizations DIVIDE; m and N from the landed candidates)")

    masses = [("1", 1.0), ("2u_0", 2.0 * U_0), ("u_0", U_0),
              ("u_0^2", U_0 ** 2)]
    norms = [("1", lambda m: 1.0), ("1/8", lambda m: 0.125),
             ("1/16", lambda m: 0.0625), ("2u_0", lambda m: 2.0 * U_0),
             ("f(m)", lambda m: f_mode(m))]
    dressings = [("undressed", 1.0), ("u_0^-2", U_0 ** -2)]

    # Definitional identity cells (exact chain members by construction).
    DEFINITIONAL.update({
        "K2 m=1/N=1/u_0^-2",          # = alpha_s exactly (the chain)
        "K2 m=2u_0/N=2u_0/u_0^-2",    # = alpha_s exactly (m cancels)
        "K2 m=1/N=1/undressed",       # = alpha_bare exactly
        "K2 m=2u_0/N=2u_0/undressed",  # = alpha_bare exactly
        "K2 m=u_0/N=1/u_0^-2",        # = alpha_LM exactly
        "K2 m=u_0^2/N=1/u_0^-2",      # = alpha_bare exactly
        "K2 m=u_0/N=2u_0/u_0^-2",     # = alpha_s/2 = block01's N exactly
    })

    cells = {}
    for mn, m in masses:
        for nn, nf in norms:
            for dn, d in dressings:
                rid = f"K2 m={mn}/N={nn}/{dn}"
                v = m / (4.0 * math.pi) / nf(m) * d
                cells[rid] = v
                add_row(rid, f"[m/(4 pi)]/N x {dn} at m = {mn}, "
                             f"N = {nn}", v)

    # C1 [A]: grid size and exhaustiveness.
    check("A", "C1 grid exhaustiveness: all 4 masses x 5 normalizations "
               "x 2 dressings = 40 cells computed and printed (every "
               "cell an exact closed form alpha_s x algebraic factor in "
               "u_0 and rationals)", len(cells) == 40,
          f"{len(cells)} cells")

    # C2 [A]: the ONLY match-window cells are the definitional identity
    # cells — and they equal alpha_s EXACTLY.
    in_match = [rid for rid, v in cells.items()
                if MATCH_LO - EPS <= v / ALPHA_S <= MATCH_HI + EPS]
    ident_s = ["K2 m=1/N=1/u_0^-2", "K2 m=2u_0/N=2u_0/u_0^-2"]
    exact_s = all(abs(cells[r] - ALPHA_S) < 1e-15 for r in ident_s)
    check("A", "C2 GUARD (the block10b §3 pattern — exact match is BY "
               "CONSTRUCTION): the ONLY cells inside [0.99, 1.01] x "
               "alpha_s are (m=1, N=1, dressed) and (m=2u_0, N=2u_0, "
               "dressed), both equal to alpha_s EXACTLY (< 1e-15) "
               "because each IS the supplier-chain identity alpha_s = "
               "(1/(4 pi)) u_0^-2 written in grid coordinates (the "
               "second after the per-mode-factor normalization cancels "
               "m).  DEFINITIONAL cells, zero mechanism content — the "
               "mechanism would be exactly the open identification; "
               "NOT candidate matches",
          sorted(in_match) == sorted(ident_s) and exact_s,
          f"in-window cells = {sorted(in_match)}")

    # C3 [A]: the exact-identity audit of all canonical cells.
    ident_checks = (
        abs(cells["K2 m=1/N=1/undressed"] - ALPHA_BARE) < 1e-15
        and abs(cells["K2 m=2u_0/N=2u_0/undressed"] - ALPHA_BARE) < 1e-15
        and abs(cells["K2 m=u_0/N=1/u_0^-2"] - ALPHA_LM) < 1e-15
        and abs(cells["K2 m=u_0^2/N=1/u_0^-2"] - ALPHA_BARE) < 1e-14
        and abs(cells["K2 m=u_0/N=2u_0/u_0^-2"] - ALPHA_S / 2.0) < 1e-15)
    check("A", "C3 exact-identity audit: the remaining canonical cells "
               "are exact chain members — (m=1, N=1, undressed) = "
               "(m=2u_0, N=2u_0, undressed) = (m=u_0^2, N=1, dressed) = "
               "alpha_bare (displacement u_0^2 = 0.7703); (m=u_0, N=1, "
               "dressed) = alpha_LM (displacement u_0 = 0.8777); "
               "(m=u_0, N=2u_0, dressed) = 1/(8 pi u_0^2) = alpha_s/2 = "
               "block01's N = 0.0516519 (displacement 1/2 exactly) — "
               "all flagged EXACT-IDENTITY in the table, never "
               "observations", ident_checks,
          f"block01 N cell = {cells['K2 m=u_0/N=2u_0/u_0^-2']:.7f}")

    # C4 [A]: K2 verdict.
    non_def_match = [r for r in in_match if r not in DEFINITIONAL]
    f2_nondef = [r for r, v in cells.items()
                 if r not in DEFINITIONAL
                 and window_class(v) == "factor2"]
    check("A", "C4 K2 VERDICT: NO non-definitional cell lands in the "
               "match window — within this dressing grid, hitting "
               "alpha_s requires EXACTLY the definitional combination "
               "(slope at unit mass, unit normalization, two-link "
               "dressing), i.e. the grid contributes no independent "
               "route to the attachment; non-identity factor-2 cells "
               "(printed flags) are exact algebraic u_0-power/rational "
               "multiples of alpha_s — observation-grade only",
          len(non_def_match) == 0 and len(f2_nondef) >= 5,
          f"non-definitional match cells = {non_def_match}; "
          f"factor-2 cells = {len(f2_nondef)}")
    return f2_nondef


# ---------------------------------------------------------------------------
# Section D — K3: the Matsubara free-energy-density surface.
# ---------------------------------------------------------------------------
def section_d():
    print("\n--- Section D [C]/[A]: K3 — free-energy-density per mode on "
          "the landed Matsubara surface ---")

    # D1 [C]: at L_t = 2 the landed closed form IS block01's determinant.
    # |det(D + m)| = prod_omega [m^2 + u^2 (3 + sin^2 omega)]^4 with
    # omega in {pi/2, 3 pi/2}, sin^2 omega = 1 exactly, so per color
    # = (m^2 + 4 u^2)^8 — exact Fraction check (sin^2 entered as the
    # exact integer 1).
    frac_ok = True
    for u in (Fraction(2, 3), Fraction(7, 8)):
        for m in (Fraction(0), Fraction(1, 3)):
            factor = (m ** 2 + u ** 2 * (3 + 1)) ** 4   # one omega
            det_formula = factor ** 2                    # two omegas
            det_block01 = (m ** 2 + 4 * u ** 2) ** 8
            frac_ok = frac_ok and det_formula == det_block01
    check("C", "D1 surface identification (exact Fraction, sin^2(pi/2) "
               "= sin^2(3 pi/2) = 1 exact): at L_t = 2 the landed "
               "Matsubara closed form prod_omega [m^2 + u_0^2 (3 + "
               "sin^2 omega)]^4 equals block01's per-color determinant "
               "(m^2 + 4 u_0^2)^8 EXACTLY — the surface's per-taste-mode "
               "decimation reading exists ONLY through this "
               "identification, and there the per-mode factor IS "
               "block01's f(m) = sqrt(m^2 + 4 u_0^2), already "
               "enumerated as K1", frac_ok,
          "4 rational test points")

    # D2 [A]: the direct n_matrix = 16 -> 15 reading is NOT constructible.
    reachable = {8 * lt for lt in range(1, 9)}
    check("A", "D2 NOT-CONSTRUCTIBLE record (honest, per the task's own "
               "criterion): the surface's mode count is n_matrix = "
               "8 L_t in {8, 16, 24, ...} — n_matrix = 15 is unreachable "
               "(no integer L_t), so a DIRECT per-entry 16 -> 15 "
               "free-energy difference does NOT exist on the landed "
               "surface; the candidate is recorded as not-constructible "
               "in that reading (itself a useful enumeration datum)",
          16 in reachable and 15 not in reachable
          and all(n % 8 == 0 for n in reachable))

    # D3 [A]: the per-entry density readout that IS constructible.
    vals = []
    for mn, m in (("u_0", U_0), ("2u_0", 2.0 * U_0), ("1", 1.0)):
        lt = 2
        df = (1.0 / (2 * lt)) * sum(
            math.log(1.0 + m * m
                     / (U_0 ** 2
                        * (3.0 + math.sin((2 * n + 1) * math.pi
                                          / lt) ** 2)))
            for n in range(lt))
        v = math.exp(-df)
        closed = 2.0 * U_0 / f_mode(m)
        vals.append((mn, v, closed))
        add_row(f"K3 exp(-Delta_f) m={mn}",
                f"per-entry free-energy-density factor at L_t = 2, "
                f"m = {mn}", v,
                "= 2 u_0/f(m) exactly")
    check("A", "D3 per-entry density readout (constructible): "
               "exp(-Delta_f(L_t = 2, m)) = 2 u_0/f(m) EXACTLY "
               "(< 1e-14 at all three masses) — values 0.894 (m = u_0), "
               "0.707 = 2^(-1/2) (threshold m = 2 u_0), 0.869 (m = 1); "
               "displacements 6.84x-8.66x — the inverse of a K1 ratio, "
               "nothing new",
          all(abs(v - c) < 1e-14 for _, v, c in vals)
          and abs(vals[1][1] - 2.0 ** -0.5) < 1e-14,
          f"threshold value = {vals[1][1]:.7f}")

    # D4 [A]: K3 verdict.
    check("A", "D4 K3 VERDICT: the direct 16 -> 15 per-entry reading is "
               "not-constructible (D2); every constructible reading "
               "(per-mode via the block01 identification = K1; "
               "per-entry density = 2 u_0/f(m)) is O(1)-displaced "
               "(6.84x-8.66x) — eliminated",
          all(window_class(v) == "out" for _, v, _ in vals))


# ---------------------------------------------------------------------------
# Section E — K4: static-potential screening share (block08 import).
# ---------------------------------------------------------------------------
def section_e():
    print("\n--- Section E [B]/[A]: K4 — static-potential screening "
          "share at threshold (block08's landed R_S2, imported) ---")

    b08 = (DOCS / "HIERARCHY_DELTA0_S2_READOUT_DRESSING_LEADING_ORDER_"
                  "PROBE_NOTE_2026-06-11.md")
    t08 = b08.read_text() if b08.exists() else ""

    # E1 [B]: literals on disk + threshold-scale honesty.
    r_thr = 1.0 / (2.0 * U_0)
    check("B", "E1 import verification + threshold-scale honesty: "
               "block08's landed R_S2 literals verified on disk "
               "(1.012323, 1.021340; displacement bounds 9.7995/9.8868; "
               "c0 = 0.0266477); the threshold separation r = 1/(2 u_0) "
               "= 0.5697 lattice units is SUB-LATTICE — the candidate "
               "is SCALE-MISMATCHED at its declared threshold scale, "
               "and the landed radii r = 4, 6, 8 are the declared "
               "answer (the threshold reading is carried by K7's r = 1 "
               "exponentials instead)",
          "1.012323" in t08 and "1.021340" in t08
          and "9.7995" in t08 and "9.8868" in t08
          and "0.0266477" in t08
          and 0.0 < r_thr < 1.0
          and abs(r_thr - 0.569683) < 5e-7,
          f"r_threshold = {r_thr:.6f} < 1")

    # E2 [A]: the imported table and its displacements.
    imported = [
        ("V-a1 r=4", 1.012323), ("V-a1 r=6", 1.014520),
        ("V-a1 r=8", 1.015913), ("V-a2 r=4", 1.018515),
        ("V-a2 r=8", 1.021340), ("V-b all r", 1.019038),
    ]
    for name, v in imported:
        add_row(f"K4 R_S2 {name}",
                "block08 per-decimation static-potential factor "
                "(imported, landed)", v)
    disps = [v / ALPHA_S for _, v in imported]
    check("A", "E2 K4 VERDICT: eliminated (already landed displaced) — "
               "R_S2 in [1.0123, 1.0213], displacements 9.7995x-9.8868x "
               "above alpha_s, matching block08's stated bounds < 5e-4; "
               "included for enumeration completeness",
          min(disps) > 9.79 and max(disps) < 9.89
          and abs(min(disps) - 9.7995) < 5e-4
          and abs(max(disps) - 9.8868) < 5e-4,
          f"displacements = [{min(disps):.4f}, {max(disps):.4f}]x")


# ---------------------------------------------------------------------------
# Section F — K5: plaquette-action cost readouts (block10a import).
# ---------------------------------------------------------------------------
def watson_g0(L: int) -> float:
    """Z^3 return Green value G(0) on the half-shifted L^3 BZ grid
    (block10a's deterministic construction, reused)."""
    c = [2.0 - 2.0 * math.cos(2.0 * math.pi * (n + 0.5) / L)
         for n in range(L)]
    s = 0.0
    for a in c:
        for b in c:
            ab = a + b
            s += sum(1.0 / (ab + cc) for cc in c)
    return s / L ** 3


def section_f():
    print("\n--- Section F [B]/[A]: K5 — plaquette-action cost readouts "
          "exp(-Delta_S_candidate) (block10a scan rows, imported + "
          "verified) ---")

    b10a = (DOCS / "HIERARCHY_DELTA0_S1PRIME_ACTION_COST_DECOMPOSITION_"
                   "NOTE_2026-06-11.md")
    t10a = b10a.read_text() if b10a.exists() else ""

    # F1 [B]: block10a literals on disk + Delta_S consistency.
    check("B", "F1 import verification: block10a literals on disk "
               "(Delta_S = 2.270081; nearest-gap 0.072856; flagged "
               "exp-gap 1.075576); recomputed Delta_S = ln(4 pi) + "
               "2 ln(u_0) matches < 5e-7",
          "2.270081" in t10a and "0.072856" in t10a
          and "1.075576" in t10a
          and abs(DELTA_S - 2.270081) < 5e-7
          and abs(DELTA_S - (math.log(4 * math.pi)
                             + 2 * math.log(U_0))) < 1e-12,
          f"Delta_S = {DELTA_S:.6f}")

    # F2 [A]: G(0) recomputed deterministically (verification, not faith).
    g = {L: watson_g0(L) for L in (24, 32, 40)}
    def rich(l1, l2):
        return (l2 * g[l2] - l1 * g[l1]) / (l2 - l1)
    g0 = rich(32, 40)
    check("A", "F2 G(0) recomputed (half-shifted BZ sums L = 24, 32, 40 "
               "+ Richardson in 1/L, block10a's construction): pair "
               "estimates agree < 2e-5; production G(0) = 0.252736 "
               "matches the Watson reference within 5e-5",
          abs(rich(24, 32) - rich(32, 40)) < 2e-5
          and abs(g0 - G0_WATSON_REF) < 5e-5,
          f"G(0) = {g0:.7f}")

    # F3 [A]: the exp(-action) table.
    k5_rows = [
        ("K5 exp(-ln(2u_0)) = 1/(2u_0)", "block01 per-mode determinant "
         "log, exponentiated", 1.0 / (2.0 * U_0), ""),
        ("K5 exp(+ln u_0) = 1/u_0", "block02 ratio-normalized per-mode "
         "log, exponentiated", 1.0 / U_0, ""),
        ("K5 pi^-4", "per-mode BZ Haar cell (2^4 block)",
         math.pi ** -4, ""),
        ("K5 pi^-3", "per-mode BZ Haar cell (2^3 block)",
         math.pi ** -3, ""),
        ("K5 1/(4 pi) = alpha_bare", "the kernel normalization itself",
         ALPHA_BARE, "= alpha_s x u_0^2 exactly (block10a row (d): "
         "definitional)"),
        ("K5 G(0)", "Z^3 return Green value (recomputed F2)", g0, ""),
        ("K5 c0 (block08)", "one-loop bubble constant (literal on disk, "
         "E1)", C0_BLOCK08, ""),
        ("K5 1/N_c", "strong-coupling weight", 1.0 / N_C, ""),
        ("K5 1/(2 N_c)", "NJL G_eff weight", 1.0 / (2 * N_C), ""),
        ("K5 1/N_c^2", "two-dimer/Weingarten layer",
         1.0 / N_C ** 2, "block09-flagged 1/N_c^2 proximity"),
    ]
    for rid, dfn, v, note in k5_rows:
        add_row(rid, dfn, v, note)
    nc2_disp = (1.0 / N_C ** 2) / ALPHA_S
    in_match = [rid for rid, _, v, _ in k5_rows
                if window_class(v) == "match"]
    check("A", "F3 K5 VERDICT: NO scan row in the match window — the "
               "nearest non-definitional row is 1/N_c^2 at 1.0756x "
               "(exactly block10a's exp-gap 1.075576, i.e. block09's "
               "numerology-risk-flagged 1/N_c^2 proximity RESTATED — no "
               "content added); 1/(4 pi) sits at u_0^2 = 0.7703x "
               "(definitional, block10a row (d)); eliminated",
          len(in_match) == 0
          and abs(nc2_disp - 1.075576) < 5e-6
          and abs(ALPHA_BARE / ALPHA_S - U_0 ** 2) < 1e-14)


# ---------------------------------------------------------------------------
# Section G — K6/K7/K8: this block's additional declared candidates.
# ---------------------------------------------------------------------------
def bz_logdet_share(m: float, u: float, L: int) -> float:
    """V(m; u) = (1/L^3) sum_k ln(1 + m^2/(u^2 s^2(k))) on the
    half-shifted d = 3 grid, s^2 = sum_mu sin^2 k_mu (block10b's
    mode-sum symbol with mean-field dressing u)."""
    s2 = [math.sin(math.pi * (2 * j + 1) / L) ** 2 for j in range(L)]
    m2 = m * m
    u2 = u * u
    tot = 0.0
    for a in s2:
        for b in s2:
            ab = a + b
            for c in s2:
                tot += math.log1p(m2 / (u2 * (ab + c)))
    return tot / L ** 3


def section_g():
    print("\n--- Section G [A]: K6/K7/K8 — this block's additional "
          "declared candidates ---")

    # G1 [A]: K6 equal-share mode-sum ratio readouts.
    k6 = [
        ("K6 15/16", "ratio-normalized additive mode-sum share after "
         "one decoupling (equal-share lemma, exact rational)",
         15.0 / 16.0, "exact rational"),
        ("K6 1/8", "d = 3 per-taste rational share", 0.125,
         "block10b-flagged observation restated"),
        ("K6 1/16", "d = 4 per-taste rational share", 0.0625,
         "block10b-flagged observation restated"),
        ("K6 exp(-1/8)", "exponentiated d = 3 share (log-Z reading)",
         math.exp(-0.125), ""),
        ("K6 exp(-1/16)", "exponentiated d = 4 share (log-Z reading)",
         math.exp(-0.0625), ""),
    ]
    for rid, dfn, v, note in k6:
        add_row(rid, dfn, v, note)
    check("A", "G1 K6 equal-share readouts: 15/16 = 0.9375 (9.08x), "
               "exp(-1/8) (8.54x), exp(-1/16) (9.09x) — O(1); the bare "
               "shares 1/8 (1.2100x) and 1/16 (0.6050x) fall in the "
               "factor-2 window EXACTLY as block10b already flagged "
               "(additive shares, not multiplicative factors; small "
               "rationals populate a factor-2 window generically) — "
               "restated, no content added",
          window_class(15.0 / 16.0) == "out"
          and window_class(0.125) == "factor2"
          and window_class(0.0625) == "factor2"
          and abs(0.125 / ALPHA_S - 1.2100) < 5e-4
          and abs(0.0625 / ALPHA_S - 0.6050) < 5e-4)

    # G2 [A]: K7 threshold screening exponentials at r = 1.
    k7 = [
        ("K7 exp(-2u_0 r), r=1", "Yukawa screening at the threshold "
         "mass 2 u_0 (mode gap), evaluated at the nearest on-lattice "
         "separation r = 1 (declared honest reading of the sub-lattice "
         "threshold scale 1/(2 u_0) = 0.5697)",
         math.exp(-2.0 * U_0), "factor-2: numerology-risk"),
        ("K7 exp(-u_0 r), r=1", "screening at mass u_0, r = 1",
         math.exp(-U_0), ""),
        ("K7 exp(-r/(2u_0)), r=1", "screening at inverse threshold "
         "separation, r = 1", math.exp(-1.0 / (2.0 * U_0)), ""),
    ]
    for rid, dfn, v, note in k7:
        add_row(rid, dfn, v, note)
    v_thr = math.exp(-2.0 * U_0)
    check("A", "G2 K7 threshold screening exponentials (r = 1, "
               "declared): exp(-2 u_0) = 0.172845 (1.6732x — factor-2 "
               "window, numerology-risk flagged below: no mechanism, no "
               "supplier, no claim), exp(-u_0) (4.02x), "
               "exp(-1/(2 u_0)) (5.48x) — none anywhere near the match "
               "window",
          window_class(v_thr) == "factor2"
          and abs(v_thr / ALPHA_S - 1.6732) < 5e-4
          and window_class(math.exp(-U_0)) == "out"
          and window_class(math.exp(-1.0 / (2.0 * U_0))) == "out")

    # G3 [A]: K8 per-taste BZ log-det share readouts (computed).
    print("    (K8 declared grids: half-shifted d = 3, L = 32 and 48; "
          "declared tolerance |L48 - L32| < 5e-4 on every readout)")
    k8_vals = {}
    stable = True
    for mn, m in (("u_0", U_0), ("2u_0", 2.0 * U_0)):
        per_l = {}
        for L in (32, 48):
            v_u = bz_logdet_share(m, U_0, L)
            v_1 = bz_logdet_share(m, 1.0, L)
            per_l[L] = (math.exp(-v_u / 8.0),
                        math.exp(-(v_u - v_1) / 8.0))
        stable = stable and all(
            abs(per_l[48][i] - per_l[32][i]) < 5e-4 for i in (0, 1))
        k8_vals[mn] = per_l[48]
        add_row(f"K8 exp(-V(m={mn};u_0)/8)",
                "per-taste BZ log-det share of the dressed mode sum "
                "(block10b symbol), exponentiated", per_l[48][0],
                "L = 48, grid-stable < 5e-4")
        add_row(f"K8 ratio-norm m={mn}",
                "dressed/undressed (u_0 vs 1) ratio-normalized per-taste "
                "log-det share, exponentiated", per_l[48][1],
                "L = 48, grid-stable < 5e-4")
    check("A", "G3 K8 per-taste BZ log-det share readouts (computed, "
               "declared grids): exp(-V/8) = 0.8383 (m = 2 u_0) and "
               "0.9281 (m = u_0); ratio-normalized 0.9771 and 0.9871 — "
               "displacements 8.11x-9.56x; grid-stable |L48 - L32| "
               "< 5e-4 on all four", stable
          and abs(k8_vals["2u_0"][0] - 0.838270) < 5e-4
          and abs(k8_vals["u_0"][0] - 0.928146) < 5e-4
          and abs(k8_vals["2u_0"][1] - 0.977066) < 5e-4
          and abs(k8_vals["u_0"][1] - 0.987067) < 5e-4,
          f"values = {[round(x, 6) for p in k8_vals.values() for x in p]}")

    # G4 [A]: K6-K8 verdict.
    extra_vals = ([v for _, _, v, _ in k6] + [v for _, _, v, _ in k7]
                  + [x for p in k8_vals.values() for x in p])
    in_match = [v for v in extra_vals if window_class(v) == "match"]
    check("A", "G4 K6-K8 VERDICT: eliminated — no additional candidate "
               "in the match window; the in-factor-2 entries (1/8, "
               "1/16, exp(-2 u_0)) are flagged observations only",
          len(in_match) == 0)


# ---------------------------------------------------------------------------
# Section H — global verdict, observations, residuals.
# ---------------------------------------------------------------------------
def section_h(k2_f2_nondef):
    print("\n--- Section H [A]/[B]: global enumeration verdict ---")

    match_rows = [(rid, v) for rid, _, v, _ in ROWS
                  if MATCH_LO - EPS <= v / ALPHA_S <= MATCH_HI + EPS]
    match_nondef = [rid for rid, _ in match_rows
                    if rid not in DEFINITIONAL]
    f2_rows = [(rid, v) for rid, _, v, _ in ROWS
               if rid not in DEFINITIONAL
               and window_class(v) == "factor2"]

    print(f"    enumerated candidate rows: {len(ROWS)}")
    print(f"    match-window entries: {len(match_rows)} "
          f"(all definitional: {[r for r, _ in match_rows]})")
    print(f"    non-definitional factor-2 entries: {len(f2_rows)}")
    for rid, v in f2_rows:
        print(f"      {rid:34s} {v:10.7f}  ({v / ALPHA_S:.4f}x)")

    # H1 [A]: the kill-criterion verdict.
    check("A", "H1 GLOBAL ENUMERATION VERDICT (the block10b R2 kill "
               "criterion, executed): over all "
               f"{len(ROWS)} enumerated candidate rows, the ONLY "
               "entries inside [0.99, 1.01] x alpha_s are the two "
               "DEFINITIONAL K2 identity cells (the supplier chain "
               "alpha_s = (1/(4 pi)) u_0^-2 itself in grid coordinates "
               "— by construction, zero mechanism content); NO candidate "
               "READOUT lands in the window with a mechanism.  THE KILL "
               "CRITERION FIRES for the enumerated class: the attachment "
               "observable, if it exists, is NOT among the K1-K8 "
               "declared readouts under the declared normalizations",
          len(match_nondef) == 0 and len(match_rows) == 2
          and len(ROWS) == 91,
          f"non-definitional matches = {match_nondef}")

    # H2 [B]: parent-note honesty.
    note_text = PARENT_NOTE.read_text() if PARENT_NOTE.exists() else ""
    lowered = " ".join(note_text.lower().split())
    required = [
        "kill criterion",
        "not among the k1-k8 declared readouts",
        "does not close the delta0 gate",
        "numerology",
    ]
    forbidden = [
        "closes the delta0 gate",
        "candidate match found",
    ]
    req_missing = [t for t in required if t not in lowered]
    forb_hit = [t for t in forbidden if t in lowered]
    check("B", "H2 parent-note honesty: the note on disk states the "
               "fired kill criterion, the constraint set ('not among "
               "the K1-K8 declared readouts'), the numerology guards, "
               "and that it does not close the DELTA0 gate; forbidden "
               "closure/match tokens absent",
          not req_missing and not forb_hit,
          f"missing = {req_missing}, hit = {forb_hit}")

    print()
    observation("K2 non-identity factor-2 cells "
                f"({len(k2_f2_nondef)} of 40): every one is an EXACT "
                "closed form alpha_s x (u_0-power x rational) — e.g. "
                "(m=2u_0, N=1, dressed) = 2 alpha_LM = 1.7554 x alpha_s "
                "(displacement = 2 u_0 exactly), (m=u_0^2, N=1, "
                "undressed) = alpha_s x u_0^4 (displacement = <P> = "
                "0.5934 exactly); small algebraic u_0-power/rational "
                "multiples populate a factor-2 window generically (the "
                "block09 lesson).  No mechanism, no supplier, no claim.")
    observation("K5 factor-2 entries: 1/N_c^2 = 1.0756 x alpha_s — "
                "EXACTLY block09's flagged 1/N_c^2 proximity "
                "(4 pi u_0^2/9 = 1.075576), restated a third time with "
                "NO content added; 1/(2 N_c) = 1.6134 x alpha_s.  "
                "Numerology-risk flags inherited and maintained.")
    observation("K6 rational shares 1/8 = 1.2100 x alpha_s and 1/16 = "
                "0.6050 x alpha_s — block10b's already-flagged in-window "
                "proximities restated: shares of an ADDITIVE mode sum, "
                "not multiplicative per-decoupling factors.  No "
                "mechanism, no supplier, no claim.")
    observation("K7 threshold screening exp(-2 u_0 x 1) = 0.172845 = "
                "1.6732 x alpha_s (new this block): a Yukawa factor at "
                "the mode-gap mass and unit separation lands in the "
                "factor-2 window.  The threshold scale 1/(2 u_0) is "
                "sub-lattice (E1), the separation choice r = 1 is a "
                "declared convenience, and no readout ties this "
                "exponential to a decoupling count.  Numerology-risk "
                "flagged; no mechanism, no supplier, no claim.")
    print()
    residual("the B4 ATTACHMENT-OBSERVABLE IDENTIFICATION (block10b R2) "
             "remains UNSUPPLIED, and now carries the computed "
             "constraint set 'NOT K1-K8': the readout in which one "
             "decoupling taste contributes exactly alpha_s = "
             "(1/(4 pi)) x u_0^-2 = 0.1033038 is NOT the "
             "determinant-share family (K1: 8.50x-24.03x), NOT the "
             "IR-slope dressing grid away from its definitional cells "
             "(K2), NOT the Matsubara free-energy-density surface (K3: "
             "direct 16->15 not-constructible; constructible readings "
             "6.84x-8.66x), NOT the static-potential screening share "
             "(K4: 9.80x-9.89x, landed), NOT the plaquette-action cost "
             "family (K5: nearest non-definitional 1/N_c^2 at 1.0756x, "
             "flagged), NOT the equal-share mode-sum ratios (K6), NOT "
             "threshold screening exponentials (K7), NOT per-taste BZ "
             "log-det shares (K8: 8.11x-9.56x).  Any closing "
             "identification must exhibit block10b's four testable "
             "consequences (log-additivity, threshold-scale evaluation, "
             "two-link vertex dressing, d = 3 substrate) AND lie "
             "outside the enumerated class.")
    residual("the DELTA0 gate (HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_"
             "GATE_NOTE_2026-05-30.md) remains OPEN: this block fires "
             "block10b's kill criterion for the enumerated readout "
             "class — an elimination within the taste-region arm of "
             "S1', NOT a closure and NOT a full elimination of S1' "
             "(readouts outside K1-K8, and the non-perturbative arms of "
             "S2/S3, are untouched).  The route inventory is not "
             "modified.")


# ---------------------------------------------------------------------------
# Terminal class-D fence (external comparators).
# ---------------------------------------------------------------------------
def section_fence():
    print("\n--- Terminal class-D fence: external comparators ---")
    print("  (No PDG quantity is needed or consumed by this enumeration; "
          "every comparison")
    print("   target is framework-internal: alpha_s/alpha_LM/alpha_bare "
          "from the B1+I2+I3 chain.)")
    src = Path(__file__).read_text()
    pdg_literal = "246." + "22"  # composed so the scan finds only real uses
    check("D", "Z1 self-scan: the PDG VEV literal appears ZERO times in "
               "this runner's source — no comparator consumed anywhere",
          src.count(pdg_literal) == 0)


def main() -> int:
    print("=" * 78)
    print(" frontier_hierarchy_delta0_b4_attachment_observable_"
          "enumeration_2026_06_11.py")
    print(" Block11 of the DELTA0 attachment campaign: executing "
          "block10b's R2 kill")
    print(" criterion — enumerate the declared candidate readouts "
          "(K1-K8), compute each")
    print(" per-decoupling multiplicative factor, tabulate displacements "
          "vs alpha_s =")
    print(" 0.1033038 (and alpha_LM/alpha_bare cross-references), and "
          "render the verdict.")
    print(" Parent note: docs/HIERARCHY_DELTA0_B4_ATTACHMENT_OBSERVABLE_"
          "ENUMERATION_")
    print("              NOTE_2026-06-11.md")
    print("=" * 78)

    section_a()
    section_b()
    k2_f2 = section_c()
    section_d()
    section_e()
    section_f()
    section_g()
    section_h(k2_f2)
    section_fence()

    print()
    print("=" * 78)
    print(f" Breakdown: A={CLASS_COUNTS['A']} B={CLASS_COUNTS['B']} "
          f"C={CLASS_COUNTS['C']} D={CLASS_COUNTS['D']} "
          f"RESIDUAL={RESIDUAL_COUNT} OBSERVATION={OBSERVATION_COUNT}")
    print(f" TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(" VERDICT: established (bounded; exact where exact, declared "
          "grids elsewhere):")
    print("   the B4-attachment observable-identification enumeration is "
          "COMPLETE for the")
    print("   declared class K1-K8 (91 candidate rows, every "
          "normalization declared).")
    print("   The ONLY match-window entries are the two definitional K2 "
          "identity cells —")
    print("   the supplier chain alpha_s = (1/(4 pi)) u_0^-2 itself in "
          "grid coordinates,")
    print("   zero mechanism content.  NO candidate readout lands in "
          "[0.99, 1.01] x")
    print("   alpha_s with a mechanism: block10b's KILL CRITERION FIRES "
          "for the")
    print("   enumerated class.  The identification theorem gains the "
          "constraint set")
    print("   'not K1-K8'; factor-2 entries are numerology-risk-flagged "
          "observations")
    print("   only; the taste-region arm of S1' survives only outside "
          "the enumerated")
    print("   readout class.  DELTA0 stays open — an elimination, not a "
          "closure.")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
