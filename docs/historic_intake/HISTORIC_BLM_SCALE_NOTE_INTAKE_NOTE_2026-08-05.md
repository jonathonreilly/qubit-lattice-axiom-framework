# Historic intake: BLM Scale for Hierarchy: alpha_V(q*) Determination

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_measurement
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

The BLM optimal scale for the staggered fermion self-energy is q*a = 2.68 (matching the known Lepage-Mackenzie Wilson value 2.63), giving alpha_V(q*) = 0.102 and hence v = 6.0 GeV — a factor ~40 short of 246 GeV, with the inverse calculation requiring an unphysical negative alpha_V.

Original verdict: The BLM prescription does NOT naturally produce the alpha_V ~ 0.14 needed for v = 246 GeV.
Scope: 1-loop BLM scale setting fed into the hierarchy formula, with sensitivity tables in alpha_V and y_t.


## Why pulled (supervisor decision, on the record)

BLM negative: the optimal-scale prescription gives v = 6 GeV, a factor ~40 short — a real falsifier of the naive hierarchy route, adverse evidence for the era's exact-match claims.

## Provenance (pinned)

- Original path: `docs/BLM_SCALE_NOTE.md`
- Source commit: `831d7d289e3ecb57405d09a5b5496778637d00d3`
- git blob: `f8babefe632086e5912d07b305253a3a4f3c75c9`
- sha256: `b49c3ee1af278bce50817dd736ab2aba4dc6ea1db1f1ce362b234ae90ba24886`
- Lines: 115; runners named: scripts/frontier_blm_scale.py

## Attached evidence (registered with, not as, this claim)

- `docs/BLM_AUDIT_NOTE.md` — Reconciliation of the two BLM computations.

## Flags carried

A negative result against the hierarchy route: reproducing v would require unphysical negative alpha_V.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
