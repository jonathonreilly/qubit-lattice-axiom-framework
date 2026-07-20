---
claim_id: microcausality_matrix_fiber_trace_norm_lemma_and_feed_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Unaudited bounded matrix-fiber extension of the supplied fixed-background kernel-to-activity feed. For a supplied fixed finite fiber dimension n_f and a background- and volume-uniform block-operator-norm kernel envelope on finite open regions, an exact CAR pair-term trace-norm identity gives a direct weighted-activity envelope and a finite-volume Lieb-Robinson corollary. The result includes the SU(2) fundamental block only when its supplied representation dimension and kernel bound meet these hypotheses. It does not derive a kernel, representation bound, Gaussian factorization, gauge integration, infinite-volume dynamics, physical propagation speed, or retained-grade result."
upstream_dependencies:
  - minimal_axioms
  - gauged_log_transfer_quasilocality_combes_thomas_narrow_theorem_note_2026-06-13
  - microcausality_gauged_kernel_weighted_activity_feed_bounded_theorem_note_2026-07-18
  - microcausality_weighted_quasilocal_class_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
  - microcausality_fermionic_even_car_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
runner: scripts/microcausality_matrix_fiber_trace_norm_lemma_and_feed_2026_07_18.py
---

# Microcausality: matrix-fiber trace-norm lemma and activity feed

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Audit authority:** the independent audit lane only; this note assigns no
audit verdict.
**Primitive status:** no primitive is approved, registered, or enlarged here.

Primary runner:
[`scripts/microcausality_matrix_fiber_trace_norm_lemma_and_feed_2026_07_18.py`](../scripts/microcausality_matrix_fiber_trace_norm_lemma_and_feed_2026_07_18.py).
Its cache is
[`logs/runner-cache/microcausality_matrix_fiber_trace_norm_lemma_and_feed_2026_07_18.txt`](../logs/runner-cache/microcausality_matrix_fiber_trace_norm_lemma_and_feed_2026_07_18.txt).

## Supplied setting

Fix a finite open region `Λ⊂Z^3`, with the ambient non-periodic `l_∞` and
`l_1` metrics, and a fixed finite fiber dimension `n_f≥1`.  At each site use
CAR modes `c_{x,a}`, `a=1,...,n_f`.  Supply a Hermitian block kernel with

> `||k_U(x,y)||op ≤ K exp(-η||x-y||∞)`,                           (1)

where `K>0` and `η>0` are common across the stated family of backgrounds and
volumes.  Choose `0<μ<η/3`.  Define, for `x≠y`,

> `h_{xy}=Σ_ab k_U(x,y)_{ab} c†_{x,a}c_{y,b} + h.c.`,
> `h_x=Σ_ab k_U(x,x)_{ab} c†_{x,a}c_{x,b}`.                       (2)

The bounded
[`GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md`](GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md)
is a direct supplier of a fixed-background block-kernel envelope; it is not
re-proved or promoted here.  A mixed representation family is covered only if
a common finite `n_f^max` is supplied and substituted for `n_f`.  The
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
memo does not select any of these inputs.

## Exact pair trace-norm lemma

For any complex `n_f×n_f` matrix `k`, put
`T=Σ_ab k_ab c†_{x,a}c_{y,b}`.  Then

> `||T+T†|| = ||k||S1`,                                          (3)

where `||k||S1` is the sum of the singular values.

Indeed, take `k=UΣV†`.  The particle-conserving mode rotations induced by
`U` and `V` preserve the CAR and turn `T+T†` into

> `Σ_i σ_i(C†_{x,i}C_{y,i}+C†_{y,i}C_{x,i})`.                    (4)

The summands are even operators on disjoint mode pairs and commute.  Each has
spectrum `{−σ_i,0,σ_i}`; their joint spectrum consists of the sums of these
values, so the maximum absolute value is `Σ_iσ_i`.  Equivalently, the
one-particle block matrix `[[0,k],[k†,0]]` has eigenvalues `±σ_i`, and its
full-Fock second quantization has the corresponding subset-sum spectrum.

The runner checks eight two-fiber matrices, including complex and non-normal
examples, and a three-fiber example with degenerate singular values.

## On-site and fiber-dimension bounds

For Hermitian `k` with eigenvalues `λ_i`, the on-site second quantization has
the subset-sum spectrum and therefore

> `||Σ_ab k_ab c†_a c_b||`
> `=max(Σ_{λ_i>0}λ_i, -Σ_{λ_i<0}λ_i) ≤ ||k||S1`.                  (5)

The inequality is strict for `diag(1,-1)` and saturated by `diag(1,2)`.
For every fiber matrix,

> `||k||S1 ≤ n_f ||k||op`,                                       (6)

with equality at the identity.  Thus the `n_f` factor cannot be removed when
only operator-norm data are supplied.  A direct trace-norm kernel envelope
would avoid that conversion.

## Matrix-fiber activity feed

Let

> `r=exp[-(η-3μ)]`,
> `F(r)=Σ_{m≥1}(24m^2+2)r^m`
> `    =2r(13+10r+r^2)/(1-r)^3`.                                 (7)

Equations (1), (3), and (6) give the direct activity envelope

> `κ_U ≤ κ_direct := n_f K[1+2F(r)]`
> `=n_f[K+4K r(13+10r+r^2)/(1-r)^3]`.                            (8)

The factor `2` multiplying `F` is the pair support size.  If one deliberately
reuses the scalar parent's triangle-inequality pair envelope, the coarser but
also valid bound is

> `κ_coarse := n_f K[1+4F(r)]`
> `=n_f[K+8K r(13+10r+r^2)/(1-r)^3]`.                            (9)

At `r=1/2`, these are respectively `293 n_f K` and `585 n_f K`.  For a
supplied SU(2) fundamental block with `n_f=2`, they are `586K` and `1170K`.
The direct bound (8) is the sharpened theorem input; (9) is retained only as a
consistency comparison with the bounded scalar feed
[`MICROCAUSALITY_GAUGED_KERNEL_WEIGHTED_ACTIVITY_FEED_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_GAUGED_KERNEL_WEIGHTED_ACTIVITY_FEED_BOUNDED_THEOREM_NOTE_2026-07-18.md).

Every term in (2) is even.  The bounded
[`MICROCAUSALITY_WEIGHTED_QUASILOCAL_CLASS_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_WEIGHTED_QUASILOCAL_CLASS_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md)
and its bounded
[`MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md)
companion then give, when `κ_U>0`, the per-background estimate with
`n_X^w(U)/κ_U` and the uniform coarse-support corollary

> `||[τ_t^U(A),B]|| ≤ ||[A,B]||`
> ` +2||A||||B|| |X| exp(-μd)(exp(2κ_direct|t|)-1)`.              (10)

If `κ_U=0`, all interaction terms vanish, the evolution is the identity, and
(10) is immediate without forming a quotient.  The finite-volume, ordinary
versus graded commutator, and zeroth-term conventions are exactly those of the
linked bounded parents.  This note establishes no periodic-graph extension or
infinite-volume dynamics.

## Boundaries

- The SU(2) specialization requires the supplied fixed fundamental block and
  a kernel envelope satisfying (1); no gauge representation is derived.
- Gauge integration and gauge-measure uniformity remain open.
- A many-body transfer interpretation still requires a supplied positive
  number-conserving Gaussian factorization; it is not inferred here.
- Non-Gaussian interactions, unbounded/mixed fibers without `n_f^max`, and
  physical propagation-speed claims are outside scope.
- No audit result or retained-grade status is assigned.

## Verification

The runner is source-contained and reads no mutable Markdown.  Descriptive
gates independently check pair norms, mode rotations, joint spectra, on-site
strictness and saturation, the trace/operator-norm conversion, evenness,
direct and coarse envelopes, the SU(2) specialization, ambient metric scope,
zero activity, and uniform monotonicity.  The committed cache fingerprints
that runner alone.
