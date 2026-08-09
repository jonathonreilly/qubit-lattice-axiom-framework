# Historic intake: Claim Status Certificate (YAML front matter)

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: pack_science_family
Era: post_reset_2026_06_29

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Certifies a bounded numerical witness against affinity at stated tolerances for one fixed operator, from a fixed finite-operator computation with source-step-free endpoints and an eleven-point residual bound. N1 records five attempted attacks on the witness (finite-difference truncation, misidentified max-absolute branch, normalization drift, floating cancellation, wrong scalar coordinate), with the active gap staying above 1.2e-5 and 60/90-digit and sparse-double implementations agreeing.

Original verdict: Bounded theorem after an exact-to-bounded demotion; No-Go Discipline status PASS at iteration 2; independent audit required and no author/review artifact assigns an effective status.
Scope: One fixed box, one fixed scalar segment, 11 backgrounds, three probes, all 27 trace-free entries, two tangent channels; A_min restored to Lattice+Qubit+Admissibility+Record; zero fitted/observed/literature inputs.
Escape conditions (negative claims): N6 live routes: a validated numerical enclosure for exact nonaffinity, a physical principle selecting the interpolator/readout, a local/smooth observable removing the spline tail, and a physical tensor/GR bridge; N2 names walls W_I (interpolation/readout contract) and W_P (physical tensor observable) and explicitly declines to assert their independence.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Self-documented exact-to-bounded demotion: a former exact/global affinity claim is demoted to a bounded numerical witness at stated tolerances for one fixed operator. The demotion itself is the record; N6 names the live routes back (validated numerical enclosure et al.).

## Provenance (pinned)

- Original path: `.claude/science/physics-loops/s3-time-tensor-primitive/CLAIM_STATUS_CERTIFICATE.md`
- Source commit: `60c90e0a6258b3394cf7235ab0b98106925e51c5`
- git blob: `fa3a19c5c652735b32452bd0664ce63d63c6be3d`
- sha256: `cc2d95b7bf806d7bdddb48d9a77c12449eb3ec96eac01beded3563b48e5c0d45`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/packsci04/11207_CLAIM_STATUS_CERTIFICATE.md](../../archive_unlanded/historic_intake_originals/packsci04/11207_CLAIM_STATUS_CERTIFICATE.md)
- Lines: 115; runners named: none
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `.claude/science/physics-loops/s3-time-tensor-primitive/NO_GO_LEDGER.md` — Companion: only the WORDING is pruned at numerical tolerance; the sibling primitive note is recorded; three route families kept honest.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: self-documented CORRECTION: the claim was demoted from exact/global to bounded numerical after a steelman showed 60/90-digit stability is not an interval proof and both implementations share derivative algebra
- Supersession (as known at extraction): records the demotion of a former exact/global claim to a bounded numerical witness after the N7 steelman; cites QUARK_ROUTE2_ETA_FLOOR_HF_BOUNDARY_NOTE.md as a method-only boundary later bypassed

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded_theorem_certificate
intake_directive: owner_2026-08-05
```

Independent audit still required.
