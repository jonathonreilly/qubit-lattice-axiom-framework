# Historic intake: Gravity Field Equation Derived: Self-Consistency Forces Poisson

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_theorem
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

The Green's-function mismatch M(L) = ||L^-1 delta - G_0 delta||/||G_0 delta|| vanishes exactly for L = -Delta_lat and is positive for all 10 tested alternatives (all M > 0.28); across the continuous family L_alpha = (-Delta)^alpha on [0.3, 2.5] the mismatch is strictly minimized at alpha = 1 with M(1) < 6e-16 versus M(0.9) = 0.125 and M(1.1) = 0.131.

Original verdict: Nothing in the Poisson derivation chain remains open - it is an algebraic chain with no model-dependent steps.
Scope: Assumes the framework axiom plus nearest-neighbor propagation and rho = |psi|^2 sourcing; the operator L is derived rather than chosen.


## Why pulled (supervisor decision, on the record)

The 'nothing open' Poisson claim — pulled as the contradiction pair's maximal half (652 grades the same step BOUNDED); audit rules.

## Provenance (pinned)

- Original path: `docs/GRAVITY_POISSON_DERIVED_NOTE.md`
- Source commit: `42803d8044824f16f74d1af66455cb15f92b5fb9`
- git blob: `c7bf9e681430d7df6ab863e53b8f1192c76decc1`
- sha256: `91a6164342245c94b8ae0d69fcaf017e226bddd31ce7d693d180c9ec62786fb5`
- Lines: 142; runners named: scripts/frontier_gravity_poisson_derived.py, scripts/frontier_newton_derived.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Claims nothing remains open, while the umbrella chain document (idx 646) grades this exact step BOUNDED and calls it the weakest link.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
