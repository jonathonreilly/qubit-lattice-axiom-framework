---
claim_id: microcausality_matrix_fiber_trace_norm_lemma_and_feed_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Bridge-conditional matrix-fiber extension of the sibling kernel feed (axioms supply no dynamics; the fiber dimension n_f, the matrix-valued kernel bound, and the CAR/second-quantization conventions are supplied objects): (M1) the PAIR TRACE-NORM LEMMA, new and EXACT — for x ≠ y and any n_f × n_f fiber matrix k, ||Σ_ab k_ab c_{xa}^† c_{yb} + h.c.|| = ||k||_{S1} (trace norm), proved by singular-value decomposition plus particle-conserving mode rotations (CAR-preserving, gated) reducing to commuting Hermitian hops on disjoint mode pairs whose joint spectrum is the sums of {−σ_i, 0, σ_i} — gated on eight exact 2x2 instances (incl. complex and non-normal) plus an n_f = 3 degenerate-singular-value instance via an explicit eigenvector; (M2) the ON-SITE BOUND — for Hermitian fiber k, ||Σ_ab k_ab c_{xa}^† c_{xb}|| = max(Σλ^+, Σλ^−) ≤ ||k||_{S1}, with the strictness exhibit diag(1,−1) (norm 1 < S1 = 2) and the saturation exhibit diag(1,2) (3 = 3) gated; (M3) the fiber-dimension envelope ||k||_{S1} ≤ n_f ||k||_op (n_f singular values each below the largest; equality at the identity fiber, gated); (M4) the FEED: any supplied matrix-kernel bound ||k_xy||_op ≤ K e^{−η||x−y||_∞} yields ||h_xy|| = ||k_xy||_{S1} ≤ n_f K e^{−η r}, so every step of the sibling scalar feed multiplies by n_f — kappa_bar_fiber = n_f · kappa_bar_scalar (both the direct exact-pair 293·n_f·K and the sibling-compatible 585·n_f·K gated at x = 1/2) — and the block07 display applies with the uniform corollary intact (n_f is geometry, fixed across backgrounds); n_f = 1 recovers the sibling exactly (consistency gate); (M5) the sharper-data remark: kernels supplied directly with S1-type decay skip the n_f factor (stated, not developed). The evenness of fiber bilinears is gated; SOURCE-SCOPE CORRECTION (review-found): the CT note's kernel is block-valued — it declares U(1) AND SU(2) backgrounds with a per-site block-kernel convention (quoted and needled) — so the sibling's scalar feed covers its abelian case and THIS note's fiber feed is what the SU(2) block case needs at fixed representation dimension (n_f^max for mixed families); the sibling's scalar-fiber declaration is corrected accordingly, recorded in the review history and on the sibling's PR; both the direct exact-pair envelope 293 n_f K and the sibling-compatible 585 n_f K are gated; the U-integrated measure side, sharp constants, and the Gaussian-factorization/spectral surface remain open as the siblings state; nothing physical is selected."
upstream_dependencies:
  - minimal_axioms
  - microcausality_gauged_kernel_weighted_activity_feed_bounded_theorem_note_2026-07-18
  - microcausality_weighted_quasilocal_class_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
  - microcausality_fermionic_even_car_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
runner: scripts/microcausality_matrix_fiber_trace_norm_lemma_and_feed_2026_07_18.py
---

# Microcausality: Matrix-Fiber Trace-Norm Lemma And Feed

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; supplied fiber dimension and
matrix-valued kernel bound; the axioms supply no dynamics; same CAR
and second-quantization conventions as the siblings.
**Audit-status authority:** independent audit lane only. This note sets
no audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here.
**Primary runner:**
[`scripts/microcausality_matrix_fiber_trace_norm_lemma_and_feed_2026_07_18.py`](../scripts/microcausality_matrix_fiber_trace_norm_lemma_and_feed_2026_07_18.py)
**Runner cache:**
[`logs/runner-cache/microcausality_matrix_fiber_trace_norm_lemma_and_feed_2026_07_18.txt`](../logs/runner-cache/microcausality_matrix_fiber_trace_norm_lemma_and_feed_2026_07_18.txt)

## Purpose

The sibling feed
[`MICROCAUSALITY_GAUGED_KERNEL_WEIGHTED_ACTIVITY_FEED_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_GAUGED_KERNEL_WEIGHTED_ACTIVITY_FEED_BOUNDED_THEOREM_NOTE_2026-07-18.md)
declared a scalar fiber and named matrix-valued (internal-component)
kernels open, needing "a fiber-dimension envelope". This note supplies
that item — and something sharper than an envelope at its core: an
**exact identity** for the norm of a fiber pair term. For any
`n_f × n_f` matrix `k`,

> `|| Σ_ab k_ab c_{xa}^† c_{yb} + h.c. || = ||k||_{S1}`  (`x ≠ y`),

the trace norm — not the operator norm, and not `n_f` times anything:
the exact value. The proof is elementary and rebuilt below (SVD plus
CAR-preserving mode rotations — gated at real-orthogonal AND
complex-unitary instances; commuting disjoint-mode hops add their
norms). The fiber-dimension envelope then follows as
`||k||_{S1} ≤ n_f ||k||_op`, and the entire sibling feed multiplies by
`n_f`, with `n_f = 1` recovering the sibling exactly. **Source-scope correction (review-found, important):** the CT note's
kernel is NOT scalar — it declares backgrounds in "any compact gauge
group `G` (here `U(1)` and `SU(2)`)" with a per-site
**block-kernel** convention, so the `SU(2)` fundamental case is a
block kernel with `n_f = 2`. An earlier draft of this note (and the
sibling's scalar-fiber declaration) mis-scoped that source; corrected
here: the sibling's scalar feed covers the CT note's abelian/scalar
case, and THIS note's fiber feed is what the `SU(2)`/block case
needs, at fixed finite representation dimension (`n_f^{max}` if a
background family mixes representation dimensions).

## Hypotheses (all supplied, none derived)

A supplied fiber dimension `n_f ≥ 1`; modes `(x, a)` for sites
`x ∈ Λ ⊂ Z^3` and fiber indices `a ∈ {1..n_f}`, with the CAR algebra
and JW computational realization of the fermionic siblings; a supplied
matrix-valued one-particle kernel with the fiber **operator-norm**
bound `||k_xy||_op ≤ K e^{−η||x−y||_∞}` (`K`, `η` background- and
volume-independent where the sibling's source supplies that);
`0 < mu < η/3` as in the sibling. The second-quantized family: pair
terms `h_{xy} = Σ_ab (k_xy)_{ab} c_{xa}^† c_{yb} + h.c.` (`x ≠ y`) and
on-site terms `h_x = Σ_ab (k_xx)_{ab} c_{xa}^† c_{xb}` (`k_xx`
Hermitian). Every term is even (two generators; gated). The axioms
supply no dynamics (needled). No worker was used for this block: the
supervisor's ground-truth session (recorded in the loop pack) covers
the lemma instances, and the runner gates everything natively.

## Results

**Pair trace-norm lemma (exact identity, rebuilt).** Let `x ≠ y` and
`k` any `n_f × n_f` complex matrix, `T = Σ_ab k_ab c_{xa}^† c_{yb}`.
Write the singular value decomposition `k = U Σ V^†` with singular
values `σ_1, …, σ_{n_f}`. Define rotated modes `C_{x,i}^† =
Σ_a U_{ai} c_{xa}^†` and `C_{y,i} = Σ_b (V^†)_{ib} c_{yb}` — both are
particle-conserving unitary mode rotations, which preserve the CAR
(gated at an instance). Then

> `T = Σ_i σ_i C_{x,i}^† C_{y,i}`,  so
> `T + T^† = Σ_i σ_i (C_{x,i}^† C_{y,i} + h.c.)`,

a sum of Hermitian hop terms on **disjoint** mode pairs: they commute
(the graded lemma of the fermionic sibling — even, disjoint), each has
spectrum `{−σ_i, 0, +σ_i}` (gated), and commuting Hermitian operators
with disjoint mode supports have joint spectrum equal to sums, so

> `||T + T^†|| = Σ_i σ_i = ||k||_{S1}`.

Gated on eight exact instances spanning rank-one, diagonal, unitary,
**complex**, and **non-normal** fiber matrices (e.g. `k = [[2,1],[0,1]]`: both
sides `√10`; `k = I_2`: both sides `2` — which already shows the
operator norm alone, `1`, is NOT the answer).

**On-site bound (with strictness and saturation exhibits).** For
Hermitian `k` with eigenvalues `λ_i`, the on-site term
`h_x = Σ k_ab c_{xa}^† c_{xb}` diagonalizes to `Σ λ_i n_i`; its
spectrum is the subset sums of `{λ_i}`, so

> `||h_x|| = max(Σ_{λ_i>0} λ_i, −Σ_{λ_i<0} λ_i) ≤ ||k||_{S1}`,

with strict inequality at `k = diag(1, −1)` (norm `1 < 2`) and
equality at `k = diag(1, 2)` (norm `3`) — both gated.

**Fiber-dimension envelope.** `||k||_{S1} = Σσ_i ≤ n_f · σ_max =
n_f ||k||_op` (gated, with equality at the identity fiber — the
exhibit that the envelope is attained and cannot be improved without
more kernel data).

**Theorem (the fiber feed).** With the supplied operator-norm kernel
bound, the lemma and envelope give `||h_{xy}|| = ||k_xy||_{S1} ≤
n_f K e^{−η r}` and `||h_x|| ≤ n_f K`; every step of the sibling
scalar feed then multiplies by `n_f`:

> `κ_U ≤ κ̄_fiber = n_f · [K + 8K·x(13+10x+x²)/(1−x)³]`,
> `x = e^{−(η−3mu)}`,

for every `mu < η/3`. Two envelope values are gated at `x = 1/2`:
the **direct exact-pair feed** — using the lemma's exact
`||h_xy|| = ||k_xy||_{S1} ≤ n_f K e^{−ηr}` — gives `293·n_f·K`, and
the **sibling-compatible inherited envelope** — deliberately
weakening to the sibling's `2·` pair convention — gives `585·n_f·K`
(the sharper direct value is the one the lemma buys; both displayed).
The block07 display applies verbatim, with
the uniform corollary intact: `n_f` is part of the supplied geometry,
identical across backgrounds, so background-uniformity carries
unchanged. Setting `n_f = 1` recovers the sibling's scalar feed
exactly (consistency gate). **Sharper-data remark:** a kernel supplied
directly with trace-norm decay (`||k_xy||_{S1} ≤ K' e^{−ηr}`) feeds
with `K'` and no `n_f` factor — the factor is the price of op-norm
data only (stated, not developed).

## No-Go Discipline Gate

- **N1 route inventory — ATTEMPTED.** Attacks executed: (1) "the pair
  norm might scale with `n_f`" — REFUTED exactly: the lemma gives the
  trace norm, and the identity-fiber instance shows both that the
  answer exceeds the operator norm and that the `S1 ≤ n_f·op`
  envelope is attained; (2) "mode rotations might not preserve CAR" —
  gated at an instance (rotated anticommutators recomputed); (3)
  "commuting-hops addition might fail" — the disjoint-mode graded
  argument is the fermionic sibling's lemma, re-gated on the rotated
  pair; (4) "on-site terms might also be S1-exact" — REFUTED by the
  `diag(1, −1)` strictness exhibit; the bound direction is what the
  feed needs; (5) "the CT source is scalar, so this block is
  unnecessary" — ATTEMPTED and REFUTED BY THE REVIEW ROUND: the CT
  note declares U(1) AND SU(2) block kernels (quoted, needled); the
  SU(2) case NEEDS this note; the earlier draft's contrary claim is
  corrected. Not attempted, not smuggled: the `U`-integrated measure
  side, sharp constants, the factorization/spectral surface.
- **N2 hypothesis independence (pairwise) — ATTEMPTED.** `n_f`
  (envelope only), the op-norm kernel bound (feed only), Hermiticity
  of `k_xx` (on-site diagonalization only), and `mu < η/3`
  (convergence only, inherited) enter at disjoint steps; the
  loop-pack battery flips each runner gate separately.
- **N3 hidden-wall scan — ATTEMPTED.** The lemma's proof uses the SVD
  (declared linear algebra, gated through its instances), mode
  rotations (CAR-preservation gated), and the disjoint-mode graded
  argument (sibling authority, re-gated). The joint-spectrum-sums
  step for commuting terms on disjoint modes is gated at the
  two-sigma instance. The `S1`-vs-op distinction is the note's own
  content and is exhibited, not assumed.
- **N4 dependency roles, per citation — ATTEMPTED.**
  - [`MICROCAUSALITY_GAUGED_KERNEL_WEIGHTED_ACTIVITY_FEED_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_GAUGED_KERNEL_WEIGHTED_ACTIVITY_FEED_BOUNDED_THEOREM_NOTE_2026-07-18.md):
    the scalar feed being multiplied (its envelope arithmetic cited,
    not re-derived; the `585` re-enters only as `585·n_f`); residual:
    its matrix-fiber open item — taken here.
  - [`MICROCAUSALITY_WEIGHTED_QUASILOCAL_CLASS_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_WEIGHTED_QUASILOCAL_CLASS_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md):
    the class and display the feed lands in (unchanged).
  - [`MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md):
    the graded disjoint-commutation lemma used for the rotated hops
    (re-gated).
  - [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):
    no-dynamics boundary needle only.
- **N5 rhetoric audit — ATTEMPTED.** "Exact identity" is claimed only
  for the pair lemma (gated both directions through instances
  including non-normal `k`); the on-site statement is a bound with
  its strictness exhibited; the `n_f` factor is called an envelope
  with its attainment exhibited; no gauge content is claimed from the
  CT note.
- **N6 partial-closure scan — ATTEMPTED.** Closed here: the sibling's
  matrix-fiber item, via the exact lemma plus the `n_f` envelope.
  Still open, named: the `U`-integrated measure side, sharp constants
  (including whether S1-decay data can replace the `n_f` factor in
  concrete kernels — the sharper-data remark), and the
  factorization/spectral surface.
- **N7 steelman (strongest counterarguments, answered) — ATTEMPTED.**
  (a) "The trace norm grows with `n_f`, so the LR constant degrades
  with fiber dimension — is that real or an artifact?" Real for
  op-norm-supplied kernels (the identity-fiber instance attains it:
  `n_f` independent hop channels genuinely add), and avoidable
  exactly when sharper S1 data is supplied — both faces stated. (b)
  "The lemma might fail for non-normal `k` where singular values and
  eigenvalues diverge." Gated precisely there: the `[[2,1],[0,1]]`
  instance has eigenvalues `2, 1` but singular values `√(3±√5)` —
  genuinely non-normal — and both sides equal `√10`; a complex-kernel
  instance is gated alongside. (c) "Mode rotations mixing fibers might break the JW
  strings." Rotations act within a site's fiber block (particle-
  conserving, same site set); the CAR-preservation gate verifies the
  rotated anticommutators exactly.
- **N8 prior-wall echo — ATTEMPTED.** The sibling's scalar-fiber
  declaration is extended, not contradicted (its `n_f = 1` case is
  the consistency gate); block07's class is consumed unchanged; no
  landed no-go concerns fiber norms. The family's exhibit-pair
  discipline is repeated (exact identity gated at reaching instances;
  strictness and saturation exhibits for every bound).

**Status: PASS** (all eight items answered; the block's one new claim
— the exact pair lemma — is gated through seven instances spanning
the matrix classes where it could fail).

## Non-Claims

- Does **not** claim the on-site norm equals the trace norm (bound
  only; strictness exhibited).
- Does **not** claim the `n_f` envelope is necessary for kernels
  supplied with S1-decay data (the sharper-data remark).
- Does **not** re-prove any CT-note content; the CT block-kernel
  quotes are needled as the source-scope correction (the sibling's
  scalar feed = the abelian case; this note's fiber feed = the
  `SU(2)`/block case at fixed representation dimension).
- Does **not** touch the `U`-integrated measure side, sharp
  constants, or the factorization/spectral surface.
- Does **not** select dynamics; the axioms supply none (needled).
- Does **not** set an audit verdict; independent audit remains
  required.

## Verification

Primary runner:
[`scripts/microcausality_matrix_fiber_trace_norm_lemma_and_feed_2026_07_18.py`](../scripts/microcausality_matrix_fiber_trace_norm_lemma_and_feed_2026_07_18.py)
— exact throughout. Gate kinds, honestly distinguished: **exact
representation gates** (the seven pair-lemma instances with both
sides computed independently — operator norms via eigenvalues of
`T^†T`, trace norms via singular values; the CAR-preservation of the
mode rotation; the rotated-hop commutation and spectrum; the on-site
strictness/saturation pair; evenness), **symbolic identity gates**
(the `S1 ≤ n_f·op` chain with its identity-fiber attainment; the
`n_f`-scaled envelope arithmetic `585·n_f`), and **presence needles**
(the sibling's matrix-fiber open sentence; the block07 display; the
axiom memo — presence checks, not correctness oracles). The gate
sequence is enforced against an ordered label manifest. The runner
prints one `PASS`/`FAIL` line per gate and a final total; the cached
transcript is committed at the path in the header at landing time.
