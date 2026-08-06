# Historic intake: Koide A1 — Brannen delta Euclidean Rotation Angle Closure Theorem

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

Plancherel algebra on the retained Brannen mass formula gives a_0 = sqrt(3) V_0 and b = (sqrt(3)/2) V_0 c exp(i delta), so delta_Brannen = arg(b) mod 2pi — a Euclidean rotation angle in radians with no R/Z -> U(1) exponential lift, meaning the audit's period-1-vs-2pi convention question never arises on this observable.

Original verdict: P_A1 blocks only the identification half by assuming a U(1) lift, and since the Brannen chain goes through arg rather than exp(2pi i c), the audit's blocking does not apply to this route.
Scope: Closes only the IDENTIFICATION half of the radian-bridge residual; the SELECTION half (arg(b)(m_*) - arg(b)(m_0) = 2/9 exactly) is carried by the retained selected-line geometry, verified numerically to 1e-12.
Escape conditions (negative claims): The prior no-go depended on identifying delta with a Type-B R/Z invariant via the canonical chi(c) = exp(2pi i c) (which gives 4pi/9 rad and would need the non-canonical period-1 lift to reach 2/9); the escape used here is that the Brannen observable never passes through that lift at all.

## Why pulled (supervisor decision, on the record)

Closes the identification half of the radian-bridge residual: delta_Brannen is a Euclidean rotation angle in radians natively (no U(1) lift assumed) — the no-go's identification half discharged.

## Provenance (pinned)

- Original path: `docs/KOIDE_A1_BRANNEN_EUCLIDEAN_ROTATION_ANGLE_CLOSURE_THEOREM_NOTE_2026-04-25.md`
- Source commit: `9eb6214cee8920880ca943de7246c92c03198a90`
- git blob: `3e4cc02ad233ae71972429c35220e0817da2a4de`
- sha256: `15d832b557e7c4344103b234d70d31258f580c48333fa729ddc63cdae569a787`
- Lines: 370; runners named: scripts/frontier_koide_a1_brannen_euclidean_rotation_angle_closure.py, scripts/frontier_koide_brannen_route3_geometry_support.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
