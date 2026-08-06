# Historic intake: Dark Energy Equation of State: w = -1 from S^3 Spectral Rigidity

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_conditional_theorem
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

On S^3 of radius R the scalar Laplacian eigenvalues are lambda_l = l(l+2)/R^2 so the first nonzero one is 3/R^2, with the coefficient 3 fixed by topology (the SO(4) Casimir on S^3 = SO(4)/SO(3)); hence Lambda = 3/R^2 is constant and T_{mu nu} = -(Lambda/8 pi G) g_{mu nu} gives w = p/rho = -1 exactly, with lattice corrections O((a/R)^2) ~ 1e-122 and themselves constant.

Original verdict: Conditional on S^3 compactification the framework predicts w = -1 exactly with no corrections at any order; it does not predict the numerical value of Lambda, and any measurement of w != -1 would rule out the S^3 spectral-gap identification.
Scope: Conditional on the S^3 compactification lane, which is itself bounded/open and not derived from the axioms.


## Why pulled (supervisor decision, on the record)

Conditional-exact w = -1 prediction from S^3 topology (lambda_1 = 3/R^2) — with the Lambda-magnitude concession honest.

## Provenance (pinned)

- Original path: `docs/W_MINUS_ONE_NOTE.md`
- Source commit: `92dd355e65bea56ab4ae6ac7602a82e4a08079f5`
- git blob: `2692cc0c1f62da42c3fa387482a3c8c77e387817`
- sha256: `1346e60779721965b9f1cd7737d2ec72bd1cda7d838d8e2d72d720c9b02fbfd9`
- Lines: 99; runners named: scripts/frontier_w_minus_one.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Concedes that the observed Lambda ~ 1e-122 is 'a coincidence of scale, not a prediction of the framework in its current form'.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
