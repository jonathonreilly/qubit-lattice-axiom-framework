# The Emergent Dynamical Metric at Weak Field: the Longitudinal Sector's GR Structure Is Verified, and the Weak-Field Gravity Sign Reduces to the (Conditional) Poisson Closure + the (Unaudited) Source-Positivity Sign

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-09
**Type:** the last gravity-sign input — emergent dynamical metric (weak-field, longitudinal sector)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:** [`scripts/emergent_dynamical_metric_weak_field_derived_2026_06_09.py`](../scripts/emergent_dynamical_metric_weak_field_derived_2026_06_09.py) (PASS=5).

## The gate

The bottom-attack ([`GRAVITY_SIGN_BOTTOM_IS_LEADING_ORDER...`](GRAVITY_SIGN_BOTTOM_IS_LEADING_ORDER_DECOUPLES_FROM_LV_REAL_BOTTOM_IS_EMERGENT_METRIC_NARROW_THEOREM_NOTE_2026-06-08.md))
reduced the gravity sign `G>0` to two inputs: (i) leading-order Lorentz isotropy, and (ii) the emergent
**dynamical** metric. Input (i) is now a granted framework primitive — `kinetic_isotropy_primitive`
(`c_t = c_s`, [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md),
on main). This note examines (ii) at weak field: it **verifies the longitudinal-sector GR structure** and
**reduces** the weak-field sign to its remaining named links — it does **not** claim an unconditional
derivation.

## What is verified (the GR structure of the longitudinal sector)

The framework's emergent-metric program **posits** the metric degree of freedom to be the
position-dependent record-density `n(x)`: a varying `n(x)` → a varying local Lieb-Robinson/front speed
`v_LR(x)` → a varying light cone = a curved effective metric. *Caveat (M1 below): that posit rests on an
unaudited note whose curving step is "named, not built."* Given the posit, the differential geometry is
exact (sympy + numpy):

- **(M1 — posit, not in-hand) The metric DOF; isotropic leading form.** The program posits `n(x)` →
  `g_00 = -(1+2Φ(x))` (`v_LR² = 1+2Φ`); the kinetic-isotropy primitive `c_t=c_s` fixes the spatial part to
  the isotropic `δ_ij` (Minkowski leading class). **Status:** the cited EMERGENT_METRIC note is
  **unaudited** and states the varying-record-density-curves-geometry step is *named, not built* — so M1 is
  the program's **posit**, not a derived in-hand input.
- **(M2 — verified) It curves.** For `g = diag(-(1+2Φ(x)),1,1,1)` the linearized Ricci is
  `R_00 = Φ''(x) = ∇²Φ` — **nonzero** for any varying record-density → a genuinely curved geometry.
  *(Standard GR; reproduced exactly in the runner.)*
- **(M3 — verified, kinematics) Geodesics.** `Γ^x_00 = Φ'(x)`, so a test particle follows the curved
  metric and accelerates `d²x/dτ² = -Φ'(x)` toward **lower** Φ. *Kinematics only* — whether matter makes a
  **well** (Φ<0 → attraction, the gravity **sign**) is **not** decided here; it is the separate
  source-positivity + reflection-positivity question (see below). The metric transmits whatever sign the
  source curvature carries.
- **(M4 — conditional) The linearized dynamics is the framework's weak-field Poisson closure,
  conditionally.** `∇²Φ = source` is [`GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE`](GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-06-07.md).
  **Status (ledger-checked): `audited_renaming`, `chain_closes: false`** — it derives `Φ = G_0 ρ`,
  `G_0=(-Δ)⁻¹` → `1/(4πr)` **only after the response identity `φ=G₀ρ` is imposed**; the physical
  source-coupling/response theorem is the auditor's flagged residual. The Newtonian `1/r` *is* the Poisson
  Green's function (`∇²(1/r)=0` for `r>0`, verified symbolically here). So the weak-field dynamics is the
  framework's **conditional** closure, **not** an unconditional derivation.

## The reduction (honest landing)

Assembling the verified GR structure (M2, M3) under the posited DOF (M1) and the conditional dynamics (M4):

> **The weak-field gravity sign `G>0` and Newtonian (`1/r`) gravity REDUCE to**
> {the verified longitudinal GR structure (M2 curvature, M3 geodesics) · the **posited** record-density
> metric DOF (M1, unaudited program) · the **conditional** weak-field Poisson closure (M4,
> `audited_renaming`) · the **unaudited** source-positivity / reflection-positivity **sign** · R1–R3
> (in review) · the kinetic-isotropy primitive}.
> This **assembles** the weak-field sign from those named links and **locates** each remaining gap; it is
> **not** an unconditional derivation.

So the bottom-attack's input (ii) is **not closed** — it is **mapped**: the longitudinal-sector geometry
is standard GR (verified), and the weak-field sign now rests on exactly four named, individually-tracked
items (the unaudited posit M1, the conditional closure M4, the unaudited sign, the in-review R1–R3) plus
the on-main primitive. The **nonlinear / strong-field** Einstein completion is separately open — the
self-gravity loop diverges ([`GATE_B_POISSON_SELF_GRAVITY`](GATE_B_POISSON_SELF_GRAVITY_NOTE.md) /
`POISSON_SELF_GRAVITY_LOOP_V3`, `retained_no_go`).

## What is and is not claimed

- **Is:** in the **longitudinal/Newtonian** sector, the optical-metric GR structure is verified — the
  metric curves (`R_00=∇²Φ`, M2) and test particles follow its geodesics (M3) — and the weak-field gravity
  sign + Newtonian `1/r` **reduce** to the named links above (M1 posit · M4 conditional closure · unaudited
  sign · in-review R1–R3 · primitive). The longitudinal-vs-TT scoping is faithful to the TT-kernel note.
- **Is not:** does **not** unconditionally derive the weak-field gravity sign or Newtonian gravity (the DOF
  posit is unaudited; the Poisson closure is `audited_renaming`/`chain_closes:false`; the sign-link is
  unaudited; R1–R3 are in review); does **not** derive the **nonlinear/strong-field** Einstein theory
  (`GATE_B`, `retained_no_go`); does **not** re-derive the lattice `1/r` (the conditional #06-07 result,
  cited); does **not** address the **TT spin-2 graviton** (separate sector, below). Adds no axiom or
  fitted value.

## Boundaries (honest)

- **Spin sector.** The verified structure is the **longitudinal / Newtonian** sector (`g_00 = -(1+2Φ)`,
  the static potential, spin-0-dominated) — the gravity **sign** + `1/r`. This is *exactly* the sector the
  matter generator `W=log|det(D+J)|` **does** couple to (its metric-Hessian is rank-1 longitudinal
  `q̂q̂⊗q̂q̂`,
  [`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING`](UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md),
  `audited_clean`). The **transverse-traceless spin-2 graviton** (radiation) is a *separate* sector this
  note does **not** address: the matter-`W` route is **dead** for it (TT in its exact kernel, same note),
  and the geometric-Regge operator is *healthy* on TT (R3, `G^lin(h_TT)=½k²h_TT`) but its status as the
  framework's *actual* graviton dynamics (vs a comparator) is the **open** spin-2-curvature-generator
  question (TT-kernel note).
- **The sign is a separate, unaudited question.** The attraction sign `G>0` is the source-positivity +
  reflection-positivity chain (`g_newton_born_as_source_positive`, **unaudited**); this note supplies the
  metric structure the sign acts through (M3 is geodesic kinematics only), not the sign itself.
- **The DOF identification is a posit.** "Record-density = metric DOF" is the framework's emergent-metric
  program ([`EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS...`](EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md),
  **unaudited**); that note states the curving step is *named, not built*. This note makes the program's
  consequence concrete (the GR structure) but does not build the posit.
- **Weak field only.** The full nonlinear GR is the open `GATE_B` frontier.
- **Chain assembly.** Several links (R1 graviton-mass gate, R2 Noether conservation, R3 Regge λ=1, the
  bottom-attack) are proposals in review. The audit lane adjudicates each link.

## Load-bearing inputs

- [`GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-06-07.md`](GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-06-07.md)
  — the **conditional** weak-field Poisson/`1/r` dynamics (M4; `audited_renaming`, `chain_closes:false`).
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — the granted `c_t=c_s` isotropic leading form (M1).
- [`EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md`](EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md)
  — the record-density → conformal class **posit** (M1; **unaudited**; curving step named-not-built).
- [`GATE_B_POISSON_SELF_GRAVITY_NOTE.md`](GATE_B_POISSON_SELF_GRAVITY_NOTE.md)
  — the nonlinear/strong-field divergence (separately open).
- [`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  — the matter generator's metric-Hessian is rank-1 longitudinal (couples to this note's Newtonian sector;
  TT spin-2 in its kernel → the TT graviton is R3's, not this note's).

## Forbidden-imports check

No PDG / fitted value. The optical-metric curvature `R_00 = ∇²Φ`, the geodesic `Γ^x_00 = Φ'`, and the
harmonicity `∇²(1/r)=0` are standard differential geometry, reproduced in the runner (sympy). The lattice
`1/r` is the conditional #06-07 result (cited, not re-derived). The record-density metric DOF is the
framework's (unaudited) emergent-metric program posit.
