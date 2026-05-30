---
claim_type: bounded_theorem
claim_status: bounded_theorem
proposal_allowed: false
---

# Sign Portability Invariant Cached Gate Certificate

**Date:** 2026-05-09; narrowed 2026-05-26
**Claim type:** bounded_theorem
**Status:** bounded cached-output certificate for the runner-defined G1/G2/G3/G4
gate checks. This is not a proof of the unit-slope theorem and not a
cross-family theorem.
**Runner:** `scripts/SIGN_PORTABILITY_INVARIANT_COMPARE.py`

## Purpose

The previous row mixed a valid cached gate sweep with theorem language about
unit-slope regularity and a cross-family corollary. This repair keeps only the
finite, auditable cache statement:

- G1: zero-source cancellation;
- G2: neutral same-point cancellation;
- G3: plus/minus antisymmetry under the runner threshold;
- G4: unit-slope tolerance on runner-accepted rows.

The committed cache reports those gates as passing on the derivation subset,
the five core families, and one holdout family.

## Bounded Claim

In `logs/runner-cache/SIGN_PORTABILITY_INVARIANT_COMPARE.txt`, the runner
reports:

```text
derivation block (second grown family) = PASS
Grown transfer basin                 G1G2G3G4 = PPPP
Alternative connectivity family      G1G2G3G4 = PPPP
Second grown-family sign             G1G2G3G4 = PPPP
Third grown-family sign              G1G2G3G4 = PPPP
Fourth family quadrant               G1G2G3G4 = PPPP
Fifth family radial                  G1G2G3G4 = PPPP
OVERALL: PASS
```

The cache also records the configured thresholds:

```text
ZERO_TOL=1e-12
NEUTRAL_TOL=1e-12
ANTISYM_TOL=5e-03
EXP_TOL=5e-03
```

This is a finite cached certificate that the runner-defined gate checks pass
on the recorded rows.

## Boundary

This row does not claim:

- row-wise lower bounds on detector-layer intensity;
- row-wise lower bounds on first-order plus-source response;
- an unconditional unit-slope theorem;
- a cross-family theorem;
- a physical sign-law derivation from accepted primitives;
- any new axiom or audit verdict.

The lower-bound theorem needed for a full unit-slope proof remains separate
science work.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/SIGN_PORTABILITY_INVARIANT_COMPARE.py
```
