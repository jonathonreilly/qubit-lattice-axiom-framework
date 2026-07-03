# The 3+1 Tick Extension of the Retained Cubic-Coxeter Complex: the Regge Second Variation Yields the Lambda-One Kinetic Fiber Metric, the Multiplier Structure, and the Comparator Signs Geometrically — Isotropically Across Tick-Mixed Directions

**Date:** 2026-06-09
**Type:** bounded_theorem
**Scope:** 3+1 tick-extension Regge second-variation theorem on the supplied
`Z^3 x Z_tau` path complex, with edge-length variables and action selection
left explicit.
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py`](../scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py) (PASS=10 FAIL=0)
**Runner cache:** [`logs/runner-cache/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.txt`](../logs/runner-cache/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.txt)

## Framing (3D+1 — the framework's structure, kept explicit)

The Lattice axiom supplies **space = `Z³` only**; time is the **emergent record tick**. The complex
built here is `Z³ × Z_τ`: the path (Kuhn-chain) simplicial complex on the 4-cell whose **constant-tick
spatial face carries exactly the retained six-tetrahedra body-diagonal chain** of
[`CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md`](CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md)
(verified combinatorially, slice-consistency check) — i.e. the **tick extension
of the retained row**, not a new spatial
structure and not a fundamental 4D lattice. The tick edge is grained on the same footing as the spatial
edge per the registered
[`kinetic_isotropy_primitive`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) (`c_t = c_s`, structural
grant only; nothing beyond it is used). The Euclidean signature is the OS0 surface; the tick **scale**
is not derived (the retained
[`POST_RECORD_CLOCK_RATE_INTERFACE`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md) boundary is
respected).

## Theorem (runner-verified; exact and numerical gates named)

Per 4-cell: 24 path 4-simplices; **15** edge classes (flat lengths² ∈ {1,2,3,4}); **50** triangle
(hinge) classes; 10 metric components → **5 non-metric modes**.

1. **Flat anchor (flat-anchor check) — the tick extension of the retained flat fact.** Every interior triangle class
   of the flat complex has deficit zero to machine precision; `S_R = Σ_t A_t δ_t = 0` on the flat OS0
   background.
2. **Exactness gates (Schlaefli/Hermiticity check, end-to-end action check).** The per-4-simplex Schläfli identity `Σ_t A_t dθ_t = 0` holds to
   machine precision in every length direction; `Q(k)` is Hermitian to machine precision (the
   complex-level Regge lemma); and a finite-difference check of the **actual action** on a periodic
   `3⁴` box matches the Bloch prediction end-to-end.
3. **Discrete gauge, exact (gauge-zero-mode check).** Vertex displacements (4 components per cell) are exact zero modes of
   `δ²S_R` at every momentum.
4. **Mode inventory (mode-inventory check, extra-branch decoupling check).** Constant metric perturbations are exact zero modes at `k=0`. The five
   non-metric modes split into **four massive branches** (raw `S_R` orientation
   eigenvalues `-48, -16×3`, hence positive after the standard Euclidean
   orientation) and **one exactly flat branch** which is an **exact zero branch
   at every momentum** and meets the metric sector only in the gauge directions: a Rocek–Williams-type spurious
   lattice direction, **exactly decoupled at quadratic order**. The physical low-energy content is the
   EH sector alone.
5. **The 4D comparator + emergent Euclidean isotropy (4D comparator check).**

   > `Q_h(k) = c · Q_EH(k) + O(k⁴)` with the **single constant `c = −1/2`** across **five** directions
   > **including the tick-space mixed ones** (pure-tick, pure-space, space-space, tick-space, full body
   > diagonal); relative residuals `~10⁻⁸`, spread `~5×10⁻⁸`.

   `Q_EH` is the 4D Euclidean linearized EH pairing (operator derived in-runner from the curvature
   definitions). `c = −1/2` is the textbook `δ²S_R = ½δ²∫√gR` with the variational sign — the Regge↔EH
   correspondence **including its normalization, derived**. The isotropy across tick-mixed directions
   is the kinetic-isotropy primitive's structural grant **realized dynamically by the geometric action
   at O(k²)** on the OS0 surface.
6. **The 3+1 reading (3+1 fiber-metric check) — the geometric λ=1 fiber metric and multipliers.** At pure-tick momentum,
   `Q_h = ω²K + O(ω⁴)` with

   > `K_spatial-trace : K_TT = −2 : +1` (the λ=1 DeWitt fiber metric, indefinite, both TT channels
   > equal), and **zero** lapse (`h_ττ`) and shift (`h_iτ`) kinetic weights (the multiplier structure).

   These are exactly the structures the 3+1 target-operator analysis certified for the continuum
   target ([`R3_GEOMETRIC_REGGE_LINEARIZATION...`](R3_GEOMETRIC_REGGE_LINEARIZATION_GIVES_HEALTHY_LAMBDA1_GRAVITON_NARROW_THEOREM_NOTE_2026-06-08.md)
   row's guarded gap) — here they come from `δ²S_R` of the geometric action **natively**.
7. **Spatial comparator signs (spatial-sign comparator check).** At zero tick-frequency with spatial `k‖x`: the two spatial TT
   channels are equal and the transverse-trace channel is equal-magnitude opposite-sign (ratio exactly
   `−1`) — the
   [`UNIVERSAL_GR_DEGENERATE_SUPERMETRIC...`](UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md)
   no-go's **supplied** pair, derived inside the 3+1 tick complex.

## Net

The supplied comparator inputs named by the degenerate-supermetric no-go
(the opposite-signed comparator pair, the non-degenerate fiber metric) and the
structural pieces the 3+1 target-operator row certified for the continuum target
(λ=1 kinetic weights, multiplier structure, gauge zeros) are reproduced by the
second variation of the geometric action on this tick complex — the retained 3D
chain extended by the emergent tick. **The single remaining sign is the overall action orientation** (`S_R` vs `−S_R`) —
the same located residual as
[`GRAVITY_SIGN_NOT_FORCED_BY_ARROW_STABILITY_OR_SPECTRAL_ROUTES...`](GRAVITY_SIGN_NOT_FORCED_BY_ARROW_STABILITY_OR_SPECTRAL_ROUTES_NO_GO_SHARPENING_NOTE_2026-06-08.md);
the geometric route adds no second sign admission.

## What is and is not claimed

- **Is:** on the `Z³×Z_τ` tick extension of the retained complex, around flat: deficits vanish; vertex
  displacements are exact zero modes at all momenta; the non-metric sector is four massive branches +
  one exactly decoupled branch; `Q_h = −½·Q_EH + O(k⁴)` isotropically across tick-mixed directions;
  the λ=1 kinetic fiber metric with zero lapse/shift weights at pure-tick momentum; the spatial
  `±` comparator pair at zero tick-frequency. Exact algebraic and numerical gates are named:
  Schläfli, Hermiticity, end-to-end action finite difference, and slice consistency
  with the retained chain.
- **Is not:** does **not** derive the edge-length degrees of freedom or select the Regge action from
  the axioms (edge lengths are the supplied dynamical variables; action selection open); does **not**
  fix the overall action orientation (the located sign residual, unchanged); does **not** derive the
  tick scale (clock-rate boundary respected; `c_t=c_s` is the primitive's structural grant); does
  **not** make nonlinear/strong-field claims; the `O(k⁴)` lattice corrections are not characterized.
  Adds no axiom, no primitive, no fitted value.

## Boundaries (honest)

- **Euclidean/OS0 level.** The Lorentzian reading is by the framework's RP/OS route; the multiplier
  structure shown here is the Euclidean quadratic form's structure at pure-tick momentum (it matches
  the continuum target's 3+1 split, which was analyzed in Lorentzian form in the in-review
  target-operator row — context, not a load-bearing dependency).
- **The exactly decoupled fifth branch** is a lattice (non-metric) direction with identically zero
  quadratic action; its behavior at higher order (cubic and beyond) is not addressed.
- The exact line-averaged metric map (midpoint phase × sinc) is load-bearing for the channel
  comparisons, as established in the 3D row's development (a phase-free map leaks the massive
  non-metric weights into the metric channels at `O(k²)`). This note uses that
  map as part of the supplied edge-length-to-metric readout; it does not derive
  the edge-length degrees of freedom from the axioms.
- Literature (Regge 1961; Rocek–Williams lattice graviton; Cheeger–Müller–Schrader) cited as context
  only; every number is computed from the complex's geometry in-runner.

## Load-bearing inputs

- [`CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md`](CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md) — the retained spatial complex; its chain is the verified constant-tick slice (slice-consistency check), its flat fact the spatial anchor.
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) — the `c_t=c_s` structural grant for the symmetric tick graining (nothing beyond its declared grant is consumed).
- [`UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md) — the supplied comparator pair and the named "derived non-degenerate fiber metric" bypass, both delivered geometrically here.
- [`R3_GEOMETRIC_REGGE_LINEARIZATION_GIVES_HEALTHY_LAMBDA1_GRAVITON_NARROW_THEOREM_NOTE_2026-06-08.md`](R3_GEOMETRIC_REGGE_LINEARIZATION_GIVES_HEALTHY_LAMBDA1_GRAVITON_NARROW_THEOREM_NOTE_2026-06-08.md) — the target-operator certificate whose explicit-`δ²S_R` guardrail this note discharges in 3+1.
- [`GRAVITY_SIGN_NOT_FORCED_BY_ARROW_STABILITY_OR_SPECTRAL_ROUTES_NO_GO_SHARPENING_NOTE_2026-06-08.md`](GRAVITY_SIGN_NOT_FORCED_BY_ARROW_STABILITY_OR_SPECTRAL_ROUTES_NO_GO_SHARPENING_NOTE_2026-06-08.md) — the located sign residual the orientation coincides with.
- [`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md) — the tick-scale boundary respected by the framing.

## Forbidden-imports check

No PDG / fitted / literature value is consumed. The complex, dihedral geometry, areas, deficits, the
Regge Hessian, and the 4D Euclidean comparator operator are constructed/derived in-runner; the
`c = −1/2` constant is an output cross-checked against the independently derived textbook
normalization. Regge / Rocek–Williams / Cheeger–Müller–Schrader appear as context only and enter no
check.
