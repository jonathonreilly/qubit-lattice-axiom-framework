# Four-hats stratification: the gauge-link / color-einselection open inputs sit at distinct positions of the frame → connection → generator chain (non-reduction, narrow theorem)

**Date:** 2026-06-09
**Claim type:** bounded_theorem (non-reduction theorem on the supplied
`C^3` carrier and displayed frame → connection → generator chain)
**Kind:** narrow theorem (bounded non-reduction; exact finite-dimensional algebra, no Monte-Carlo in the logic path)
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Carrier:** the irreducible color triplet `C^3`.
**Runner:** `scripts/frontier_four_hats_frame_connection_generator_stratification_2026_06_09.py` (`TOTAL: PASS=18 FAIL=0`).

## Setting

The interacting-gauge foundation converged onto a single undelivered input — the
continuous-time gauge-link / color-einselection dynamics — with four open "hats"
(`ST1_ST2_SAME_WALL_GAUGE_DYNAMICS_RESIDUAL_CONVERGENCE...`):

- **ADM-1** — the static local color-frame / pointer-projector choice `{P_r}`.
- **hat 4** — the blocking / record-write isometry. Block 10
  (`COLOR_EINSELECTION...BLOCKING_ISOMETRY...`, PR #3450) reduced its undelivered
  content to that same `{P_r}` choice.
- **R2 / ADM-2** — color depolarization. The block-09 consolidation
  (`COLOR_DEPOLARIZATION_ADM2_GATING_ADMISSIONS_COLLAPSE_TO_TWO...`, landed on
  main and cited for framing only) names the requirement of a record frame `B`
  together with a non-diagonal connection `V ≠ I3` (the "primitivity" facet;
  block 07).
- **R1** — the continuous-time link generator. The record axiom supplies none
  (`record_classical_semigroup_boundary_2026-06-06` = retained;
  `record_markov_generator_embeddability_boundary_2026-06-06` = retained_no_go).

Block 10 noted that ADM-1, ADM-2 and hat 4 share a record-frame root while R1 sits on a
distinct wall, using only the global fact that the irreducible triplet has no nontrivial
SU(3)-invariant projector (commutant = scalars). This note SHARPENS that into a
per-arrow statement: the campaign's own objects line up along a chain on `C^3`,

```
   record frame {P_r}        connection V             generator X
   (ADM-1, hat 4)   ---->    (ADM-2 driver)  ---->    (R1)
                    arrow 1                  arrow 2
```

and there is an EXACT non-trivial gap at each arrow, so the four hats are stratified
along the chain rather than reducible to a single missing input.

## Theorem (non-reduction along the chain)

On the irreducible carrier `C^3`:

**Arrow 1 (frame → connection) is not onto.** The SU(3) stabilizer of a complete record
frame `{P_i = |e_i⟩⟨e_i|}` — the connections `V` with `V P_i V† = P_i` for all `i` — is
exactly the maximal torus `T^2` of connections diagonal in that frame, of Lie-algebra
dimension `2` in `su(3)` (`8 − 6`). A record frame therefore leaves a `6`-dimensional
family of `su(3)` connection directions undetermined: it does not deliver `V`. Moreover
the residual torus connections are precisely the color-diagonal ones, for which the
predictability-sieve unistochastic matrix `S_ij = |⟨e_i|V|e_j⟩|^2 = I3` — exactly the
block-07 "free / color-diagonal hopping does not depolarize" case. The depolarization
data lives TRANSVERSE to the frame stabilizer (the `6` off-diagonal `su(3)` directions),
precisely where the record frame supplies nothing.

**Arrow 2 (connection → generator) is not onto.** A regular connection `V ∈ SU(3)` admits
an infinite `Z`-lattice of `su(3)` logarithms `X` (`exp X = V`), each a valid traceless
anti-Hermitian generator, with unbounded mutual separation. A single-step holonomy `V`
therefore does not deliver a generator. This is the connection-level face of
`record_markov_generator_embeddability_boundary` (retained_no_go).

**Composition.** Arrow 1 not onto AND arrow 2 not onto ⇒ the chain has two genuine gaps,
so the four hats occupy distinct chain positions and do not collapse onto one missing
input.
The record axiom delivers no object on the chain (frame:
`record_formation_not_unconditionally_forced` = retained_no_go; generator:
`record_markov_generator_embeddability_boundary` = retained_no_go). The pointer-frame hats
`{ADM-1, hat 4}` (and the frame prerequisite of ADM-2) sit at the source; ADM-2's
depolarization driver is the transverse connection one arrow downstream; R1 is the
generator two arrows downstream.

## What the runner verifies (exact)

1. `su(3)` basis is `8`-dimensional, traceless anti-Hermitian.
2. Frame stabilizer dimension `= 2` (maximal torus `T^2`) for several random record
   frames `B`; residual connection freedom `8 − 2 = 6 > 0` (arrow 1 not onto).
3. The stabilizer connection is color-diagonal in the frame and gives `S = I3`
   (block-07 no-depolarization); a transverse connection gives all-nonzero `S`
   (depolarization-capable). Depolarization data is transverse to the frame.
4. A regular `V` exponentiates from `≥ 5` distinct valid `su(3)` generators with
   separations growing without bound (arrow 2 not onto; `Z`-lattice, not a finite set).
5. Composition: a gap at each arrow; the record axiom delivers neither endpoint; NO hat
   discharged (each downstream object remains undelivered — the theorem strengthens the
   obstruction, it does not deliver any pointer set, connection, or generator).

## Honest boundary — what this does NOT do

- It does **not** discharge any hat. It is a non-reduction (a sharper obstruction): it
  exhibits the exact residual at each arrow and shows the record axiom delivers no
  endpoint. Supplying a named `{P_r}`, a named connection `V`, or a named generator
  branch remains an undelivered conditional input at the corresponding arrow.
- It does **not** claim a partition map for the irreducible triplet. `{P_r}` is used as
  a supplied record frame (a free choice, not covariant); its SU(3) stabilizer being only
  `T^2` is consistent with the block-10 absence of any nontrivial SU(3)-invariant
  projector.
- The chain is the campaign's induced-object chain on the supplied `C^3` carrier; it is
  conditional on that carrier and on the composite-link construction that introduces the
  connection `V`. It does not assert that any particular frame, connection, or generator
  is the framework's realized object.
- ADM-2's second consolidated facet — the global color-singlet / Gauss-law condition
  (block 09 mechanism B) — is an import on the matter STATE, off this single-edge chain;
  this note addresses only the local frame/connection/generator facet.
- Arrow 2's `Z`-lattice is the generic regular-`V` count; degenerate-spectrum connections
  carry an even larger (continuous) generator ambiguity, only widening the gap.

## No-Go Discipline Gate

Negative/non-reduction claim: fixing an upstream object in the displayed chain
does not deliver the downstream object, and the four hats do not collapse to one
missing input.

- **N1 alternative routes:** (1) frame could determine connection — ruled out
  by the exact `T^2` stabilizer, leaving six transverse directions; (2) the
  residual torus could depolarize — ruled out by `S = I3`; (3) a holonomy could
  select a generator — ruled out by the infinite logarithm lattice; (4) Record
  could supply the missing frame or generator — ruled out only by the cited
  retained Record no-go rows; (5) a larger composite dynamics could supply one
  of the objects — not ruled out, and explicitly left as the corresponding
  undelivered input.
- **N2 wall independence:** the supplied `C^3` carrier, supplied frame,
  supplied connection, generator branch choice, and retained Record no-go
  boundaries are distinct. Closing the frame gap would not choose a logarithm
  branch; choosing a generator would not choose a record frame; deriving a
  frame or connection in future dynamics would retire only that arrow.
- **N3 hidden-wall scan:** the supplied carrier, supplied `{P_i}`, regular
  connection `V`, composite-link chain, and retained Record no-go boundaries
  are named. The theorem claims no realized frame, connection, generator,
  probability rule, readout weighting, or dynamics.
- **N4 residual matching:** the frame endpoint cites
  `record_formation_not_unconditionally_forced`; the generator endpoint cites
  `record_markov_generator_embeddability_boundary`; block-07/09/10 rows are
  contextual campaign targets, while the runner re-derives the decisive
  stabilizer, unistochastic, and logarithm facts.
- **N5 rhetoric audit:** "does not collapse" is scoped to the displayed
  frame → connection → generator chain on the supplied `C^3` carrier. It is
  not a universal no-go against future dynamics deriving a particular object.
- **N6 partial-closure scan:** no approved axiom, primitive, convention, or
  retained theorem currently supplies the missing frame, connection, or
  generator branch. Any owner-approved primitive or future retained theorem
  would retire the corresponding missing input, not silently collapse all
  arrows.
- **N7 steelman:** a future retained color dynamics could select a pointer
  frame, connection, and generator jointly. That would be real progress and
  would discharge hats; it would not contradict the present algebraic
  non-reduction, which says none of those selections follows from the upstream
  object alone.
- **N8 cross-cycle echo:** blocks 09 and 10 already reduced several hats to a
  shared record-frame root. This note preserves that progress but prevents an
  over-collapse: the per-arrow residuals remain distinct unless future work
  supplies the named missing object.

## Citations (verified live on current `main`)

- `record_classical_semigroup_boundary_2026-06-06` — retained.
- `record_markov_generator_embeddability_boundary_2026-06-06` — retained_no_go.
- `record_formation_not_unconditionally_forced_by_minimal_axioms...` — retained_no_go.
- `graph_first_su3_integration_note`, `cl3_color_automorphism_theorem` — retained.
- Block-07/09/10 per-mechanism notes and the composite-link / blocking-isometry source
  proposals are cited for framing only; this runner re-derives all decisive algebra and
  consumes none of them as inputs.
