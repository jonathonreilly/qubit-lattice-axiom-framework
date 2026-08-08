# Historic intake: PR #230 FH/LSZ Pole-Fit Kinematics Gate

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

The four-mode manifest measures (0,0,0), (1,0,0), (0,1,0), (0,0,1), but on a cubic volume the three one-step axis modes share the same p_hat^2 shell — so each volume has only two shells, enough for a finite positive-momentum secant but not to locate an isolated pole, determine dGamma_ss/dp^2 there, or control a continuum remainder without importing a model.

Original verdict: Retained closure needs richer pole-fit kinematics or a theorem, plus FV/IR/zero-mode control and the retained-proposal gate.
Scope: Blocks treating a completed four-mode chunk set as the pole derivative; does not reject the chunks as measurement support.
Escape conditions (negative claims): Richer kinematics is the escape, and is exactly the eight-mode stream launched at idx 2268.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The kinematics flaw identified AT CAMPAIGN START: three axis modes share one shell, yet the 63-chunk stream ran to completion — process fact the audit must see.

## Provenance (pinned)

- Original path: `docs/YT_FH_LSZ_POLE_FIT_KINEMATICS_GATE_NOTE_2026-05-01.md`
- Source commit: `0dca6394fb67d9dd4cbd71f278a884c7c632870a`
- git blob: `7f37b49563e17bb6a5b3f02a4fe989982a6b0802`
- sha256: `7cd9b9b9267759d99139668550eae65204556e44ccd57491036eeb67484c4b32`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch07/2270_YT_FH_LSZ_POLE_FIT_KINEMATICS_GATE_NOTE_2026-05-01.md](../../archive_unlanded/historic_intake_originals/branch07/2270_YT_FH_LSZ_POLE_FIT_KINEMATICS_GATE_NOTE_2026-05-01.md)
- Lines: 46; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_yt_fh_lsz_pole_fit_kinematics_gate(.py)`

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

The four-mode production plan was launched and run to completion despite this gate showing it could not supply the pole derivative.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_no_go
intake_directive: owner_2026-08-05
```

Independent audit still required.
