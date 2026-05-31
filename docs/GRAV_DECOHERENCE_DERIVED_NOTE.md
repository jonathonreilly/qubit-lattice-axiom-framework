# Gravitational Decoherence Rate -- Conditional Penrose-Diosi/BMV Companion

**Status:** bounded companion
**Claim type:** bounded support note
**Type:** conditional / support
**Date:** 2026-04-13
**Script:** `scripts/frontier_grav_decoherence_derived.py`
**Depends on:** `frontier_newton_derived.py` (formal lattice Green kernel support), `frontier_dm_coulomb_from_lattice.py` (subtracted Fourier integral)

```yaml
actual_current_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "supplied Penrose-Diosi/BMV numerics with lattice form-factor diagnostics"
hypothetical_axiom_status: null
admitted_observation_status: "uses admitted SI constants, BMV/NV geometry choices, and the current Planck-scale lattice pin"
proposal_allowed: false
proposal_allowed_reason: "the physical source/readout, G-normalization, Penrose-Diosi rate law, and BMV geometry bridge remain supplied rather than retained derivations"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

**Source-note boundary:** this note is not an axioms-only derivation of
gravitational decoherence. It is a bounded companion calculation for a supplied
Penrose-Diosi/BMV model, with framework-adjacent lattice Green form-factor
diagnostics.

**Current publication disposition:** bounded companion only. Not on the
retained flagship claim surface.

---

## Conditional Calculation Chain

Given the following supplied premises:

1. a conditional/formal lattice-Poisson authority for `(-Delta_lat) phi = rho`;
2. a supplied physical mass-source/readout rule `phi(r) = -G_N m G_lat(r - x)`;
3. a supplied SI normalization for `G_N`, `hbar`, and the physical lattice
   spacing;
4. a supplied Penrose-Diosi field-distinguishability-to-rate bridge
   `gamma = E_G / hbar`; and
5. supplied BMV/NV geometry and wavepacket conventions,

the runner evaluates the companion numerical packet:

- the lattice Green ratio `G_lat(r) / G_cont(r)` on the on-axis `Z^3` sample;
- the point-particle Penrose-Diosi rate `G_N m^2 / (hbar delta_x)`;
- Gaussian/sphere geometry variants used in the legacy note;
- BMV phase and decoherence-budget diagnostics; and
- a Planck-pin extrapolation showing that the lattice form-factor correction is
  negligible at the listed micrometer separations once the physical lattice pin
  is supplied.

This chain supports conditional phenomenology only. It does not close the
bridge from the minimal framework primitives to physical gravitational
decoherence.

---

## Key Conditional Results

### Decoherence Rates

These values are read as conditional on the supplied Penrose-Diosi/BMV packet,
not as retained framework predictions.

| Configuration | m (kg) | delta_x | gamma (Hz) | tau (s) | Phi_ent (rad) |
|--------------|--------|---------|------------|---------|---------------|
| Conservative NV | 10^{-14} | 1 um | 52.6 | 0.019 | 6.3e-3 |
| BMV original | 10^{-14} | 250 um | 0.253 | 3.95 | 12.4 |
| Aspelmeyer tabletop | 10^{-12} | 10 um | 5.7e4 | 1.8e-5 | 1.3e3 |
| Optimistic next-dec | 10^{-10} | 1 um | 7.6e9 | 1.3e-10 | 5.1e7 |

### Lattice Form Factor (3D, on-axis)

| r (lattice units) | F = G_lat / G_cont | |F - 1| |
|---|---|---|
| 1 | 1.030 | 3.0% |
| 5 | 0.990 | 1.0% |
| 10 | 1.014 | 1.4% |
| 20 | 1.006 | 0.6% |
| 30 | 1.004 | 0.4% |

The form-factor table is retained here only as a diagnostic snapshot of the
runner's finite-grid calculation. It should not be cited as a proof of an
unconditional continuum limit or as a retained physical self-energy
normalization. The prior prose claim that the on-axis table is below 1% for
all `r >= 5` is not used as a support claim because the displayed `r = 10`
entry is about 1.4%.

### Lattice Correction at Physical Scales

Conditional on the current Planck-scale package pin `a = l_Planck =
1.616e-35 m`, the runner extrapolates

    delta_x = 1 um:   delta_x/a = 6.2e28,  |F-1| ~ 6.5e-58
    delta_x = 250 um: delta_x/a = 1.5e31,  |F-1| ~ 10^{-62}

This is a conditional scale estimate. The Planck lattice pin and the physical
coupling/readout are not supplied by this note.

---

## BMV Feasibility Readout

At BMV original parameters (m = 10 pg, delta_x = 250 um, d = 200 um, T = 2 s),
conditional on the supplied geometry/readout model:

- **Decoherence rate:** `gamma_grav = 0.253 Hz`
- **Decoherence budget:** `gamma_total < 1/T = 0.5 Hz`
- **Gravity uses 50.6% of the budget** under that model
- **Entanglement phase:** `Phi = 12.4 rad`

The arms cross in the listed geometry (`d - delta_x = -50 um`), so the legacy
calculation applies a supplied `10 um` minimum-approach cutoff. This cutoff is
part of the companion model, not a framework-native consequence.

---

## Born-Rule Cross-Constraint Status

The runner preserves the historical beta-to-gamma sensitivity calculation as
conditional phenomenology only:

    gamma(beta) = gamma_0 * [1 + (beta - 1) + O((beta - 1)^2)]

This note does not derive that cross-constraint from the current framework
surface. A future retained bridge would need to separately prove the relevant
propagator-linearity/readout relation and its mapping to a gravitational
decoherence rate.

---

## Open Imports That Remain Load-Bearing

- retained derivation of the closure identity `L^{-1} = G_0` from the minimal
  framework primitives;
- physical mass-source/readout rule for a superposed matter configuration;
- gravitational coupling and SI unit normalization;
- Penrose-Diosi field-distinguishability-to-rate bridge;
- BMV/NV geometry, wavepacket, and cutoff conventions;
- Planck-scale lattice spacing authority for the physical `a`;
- Born-rule beta-to-gamma cross-constraint; and
- corrected self-energy/form-factor normalization if this lane is later
  promoted beyond companion numerics.

---

## Verification

The script runs the numerical checks plus source-boundary checks. The source
checks require the conditional/support classification above and reject the old
axioms-only wording.

## Audit Dependency Repair Links

This graph-bookkeeping section records explicit dependency links named by a
prior conditional audit so the audit citation graph can track them. It does not
promote this note or change the audited claim scope.

- [newton_law_derived_note](NEWTON_LAW_DERIVED_NOTE.md)
- [gravity_full_self_consistency_note](GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md)
