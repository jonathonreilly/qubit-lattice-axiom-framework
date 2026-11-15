# Expanded target: existence and a physical mass gap

The owner explicitly expanded the full-proof goal on 29 October 2026:
“Include existence and the mass gap.” The earlier T_OS existence target
remains a necessary milestone. This file records the added target and a
spectral reduction to a precise missing estimate. It is author support
pending independent review, not a mass-gap proof.

## 1. The target and the comparison

For the present SU(N), N≥2, construction, obtain a non-trivial local
Yang–Mills theory on R^4, its correctly normalized gauge-invariant local
observable hierarchy, and a physical Hilbert-space reconstruction with
nonnegative time-translation generator H and vacuum Ω. Prove a number
m_*>0, in fixed physical units, such that

    ker H = span{Ω},
    spec(H) ⊂ {0} ∪ [m_*,∞),

with a nonzero excited sector and finite infimum of its energy spectrum.
The same theory must satisfy the required locality, covariance, regularity
and Yang–Mills short-distance identification. The existing qualified
scalar/partial-test-algebra construction is not silently enlarged to the
full gauge-invariant local field family.

The [official Jaffe–Witten statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf),
§§3–4, requires a non-trivial quantum field theory on R^4, positive energy,
a unique vacuum, local gauge-invariant fields and a finite positive mass
threshold. Its group quantifier is every compact simple gauge group.
The current SU(N) construction therefore must not be advertised as proving
that entire group range without a further extension. The primary text's
§§3–4 were read for this target; it supplies no missing estimate here.

The [OpenAI announcement of 26 October 2026](https://openai.com/index/building-scientific-understanding-with-academic-communities/)
reports Yang–Mills existence and a Lean formalization, with the physics
artifacts awaiting release by its external collaboration. It announces
no physical mass-gap theorem. A verified gap would extend that announced
Yang–Mills result. We have not inspected its unreleased proof, and the
announcement is not an analytic input to this construction. This is a
comparison of stated scope, not a claim that the current PR exceeds it.

## 2. A sufficient reflected-correlation criterion

This elementary reduction assumes a valid reconstruction; it does not
construct one. Let H≥0 be self-adjoint on a Hilbert space, HΩ=0 and
||Ω||=1. Suppose the centered vectors v_F supplied by a positive-time
observable algebra have dense linear span in Ω-perp. Let

    C_F(t) = <v_F, exp(-tH) v_F>,   t≥0.

In a matching OS reconstruction this is the centered reflected Euclidean
correlation of F with its time translate. The matching of that expression,
its domains, products and renormalizations must be proved for the actual
observable hierarchy. Assume a common m_*>0 and, for every such F, finite
A_F and t_F with

    0 ≤ C_F(t) ≤ A_F exp(-m_* t),   t≥t_F.              (MG1)

Then H has no spectrum in [0,m_*) on Ω-perp and its kernel is exactly
span{Ω}.

Proof. Let E_H be the spectral measure of H. For 0≤b<m_*, positivity gives

    C_F(t) ≥ exp(-b t) ||E_H([0,b]) v_F||^2.

Together with MG1 this forces E_H([0,b])v_F=0 by sending t to infinity.
The spectral projection is bounded, so the same holds on the dense linear
span and then on Ω-perp. A countable increasing sequence b→m_* gives the
assertion. Since Ω is a zero eigenvector, the claimed kernel follows.
If Ω-perp is nonzero, some vector has nonzero spectral measure in a finite
interval [0,R], because E_H([0,R]) tends strongly to the identity as R→∞.
Thus the excited spectral infimum is finite as well as positive. ∎

Only diagonal reflected correlations are needed for this spectral step;
they must cover a dense family of centered states. Bounds for one selected
scalar two-point function do not supply that density. A_F and t_F may
depend on F; m_* must not.

## 3. The actual estimate still to construct

A usable sufficient lattice statement is MG1 for the appropriately
renormalized reflected observables. For each physical F, choose finite
A_F and t_F independent of ultraviolet cutoff and volume, and a common
physical m_*>0. Require the estimate for t_F<=t<=T_safe(volume), with
T_safe tending to infinity along the same hierarchy, so every fixed
t>=t_F eventually lies below the finite-volume wrap-around bound.
For each such fixed physical t, first
pass to the same continuum/infinite-volume hierarchy used by the existence
proof. The uniform estimate then survives. Only after this passage is
t sent to infinity in the spectral argument. No interchange of an
uncontrolled t→∞ limit with cutoff removal is allowed.

The actual unresolved construction has the following interfaces:

| Obligation | Required output | Current state |
|---|---|---|
| MG0: existence and reconstruction | Actual common hierarchy, physical normalization, complete field-domain and OS/reconstruction hypotheses | Open; the existing T_OS producer work continues |
| MG1: infrared estimate | Uniform exponential reflected-correlation decay for a dense observable family, or an equivalent physical transfer-operator gap | Not constructed |
| MG2: source transport | Exact fine-to-coarse observable maps with quantitatively decaying tails, all products, normalizers and failed returns retained | Open; source-local construction covers only its stated sectors |
| MG3: cutoff/volume passage | Uniform physical rate, prefactors and onset time on the same trajectory, with the fixed-t limit justified | Open |
| MG4: non-trivial excited sector | A surviving non-vacuum observable state in the reconstructed theory | Open; the existing non-freeness and lower-matching inputs remain necessary |
| MG5: final theorem scope | Correct local Yang–Mills identification; exact gauge-group and observable quantifiers | Open; no whole-theorem certification |

Two concrete mechanism families merit investigation. An exact continuation
of the effective action to a fixed physical coarse scale might reach a
provable strong-coupling cluster regime; this needs a quantitative crossover
theorem, not extrapolation of the weak-coupling beta function. Alternatively,
a direct gauge-invariant transfer-operator estimate might yield a lower
bound uniform under cutoff and volume removal; a finite-dimensional
positivity argument alone cannot do this. These are proposed routes,
not assumptions that the missing inequalities hold.

## 4. Explicit scope controls

An auxiliary massive block does not imply MG1. For μ>0 the quadratic
two-field matrix

    [[k^2+μ, -μ], [-μ, μ]]

has a b-block gap μ, but its Schur complement after eliminating b is
exactly k^2. Its remaining field is massless. This directly distinguishes
the current fixed-depth/internal/coercivity gaps from the requested gap.

Likewise, a sequence of positive cutoff masses m_a→0 proves no positive
limiting threshold. Finally, on CΩ ⊕ Cv ⊕ L^2((0,1)), take H to be zero
on Ω, one on v, and multiplication by x on L^2((0,1)). The correlation
of v is exp(-t), yet the full excited spectrum reaches zero. This shows
why a single gapped observable cannot replace a dense-family argument.

No auxiliary gap, one-loop coefficient, finite determinant check or
conditional use of MG1 will be counted as full-proof completion. The
actual infrared producer and the complete existence inputs must both be
proved and independently checked.
