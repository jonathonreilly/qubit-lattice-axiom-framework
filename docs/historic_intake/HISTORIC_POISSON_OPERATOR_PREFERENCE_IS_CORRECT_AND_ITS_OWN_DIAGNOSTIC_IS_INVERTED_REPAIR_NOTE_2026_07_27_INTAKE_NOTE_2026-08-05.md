# Historic intake: The parent note's operator preference is correct and its own diagnostic is inverted, under a far-field protocol on the tested operator family

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: closed_unmerged_never_landed
Era: post_reset_2026_06_29 — no axiom load-bearing; assumes landed lattice Green's function content on Z^3, G(r) = 1/(4*pi*r) + [5/(32*pi)] K4(nhat)/r^3 + O(1/r^5)

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Under a fixed-window far-field protocol on a boundary-free lattice up to N=192, unscreened Poisson recovers the landed asymptotic (beta 2.329 to 1.126, 4*pi*r*G to 0.855) while biharmonic decays not at all (beta 0.138 to 0, beta*N ~ 26), the 1/r^2 kernel returns exactly 2.000000000, and the screened sweep runs 1.68/3.10/5.60/7.39/9.74; but the parent note's own scaling window (radii 2..N/2-3) scores biharmonic at beta = 1.005 at N=24 versus Poisson at ~1.8 — the diagnostic is inverted, not merely noisy. A box-scaling window converges to a stable wrong value (beta ~ 1.66, 4*pi*r*G ~ 0.65).

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Terminal of the three-cycle diagnostic arc: parent conclusion recovered on a far-field protocol while the parent's own beta diagnostic is inverted (scores biharmonic 1.005); evidence-order correction on a landed critical row.

## Provenance (pinned)

- Original path: `docs/POISSON_OPERATOR_PREFERENCE_IS_CORRECT_AND_ITS_OWN_DIAGNOSTIC_IS_INVERTED_REPAIR_NOTE_2026-07-27.md`
- Source commit: `233bd8f3d4b734997068b20efc89cc96f92986d3`
- git blob: `c5fe0028cb28c341d66f647a71ce0717c7e8b9fd`
- sha256: `e35f8f95cc6b29c6a7a0eddced5ed4adac36db4a27565e6be3e2859e034a6806`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/recovery/3090_POISSON_OPERATOR_PREFERENCE_IS_CORRECT_AND_ITS_OWN_DIAGNOSTIC_IS_INVERTED_REPAIR_NOTE_2026-07-27.md](../../archive_unlanded/historic_intake_originals/recovery/3090_POISSON_OPERATOR_PREFERENCE_IS_CORRECT_AND_ITS_OWN_DIAGNOSTIC_IS_INVERTED_REPAIR_NOTE_2026-07-27.md)
- Lines: 248; runners named: historic runner (unpinned, not in this packet): `scripts/physical_poisson_far_field_protocol_repair_cycle712_2026_07_27​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/CYCLE712_VALUE_NO_GO_AND_CLUSTER_CAP_GATES_2026-07-27.md` — The inverted-diagnostic finding; carried in the arc terminal 3090.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): The parent note's Bounded Claim 1 conclusion is recovered on a far-field diagnostic while its own evidence orders the operators backwards, and the parent construction cannot supply the localized source the measurement needs (U9).
- Extraction scope (triage compression; may reflect later context): Not a claim that Poisson is the field equation of the lane, and explicitly not a uniqueness theorem over all local operators (the parent note's finite-family caveat stands); the far-field rows are periodic rather than Dirichlet while the inversion row U4 is Dirichlet; U1 is a control against landed repo content, not a new derivation; nothing here is self-consistent.
- Extraction escape conditions (negative claims; triage compression): The no_go against the parent diagnostic is scoped to that window protocol on the tested operator family, not to all decay diagnostics; the far-field separation is measured periodically, which removes the Dirichlet boundary rather than modelling it — the note names this as the honest reason and a limitation of the measurement; U9's 'cannot be obtained self-consistently' is a structural limit of the parent construction (normalized branch scale-locked at RMS/N ~ 0.30, un-normalized spreads to ~0.51 with total mass diverging 4.19e6 to 1.38e20), escapable only by an externally prescribed source or a source term that is not the normalized propagator density.
- Extraction red flags: Self-declared limitation that the far-field separation is periodic while the parent construction is Dirichlet; audit_required_before_effective_retained: true and bare_retained_allowed: false in its own status block.
- Supersession (as known at extraction): Third of a three-cycle arc on parent row self_consistency_forces_poisson_note (critical root, 727 transitive descendants) after #5656 and #5662; performs the successor #5662 named; proposes a revision replacing Bounded Claim 1's evidence and withdrawing the distance-law citation; the note does not edit the parent or any audit-lane surface.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
