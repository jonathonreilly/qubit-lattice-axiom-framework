# Historic intake: Scale-free adjacency ceiling and the dissection cost bracket — Cycle 724

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: fork_pr_only
Era: post_reset_2026_06_29 — LATTICE axiom's 6-NN adjacency and proper cubic rotations from MINIMAL_AXIOMS_2026-06-29 define the admissible set

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

An adjacency-only vertex set is affinely flat: any set of lattice sites pairwise at L1 distance at most one occupies at most two distinct positions (verified by complete enumeration over the 125 sites of the -2..2 box, zero offending triples), so such a set lies in a two-site slab crossed with the tick axis, has affine rank in {1,2}, and every five-subset has cell volume exactly zero. Hence no nondegenerate 3- or 4-simplex is adjacency-only at any lattice scale, vertex choice, or box — removing the escape that a refined cell might be adjacency-only. The cost question is then bracketed at 96 to 108 (unimodular corner dissections; 56 for mixed volumes), and one refinement step gives a region floor of 80.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Scale-free ceiling: adjacency-only vertex sets are affinely flat (escape-proof by construction) — closes the refinement escape without enumeration.

## Provenance (pinned)

- Original path: `docs/PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03.md`
- Source commit: `c28a1e42f7441f98ceced0c41f348ebf15ef3dd2`
- git blob: `fe63c75ccbb684c60e6553c7bb00f9b66006cbaf`
- sha256: `18d228717a4ccf0bb9d3a3ac0d240b47e53d9f4de3d1794ef21354aa6e10ecab`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/recovery/3104_PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03.md](../../archive_unlanded/historic_intake_originals/recovery/3104_PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03.md)
- Lines: 216; runners named: historic runner (unpinned, not in this packet): `scripts/physical_scale_free_adjacency_dissection_bracket_cycle724_2026_08_03​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): The scale-free ceiling closes the refinement escape without enumeration, turning cell count from a feasibility question into a cost question; the bracket 96 to 108 is not closed and 108 is not claimed optimal.
- Extraction scope (triage compression; may reflect later context): The affine-flatness result is scale-free and vertex-free; every subsequent cost statement is over corner vertex sets of a specified cell; the 96 floor is over unimodular corner dissections only; clique numbers 8 and 16 are maxima over the corner census only; the refined measurement is at one refinement step with no sequence, limit, or asymptotic claim; nothing here concerns the second-variation form, its spectrum, or any continuum quantity.
- Extraction escape conditions (negative claims; triage compression): The negative (no adjacency-only nondegenerate simplex) is escape-proof by construction — scale-free, vertex-free, box-free — which is precisely its point against the refinement escape the previous cycle left open. The refined region floor 80 exceeds the coarse floor 56 but sits BELOW the achieved coarse count 108, so nothing shows a finer construction must cost more; the note states this against interest.
- Extraction red flags: Records a caught error: an earlier reading of this graph took clique candidates in increasing rather than decreasing colour order, silently under-reporting and producing a below-average clique of 14 and an inflated floor of 98. The note names the below-average maximum of 16 as the one number with no colour-free confirmation and invites attack there.
- Supersession (as known at extraction): Supersedes the in-flight cycle 723 corner-restricted adjacency result and its floor of 48; removes the escape that cycle left open.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
