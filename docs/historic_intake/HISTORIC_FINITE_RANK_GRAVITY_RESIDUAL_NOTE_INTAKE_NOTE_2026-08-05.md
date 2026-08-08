# Historic intake: Finite-Rank Strong-Field Source Closure and 4D Einstein-Residual Test

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

The Woodbury identity gives G_W P = G_0 P (I - W G_S)^-1 so any positive-semidefinite multi-site support with off-diagonal mixing still produces an exterior field through one renormalized source q_eff, and the exterior stays exactly harmonic; feeding it directly into the conformastatic ansatz leaves a vacuum Einstein residual |G| ~ 9.85e-2, while the monopole projection of the same field reduces it to 1.52e-4 (a factor ~650).

Original verdict: The exact source foothold now covers a broad finite-rank class, but the remaining gap is sharply why the exact harmonic exterior data reduce to the isotropic-vacuum surface the metric candidate uses.
Scope: Three exact checks pass at machine precision; the bounded checks use shell-averaged fits with ~5.2% relative RMS error (a = 0.3465, b = 0.6312) at sampled exterior probe points.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Woodbury finite-rank residual theorem: any PSD multi-site support reduces to one renormalized harmonic source — the strong-field source model's general form.

## Provenance (pinned)

- Original path: `docs/FINITE_RANK_GRAVITY_RESIDUAL_NOTE.md`
- Source commit: `248edc338c216213ba0087e60b2693a968e0f718`
- git blob: `be69fddfcad4be334e2a7cd36427ca4df8505f9f`
- sha256: `33edd4ec072404e465ef0c5ea4a9d4ada93cb4d66b74090770645b3e39402619`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/463_FINITE_RANK_GRAVITY_RESIDUAL_NOTE.md](../../archive_unlanded/historic_intake_originals/branch02/463_FINITE_RANK_GRAVITY_RESIDUAL_NOTE.md)
- Lines: 170; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_finite_rank_gravity_residual(.py)`

## Attached evidence (registered with, not as, this claim)

- `docs/FINITE_RANK_DTN_CORRECTION_OPERATOR_NOTE.md` — Exact DtN correction operator; family evidence.
- `docs/FINITE_RANK_SUPPORT_ACTIVE_AMPLITUDE_LAW_NOTE.md` — Rank-one amplitude law; closes the scalar ambiguity.

## Flags carried

The direct common-source candidate is NOT a vacuum Einstein solution; only its monopole projection is close, and the reduction is not derived.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
