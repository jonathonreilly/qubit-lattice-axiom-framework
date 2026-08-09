# Historic intake: Velocity-Anisotropy Computation: the delta v ~ 0.31 Signal Was a Doubler Artifact (Validation / False-Alarm Retraction)

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: branch_only_never_mainlined
Era: may_june_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

A prototype one-loop delta v/v = B - A ~ +0.31 per g^2 C_2 — which would have falsified the framework against LV bounds ~1e-20 — is diagnosed as four compounding errors dominated by fermion doublers: naive A is log-divergent (-0.295, -0.322, -0.332 at N = 16, 24, 32), B == 0 is a parity artifact not a Ward identity, and A, B are gauge-dependent off-shell renorms rather than the pole velocity. Wilson (r=1, doubler-free) collapses the anisotropy ~5x to a convergent 0.058 with B = -0.025, and an isotropic 4d-symmetric control gives -0.004 ~ 0.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

THE FALSE-ALARM RETRACTION: a would-be framework falsification (delta v/v ~ +0.31 vs LV bounds) diagnosed as four compounding errors — integrity exemplar.

## Provenance (pinned)

- Original path: `docs/VELOCITY_ANISOTROPY_DOUBLER_ARTIFACT_VALIDATION_NOTE_2026-06-07.md`
- Source commit: `338e6d544368e62b446425a6823ee7a7f3ce002f`
- git blob: `384b7e2c5a82533354a86e173b55c418216e9b15`
- sha256: `0a03febce9c8b788118a14b223a9947588153b9d6042cf242dc981a06e363d14`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch07/2099_VELOCITY_ANISOTROPY_DOUBLER_ARTIFACT_VALIDATION_NOTE_2026-06-07.md](../../archive_unlanded/historic_intake_originals/branch07/2099_VELOCITY_ANISOTROPY_DOUBLER_ARTIFACT_VALIDATION_NOTE_2026-06-07.md)
- Lines: 147; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_velocity_anisotropy_doubler_artifact_validation_2026_06_07​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/VELOCITY_ANISOTROPY_DISCRETIZATION_ARTIFACT_NOTE_2026-06-07.md` — The bare-quantity uncomputability sharpening.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): The 0.31 alarm is retracted and the framework is NOT falsified at O(g^2); status reverts to LORENTZ_NATURALNESS_GAP with delta v ~ O(alpha_s/pi), generically nonzero and uncomputed at the gauge-invariant pole level.
- Extraction scope (triage compression; may reflect later context): Validation of a prototype that was never shipped as a claim; sets no audit status and does not change #3123/#3134.
- Extraction red flags: Explicit false-alarm retraction of a would-be falsification; also rejects the opposite 'shared-kernel kills it' claim, leaving delta v neither 0.3 nor 0.
- Supersession (as known at extraction): Retracts its own prototype alarm; itself sharpened by idx 2098, which shows the surviving 0.058 is also discretization-dependent.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_retraction
intake_directive: owner_2026-08-05
```

Independent audit still required.
