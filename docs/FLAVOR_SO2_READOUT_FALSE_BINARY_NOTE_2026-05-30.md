# Flavor SO(2) Readout: Finite Determinant Algebra Scope Repair

**Date:** 2026-05-30
**Scope repair date:** 2026-06-04
**Claim type:** bounded_theorem
**Actual current surface status:** bounded-support
**Runner:** `scripts/flavor_so2_readout_false_binary_2026_05_30.py` (SCORECARD PASS=4).
**Audit repair target:** keep the supplied `C3` singlet/doublet algebra, but do not claim a global
framework exhaustiveness theorem for readout/measure normalizations.

## Narrow Claim

This packet proves only the finite algebra executed by the runner:

1. A continuous rephase `C -> exp(i alpha) C` is incompatible with `C^3=I` except at the three cube-root
   phases. The packet therefore verifies the stated obstruction to a continuous `U(1)_b` rephase of
   the chosen cyclic generator.
2. The phase `delta=arg(b)` moves the circulant spectrum, but the Koide trace ratio
   `sum(lambda_i^2)/(sum(lambda_i))^2` is independent of `delta` in the supplied family.
3. For `alpha P_s + beta P_d`, the real determinant gives `alpha beta^2`, while the stipulated
   singlet/doublet block-counting product gives `alpha beta`. These are two different countings of the
   supplied `1+2` decomposition.
4. The full degeneracy locus of the supplied circulant spectrum is `delta=m*pi/3`, not only
   `sin(delta)=0`.

These checks are useful bounded algebra. They do not prove that the framework exhausts all admissible
readout/measure normalizations, and they do not prove that no framework rule can select one of the two
countings.

## Out Of Scope

The following earlier conclusions are not asserted by this narrowed note:

- The framework baseline plus retained inputs leave the count globally undetermined.
- Both determinant/counting readings are native physical readouts.
- Neither determinant/counting reading is forced by any framework rule.
- Any physical claim that the doublet-count choice remains unselected.
- Any K-theory, PRR, or charged-lepton mass-readout selection conclusion.

Those statements would require the auditor-requested exhaustiveness or selector theorem. This branch
does not add that theorem; it makes the existing row honest as a finite algebraic support packet.

## Audit Relevance

The auditor judged the runner's S1-S4 algebra to be substantive but found the central conclusion too
broad. This repair takes the bounded-scope path: it keeps the verified formulas and removes the global
no-selector claim from the load-bearing result. It does not retag the audit ledger, does not propose an
effective status change, and does not add a new axiom.
