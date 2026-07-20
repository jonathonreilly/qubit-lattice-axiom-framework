---
claim_id: microcausality_directional_tilt_axis_cone_refinement_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Bridge-conditional directional counting refinement of the supplied nearest-neighbor bond-Hamiltonian walk expansion. For a fixed finite region and fixed local inputs, an axis separation m and rational y>1 give ||[tau_t(A),B]|| <= 2||A||||B|| n_X (y^2/S_parallel(y)) y^(-2m) (exp(2J S_parallel(y)|t|)-1), where S_parallel(y)=y^2+4y+4/y+y^(-2). A family-uniform statement additionally assumes finite J_* and uniform local-input bounds. The associated cone slope is a mathematical Lieb-Robinson-type slope in lattice-site/Heisenberg-time units, not a physical pole, group, or wavefront velocity. The y=5/2 comparison is certified only against the declared six-point rational scan."
upstream_dependencies:
  - minimal_axioms
  - microcausality_all_time_volume_uniform_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
runner: scripts/microcausality_directional_tilt_axis_cone_refinement_2026_07_18.py
---

# Microcausality: Directional-Tilt Axis-Cone Refinement

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; the supplied Hamiltonian, finite-matrix
analysis context, and Duhamel walk expansion are inherited from the parent.
Only the counting of those walks is refined.
**Audit-status authority:** independent audit lane only. This note sets no
audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here.
**Primary runner:**
[`scripts/microcausality_directional_tilt_axis_cone_refinement_2026_07_18.py`](../scripts/microcausality_directional_tilt_axis_cone_refinement_2026_07_18.py)
**Runner cache:**
[`logs/runner-cache/microcausality_directional_tilt_axis_cone_refinement_2026_07_18.txt`](../logs/runner-cache/microcausality_directional_tilt_axis_cone_refinement_2026_07_18.txt)

## Placement and supplied hypotheses

The parent
[`MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md)
provides the load-bearing Duhamel expansion and the immediately-previous-bond
walk set. This note imports that theorem rather than re-proving its algebraic
and ODE steps. The
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
memo supplies cubic-lattice geometry only; it does not choose the Hamiltonian,
transfer operator, time convention, or dynamics.

Let `Lambda` be a fixed finite subset of `Z^3` with its nearest-neighbor
bonds, and let the Hermitian bond terms, `H`, the Heisenberg convention, and
the finite-matrix ODE context be exactly those supplied to the parent. Write
`J = max_b ||h_b||` for this region. Let `A` and `B` have nonempty disjoint
supports `X` and `Y`, and let

> `n_X = #{b : b intersects X}`.

Fix a coordinate axis, written as the first axis. Put
`a = max_{x in X} x_1` and assume
`Y` lies in the half-space `x_1 >= a+m`, where the integer `m >= 1` is the
axis separation.

For a family of regions, independence of the displayed constants from
region volume requires the additional hypotheses

> `J_* = sup_{Lambda,b} ||h_b^(Lambda)|| < infinity`

and uniform control of `||A||`, `||B||`, and `n_X` (or a fixed support-size
bound). Finiteness of each individual region does not imply these uniform
family assumptions.

## Directional walk count

For a bond `b={p,q}`, define its first-axis height by
`phi(b)=p_1+q_1`. Direct enumeration of the ten neighboring bonds gives

- parallel starting bond:
  `Delta phi in {-2 (x1), -1 (x4), +1 (x4), +2 (x1)}`;
- either transverse starting orientation:
  `Delta phi in {-1 (x2), 0 (x6), +1 (x2)}`.

The corresponding positive tilt polynomials are

> `S_parallel(y) = y^2 + 4y + 4/y + 1/y^2`,

> `S_transverse(y) = 2y + 6 + 2/y`.

They both equal `10` at `y=1`, and

> `S_parallel(y)-S_transverse(y)
> = (y-1)^2 (y^2+4y+1)/y^2 >= 0`.

Thus for `y>=1` the tilted row sum at every step is at most
`S_parallel(y)`. A finite-region boundary removes positive row terms and
cannot worsen this estimate. Backward induction on the remaining steps then
gives, for every `k`-bond walk from the `n_X` starting bonds,

> `sum_walks y^(phi(b_k)-phi(b_1))
> <= n_X S_parallel(y)^(k-1)`.

The elementary inequality
`1_{gain >= r} <= y^(gain-r)` therefore yields

> `#{k-bond walks with height gain >= r}
> <= n_X S_parallel(y)^(k-1) y^(-r)`.

This proof includes mixed parallel/transverse walks because the row bound is
applied after every actual bond type; it does not replace such walks by a
single-orientation model.

## Exact endpoint offset and theorem

A bond touching the plane `x_1=r` has height in
`{2r-1,2r,2r+1}`. Hence a starting bond touching `X` has height at most
`2a+1`, while an ending bond touching `Y` has height at least
`2(a+m)-1`. Every contributing walk therefore has gain at least `2m-2`.
The offset cannot be strengthened uniformly to `2m-1`: for `m=1`, the bond
from `(0,0,0)` to `(1,0,0)` touches both separated one-site supports and has
endpoint gain `0=2m-2`. The runner checks this witness explicitly.

Insert the directional count into the parent's unchanged `k`-term and sum
the exponential series. For every rational `y>1`,

> `||[tau_t(A),B]||
> <= 2||A||||B|| n_X (y^2/S_parallel(y)) y^(-2m)
>    (exp(2J S_parallel(y)|t|)-1)`.

The factor `y^2/S_parallel(y)` is fixed by the exact `2m-2` offset; replacing
it by `y/S_parallel(y)` would encode the false stronger offset. The runner
checks both the assembly identity and this negative mutation.

For a fixed finite region and fixed local inputs, the display holds for all
real `t`. At `y=5/2`,

> `S_parallel(5/2)=1801/100`, and `y^(-2m)=(4/25)^m`.

This is an axis-aligned estimate. For a diagonal separation the parent's
isotropic distance bound may be stronger; both estimates remain valid on
their stated hypotheses.

## Mathematical cone-slope readout

The exponential and spatial factors balance at the mathematical
Lieb-Robinson-type cone slope

> `v_axis(y) = J S_parallel(y)/ln(y)`.

This quantity is expressed in lattice-site/Heisenberg-time units. It is not a
physical pole velocity, group velocity, wavefront speed, or a framework
prediction of any measured propagation speed.

At `y=5/2`, the exact readout is

> `v_axis(5/2)=(1801/100)J/ln(5/2)`.

Its coefficient is strictly below `20e`; consequently
`v_axis(5/2) <= 20eJ` for `J>=0`, with strict inequality when `J>0`.
Indeed,
`e > sum_{n=0}^6 1/n! = 1957/720`, while the positive atanh series gives

> `ln(5/2)=2 atanh(3/7)
> > 2(3/7+(3/7)^3/3)=312/343`.

Therefore

> `20 e ln(5/2)
> > 20(1957/720)(312/343) > 1801/100`,

with final rational margin `3234971/102900`.

For the declared scan

> `y in {5/4, 3/2, 2, 5/2, 3, 4}`,

the point `5/2` has the smallest value of `S_parallel(y)/ln(y)`. The runner
certifies all five pairwise comparisons using rational lower and upper bounds
from the atanh series, including a rational geometric tail bound. This is a
finite-scan statement only; no assertion is made about minimization over
other values of `y`.

## Claim boundaries

- The result is conditional on the parent's supplied bond Hamiltonian,
  Heisenberg convention, finite-matrix ODE context, and walk-expansion
  theorem. Its current audit status cannot exceed that dependency.
- It does not construct or control a reconstructed many-body transfer
  Hamiltonian, compose quasilocal tails, or integrate over `U`.
- It does not apply to plaquette interactions or prove a multi-axis product
  estimate.
- It does not select dynamics, establish generic interaction-path novelty,
  or set an audit verdict.
- The finite-region theorem does not by itself supply the `J_*` and uniform
  local-input conditions required for a family-uniform statement.

## Verification

The primary runner performs exhaustive finite-box height-table checks for the
parallel and both transverse orientations, symbolic tilt and series
identities, the exact minimal-offset witness, an explicit false-offset and
false-prefactor mutation rejection, exact rational evaluation at `y=5/2`,
and rational atanh interval certificates for every finite-scan comparison.
It has no mutable prose inputs, so the runner cache is content-pinned to the
runner source alone.
