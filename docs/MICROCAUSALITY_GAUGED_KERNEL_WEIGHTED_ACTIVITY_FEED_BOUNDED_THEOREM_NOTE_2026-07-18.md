---
claim_id: microcausality_gauged_kernel_weighted_activity_feed_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Unaudited bounded feed from a supplied background- and volume-uniform scalar one-particle exponential kernel estimate to the weighted finite-support Lieb-Robinson activity. The result covers the scalar-fiber fixed-background bilinear and, conditionally on a supplied positive number-conserving Gaussian factorization, the corresponding many-body log-transfer commutators. It does not cover SU(2) or other matrix fibers, gauge integration, interacting non-Gaussian transfer operators, a derived dynamics, a physical propagation speed, or a retained-grade result."
upstream_dependencies:
  - minimal_axioms
  - microcausality_weighted_quasilocal_class_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
  - microcausality_fermionic_even_car_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
  - gauged_log_transfer_quasilocality_combes_thomas_narrow_theorem_note_2026-06-13
  - free_bilinear_quasilocal_lr_bridge_theorem_note_2026-06-10
runner: scripts/microcausality_gauged_kernel_weighted_activity_feed_2026_07_18.py
---

# Microcausality: scalar gauged-kernel weighted-activity feed

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Audit authority:** the independent audit lane only; this note assigns no
audit verdict.
**Primitive status:** no primitive is approved, registered, or enlarged here.

Primary runner:
[`scripts/microcausality_gauged_kernel_weighted_activity_feed_2026_07_18.py`](../scripts/microcausality_gauged_kernel_weighted_activity_feed_2026_07_18.py).
Its cache is
[`logs/runner-cache/microcausality_gauged_kernel_weighted_activity_feed_2026_07_18.txt`](../logs/runner-cache/microcausality_gauged_kernel_weighted_activity_feed_2026_07_18.txt).

## Supplied scalar-fiber setting

The bounded
[`GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md`](GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md)
is used only as a supplier.  On its scalar one-component, fixed-background
slice, assume its kernel estimate in a finite open region `Λ ⊂ Z^3`, using
the ambient (non-periodic) `l_∞` and `l_1` metrics:

> `|k_U(x,y)| ≤ K exp(-η ||x-y||_∞)`,                              (1)

where supplied `K>0` and `η>0` are common to every background `U` and every
volume in the family.  This note neither re-proves that estimate nor promotes
the supplier's unaudited status.

The matrix `k_U` is Hermitian.  With one CAR mode per site, define the even
Hermitian terms

> `h_{xy}=k_U(x,y)c_x†c_y + conjugate(k_U(x,y))c_y†c_x`, `x<y`,
> `h_x=k_U(x,x)c_x†c_x`.                                          (2)

Their sum is the supplied scalar bilinear `H_U`.  Choose `μ` with

> `0 < μ < η/3`.                                                   (3)

The
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
memo does not select `U`, `k_U`, `H_U`, `K`, `η`, or `μ`.

## From the kernel envelope to weighted activity

The Jordan--Wigner representation gives
`||c_x†c_y||=||c_x†c_x||=1`.  Therefore

> `||h_{xy}|| ≤ 2K exp(-η||x-y||_∞)`, `||h_x||≤K`.                 (4)

This is a safe triangle-inequality envelope.  In the scalar representation
the exact off-diagonal pair norm is `|k_U(x,y)|`, so (4) deliberately carries
a factor-two slack.

On `Z^3`,

> `||z||_1 ≤ 3||z||_∞`,
> `#{z:||z||_∞=r}=(2r+1)^3-(2r-1)^3=24r^2+2`.                    (5)

Set `q=exp[-(η-3μ)]`, so (3) implies `0<q<1`.  The site-weighted
activity from the linked weighted-support theorem obeys

> `κ_U := sup_x Σ_{S∋x} ||h_S|| |S| exp(μ diam_1(S))`
> `≤ K + 4K Σ_{r≥1}(24r^2+2)q^r`
> `= K + 8K q(13+10q+q^2)/(1-q)^3 =: κ_bar`.                    (6)

The factor `4` in the pair sum is the product of the norm-envelope factor `2`
and the support size `|{x,y}|=2`.  The numerator follows from

> `24q(1+q)+2q(1-q)^2=2q(13+10q+q^2)`.                           (7)

At `q=1/2`, (6) gives `κ_bar/K=585`.  Replacing the triangle envelope
by the exact scalar pair norm gives the sharper scalar value `293`; these are
an envelope and a scalar sharpening, not two values for the same convention.
Both are runner-checked.

Because `K` and `η` are supplied uniformly, `κ_bar` is common to every
background and volume.  The signs or phases of the scalar kernel do not enter
this conclusion.  A three-site `Z_2` sign family in the runner checks that all
eight sign backgrounds have the same exact and envelope activities.

## Bounded consequence

The bounded
[`MICROCAUSALITY_WEIGHTED_QUASILOCAL_CLASS_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_WEIGHTED_QUASILOCAL_CLASS_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md)
supplies the finite-volume weighted-support estimate, and the bounded
[`MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md)
supplies the ordinary/graded CAR convention.  Both dependencies remain
unaudited bounded inputs.

If `κ_U>0`, the first theorem gives, for disjoint finite supports `X,Y`,
`d=d_1(X,Y)≥1`, and all real `t`,

> `||[τ_t^U(A),B]|| ≤ ||[A,B]||`
> ` + 2||A||||B||(n_X^w(U)/κ_U) exp(-μd)(exp(2κ_U|t|)-1)`.        (8)

Using `n_X^w(U)/κ_U≤|X|` and `κ_U≤κ_bar` gives the single uniform
corollary

> `||[τ_t^U(A),B]|| ≤ ||[A,B]||`
> ` + 2||A||||B|| |X| exp(-μd)(exp(2κ_bar|t|)-1)`.                (9)

If `κ_U=0`, every interaction term vanishes, `τ_t^U` is the identity, and
(9) is immediate; the quotient in (8) is not used.  The zeroth term vanishes
for disjoint tensor-local observables and whenever at least one CAR observable
is even.  For an odd--odd ordinary commutator it is retained.

The slope obtained from the exponential in (9) is only a mathematical
Lieb--Robinson majorant for supplied inputs.  It is not a selected or measured
physical speed.

## Conditional transfer interpretation

Equation (9) is unconditional only for the scalar bilinear after (1)--(3) are
supplied.  It applies to a many-body transfer operator only under the additional
supplied positive number-conserving Gaussian factorization

> `T_MB[U]=C(U) Γ(T_1[U])`, `C(U)>0`.                              (10)

Then
`-log T_MB=-log C(U)·1+dΓ[-log T_1]`; the scalar identity shift drops from
commutators.  A one-particle restriction does not imply (10): the positive
operator `exp[-dΓ(h)-g n_1n_2]` has one-particle restriction `exp(-h)` but an
interacting many-body logarithm.

Accordingly, this note supplies only the scalar one-mode/U(1) slice of the
fixed-background composition requested by the Combes--Thomas note.  Its
SU(2) and other matrix-fiber kernels, non-Gaussian transfer operators, and the
`U`-integrated gauge-measure problem remain open here.

The bounded
[`FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md`](FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md)
is only a scalar pair-interaction comparator.  Its dimensional threshold
pattern is consistent with (3); it is not used as an execution-time oracle.

## Boundaries

- No matrix-fiber, SU(2), or nonabelian activity estimate is proved here.
- No gauge integration or gauge-measure uniformity is proved.
- No periodic-graph extension or infinite-volume dynamics is established.
- No Gaussian factorization is inferred from a one-particle kernel.
- No kernel estimate, dynamics, physical speed, or sharp constant is derived.
- No audit result or retained-grade status is assigned.

## Verification

The runner is source-contained and reads no Markdown or other mutable science
input.  Its descriptive gates independently check the CAR pair norm, shell
count, metric conversion, activity factors, closed form, threshold, zero-
activity case, uniform corollary, sign-background exhibit, and Gaussian
identity shift.  It prints one `PASS` or `FAIL` line per gate and a final total;
the committed cache is generated from that runner alone.
