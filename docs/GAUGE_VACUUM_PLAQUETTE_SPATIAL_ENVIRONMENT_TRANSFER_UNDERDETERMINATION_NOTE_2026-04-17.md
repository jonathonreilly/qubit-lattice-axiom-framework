# Gauge-Vacuum Plaquette Spatial-Environment Transfer Underdetermination

**Date:** 2026-04-17 (scope narrowed 2026-05-24 per audit `or-narrow` repair
target: claim restricted to finite structural-surface underdetermination of
the listed positivity / self-adjointness / swap-symmetry / normalization
witness packet, not the full `beta = 6` Wilson-parent / factorization stack).
**Status:** finite structural-surface underdetermination obstruction on the
listed witness packet only — the explicitly enumerated positivity,
self-adjointness, conjugation-symmetry, and positive-symmetric-boundary
structural conditions do not by themselves force a unique
`beta = 6` spatial-environment pair `(S_6^env, eta_6)` on the marked
class-function sector witness surface used by the runner. This note does
not assert that the listed structural surface exhausts the full
`beta = 6` Wilson-parent / factorization admissibility stack.
**Type:** no_go
**Runner:** `scripts/frontier_gauge_vacuum_plaquette_first_three_sample_environment_evaluator_route_2026_04_17.py`

## Question

Do the current exact plaquette PF theorems now on `main`, together with the new
Wilson parent/compression theorem, already force the explicit `beta = 6`
spatial-environment transfer object

`S_6^env`

and boundary state

`eta_6`?

## Answer (narrowed scope)

No — but only at the narrowed scope below.

The listed positivity, self-adjointness, conjugation-symmetry, and
positive-symmetric-boundary structural conditions, evaluated on the finite
class-sector witness surface used by the runner, do not by themselves
force a unique `beta = 6` spatial-environment pair `(S_6^env, eta_6)` on
that witness surface. The runner exhibits two distinct admissible
witnesses satisfying the listed structural surface and inducing
different normalized boundary character data and different induced
three-sample plaquette PF values.

This note does **not** claim that the listed structural surface exhausts
the full `beta = 6` Wilson-parent / factorization / current-stack
admissibility constraints. Whether further constraints from the full
beta = 6 stack collapse the witness surface to a unique pair is left
open and is not closed by this note.

So the narrowed reading is: on the listed structural surface, the live
plaquette PF gap is not closed by the surface alone; the broader gap
question remains scoped to a separate retained bridge.

## Setup

From the exact spatial-environment transfer theorem already on `main`:

- there is one explicit positive self-adjoint orthogonal-slice transfer law
  `S_beta^env`,
- there is one positive conjugation-symmetric boundary state `eta_beta`,
- and the environment coefficients satisfy the exact matrix-element law

  `z_(p,q)^env(beta) = <chi_(p,q), (S_beta^env)^(L_perp-1) eta_beta>`.

Equivalently,

`rho_(p,q)(beta)
 = <chi_(p,q), (S_beta^env)^(L_perp-1) eta_beta>
   / <chi_(0,0), (S_beta^env)^(L_perp-1) eta_beta>`.

From the exact factorization stack already on `main`:

- `T_src(6) = exp(3 J) D_6^loc C_(Z_6^env) exp(3 J)`,
- `J` is the explicit self-adjoint plaquette source operator,
- `D_6^loc` is the exact local Wilson marked-link factor.

From the new Wilson parent/compression theorem:

- the plaquette PF lane already sits inside one Wilson parent/descendant
  structure,
- but the explicit residual environment data are still listed as open.

## Theorem 1 (narrowed): the listed structural surface does not determine a unique admissible spatial-environment transfer pair on the witness surface

Choose two distinct admissible positive self-adjoint
conjugation-symmetric spatial transfer witnesses

`(S_A, eta_A) != (S_B, eta_B)`

on the marked class-function sector witness surface used by the runner.

Both satisfy the listed structural conditions enumerated in the witness
surface:

- `S_A > 0`, `S_B > 0`,
- `S_A = S_A^*`, `S_B = S_B^*`,
- both commute with the conjugation swap `(p,q) <-> (q,p)`,
- `eta_A` and `eta_B` are positive and conjugation-symmetric.

Define the normalized boundary character data

`rho_A(p,q)
 = <chi_(p,q), S_A^(L_perp-1) eta_A>
   / <chi_(0,0), S_A^(L_perp-1) eta_A>`

and

`rho_B(p,q)
 = <chi_(p,q), S_B^(L_perp-1) eta_B>
   / <chi_(0,0), S_B^(L_perp-1) eta_B>`.

Then the runner exhibits admissible choices on the listed surface with

`rho_A != rho_B`.

So the listed structural surface alone does **not** determine unique
`beta = 6` spatial-environment data on the witness surface. This does
not audit whether the full `beta = 6` Wilson-parent / factorization
admissibility stack collapses the witness surface to a single pair.

## Theorem 2 (narrowed): on the listed witness surface, distinct admissible spatial-environment data can still induce different plaquette PF data

Insert the two admissible coefficient sequences into the exact factorized
source-sector law:

`T_A = exp(3 J) D_6^loc diag(rho_A) exp(3 J)`,
`T_B = exp(3 J) D_6^loc diag(rho_B) exp(3 J)`.

The runner exhibits admissible pairs on the listed structural surface
for which the resulting Perron states induce different moment sequences
for the same explicit source operator `J`, and therefore different
symmetry-reduced Jacobi coefficients.

So on the listed structural surface alone, distinct admissible witnesses
can map to distinct induced plaquette PF data. The note does not claim
this exhausts all `beta = 6` Wilson-parent / factorization admissibility
constraints — collapse of the witness surface to a unique induced
PF datum under the full beta = 6 stack is left open.

## Corollary 1 (narrowed): the listed structural surface alone is not the closing object

Under the narrowed scope, the listed witness-surface constraints
(positivity, self-adjointness, conjugation-symmetry, normalization) are
not by themselves the closing object for unique `beta = 6` data. A
closing object on the witness surface would have to add at least one
further constraint beyond the listed structural surface. This corollary
does not name what that further constraint is and does not adjudicate
whether the full `beta = 6` Wilson-parent / factorization stack already
supplies it.

## What this closes (narrowed)

- on the listed structural witness surface only: the enumerated
  positivity, self-adjointness, conjugation-symmetry, and
  positive-symmetric-boundary conditions do not by themselves force a
  unique `beta = 6` spatial-environment pair on that witness surface
- equivalently: the listed structural surface alone does not collapse
  to a single induced `(rho_(p,q)(6))` sequence on the runner's witness
  packet

## What this does not close

- whether the full `beta = 6` Wilson-parent / factorization /
  current-stack admissibility constraints collapse the witness surface
  to a unique pair
- explicit `S_6^env`
- explicit `eta_6`
- explicit coefficients `rho_(p,q)(6)`
- explicit framework-point Perron moments or Jacobi coefficients
- analytic closure of canonical `P(6)`
- a global sole-axiom PF selector

## Command

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_first_three_sample_environment_evaluator_route_2026_04_17.py
```

## Audit boundary (2026-05-24 — `or-narrow` repair target taken)

This revision addresses the generated-audit repair target:

> missing_bridge_theorem: prove that the finite positive self-adjoint
> swap-symmetric witness surface used by the runner is admissible under
> the full beta=6 spatial-environment and Wilson-parent/factorization
> stack, or narrow the claim to finite structural-surface
> underdetermination.

This revision takes the second branch of the repair target. The status
line, Answer section, Theorem 1, Theorem 2, Corollary 1, and the
"what this closes" / "what this does not close" lists are rescoped so
that the no-go is read on the listed structural witness surface alone
(positivity, self-adjointness, conjugation-symmetry, positive-symmetric
boundary). The note no longer asserts that the listed structural surface
exhausts the full `beta = 6` Wilson-parent / factorization / current-stack
admissibility constraints; whether further constraints from that broader
stack collapse the witness surface to a single pair is left open and is
not closed here. No new mathematics is added; no new derivations are
introduced; the runner is unchanged.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TRANSFER_THEOREM_NOTE.md)
- `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17`
  (see-also cross-reference; backticked to break cycle-0015 in the citation
  graph. The beta6 evaluation-seam note's own dependency-repair list already
  cites this underdetermination note as upstream (its evaluation seam is a
  reduction of the spatial-environment transfer underdetermination surface);
  the load-bearing citation direction is beta6 -> underdetermination, not
  vice versa.)
- `gauge_vacuum_plaquette_compressed_rim_functional_uniqueness_note_2026-04-17`
  (see-also cross-reference; backticked to break plaquette-cluster cycles
  0001-0007 in the citation graph. The compressed-rim-functional uniqueness
  theorem is a downstream class-sector retained theorem in the plaquette PF
  stack; the present underdetermination obstruction note's body cites the
  upstream "exact spatial-environment transfer theorem" rather than this
  downstream uniqueness theorem, and the compressed-rim note carries its
  own backticked downstream-consumer pointer back here. The load-bearing
  citation direction is *compressed_rim_functional_uniqueness →
  underdetermination* via the spatial-environment transfer chain, not vice
  versa.)
- `gauge_vacuum_plaquette_first_symmetric_three_sample_exact_radical_reconstruction_map_note_2026-04-17`
  (see-also cross-reference; backticked to break plaquette-cluster cycles
  in the citation graph. The exact-radical-reconstruction-map note is a
  downstream sampling-reconstruction theorem; the present underdetermination
  obstruction note does not consume the reconstruction map for its no_go
  surface, which is closed by the spatial-environment transfer / Wilson
  parent stack cited in the body. The load-bearing citation direction is
  *exact_radical_reconstruction_map → underdetermination*, not vice versa.)
- `gauge_vacuum_plaquette_first_symmetric_three_sample_current_stack_constraint_boundary_note_2026-04-17`
  (see-also cross-reference; backticked to break plaquette-cluster cycles
  in the citation graph. The current-stack constraint-boundary note is a
  downstream three-sample sampling-burden theorem that itself cites the
  present underdetermination note via the spatial-environment-transfer
  measure theorem chain. The load-bearing citation direction is
  *current_stack_constraint_boundary → underdetermination*, not vice versa.)
- `gauge_vacuum_plaquette_first_three_sample_local_wilson_retained_positive_cone_obstruction_note_2026-04-17`
  (see-also cross-reference; backticked to break plaquette-cluster cycles
  in the citation graph. The local-Wilson positive-cone-obstruction note is
  a downstream three-sample positive-cone reduction; the present
  underdetermination obstruction is upstream in the plaquette PF gap
  argument and does not consume the positive-cone reduction for its no_go
  surface. The load-bearing citation direction is
  *positive_cone_obstruction → underdetermination*, not vice versa.)
