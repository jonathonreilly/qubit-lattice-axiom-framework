# Block 16 V1-V5 Scratch

Row: `s3_time_bilinear_tensor_primitive_note`
State: `open_gate` (definition-only, class-A), 482 desc, unaudited.
Lane: s3 (continues blocks 02, 07, 12; distinct sub-problem).

## Setup

Target is the bilinear support carrier
`K_R(q) := [[u_E(q), u_T(q)], [delta_A1(q) u_E(q), delta_A1(q) u_T(q)]]`
on the seven-site star support.

Named admitted inputs:
- `delta_A1` from retained-bounded `TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE`
- `u_E(q) := <E_x, q>`, `u_T(q) := <T1x, q>` (linear functionals in the adapted basis)
- `delta_A1`-decoupling fact (upstream open: `delta_A1 ⊥ {E_x, T1x, E_perp, T1y, T1z}`)

Three named open theorem targets in source note:
1. retained derivation of the `delta_A1`-decoupling fact
2. retained derivation of aligned-bright coordinate identification
3. bridge theorem identifying `K_R` with a physical tensor primitive

## Distinct angles from prior blocks

- Block 02: AC_phi_lambda C3-foreclosure (different sub-row — coupling structure)
- Block 07: background uniqueness `PL S^3 x R` + Hessian channel no-go (different scope — kinematics)
- Block 12: time-channel rigidity on `Theta_R -> Lambda_R` coupling family (downstream — slice coupling)
- This block: the **carrier `K_R` itself** as an algebraic primitive — structural
  properties of the *carrier* (not coupling, not uniqueness, not slice).

V1-V5 must be distinct from all of these.

## V1 — Direct derivation of decoupling fact

Try to prove `delta_A1 ⊥ {E_x, T1x, E_perp, T1y, T1z}` from the Green-matrix
structure on the seven-site star support.

VERDICT: This is gap (1) named in the source note as "real derivation gap,
not import-redirect". The note states no upstream retained-grade derivation
exists on `main`. Anti-pattern: trying to close the named open gap in this
block would either (a) require new primitives (forbidden under A_min) or
(b) collapse into the runner's class-D finite-grid shadow, which the note
explicitly downgrades. SKIP.

## V2 — Aligned-bright coordinate identification

Try to prove `u_E ↔ <E_x, ·>`, `u_T ↔ <T1x, ·>` as canonical bright
coordinates from a derived bright/dark decomposition.

VERDICT: This is gap (2). The decomposition would need an unaudited canonical
bright/dark theorem on the support block. SKIP — same risk as V1.

## V3 — Physical tensor-primitive bridge

Try to identify `K_R(q)` with a physical tensor primitive in the GR readout
chain (e.g., from `S3_TIME_SPACETIME_TENSOR_PRIMITIVE_NOTE` or the
Einstein/Regge identification).

VERDICT: This is gap (3) and the *third* upstream blocker. Bridge theorems
to physical dynamics require either the conditional readout-triple (already
audited-clean no-go: `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE`) or a new
dynamics primitive (forbidden under A_min). SKIP.

## V4 — Class-B bounded readout sharpening

Try to sharpen the bounded projection `Theta_R^(0) = P_R^(0) vec(K_R)` from
endpoint-fixed to globally-fitted; or extend to off-A1 backgrounds.

VERDICT: This sharpens a class-B readout, not a class-A primitive on the
row. The bounded coefficients `a_E, b_E, a_T, b_T` are already endpoint-fixed
from `eta_floor_tf`; promoting beyond endpoint-fixed would require a new
upstream certificate on the bright-channel response function. Also, this
re-states the block 12 angle (sharpen the conditional family), just on the
spatial side instead of the time side. SKIP — too close to block 12.

## V5 — Structural rank-1 outer-product factorization of K_R

This is the angle.

**Observation:** Under the named admitted inputs, the symbolic carrier

`K_R(q) = [[u_E(q), u_T(q)], [delta_A1(q) u_E(q), delta_A1(q) u_T(q)]]`

factors algebraically as a rank-1 outer product

`K_R(q) = w(q) v(q)^T`

where `w(q) := (1, delta_A1(q))^T` (column vector in the "scaling channel")
and `v(q) := (u_E(q), u_T(q))^T` (column vector in the "bright channel").
Equivalently `vec K_R(q) = v(q) ⊗ w(q)` (Kronecker outer product).

This factorization is a *purely algebraic structural property* of the
definition itself, independent of:
- whether `delta_A1` is exactly blind to non-A1 perturbations (gap 1),
- whether `(u_E, u_T)` are canonical bright coordinates (gap 2),
- whether `K_R` is a physical tensor primitive (gap 3).

The factorization implies the following structural properties (R1)-(R5):

(R1) **Rank-1 universality.** For every `q` on the seven-site star support,
     the 2x2 matrix `K_R(q)` has rank at most 1, with strict equality
     precisely when both `u_E(q) != 0` and `u_T(q) != 0` (so the bright
     channel is non-degenerate). When the bright channel is non-degenerate,
     the rank is exactly 1 regardless of the value of `delta_A1(q)`.

(R2) **Row-proportionality identity.** The two rows of `K_R(q)` are
     proportional: row_2 = `delta_A1(q) * row_1`. Equivalently the
     determinant vanishes identically: `det K_R(q) = 0` for every `q`.

(R3) **Column-proportionality identity.** The two columns of `K_R(q)` are
     proportional: col_2 = `(u_T(q) / u_E(q)) * col_1` whenever `u_E(q) != 0`.
     Symmetrically `col_1 = (u_E(q) / u_T(q)) * col_2` whenever `u_T(q) != 0`.
     The ratios are scale-invariant in `delta_A1`.

(R4) **Channel-separation of K_R partial derivatives along bright/scaling
     directions.** Under the named admitted decoupling fact, the partial
     derivatives split cleanly:
     - `partial_{E_x} K_R(q) = (1, delta_A1(q))^T (1, 0)`  (bright-channel
       perturbation acts only on `u_E`; scaling channel inherits the
       background `delta_A1`)
     - `partial_{T1x} K_R(q) = (1, delta_A1(q))^T (0, 1)`  (bright-channel
       perturbation acts only on `u_T`)
     - `partial_{delta} K_R(q)` is a rank-1 perturbation along the second
       row only: `[0, 0; u_E, u_T]`, which is in the span of `(0, 1)^T`
       times `v(q)^T` (i.e., orthogonal-to-`(1,0)` in the scaling channel).
     This is a *structural channel-separation*: bright perturbations move
     `v(q)`, scaling perturbations move `w(q)`, and the two are orthogonal
     in the outer-product structure.

(R5) **Singular-value collapse.** The two singular values of `K_R(q)` are
     `||w(q)|| * ||v(q)||` and `0`. Explicitly:
     - `sigma_1(q) = sqrt(1 + delta_A1(q)^2) * sqrt(u_E(q)^2 + u_T(q)^2)`
     - `sigma_2(q) = 0`
     The single non-zero singular value FACTORS algebraically into a
     pure-scaling contribution (`sqrt(1+delta^2)`, depending only on the
     scalar background datum) and a pure-bright contribution
     (`sqrt(u_E^2 + u_T^2)`, depending only on the bright projections).
     This is the singular-value version of the rank-1 factorization.

These five properties are a positive narrow theorem on the row. They are
**independent of** and **do not bypass** any of the three named open gaps:
- decoupling (gap 1) only enters R4's *channel-separation interpretation*
  of partial derivatives; the rank-1 factorization itself holds without it.
- aligned-bright identification (gap 2) is not needed; the factorization
  only refers to `(u_E, u_T)` as the linear functionals defined in the
  source note.
- physical-primitive bridge (gap 3) is not asserted; R1-R5 are pure
  algebraic structure of the *symbol* `K_R`.

This is distinct from all four prior blocks:
- Block 02 (AC_phi_lambda C3-foreclosure): different downstream object.
- Block 07 (background uniqueness + Hessian no-go): about backgrounds and
  the Hessian channel, not the bilinear carrier symbol.
- Block 12 (`Xi_P = (P_R c) ⊗ V_R(t)` factor rigidity): about the
  conditional time-coupling family on top of `K_R`; here the focus is the
  carrier `K_R` itself, before time coupling is applied. Both blocks use
  outer-product factorizations but on different objects: block 12 factors
  *across time vs. space*; this block factors *within the carrier itself*
  (scaling channel vs. bright channel).

## Chosen angle: V5

Deliverable: positive narrow theorem on the row, scope-bounded.
- Statement: Under the named admitted inputs of
  `S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md`, the symbolic carrier `K_R`
  factors algebraically as a rank-1 outer product
  `K_R(q) = (1, delta_A1(q))^T (u_E(q), u_T(q))`, and the five structural
  properties (R1)-(R5) hold by polynomial identity for every `q` in the
  seven-site star support.
- Effect on row: row remains `open_gate` for the three named upstream
  gaps. A positive narrow theorem on the *internal algebraic structure*
  of the carrier is now landed, sharpening the picture from "definition
  only" to "definition with a derived rank-1 outer-product structure".
- Type: `positive_theorem`, narrow scope. Does NOT close the parent
  `open_gate`. The three open theorem targets remain upstream of this
  note and are explicitly re-cited.

## Runner plan

1. Build `K_R(q)` from the same upstream helpers as the primary runner
   (`support_delta` + `build_adapted_basis`).
2. Sample carriers on a grid of `q` values (canonical A1 family at several
   `r`; A1 baseline plus bright perturbations of varying amplitudes; A1
   baseline plus dark perturbations; mixed perturbations).
3. For every sampled `q`:
   (R1) Verify rank of `K_R(q)` is `<= 1` numerically (smallest singular
        value is at most ~1e-12).
   (R2) Verify `det K_R(q) = 0` to machine precision.
   (R3) Verify `row_2(q) == delta_A1(q) * row_1(q)` and
        `col_2(q) * u_E(q) == u_T(q) * col_1(q)` (avoiding division by zero).
   (R4) Verify channel-separation:
        - `(K_R(q + h E_x) - K_R(q)) / h` to leading order matches
          `(1, delta_A1(q))^T (1, 0)` (with O(h) residual under decoupling)
        - similarly for T1x with `(0, 1)`
        - `partial_{delta}` along an *artificial* delta-variation matches
          `[[0,0],[u_E, u_T]]` (i.e., the second-row only structure)
   (R5) Verify singular value factorization:
        - `sigma_1(q) == sqrt(1 + delta^2) * sqrt(u_E^2 + u_T^2)`
        - `sigma_2(q) <= ~1e-12`

Hard rules: A_min only (no new axiom imports; uses only the cited
authorities already used by the primary runner).

## Hard-rules confirmation

A_min only: all ingredients (`delta_A1`, `u_E`, `u_T`, basis vectors) are
imported from cited audited authorities (`TENSOR_SUPPORT_CENTER_EXCESS_LAW`
and `frontier_same_source_metric_ansatz_scan`). No new primitives. The
theorem is a purely algebraic property of the already-defined symbol.

## Cross-block independence

R1-R5 are stated and verified WITHOUT using:
- block 02's coupling-residual classification
- block 07's background-uniqueness or Hessian no-go
- block 12's time-channel rigidity (`Xi_P` family)

Conversely, the blocks above could (in principle) cite R1-R5 in future
synthesis, but this block does not enforce that direction. The five
properties are independent algebraic statements on the carrier symbol.
