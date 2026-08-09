# Historic intake: Analysis: Continuum Limit

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: march_2026_event_network_era
Era: march_event_network — 8-neighbor rectangular lattice with delay field as discrete Green's function on a finite domain

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

The model has no naive continuum limit on a fixed grid: signal-speed anisotropy is scale-invariant at 8.23% for all measurement distances 5-70 grid units (off-axis action excess 7.06-7.25% at all path lengths), while interference converges (V(y=1) stabilizes at 0.978-0.985 for widths >= 12) and gravity dilutes (action-diff per unit path length falls from -0.345 at width=20 to -0.160 at width=80).

Original verdict: Discreteness is irreducible on a fixed grid — the 8.2% anisotropy is a permanent lattice feature defining a model 'Planck scale', and a continuum limit requires changing the graph itself (finer spacing, irregular/random graphs, or extended neighbor connectivity).
Scope: Fixed 8-neighbor rectangular lattice; distances 5-70 grid units; widths 20-80.
Escape conditions (negative claims): The no-continuum-limit result is stated to hold only for a FIXED rectangular 8-neighbor grid probed at larger distances; the note names three escapes — finer grid spacing (more nodes per physical unit), irregular/random graphs with no preferred directions, or extended neighbor connectivity — and speculates a GROWING graph would reduce anisotropy in physical units.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Clean bounded no-go: no naive continuum limit on a fixed 8-neighbor grid — 8.23% scale-invariant anisotropy matching the exact staircase bound — with three named escapes; lineage-relevant to current Z^d anisotropy questions.

## Provenance (pinned)

- Original path: `.claude/science/analyses/continuum-limit-2026-03-30.md`
- Source commit: `611bf217ac84c02910c6b2aeb91b1a0cefc5f582`
- git blob: `5a76aaab6d8ad5ee0dacda46e6ec5b348e291c55`
- sha256: `c63133dc9fe31d4a5caf020384b2247a28cf296b5016eed80355ccdaacb35c74`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/march/3113_continuum-limit-2026-03-30.md](../../archive_unlanded/historic_intake_originals/march/3113_continuum-limit-2026-03-30.md)
- Lines: 33; runners named: none
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `.claude/science/analyses/lorentz-breaking-2026-03-30.md` — The 8.2% anisotropy with exact staircase bound; same result as the continuum-limit no-go's core number; evidence attachment.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: none recorded
- Supersession (as known at extraction): none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_analysis
intake_directive: owner_2026-08-05
```

Independent audit still required.
