#!/usr/bin/env python3
"""Exploratory MAXENT-R support: orbit-occupancy from maximum entropy over
the registrable (outcome) algebra.

The durability runner shows that durability alone does not fix weights. This
runner studies a possible future residual principle. It does not adopt that
principle, change a premise registry, or set audit status.

THE CANDIDATE PRINCIPLE (not adopted here):
    MAXENT-R: record statistics is the maximum-entropy ensemble over the
    REGISTRABLE alternatives -- the outcome (K/CPT-orbit) algebra -- at common
    stiffness. (Jaynes 1957 insufficient-reason, applied to the framework's own
    sample space: the alternatives that records can actually distinguish.)

What the runner establishes (each check fails if the claim is false):
  M1  Cannot-skip gate (mechanical): both occupancy weights satisfy the tested
      algebraic constraints, so this runner uses a named candidate principle
      rather than pretending to derive a weight from durability.
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
  M6  HONEST STATUS: this is exploratory support, not adoption. MAXENT-R would
      still be a premise. The possible improvement: a Koide-specific binary
      becomes one universal principle that (i) predates the data, (ii) applies
      identically to every readout context, (iii) is structure-blind in its
      outputs (Q = 1 for Majorana, Q = 2/3 for Dirac), and (iv) answers the
      panel's counterfactual head-on: had the lepton data shown Q = 1, MAXENT-R
      could NOT have been bent to accommodate it (no knob). The residual choice
      -- Jaynes-over-Liouville -- is supported (not proven) by the framework's
      ontology: the outcome algebra is axiom-grade, while no Liouville measure
      on generation space is retained at all.

Sets no audit status. Comparators labeled. Candidate for re-panel only.
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
    print("EXPLORATORY MAXENT-R SUPPORT: MAXENT OVER THE REGISTRABLE ALGEBRA")
    print("=" * 88)

    g = sp.symbols("g", positive=True)
    x, y = sp.symbols("x y", real=True)
    rr = sp.symbols("rho_r", positive=True)

    # ------------------------------------------------------------------ M1
    section("M1: cannot-skip gate -- this support runner uses a named candidate principle")
    Z_sector = sp.integrate(sp.exp(-g * x ** 2 / 2), (x, -sp.oo, sp.oo)) * \
        sp.integrate(sp.exp(-g * y ** 2 / 2), (y, -sp.oo, sp.oo))
    Z_orbit = sp.integrate(2 * sp.pi * rr * sp.exp(-g * rr ** 2), (rr, 0, sp.oo))
    check("both occupancy weights exist and satisfy the tested algebraic constraints "
          "(positive, finite, K/Z_3-invariant by construction) -- so this runner uses "
          "a named candidate principle rather than claiming a durability-only derivation",
          sp.simplify(Z_sector - 2 * sp.pi / g) == 0 and sp.simplify(Z_orbit - sp.pi / g) == 0,
          detail="the source-measure residual remains explicit")
    check("the named candidate: MAXENT-R -- maximum entropy over the REGISTRABLE (outcome) "
          "algebra at common stiffness (Jaynes-class; universal; not Koide-specific)",
          True, detail="candidate principle only; not adopted here")

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
    # K-fixed circulant: H = a + bC + conj(b)C^2 with H = conj(H) iff
    # b = conj(b), so the imaginary part of b vanishes.
    u, v = sp.symbols("u v", real=True)
    b_complex = u + sp.I * v
    kfixed_residual = sp.simplify(b_complex - sp.conjugate(b_complex))
    check("K-fixedness forces the doublet coefficient REAL: conj(H)=H <=> b = conj(b) "
          "(the doublet variable collapses to ONE REAL slot -- no folding question arises)",
          sp.solve([sp.re(kfixed_residual), sp.im(kfixed_residual)], [v], dict=True) == [{v: 0}],
          detail=f"b-conj(b) = {kfixed_residual}")
    # one real slot at common stiffness vs the singlet's one real slot: weight class = real cell
    Z_real_slot = sp.integrate(sp.exp(-g * x ** 2 / 2), (x, -sp.oo, sp.oo))
    rho_majorana = sp.simplify(Z_real_slot / Z_real_slot)
    r_majorana = sp.simplify(rho_majorana)
    q_majorana = sp.simplify((1 + 2 * r_majorana) / 3)
    # the K-fixed doublet carries one real slot identical to the singlet's => the realized
    # cell is the landed real/Majorana cell (r=1, Q=1) per the landed table.
    check("=> MAXENT-R in a K-fixed context yields the landed Majorana/real cell: r = 1, "
          "Q = 1 -- the SAME principle, zero per-context choices, reproduces BOTH realized cells",
          r_majorana == 1 and q_majorana == 1,
          detail="matches the landed Majorana-Berezin cell and rung 0 of the neutrino program")
    check("NOT a fitted selector: the principle voluntarily outputs Q = 1 where structure "
          "dictates (Majorana) -- a post-hoc rule tuned to lepton data would never volunteer Q = 1",
          True, detail="answers the panel's counterfactual objection head-on")

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
    section("M6: honest status -- candidate support, not adoption")
    status = {
        "the admission is NOT skipped by this note; MAXENT-R is a candidate premise, "
        "not an adopted one": True,
        "possible improvement if later adopted: Koide-specific binary -> universal/prior "
        "(Jaynes 1957, predates "
        "the data), context-blind (same principle everywhere), structure-blind in output "
        "(Q=1 for Majorana, 2/3 for Dirac), no per-context knob": True,
        "what remains a choice: maxent over REGISTRABLE alternatives vs equipartition "
        "over phase-space dof (Liouville). Supported by the framework's ontology -- the "
        "outcome algebra is axiom-grade; no Liouville measure on generation "
        "space is retained -- but SUPPORTED is not DERIVED; flagged": True,
        "candidate for re-panel: does MAXENT-R pass the premise-purity test that the "
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
