# Historic intake: Color-Singlet Zero-Mode-Removed Ladder Pole Search

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_bounded_result
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

## Why pulled (supervisor decision, on the record)

Color-singlet denominator terminal: finite pole witnesses are route information (volume stability fails) — the narrow positive route named.

## Provenance (pinned)

- Original path: `docs/YT_COLOR_SINGLET_ZERO_MODE_REMOVED_LADDER_POLE_SEARCH_NOTE_2026-05-01.md`
- Source commit: `08afdf263d4b43a0a187c390e9313615cb2f842d`
- git blob: `65b8f4682df981eb12ea4e847b33d00f005aaf41`
- sha256: `eff6242c3ed19a09fda9cebb8992c8ee32307dd2ca8a5c91ca49754687b1eed4`
- Lines: 51; runners named: scripts/frontier_yt_color_singlet_zero_mode_removed_ladder_pole_search.py

## Attached evidence (registered with, not as, this claim)

- `docs/YT_COLOR_SINGLET_FINITE_Q_IR_REGULAR_NOTE_2026-05-01.md` — Color-singlet chain link.
- `docs/YT_COLOR_SINGLET_ZERO_MODE_CANCELLATION_NOTE_2026-05-01.md` — Color-singlet chain link.

## Flags carried

none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
