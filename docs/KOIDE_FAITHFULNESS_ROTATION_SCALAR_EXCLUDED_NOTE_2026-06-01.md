---
claim_id: koide_faithfulness_rotation_scalar_excluded_note_2026-06-01
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Faithfulness via M spin content: the inert spatial-rotation scalar is excluded (signature-free); the residual is a matter-attachment pin, not the (3,1) signature

**Date:** 2026-06-01
**Claim type:** bounded exclusion fragment + honest residual demarcation. Adds no
axiom and no import. `Q=2/3` never enters.
**Status authority:** independent audit lane only.
**Primary runner:**
`scripts/frontier_koide_faithfulness_rotation_scalar_excluded.py`
with cache
`logs/runner-cache/frontier_koide_faithfulness_rotation_scalar_excluded.txt`
(10/10 checks).

## Setting

The P1 capstone (`KOIDE_P1_COLLAPSES_FRAME_RESIDUALS_NOTE_2026-06-01`, sibling PR)
left the carrier frame with one residual — **faithfulness** (the boost-acting Weyl
rep over the trivial scalar `J=K=0` on the on-site ℂ²) — *admitted* by
microcausality. This note attacks it through the **spin content** instead, finds a
clean signature-free fragment, and corrects an over-optimistic hope (that
faithfulness would collapse to the `(3,1)` signature).

## The clean fragment (signature-free, retained-clean)

The inert **spatial-rotation** scalar (`J=0` on the on-site ℂ² algebra) is
**excluded**:

1. The internal-external SU(2) merger
   (`internal_external_su2_merger`, retained_bounded, runner 273/273) gives the
   on-site ℂ² algebra the **spatial Spin(3) action**:
   `U(R)=exp(iθ·S)` conjugates `σ_i` as `R_ij σ_j` (verified, runner §A) — so
   `J_i = σ_i/2 ≠ 0` are the spatial-rotation generators (the "merger gives only an
   *internal* su(2)" hole is **refuted**).
2. With `J = σ/2 ≠ 0`, `K=0` **fails** the boost bracket `[K_i,K_j] = ±iε_ijk J_k`
   at every off-diagonal pair — in **both** `so(3,1)` and `so(4)` (runner §B). So
   `K=0` (the inert spatial-rotation scalar) is excluded by `J≠0` **alone**,
   *independent of the signature*.
3. The `so(3,1)` completions of `J=σ/2` are **exactly** the two faithful Weyl
   chiralities `K=±iσ/2` (the merger bivector `B_i`, faithful 6-real-dim image);
   `so(4)` gives `K=±σ/2` (Hermitian 4th rotation). **No `K=0` branch** (runner §C).
4. So the signature `ε=e_4²` selects only the **flavor** of the forced nonzero `K`
   (boost, anti-Hermitian, vs an `so(4)` 4th rotation, Hermitian) — **not**
   `K=0`-vs-`K≠0` (runner §D).

So: *once `J≠0`, no trivial-boost (`K=0`) completion exists* — the rotation-scalar
is killed by the spin content, exactly where microcausality was powerless (it
admits the `J=0` scalar). This rotation-half exclusion is **retained-clean and
signature-free** (`internal_external_su2_merger` retained_bounded +
`per_site_su2_spin_half` retained + `cl3_per_site_hilbert_dim_two` retained + the
`so`-bracket fact).

## What this does NOT close (the honest residual)

The full faithfulness **value** (the Weyl boost `K=iσ/2` *on matter*) does **not**
reduce to the `(3,1)` signature alone. It stacks three residuals, dominated by an
**upstream matter-attachment pin** that is *independent* of the signature:

1. **Matter-attachment (dominant, upstream, signature-independent — disclaimed by
   the retained surface).** The merger is an **operator-frame** identification
   ("the per-site Pauli su(2) and the Clifford Spin(3) generators are the same
   *operator* triple on ℂ²"; "not a Coleman–Mandula / Haag–Łopuszański–Sohnius
   claim"). Its load-bearing input `per_site_su2_spin_half` (retained) **explicitly
   "does not identify this action with the physical spin generator of every matter
   excitation."** So a matter excitation can carry the operator-frame data yet be
   assigned `J=0` at the *field* index — **the merger does not, by itself, exclude
   the inert *matter* scalar.** The unsupplied premise is "matter field index = the
   ℂ² spinor under spatial rotations."
2. **The `(3,1)` signature (unaudited).** It only labels the forced nonzero `K` a
   *boost* (anti-Hermitian) vs an `so(4)` 4th rotation; `cl3_to_cl31_spinor_extension`
   (retained) delegates `ε=−1` to `anomaly_forces_time` (unaudited).
3. **Carrier identification (retained-disconnected).** `cl3_to_cl31` puts the
   Cl(3,1) boost on `R⁴` (Majorana), **not** the per-site ℂ²; the first-order-`D`
   route to the on-site boost rides the unaudited
   `staggered_dirac_kawamoto_smit_forcing` and the `audited_conditional`
   `lorentz_boost_free_staggered_fermion_2point` (Euclidean SO(4), taste-scalar).

So faithfulness is **sharpened, not collapsed**: the dominant open piece is the
**matter-attachment pin** (upstream of, and independent of, the signature) — *not*
the signature, as an earlier reading hoped.

## The corrected picture

- **Retained-clean, signature-free:** the *spatial-rotation* scalar is excluded
  (this note's fragment).
- **Still open:** the *matter*-rep attachment (`J=σ/2` on the matter field index),
  then the `(3,1)` signature flavor, then the on-site-ℂ²-Weyl-block carrier
  identification.

## Next path

Source two narrow rows to close the remaining stack: **(a)** a matter-attachment
row lifting `per_site`'s operator-frame su(2) to the matter rep (matter field index
= the ℂ² spinor under spatial rotations) — closing the gap `per_site` explicitly
disclaims; **(b)** a carrier row bridging the on-site ℂ² to the Cl(3,1) Weyl block
under emergent boosts (vs the `M₄(R)`/`R⁴` Majorana module). If both land retained,
faithfulness collapses to just the `(3,1)` signature (the already-known `G3`).
Separately worth probing: whether the native first-order real anti-Hermitian `D`
(retained_bounded) + emergent-Lorentz can supply the matter-attachment pin
*without* the unaudited Kawamoto–Smit reconstruction.

## Non-circularity

Never assumes the faithful rep or `Q=2/3`: the merger action, the `K=0` bracket
failure, the two Weyl completions, and the `so(4)` comparison are computed forward
(runner).

## Anchors (live-ledger tiers, verified origin/main 2026-06-01)

retained / retained_bounded:
`internal_external_su2_merger` (retained_bounded, the spatial Spin(3) action),
`per_site_su2_spin_half` (retained, disclaims matter-attachment),
`cl3_per_site_hilbert_dim_two` (retained),
`cl3_to_cl31_spinor_extension` (retained, delegates the signature),
`cpt_exact_real_anti_hermitian_d` (retained_bounded). **Not cited as retained (the
faithfulness *value* rides these):** `anomaly_forces_time` (unaudited, the
signature), `staggered_dirac_kawamoto_smit_forcing` (unaudited),
`lorentz_boost_free_staggered_fermion_2point` (audited_conditional).
