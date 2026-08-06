# Historic intake: PR #230 FH/LSZ Polynomial-Contact Finite-Shell No-Go

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_no_go
Stratum: branch_only_never_mainlined
Era: may_june_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

For n distinct shell points any chosen residual values S_i can be written as C_i - P(x_i) = S_i for a unique polynomial P of degree at most n-1, so unconstrained polynomial contact subtraction identifies nothing; the runner exhibits two strict positive one-pole Stieltjes residuals S(x) = residue/(x + mass_sq) with different mass_sq, each reproduced from the measured eight shells by an interpolated degree-7 contact term.

Original verdict: Finite-shell Stieltjes checks after an unconstrained polynomial subtraction do not identify the physical two-point object, the pole residue, or kappa_s.
Scope: Blocks promoting finite polefit8x8 rows via arbitrary higher-degree local contact subtraction.
Escape conditions (negative claims): A constrained or derived contact term (a same-surface certificate or microscopic denominator theorem) is untouched by this argument.

## Why pulled (supervisor decision, on the record)

Polynomial-contact no-go: unconstrained subtraction can manufacture any residual — closes the contact-fitting loophole exactly.

## Provenance (pinned)

- Original path: `docs/YT_FH_LSZ_POLYNOMIAL_CONTACT_FINITE_SHELL_NO_GO_NOTE_2026-05-05.md`
- Source commit: `ad2370a628a50e6627db522b43e458ffe4cd1cd1`
- git blob: `03e55838dd3a6211087cba487520acea8d00409d`
- sha256: `259373360446bf1df2f2977a0140f36acc7e665ea51ff0690e6ae7173ad77264`
- Lines: 72; runners named: scripts/frontier_yt_fh_lsz_polynomial_contact_finite_shell_no_go.py

## Attached evidence (registered with, not as, this claim)

- `docs/YT_FH_LSZ_AFFINE_CONTACT_COMPLETE_MONOTONICITY_NO_GO_NOTE_2026-05-05.md` — The affine complete-monotonicity predecessor.
- `docs/YT_FH_LSZ_CONTACT_SUBTRACTION_IDENTIFIABILITY_NOTE_2026-05-05.md` — Affine-contact boundary predecessor.
- `docs/YT_FH_LSZ_POLYNOMIAL_CONTACT_REPAIR_NO_GO_NOTE_2026-05-05.md` — Companion: both fitting regimes fail.

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
