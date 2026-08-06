# Historic intake: The self-consistent beta has no far field to extrapolate, so the finite-size caveat cannot defend it, given the parent note's own construction and diagnostic

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_no_go
Stratum: closed_unmerged_never_landed
Era: post_reset_2026_06_29 — no axiom load-bearing; assumes the parent propagator construction and check_field_physics diagnostic

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Poisson's self-consistent exponent extrapolates to b_inf = 1.2747 +/- 0.0177 (1/N) or 1.1578 +/- 0.0012 (1/N + 1/N^2), never to the asserted 1.0 (beta = 1.2550 at N=48, moving only +0.0311 per doubling); the Poisson-vs-biharmonic gap shrinks monotonically from +0.1562 at N=20 to +0.0732 at N=48 and the two families disagree on its extrapolated sign; and the mechanism is that the parent source is scale-locked (total mass exactly 1.000000 with RMS/N essentially constant at 0.3406 to 0.3014 over N=16..48) with the fit window's enclosed source-mass fraction RISING from 0.5067 to 0.8449, so enlarging the lattice moves the diagnostic further from a far-field measurement.

Original verdict: The parent note's finite-size caveat is removed as the sole defence of Bounded Claim 1, and the cited distance-law script measures ray deflection in a prescribed field (the string self_consistent does not occur in it) — a different observable in a different field.
Scope: Every row scoped to the tested construction at the parent note's parameters and stated lattice sizes (N=16..48; N=12 excluded because check_field_physics returns nan); not a claim that the lane's field equation is not Poisson, that any rival is better, or that no extrapolation family could reach 1.0 — only the two the repo's own distance-law script uses.
Escape conditions (negative claims): Confined to the caveat and the diagnostic. Escapes named: another extrapolation family could in principle reach 1.0 (untested beyond two); S6 does not claim the field has no far field, only that this fit window does not sample one; the strongest objection (that a box-filling self-consistent source need not have a continuum limit at all) is accepted as correct physics but shown to strengthen rather than rescue, since either the limit is 1.16-1.27 or there is no continuum value to appeal to. The constructive repair — a localized source of fixed extent and fixed total mass with the exponent fitted outside it — is named as the successor and requires giving up the per-layer normalization, which cycle 710 R6 showed does not by itself repair the response kernel, so both repairs would be needed.

## Why pulled (supervisor decision, on the record)

No-go: self-consistent beta extrapolates to 1.27/1.16, never 1.0 — removes the finite-size caveat as sole defence of the landed Bounded Claim 1.

## Provenance (pinned)

- Original path: `docs/POISSON_SELF_CONSISTENT_BETA_HAS_NO_FAR_FIELD_TO_EXTRAPOLATE_DEMOTION_NOTE_2026-07-26.md`
- Source commit: `refs/pull-cache/5662`
- git blob: `0a6df449bc39d178db451b4bddcd6b20fbec2c47`
- sha256: `f2ac73ea05b0a99266c2080493e43503ec9933ca9fba57be47d8f4f0b0a49241`
- Lines: 230; runners named: scripts/physical_poisson_beta_has_no_continuum_limit_cycle711_2026_07_26.py, scripts/frontier_distance_law_definitive.py

## Attached evidence (registered with, not as, this claim)

- `docs/CYCLE711_VALUE_AND_NO_GO_GATES_2026-07-26.md` — Gate record for Cycle 711 — process record of 3093's no-go content.

## Flags carried

audit_required_before_effective_retained: true, bare_retained_allowed: false; only two extrapolation families tested.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
