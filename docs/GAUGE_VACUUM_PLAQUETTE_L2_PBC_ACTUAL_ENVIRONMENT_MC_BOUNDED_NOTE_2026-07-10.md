---
claim_id: gauge_vacuum_plaquette_l2_pbc_actual_environment_mc_bounded_note_2026-07-10
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# L_s=2 PBC Actual Unmarked Wilson Environment Coefficient, Bounded MC

**Date:** 2026-07-10
**Type:** bounded_theorem
**Status:** bounded support note on one explicitly selected finite geometry;
the computation is stochastic and the status is a source-side proposal only.
**Runner:**
`scripts/frontier_gauge_vacuum_plaquette_l2_pbc_environment_mc_bounded_2026_07_10.py`
**Output:**
`outputs/frontier_gauge_vacuum_plaquette_l2_pbc_environment_mc_bounded_2026_07_10.txt`

## Claim-status fields

```yaml
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "the result is a stochastic finite-volume coefficient packet and the temporal stripping bridge remains open"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Result

The finite geometry and exact coefficient definition are the `L_s=2` case of
the linked
[`RESIDUAL_ENVIRONMENT_GEOMETRY_DEPENDENCE_NO_GO_NOTE`](GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_GEOMETRY_DEPENDENCE_NO_GO_NOTE_2026-07-10.md).
Select the standard three-dimensional periodic Wilson spatial complex at
`L_s=2`: 24 positive-direction link variables and 24 oriented plaquette
factors. Mark the `(x,y)` plaquette based at `(0,0,0)` and omit only its
Boltzmann factor. The runner samples all 24 links with the remaining
23-plaquette weight at `beta=6`.

For the marked holonomy `U_m`, the actual environment convolution coefficient
is

```text
rho_lambda^(env,L_s=2,PBC)(6)
  = (1/d_lambda) E_[23-plaquette Wilson measure][conj(chi_lambda(U_m))].
```

Four independent fixed-seed chains, with two hot and two cold starts, give

```text
rho_(1,0)^(env,L_s=2,PBC)(6) = 0.0688943 +/- 0.0047454,
```

where the quoted `+/-` is the nominal standard error across 80 sequential
within-chain batch means. Independence of adjacent batches is not established.
This is a reproducible stochastic diagnostic, not a calibrated or rigorous
confidence interval.

The lower-significance companion estimates are

```text
rho_(1,1) = 0.0047217 +/- 0.0018223,
rho_(2,0) = 0.0031633 +/- 0.0015488.
```

Only the fundamental coefficient passes the declared five-error-unit
nonzero-signal heuristic. The charge-conjugation imaginary parts remain within
the runner's four-error-unit diagnostic.

## Bounded discriminator

The normalized single-link Wilson packet computed by
[`GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md`](GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md)
has

```text
rho_(1,0)^single-link(6) = 0.422531740.
```

The selected actual coupled environment instead gives

```text
rho_(1,0)^(env,L_s=2,PBC)(6) - rho_(1,0)^single-link(6)
  = -0.353637419,
```

or 74.5 declared batch-diagnostic error units. Thus the selected coupled environment is
strongly distinguished from the single-link packet under the declared
bounded diagnostic. This is a discriminating runner for one branch of the
audit blocker: both quantities are computed, and the diagnostic does not
support identifying them by name.

## Diagnostics

- proposal acceptance: `0.6088--0.6102` across four chains;
- fundamental chain means: `0.07362, 0.05413, 0.06715, 0.08068`;
- independent `beta=0` Haar controls are consistent with zero under the
  four-standard-error gate;
- hot/cold chain spread passes the declared bounded diagnostic;
- all six runner checks pass.

The fixed stochastic protocol is part of the claim boundary: four seeds, two
hot and two cold starts, 4000 burn sweeps, 16000 sample sweeps per chain,
thinning by four, proposal step `0.8`, and 20 sequential batches per chain.
The 4/5/8/20-error-unit gates for controls, signal, chain spread, and packet
discrimination are declared heuristic PASS thresholds, not coverage claims.

## Claim boundary

This packet does not supply theorem-grade or all-weight closure. In
particular, it does not establish:

- a rigorous error bar or exact `beta=6` coefficient;
- the `L_s=2` APBC five-unmarked-plaquette staging geometry used by a separate
  gauge-scalar bridge note;
- `L_s=3`, large-volume, or thermodynamic environment data;
- the temporal marked/non-marked mixed-kernel compression theorem;
- equality of the current stripped residual source-sector operator with this
  geometry-indexed environment;
- a plaquette value or source-sector Perron solve.

No integrated-autocorrelation-time estimate, effective-sample-size
certificate, batch-size stability theorem, or rigorous confidence interval is
claimed. No observed plaquette value, fitted selector, generic positive witness, or
single-link coefficient is used as a derivation input. The single-link value
appears only after the environment solve as a bounded discrimination
comparator.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_gauge_vacuum_plaquette_l2_pbc_environment_mc_bounded_2026_07_10.py
```

Expected summary:

```text
SUMMARY: PASS=6 FAIL=0
```
