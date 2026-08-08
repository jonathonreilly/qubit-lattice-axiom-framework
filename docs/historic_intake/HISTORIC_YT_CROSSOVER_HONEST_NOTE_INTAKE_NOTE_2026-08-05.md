# Historic intake: y_t Lane: Honest Crossover Assessment

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: meta
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Declares itself the single authority for the y_t gate: y_t = g_s/sqrt(6) and Z_Y = Z_g at every blocking level are exact, Cl(3) survives blocking, Feshbach projection is verified on the actual staggered Hamiltonian, and V-to-MSbar is computed at 1-loop — but the framework's alpha_V(M_Pl) ~ 0.15 differs from the SM-run alpha_s(M_Pl) ~ 0.019 by 8x, and integrating the continuous 2-loop beta downward gives m_t = 181.6 GeV, 5.0% above 173.0, with lattice step-scaling showing the beta function suppressed ~30x relative to perturbative QCD at L = 4..12.

Original verdict: The lane is NOT closed — the 8x mismatch is real and unresolved and the non-perturbative crossover is bounded, not derived — but it is stronger than before; minimum acceptable status is BOUNDED with one imported input.
Scope: Gate assessment with derived, bounded and not-derived inputs itemized.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The self-declared y_t single-authority meta: exact algebra + NOT-closed verdict + the 8x crossover mismatch + internal alpha_V inconsistency flagged — the lane's April-May authority statement.

## Provenance (pinned)

- Original path: `docs/YT_CROSSOVER_HONEST_NOTE.md`
- Source commit: `81a4efe78660d1bb27dc930c5e7cd8d8f2cc9149`
- git blob: `4e1f2864af35f140ee7e473c113034120e8a34ce`
- sha256: `1846858e13a765092078cb111b119328b75c5e2c687a757aa93bd64ff0c2c2fb`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch07/2168_YT_CROSSOVER_HONEST_NOTE.md](../../archive_unlanded/historic_intake_originals/branch07/2168_YT_CROSSOVER_HONEST_NOTE.md)
- Lines: 96; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_yt_cl3_preservation(.py)`; historic runner (unpinned, not in this packet): `scripts/frontier_wilsonian_eft(.py)`; historic runner (unpinned, not in this packet): `scripts/frontier_yt_boundary_resolution(.py)`; historic runner (unpinned, not in this packet): `scripts/frontier_yt_step_scaling(.py)`

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Quotes alpha_V(M_Pl) ~ 0.15 where sibling notes in the same lane use 0.092-0.093, and its m_t = 181.6 GeV conflicts with the 171.0 GeV that idx 2142 uses to declare the gate closed on the same date.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_meta
intake_directive: owner_2026-08-05
```

Independent audit still required.
