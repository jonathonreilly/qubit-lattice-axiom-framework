# Historic intake: Erratum: the Weak-Field Rival Action Formula Is Misstated in Probe — L*sqrt(1-phi) Is Weak-Field Linear, and the Measured 0.50 Row Is L(1-sqrt(f))

Explicit subject: The landed P4 note states in three places that the rival action is S = L*sqrt(1-phi) giving F~sqrt(M) = 0.50 and NOT Newtonian, but the probe's action_value() actually computes L*(1.0 - np.sqrt(f)) — leading power 1/2 — while L*sqrt(1-phi) expands as f/2 + f^2/8 + .. (Historic code `P4`: era-local shorthand from the original's own title. The repo's controlled vocabulary keeps the explicit scientific name primary on live surfaces — vocab_lint's legacy_alias_strip rule removes alias parentheticals — so the code is preserved here, in the pinned original, and in its archived copy; the pinned original defines it.)

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: closed_unmerged_never_landed
Era: post_reset_2026_06_29 — no axiom involved; assumes the landed ACTION_UNIQUENESS universality classes keyed to leading power on a fixed family

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

The landed P4 note states in three places that the rival action is S = L*sqrt(1-phi) giving F~sqrt(M) = 0.50 and NOT Newtonian, but the probe's action_value() actually computes L*(1.0 - np.sqrt(f)) — leading power 1/2 — while L*sqrt(1-phi) expands as f/2 + f^2/8 + ... with leading power 1, placing it in the Newtonian class alongside L(1-f), L*exp(-f) and L/(1+f). Consequence: the mass-law exponent cannot discriminate valley-linear from L*sqrt(1-phi), so the comparison as Barrier B(c) frames it has no content.

Original verdict: P4's number 0.50 is correct for the action it meant; the formula it prints is not that action, and the genuine alternative on the mass-law observable is the sublinear class.
Scope: Erratum only: corrects a formula, changes no numerical result, no verdict, no lane status, no axiom or registry surface; every row is a leading-power extraction from a closed-form valley depth with no lattice run and no fitted quantity.
Escape conditions (negative claims): The E5 negative is explicitly narrowed: only the leading mass exponent is blind to the difference between L(1-f) and L*sqrt(1-phi); the two are different functions and higher-order behaviour or a different observable could in principle separate them. An earlier draft claimed outright undecidability and was corrected.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

ERRATUM against a landed note: P4 prints S = L*sqrt(1-phi) in three places but computes L*(1-sqrt(f)); the corrected genuine content and the narrowed E5 negative must be on the ledger.

## Provenance (pinned)

- Original path: `docs/ERRATUM_WEAK_FIELD_RIVAL_ACTION_FORMULA_IS_MISSTATED_IN_PROBE_P4_NOTE_2026-07-26.md`
- Source commit: `refs/pull-cache/5651`
- git blob: `5c288f22d13255956ff72c40582191ba00c6d676`
- sha256: `c328721e6b0562ec72edf4935f4a6009c289f865f5a6072429517a90c2854c86`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/recovery/3082_ERRATUM_WEAK_FIELD_RIVAL_ACTION_FORMULA_IS_MISSTATED_IN_PROBE_P4_NOTE_2026-07-26.md](../../archive_unlanded/historic_intake_originals/recovery/3082_ERRATUM_WEAK_FIELD_RIVAL_ACTION_FORMULA_IS_MISSTATED_IN_PROBE_P4_NOTE_2026-07-26.md)
- Lines: 158; runners named: historic runner (unpinned, not in this packet): `scripts/physical_weak_field_action_form_erratum_cycle707b_2026_07_26​.py`; historic runner (unpinned, not in this packet): `scripts/action_universality_probe​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Self-reported: an earlier draft overstated E5 as outright undecidability and was narrowed; an accompanying attempt to supply a mechanism for the exponent was rejected at the value gate and excluded from the branch; parent row gravity_full_self_consistency_note is critical with 773 transitive descendants, but the note explicitly disclaims that the transcription error bears on them.
- Supersession (as known at extraction): Corrects docs/G_NEWTON_SELF_CONSISTENCY_BOUNDED_SHARPENING_NOTE_2026-05-10_planckP4.md (Barrier B(c) at lines ~89, ~199, ~305).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_erratum
intake_directive: owner_2026-08-05
```

Independent audit still required.
