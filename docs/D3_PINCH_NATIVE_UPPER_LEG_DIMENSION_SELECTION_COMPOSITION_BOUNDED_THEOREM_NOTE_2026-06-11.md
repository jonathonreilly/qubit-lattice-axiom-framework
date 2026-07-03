# The d = 3 Pinch With A Native Upper Leg: The Saturation Residual Discharges Into The Dimension-Selection Lane

**Date:** 2026-06-11
**Claim type:** bounded_theorem (a composition: the landed dimension-selection
lower leg and the landed qubit/adjacency-rank upper leg pinch the lattice
dimension to `{3}` exactly; the lower leg's named criteria are inherited, not
erased)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/d3_pinch_native_upper_leg_composition_2026_06_11.py`](../scripts/d3_pinch_native_upper_leg_composition_2026_06_11.py)
(SCORECARD: PASS=19, FAIL=0; cached:
[`logs/runner-cache/d3_pinch_native_upper_leg_composition_2026_06_11.txt`](../logs/runner-cache/d3_pinch_native_upper_leg_composition_2026_06_11.txt))

---

## What this composes

Two landed legs, previously unconnected:

- **The lower leg (landed).**
  [`DIMENSION_SELECTION_NOTE.md`](DIMENSION_SELECTION_NOTE.md) (live ledger:
  `retained_bounded`): `d <= 2` fails and `d = 3, 4, 5` pass the lane's
  attractive-gravity / `beta ~ 1` finite-runner criteria, with the bridge
  [`DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_V2_2026-05-20.md`](DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_V2_2026-05-20.md)
  (`retained_bounded`).
- **The upper leg (landed, native).**
  [`ADJACENCY_RANK_QUBIT_CLIFFORD_BOUND_NARROW_THEOREM_NOTE_2026-06-10.md`](ADJACENCY_RANK_QUBIT_CLIFFORD_BOUND_NARROW_THEOREM_NOTE_2026-06-10.md):
  a Dirac-square NN carrier exists on the one-qubit-per-site lattice iff
  `d <= 3` — kinematic (carrier algebra), framework-native.

**The pinch:**

```text
    {3, 4, 5}  \cap  {d : d <= 3}   =   {3}     exactly.
```

The runner re-derives the upper set (`U = {1,2,3}`: Pauli sub-frames exist;
the extension system `{X, sigma_a} = 0` has nullspace exactly zero; a
4-family needs a rank-4 orthonormal Gram in `R^3`), takes the lower pass-set
as a **cited** `retained_bounded` input, and computes the intersection
(runner Parts A, D).

## The native lower-leg surrogate (computed, not cited)

To make the composition's lower leg inspectable in the same runner, the
kernel-decay surrogate is computed per dimension: **the `Z^d`
nearest-neighbor graph Laplacian admits a decaying point-source kernel iff
`d >= 3`** (random-walk transience, exhibited finitely):

- `d = 1`: the torus potential kernel matches `a(r) = r(L-r)/(2L)` exactly —
  linear divergence, no decaying kernel;
- `d = 2`: the potential kernel grows by `ln(2)/(2 pi)` per `L`-doubling
  (measured increments 0.1111, 0.1105, 0.1104 vs 0.1103) — logarithmic
  divergence;
- `d = 3, 4, 5`: `G_L(r)` converges in `L` at fixed `r`, and the limiting
  kernel is positive and decreasing;
- `d = 3` tail corroboration: the Bessel heat-kernel representation gives
  `4 pi r G(r) = 1.0198, 1.0041, 1.0010` at `r = 4, 8, 16` and
  `G(0) = 0.252734`, reproducing the landed table of
  [`LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md`](LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md)
  and the `retained_bounded` asymptotic of
  [`LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md);
  the `1/(4 pi r)` reference scale is itself derived in-runner from the
  continuum heat-kernel identity (no imported constant).

The surrogate's pass-set on the tested range is `{3, 4, 5}` — **agreeing
with the cited lane's pass-set** in the runner's lower-leg, tail, and
composition checks. Both lower sources pinch with the native upper leg to
`{3}`.

## What the composition changes

**(1) The pinch's upper leg is now native.** The previously landed upper leg
routed through stable-circular-orbit / atomic-stability support
(`DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md`, the
`BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md` support row,
and `D3_UPPER_BOUND_IMPORT_SCOPE_GATE_NOTE_2026-06-06.md`) precisely because
of its textbook-import flavor. This composition consumes none of those routes
(the runner derives no quantity from them); they remain as independent
corroboration of the same bound. The scope gate's named concern is relieved
for this composition, not bypassed.

**(2) The saturation residual discharges into named criteria.** The
adjacency-rank note converted "why 3?" into "why saturate?" and left the
saturation reading open. This composition supplies the answer at the
composition's conditionality: **`d <= 2` fails the lower leg** (no decaying
mediator kernel; the lane's attractive-gravity criteria). "Why does the
realized lattice saturate the qubit's capacity" becomes "because
sub-saturating dimensions fail the dimension-selection lane's named
criteria" — a discharge INTO those criteria, which remain the composition's
inherited scope.

## The post-composition dimension statement

```text
  d <= 3   from the Quantum one-qubit carrier plus the Dirac-square
           NN carrier-class reading      (kinematic carrier algebra)
  d >= 3   from the dimension-selection  (named criteria: attractive gravity /
           lane + kernel-decay surrogate  decaying mediator kernel)
  => d = 3 pinched, with both legs landed and the upper leg native.
```

What "unforced" content remains in the dimension is exactly the two legs'
named scopes: the Dirac-square carrier-class reading (upper) and the
selection criteria (lower). Neither is erased by the composition; both are
strictly narrower than the bare dimension choice recorded in
`AXIOM_REDUCTION_NOTE.md`.

## Hostile/contrast witnesses

| leg dropped | witness | outcome |
|---|---|---|
| upper | `d = 4, 5` pass both lower sources (computed) | pinch degrades to `{3,4,5}` |
| lower | the `d = 1` Dirac-square carrier exists exactly (computed) | `d = 1, 2` remain admissible |
| both lower sources' agreement | cited set vs surrogate set | equal on the tested range |

Both legs are load-bearing; the pinch is a genuine two-sided composition.

## No-Go Discipline Gate (for the dimension-exclusion leg)

The negative claim is scoped: within the composed finite-dimensional
Dirac-square carrier class and the dimension-selection lower criteria, the
only surviving dimension in the tested/cited lane is `d = 3`.

- **N1 alternative routes:** (1) use only the lower leg — fails because
  `d = 4,5` pass both lower sources; (2) use only the upper leg — fails
  because `d = 1,2` satisfy the native upper bound; (3) use the prior
  orbit/atomic upper route — not consumed here, only corroborating; (4) use a
  different carrier class — outside this composition and left to the
  adjacency-rank scope; (5) reject the lower selection criteria — named open
  inherited from the dimension-selection lane.
- **N2 wall independence:** the collapsed wall set is {Dirac-square
  one-qubit carrier upper leg, dimension-selection lower criteria}. Neither
  closes the other: dropping either leg leaves extra dimensions, as shown by
  the hostile witnesses.
- **N3 hidden-wall scan:** "native upper" means carrier-native, not
  axiom-only; it still consumes the Dirac-square carrier-class reading.
  "Lower" means the named attractive-gravity/kernel-decay criteria, not an
  axiom-derived dimension-free baseline.
- **N4 residual matching:** the textbook-import upper-bound concern is
  relieved only for this composition's upper leg. The dimension-selection
  note's own boundary remains inherited.
- **N5 rhetoric audit:** "`d = 3`" is scoped to this composition. It is not a
  framework-wide derivation of `Z^3` from a dimension-free baseline, and it
  does not exclude other carrier classes by this argument.
- **N6 partial-closure scan:** no new axiom or primitive is introduced. The
  partial closure is the legitimate import-retirement shape: replace the old
  textbook upper route with a native adjacency-rank upper route, while leaving
  the lower criteria explicit.
- **N7 steelman:** a hostile reviewer can still attack the lower criteria:
  if realized mediator physics does not require the cited decaying-kernel /
  attractive-gravity condition, the pinch collapses to the native upper bound
  `d <= 3`. This is acknowledged as inherited lower-leg scope, not erased.
- **N8 cross-cycle echo:** this follows the same import-retirement pattern as
  earlier bounded repairs: narrow one leg to a native proof where available,
  and keep the remaining admitted/selection leg explicit.

## What this does not do

- It does not derive the lower leg's criteria from the axioms: attractive
  gravity / kernel decay are **named selection requirements** with their own
  `retained_bounded` scope. The dimension-selection note's own boundary —
  `Z^3` has not been derived from a dimension-free framework baseline — is
  inherited verbatim, not erased.
- It does not exclude `d = 4, 5` by the lower leg (they pass it) or
  `d = 1, 2` by the upper leg (they satisfy it): each exclusion belongs to
  exactly one leg.
- It does not promote the textbook orbit/atomic routes or depend on them.
- It does not change any axiom memo, register or deregister any primitive,
  and it does not set audit status. The upper leg inherits the
  adjacency-rank note's landed-but-unaudited conditionality; the composition
  is graded by its weakest leg.

## Falsifiers

- A decaying point-source kernel for the `Z^1` or `Z^2` NN graph Laplacian
  (would refute the surrogate's fail-set).
- A divergence of `G_L(r)` at fixed `r` for `d = 3` (would refute the
  surrogate's pass-set and contradict the landed Green-function surface).
- A 4th anticommuting element of `M_2(C)` (would refute the upper leg).
- A retained derivation that the realized mediator kernel need not decay
  (would empty the lower leg's criteria and reduce the pinch to the upper
  bound alone).

## Dependencies

- [ADJACENCY_RANK_QUBIT_CLIFFORD_BOUND_NARROW_THEOREM_NOTE_2026-06-10.md](ADJACENCY_RANK_QUBIT_CLIFFORD_BOUND_NARROW_THEOREM_NOTE_2026-06-10.md)
  — the native upper leg; landed but unaudited, so conditionality is
  inherited.
- [DIMENSION_SELECTION_NOTE.md](DIMENSION_SELECTION_NOTE.md) — the lower
  leg's pass/fail set (`retained_bounded`), cited as input.
- [DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_V2_2026-05-20.md](DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_V2_2026-05-20.md)
  — the lower leg's bridge (`retained_bounded`).
- [LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md)
  — the `retained_bounded` `1/(4 pi r)` asymptotic the surrogate reproduces.
- [LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md](LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md)
  — the Bessel representation used for the tail corroboration; landed but
  unaudited, so conditionality is inherited for that corroboration.
Relation-only, not consumed: `DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md`,
`BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`,
`D3_UPPER_BOUND_IMPORT_SCOPE_GATE_NOTE_2026-06-06.md`, and
`AXIOM_REDUCTION_NOTE.md`.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane is the only
status authority.
