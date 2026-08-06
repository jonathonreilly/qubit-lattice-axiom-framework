# Historic intake: 64^3 Distance Law: Frozen / Static-Source Control Note

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_bounded
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

The frozen/static-source control reveals a real field-shape discrepancy: FROZEN and ANALYTIC arms are exactly identical while the DYNAMIC (Poisson-solved) arm differs, with the ratio f_fro/f_dyn running from ~0.53 at r = 2 to ~0.70 at r = 8 on the 64^3 grid — the Poisson solver on a finite Dirichlet box carries image-charge boundary corrections that reshape the near-to-mid field and steepen the exponent.

Original verdict: The dynamic-versus-analytic gap is a boundary-condition artifact, which the control identifies rather than the continuation's headline exponent being wrong.
Scope: Companion control to the 64^3 continuation; max spread across arms grows from 1.82% at N = 31 to 3.26% at N = 64.


## Why pulled (supervisor decision, on the record)

Control finding: the headline distance-law measurement is contaminated by a Dirichlet boundary artifact (FROZEN = ANALYTIC exactly; DYNAMIC differs) — a real integrity result against the lane's headline.

## Provenance (pinned)

- Original path: `docs/DISTANCE_LAW_64_FROZEN_CONTROL_NOTE.md`
- Source commit: `3f333ad709d03ea43d5d45c7629e2516afef8559`
- git blob: `21b6d6a961fa1265c707929ca5f0c08178b0830d`
- sha256: `5c0e2d3ed31f4099853cf2ab82aa4c088be1415e8deaf67236bb46a811adac9a`
- Lines: 118; runners named: scripts/frontier_distance_law_64_frozen_control.py

## Attached evidence (registered with, not as, this claim)

- `docs/DISTANCE_LAW_64_BOUNDED_CONTINUATION_NOTE.md` — Monotone convergence toward 1/r^2; continuation.

## Flags carried

Shows the headline distance-law measurement is contaminated by Dirichlet image charges in the near-to-mid region.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
