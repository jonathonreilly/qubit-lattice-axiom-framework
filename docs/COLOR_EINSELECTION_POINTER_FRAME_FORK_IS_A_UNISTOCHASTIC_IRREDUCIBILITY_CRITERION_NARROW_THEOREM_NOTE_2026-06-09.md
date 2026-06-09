# The Color-Einselection Pointer-Frame Fork Is a Unistochastic-Irreducibility Criterion

**Date:** 2026-06-09
**Type:** narrow theorem (an exact channel / Markov-chain criterion resolving the
einselection pointer-frame multiplicity fork) — relocates ST2's ADM-2 open input from
"is a multi-frame averaging admitted?" onto a concrete matter-dynamics property
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_color_einselection_pointer_frame_unistochastic_criterion_2026_06_09.py`
**Cache:** `logs/runner-cache/frontier_color_einselection_pointer_frame_unistochastic_criterion_2026_06_09.txt`
**Status:** source proposal. The statements are exact finite-dimensional channel and
Markov-chain algebra (no Monte-Carlo fit enters the derivation path; random states are
only witnesses for already-proven identities). Authority role: source proposal; the
independent audit lane sets any retained status.

## Context

The gauge-link / color-einselection dynamics frontier has four undelivered inputs (the
"four hats"): the static local-frame redundancy **ADM-1**, a continuous-time gauge-link
**generator R1** (arrow + rate), the mixing regime **R2** that delivers the heat-kernel
convolution attractor, and the **blocking-isometry** selection.

R2's premise reduces (source proposals, `unaudited` on the live ledger at drafting —
cited as proposals, not as retained) to **ADM-2**: the emergent-time gauge-link step
measure is Ad-invariant. Block 04 of this campaign
(`MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE...`, on `main` via
the closed-PR-#3431 cherry-pick, still `unaudited`) sharpened ADM-2 to a **necessary
condition on a matter order parameter**: the step measure can be Ad-invariant only if the
coupled matter color density is unpolarized, `ρ_color = I₃/3`. Block 05 (PR #3433, OPEN at
drafting; cited as a source proposal) then proved a **single-frame impossibility**: a
single projective record frame — and any color-blind instrument — fixes the entire
diagonal subalgebra in that frame (a 2-simplex of states), not the single point `I₃/3`, so
a generic state stays polarized. Block 05 exhibited a **conditional multi-frame
sufficiency**: two complementary (mutually unbiased) frames, or a finite irreducible
twirl, drive `ρ_color → I₃/3`, but that averaging is a **named multi-instrument
admission** Record does not supply.

That left an explicit fork (block 05's named successor):

> **Does the framework's einselection layer select ONE preferred color pointer frame**
> (whence the single-frame impossibility stands and depolarization fails), **or a
> complementary multi-frame set** (whence depolarization is admitted)?

Block 05's single-frame impossibility was proved for a single dephasing acting **alone**.
But the einselection layer also carries the **coherent matter (hopping) evolution** between
record steps. This note resolves the fork by analysing the two together.

## Retained grounds used (verified on the live ledger at drafting)

- `graph_first_su3_integration_note` — **retained**: global `SU(3)` is the commutant of
  the observables; color is the irreducible fundamental triplet. (Used: `I₃/3` is the
  unique `SU(3)`-invariant density; conjugation `X → g X g†` is the color action.)
- `record_classical_semigroup_boundary_2026-06-06` — **retained**, and
  `record_markov_generator_embeddability_boundary_2026-06-06` — **retained_no_go**: the
  Record axiom supplies no continuous Markov generator, rate, weighting, or normalization.
- `record_formation_not_unconditionally_forced_by_minimal_axioms_narrow_no_go_note_2026-06-06`
  — **retained_no_go**: record formation is not unconditionally forced, so any record
  instrument / frame is a **named admission**.

Source proposals cited as proposals (not retained): the block-04 necessary condition (on
`main` via closed-PR-#3431, `unaudited`); block 05's single-frame impossibility / conditional
multi-frame sufficiency dichotomy
(`COLOR_DEPOLARIZATION_REQUIRES_MULTIFRAME_AVERAGING...`, PR #3433); the two-instrument
einselection language — frame-naming (I-A) and color-blind total-occupation Lueders (I-B) —
from `record_instrument_composite_link_pointer_erasure_exact_slaving_bounded_theorem_note_2026-06-09`
and `persistent_record_instrument_construction_narrow_theorem_note_2026-05-22` (both
`unaudited`).

Doubly-stochastic / unistochastic matrices, Perron–Frobenius irreducibility/primitivity,
and the predictability sieve are standard mathematics, cited as method and reproduced
exactly by the runner.

## Setup

`ρ_color` is the `3×3` Hermitian color reduced density (`tr ρ = 1`). One **named record
frame** `B = {|e_i⟩}` (the block-02 frame-naming instrument I-A, an admission) acts as the
complete projective dephasing channel `D_B(X) = Σ_i P_i X P_i` with rank-one `P_i =
|e_i⟩⟨e_i|`. The coherent matter color dynamics acts between record steps as a unitary kick
`Ad_U(ρ) = U ρ U†`. One emergent-time step of the einselection layer is the composite
**predictability-sieve channel**

> `Φ(ρ) = D_B( U ρ U† )`.

The **order parameter** is the color purity above its floor (the same one as blocks 04/05),
`P(ρ) = Tr(ρ²) − 1/3 = ‖traceless(ρ)‖_F² ≥ 0`, with `P = 0` iff `ρ = I₃/3`. "Depolarize"
means drive `P → 0`.

## Theorem (the fork is a unistochastic-irreducibility criterion; exact)

> Define the **unistochastic matrix** `S_ij = |⟨e_i|U|e_j⟩|²`. Then:
>
> 1. `Φ` maps every state into the `B`-diagonal subalgebra in one step, and on that
>    subalgebra `Φ(diag p) = diag(S p)`. `S` is doubly stochastic for every unitary `U`,
>    so `I₃/3` is always a fixed point.
> 2. The **color pointer states** (fixed points of `Φ`) are exactly the `B`-diagonal
>    states whose probability vector is `S`-stationary. Hence the fixed-point set is a
>    single point iff `S` is **irreducible**, and `Φⁿ(ρ) → I₃/3` for every `ρ` iff `S` is
>    **primitive** (irreducible **and** aperiodic).
> 3. Three regimes:
>    - **`[U,B] = 0`** (`U` diagonal in `B`): `S = I`, the entire `B`-diagonal 2-simplex
>      is fixed. Frame `B` is einselected, every `B`-basis state is a stable color pointer
>      state, and `ρ_color` is **not** depolarized — this **recovers block 05's
>      single-frame polarized boundary** as the commuting limit.
>    - **`S` reducible** (`U` block-diagonal): `≥ 2` ergodic classes, multiple pointer
>      states, color information survives, **no** depolarization.
>    - **`S` primitive** (sufficient: `U` has no zero amplitude in `B`): the **unique**
>      color pointer state is `I₃/3` and `Φⁿ(ρ) → I₃/3` — color is fully einselected away
>      with the **single** record frame `B`. The complementary "second frame" is supplied
>      by the matter unitary `U`, not by a second instrument.
> 4. `P(ρ)` is a strict Lyapunov function under a primitive step: it decreases
>    monotonically to `0`.

**Proof.**

*(1)* `D_B` projects onto diagonals, so `range Φ ⊆` diagonal subalgebra — one step. For a
diagonal input, `[U (diag p) U†]_ii = Σ_j |U_ij|² p_j = (S p)_i`, giving
`Φ(diag p) = diag(S p)`. Unitarity gives `Σ_i |U_ij|² = Σ_j |U_ij|² = 1`, so `S` is doubly
stochastic and `S·(1/3,1/3,1/3)ᵀ = (1/3,…)ᵀ`, i.e. `Φ(I₃/3) = I₃/3`. `Φ` is CPTP
(composition of a unitary conjugation and a Lueders channel).

*(2)* A fixed point must lie in `range Φ` (diagonal) and satisfy `p = S p`. For a doubly
stochastic `S`, Perron–Frobenius gives: a unique stationary distribution iff `S` is
irreducible (one ergodic class), and `Sⁿ → J/3` (the uniform projector) iff `S` is
primitive. Since `Φ` collapses to `S` on the diagonal after one step, `Φⁿ(ρ) → I₃/3` iff
`S` is primitive.

*(3)* `[U,B]=0 ⇒ |U_ij|² = δ_ij ⇒ S = I`: every diagonal state is fixed. Block-diagonal
`U ⇒ S` block-diagonal (reducible): each block carries its own stationary content. A
strictly positive `S` (every `|U_ij|² > 0`) is primitive (Perron–Frobenius), so the
unique stationary distribution is uniform and `Φⁿ → I₃/3`.

*(4)* `P` is convex and `S`-contractive: `‖S p − 1/3‖` decreases under a primitive doubly
stochastic `S` (the second-largest singular value is `< 1`), and `P(diag p) = ‖p‖² − 1/3`
is monotone in `‖p − 1/3‖`. ∎

## What this resolves, and what it does not

**The fork resolves into a property of the matter unitary relative to the record frame.**
Einselection does not, by itself, select a single color pointer frame: whether a robust
color pointer frame survives is governed entirely by `S`'s reducibility. When the matter
unitary commutes with the admitted record frame, frame `B` is einselected and color stays
polarized (block 05's single-frame regime). When the matter unitary mixes that frame
(`S` primitive), **no** color pointer frame survives and `ρ_color` depolarizes to `I₃/3` —
with a **single** record frame. The matter dynamics supplies the complementarity that
block 05 obtained from a second instrument; the two-instrument multi-frame averaging
admission is therefore **not** the only route to depolarization.

**Relocation (no hat discharged).** This is a criterion, not a delivery. Depolarization
under a single record frame holds **iff** `S` is primitive, and `S`'s primitivity is a
property of the coupled matter color unitary relative to the admitted frame `B`. Record
supplies **neither** the frame (a named admission on the `retained_no_go`
record-formation ground) **nor** the matter unitary's alignment to it. So ADM-2's open
input relocates a third time: from block 05's "is a multi-frame averaging admitted?" onto

> **does the derived matter color unitary mix the admitted record frame — is `S`
> primitive (e.g. no zero amplitude in `B`)?**

— a concrete property checkable on the staggered-Dirac matter realization (a separate
lane), undelivered here. None of the four hats is discharged: ADM-1 (static frame
redundancy), R1 (a continuous-time link generator with arrow + rate), R2's delivery, and
the blocking isometry are untouched, and no ST1-vs-ST2 ranking is made.

## Guards (panel-relevant)

- **`SU(3)`-covariance is not contraction.** The identity channel is `SU(3)`-covariant yet
  inert (runner C10), consistent with block 05's color-blind I-B being inert. `Φ` itself is
  frame-fixed (not globally `SU(3)`-covariant) — covariance is instrument-inherited, as in
  block 02/03.
- **Not a sufficiency-from-axioms claim.** Depolarization follows only **conditionally** on
  the named record frame **and** `S` primitivity (the undelivered input). This is the same
  conditional-sufficiency status as block 05's multi-frame exhibit, in the converse, more
  economical direction; it is distinct from the refuted first-moment "annealed-twirl =
  central CLT" **sufficiency**.
- **Fixed-point uniqueness vs relaxation are different.** Irreducibility gives a unique
  stationary state; **primitivity** (also aperiodic) is needed for `Φⁿ` to actually relax
  (runner C7: a cyclic-permutation `U` is irreducible but periodic — unique fixed point,
  yet oscillation, with only a Cesàro average equal to `I₃/3`). The relocation names
  **primitivity**, not mere irreducibility.
- **Single record frame; no purity-conservation claim.** Reduced color purity is not
  conserved under a global unitary, and `Φ` is a genuine contraction on the diagonal — no
  conservation law is invoked.

## Does NOT close

This note does not derive depolarization from the axioms, does not establish that the
staggered-Dirac matter unitary is primitive in any record frame, does not deliver R1, and
makes no claim about ADM-1, R2's delivery, or the blocking isometry. The record frame `B`
remains a named admission; `S`'s primitivity is a new, undelivered open input on the
matter-realization lane. The result is the exact criterion plus the relocation, on the
single-edge / single-frame color carrier with a complete (`λ = 1`) record step.

## Computed content

Runner `frontier_color_einselection_pointer_frame_unistochastic_criterion_2026_06_09.py`,
`TOTAL: PASS=28 FAIL=0` (exact 3×3 color algebra; random states are witnesses only):
C1 one-step diagonalization + CPTP; C2 `Φ(diag p) = diag(S p)`; C3 `S` doubly stochastic
(incl. `d=2`); C4 `I₃/3` always fixed; C5 commuting limit recovers block-05 polarized
boundary; C6 reducible `S` → surviving sector; C7 irreducible-but-periodic oscillation +
Cesàro `I₃/3`; C8 primitive `S` → unique `I₃/3` + relaxation, strictly-positive sufficient
condition; C9 `P` Lyapunov; C10 covariance ≠ contraction guard; C11 the verdict depends on
`S` (diagonal-phase-dressing invariant) alone.
