# Color Depolarization to I₃/3 Requires a Multi-Frame Averaging Structure, Not a Single Record Frame

**Date:** 2026-06-09
**Type:** narrow theorem (a single-frame impossibility + a conditional multi-frame
sufficiency exhibit) — relocates ST2's ADM-2 open input onto a named multi-frame
averaging admission
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_color_depolarization_requires_multiframe_averaging_2026_06_09.py`
**Cache:** `logs/runner-cache/frontier_color_depolarization_requires_multiframe_averaging_2026_06_09.txt`
**Status:** source proposal. The statements are exact finite-dimensional `su(3)`
representation-theory and channel facts (no Monte-Carlo fit enters the derivation path).
Authority role: source proposal; the independent audit lane sets any retained status.

## Context

The gauge-link / color-einselection dynamics frontier has four undelivered inputs (the
"four hats"): the static local-frame redundancy **ADM-1**, a continuous-time gauge-link
**generator R1** (arrow + rate), the mixing regime **R2** that delivers the heat-kernel
convolution attractor, and the **blocking-isometry** selection.

R2's premise was reduced (source proposals, `unaudited` on the live ledger at drafting —
cited as proposals, not as retained) to **ADM-2**: *the emergent-time gauge-link step
measure is Ad-invariant (bi-invariant)*, whence any bi-invariant per-step kernel flows
under convolution to the heat kernel `exp(t Δ / 2)`
(`adm2_global_su3_symmetry_reduces_action_form_bi_invariance_narrow_theorem_note_2026-06-08`).
Block 04 of this campaign
(`MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE...`; landed on
`main` via cherry-pick when PR #3431 was closed; still `unaudited` — no ledger row —
so cited as a source proposal, not retained) sharpened ADM-2 to a **necessary
condition on a matter order parameter**: the step measure can be Ad-invariant only if
the coupled matter color density is unpolarized, `ρ_color = I₃ / 3`. That left exactly
one open input:

> **Does the framework's dynamics depolarize `ρ_color` to `I₃ / 3`** (the color-blind /
> confined ensemble)?

This note attacks that converse open input. It does **not** derive depolarization from
the axioms; it proves what is and is not capable of delivering it, and relocates the open
input onto a sharper named admission.

## Retained grounds used (verified on the live ledger at drafting)

- `graph_first_su3_integration_note` — **retained**: global `SU(3)` is the commutant of
  the observables; color is the irreducible fundamental triplet. (Used: `I₃/3` is the
  unique `SU(3)`-invariant density; conjugation `X → g X g†` is the color action.)
- `record_classical_semigroup_boundary_2026-06-06` — **retained**, and
  `record_markov_generator_embeddability_boundary_2026-06-06` — **retained_no_go**: the
  Record axiom supplies no continuous Markov generator, rate, weighting, or
  normalization. (Used: a `≥2`-element averaging structure is a weighting over
  instruments and is not supplied by Record.)
- `record_formation_not_unconditionally_forced_by_minimal_axioms_narrow_no_go_note_2026-06-06`
  — **retained_no_go**: record formation is not unconditionally forced, so any record
  instrument/frame is a **named admission**.

Source proposals cited as proposals (not retained): the block-04 necessary condition
(on `main` via the closed-PR-#3431 cherry-pick, still `unaudited`); the two-instrument
einselection language — frame-naming (I-A) and color-blind
total-occupation Lueders (I-B) — from
`record_instrument_composite_link_pointer_erasure_exact_slaving_bounded_theorem_note_2026-06-09`
(`unaudited`) and `persistent_record_instrument_construction_narrow_theorem_note_2026-05-22`
(`unaudited`).

The `su(3)` representation facts (irreducible triplet; `I₃/3` the unique invariant
state), the qutrit mutually-unbiased-basis overlaps `1/3`, and the Heisenberg–Weyl
displacement operators are standard mathematics, cited as method and reproduced exactly
by the runner.

## Setup

`ρ_color` is the `3×3` Hermitian color reduced density (`tr ρ = 1`), the same object
block 04 named. The **order parameter** is the color purity above its floor,

> `P(ρ) = ‖traceless(ρ)‖_F² = Tr(ρ²) − 1/3`,

exact, `≥ 0`, and `= 0` iff `ρ = I₃/3` (the same order parameter as block 04). "Depolarize"
means drive `P → 0`. The available actions on this sector are the einselection-layer
record instruments (block 02: a frame-naming projective dephasing I-A, or a color-blind
total-occupation Lueders I-B) and the coherent matter (hopping) evolution.

## Theorem (single-frame impossibility; exact, model-independent)

> **No single projective record frame, and no color-blind instrument, can depolarize
> `ρ_color` to `I₃/3`.** A single Lueders dephasing in one orthonormal color frame fixes
> the entire diagonal subalgebra in that frame — a 2-simplex of states, not the single
> point `I₃/3` — so a generic state stays polarized (`P > 0`). A color-blind
> (`SU(3)`-covariant, scalar-projector) instrument has `I₃` as its only invariant
> projector on the triplet and therefore acts as the identity on `ρ_color`, contracting
> nothing.

**Proof.**

1. **Unique invariant (D1).** The only Hermitian `X` with `[λ_a, X] = 0` for all eight
   Gell-Mann generators is a multiple of `I` (Schur on the irreducible triplet); the
   runner computes the solution space of `[λ_a, ·] = 0` and finds it exactly
   one-dimensional. Hence `I₃/3` is the unique invariant density and `P` vanishes only
   there.
2. **Single frame (D2).** A projective Lueders channel `D_B(ρ) = Σ_k P_k ρ P_k` with
   rank-1 `P_k` from one orthonormal frame `B` maps every `ρ` into the diagonal
   subalgebra of `B` and fixes every diagonal state. Its fixed-point set is the
   population 2-simplex `{diag(p₁,p₂,p₃) : Σ pᵢ = 1}`, which has two free dof and is not
   the single point `I₃/3`. The runner exhibits a fully-dephased polarized state with
   `P = 0.127 > 0`.
3. **Color-blind instrument (D3).** The color-blind total-occupation Lueders (I-B) has,
   on the single-particle triplet, the lone invariant projector `I₃`; the channel
   `ρ ↦ I₃ ρ I₃ = ρ` is the identity. It registers no color content and contracts
   nothing.

## Conditional sufficiency (exhibited admission space; exact constructions)

> **A `≥2`-element averaging structure DOES depolarize `ρ_color` to `I₃/3`, exactly.**
> (a) Cycling two **mutually unbiased** color frames (computational + Fourier): because
> all MUB overlaps equal `1/3`, dephasing in one then the other yields **exactly** `I₃/3`
> in two steps. (b) A **finite irreducible twirl**: the uniform average over the nine
> Heisenberg–Weyl displacement operators yields **exactly** `I₃/3` in one step. Along both
> routes `P` is non-increasing and reaches `0`.

These are **sufficiency exhibits conditional on a named admission**: they show what a
multi-frame / finite-irreducible averaging *would* deliver. The averaging is a uniform
**weighting** over instruments — dropping the uniform weight breaks it (the runner
exhibits a non-uniform finite average that does **not** reach `I₃/3`, `‖·‖ = 0.188`), so
the **weight is load-bearing**, not the group alone.

## Why Record does not supply it (the relocation)

A twirl, a uniform finite-group average, or a multi-frame cycle is a weighting /
normalization over instruments. The Record axiom supplies no weighting, normalization, or
probability (`record_classical_semigroup_boundary` retained;
`record_markov_generator_embeddability_boundary` retained_no_go), and record formation is
not unconditionally forced (`record_formation_not_unconditionally_forced` retained_no_go).
So each frame is a named admission and the multi-frame average is a **named
multi-instrument admission** — not delivered by Record. Two guards fence the obvious
overclaims (D5):

- **Covariance ≠ contraction.** The identity channel is `SU(3)`-covariant yet depolarizes
  nothing; covariance alone does not single out `I₃/3` as an attractor.
- **No purity-conservation claim.** A generic single global unitary on `color ⊗ env`
  changes the reduced color purity (entanglement), so we do **not** claim coherent
  evolution preserves `P`; but a single unitary still does not single out `I₃/3` as an
  attractor (`‖ρ_color' − I₃/3‖ = 0.539` in the runner's deterministic instance).

**Relocation.** Block 04 reduced ADM-2 to "is `ρ_color = I₃/3`?" This note reduces *that*
to **"is the multi-frame (complementary-basis / finite-irreducible) averaging admitted?"**
— a sharper, named admission, parallel to block 02's instrument admissions. The new
model-independent **teeth** are the single-frame impossibility and the color-blind
inertness; the multi-frame constructions only **exhibit the admission space**.

## What this does NOT do (honest boundary)

- It does **not** derive that the framework adopts any multi-frame averaging protocol.
  Depolarization remains **conditional on a named multi-instrument admission**; the
  axioms (with the retained Record boundaries) do not supply the averaging weight.
- It does **not** deliver the gauge-link generator **R1**, does **not** discharge the
  static frame redundancy **ADM-1**, does **not** select the blocking isometry, and
  asserts **no** ST1/ST2 ordering.
- It is the **converse** direction to block 04's necessary condition, fenced as an
  admission exhibit — **not** a derivation of depolarization, and distinct from the
  refuted first-moment "annealed-twirl = i.i.d.-central CLT" sufficiency claim.
- The single-frame impossibility is stated for projective (rank-1 orthonormal-frame)
  record instruments and the color-blind scalar-projector instrument — the einselection
  instruments block 02 actually supplies. A generalized-measurement instrument outside
  that class is a separate (and itself admission-bearing) object.

## Trace

`trace_class: frontier_discovery / upstream_support`. It shapes R2/ADM-2 by relocating
its remaining open input (color depolarization) onto a named multi-frame averaging
admission, and supplies the exact single-frame impossibility that pins why Record alone
does not close it. It closes no lane and discharges no hat. Companion certificate:
`CLAIM_STATUS_CERTIFICATE_BLOCK05.md`.
