# Historic intake: Plaquette Scalar-Bridge Theorem: Analytic Route on Main

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

On the 3+1 scalar-bridge surface <P>(beta) = <P>_1plaq(beta_eff) with beta_eff = beta (3/2)(2/sqrt3)^(1/4), built from local Wilson source-response, the scalar 3+1 temporal ratio A_inf/A_2 = 2/sqrt3, the four-link map P(u_0 V) = u_0^4 P(V) and the incidence factor Gamma_coord = 6/4 = 3/2. At beta = 6 this gives <P> = 0.5935307..., differing from the historical same-surface 0.5934 in the fifth decimal.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Bridge theorem that RETRACTS a landed negative and leaves a repo-wide inconsistency (consumers quote 0.5934; bridge gives 0.59353) — audit work order.

## Provenance (pinned)

- Original path: `docs/PLAQUETTE_ANALYTIC_DERIVATION_NOTE.md`
- Source commit: `3026d0167c0f09bd71eef26815e80691122e64ca`
- git blob: `c14e7b91c7d06bb240588709dc4968ef7cc222c5`
- sha256: `47a26f97425b3b3186bad35682809fc044e2da4512a6abb8d61cfdef040d44ee`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch05/1505_PLAQUETTE_ANALYTIC_DERIVATION_NOTE.md](../../archive_unlanded/historic_intake_originals/branch05/1505_PLAQUETTE_ANALYTIC_DERIVATION_NOTE.md)
- Lines: 92; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_scalar_3plus1_temporal_ratio​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_gauge_vacuum_plaquette_bridge_theorem​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): The theorem gap is closed on the chosen route with qualifiers; not promoted as a fully universal analytic derivation.
- Extraction scope (triage compression; may reflect later context): Closed on the chosen 3+1 scalar-bridge route only; no uniqueness claim for that route, and repo-wide numeric migration from 0.5934 is pending.
- Extraction red flags: Retracts a previously landed negative result and leaves a known repo-wide inconsistency: downstream consumers still quote 0.5934 while the bridge gives 0.59353.
- Supersession (as known at extraction): Explicitly RETRACTS the earlier main-derived negative note N1 ('<P> not analytically derivable'); defers to GAUGE_VACUUM_PLAQUETTE_BRIDGE_THEOREM_NOTE as authority.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bridge_theorem_closed_on_main
intake_directive: owner_2026-08-05
```

Independent audit still required.
