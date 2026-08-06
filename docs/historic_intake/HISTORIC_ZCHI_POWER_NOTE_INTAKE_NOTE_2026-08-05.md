# Historic intake: Z_chi Power in the Hierarchy Formula

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_bounded_theorem
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Resolves the Z_chi power in v = M_Pl exp(-lambda_0/|beta_lambda|): N_eff = 12 Z_chi^2 in terms of y_bare (equivalently 12 with no explicit Z_chi in terms of y_phys), because beta_lambda is a box diagram (y^4, Z_chi^4) while lambda_0 is a self-energy (y^2, Z_chi^2) and the ratio cancels two powers. With alpha_V(M_Pl)=0.092, g_s=1.075, y_bare=0.439 and Z_chi=0.942 (Sigma_1=6), N_eff = 10.64 gives v ~ 226 GeV = 0.92 v_PDG.

Original verdict: DERIVED as an exponent-bookkeeping result, but the numerical output is 8% low (226 vs 246 GeV) and v depends exponentially on Sigma_1 (Sigma_1 = 7.1 would give exactly 246 GeV).
Scope: The correct power of the wavefunction renormalization in the Coleman-Weinberg hierarchy formula.
Escape conditions (negative claims): 2-loop RGE corrections, gauge-boson contributions to V_CW, running of y_t between M_Pl and v, and O(alpha_s) corrections to the lambda_0 matching — all called calculable O(10%) effects.

## Why pulled (supervisor decision, on the record)

Z_chi exponent bookkeeping resolution (v = 226 GeV, 8% low) WITH the severe exponential-sensitivity flag — the April hierarchy note in its honest form.

## Provenance (pinned)

- Original path: `docs/ZCHI_POWER_NOTE.md`
- Source commit: `59bf5717143119081ba18526e51f90e9e14b181e`
- git blob: `e155d5bfa86bb41712365c9dd8a0733b197f2b22`
- sha256: `9d7f70dc8eabf7dc2a76eb58c5c4025ea11954e5349ccab33d41c6050baf9a01`
- Lines: 102; runners named: scripts/frontier_zchi_power.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

The stated sensitivity is severe: v depends exponentially on Sigma_1, and the note observes that the desired 246 GeV corresponds to Sigma_1 = 7.1 rather than the standard staggered 6 — a tuning-shaped escape presented as 'well within the range of lattice estimates'.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
