# Historic intake: DM Thermodynamic Closure: Continuum Limit Dependency Resolved

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

Shows the three claimed 'continuum limit' dependencies (C(L) -> pi, rho ~ T^4, x_F convergence) are thermodynamic limits (N -> infinity at fixed a = l_Planck), not the forbidden continuum limit a -> 0; eigenvalue counting converges to the Weyl/BZ prediction at ratio 0.980 for L = 16 with rate O(L^-1.84), and finite-size corrections at N ~ 10^185 are O(10^-120).

Original verdict: Resolves an internal documentation inconsistency across DM_SIGMA_V_LATTICE and DM_RELIC_GAP_CLOSURE, but the lane stays BOUNDED because of the g_bare = 1 self-dual-point assumption.
Scope: Relies on the cubical lattice being a PL 3-manifold plus Moise 1952 to apply Weyl's law, and on the taste-physicality theorem forbidding a -> 0.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Limit-language correction across the lane: the claimed continuum dependencies are thermodynamic limits at fixed a — repairs a documentation inconsistency with real content.

## Provenance (pinned)

- Original path: `docs/DM_THERMODYNAMIC_CLOSURE_NOTE.md`
- Source commit: `877af207a69ad71993b44b19ca4c4c24a5aac8e5`
- git blob: `dfc74f163c706e1a0b8268a49a79169f3560407b`
- sha256: `0cff0f7aa89b453633f9c281a14a85c4dc701ee57ea23c2fc35cbe459dffba7b`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/408_DM_THERMODYNAMIC_CLOSURE_NOTE.md](../../archive_unlanded/historic_intake_originals/branch02/408_DM_THERMODYNAMIC_CLOSURE_NOTE.md)
- Lines: 250; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_dm_thermodynamic_closure(.py)`

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded
intake_directive: owner_2026-08-05
```

Independent audit still required.
