# Faithfulness via Matter-Operator Spin Content: spatial-rotation scalar excluded; matter attachment remains open

**Date:** 2026-06-01
**Claim type:** bounded_theorem
**Claim boundary:** bounded exclusion fragment. Once the operator-frame
spatial `Spin(3)` action is applied, a `K=0` completion is not a
Lorentz/rotation-algebra completion. This note does not identify that
operator-frame action with every matter excitation, derive the `(3,1)`
signature, close faithfulness, or set an audit verdict.
**Primary runner:**
`scripts/frontier_koide_faithfulness_rotation_scalar_excluded.py`
with cache
`logs/runner-cache/frontier_koide_faithfulness_rotation_scalar_excluded.txt`
(10/10 checks).

## Setting

The microcausality/reflection-positivity localization note
(`KOIDE_P1_COLLAPSES_FRAME_RESIDUALS_NOTE_2026-06-01`, companion candidate)
left the carrier frame with one residual — **faithfulness** (the boost-acting Weyl
rep over the trivial scalar `J=K=0` on the on-site ℂ²) — *admitted* by
microcausality. This note attacks it through the **spin content** instead, finds a
clean signature-free fragment, and corrects an over-optimistic hope (that
faithfulness would collapse to the `(3,1)` signature).

## The clean fragment (signature-free bounded algebra)

The inert **spatial-rotation** scalar (`J=0` on the on-site ℂ² algebra) is
**excluded**:

1. The internal-external SU(2) merger
   (`internal_external_su2_merger`, cited bounded authority, runner 273/273) gives the
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
admits the `J=0` scalar). This rotation-half exclusion is signature-free bounded
algebra from the cited operator-frame authorities plus the `so`-bracket fact.

## What this does NOT close (the honest residual)

The full faithfulness **value** (the Weyl boost `K=iσ/2` *on matter*) does **not**
reduce to the `(3,1)` signature alone. It stacks three residuals, dominated by an
**upstream matter-attachment pin** that is *independent* of the signature:

1. **Matter-attachment (dominant, upstream, signature-independent — disclaimed by
   the current retained surface).** The merger is an **operator-frame** identification
   ("the per-site Pauli su(2) and the Clifford Spin(3) generators are the same
   *operator* triple on ℂ²"; "not a Coleman–Mandula / Haag–Łopuszański–Sohnius
   claim"). Its load-bearing input `per_site_su2_spin_half` **explicitly
   "does not identify this action with the physical spin generator of every matter
   excitation."** So a matter excitation can carry the operator-frame data yet be
   assigned `J=0` at the *field* index — **the merger does not, by itself, exclude
   the inert *matter* scalar.** The unsupplied premise is "matter field index = the
   ℂ² spinor under spatial rotations."
2. **The `(3,1)` signature (unaudited).** It only labels the forced nonzero `K` a
   *boost* (anti-Hermitian) vs an `so(4)` 4th rotation; `cl3_to_cl31_spinor_extension`
   delegates `ε=−1` to `anomaly_forces_time` (unaudited).
3. **Carrier identification (retained-disconnected).** `cl3_to_cl31` puts the
   Cl(3,1) boost on `R⁴` (Majorana), **not** the per-site ℂ²; the first-order-`D`
   route to the on-site boost rides the unaudited
   `staggered_dirac_kawamoto_smit_forcing` and the conditional
   `lorentz_boost_free_staggered_fermion_2point` (Euclidean SO(4), taste-scalar).

So faithfulness is **sharpened, not collapsed**: the dominant open piece is the
**matter-attachment pin** (upstream of, and independent of, the signature) — *not*
the signature, as an earlier reading hoped.

## The corrected picture

- **Bounded, signature-free:** the *spatial-rotation* scalar is excluded
  (this note's fragment).
- **Still open:** the *matter*-rep attachment (`J=σ/2` on the matter field index),
  then the `(3,1)` signature flavor, then the on-site-ℂ²-Weyl-block carrier
  identification.

## Next path

Source two narrow rows to close the remaining stack: **(a)** a matter-attachment
row lifting `per_site`'s operator-frame su(2) to the matter rep (matter field index
= the ℂ² spinor under spatial rotations) — closing the gap `per_site` explicitly
disclaims; **(b)** a carrier row bridging the on-site ℂ² to the Cl(3,1) Weyl block
under emergent boosts (vs the `M₄(R)`/`R⁴` Majorana module). If both later pass
independent audit,
faithfulness collapses to just the `(3,1)` signature (the already-known `G3`).
Separately worth probing: whether the native first-order real anti-Hermitian `D`
plus emergent-Lorentz can supply the matter-attachment pin
*without* the unaudited Kawamoto–Smit reconstruction.

## Non-circularity

Never assumes the faithful rep or `Q=2/3`: the merger action, the `K=0` bracket
failure, the two Weyl completions, and the `so(4)` comparison are computed forward
(runner).

## Load-bearing authorities

[INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md](INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md),
[PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md](PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md),
[CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md](CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md),
[CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md),
and
[CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md).

Non-load-bearing residual context remains plain text:
`anomaly_forces_time`, `staggered_dirac_kawamoto_smit_forcing`, and
`lorentz_boost_free_staggered_fermion_2point`.
