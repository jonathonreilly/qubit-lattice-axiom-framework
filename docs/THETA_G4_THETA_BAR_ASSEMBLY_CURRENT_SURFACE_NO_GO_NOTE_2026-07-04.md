# Theta G4 Theta-Bar Assembly Current-Surface No-Go Note

**Date:** 2026-07-04
**Type:** no_go
**Claim type:** no_go
**Scope boundary:** current-surface no-go against retiring theta by using the
paired-shift assembly law alone. The fixed-grading assembly theorem supplies
bookkeeping for the invariant combination
`theta_bar = theta_gauge + arg det(M_u M_d)`, but current gauge-side and
mass-side support do not supply the physical values, nontrivial transfer, or
registration needed to set `theta_bar = 0`. This note does not retire theta,
does not set `theta_bar = 0`, does not edit any Tier-A registry, primitive,
axiom, audit verdict, or publication-status surface, and does not claim that
future gauge/mass assembly routes are impossible.
**Audit boundary:** independent audit lane only.
**Primary runner:**
[`scripts/theta_g4_theta_bar_assembly_current_surface_no_go_2026_07_04.py`](../scripts/theta_g4_theta_bar_assembly_current_surface_no_go_2026_07_04.py)

## Target

The theta Tier-A row has two live residual atoms:

```text
gauge_side_winding_account
mass_side_orientation_determinant_readout_bridge
```

The gauge positive-route status split the gauge side into G1-G4. G4 is the
last step:

```text
connect the gauge-side sector functional to the invariant
theta_bar = theta_gauge + arg det(M_u M_d), including the mass-side
determinant channel and anomaly-covariant paired-shift bookkeeping.
```

This block asks whether the current assembly material itself retires theta.
It does not.

## Source Surfaces

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  current Lattice, Qubit, Admissibility, and Record surface, while withholding
  source/action, weighting, update laws, readout-context selection,
  physical-observable identification, and downstream theory consequences.
- [`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md)
  and [`docs/audit/data/tier_a_admissions.json`](audit/data/tier_a_admissions.json)
  keep theta live through the gauge-side winding account and mass-side
  determinant-readout bridge.
- [`STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md`](STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md)
  organizes theta into gauge-side and mass-side residuals and says the
  bookkeeping does not retire the admission.
- [`STRONG_CP_THETA_ZERO_NOTE.md`](STRONG_CP_THETA_ZERO_NOTE.md) is a
  retained-bounded selected-surface theorem for an explicitly theta-free
  Wilson-plus-staggered scalar-mass surface; it does not derive that selected
  surface from the minimal axioms.
- [`THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md`](THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md)
  records G4 as the final physical assembly gate, after G1-G3 and the
  mass-side determinant channel are supplied.
- [`THETA_ASSEMBLY_PAIRED_SHIFT_FIXED_GRADING_MCKEAN_SINGER_REDUCTION_NARROW_THEOREM_NOTE_2026-07-02.md`](THETA_ASSEMBLY_PAIRED_SHIFT_FIXED_GRADING_MCKEAN_SINGER_REDUCTION_NARROW_THEOREM_NOTE_2026-07-02.md)
  proves the fixed-grading paired-shift bookkeeping law and the balanced
  collapse `n = 0`, while explicitly not supplying either side's physical
  value or the nontrivial supplier direction.
- [`THETA_G1_4D_CARRIER_SUPPLY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md`](THETA_G1_4D_CARRIER_SUPPLY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md)
  blocks current-surface supply of the physical 4D closed-nonexact carrier.
- [`THETA_G1_DEFECT_CLOSURE_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md`](THETA_G1_DEFECT_CLOSURE_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md)
  blocks current-surface supply of `dn=0` or defect suppression.
- [`THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md`](THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md)
  blocks current-surface supply of the odd-sensitive phase insertion,
  coefficient, and physical registration.
- [`THETA_MASS_W2_PHYSICAL_REGISTRABILITY_STRETCH_NO_GO_NOTE_2026-07-04.md`](THETA_MASS_W2_PHYSICAL_REGISTRABILITY_STRETCH_NO_GO_NOTE_2026-07-04.md)
  blocks current-surface supply of the mass-side W2 physical registrability
  bridge.
- [`THETA_MASS_DETERMINANT_BRIDGE_RETIREMENT_READINESS_NO_GO_NOTE_2026-07-04.md`](THETA_MASS_DETERMINANT_BRIDGE_RETIREMENT_READINESS_NO_GO_NOTE_2026-07-04.md)
  records that the mass-side determinant stack is not yet a retirement
  authority.

## No-Go Statement

The implication

```text
paired-shift bookkeeping is derived
+ theta_bar is invariant under gauge/mass rephasing
therefore theta_bar = 0 is derived and theta is retired
```

is invalid.

The exact paired-shift law has the form

```text
theta_gauge -> theta_gauge - n alpha
arg det M  -> arg det M  + n alpha
theta_bar  = theta_gauge + arg det M.
```

It proves

```text
theta_bar' = theta_bar.
```

It does not prove

```text
theta_bar = 0.
```

Invariance is a covariance/bookkeeping statement. A value theorem needs the
physical gauge-side sector functional, the physical mass-side determinant
readout, and the correct anomaly-covariant transfer interface. The current
surface has support and no-gos around those pieces, but not all the pieces
themselves.

## Exact Assembly Boundary

The fixed-grading assembly theorem gives `n = 2 tr(eps)`. On the balanced
framework staggered surface, `tr(eps) = 0`, so `n = 0`: the paired-shift law is
exact but trivial. It neither transfers phase between the two sides nor sets
either side's value.

On an unbalanced synthetic surface, `n` can be nonzero and the two shift
factors can cancel exactly. That demonstrates the bookkeeping mechanism. It
still does not make the synthetic grading, the nonzero transfer, or the
background-dependent supplier class a physical theta surface.

Thus both cases fail as theta retirement:

| assembly case | what is supplied | why it does not retire theta |
|---|---|---|
| balanced fixed grading | exact invariance with `n = 0` | no nontrivial transfer or value selection |
| synthetic nonzero grading | exact cancellation with `n != 0` | not a supplied physical gauge/mass theta surface |
| future anomaly-covariant supplier | possible route | not present in current axioms/primitives or current theta packets |

## Dependency Gate

G4 is intentionally downstream. The current route map already says assembly
comes after gauge-side G1-G3 and the mass-side bridge. Those prerequisites are
not currently supplied:

- G1 physical 4D carrier and closedness/suppression remain open;
- G2 physical sector/readout registration remains open;
- G3 phase source, coefficient, and physical action/measure registration
  remain open;
- mass-side W2 physical registrability and action-level determinant entry
  remain open;
- audit/dependency closure of the relevant theta support packets remains
  independent audit-lane work.

Therefore G4 cannot be used as a back door to retire theta.

## What This Moves

| Before | After |
|---|---|
| Paired-shift invariance could be overread as a theta value theorem. | It is classified as exact bookkeeping, not value selection. |
| The balanced `n=0` fixed-grading result could be mistaken for strong-CP closure. | It is pinned as trivial transfer on that surface. |
| Synthetic nonzero transfer could be mistaken for a supplied physical route. | It remains an escape-hatch witness for the supplier class, not a premise. |
| The theta route map had G4 named but not isolated as its own current-surface no-go. | G4 is now blocked until gauge-side G1-G3 and mass-side determinant gates are supplied. |

## What Does Not Move

- Theta is not retired.
- `theta_bar = 0` is not derived.
- The Tier-A registry is not edited.
- No axiom or primitive is changed.
- No audit status or effective status is changed.
- No physical gauge-side theta value is supplied.
- No physical mass-side determinant value is supplied.
- No anomaly-covariant nontrivial supplier is supplied.
- No owner-governance premise is adopted.

## Remaining Live Routes

1. **Gauge-side G1-G3.** Supply the physical 4D carrier, closedness or defect
   suppression, physical sector/readout registration, and odd-sensitive phase
   insertion.
2. **Mass-side bridge.** Supply W2 physical registrability and action-level
   determinant entry for the physical quark mass surface.
3. **Nontrivial anomaly-covariant supplier.** Derive a physical transfer
   supplier beyond fixed balanced grading.
4. **Full theta-bar assembly theorem.** Only after the side gates are supplied,
   prove the invariant interface and the value `theta_bar = 0`.
5. **Owner governance.** Register a narrow gauge/mass assembly premise if the
   framework intentionally treats it as primitive.

## No-Go Discipline Gate

**N1 alternative route enumeration.** Balanced fixed grading, synthetic
nonzero grading, paired-shift covariance, gauge-side G1-G3, mass-side W2,
action-level determinant entry, audit closure, nontrivial supplier, and owner
governance are separated.

**N2 wall independence.** This block targets only G4 assembly. It does not
decide the side gates themselves.

**N3 hidden-wall scan.** The proof imports no neutron-EDM bound, observed
theta value, fitted selector, axion premise, topological-sector primitive,
determinant-channel primitive, anomaly supplier primitive, audit verdict, or
registry edit.

**N4 residual matching.** The result matches the theta registry: both
gauge-side winding and mass-side determinant-readout residuals remain live.

**N5 proven surface.** Proven here is a current-surface no-go against using
assembly bookkeeping alone as theta retirement. This is not a terminal no-go
against future full assembly theorems.

**N6 partial closure.** The block sharpens the order of operations: do not use
G4 until the physical side gates are supplied.

**N7 steelman.** A reviewer can say the paired-shift law is exactly the right
invariant interface. Correct. This block preserves it and only rejects treating
invariance as a value theorem.

**N8 cross-cycle echo.** This mirrors AC and R-eta: a correct normal form or
bookkeeping identity is not the missing physical readout/action bridge.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/theta_g4_theta_bar_assembly_current_surface_no_go_2026_07_04.py
```

Expected close: `FAIL=0` with at least 110 checks.
