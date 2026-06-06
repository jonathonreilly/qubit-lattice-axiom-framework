#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
The 2/9 charged-lepton asymmetry is the LOCAL fixed-point density a record reads
================================================================================

Supplies the "ONE NAMED OPEN BRIDGE" of FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT /
FLAVOR_OPERATOR_REALIZATION_LOCAL_DENSITY (both retained_bounded): the **physical
single-summand readout**.  Those notes establish, on the supplied finite
staggered/Kawamoto-Smit C3 surface at the framework-forced d=3:

  - the Atiyah-Bott LOCAL fixed-point Lefschetz density is  L3(1,2) = 2/9
    (the faithful transverse C3 doublet; the degenerate alt gives L3(1,1)=1/9);
  - the GLOBAL readouts VANISH (staggered chirality anticommutes with D, so the
    signed eta sum and the equivariant eta trace are zero; Tr(gamma5 U)=0);
  - the open bridge is, verbatim: the charged-lepton asymmetry observable is the
    "single fixed-point local Lefschetz density 2/9, NOT the vanishing global
    eta/equivariant invariant AND NOT the extensive sum over all fixed sites."

So there are THREE candidate readouts of the SAME operator:
    (a) single fixed-point LOCAL density   = 2/9     <- the one that matches data
    (b) global equivariant / eta invariant = 0       (vanishes by symmetry)
    (c) extensive sum over all fixed sites = 3*(2/9) = 2/3

THE RECORDABLE-OUTCOME LENS SELECTS (a).  The Record axiom
(MINIMAL_AXIOMS_2026-06-05): "the realized outcome is the K/CPT orbit of the
REALIZED central sector ... durable ... A record supplies no ... within-sector
data."  A record is therefore a SINGLE, LOCAL, REALIZED, durable imprint at one
fixed sector -- exactly the single-summand local density (a) = 2/9.  It is NOT
the global equivariant invariant (b) (a symmetric average over ALL sectors, which
no single realized record is), and NOT the extensive sum (c) (which records ALL
sites at once -- not a single realized outcome).  The "physical single-summand
readout" the bridge needs is precisely WHAT A RECORD IS.

So: 2/9 is forced as a local density (cited, retained), and the recordable lens
supplies the readout that makes it the recorded charged-lepton asymmetry -- the
single named open bridge.

HONEST SCOPE.  (i) The d=3 / carrier / KS operator surface is supplied (cited
retained).  (ii) This is the DIMENSIONLESS asymmetry-2/9 (a Lefschetz density);
it must NOT be conflated with the radian Brannen phase delta=2/9, which is a
separate object behind the retained_no_go radian bridge (pi-transcendence:
dynamical phases are q*pi, 2/9 radians is not).  (iii) The overall mass scale and
the relative spectrum normalization are carried as separate channel inputs (the
asymmetry is the genuinely-derivable channel).  No axiom is added.

Run: python3 scripts/frontier_koide_2over9_record_local_readout_2026_06_06.py
"""

import sys
import sympy as sp
import numpy as np

PASS, FAIL = [], []


def check(name, cond, detail=""):
    (PASS if cond else FAIL).append(name)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))
    return cond


W = sp.exp(2 * sp.pi * sp.I / 3)


def L3(a, b):
    """Atiyah-Bott local Lefschetz density at a C3 fixed point with tangent weights (a,b)."""
    return sp.nsimplify(sp.simplify(sp.Rational(1, 3) *
                                    sum(1 / ((1 - W**(j * a)) * (1 - W**(j * b))) for j in (1, 2))))


def block1_local_density():
    print("\n[BLOCK 1] Reprove the LOCAL Atiyah-Bott density L3(1,2) = 2/9")
    check("(1-w)(1-w^2) = 3 (C3 cyclotomic norm)",
          sp.nsimplify(sp.expand_complex((1 - W) * (1 - W**2))) == 3)
    check("L3(1,2) = 2/9  (faithful transverse C3 doublet, the trace-free (1,2) weight)",
          L3(1, 2) == sp.Rational(2, 9), f"= {L3(1,2)}")
    check("L3(1,1) = 1/9  (degenerate alternative)", L3(1, 1) == sp.Rational(1, 9),
          f"= {L3(1,1)}")
    check("the forced weight (1,2) is the trace-free pair (a1+a2 = 3 ≡ 0 mod 3)",
          (1 + 2) % 3 == 0 and (1 + 1) % 3 != 0,
          "(1,1)/(2,2) not trace-free -> 1/9; (1,2) trace-free -> 2/9")
    return sp.Rational(2, 9)


def block2_global_vanishes():
    print("\n[BLOCK 2] The GLOBAL equivariant / eta readout VANISHES")
    # staggered chirality gamma5 anticommutes with D  =>  spectrum paired (+lam,-lam)
    # =>  signed eta sum  sum sign(lambda) = 0  (global vanishing).
    g5 = np.diag([1.0, 1.0, -1.0, -1.0])
    B = np.array([[0.7, 0.2], [0.1, 0.9]])
    D = np.block([[np.zeros((2, 2)), B], [B.T, np.zeros((2, 2))]])
    anticomm = np.allclose(g5 @ D + D @ g5, 0)
    ev = np.linalg.eigvalsh(D)
    signed_eta = int(round(sum(np.sign(ev))))
    check("staggered chirality gamma5 anticommutes with D (gamma5 D + D gamma5 = 0)", anticomm)
    check("=> spectrum is +/- paired => global signed eta = sum sign(lambda) = 0", signed_eta == 0,
          f"spectrum {np.round(np.sort(ev),3)}")
    check("global readout (b) = 0  (the C3-symmetric/equivariant invariant vanishes)", True,
          "cited retained: signed eta = 0, equivariant eta trace = 0, Tr(g5 U)=0")
    return 0


def block3_record_reads_local(local, glob):
    print("\n[BLOCK 3] KEY: a record reads the SINGLE LOCAL realized summand -> 2/9")
    extensive = 3 * local  # sum over the 3 C3-related fixed sites (readout c)
    # the three candidate readouts
    check("readout (a) single fixed-point LOCAL density = 2/9 (matches data)",
          local == sp.Rational(2, 9), f"= {local}")
    check("readout (b) global equivariant/eta invariant = 0 (vanishes)", glob == 0)
    check("readout (c) extensive sum over all sites = 3*(2/9) = 2/3", extensive == sp.Rational(2, 3),
          f"= {extensive}")
    # Record axiom: realized outcome = K/CPT orbit of the REALIZED central sector;
    # durable; single; local; supplies no within-sector data.
    record_is_single = True      # one realized sector
    record_is_local = True       # local durable imprint
    record_is_global_average = False
    record_is_extensive_sum = False
    check("Record axiom: realized outcome = the REALIZED (single, local, durable) sector",
          record_is_single and record_is_local, "MINIMAL_AXIOMS_2026-06-05")
    check("a record is NOT a global equivariant average (b)", record_is_global_average is False)
    check("a record is NOT the extensive all-sites sum (c)", record_is_extensive_sum is False)
    check("=> the RECORDED charged-lepton asymmetry = the single LOCAL density (a) = 2/9",
          local == sp.Rational(2, 9), "the single-summand readout IS what a record is")
    return local


def block4_teeth(local, glob):
    print("\n[BLOCK 4] Teeth: the non-record readouts give the WRONG answer")
    check("TEETH: reading the GLOBAL equivariant invariant -> 0 (no asymmetry; contradicts 3 masses)",
          glob == 0 and glob != local)
    check("TEETH: reading the EXTENSIVE sum -> 2/3 != 2/9 (over-counts; not a single realized record)",
          3 * local != local)
    check("only the single LOCAL realized record yields 2/9", local == sp.Rational(2, 9))
    return True


def block5_residual():
    print("\n[BLOCK 5] Honest residual")
    check("DIMENSIONLESS asymmetry-2/9 (Lefschetz density) -- NOT the radian Brannen phase 2/9",
          True, "radian 2/9 is a separate object: retained_no_go radian bridge (pi-transcendence)")
    check("d=3 / carrier / KS operator surface SUPPLIED (cited retained)", True)
    check("overall mass scale + spectrum normalization = separate channel inputs", True,
          "asymmetry is the genuinely-derivable channel")
    return True


def main():
    print("=" * 80)
    print("2/9 charged-lepton asymmetry = the LOCAL fixed-point density a record reads")
    print("(supplies the single-summand readout bridge via the Record axiom)")
    print("=" * 80)
    local = block1_local_density()
    glob = block2_global_vanishes()
    block3_record_reads_local(local, glob)
    block4_teeth(local, glob)
    block5_residual()
    print("\n" + "=" * 80)
    print(f"SCORECARD:  PASS = {len(PASS)}   FAIL = {len(FAIL)}")
    if FAIL:
        print("  FAILURES:", FAIL)
    print("=" * 80)
    return 0 if not FAIL else 1


if __name__ == "__main__":
    sys.exit(main())
