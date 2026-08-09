# Historic intake: Color-Singlet Zero-Mode-Removed Ladder Pole Search

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

Scanning N = 3..6 and masses 0.20-1.00 with the q=0 mode removed finds four rows with lambda_max >= 1 (finite pole witnesses) but volume stability fails (local m=0.30 gives 0.266, 1.463, 0.127, 0.366 at N=3,4,5,6), projector stability fails (N6 m=0.20: local 1.487 vs point-split 0.510), all crossing rows sit on even grids with 16 sin(p)=0 corners, and the residue-proxy spread is 5.15x. PASS=9 FAIL=0.

Original verdict: The finite pole witnesses are route information, not scalar LSZ closure — they are sensitive to finite-volume parity, taste-corner aliasing, source projector, and the total-momentum derivative.
Scope: Finite Wilson-exchange ladder with color-singlet q=0 removal at mu_IR^2 = 0.
Escape conditions (negative claims): The narrower positive route is named: derive the continuum/taste/projector limit of the interacting color-singlet scalar denominator and its inverse-propagator derivative, or measure the same-source pole derivative in production FH/LSZ data.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Color-singlet denominator terminal: finite pole witnesses are route information (volume stability fails) — the narrow positive route named.

## Provenance (pinned)

- Original path: `docs/YT_COLOR_SINGLET_ZERO_MODE_REMOVED_LADDER_POLE_SEARCH_NOTE_2026-05-01.md`
- Source commit: `08afdf263d4b43a0a187c390e9313615cb2f842d`
- git blob: `65b8f4682df981eb12ea4e847b33d00f005aaf41`
- sha256: `eff6242c3ed19a09fda9cebb8992c8ee32307dd2ca8a5c91ca49754687b1eed4`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch07/2162_YT_COLOR_SINGLET_ZERO_MODE_REMOVED_LADDER_POLE_SEARCH_NOTE_2026-05-01.md](../../archive_unlanded/historic_intake_originals/branch07/2162_YT_COLOR_SINGLET_ZERO_MODE_REMOVED_LADDER_POLE_SEARCH_NOTE_2026-05-01.md)
- Lines: 51; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_yt_color_singlet_zero_mode_removed_ladder_pole_search​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/YT_COLOR_SINGLET_FINITE_Q_IR_REGULAR_NOTE_2026-05-01.md` — Color-singlet chain link.
- `docs/YT_COLOR_SINGLET_ZERO_MODE_CANCELLATION_NOTE_2026-05-01.md` — Color-singlet chain link.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: none recorded
- Supersession (as known at extraction): TERMINAL of the color-singlet denominator sub-chain: the cleaned kernel still yields no stable pole.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded_result
intake_directive: owner_2026-08-05
```

Independent audit still required.
