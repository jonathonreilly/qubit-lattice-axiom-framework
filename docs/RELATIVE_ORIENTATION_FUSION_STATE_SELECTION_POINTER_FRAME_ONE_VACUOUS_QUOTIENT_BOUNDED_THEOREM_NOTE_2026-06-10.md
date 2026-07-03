# Relative-Orientation Fusion: the Open-Shell State Selection and the Instrument-Frame Orientation Share One Vacuous Global Quotient

**Date:** 2026-06-10
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** Deterministic machine-precision theorem on the joint state/frame
parameter space for a supplied `C^3` color carrier and the named instrument classes.
It identifies one shared vacuous **global** SU(3) orientation quotient and leaves the
local ADM-1 frame root, state-selection invariant content, relative orientation, and
all weights untouched.
**Primary runner:** [`scripts/frontier_relative_orientation_fusion_state_frame_quotient_2026_06_10.py`](../scripts/frontier_relative_orientation_fusion_state_frame_quotient_2026_06_10.py)
**Runner cache:** [`logs/runner-cache/frontier_relative_orientation_fusion_state_frame_quotient_2026_06_10.txt`](../logs/runner-cache/frontier_relative_orientation_fusion_state_frame_quotient_2026_06_10.txt) (PASS=14, FAIL=0)
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.

## The parked question

The Pauli open-shell color-marginal note parked a deliberately unclaimed
shape-observation: *the open-shell degenerate-manifold selection (admission (B)'s
residual) has the same shape as the pointer-frame root `{P_r}` — a selection on a
degeneracy the framework doesn't canonically supply. Are they the same residual?*
The "two things share a shape ⟹ same root" move is
the unification over-reach family panel-caught twice on 2026-06-08 — so this note answers
the question **precisely**, and the precise answer is **neither identification nor
independence**.

## The theorem (machine-precision runner `PASS=14 FAIL=0`)

Consider the **joint parameter space** of the two selections: `(state ρ on the color
carrier) × (instrument color frame(s) u)` — admission (B)'s open-shell residual times the
pointer-frame root.

**(F1) Diagonal vacuity.** Every record-level consequence tested here — single-step
outcome probabilities, post-instrument states (covariant, so all longer sequences inherit
it by induction), and multi-step record distributions — is invariant under the
simultaneous rotation `(ρ, u) → (gρg†, gu)`, `g ∈ SU(3)` (trace cyclicity; verified to
`10⁻¹⁶` over Haar trials). **The two absolute color orientations are jointly
unregistrable: the joint space carries one vacuous global-SU(3) quotient — 8 directions
once.** Non-circularity: F1 presupposes only common-`g` conjugation of frame-*dependent*,
non-invariant observables `B = uPu†` — pure cyclicity, **not** the gauge-invariance
premise (the panel probed: `B` is genuinely non-invariant, dev `1.27`, yet co-rotation
holds). The jointly-vacuous direction is the standard inert global-SU(3) covariance of
the whole state-plus-instrument setup (cf. the unistochastic pointer-frame fork: *"Covariance is not
contraction. The identity channel is SU(3)-covariant and inert"*). And the "8 once" is
**internal joint-space bookkeeping** — no prior note ever tracked these as two
independent 8-dimension admissions; the bookkeeping clarifies the joint parameter space,
it does not collapse any previously-counted residual.

**(F2) Teeth — the fusion is not collapse.** Rotating the state *alone* changes registered
content at order 1 (shift `0.22`); rotating the frame family *alone* likewise (`0.19`).
Neither absolute orientation is vacuous with the other held fixed: **the relative
orientation is registrable — only under a frame-naming (commutant-breaking) instrument;
under a color-blind (invariant) instrument it is vacuous, reproducing the color-orientation
retirement control** (the F4
control proves this inline at `10⁻¹⁷`). This is a **complementary** statement
about a *different instrument class* — the color-orientation retirement note retires state
orientation *given* invariant
observables; F2 characterizes what becomes registrable when that premise is dropped. It
does **not** widen that retirement.

**(F3) Sharpness — no hidden extra vacuity in the tested family.** At a generic point, the
finite-difference kernel check on the 16 absolute-orientation directions is
10-dimensional: the 8 diagonal directions plus the 2 trivial state-stabilizer flows
(which move nothing). Rank 6, computed. And the frame family is **tomographically
complete to numerical precision** — the content functional determines `ρ` to `10⁻¹⁶`, so no further
unregistered direction hides in the family.

**(F4) Fock-level application — the Pauli open-shell instance.** For a color-*asymmetric*
ground state of the open-shell manifold (`L=3`, `n_f=2`/color; `ρ_color ≠ I₃/3` at the
ground energy; the many-body fixed-`N=6` ground manifold here has degeneracy `20` —
distinct from the Pauli note's *single-particle cubic* Fermi-shell counts `12/20`, which concern a
different object) and a color-frame-naming occupation instrument: the record distribution is
invariant under the diagonal rotation to `10⁻¹⁶`, changes under a state-only
rotation (`0.054` — the open-shell selection's orientation is registrable **only relative
to the instrument frame**), and is invariant under state-only rotation when the instrument
is color-blind (`10⁻¹⁷` — the color-orientation retirement case, reproduced at the Fock level).

**(F5) Non-identification — the residuals' remainders are distinct.** With frames fixed,
states with different `ρ_color` *spectra* give different content: the state selection
keeps instrument-independent registrable content (its orbit invariants). With the state
fixed, the two instrument *classes* (frame-naming vs color-blind) give different content:
the frame-side residual keeps its own class datum. **The selections fuse at their
orientation parts only.**

## What this resolves, refines, and leaves open

- **The parked question, resolved precisely:** the open-shell selection and the
  pointer-frame selection are **not** the same residual (F5) and **not** independent
  residuals (F1/F3): their absolute-orientation parts **fuse into one shared vacuous
  SU(3) quotient**, and their registrable remainders are distinct — for the state side,
  the orbit invariants (which `ρ_color` spectrum, the Pauli note's irreducible core);
  for the frame side, the instrument class plus the **relative orientation**.
- **Admission (B) / global color-neutrality refined, not discharged — and the local
  ADM-1 frame root `{P_r}` is UNTOUCHED:** the rotation here is **global** (one `g` at
  every site), so per the color-orientation retirement boundary (a global rotation "does not deliver a local
  connection... supplying no per-edge link data") this theorem cannot and does not refine
  the static *local* per-site frame root. What fuses is the **global** orientation pair:
  the state's global color orientation (the (B)-side datum) and the instrument family's
  global frame orientation. The `{P_r}` which-partition residual stands exactly as the
  stratification theorem left it. The (B)-side refinement: the open-shell residual's
  registrable content is exactly its orbit-invariant part (the spectrum data the Pauli note
  priced); its orientation part was never independently registrable to begin with.
- **No weight is assigned anywhere** (the theorem identifies vacuous *directions*, fixes
  no values); `r` is untouched (generation factor — no part of this argument reaches it).
- **Conditional on:** the supplied `C³` color carrier; the named instrument classes
  (frame-naming occupation / color-blind occupation); where dynamics appears, the named
  color-diagonal hopping (global color rotations commute with it — the graph-first SU(3) commutant
  structure, `graph_first_su3_integration_note` lineage).

## Load-bearing inputs

- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md) — retained
  graph-first SU(3) commutant lineage for the named color-diagonal hopping context.
- Standard finite-dimensional matrix mechanics: trace cyclicity, group actions and
  stabilizers, quantum state tomography, and Jordan-Wigner Fock lifts of one-body rotations.
- Supplied bounded context: `C^3` color carrier and the named frame-naming / color-blind
  instrument classes.

## Context Only

Plain-text reader pointers below are non-load-bearing and intentionally not markdown-linked:

- `PAULI_CLOSED_SHELL_COLOR_MARGINAL_DISCHARGE_DISCRETE_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-10.md`
  — parked the shape question and supplies the open-shell motivation; F4/F5 stand on this
  note's runner algebra, not on that note's grade.
- `COLOR_ORIENTATION_OF_THE_STATE_IS_PREDICTIVELY_VACUOUS_NARROW_THEOREM_NOTE_2026-06-09.md`
  — color-blind orientation retirement control reproduced inline here.
- `FOUR_HATS_FRAME_CONNECTION_GENERATOR_STRATIFICATION_NON_REDUCTION_NARROW_THEOREM_NOTE_2026-06-09.md`
  — local `{P_r}` frame-root context left untouched.
- `COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09.md`
  — instrument-side pointer-frame fork context.
