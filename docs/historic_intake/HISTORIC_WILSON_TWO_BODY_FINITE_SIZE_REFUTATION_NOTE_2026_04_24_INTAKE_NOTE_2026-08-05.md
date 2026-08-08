# Historic intake: Wilson Two-Body (m_a + m_b) Newton Scaling: Finite-Size Refutation

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

Across sides 11, 13, 15, 17 with seven mass configs (56 simulations, 41 s) the CV of sa_cross/(m_a + m_b) barely moves (28.7 -> 28.6 -> 28.5 -> 28.5%) and the (2,3)/(3,2) asymmetry likewise (41.9 -> 40.7 -> 40.4 -> 40.3%), while per-config ratios are side-independent to 1-2%. At the observed rates (CV ~0.031%/side) reaching CV < 15% would need ~431 more sides, i.e. ~9e7 sites.

Original verdict: The finite-size hypothesis is REFUTED: the (m_a + m_b) Newton scaling fails as a thermodynamic-limit law, per-config ratios are intrinsic Wilson-Hartree numbers with a 3.5x spread, and the Wilson two-body open-boundary Hartree system is not strictly Newtonian.
Scope: Single seed per side, one separation, one parameter set on the open-boundary Wilson Hartree carrier.
Escape conditions (negative claims): Named falsifiers/escapes: a side > 17 sweep with significantly faster CV decrease would reopen finite size; a closed/periodic/staggered protocol reaching CV < 15% would isolate the failure to the open-boundary Hartree carrier; a static-source approximation would calibrate how much comes from dynamical wave-packet feedback.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

REFUTED terminal: the (m_a + m_b) Newton scaling fails as a finite-size hypothesis (CV flat 28.7->28.5% across sides) — the Wilson two-body chain's honest end.

## Provenance (pinned)

- Original path: `docs/WILSON_TWO_BODY_FINITE_SIZE_REFUTATION_NOTE_2026-04-24.md`
- Source commit: `01c13e53fd7d6f18c1bb77989897f3be5886b2eb`
- git blob: `ca79cca0723feb8ca264418f39aaa200147357df`
- sha256: `41b4ca35d88655666a0cad29c592e66e60058517b6177dcce87a459f9cc6f833`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch07/2130_WILSON_TWO_BODY_FINITE_SIZE_REFUTATION_NOTE_2026-04-24.md](../../archive_unlanded/historic_intake_originals/branch07/2130_WILSON_TWO_BODY_FINITE_SIZE_REFUTATION_NOTE_2026-04-24.md)
- Lines: 189; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_wilson_two_body_separation_acceleration_finite_size(.py)`; historic runner (unpinned, not in this packet): `scripts/frontier_wilson_two_body_open(.py)`

## Attached evidence (registered with, not as, this claim)

- `docs/WILSON_TWO_BODY_ACTION_REACTION_BOTH_MASSES_NOTE_2026-04-23.md` — Smoke-test head.
- `docs/WILSON_TWO_BODY_SEPARATION_ACCELERATION_SCALING_NOTE_2026-04-24.md` — Middle link: sign robust, magnitude 2.6x off.

## Flags carried

Refutes an active-queue target: the loop-2 both-masses result (CV 3.6%) is downgraded to a per-packet result that does not generalize to the per-separation Newton form.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_refutation
intake_directive: owner_2026-08-05
```

Independent audit still required.
