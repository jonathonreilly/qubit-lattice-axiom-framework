# Historic intake: Hadamard Basis: Simultaneous T_mu Eigenbasis + S_3 Label Action

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

The Hadamard basis |psi_s> = (1/sqrt8) sum_alpha (prod_mu s_mu^{alpha_mu})|alpha> simultaneously diagonalizes the cube shifts (S_mu|psi_s> = s_mu|psi_s>) and, via the intertwiner, the lattice translations on BZ corners; Q = S_1S_2S_3 has eigenvalue s_1s_2s_3 with rank-4 projectors Pi_pm, S_3 acts by label permutation U(pi)|psi_s> = |psi_{pi.s}>, and hw-parity is S_3-invariant because s_1s_2s_3 is symmetric.

Original verdict: Gives a unified block-diagonalization in which each hw-parity block is a 4-dimensional S_3-invariant subspace.
Scope: Pure algebra on C^8 and the BZ-corner subspace of C^{L^3}; a composition result, not new physics.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Hadamard/S3 composition theorem: simultaneous diagonalization of shifts and translations — grind-program exact infrastructure.

## Provenance (pinned)

- Original path: `docs/HADAMARD_S3_COMPOSITION_NOTE.md`
- Source commit: `ccc70f8012f77eb5d62b84c3af12c10a1daff913`
- git blob: `bf1b00d81851e72a44595cfe67446525002d7a18`
- sha256: `87ae37cc40b80f1255dea73ecb9fb247f45916f4f21c573f6955d5f5fbc3859e`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/660_HADAMARD_S3_COMPOSITION_NOTE.md](../../archive_unlanded/historic_intake_originals/branch02/660_HADAMARD_S3_COMPOSITION_NOTE.md)
- Lines: 63; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_hadamard_s3_composition(.py)`

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
