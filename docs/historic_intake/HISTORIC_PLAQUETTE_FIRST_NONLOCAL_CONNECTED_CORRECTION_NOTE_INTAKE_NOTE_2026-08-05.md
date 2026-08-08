# Historic intake: First Nonlocal Connected Plaquette Correction on the Exact 3+1 Lattice

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

P_full(beta) = P_1plaq(beta) + beta^5/472392 + O_nonlocal(beta^6): the local block and full lattice agree through O(beta^4), and the first distinct correction is the area-5 cube complement with coefficient 4 * 2 * (1/6^6) * (1/81) = 1/472392, using the oriented cube-boundary moment 3^(8-12) = 1/81. Runner 10 pass / 0 fail.

Original verdict: The first nonlocal connected departure from the one-plaquette block is known exactly; this does not close analytic P(beta = 6).
Scope: First nonlocal CONNECTED correction only; lower-order distinct-plaquette terms exist as plaquette-antiplaquette bubbles but factor out as exact unit bubbles.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Exact first nonlocal correction: P_full = P_1plaq + beta^5/472392 + O(beta^6) — the open-surface departure known exactly.

## Provenance (pinned)

- Original path: `docs/PLAQUETTE_FIRST_NONLOCAL_CONNECTED_CORRECTION_NOTE.md`
- Source commit: `60a264ba93427b648c4c01edb5b2437542b78eb5`
- git blob: `1a24c47e51336ee45c4fe930aad48d31d9b5a164`
- sha256: `835c08701cdf2e6ae49765d70c242d86e4ebdaf1a69528ca4afa6e0be84a5712`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch05/1509_PLAQUETTE_FIRST_NONLOCAL_CONNECTED_CORRECTION_NOTE.md](../../archive_unlanded/historic_intake_originals/branch05/1509_PLAQUETTE_FIRST_NONLOCAL_CONNECTED_CORRECTION_NOTE.md)
- Lines: 182; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_plaquette_first_nonlocal_connected_correction(.py)`

## Attached evidence (registered with, not as, this claim)

- `docs/PLAQUETTE_BETA6_PROVENANCE_NOTE.md` — Plaquette family member (1512's normalization mismatch flag carried).
- `docs/PLAQUETTE_BETA6_WILSON_NORMALIZATION_NATIVE_IMPORT_REPAIR_2026-06-17.md` — Plaquette family member (1512's normalization mismatch flag carried).
- `docs/PLAQUETTE_CLOSURE_MATHEMATICAL_PROBES_NOTE_2026-05-05.md` — Plaquette family member (1512's normalization mismatch flag carried).
- `docs/PLAQUETTE_MINIMAL_BLOCK_CLOSED_FORM_NOTE_2026-05-05.md` — Plaquette family member (1512's normalization mismatch flag carried).
- `docs/PLAQUETTE_SINGLE_EXACT_NOTE.md` — Plaquette family member (1512's normalization mismatch flag carried).

## Flags carried

none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_exact_finite_order_gauge_theorem_beyond_the_one_plaquette_block
intake_directive: owner_2026-08-05
```

Independent audit still required.
