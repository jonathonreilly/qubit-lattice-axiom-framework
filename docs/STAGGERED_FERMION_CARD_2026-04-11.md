# Staggered Fermion Canonical 17-Card Finite Runner Certificate

**Date:** 2026-04-11; finite-runner scope repair 2026-05-25
**Status:** bounded-support finite runner certificate. No screened-Poisson bridge, positive-source theorem, physical gravity interpretation, universal graph-family claim, or framework-native staggered-Dirac realization is part of the binding theorem.
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_staggered_17card_finite_scope_repair.py`
**Canonical runner executed by primary runner:** `scripts/frontier_staggered_17card.py`
**Status authority:** independent audit lane only.
**Packet source update (2026-07-15; PR #5385):** claim-scoped audit packets
include the complete source of `scripts/frontier_staggered_17card.py` alongside
the primary wrapper.

## Actual claim

This row now claims only the finite computational certificate produced by the
canonical repository runner `scripts/frontier_staggered_17card.py`.

At the fixed runner constants

```text
MASS = 0.3
G = 50.0
S = 5e-4
DT = 0.15
```

with the runner's prescribed external potential builders and parity-coupled
diagonal term

```text
H_diag = (m + V(x)) epsilon(x),
```

the canonical runner reports:

- 1D card, `n = 61`: `SCORE: 17/17`;
- 3D card, `n = 9`: `SCORE: 17/17`;
- 3D card, `n = 11`: `SCORE: 17/17` with the stated C17 family-coverage gate;
- 3D card, `n = 13`: `SCORE: 17/17` with the stated C17 family-coverage gate.

That fixed finite runner certificate is the entire repaired theorem.

## Why this repair is narrow

The prior conditional audits accepted that the canonical runner computes a
nontrivial finite score surface, but kept the row conditional because the old
card also claimed a broader physical sign chain. That chain used imported
premises: a screened-Poisson source law, positive source and positivity
readout, free `G` and `mu`, selected graph families, sign conventions, and
framework-native staggered-Dirac realization.

This repair withdraws those physical and framework-realization claims from
the binding theorem. The row is only a finite runner certificate for the
prescribed external-potential card.

## What this row does not claim

- It does not derive `(L + mu^2) Phi = G rho`.
- It does not derive `rho = |psi|^2`, `Phi >= 0`, or a positive-source bridge.
- It does not derive `G`, `mu`, the graph families, or a universal graph claim.
- It does not derive physical gravity, attraction, or a dynamical metric.
- It does not derive the staggered-Dirac structure from the framework.
- It does not claim the companion multi-runner aggregate tables from older versions of this card.
- It does not add an axiom or apply an audit verdict.

The bridge from this finite runner certificate to a physical staggered-gravity
theorem remains a separate open science problem.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_staggered_17card_finite_scope_repair.py
```

Expected result:

```text
Staggered canonical 17-card finite-scope repair
TOTAL: PASS=20 FAIL=0
```
