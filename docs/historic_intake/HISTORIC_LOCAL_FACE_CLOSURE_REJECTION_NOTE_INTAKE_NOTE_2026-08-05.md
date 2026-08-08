# Historic intake: Minimal Local Face-Closure Candidate Rejection at beta = 6

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: no_go
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

The minimal local closure system G = 1 + 3 p^4 G^5 + p^14 G^15 has no positive real solution: with the strict lower bound p_low = 0.42253173964998 < P_1plaq(6), the residual g(G) has g(0) > 0, g'' > 0 for G > 0, a unique positive minimum near G_* = 1.202246940360351 with g(G_*) = 0.0380192306425637 > 0, so g(G) > 0 for all G > 0.

Original verdict: The weakest local face-closure axiom is rejected — the exact local theorems are real but do not by themselves produce a physically admissible analytic plaquette closure.
Scope: Rejects only the weakest explicit local closure axiom (one generic frontier-face amplitude plus the local one-cell/three-cell launch sectors) at beta=6; does not derive analytic P(6).
Escape conditions (negative claims): Closure must retain nontrivial correlations among outgoing frontier faces beyond this minimal local factorization; the next stronger exact obstruction is recorded in ONE_SHELL_FACE_STATE_TRANSFER_NO_GO_NOTE (even the full multiset of one-shell boundary-face states does not determine the next rooted continuation count).

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Exact rejection of the weakest local face-closure axiom: no positive real solution — with the correlation-retention escape named.

## Provenance (pinned)

- Original path: `docs/LOCAL_FACE_CLOSURE_REJECTION_NOTE.md`
- Source commit: `60a264ba93427b648c4c01edb5b2437542b78eb5`
- git blob: `40ae51af105615d6400f2cddfd692f9bdebf266d`
- sha256: `688b768ed19fba0b1f36951970fff6d44566a9ae6a8822bf2a69ec794b1cf21f`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch04/1112_LOCAL_FACE_CLOSURE_REJECTION_NOTE.md](../../archive_unlanded/historic_intake_originals/branch04/1112_LOCAL_FACE_CLOSURE_REJECTION_NOTE.md)
- Lines: 100; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_local_face_closure_rejection(.py)`

## Attached evidence (registered with, not as, this claim)

- `docs/ONE_SHELL_FACE_STATE_TRANSFER_NO_GO_NOTE.md` — One-shell multiset insufficiency.

## Flags carried

none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_no_go
intake_directive: owner_2026-08-05
```

Independent audit still required.
