# The Emergent Dynamical Metric Is Derived at Weak Field: the Record-Density Field Curves the Geometry and Obeys the Retained Poisson Dynamics — the Weak-Field Gravity Sign + Newtonian Gravity Are Derived; Only the Nonlinear EH Remains

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-09
**Type:** the last gravity-sign input — emergent dynamical metric (weak-field closure)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:** [`scripts/emergent_dynamical_metric_weak_field_derived_2026_06_09.py`](../scripts/emergent_dynamical_metric_weak_field_derived_2026_06_09.py) (PASS=5).

## The gate

The bottom-attack ([`GRAVITY_SIGN_BOTTOM_IS_LEADING_ORDER...`](GRAVITY_SIGN_BOTTOM_IS_LEADING_ORDER_DECOUPLES_FROM_LV_REAL_BOTTOM_IS_EMERGENT_METRIC_NARROW_THEOREM_NOTE_2026-06-08.md))
reduced the gravity sign `G>0` to two inputs: (i) leading-order Lorentz isotropy, and (ii) the emergent
**dynamical** metric. Input (i) is now a granted framework primitive — `kinetic_isotropy_primitive`
(`c_t = c_s`, [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md),
on main). This note closes (ii) at weak field.

## Result (the emergent dynamical metric is derived at weak field)

**The metric degree of freedom IS the position-dependent record-density.** A varying record-density `n(x)`
→ a varying local Lieb-Robinson/front speed `v_LR(x)` → a varying light cone = a curved effective metric.
Verified (exact sympy + numpy):

- **(M1) The metric DOF exists, isotropic leading form.** `n(x)` parameterizes `g_00 = -(1+2Φ(x))`
  (`v_LR² = 1+2Φ`); the kinetic-isotropy primitive `c_t=c_s` fixes the spatial part to the isotropic
  `δ_ij` (Minkowski leading class). So the framework **has** a dynamical metric field — the record-density,
  varying in space.
- **(M2) It curves.** For `g = diag(-(1+2Φ(x)),1,1,1)` the linearized Ricci is `R_00 = Φ''(x) = ∇²Φ` —
  **nonzero** for any varying record-density → a genuinely curved emergent geometry.
- **(M3) Geodesic kinematics.** `Γ^x_00 = Φ'(x)`, so a test particle follows the curved metric and
  accelerates `d²x/dτ² = -Φ'(x)` toward **lower** Φ. *Kinematics only* — whether matter makes a **well**
  (Φ<0 → attraction, the gravity **sign**) is the assembled-chain result (reflection positivity: no ghost
  → `G>0`; + the in-review source-positivity / symmetric-mediator analysis), **cited, not derived here**.
  The metric transmits whatever sign the source curvature carries.
- **(M4) Its linearized dynamics is DERIVED.** `∇²Φ = source` is the framework's **retained** weak-field
  Poisson closure ([`GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE`](GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-06-07.md),
  `retained_bounded`: `Φ = G_0 ρ`, `G_0 = (-Δ)⁻¹` the unique linear-response kernel, point source →
  `1/(4πr)`). The Newtonian `1/r` is the Poisson Green's function (`∇²(1/r)=0` for `r>0`, verified
  symbolically). So the weak-field gravitational **dynamics** of the record-density/metric field is
  **derived, not supplied.**

## The landing

**At weak field — the regime where the gravity sign and Newtonian gravity live — the emergent dynamical
metric is derived:** the DOF (record-density), the isotropic leading form (kinetic-isotropy primitive),
the curvature (`R_00=∇²Φ`), the attractive geodesics, and the dynamics (the retained Poisson closure) are
all in hand. Therefore:

> **The weak-field gravity sign `G>0` and Newtonian (`1/r`, attractive) gravity are derived** from
> {R1 graviton massless · R2 Noether stress conservation · R3 healthy λ=1 Regge operator · reflection
> positivity · the kinetic-isotropy primitive · the record-density metric DOF · the retained weak-field
> Poisson dynamics}.

The **only** remaining open gravity frontier is the **nonlinear / strong-field Einstein completion** — the
self-gravity loop diverges ([`GATE_B_POISSON_SELF_GRAVITY`](GATE_B_POISSON_SELF_GRAVITY_NOTE.md) /
`POISSON_SELF_GRAVITY_LOOP_V3`, `retained_no_go`) — a separate, harder frontier that does **not** affect
the weak-field gravity sign or Newtonian gravity.

## What is and is not claimed

- **Is:** the emergent dynamical metric is derived at weak field in the **longitudinal/Newtonian** sector
  — the metric DOF is the record-density (M1), it curves the geometry (M2), test particles follow its
  geodesics (M3, kinematics), and its linearized dynamics is the retained weak-field Poisson/`1/r` closure
  (M4); with the kinetic-isotropy primitive for the isotropic form. **Assembled** with the cited chain
  (RP + source-positivity for the sign; R1–R3 for massless/conservation/TT), the weak-field gravity sign
  `G>0` and Newtonian gravity are derived.
- **Is not:** does **not** derive the **nonlinear / strong-field** Einstein theory (the self-gravity loop
  diverges — `GATE_B`, `retained_no_go` — genuinely open); does **not** re-derive the lattice `1/r` (that
  is the retained #06-07 result, cited); does **not** itself establish R1/R2/R3 (those are the cited chain
  links, several in review). Adds no axiom or fitted value. Weak-field, form/sign level.

## Boundaries (honest)

- **Spin sector.** This note's new contribution is the **longitudinal / Newtonian** metric sector
  (`g_00 = -(1+2Φ)`, the static potential, spin-0-dominated) — the gravity **sign** + `1/r`. This is
  *exactly* the sector the matter generator `W=log|det(D+J)|` **does** couple to (its metric-Hessian is
  rank-1 longitudinal `q̂q̂⊗q̂q̂`,
  [`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING`](UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md)).
  The **transverse-traceless spin-2 graviton** (radiation) is a *separate* sector this note does **not**
  address: the matter-`W` route is **dead** for it (TT in its exact kernel, same note), and the
  geometric-Regge operator is *healthy* on TT (R3, `G^lin(h_TT)=½k²h_TT`) but its status as the framework's
  *actual* graviton dynamics (vs a comparator) is the **open** spin-2-curvature-generator question (TT-kernel
  note). The gravity **sign + Newtonian gravity live entirely in the longitudinal sector** (this note) and
  do **not** require the TT term.
- **The sign is assembled, not re-derived.** The attraction sign `G>0` is the cited reflection-positivity
  + source-positivity chain; this note supplies the metric DOF + curvature + dynamics that the sign acts
  through (M3 is geodesic kinematics only).
- **Weak field only.** This lands the weak-field gravity sign + Newtonian gravity (the regime where they
  live). The full nonlinear GR is the open `GATE_B` frontier.
- **Chain assembly.** Several links (R1 graviton-mass gate, R2 Noether conservation, R3 Regge λ=1, the
  bottom-attack) are proposals in review; this note assembles them with the on-main primitive + the
  retained Poisson closure. The audit lane adjudicates each link.
- **The record-density → metric identification** is the framework's emergent-metric program
  ([`EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS...`](EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md));
  this note makes its dynamical (curving) consequence concrete at weak field.

## Load-bearing inputs

- [`GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-06-07.md`](GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-06-07.md)
  — the retained weak-field Poisson/`1/r` dynamics (M4).
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — the granted `c_t=c_s` isotropic leading form (M1).
- [`EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md`](EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md)
  — the record-density → conformal class (the metric DOF).
- [`GATE_B_POISSON_SELF_GRAVITY_NOTE.md`](GATE_B_POISSON_SELF_GRAVITY_NOTE.md)
  — the nonlinear/strong-field divergence (the one remaining open frontier).
- [`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  — the matter generator's metric-Hessian is rank-1 longitudinal (couples to this note's Newtonian
  sector; TT spin-2 in its kernel → the TT graviton is R3's, not this note's).

## Forbidden-imports check

No PDG / fitted value. The optical-metric curvature `R_00 = ∇²Φ`, the geodesic `Γ^x_00 = Φ'`, and the
harmonicity `∇²(1/r)=0` are standard differential geometry, reproduced in the runner (sympy). The lattice
`1/r` is the retained #06-07 result (cited, not re-derived). The record-density metric DOF is the
framework's emergent-metric program.
