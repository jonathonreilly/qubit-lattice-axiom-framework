# Frozen-source comparison of the quantum-metric witness

**Result:** no actionable mathematical or implementation defect was found
in the specified frozen author packet. Its finite witness agrees exactly
with the independently sealed calculation. This is source-bound scientific
scrutiny, not a publication, retention, or formal audit determination.

The author note was read completely (220 lines, 10,751 bytes), as were its
checker (170 lines, 7,815 bytes), complete result JSON, and author seal. These
reads occurred after the independent pre-comparison seal
`72116be479051ed6e637d4a3b3c466c5f2016559a0c9cf0ae44e986a2e13d4b8`.
All three source and twelve artifact rows of that earlier seal remain
unchanged. `REPORT.md`, `DERIVATION.md`, the independent runner and their
original outputs are preserved without editing.

## Argument and scope checked

1. **The target is an actual joint-law intertwiner.** The note asks for
   `Lambda_t E(mu)=E(mu P_t)` for every joint classical law and defines E
   using tensor products of the fixed sixteen-dimensional rho_a. It does
   not replace the evolved joint law with a product of its marginals. The
   supplied positive product perturbation is included in this domain. The
   test also applies if exactness is required only on the stationary product
   and all these small product perturbations. No claim that a local classical
   transition separately needs a CP lift is used.

2. **The reference really is stationary and full rank.** Each route is a
   permutation of black anchors, and its drive sums to zero by index shifts
   around its cycles. The reverse-minus-forward-rate sign is correct. A
   homogeneous product is invariant under each endpoint exchange, which
   proves the stationary master equation. The state construction is strictly
   positive, so its average tau and the finite product Sigma are full rank.
   Count-sector reducibility is harmless here. At N=2048 all context sites
   are distinct. The rate lower bound 1/20 is correct.

3. **The contraction proof does not import an unverified theorem.** Applying
   a two-positive trace-preserving map to the displayed positive two-by-two
   operator block and taking a Schur complement gives exactly the required
   quantum-metric contraction. This holds for arbitrary global CPTP maps
   fixing Sigma; a Lindblad decomposition, detailed balance and a quantum
   semigroup are unnecessary. The assumed differentiable family is more
   than the small-time contradiction needs: the finite classical output and
   its metric are analytic regardless of how candidate maps are selected.

4. **Generated correlations are accounted for.** Sigma^-1 Delta is a sum
   of one-factor operators. Thus the first metric derivative pairs the full
   tangent derivative only with its one-factor marginals. This is an exact
   tensor identity, not a later-time product closure. The factor 2, real
   part, partial traces and division by K=N^3/2 agree with the independent
   derivation. There are N^2/2 black anchors per first-coordinate plane.

5. **The microscopic and Fourier conventions agree.** The rate is
   k0/2+h/4. The -e1 route has first-coordinate displacement -2, and the
   four transverse routes have displacement -1; their drive matrices cancel
   in opposite-direction pairs. The full current linearization, signs of
   the skew stencil, factors 1 and 4, and the triangle shift x-N/4 all match
   the independent direct four-context enumeration. In Fourier convention
   exp(ikx), the two-field symbol is
   `-d I-i g [[0,1],[4,0]]`, with the d and g stated in the author note.

6. **The positive witness is admissible and finite.** For |epsilon|<1/7 the
   initial classical probabilities are strictly positive. The exact local
   metric entries u, v and zero mixed entry agree. The derivative per pair
   in microscopic time is

       253943551350785258709380168798915548993408646371
       /3288323073641053210935625659843220349235316654080000
       = +0.0000772258521026651502170470997... .

   Thus the contraction contradiction is present at finite N, without a
   hydrodynamic theorem or smoothness assumption on the triangle. The
   independent calculation did not build the enormous global matrix.

7. **The longer-wavelength observation is necessary only.** For the stated
   diagonal metric M=diag(u,v), the Hermitian metric derivative matrix has
   determinant

       4 d^2 u v-g^2(u-4v)^2.

   At fixed gamma=1, d=O(k^2) and g=k/7+O(k^3). With fixed positive u,v and
   u!=4v this determinant is negative at sufficiently small nonzero k, so a
   positive direction exists. Consequently exact contraction for the same
   encoding on arbitrarily large even tori requires u=4v in this sector.
   The statement is correctly restricted to a necessary condition; it is
   not a sufficient CP-extension criterion. The orthogonal-label classical
   metric (7,7/4) passes this necessary test.

8. **Placement and negative-claim limits are explicit.** The note grants
   an abstract sixteen-dimensional factor per classical pair; it does not
   supply a map placing four physical qubits on distinct microscopic sites.
   Its obstruction already permits global quantum operations on those
   abstract factors. It does not invalidate encoding injectivity, prohibit
   other codes or correlated preparations, or derive a general framework or
   physical no-go. The source explicitly keeps publication gates and formal
   audit status separate. Those boundaries are consistent with the proof.

## Executable comparison and provenance

`compare_sources.py` authenticates the exact author sources, all five rows
of the author pre-comparison artifact seal, and all four prior input hashes.
The fourth prior input is the unchanged second-campaign encoding checker;
its previous verification is reused by identity. It is not an imported
third-campaign calculation in the blind derivation.

Using the independently derived triangle-sum formulas and independent local
metric, the comparison reconstructs every exact u/v coefficient and rational
derivative in all six reported profiles: both orientations at N=512, 1024
and 2048. All agree, and only the + orientation at N=2048 is positive. This
also verifies that the prose has not suppressed a contrary small-size result.
The author checker is source-inspected but was not reexecuted merely to
repeat its controls. Its 336 covariance checks are correctly implemented;
the construction and covariance were independently checked previously at
the unchanged encoding identity. The new blind checker additionally tests
the microscopic four-context current itself, which the author runner uses
through its stated exact linearization.

The author stdout is byte-identical to its result JSON and stderr is empty.
The author seal explicitly says the precise execution start time was not
recorded; this review authenticates those bytes and their agreement, not an
independently observed start time. Its recorded prior floating screen is
treated as disclosed witness selection, not preregistration or a proof input.
No other third-campaign work or screen was read.

The contextual Temme citation was not separately consulted or imported. The
elementary contraction proof suffices, so this review makes no independent
bibliographic verification claim about that paper's equation numbering.

## Preserved comparison-helper failure

The first comparison run failed at a SymPy structural matrix equality:
`I*g*(-u+4*v)` and `-I*g*(u-4*v)` were represented differently despite being
identical. The displayed difference expands entrywise to zero. The original
checker, full streams, receipt and diagnosis are preserved under
`failed_attempts/symbolic_matrix_equality/`; the first top-level streams are
also retained. The two symbolic polynomial comparisons were changed to
compare expanded differences with zero. No mathematical expected value or
author source changed. `COMPARISON_RUN_2.*` records the successful rerun.
This is distinct from the blind independent run, which passed on its first
execution.

## Frozen identities and unresolved work

- Author note: f8b7e30ac671f19c93e5c9456c1f4e892f221eaa7888435e7aec5155126455e7.
- Author checker: be629d6d9ef483bda8b246e19135b1cc5524bffc6075612ea36d0c53532749ce.
- Author result and stdout: 1a319d4d17b3ac9a18ce665e55087ea6aafb84d3baa0869529785e2a01b54da0.
- Author pre-comparison seal: a472ec115b47d6a923006820dff4f0b2cb1060838a6bf8e3aefe26c083fed4de.
- Complete source rows and arithmetic checks: `COMPARISON_RESULTS.json`.

No correction is requested for this frozen packet. The remaining construction,
alternative-resource, general no-go and publication questions listed in the
source are outside this bounded check. The final seal binds this comparison
and its failed/successful execution evidence while preserving the original
pre-comparison packet.
