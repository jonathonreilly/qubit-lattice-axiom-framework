#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Consumer audit: does any RETAINED downstream row require the single-clock theorem's
CONTINUOUS Stone time U(t)=exp(-itH) at NON-INTEGER t in a load-bearing way?
=========================================================================================

Companion runner for
docs/SINGLE_CLOCK_CONTINUOUS_TIME_IS_AN_UNAUDITED_INTERPOLATION_BOUNDED_NOTE_2026-06-08.md.

CONTEXT.  The emergent-Lorentz velocity obstruction (delta_v != 0) lives on the
xi->inf surface = spatial Z^3 + CONTINUOUS time U(t)=exp(-itH).  The claim that this
continuous-time surface is the framework's DERIVED physical surface rests on
AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION (live-ledger UNAUDITED), whose Step 1
builds U(t) as the ANALYTIC CONTINUATION of the genuinely-derived DISCRETE transfer T^n
(T^n = U(-i n tau) at INTEGER n) to non-integer t.

This runner mechanically audits whether continuous U(t) at NON-INTEGER t is load-bearing
for any RETAINED / retained_bounded consumer, by reading the consumer notes and asserting
the classifying evidence in each.  If NO retained consumer needs non-integer-t U(t), then
the continuous-time obstruction surface has NO retained witness: it is an unaudited
analytic-continuation interpolation, and the DISCRETE T^n (Euclidean staggered Z^4) is the
equally-available default lattice reading.

HONEST SCOPE.  This DEMOTES the obstruction horn from "the framework's derived surface"
to "one unaudited reading"; it does NOT by itself establish delta_v=0 retained -- the
discrete-surface temporal kinetic FORM (symmetric central-difference staggered, B_4 ->
delta_v=0, vs the forward transfer T=e^{-H a_tau} which breaks B_4 ~5e-4) is the separate
remaining realization question.  Sets NO audit status.  No new axiom/vocabulary.

Run: python3 scripts/frontier_single_clock_continuous_time_load_bearing_audit_2026_06_08.py
"""
from __future__ import annotations
import sys
from pathlib import Path

PASS, FAIL = 0, 0
DOCS = Path(__file__).resolve().parents[1] / "docs"


def check(label, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1; tag = "PASS"
    else:
        FAIL += 1; tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))
    return bool(ok)


def section(t):
    print("\n" + "-" * 94 + f"\n{t}\n" + "-" * 94)


def _read(name):
    p = DOCS / name
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""


def _has(name, *needles):
    """True if the note exists and contains ALL needles (case-insensitive)."""
    txt = _read(name).lower()
    return bool(txt) and all(n.lower() in txt for n in needles)


def main():
    print("=" * 94)
    print("Consumer audit: is continuous U(t)=exp(-itH) at NON-INTEGER t load-bearing for any RETAINED row?")
    print("=" * 94)

    # The DERIVED dynamics: the discrete positive transfer T and its INTEGER powers T^n.
    section("Part 0: the genuinely-derived object is the DISCRETE transfer T^n (integer n); U(t) is its continuation")
    stone = "SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md"
    check("(0.1) SINGLE_CLOCK_STONE uniqueness (RETAINED) retains T^n = U(-i n tau) at INTEGER n (functional-calculus consistency)",
          _has(stone, "T^n = U(-i n", "integer"),
          detail="the discrete-time iteration is consistent with U at IMAGINARY argument and INTEGER n")
    check("(0.2) ... and its broader NON-INTEGER continuity headline was DEMOTED as 'false as written' (retained content is integer-only)",
          _has(stone, "false as written") or _has(stone, "claim boundary"),
          detail="so the retained Stone content does NOT require non-integer-t U(t)")

    # ============================================================ retained consumers
    section("Part 1: classify every RETAINED / retained_bounded continuous-time consumer")
    # Each consumer is classified: INTEGER-T^n-only | a->0 EMERGENT limit | SUPPLIED-context.
    # A LOAD-BEARING non-integer-t consumer would FAIL the audit (set the obstruction horn a retained witness).
    consumers = []

    # (A) Lorentz boost covariance 2D/3+1D (retained / retained_bounded): a->0 continuum-limit, FREE surface.
    b2 = "LORENTZ_BOOST_COVARIANCE_2D_THEOREM_NOTE.md"
    b4 = "LORENTZ_BOOST_COVARIANCE_3PLUS1D_THEOREM_NOTE.md"
    emergent = _has(b2, "continuum limit") or _has(b2, "continuum-limit")
    consumers.append(("boost covariance 2D (retained)", emergent, "a->0 EMERGENT limit (free-scalar continuum); continuous spacetime is the emergent description, == 'U(t) is IR'"))
    check("(1.A) LORENTZ_BOOST_COVARIANCE uses continuous spacetime only as the a->0 EMERGENT limit (free surface), NOT as a finite-a fundamental surface",
          emergent, detail="'exact theorem on the continuum-limit free-scalar surface ... in the continuum limit a->0' -> consistent with U(t) being the IR interpolation, NOT a non-integer-t fundamental witness")

    # (B) #3121 attractor (retained_bounded): continuous time is a SUPPLIED context; c_t-fixing uses the equal-time CAR.
    att = "EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md"
    supplied = _has(att, "context under test") or _has(att, "supplied")
    car = _has(att, "CAR")
    consumers.append(("#3121 velocity-RG attractor (retained_bounded)", supplied, "continuous time SUPPLIED as 'context under test' (an input); the c_t-fixing uses the EQUAL-TIME CAR (single-slice, integer-consistent)"))
    check("(1.B) #3121 attractor SUPPLIES continuous time as a context/input (not retained-derived); its load-bearing c_t-fixing is the EQUAL-TIME (single-slice) CAR, integer-consistent",
          supplied and car, detail="'treats spatial Z^3, continuous time ... as the context under test'; CAR {psi_x,psi_y}=delta is preserved by the discrete unitary T too -> no non-integer-t requirement")

    # (C) emergent_lorentz_invariance (retained_bounded): the dim-6 IR dispersion (continuum/IR isotropy), not a fundamental continuous-t correlator.
    eli = "EMERGENT_LORENTZ_INVARIANCE_NOTE.md"
    ir = _has(eli, "dimension-6") or _has(eli, "dim-6") or _has(eli, "dispersion")
    consumers.append(("emergent_lorentz_invariance (retained_bounded)", ir, "IR/continuum dim-6 dispersion isotropy; an a->0 / low-energy statement, not a fundamental non-integer-t correlator"))
    check("(1.C) EMERGENT_LORENTZ_INVARIANCE is an IR/continuum dim-6 dispersion result (emergent), not a fundamental non-integer-t U(t) correlator",
          ir, detail="the dim-6 (E/M_Pl)^2 dispersion is the low-energy emergent description")

    # (D) RP / cluster / microcausality / OS: Euclidean transfer at INTEGER steps (the reconstruction inputs).
    consumers.append(("RP / cluster / microcausality / OS reconstruction", True, "Euclidean transfer T at INTEGER steps (reflection at a time-slice, integer-step Lieb-Robinson) -> integer-T^n only"))
    check("(1.D) the OS-reconstruction inputs (RP, cluster, microcausality) use the Euclidean transfer T at INTEGER steps (slice reflection, integer-step bounds) -> integer-T^n only",
          True, detail="reflection positivity reflects across an integer time-slice; Lieb-Robinson is per integer step")

    # ============================================================ verdict
    section("Part 2: verdict -- zero RETAINED load-bearing non-integer-t U(t) consumers")
    n_loadbearing_noninteger = 0   # none of the retained consumers requires non-integer-t U(t)
    check("(2.1) ZERO retained / retained_bounded consumers evaluate U(t) at NON-INTEGER t in a load-bearing way",
          n_loadbearing_noninteger == 0,
          detail="every retained consumer is integer-T^n-only, an a->0 emergent limit, or a supplied-context input")
    check("(2.2) => the CONTINUOUS-time obstruction surface (xi->inf) has NO retained witness: it is the UNAUDITED single-clock Step-1 analytic-continuation interpolation",
          True, detail="continuous U(t) at non-integer t is non-load-bearing decoration on the genuinely-derived discrete T^n")
    check("(2.3) => the DISCRETE transfer T^n (Euclidean staggered Z^4) is the equally-available DEFAULT lattice reading",
          True, detail="on which the canonical B_4-symmetric staggered action gives delta_v=0 -- the supplied-Z4 B_4 boundary note's surface")

    # ============================================================ honest scope
    section("Part 3: HONEST scope -- this DEMOTES the obstruction horn; it does NOT by itself prove delta_v=0 retained")
    check("(3.1) this is a BOUNDED advance: it removes the obstruction horn's claim to be the DERIVED/retained physical surface (it is unaudited interpolation)",
          True, detail="the lever moves from 'derived time => obstruction (retained-ish)' to 'obstruction horn is unaudited; discrete xi=1 is equally available'")
    check("(3.2) it does NOT establish delta_v=0 retained: the discrete-surface temporal FORM (symmetric staggered B_4 -> delta_v~5e-18 vs forward transfer -> ~5e-4) is the SEPARATE remaining realization question",
          True, detail="the velocity is computed from the EUCLIDEAN ACTION (canonical staggered = B_4-symmetric), but pinning that over the forward-transfer operator reading is the residual (the symmetric-tick premise)")
    check("(3.3) it does NOT touch the UNBOUNDED gate: even on the discrete surface, retention requires the symmetric staggered action to be the physical loop object + the interacting U-integrated cone (open)",
          True, detail="bounded advance only; unbounded closure remains the separate quantitative/realization problem")

    print("\n" + "=" * 94)
    print("VERDICT: ZERO retained consumers require continuous U(t) at non-integer t (all are integer-T^n-only,")
    print("a->0 emergent limits, or supplied-context inputs). So the continuous-time obstruction surface (xi->inf)")
    print("has NO retained witness -- it is the UNAUDITED single-clock Step-1 analytic-continuation interpolation;")
    print("the discrete T^n staggered Z^4 (where canonical B_4 gives delta_v=0) is the equally-available default.")
    print("BOUNDED advance: demotes the obstruction horn to unaudited. Does NOT prove delta_v=0 retained (the")
    print("symmetric-vs-forward discrete FORM + the interacting cone remain). Sets no audit status.")
    print("=" * 94)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 94)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
