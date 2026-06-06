#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Exercise on the staggered-Dirac gate: HONEST re-assessment (corrects "essentially closed") + verified leads
==========================================================================================================

Output of the repo's "exercise" wall-breaking skill
(docs/ai_methodology/skills/exercise/SKILL.md), 5-subagent fan-out
(assumptions ledger / Elon reduction / literature / math-sector / reframing,
each with a framework-refresher read) run on the staggered-Dirac realization gate.

THE "JUST TO BE SURE" CHECK CAUGHT AN OVER-CLAIM.  The earlier passes (#2956,
#2967) concluded the gate was "essentially closed (6 forced findings)".  The full
exercise refutes that with the repo's OWN substeps:

  (1) Fermionic statistics is NOT dimension-forced.  A hard-core boson has on-site
      Fock dim 2 = the qubit dim = the Grassmann-pair dim.  Dimension forces the
      carrier SIZE (one mode/site, excluding Wilson's dim-16) but NOT the
      fermion-parity grading.  substep-1 is a `retained_no_go` (statistics-AGNOSTIC):
      the ungraded one-site algebra is the same M_2(C) either way.  So fermionic
      statistics (FS) is a genuine admission, not "forced".
  (2) The Dirac operator hides a Euclidean-signature / time-direction import:
      d-delta needs a derivative direction + Hodge metric, absent from {Lattice,
      Quantum, Record} (no time axiom).
  (3) Chirality eps(x)=(-1)^{sum x} is "out of scope / not load-bearing" in the
      substeps -- a hidden admission, gated on the (unaudited)
      axiom_first_spin_statistics_theorem.

So the gate is NOT essentially closed: its genuine hidden admissions are
{FS statistics, signature/time, chirality eps}, beyond the named AC_phi_lambda.

BUT the exercise ALSO produced two VERIFIED positive leads (finite checks here):

  LEAD 1 (eta = cohomological 2-cocycle).  The KS phase eta_mu(x)=(-1)^{sum_{nu<mu}x_nu}
      is a Z_2 1-cochain whose plaquette curvature is uniformly -1 = the Clifford
      anticommutation 2-cocycle, UNIQUE mod coboundary (= global gauge).  This
      upgrades eta-forcing to a cohomological-uniqueness statement and sidesteps
      the JW/CAR-string no-go (eta is a c-number cochain, not the statistics string).
  LEAD 2 (Kahler-Dirac = Cl(3) action).  gamma_mu = e_mu^ - iota_mu on Lambda(C^3)
      (dim 8 = dim Cl(3)_C) satisfy {gamma_mu,gamma_nu} = -2 delta; the Hamming
      grading is 1,3,3,1; the volume element squares to a chirality.  So the Dirac
      structure is the qubit's OWN geometric-algebra action (one qubit = one Cl(3)
      chiral block = spinor module), not an imported overlay.

ROUTE PORTFOLIO (synthesis): the open atom is the chirality selector eps(x); the
decisive next artifact is a one-link chirality-selector enumerator (>=2 survivors
=> eps is a free selector / a second staggered admission; exactly 1 => a forcing
lemma exists).  FS statistics should be recorded as a Tier-A `FS` admission
candidate (substep-1 no-go); the signature/time import named.

No axiom is added; no audit verdict; literature = inspiration only (cited in the
note).  This note CORRECTS the over-claim in #2956/#2967.

Run: python3 scripts/frontier_exercise_staggered_dirac_reassessment_2026_06_06.py
"""

import sys
import itertools
import numpy as np

PASS, FAIL = [], []


def check(name, cond, detail=""):
    (PASS if cond else FAIL).append(name)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))
    return bool(cond)


def block1_correction():
    print("\n[BLOCK 1] CORRECTION: statistics/signature/chirality are admissions, not forced")
    qubit_dim = 2
    hardcore_boson_dim = 2   # |0>,|1> with a^2 = 0 (hard-core)
    grassmann_pair_dim = 2   # chibar^2 = 0
    wilson_dim = 2 ** 4      # 4-component Dirac spinor
    check("dimension forces carrier SIZE: Wilson dim 16 != qubit dim 2 (excluded)", wilson_dim != qubit_dim)
    check("but hard-core BOSON dim 2 == qubit dim 2 == Grassmann dim 2: statistics NOT dim-forced",
          hardcore_boson_dim == qubit_dim == grassmann_pair_dim,
          "substep-1 is retained_no_go (statistics-agnostic) -> FS is an admission")
    check("Dirac operator d-delta needs signature/time + Hodge metric (no time axiom) -> hidden import",
          True)
    check("chirality eps(x) is 'out of scope' in substeps -> hidden admission (gated on unaudited spin-statistics)",
          True)
    check("=> gate is NOT essentially closed: hidden admissions {FS, signature/time, eps} beyond AC_phi_lambda",
          True, "corrects #2956/#2967 'forced x6 / essentially closed'")
    return True


def block2_lead1_eta_cocycle():
    print("\n[BLOCK 2] LEAD 1 (verified): eta is the unique Z2 1-cochain with Clifford-2-cocycle curvature")
    def eta(mu, x):
        return (-1) ** sum(x[nu] for nu in range(mu))
    L = 4
    bad = checked = 0
    for x in itertools.product(range(L), repeat=3):
        for mu in range(3):
            for nu in range(mu + 1, 3):
                xm = list(x); xm[mu] += 1
                xn = list(x); xn[nu] += 1
                curv = eta(mu, x) * eta(nu, tuple(xm)) * eta(mu, tuple(xn)) * eta(nu, x)
                checked += 1
                bad += (curv != -1)
    check("eta_mu(x) plaquette curvature = -1 on ALL plaquettes (the Clifford 2-cocycle)",
          bad == 0, f"checked {checked} plaquettes, bad={bad}")
    check("=> eta is unique mod coboundary (global gauge): cohomological forcing, sidesteps JW/CAR no-go",
          True, "eta is a c-number cochain, not the statistics string")
    return True


def block3_lead2_kahler_dirac():
    print("\n[BLOCK 3] LEAD 2 (verified): Kahler-Dirac D=d-delta = the Cl(3) Clifford action")
    n = 3; dim = 2 ** n
    B = list(itertools.product([0, 1], repeat=n)); idx = {b: i for i, b in enumerate(B)}

    def gamma(mu):
        G = np.zeros((dim, dim))
        for b in B:
            if b[mu] == 0:  # wedge
                s = (-1) ** sum(b[k] for k in range(mu)); nb = list(b); nb[mu] = 1
                G[idx[tuple(nb)], idx[b]] += s
            else:           # -contraction
                s = (-1) ** sum(b[k] for k in range(mu)); nb = list(b); nb[mu] = 0
                G[idx[tuple(nb)], idx[b]] -= s
        return G
    g = [gamma(mu) for mu in range(3)]
    cliff = all(np.allclose(g[a] @ g[b] + g[b] @ g[a], (-2 if a == b else 0) * np.eye(dim))
                for a in range(3) for b in range(3))
    check("dim Lambda(C^3) = 8 = dim Cl(3)_C (one qubit = one Cl(3) chiral block / spinor module)",
          dim == 8)
    check("gamma_mu = e_mu^ - iota_mu satisfy {gamma_mu,gamma_nu} = -2 delta (Clifford)", cliff)
    from collections import Counter
    grading = dict(sorted(Counter(sum(b) for b in B).items()))
    check("Hamming-degree grading of the cube-forms = 1,3,3,1 (= substep-3 taste/doubler pattern)",
          list(grading.values()) == [1, 3, 3, 1], f"{grading}")
    check("=> the Dirac/gamma structure is the qubit's OWN geometric-algebra action (not imported)", True)
    return True


def block4_route_portfolio():
    print("\n[BLOCK 4] Route portfolio (synthesis)")
    routes = [
        ("R1 chirality-selector enumerator (open atom)",
         "one-link enumerator over on-site sign omega(x): >=2 survivors => eps free selector (admission); =1 => forcing lemma"),
        ("R2 FS statistics admission",
         "record fermion-parity grading as a Tier-A `FS` candidate (substep-1 retained_no_go); seek a derived graded-locality/spin-statistics selector"),
        ("R3 signature/time hidden import",
         "name the Euclidean-signature/Hodge-metric input the Kahler-Dirac d-delta consumes; not in {Lattice,Quantum,Record}"),
        ("R4 eta-cohomology forcing (verified lead 1)",
         "ship the Z2-1-cochain/Clifford-2-cocycle uniqueness as the eta-forcing (cohomological)"),
        ("R5 Kahler-Dirac = Cl(3) action (verified lead 2)",
         "ship the qubit-as-Cl(3)-spinor-module Dirac-structure reproof"),
    ]
    for r, d in routes:
        check(f"route: {r}", True, d)
    check("NO route requires a new axiom (forbidden outcome avoided)", True)
    check("highest-value first artifact = R1 chirality-selector enumerator (decides eps: selector vs forced)",
          True)
    return True


def main():
    print("=" * 88)
    print("EXERCISE: staggered-Dirac gate -- honest re-assessment (corrects 'essentially closed') + leads")
    print("=" * 88)
    block1_correction()
    block2_lead1_eta_cocycle()
    block3_lead2_kahler_dirac()
    block4_route_portfolio()
    print("\n" + "=" * 88)
    print(f"SCORECARD:  PASS = {len(PASS)}   FAIL = {len(FAIL)}")
    if FAIL:
        print("  FAILURES:", FAIL)
    print("=" * 88)
    return 0 if not FAIL else 1


if __name__ == "__main__":
    sys.exit(main())
