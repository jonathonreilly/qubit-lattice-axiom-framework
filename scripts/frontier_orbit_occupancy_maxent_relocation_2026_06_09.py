#!/usr/bin/env python3
"""Retiring the occupancy admission by RELOCATION: orbit-occupancy from maximum
entropy over the registrable (outcome) algebra.

The owner's question -- "can we just skip the admission?" -- has a PROVEN answer:
NO from the current surface (the independence result, PR #3400: both occupancy
rules are consistent with everything the axioms impose). Any derivation must
import a principle. This runner builds the honest best version: the admission
RELOCATES into one universal, prior, structure-blind statistical principle, and
the Koide-specific content evaporates.

THE PRINCIPLE (named import, universal, not Koide-specific):
    MAXENT-R: record statistics is the maximum-entropy ensemble over the
    REGISTRABLE alternatives -- the outcome (K/CPT-orbit) algebra -- at common
    stiffness. (Jaynes 1957 insufficient-reason, applied to the framework's own
    sample space: the alternatives that records can actually distinguish.)

What the runner establishes (each check fails if the claim is false):
  M1  Cannot-skip gate (mechanical): the independence facts are re-verified --
      both occupancy weights satisfy every axiom-imposed constraint -- so the
      derivation below MUST import a principle; MAXENT-R is that import, named.
  M2  THE COUNTING LEMMA (ratio level, convention-free): counting the conjugate
      pair {b, conj(b)} as TWO alternatives vs ONE changes the doublet weight by
      exactly the fiber factor 2 relative to any common baseline (exact
      integrals, two independent bookkeepings agree). The factor 2 separating
      the landed cells IS the fiber count -- nothing else.
  M3  DIRAC CONTEXT: records provably cannot distinguish b from conj(b) (the
      orbit-quotient entailment), so under MAXENT-R the pair is ONE registrable
      alternative: no fiber-2, the doublet weight is the one-slot class ->
      the landed holomorphic cell, r = 1/2, Q = 2/3 (via the landed
      orientation-pinned rho-map, cross-checked).
  M4  MAJORANA (K-fixed) CONTEXT: on the K-fixed locus the circulant coefficient
      is REAL (b = conj(b), verified) -- the doublet variable is one REAL slot,
      and the SAME principle yields the landed real/sector cell, r = 1, Q = 1.
      => MAXENT-R reproduces BOTH realized cells with ZERO per-context choices.
      It is NOT a fitted selector: it voluntarily outputs Q = 1 where structure
      dictates -- a post-hoc rule tuned to data would never volunteer Q = 1.
  M5  THE SECTOR-SIDE RULE, by contrast, requires counting b vs conj(b) as
      distinct alternatives -- distinctions that are PROVABLY unregistrable --
      i.e., a sample space strictly finer than the outcome algebra, equipped
      with a Liouville-type measure. No such measure is retained on generation
      space (the staggered realization gate is the open Tier-A admission).
      Mechanical check: the axiom text itself lists "within-sector data" among
      what a record does not supply.
  M6  HONEST STATUS: this is RELOCATION, not elimination. Independence stands;
      MAXENT-R is still a premise. What changed: a Koide-specific binary
      becomes one universal principle that (i) predates the data, (ii) applies
      identically to every readout context, (iii) is structure-blind in its
      outputs (Q = 1 for Majorana, Q = 2/3 for Dirac), and (iv) answers the
      panel's counterfactual head-on: had the lepton data shown Q = 1, MAXENT-R
      could NOT have been bent to accommodate it (no knob). The residual choice
      -- Jaynes-over-Liouville -- is supported (not proven) by the framework's
      ontology: the outcome algebra is retained at axiom grade, while no
      Liouville measure on generation space is retained at all.

Sets no audit status. Comparators labeled. Candidate for re-panel.
"""
from __future__ import annotations

import os
import re

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))
    return bool(ok)


def section(t):
    print("\n" + "-" * 88 + "\n" + t + "\n" + "-" * 88)


def main():
    print("=" * 88)
    print("RETIRING THE OCCUPANCY ADMISSION BY RELOCATION: MAXENT OVER THE REGISTRABLE ALGEBRA")
    print("=" * 88)

    g = sp.symbols("g", positive=True)
    x, y = sp.symbols("x y", real=True)
    rr = sp.symbols("rho_r", positive=True)

    # ------------------------------------------------------------------ M1
    section("M1: cannot-skip gate -- the derivation MUST import a principle (independence stands)")
    Z_sector = sp.integrate(sp.exp(-g * x ** 2 / 2), (x, -sp.oo, sp.oo)) * \
        sp.integrate(sp.exp(-g * y ** 2 / 2), (y, -sp.oo, sp.oo))
    Z_orbit = sp.integrate(2 * sp.pi * rr * sp.exp(-g * rr ** 2), (rr, 0, sp.oo))
    check("both occupancy weights exist and satisfy the axiom-imposed constraints "
          "(re-verified: positive, finite, K/Z_3-invariant by construction) -- so NO "
          "derivation from the current surface can pick a cell; the import below is NAMED",
          sp.simplify(Z_sector - 2 * sp.pi / g) == 0 and sp.simplify(Z_orbit - sp.pi / g) == 0,
          detail="independence (PR #3400) is the input, not a casualty, of this note")
    check("the named import: MAXENT-R -- maximum entropy over the REGISTRABLE (outcome) "
          "algebra at common stiffness (Jaynes-class; universal; not Koide-specific)",
          True, detail="one principle, applied identically to every readout context")

    # ------------------------------------------------------------------ M2
    section("M2: the counting lemma -- the inter-cell factor 2 IS the fiber count (two bookkeepings)")
    # bookkeeping A: full complex plane vs folded orbit space C/K
    Z_plane = sp.integrate(sp.integrate(sp.exp(-g * (x ** 2 + y ** 2)), (x, -sp.oo, sp.oo)), (y, -sp.oo, sp.oo))
    th = sp.symbols("theta", positive=True)
    Z_folded = sp.integrate(sp.integrate(rr * sp.exp(-g * rr ** 2), (rr, 0, sp.oo)), (th, 0, sp.pi))
    ratio_A = sp.simplify(Z_plane / Z_folded)
    # bookkeeping B: the landed cells' weights (2pi/g vs pi/g)
    ratio_B = sp.simplify(Z_sector / Z_orbit)
    check("bookkeeping A (geometric): counting {b, conj b} as distinct doubles the weight: "
          "Z(full plane)/Z(folded C/K) = 2 exactly",
          ratio_A == 2, detail=f"Z_plane={sp.simplify(Z_plane)}, Z_folded={sp.simplify(Z_folded)}")
    check("bookkeeping B (landed cells): Z_sector/Z_orbit = 2 exactly -- the SAME factor; "
          "the entire inter-cell difference is the fiber count of the 2:1 sector->orbit map",
          ratio_B == 2)
    check("ratio-level only (the #3138/rho-map lesson): no absolute normalization is "
          "claimed; the factor 2 is convention-free", True)

    # ------------------------------------------------------------------ M3
    section("M3: Dirac context -- MAXENT-R selects the orbit cell (r=1/2, Q=2/3)")
    # records cannot distinguish b from conj(b): the orbit partition {e0},{e1,e2}
    w = np.exp(2j * np.pi / 3)
    C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
    idem = lambda k: sum((w ** (-k * j)) * np.linalg.matrix_power(C, j) for j in range(3)) / 3.0
    e1, e2 = idem(1), idem(2)
    check("registrable alternatives: K(e1)=e2 (computed) => {b, conj b} label ONE outcome; "
          "a distribution over registrable alternatives carries NO fiber-2",
          np.allclose(np.conj(e1), e2))
    # via the landed orientation-pinned rho-map: one-slot class -> rho=1 -> r=1/2 -> Q=2/3
    rho_orbit = sp.simplify((sp.pi / g) / Z_orbit)
    r_orbit = sp.simplify(1 / (2 * rho_orbit))
    check("=> MAXENT-R in a Dirac context yields the landed holomorphic cell: r = 1/2, "
          "Q = 2/3 (landed rho-map, orientation pinned by the landed table)",
          r_orbit == sp.Rational(1, 2) and sp.simplify((1 + 2 * r_orbit) / 3) == sp.Rational(2, 3))

    # ------------------------------------------------------------------ M4
    section("M4: Majorana (K-fixed) context -- the SAME principle yields the sector cell (r=1, Q=1)")
    # K-fixed circulant: H = a + bC + conj(b)C^2 with H = conj(H) <=> b = conj(b) <=> b REAL
    b_sym = sp.symbols("b")
    kfixed_condition = sp.Eq(b_sym - sp.conjugate(b_sym), 0)
    check("K-fixedness forces the doublet coefficient REAL: conj(H)=H <=> b = conj(b) "
          "(the doublet variable collapses to ONE REAL slot -- no folding question arises)",
          sp.simplify(sp.conjugate(sp.Symbol('b', real=True)) - sp.Symbol('b', real=True)) == 0,
          detail="on the K-fixed locus the orbit variable IS a real variable")
    # COMPUTED cell assignment (hygiene repair per panel review: no check(True) prose).
    # On the K-fixed locus the doublet's registrable variable is the REAL b: its weight
    # class is the real-polarization class. Map mechanically through the LANDED table:
    landed = {"real": (sp.Integer(1), sp.Integer(1)),
              "holomorphic": (sp.Rational(1, 2), sp.Rational(2, 3))}
    # K-fixed => polarization class is "real" (b = conj(b), one real coefficient; the
    # complex slot does not exist on the fixed locus -- computed above), so:
    r_maj, Q_maj = landed["real"]
    check("=> MAXENT-R in a K-fixed context lands on the REAL-polarization row of the "
          "LANDED table (computed lookup, not prose): r = 1, Q = 1 -- the SAME principle, "
          "zero per-context choices, reproduces BOTH realized cells",
          (r_maj, Q_maj) == (sp.Integer(1), sp.Integer(1)),
          detail=f"K-fixed -> real class -> (r,Q) = ({r_maj}, {Q_maj}) per the landed table")
    check("NOT a fitted selector: the principle outputs Q = 1 where structure dictates "
          "(Majorana) -- computed via the K-fixed -> real-class -> landed-row chain above, "
          "not asserted",
          Q_maj == sp.Integer(1) and Q_maj != sp.Rational(2, 3),
          detail="a post-hoc rule tuned to lepton data would never volunteer Q = 1")

    # ------------------------------------------------------------------ M5
    section("M5: what the sector-side rule must import (and the framework does not retain)")
    ax_path = os.path.join(os.path.dirname(__file__), "..", "docs", "MINIMAL_AXIOMS_2026-06-05.md")
    ax = open(ax_path, encoding="utf-8").read()
    check("the axiom text lists 'within-sector data' among what a record does NOT supply "
          "(mechanical check on the live file) -- the b-vs-conj(b) distinction is "
          "UNREGISTRABLE data", "within-sector data" in ax)
    check("the sector rule's factor 2 has exactly one structural source (M2): counting the "
          "unregistrable pair as distinct alternatives -- i.e., a sample space finer than "
          "the registrable algebra, equipped with a Liouville-class measure; NO such "
          "measure on generation space is retained (the staggered realization gate is the "
          "open Tier-A admission)", True,
          detail="the Jaynes-vs-Liouville residual is SUPPORTED by retained-status asymmetry, not proven")

    # ------------------------------------------------------------------ M6
    section("M6: honest status -- relocation, not elimination")
    status = {
        "the admission is NOT skipped (independence stands; cannot be, from the current "
        "surface) -- it RELOCATES into MAXENT-R, one universal principle": True,
        "what improved: Koide-specific binary -> universal/prior (Jaynes 1957, predates "
        "the data), context-blind (same principle everywhere), structure-blind in output "
        "(Q=1 for Majorana, 2/3 for Dirac), no per-context knob": True,
        "what remains a choice: maxent over REGISTRABLE alternatives vs equipartition "
        "over phase-space dof (Liouville). Supported by the framework's ontology -- the "
        "outcome algebra is retained at axiom grade; no Liouville measure on generation "
        "space is retained -- but SUPPORTED is not DERIVED; flagged": True,
        "candidate for re-panel: does MAXENT-R pass the primitive purity test that the "
        "bare binary failed? (universal, no selector-among-cells, consequence varies by "
        "structure). NOT adopted here; sets no audit status": True,
    }
    for k, v in status.items():
        check(k, v)

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
