# Cycle-330 symmetric edge sign: physical-M2 adversarial synthesis

Date: 2026-07-25
Status: **corrected classifier retained; specific physical route defect exhibited**
Authority: **none**
Audit: **unset**

## Result

The corrected bounded postproduct classifier is

```text
s = x_outer (1-tag_u) (1-tag_v).
```

It is exact on the landed Cycle-311/315 branch grammar and repairs the failed
first-round extrapolation

```text
s_old = x_outer z_outer (1-tag_u) (1-tag_v).
```

The corrected root candidate appropriately calls its eight-entry diagonal a
coefficient/ray-space translator and leaves a physical matrix-unit synthesis
open.  This audit tests that stronger open question.  No unitary on just the
outer-edge `M2` and its two endpoint-tag `M2`s realizes the translator on the
landed physical state vectors.

The obstruction is specific.  Every arm has a positive vacuum ray and a
negative `n_L=n_R=1` ray with endpoint tags `00`.  None of the shared edge's
single-factor `X`, `Z` or `Y` is in the fixed-Wilson vacuum stabilizer, so both
rays have local marginal

```text
rho_edge,tags = I_edge/2 tensor |00><00|_tags.
```

Exact action on the positive ray forces the local operator to restrict to
`+I` on this two-dimensional support; exact action on the negative ray forces
`-I` on the same support.  The physical matrix-unit equations have
coefficient rank 4 and augmented rank 5.  They have no exact solution, even
before unitarity is imposed.

This is a counterexample to the three-`M2` physical route, not a no-go for a
larger bounded support, clean physical syndrome registers, or an
ancilla-assisted extraction and uncomputation circuit.

## Corrected versus legacy sign

On the six interior Cycle-330 center-arm fixtures, the corrected and legacy
classifiers coincide because no positive `(x,z,t_u,t_v)=(1,0,0,0)` row occurs
there.  A fixed periodic-seam witness separates them without a refit:

- L5: outer edge 74, bodies `(0,0,4)` and `(0,0,0)`, modes 4 and 5;
- held L6: outer edge 89, bodies `(0,0,5)` and `(0,0,0)`, modes 4 and 5;
- logical labels `n_L=n_R=1`, each with mode label `(0,)`;
- term pairs `(6,9)` and `(7,8)` have local pattern `(1,0,0,0)` and physical
  order sign 1 at both sizes;
- the corrected classifier returns 1;
- Route B's six-term diagnostic returns 1 through monomial 4;
- the legacy `x*z` classifier returns 0.

The legacy formula is retained only as a failed extrapolation control.

## Label space is not state space

The corrected table uses the three bits `(x_outer,tag_u,tag_v)`, so its label
dimension 8 now matches the Hilbert dimension of three physical `M2`s.  The
remaining defect is not dimensional.

On the tag-`00` slice, the table fixes the `I,Z` preparation labels and negates
`X,Y`.  This is conjugation by `Z` on one-`M2` operator coordinates; its Choi
eigenvalues are `(0,0,0,2)`.  But the desired state-vector action is left
action on `P|vacuum>`, not conjugation of the preparation operator.  Because
the fixed-Wilson edge marginal is `I/2`, `Z_edge|vacuum>` is orthogonal to the
vacuum rather than equal to it.  A channel identity in Pauli-coordinate space
does not supply the requested phase on the physical rays.

## Actual encoding-level intertwiner check

The counterexample also survives the full Cycle-315 encoding, so it does not
depend on treating expansion terms as standalone inputs.

The encoded vacuum column is AB/BA fixed, has endpoint tags `00`, and is full
Schmidt rank on the shared edge.  Any three-`M2` encoding intertwiner must
therefore be identity on the entire edge tensor `|00>` local sector.  The
runner independently constructs the AB and BA matrices and projects their
difference onto that same sector.  At L5 and held L6:

- the abstract ray-index diagonal intertwiner has maximum column residual 0;
- the minimum over six arms of the largest projected AB/BA column residual is
  `1.4142135623730945`;
- 216 logical columns per size have nonzero projected AB/BA difference.

The sparse diagonal on the `RayReducer` row index is thus a valid abstract
global ray-basis unitary, but it is not supported on the declared three
physical tensor factors.

## Exact six-direction census

At each of L5 and held L6:

- 23,784 center-arm branch-term cases;
- 1,200 negative-order signs;
- zero corrected-formula errors;
- zero legacy-formula errors on this interior-only fixture;
- zero Route-B six-term errors;
- zero AB/BA Pauli phase-relation failures;
- zero physical-row sign conflicts;
- Route-B observed pattern counts `(347,258,347,258,158,158)`;
- zero endpoint-swap errors;
- zero abstract ray-diagonal encoding residual.

Route B remains correctly scoped as a label diagnostic.  Its six monomials
use seven active operator-coordinate bits on five underlying physical `M2`
factors (three face factors and two tags): label-space dimension 128 versus
physical Hilbert dimension 32.  The seam witness shows that Route B retains
the corrected sign, but it still does not supply a physical matrix-unit
circuit.

## Matrix-unit, support and leakage controls

Writing `K = H_edge tensor |00>_tags`, the branch requirements are

```text
U|K = +I_K,
U|K = -I_K.
```

The least-squares solution over arbitrary nonunitary `2 x 2` restrictions has
one unit of state-vector error on each witness and combined residual
`sqrt(2)`.  For every unitary on the full three-`M2` support, including any
leakage out of `K`, the equal local marginals imply

```text
||(U-I) psi_plus||^2 + ||(U+I) psi_minus||^2 = 4.
```

At least one witness residual is at least `sqrt(2)`.  The identity has zero
positive residual and negative residual 2.  A tag flip has unit target-ray
leakage probability and residual `sqrt(2)` on each witness.

## Deletion and covariance

Aggregated over the six interior directions per size:

- removing the corrected `x` control produces 11,064 errors;
- removing either endpoint-tag control produces 2,580 errors;
- deleting the sign gate produces 1,200 errors;
- deleting Route-B monomials 0 through 5 produces respectively
  `(3024,1512,3780,3780,3024,1200)` errors.

All corrected controls and all six Route-B monomials are active.

The result is endpoint symmetric and frame stable:

- every directed arm has the same positive/negative full-Schmidt witness at
  L5 and L6;
- all 24 proper-cubic frames were checked;
- each source direction reaches all six directions four times;
- all 576 ordered frame products and 3,456 direction-composition cases have
  zero failures;
- endpoint reversal leaves the corrected formula invariant.

Covariance transports the same physical-route defect; it does not turn a
Pauli preparation label into a physical state register.

## Bound sources

- corrected root candidate SHA-256:
  `18c4d81fe0b909b6589c6c7b7bfd4b1bbbb54159a7549349e0c17654c139b9d0`;
- Route-B runner SHA-256:
  `1690b2aec7c1864988a158c56c0d78e8d69c257e6559cea1e048588908e30d78`.

The adversarial runner reports 7 PASS / 0 FAIL and terminal

```text
THREE_M2_POSTPRODUCT_LABEL_GATE_DEFECT_EXHIBITED_LARGER_PHYSICAL_ROUTE_OPEN
```

## Open

- a larger-support matrix-unit completion that extracts physical stabilizer
  syndromes rather than reading Pauli preparation coordinates;
- clean physical syndrome registers and their preparation/uncomputation;
- a primitive nearest-neighbor circuit and leakage-free intertwiner on that
  enlarged support;
- the complete simultaneous two-star `M64` update and recurrent schedule.

No broader impossibility, minimum-support, shared-obstruction or
axiom-pressure claim is made.

## Reproduce

```bash
python3 scripts/frontier_cycle330_symmetric_edge_sign_physical_m2_adversary_2026_07_25.py
```
