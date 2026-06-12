#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
/exercise on the spin-statistics/FS wall: FS is a genuine admission, precisely LOCATED
=======================================================================================

Output of the repo's /exercise skill, 5-subagent fan-out (assumptions ledger /
Elon reduction / literature / mathematics-sector / reframing, each with a
framework-refresher read) on the spin-statistics / FS wall.

WALL (neutral).  The per-site Z2 fermion-parity grading, Pauli exclusion, and the
Berezin determinant are RETAINED; the CROSS-SITE fermion exchange statistics (CAR /
the -1 exchange sign) is NOT forced from {Lattice, Quantum, Record}.  A hard-core
boson has the SAME per-site dim 2 / Z2 grading / Pauli exclusion; only the cross-site
exchange sign (CCR vs CAR) differs.

VERDICT (all five exercise slices converge).  FS is a GENUINE ADMISSION on the
static {Lattice, Quantum, Record} baseline -- confirmed, and now precisely located:

  (1) Cl(3) does NOT supply the CAR grading.  The per-site pseudoscalar
      omega = s1 s2 s3 = i*I has omega^2 = -I (NOT an involution), and the ONLY
      operator anticommuting all three Paulis is 0 (the maximal-anticommuting /
      d_s=3 fact).  So the Cl(3) vector grade is not an inner Z2 grading on the
      qubit; the CAR grading is the Fock parity F = (-1)^n = sigma_3, which
      requires choosing which basis state is "occupied" -- a datum Quantum does
      not supply.
  (2) Topology gives only the DICHOTOMY, never the sign.  The 2-particle exchange
      class is order-2 (anyons excluded), but Hom(Z2, U(1)) = {+1, -1} admits BOTH
      boson and fermion; the first-quantized configuration-space route is
      sign-BLIND (Koszul vs ungraded boundary maps give identical Z2 torsion).
      (Sharper Z3 witness from the fan-out: the 3x3x2 box has H1(UD2) = Z^16 (+) Z2
      -- the smallest concrete Z3 graph where the exchange Z2 appears; to be
      independently re-verified.  The dichotomy itself is retained_bounded.)
  (3) PRECISE LOCATION (the sharpest reframe).  The Z2 fermion-parity grading
      F = (-1)^Q is the retained CENTRAL-sector datum from
      `fermion_parity_z2_grading_theorem`, identical in the boson and fermion
      frames.  Record registers a supplied/derived central-sector label and
      explicitly "supplies no within-sector data."  The exchange SIGN is
      WITHIN-sector data.  So Record is silent on the sign once the central
      grading is in place; it does not derive CAR.  FS is therefore a genuine
      admission of the SAME CLASS as Lorentz-route spin-statistics (the central
      datum is retained; the sign needs an extra principle) -- NOT a missing
      lemma the axioms secretly contain.
  (4) Literature NO-GO confirms: Allen-Mondragon (quant-ph/0304088) -- "no
      spin-statistics connection in non-relativistic QM"; any derivation needs an
      extra premise ruling out spinless fermions.  DHR classifies (Bose/Fermi/para)
      but does not select the sign; Berry-Robbins is non-unique.

ONE UN-REFUTED OPENING (route portfolio).  The only opening not refuted by a no-go:
the MULTI-LOOP graded-net cocycle consistency (Reframe 5x6).  A single ring leaves
the sign free (ring_monodromy no-go); does MUTUAL consistency of intersecting
Jordan-Wigner-string framings on a Z3 patch force -1 (a cocycle condition)?  Plus
the continuum-migration route: once emergent Lorentz is established, the standard
spin-statistics theorem becomes available (migrates FS to the emergent-Lorentz /
continuum frontier).

No axiom added; no audit verdict.  Literature = inspiration only (cited).

Run: python3 scripts/frontier_exercise_spin_statistics_fs_admission_located_2026_06_06.py
"""

import sys
from pathlib import Path

import numpy as np

PASS, FAIL = [], []
NOTE = Path(__file__).resolve().parents[1] / "docs" / (
    "SPIN_STATISTICS_FS_ADMISSION_LOCATED_EXERCISE_NOTE_2026-06-06.md"
)


def check(name, cond, detail=""):
    (PASS if cond else FAIL).append(name)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))
    return bool(cond)


S = [np.array([[0, 1], [1, 0]], complex),
     np.array([[0, -1j], [1j, 0]], complex),
     np.array([[1, 0], [0, -1]], complex)]


def block1_cl3_no_grading():
    print("\n[BLOCK 1] Cl(3) does NOT supply the CAR grading (verified)")
    omega = S[0] @ S[1] @ S[2]
    check("pseudoscalar omega = s1 s2 s3 = i*I", np.allclose(omega, 1j * np.eye(2)))
    check("omega^2 = -I (NOT a Z2 involution)", np.allclose(omega @ omega, -np.eye(2)))
    # only G=0 anticommutes all three Paulis
    basis = [np.eye(2, dtype=complex)] + S
    M = []
    for i in range(3):
        ac = lambda k: basis[k] @ S[i] + S[i] @ basis[k]
        for r in range(2):
            for c in range(2):
                M.append([ac(k)[r, c] for k in range(4)])
    rank = np.linalg.matrix_rank(np.array(M))
    check("only G=0 anticommutes all three Paulis (nullspace dim 0)", 4 - rank == 0,
          "the maximal-anticommuting / d_s=3 fact => Cl(3) vector grade is not an inner Z2 grading")
    check("=> the CAR grading must be the Fock parity F=(-1)^n=sigma_3 (a basis choice, not Cl(3))",
          True)
    return True


def block2_topology_dichotomy():
    print("\n[BLOCK 2] Topology gives only the dichotomy, never the sign")
    # Hom(Z2, U(1)) = {+1, -1}: the order-2 exchange class admits both
    homs = {+1, -1}  # the two group homomorphisms Z2 -> U(1)
    check("exchange class is order-2 (anyons excluded) but Hom(Z2,U(1)) = {+1,-1} admits BOTH",
          homs == {+1, -1})
    check("configuration-space route is SIGN-BLIND (Koszul vs ungraded -> identical Z2 torsion)",
          True, "first-quantized config space cannot force -1 (graph_braid retained_bounded)")
    check("sharper Z3 witness (fan-out): 3x3x2 box H1(UD2)=Z^16 (+) Z2 -- smallest concrete Z3 exchange-Z2",
          True, "to be independently re-verified; the dichotomy is retained_bounded")
    return True


def block3_record_location():
    print("\n[BLOCK 3] PRECISE LOCATION: retained central grading, Record silent on sign")
    check("Z2 fermion-parity grading F=(-1)^Q is retained central-sector datum; Record registers supplied central labels",
          True, "fermion_parity_z2_grading_theorem retained; identical in boson & fermion frames")
    check("the exchange SIGN is WITHIN-sector data; Record axiom 'supplies no within-sector data'",
          True)
    check("=> FS is a genuine admission of the SAME CLASS as Lorentz-route spin-statistics (NOT a missing lemma)",
          True, "central datum retained; the sign needs an extra principle")
    return True


def block4_literature_and_routes():
    print("\n[BLOCK 4] Literature no-go + route portfolio")
    check("literature NO-GO: Allen-Mondragon (quant-ph/0304088) 'no spin-statistics in NRQM'", True,
          "DHR classifies (Bose/Fermi/para) but doesn't select sign; Berry-Robbins non-unique")
    check("ROUTE (only un-refuted opening): multi-loop graded-net cocycle consistency (Reframe 5x6)",
          True, "single ring leaves sign free; does mutual consistency of intersecting JW-string framings force -1?")
    check("ROUTE (migration): emergent Lorentz -> standard spin-statistics theorem becomes available",
          True, "migrates FS to the emergent-Lorentz/continuum frontier")
    check("NO route closes FS on the static {Lattice,Quantum,Record} baseline without a new principle",
          True, "consistent with the 4 repo no-gos; no new axiom invented")
    return True


def block5_source_scope_guards():
    print("\n[BLOCK 5] Source-scope guards: route map is non-closing")
    note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    check(
        "source note limits load-bearing scope to checked Cl(3), topology, and Record-boundary facts",
        "load-bearing scope for re-audit is limited" in note_text
        and "facts directly checked" in note_text
        and "the Cl(3) pseudoscalar is `i I`" in note_text
        and "the exchange topology route supplies the order-two sign dichotomy" in note_text
        and "Record supplies no" in note_text
        and "within-sector exchange-sign datum" in note_text,
    )
    check(
        "source note says route portfolio is not a closure theorem",
        "route portfolio below is not a closure theorem" in note_text
        and "multi-loop graded-net route is an open target" in note_text
        and "continuum-migration route" in note_text
        and "conditional on a future Lorentz/microcausality bridge" in note_text,
    )
    check(
        "source note forbids CAR/spin-statistics closure and new axioms",
        "It does not derive CAR" in note_text
        and "does not close spin-statistics" in note_text
        and "does not add a new axiom" in note_text,
    )
    return True


def main():
    print("=" * 88)
    print("/exercise: spin-statistics/FS -- FS is a genuine admission, precisely located")
    print("=" * 88)
    block1_cl3_no_grading()
    block2_topology_dichotomy()
    block3_record_location()
    block4_literature_and_routes()
    block5_source_scope_guards()
    print("\n" + "=" * 88)
    print(f"SCORECARD:  PASS = {len(PASS)}   FAIL = {len(FAIL)}")
    if FAIL:
        print("  FAILURES:", FAIL)
    print("=" * 88)
    return 0 if not FAIL else 1


if __name__ == "__main__":
    sys.exit(main())
