# Handoff

## What This Branch Does

Repairs the finite-Lambda LR theorem proof by replacing the invalid
support-union path count with an interaction-graph chain count and by using the
lattice `ell_1` metric consistently.

## What It Does Not Do

- It does not edit `docs/audit/**`.
- It does not change audit verdicts.
- It does not add a new axiom.
- It does not complete the spatial cluster-decomposition filter lemma.
- It does not claim thermodynamic-limit or continuum clustering.

## Reviewer Checks

- Confirm Lemma B counts fixed-degree local-term chains, not arbitrary
  support-union growth.
- Confirm `R_0 = 2a` is consistently tied to `ell_1` distance.
- Confirm the CD section remains support-only/conditional.

## PR

Pending.
