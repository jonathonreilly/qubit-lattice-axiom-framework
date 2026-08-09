# Historic intake: Koide Higgs-Dressed Transport Susceptibility Theorem

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

The empirical slope is given an exact identity: alpha = -F_lambda/F_h0 = 1 - lambda_*^2 (P_t t' + P_d d')/P_x, numerically alpha = 0.959212206684 with backreaction 0.040787793364 (t' = -6.144428397, d' = -3.073052276), so the visible chamber link would track exact Koide with slope 1 if the reached 2x2 block were frozen.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

alpha = 1 - lambda_*^2 (P_t t' + P_d d')/P_x exactly — the empirical slope becomes an exact identity; the transport chain's one genuine theorem.

## Provenance (pinned)

- Original path: `docs/KOIDE_HIGGS_DRESSED_TRANSPORT_SUSCEPTIBILITY_THEOREM_NOTE_2026-04-20.md`
- Source commit: `cdfc2ad52b45bca6d108ffc7e121fe6984d06328`
- git blob: `eb00159248331be95184f54c2afbb73b39622c60`
- sha256: `ffdc269d85d11effb8586548f3772a63cb39568abec34c1550c81c12cabccc60`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch03/859_KOIDE_HIGGS_DRESSED_TRANSPORT_SUSCEPTIBILITY_THEOREM_NOTE_2026-04-20.md](../../archive_unlanded/historic_intake_originals/branch03/859_KOIDE_HIGGS_DRESSED_TRANSPORT_SUSCEPTIBILITY_THEOREM_NOTE_2026-04-20.md)
- Lines: 167; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_koide_higgs_dressed_transport_susceptibility_theorem​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): alpha is no longer a fit — the entire gap between bare chamber-link tracking and exact Koide is a single ~4.08% reached-block backreaction.
- Extraction scope (triage compression; may reflect later context): Exact local susceptibility identity at the physical root; no derivation of the backreaction, of lambda_*, or of Q = 2/3.
- Extraction red flags: none recorded
- Supersession (as known at extraction): Sharpens the affine-germ theorem's empirical coefficient into an exact identity; sharpened by the omitted-channel self-energy theorem. The whole eight-note chain is then shown non-selective by the basin-transfer no-go.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
