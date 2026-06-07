# Continuous Gauge Dynamics — Admission Map (Research-Map Note)

**Date:** 2026-06-07
**Type:** research map / meta
**Claim type:** meta
**Status authority:** independent audit lane only. This is a backward-looking
map that catalogs the current decomposition of the continuous-gauge-dynamics
lane; it sets no audit verdict, predicts none, and introduces no new axiom, no
new admitted input, and no fitted/imported value. Each row points to its
existing source authority and that note's own status.
**Purpose:** record, in one place, the decomposition of "derive continuous
gauge dynamics" into a derived form-class + a precise, classified residual, so
the lane is not re-attacked as a single undifferentiated wall.

## The decomposition

"Derive continuous gauge dynamics" is **not one wall**. It factors as:

| piece | status | source authority |
|---|---|---|
| **form-class** (gauge-invariant-local: plaquette + covariant hopping + mass) | **derived — modulo two un-derived bridges** | [`DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md`](DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md) |
| **R_form** (which magnetic functional in the class) | **irreducible admission (import-bridge)** | [`RECORD_DOES_NOT_SELECT_MAGNETIC_GAUGE_FUNCTIONAL_NO_GO_NOTE_2026-06-07.md`](RECORD_DOES_NOT_SELECT_MAGNETIC_GAUGE_FUNCTIONAL_NO_GO_NOTE_2026-06-07.md), [`BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md`](BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md) |
| **R_coupling** (the bare gauge coupling β = 2N_c/g_bare²) | **not an admission** — vacuous rescaling convention (`β·g²` rescaling-invariant); not in the Tier-A registry | [`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md) |
| **continuum-orbit** (the lattice → continuum a→0 limit / continuum gauge orbit) | **not needed** — the framework is a permanent fixed Planck-scale lattice; emergent Lorentz is a fixed-a low-energy statement; no continuum limit is required | [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) |
| **R_value** (⟨P⟩(β=6)) | **a calculation, not an admission** — unique in principle; reached today by Monte-Carlo; analytically compute-walled (treewidth-29) | [`BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md) |

## The admission count

Within the derived form-class, the residual that is a genuine *admission* (not a
convention, not a calculation, not an unnecessary import) is **R_form alone**.
The two bridges the form-derivation rests on — the two-endpoint Gauss-generator
structure and the quantum-Darwinism record reading — are themselves
un-derived import-bridges. So:

- **N = 1** irreducible admission within the derived class (R_form), **or**
- **{R_form + 2 form-class bridges} = 3 import-bridges** if the two un-derived
  bridges of the form-derivation are counted as admissions.

Either way: **no new dynamics axiom is required.** The residual is a functional
choice (R_form) plus two derivation-bridges, on top of a compute-walled
calculation (R_value). The two dimensionless Tier-A admissions of the whole
framework (the flavor gate `AC_φλ` and `θ`) are **not** gauge-dynamics
admissions, and the bare coupling is **not** among them.

## Load-bearing caveats (must travel with any use of this map)

1. **"Form derived" is modulo two un-derived bridges.** The two bridge notes
   ([`TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md`](TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md),
   [`RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`](RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md))
   state in their own text that they do not derive their bridges from
   `{Lattice, Quantum, Record}`. The qualifier is load-bearing.
2. **The supporting stack is unaudited.** The form-class note, both bridge
   notes, and the R_form no-go are all currently pending independent audit; the
   map asserts no audit status.

## The one open derivation lever

R_form is a theorem-grade obstruction (the convolution-semigroup
counter-witness) and R_value is a pure compute wall — neither is reducible by
reasoning. The single place where *derivation* (not import, not compute) is
still live is **discharging a form-class bridge**: deriving the two-endpoint
Gauss-generator structure (and the quantum-Darwinism record reading) from
`{Lattice, Quantum, Record}` would convert "form derived modulo two bridges"
into "form derived."

## Provenance

`Lattice (Z³) + Quantum (qubit M₂(ℂ)) + Record`. No new axiom, no new admitted
input, no fitted/imported value. Comparator values (the `SU(3)` `β=6` plaquette
expectations) are used only as cross-checks, never as derivation inputs.
