---
claim_id: microcausality_corner_class_factorization_discharge_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Finite-dimensional number-conserving fermionic second quantization and its logarithmic-generator identity, with composition only on the supplied free U=1 corner surface. Fixed-background factorization, gauge integration, locality envelopes, Lieb-Robinson bounds, and physical-time selection are not claimed."
upstream_dependencies:
  - corner_axis_free_transfer_extension_per_channel_trace_correspondence_and_mode_set_fork_bounded_note_2026-06-12
  - microcausality_gauged_kernel_weighted_activity_feed_bounded_theorem_note_2026-07-18
runner: scripts/microcausality_corner_class_factorization_discharge_2026_07_18.py
---

# Finite-Mode Second Quantization And The Free-Corner Log Bridge

**Date:** 2026-07-18

**Type:** bounded_theorem

**Audit-status authority:** independent audit lane only

**Primary runner:**
[`scripts/microcausality_corner_class_factorization_discharge_2026_07_18.py`](../scripts/microcausality_corner_class_factorization_discharge_2026_07_18.py)

**Runner cache:**
[`logs/runner-cache/microcausality_corner_class_factorization_discharge_2026_07_18.txt`](../logs/runner-cache/microcausality_corner_class_factorization_discharge_2026_07_18.txt)

## Scope

This note proves a finite-dimensional exterior-algebra identity. It then uses
that identity only on the free `U = 1` corner surface where the cited source
already supplies the operator equality `T_k^2 = Gamma(t_k)` channel by
channel. It does not infer a many-body transfer operator from a one-particle
kernel.

The distinction is load-bearing. The current source tree does not
supply `T_MB^2[U] = Gamma(t[U])` at a general fixed gauge background. The
conditional finite-matrix recurrence in
`RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md`
explicitly excludes a Fock-space second quantization, while
`CORNER_TRANSFER_EXTENDS_TO_FIXED_GAUGE_BACKGROUNDS_BOUNDED_NOTE_2026-06-12.md`
constructs classical fixed-background matrices and separately records a trace
identity. Neither statement is an operator identification. Fixed-background
factorization therefore remains open.

## Finite-mode theorem

Let `H` be a complex Hilbert space of finite dimension `n`, and let

`F(H) = direct_sum_(q=0)^n wedge^q H`

be its fermionic Fock space. For a linear map `A : H -> H`, define the
number-conserving second quantization

`Gamma(A) = direct_sum_(q=0)^n wedge^q A`.

For an operator `X` on `H`, let `dGamma(X)` denote the infinitesimal exterior
action: on `wedge^q H`, it is the sum of `X` acting in each occupied slot.
These definitions give the following exact finite-dimensional identities.

1. **Functoriality.** For arbitrary linear maps `A` and `B`,
   `Gamma(A) Gamma(B) = Gamma(AB)`. No commutativity hypothesis is needed for
   this algebraic identity.
2. **Canonical intertwiner.** With `a^dag(f)` denoting exterior multiplication
   by `f`,
   `Gamma(A) a^dag(f) = a^dag(Af) Gamma(A)`, and `Gamma(A)` fixes the vacuum.
   These relations determine `Gamma(A)` on decomposable occupation vectors.
3. **Positive logarithm.** If `t` is strictly positive, then
   `Gamma(t) = exp(dGamma(log t))` and
   `-log Gamma(t) = dGamma(-log t)`.
4. **Trace identity.** `Tr_F Gamma(A) = det_H(1 + A)`. In particular this
   holds for positive `t` without choosing an eigenbasis in the statement.
5. **Direct sums.** Under the canonical exterior-algebra identification,
   `Gamma(direct_sum_k A_k) = tensor_k Gamma(A_k)`.

For the positive-logarithm identity, diagonalize
`t = V diag(lambda_1,...,lambda_n) V^dag` with every `lambda_j > 0`.
On the occupation vector indexed by `S subset {1,...,n}`, `Gamma(t)` has
eigenvalue `product_(j in S) lambda_j`, while `dGamma(log t)` has eigenvalue
`sum_(j in S) log lambda_j`. Exponentiating or taking the principal logarithm
gives item 3. Summing the occupation eigenvalues gives

`Tr Gamma(t) = sum_S product_(j in S) lambda_j
             = product_j (1 + lambda_j)
             = det(1 + t)`.

Functoriality follows sector by sector from
`wedge^q A wedge^q B = wedge^q(AB)`. The intertwiner follows because applying
`Gamma(A)` after exterior multiplication maps
`f wedge v_1 wedge ...` to `Af wedge Av_1 wedge ...`.

Strict positivity is essential only for the bounded principal logarithm. A
singular `t` still has a well-defined exterior action and trace identity, but
`log t` and `log Gamma(t)` are not finite operators.

## Why trace data do not identify the functor

Trace, positivity, and multiplication alone do not select the canonical
creation operators. Let `W` be a fixed number-preserving unitary which acts
nontrivially inside a two-particle sector and define
`Gamma_tilde(A) = W Gamma(A) W^dag`. It preserves traces and functoriality and
maps positive `A` to positive operators, but it need not satisfy the canonical
creation intertwiner. For `t = diag(2,3,5)`, swapping the occupation states
with eigenvalues `6` and `10` changes the corresponding entries of
`-log Gamma_tilde(t)` relative to the standard `dGamma(-log t)`.

Thus the exterior action or, equivalently, the canonical creation
intertwiner is the pin. The trace/determinant correspondence by itself is not
a Gaussian-factorization theorem.

## Composition on the supplied free corner surface

The cited
[`CORNER_AXIS_FREE_TRANSFER_EXTENSION_PER_CHANNEL_TRACE_CORRESPONDENCE_AND_MODE_SET_FORK_BOUNDED_NOTE_2026-06-12.md`](CORNER_AXIS_FREE_TRANSFER_EXTENSION_PER_CHANNEL_TRACE_CORRESPONDENCE_AND_MODE_SET_FORK_BOUNDED_NOTE_2026-06-12.md)
supplies, on its free finite-mode `1+1d` surface and positive-mass domain,

`t_k = exp(-2 E_k)`,  `T_k^2 = Gamma(t_k)`

for each of the three decoupled generation channels. Applying the theorem
gives the exact dimensionless logarithmic generator

`-1/2 log T_k^2 = dGamma(E_k)`.

For the full free corner tensor product,

`T_corner^2 = tensor_k T_k^2
            = Gamma(direct_sum_k t_k)`,

and hence

`-1/2 log T_corner^2 = sum_k dGamma(E_k)`

under the canonical tensor-factor identification. This verifies the
Gaussian-factorization hypothesis named in
[`MICROCAUSALITY_GAUGED_KERNEL_WEIGHTED_ACTIVITY_FEED_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_GAUGED_KERNEL_WEIGHTED_ACTIVITY_FEED_BOUNDED_THEOREM_NOTE_2026-07-18.md)
only on that already-supplied free `U = 1` surface. The factorized form has no
additional scalar there because the cited source supplies the operator
equality itself. This does not determine any background-dependent scalar or
normalization beyond that free source surface.

This is an algebraic logarithmic-generator identification. It does not select
physical time or derive dynamics from the framework axioms.

## Open problems and non-claims

- **Fixed gauge backgrounds:** no current source identifies the classical
  fixed-background recurrence matrix with a Fock-space `Gamma(t[U])`.
- **Gauge integration:** no measure over backgrounds or interacting transfer
  is supplied.
- **Locality and Lieb-Robinson bounds:** this note proves no spatial kernel
  envelope and makes no open-chain or periodic-chain activity claim. A
  one-particle locality estimate cannot be fed into a many-body bound until the
  operator identification and boundary convention are both supplied.
- **Matrix fibers:** if a future one-dimensional open-chain bridge supplies a
  block-operator-norm envelope with fixed fiber dimension `n_f`, the coarse
  activity expression carries the factor `n_f`; scalar-fiber constants do not
  transfer to a non-Abelian block kernel.
- **Physical interpretation:** no species choice, occupancy choice, physical
  velocity, infinite-volume dynamics, or retained-grade status follows.

The primary runner is source-contained. It checks the exterior functor on
noncommuting matrices, the canonical creation intertwiner, positive logarithm
and trace identities, direct-sum channel factorization, the free-corner
composition, the singular-log boundary, and a conjugated-functor
counterexample. It reads no mutable Markdown and assigns no audit verdict.
