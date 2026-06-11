# The Spin-2-Coupled Two-Derivative Curvature Generator Named by the Polarization-Frame Gate Exists on the Flat Atlas — the Landed Geometric Rows Supply It, and the Gate's Frame-Ambiguity Obstruction Fails for It

**Date:** 2026-06-10
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_universal_gr_spin2_curvature_generator_supplied_2026_06_10.py`](../scripts/frontier_universal_gr_spin2_curvature_generator_supplied_2026_06_10.py) (PASS=6 FAIL=0)
**Runner cache:** [`logs/runner-cache/frontier_universal_gr_spin2_curvature_generator_supplied_2026_06_10.txt`](../logs/runner-cache/frontier_universal_gr_spin2_curvature_generator_supplied_2026_06_10.txt)

## The gate (engaged at its own stated boundary)

[`UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_ATTEMPT.md`](UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_ATTEMPT.md)
(`open_gate`) records the direct universal route's exact obstruction: the scalar observable generator +
`3+1` lift + unique symmetric quotient kernel do **not** supply a canonical channel split — *"two valid
3+1 polarization frames related by a spatial rotation yield different localized channel coefficients
for the same kernel"* (its runner's `frame_delta = 6.767e-02`); only the rank-2 scalar-channel
projector is canonical. Its named **minimal extra structure**: a covariant polarization-frame / projector
bundle *"required to turn the exact quotient kernel into a canonical Einstein/Regge dynamics law"*
(same wall as [`UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md`](UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md)).
The landed TT-kernel row
([`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING...`](UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md))
re-scoped the missing object to *"a spin-2-coupled, two-derivative (curvature) observable generator"*
and proved the scalar-`W` route cannot supply it (per-mode metric Hessian rank-1 longitudinal, TT in
its exact kernel).

## The supply (landed rows) and what this note verifies

The cubic-Coxeter Regge second variation on the framework's own `Z³ × Z_τ` complex **is** such a
generator: `δ²S_R = −½ × (linearized EH pairing) + O(k⁴)`, exactly and isotropically
([`CUBIC_COXETER_REGGE_SECOND_VARIATION...`](CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md),
[`...3PLUS1_TICK_EXTENSION...`](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md)),
with the channel weights and multiplier structure derived
([`UNIVERSAL_GR_3PLUS1_CONSTRAINT_MULTIPLIER_STRUCTURE...`](UNIVERSAL_GR_3PLUS1_CONSTRAINT_MULTIPLIER_STRUCTURE_DERIVED_FIBER_METRIC_BOUNDED_THEOREM_NOTE_2026-06-09.md))
and the EH class forced by embedding-independence + locality
([`CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION...`](CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_NARROW_THEOREM_NOTE_2026-06-10.md)).
This note verifies the **gate's own criteria** against that landed object (machinery inlined from the
landed 3+1 runner; runner-verified):

1. **Two-derivative (F1).** The generator's metric-sector form vanishes at `k=0` exactly
   (`|Q_h(0)| = 1.8e-15`; constant metric perturbations re-flatten) and is `O(k²)` at leading order
   (`|Q_h(2k)|/|Q_h(k)| = 3.999999`).
2. **Spin-2-coupled, with the scalar-`W` contrast (F2).** Both TT channels are nonzero at `O(k²)`
   (the landed `−¼k²` values, equal), while the scalar-`W` per-mode Hessian — reproduced in-runner —
   has the TT block in its **exact** kernel (overlap `3e-30`): the geometric route supplies what the
   scalar route provably cannot.
3. **The gate's obstruction fails for the new object (F3).** Under random SO(4) frame rotations, the
   generator's form at the rotated momentum equals `c × M_EH(Rk)` with **the same single constant
   `c = −½`** (spread `2e-8` over six random frames; residuals `4e-8` — the `O(k⁴)`/numerical floor).
   Where the scalar route had `frame_delta = 6.8e-2`, here the localized channel data **collapses to
   one frame-covariant constant per momentum**.
4. **Canonical split, all channels (F4).** The frame-invariant channel weights (the form's spectrum in
   the tensor metric) agree between rotated frames to `2.5e-8` — the *"only the scalar channel is
   canonical"* limitation is superseded: every channel weight is a frame-independent scalar per
   momentum.
5. **The flat-atlas target reached (F5).** The generator's localization **is** the linearized
   Einstein/Regge law (`Q_h = c × EH pairing`, one constant, across tick, space, and mixed momenta):
   *"a canonical Einstein/Regge dynamics law"* exists on the flat atlas **without adding a bundle
   primitive**. The geometric action supplies the curvature generator directly, bypassing the scalar-`W`
   localization problem.

## What is and is not claimed

- **Is:** the gate's named minimal missing object exists on the **flat `Z³ × Z_τ` atlas at the
  linearized level** — it is the landed geometric rows' second variation — and the gate's exact
  obstruction (frame-dependent localized channel coefficients) **fails** for it (F1–F5, all
  runner-verified against the landed machinery).
- **Is not:** does **not** retag the gate row or any blocker row (status authority: audit lane); does
  **not** claim the `PL S³ × R` version (the gate's own atlas) — the S³ transplant of the geometric
  construction is named open; does **not** overturn the scalar-`W` facts (the bundle non-canonicity
  and the TT-kernel are true properties of that route, reproduced in F2 — the resolution is that the
  universal lane's tensor sector need not route through scalar-`W`); does **not** address the
  nonlinear completion; adds no axiom, no primitive, no fitted value.

## Boundaries (honest)

- **Flat atlas, linearized.** The gate sits on `PL S³ × R`; this supply is the flat-background
  statement. The S³ transplant (curved-background Regge second variation on the sphere complex) and
  the nonlinear completion remain the gate-side residuals.
- **Frame covariance is verified at the `O(k²)` level** (residuals at the `O(k⁴)` floor); the `O(k⁴)`
  lattice fingerprint is the landed fingerprint row's territory (cubic-anisotropic there, as it must
  be on a lattice).
- Any dictionary from edge-length degrees of freedom to matter-correlation data is separate and not
  consumed here. The dynamics' embedding-independence provenance remains the named open item of the
  action-selection row.

## Load-bearing inputs

- [`UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_ATTEMPT.md`](UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_ATTEMPT.md) — the open gate whose named minimal object this note supplies (flat atlas).
- [`UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md`](UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md) — the blocker statement of the same wall.
- [`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md) — the re-scope to the spin-2 curvature generator + the scalar-`W` no-go (reproduced in F2).
- [`CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md`](CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md) and [`CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md`](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md) — the landed generator (machinery inlined and re-verified here).
- [`UNIVERSAL_GR_3PLUS1_CONSTRAINT_MULTIPLIER_STRUCTURE_DERIVED_FIBER_METRIC_BOUNDED_THEOREM_NOTE_2026-06-09.md`](UNIVERSAL_GR_3PLUS1_CONSTRAINT_MULTIPLIER_STRUCTURE_DERIVED_FIBER_METRIC_BOUNDED_THEOREM_NOTE_2026-06-09.md) — the derived channel weights and multiplier structure.
- [`CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_NARROW_THEOREM_NOTE_2026-06-10.md`](CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_NARROW_THEOREM_NOTE_2026-06-10.md) — the EH-class forcing (why the localization is canonical).
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) — the `c_t = c_s` structural grant for the tick direction.

## Forbidden-imports check

No PDG / fitted / literature value is consumed. The generator, the comparator operator, the rotation
representations, and all residuals are computed in-runner from the landed complex's geometry and the
curvature definitions; the gate's `frame_delta = 6.767e-02` is quoted from its own note as the
contrast, not consumed by any check.
