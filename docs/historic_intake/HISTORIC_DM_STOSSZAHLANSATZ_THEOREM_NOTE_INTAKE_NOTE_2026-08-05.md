# Historic intake: Lattice Stosszahlansatz Theorem

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_theorem
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

On Z^3_L with M = -Delta_L + m^2 the two-particle density satisfies |rho_2 - rho_1 rho_1| <= 2 C^2 exp(-2 mu |x-y|) with mu = 0.9 ln(1 + m^2/6) and C = 1/(m^2 - 6(e^mu - 1)), proved in five self-contained steps (spectral gap -> lattice Combes-Thomas decay -> Wick cluster property -> thermodynamic limit -> freeze-out), giving error < 10^-45000 at x_F = 25.

Original verdict: PROVED as a self-contained lattice theorem replacing the cited linked-cluster/propagation-of-chaos arguments, but it closes only the Stosszahlansatz sub-gate, not the relic mapping lane.
Scope: Free (Gaussian) field only - Wick's theorem is exact there; the interacting case needs spectral-gap persistence under weak coupling, and freeze-out density is a bounded cosmological input.


## Why pulled (supervisor decision, on the record)

Self-contained lattice Stosszahlansatz theorem (explicit decay constants, five steps) honestly scoped to the free theory — a real theorem replacing cited arguments.

## Provenance (pinned)

- Original path: `docs/DM_STOSSZAHLANSATZ_THEOREM_NOTE.md`
- Source commit: `56d8565f1199dd1eb91f4329941e416a8662d7d0`
- git blob: `769b9fc1b97ed4d997806a0283a5425ff9386243`
- sha256: `d2ff19121ed25442119c2b54118225067aa2d581aaf2a11250d58f10e3290c36`
- Lines: 165; runners named: scripts/frontier_dm_stosszahlansatz_theorem.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Explicitly proved only for the free Gaussian theory; the interacting extension is expected but not proved.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
