# Gauge-Vacuum Plaquette Beta=6 Finite Seam Route Repair

**Date:** 2026-04-17; 2026-05-27 scope repair.
**Status:** finite witness/evaluator-route bounded support. This row now
claims only the finite class-sector route certified by the runner: the
three-sample left evaluator is fixed, the beta-side vector is a common input,
and the listed finite structural surface does not determine that beta-side
input uniquely. It does not claim that the full untruncated Wilson/Haar
environment transfer identity, the exact one-slab/rim integral boundary
objects, or the physical `beta = 6` matrix elements are already derived.
**Type:** bounded_theorem
**Status authority:** independent audit lane only; this source note does not
retag itself as retained.
**Runner:** `scripts/frontier_gauge_vacuum_plaquette_beta6_finite_seam_route_repair.py`

## 2026-05-27 Scope Repair

The prior version overstated the current surface by treating
`K_6^env` and `B_6(W)` as already-fixed exact Wilson/Haar integral objects.
The current upstream transfer packet is narrower: it supplies a finite
class-sector witness packet, not the full physical Wilson environment.

This repair keeps the useful science and removes the overclaim. The row now
binds only the finite route that is actually checked:

- the universal three-sample left operator is fixed on the finite
  dominant-weight box;
- its first symmetric restriction is the exact radical matrix `F` and has rank
  three;
- any candidate normalized beta-side vector `rho` is mapped to a three-sample
  value triple by that same fixed left operator;
- the listed finite structural surface admits distinct positive self-adjoint
  conjugation-symmetric beta-side witnesses and therefore does not determine a
  unique normalized triple.

The physical `beta = 6` integral-evaluation problem remains open. This row is
a bounded finite witness and route-separation theorem, not a closed plaquette
PF evaluator.

## Question

After the current finite transfer-witness and underdetermination repairs, what
is the strongest honest statement about the first `beta = 6` three-sample
plaquette seam?

## Answer

It is a finite evaluator-route theorem plus an underdetermination boundary.

On the runner's finite class-sector witness surface, the left evaluator for
the three sample holonomies is fixed. The first symmetric restriction is the
explicit radical matrix `F`, and it has rank three. Therefore the three-sample
route factors through one common beta-side vector hit by a fixed three-row
operator.

However, the current finite structural inputs - positivity, self-adjointness,
conjugation symmetry, positive symmetric boundary vector, and normalization -
do not determine that common beta-side vector. The runner exhibits two
admissible finite witnesses satisfying those structural constraints and
producing different normalized three-sample triples.

So the seam has been separated into:

- fixed left evaluation geometry; and
- still-open beta-side environment data.

## Finite Setup

Let the finite dominant-weight box be

`B_N = {(p,q): 0 <= p,q <= NMAX}`, with `NMAX = 5`.

Let `E_3` be the three-row sample operator whose rows are the Peter-Weyl
character evaluation rows at the three sample holonomies `W_A`, `W_B`, and
`W_C` used by the runner.

For any normalized beta-side vector

`rho = z / z_(0,0)`

on `B_N`, the induced normalized three-sample values are

`Zhat = E_3 rho`.

The route theorem is about this finite map and the structural witness surface
used by the runner. It is not a claim that `rho` has been identified with the
physical Wilson/Haar environment at `beta = 6`.

## Theorem 1: fixed finite three-sample left evaluator

On the first symmetric witness sector spanned by

`chi_(0,0)`, `chi_(1,0) + chi_(0,1)`, and `chi_(1,1)`,

the three-sample row operator restricts exactly to the radical matrix `F`
printed by the runner.

The runner verifies:

- the symbolic radical expression for `F`;
- numerical equality between the direct character evaluation and the row
  operator implementation;
- `rank(F) = 3`.

Thus the first symmetric left evaluator is fixed and does not collapse to a
one- or two-sample scalar readout.

## Theorem 2: listed finite structural constraints do not determine the beta-side vector

The runner constructs two finite beta-side witnesses

`(S_A, eta_A)` and `(S_B, eta_B)`

on the same dominant-weight box. Both satisfy the listed finite structural
surface:

- positive self-adjoint transfer witness;
- conjugation-swap symmetry `(p,q) <-> (q,p)`;
- positive conjugation-symmetric boundary vector;
- normalized positive boundary-amplitude sequence.

They induce normalized vectors

`rho_A = S_A^DEPTH eta_A / (S_A^DEPTH eta_A)_(0,0)`

and

`rho_B = S_B^DEPTH eta_B / (S_B^DEPTH eta_B)_(0,0)`.

The runner verifies `rho_A != rho_B` and

`E_3 rho_A != E_3 rho_B`.

Therefore the listed finite structural surface alone does not determine the
beta-side vector or the normalized three-sample values.

## Corollary: the remaining seam is beta-side construction, not left-evaluator selection

The finite left evaluator is no longer the ambiguous object on this route. The
remaining work is to construct or derive the actual physical beta-side
environment data, or to prove a stronger admissibility theorem that collapses
the finite witness surface to a unique beta-side vector.

## What This Closes

- finite identification of the fixed three-row left evaluator on the first
  symmetric witness sector;
- exact radical form and rank-three non-collapse of that finite evaluator;
- finite witness that the listed structural constraints do not uniquely select
  beta-side normalized three-sample values;
- a narrower target for later plaquette PF work: construct the beta-side
  vector instead of searching for a new left-evaluator convention.

## What This Does Not Close

- the full untruncated spatial Wilson environment transfer identity;
- exact one-slab or rim Wilson/Haar integral boundary objects;
- physical `K_6^env` or `B_6(W)` matrix elements;
- explicit physical coefficients `rho_(p,q)(6)`;
- explicit framework-point plaquette PF data;
- analytic closure of canonical `P(6)`;
- a retained plaquette PF evaluator.

## Why This Matters

The row still preserves a useful scientific reduction, but now at the scale
the repository can actually support. It tells us that the left sample geometry
is fixed on the finite witness surface and that the hard work is the beta-side
environment construction. That is a narrower and more useful next target than
the old overbroad exact-integral language.

## Command

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_beta6_finite_seam_route_repair.py
```

Expected summary:

- `THEOREM PASS=5 SUPPORT=5 FAIL=0`

## Audit Dependency Repair Links

This graph-bookkeeping section records explicit dependency links named by a
prior conditional audit so the audit citation graph can track them. It does
not promote this note or change the audited claim scope.

- [gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TRANSFER_THEOREM_NOTE.md)
- `gauge_vacuum_plaquette_compressed_rim_functional_uniqueness_note_2026-04-17`
  (downstream consumer; backticked to avoid length-3 cycle through
  beta6_scalar_value_insufficiency - citation graph direction is
  *compressed_rim_functional_uniqueness -> beta6_scalar_value_insufficiency
  -> this_evaluation_seam*)
- `gauge_vacuum_plaquette_first_symmetric_three_sample_exact_radical_reconstruction_map_note_2026-04-17`
  (downstream consumer; backticked to avoid length-2 cycle -
  citation graph direction is *first_symmetric_reconstruction_map ->
  this_seam*)
- `gauge_vacuum_plaquette_first_symmetric_three_sample_current_stack_constraint_boundary_note_2026-04-17`
  (downstream consumer; backticked to avoid length-3 cycle through
  first_symmetric_reconstruction_map - citation graph direction is
  *current_stack_constraint_boundary -> first_symmetric_reconstruction_map
  -> this_seam*)
- [gauge_vacuum_plaquette_spatial_environment_transfer_underdetermination_note_2026-04-17](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TRANSFER_UNDERDETERMINATION_NOTE_2026-04-17.md)
- `gauge_vacuum_plaquette_first_three_sample_local_wilson_retained_positive_cone_obstruction_note_2026-04-17`
  (see-also cross-reference; backticked to break residual plaquette-cluster
  cycles through the local-Wilson positive-cone-obstruction surfaced after the
  underdetermination see-also edges were demoted. The positive-cone-obstruction
  note is a downstream three-sample positive-cone reduction; the present note
  now uses only the finite left-evaluator/witness-surface route and does not
  consume the positive-cone reduction for its own scope. The load-bearing
  citation direction is *positive_cone_obstruction -> this_seam*, not vice
  versa.)
