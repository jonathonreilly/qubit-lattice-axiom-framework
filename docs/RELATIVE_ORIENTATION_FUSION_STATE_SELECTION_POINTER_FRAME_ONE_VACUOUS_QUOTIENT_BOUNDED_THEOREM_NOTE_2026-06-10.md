# Relative-Orientation Fusion: the Open-Shell State Selection and the Instrument-Frame Orientation Share One Vacuous Global Quotient

**Date:** 2026-06-10
**Type:** bounded theorem (retire-mode; resolves the parked shape-question between two named residuals)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_relative_orientation_fusion_state_frame_quotient_2026_06_10.py`
**Cache:** `logs/runner-cache/frontier_relative_orientation_fusion_state_frame_quotient_2026_06_10.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=14 FAIL=0`, exact, no MC.

## The parked question

PR #3474 ended with a deliberately unclaimed shape-observation: *the open-shell
degenerate-manifold selection (admission (B)'s residual) has the same shape as the
pointer-frame root `{P_r}` — a selection on a degeneracy the framework doesn't canonically
supply. Are they the same residual?* The "two things share a shape ⟹ same root" move is
the unification over-reach family panel-caught twice on 2026-06-08 — so this note answers
the question **precisely**, and the precise answer is **neither identification nor
independence**.

## The theorem (exact — runner `PASS=14 FAIL=0`)

Consider the **joint parameter space** of the two selections: `(state ρ on the color
carrier) × (instrument color frame(s) u)` — admission (B)'s open-shell residual times the
pointer-frame root.

**(F1) Diagonal vacuity.** Every record-level consequence — single-step outcome
probabilities, post-instrument states (covariant, so all longer sequences inherit it by
induction), and multi-step record distributions — is **exactly invariant** under the
simultaneous rotation `(ρ, u) → (gρg†, gu)`, `g ∈ SU(3)` (trace cyclicity; verified to
`10⁻¹⁶` over Haar trials). **The two absolute color orientations are jointly
unregistrable: the joint space carries one vacuous global-SU(3) quotient — 8 directions
once.** Non-circularity: F1 presupposes only common-`g` conjugation of frame-*dependent*,
non-invariant observables `B = uPu†` — pure cyclicity, **not** the gauge-invariance
premise (the panel probed: `B` is genuinely non-invariant, dev `1.27`, yet co-rotation
holds). The jointly-vacuous direction is the standard inert global-SU(3) covariance of
the whole state-plus-instrument setup (cf. #3436 on main: *"Covariance is not
contraction. The identity channel is SU(3)-covariant and inert"*). And the "8 once" is
**internal joint-space bookkeeping** — no prior note ever tracked these as two
independent 8-dimension admissions; the bookkeeping clarifies the joint parameter space,
it does not collapse any previously-counted residual.

**(F2) Teeth — the fusion is not collapse.** Rotating the state *alone* changes registered
content at order 1 (shift `0.22`); rotating the frame family *alone* likewise (`0.19`).
Neither absolute orientation is vacuous with the other held fixed: **the relative
orientation is registrable — only under a frame-naming (commutant-breaking) instrument;
under a color-blind (invariant) instrument it is vacuous, reproducing #3458** (the F4
control proves this inline at `10⁻¹⁷`). This is a **complementary** statement to #3458
about a *different instrument class* — #3458 retires state orientation *given* invariant
observables; F2 characterizes what becomes registrable when that premise is dropped. It
does **not** widen #3458's retirement.

**(F3) Sharpness — no hidden extra vacuity.** At a generic point, the kernel of the
registered-content differential on the 16 absolute-orientation directions is **exactly**
10-dimensional: the 8 diagonal directions plus the 2 trivial state-stabilizer flows
(which move nothing). Rank 6, computed. And the frame family is **tomographically
complete** — the content functional determines `ρ` exactly (`10⁻¹⁶`), so no further
unregistered direction hides in the family.

**(F4) Fock-level application — the actual #3474 instance.** For a color-*asymmetric*
ground state of the open-shell manifold (`L=3`, `n_f=2`/color; `ρ_color ≠ I₃/3` at the
ground energy; the many-body fixed-`N=6` ground manifold here has degeneracy `20` —
distinct from #3474's *single-particle cubic* Fermi-shell counts `12/20`, which concern a
different object) and a color-frame-naming occupation instrument: the record distribution is
exactly invariant under the diagonal rotation (`10⁻¹⁶`), changes under a state-only
rotation (`0.054` — the open-shell selection's orientation is registrable **only relative
to the instrument frame**), and is invariant under state-only rotation when the instrument
is color-blind (`10⁻¹⁷` — #3458's case, reproduced at the Fock level).

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
  the orbit invariants (which `ρ_color` spectrum, the #3474 ledger's irreducible core);
  for the frame side, the instrument class plus the **relative orientation**.
- **Admission (B) / global color-neutrality refined, not discharged — and the local
  ADM-1 frame root `{P_r}` is UNTOUCHED:** the rotation here is **global** (one `g` at
  every site), so per #3458's own boundary (a global rotation "does not deliver a local
  connection... supplying no per-edge link data") this theorem cannot and does not refine
  the static *local* per-site frame root. What fuses is the **global** orientation pair:
  the state's global color orientation (the (B)-side datum) and the instrument family's
  global frame orientation. The `{P_r}` which-partition residual stands exactly as the
  stratification theorem left it. The (B)-side refinement: the open-shell residual's
  registrable content is exactly its orbit-invariant part (the spectrum data #3474
  priced); its orientation part was never independently registrable to begin with.
- **No weight is assigned anywhere** (the theorem identifies vacuous *directions*, fixes
  no values); `r` is untouched (generation factor — no part of this argument reaches it).
- **Conditional on:** the supplied `C³` color carrier; the named instrument classes
  (frame-naming occupation / color-blind occupation); where dynamics appears, the named
  color-diagonal hopping (global color rotations commute with it — the retained commutant
  structure, `graph_first_su3_integration_note` lineage).

## Cross-references

- The parked observation and the open-shell residual: PR #3474
  (`PAULI_CLOSED_SHELL_COLOR_MARGINAL_DISCHARGE_DISCRETE_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-10`)
  — **not yet on origin/main** (branch-only source proposal); F4/F5 stand on the algebra
  verified here, not on that note's grade.
- The orientation retirement this complements (different instrument class): PR #3458, on
  main as [`COLOR_ORIENTATION_OF_THE_STATE_IS_PREDICTIVELY_VACUOUS_NARROW_THEOREM_NOTE_2026-06-09`](COLOR_ORIENTATION_OF_THE_STATE_IS_PREDICTIVELY_VACUOUS_NARROW_THEOREM_NOTE_2026-06-09.md)
  (commit `e38c379e2`).
- The pointer-frame root: the four-hats stratification (PR #3453) and the campaign
  consolidation (blocks 04–10, on main).
- The unistochastic pointer-frame fork (instrument-side structure): PR #3436 (on main).
- Standard math (method only): trace cyclicity; group actions and stabilizers; quantum
  state tomography; Jordan–Wigner Fock lifts of one-body rotations.
